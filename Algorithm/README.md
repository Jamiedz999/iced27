# fuzzy-search-algorithm

The moving-window fuzzy passage matcher from
[uCeltic](https://github.com/uCeltic/uCeltic), extracted as a standalone,
dependency-light Python package so the algorithm can be optimised on its own —
no Django, no database, no HTTP, no TEI parsing.

## What the algorithm does

Given a query of `Q` words and a document of `N` words, it slides a window of
`W` words over the document and scores how closely each window matches the
query. It is built for medieval Irish manuscript witnesses, where the same
passage varies in spelling and in which words are present, so it tolerates both
**spelling variation** (fuzzy word comparison) and **inserted or omitted
words** (a window longer than the query, and an order-free pairing).

A **score** is a *dissimilarity* in `[0, 1]`: `0` is identical, `1` is nothing
in common. Callers turn it into a match percentage with `(1 − score) × 100`.

### The three stages

1. **Distance matrix.** `D[k][j]` = normalized Levenshtein distance between
   query word `k` and document word `j`, for all `Q × N` pairs. Repeated
   document words are computed once per query word and cached.
2. **Per-row window minima.** For each query word, a monotonic deque gives
   `row_min[k][i] = min(D[k][i .. i+W-1])` for every window start `i` in `O(N)`.
3. **Lower-bound prefilter, then greedy scoring.**
   `LB(i) = (Σ_k row_min[k][i]) / Q` is a lower bound on window `i`'s true
   score, so only windows with `LB(i) ≤ threshold` need the expensive step:
   `calculate_dissimilarity_score`, a greedy assignment that repeatedly takes
   the smallest remaining distance and strikes out its row and column, pairing
   each query word with a distinct document word. That pairing is what makes
   the match order-free.

`W = max(1, int(Q × window_size_ratio))`, default ratio `1.3` — the 30 %
headroom is what lets a match absorb inserted words.

## Layout

| Path | What it is |
| --- | --- |
| `fuzzysearch/common.py` | Shared definitions (tokenizing, window size, greedy scorer) and the snippet/anchor layer |
| `fuzzysearch/optimized.py` | Optimised pipeline: `run_search` + `moving_window_similarity1`. **The thing being optimised.** |
| `fuzzysearch/naive.py` | Naive pipeline: `run_search` + `full_scan` — the oracle. Never optimise this |
| `fuzzysearch/vocab.py` | Word IDs and the precomputed V×V Levenshtein table over `corpus/` (Medieval + Modern Irish, one vocabulary, lowercased) |
| `fuzzysearch/pipeline.py` | One case-insensitive matcher whose stages (distance source, window pruning) are chosen by name — for ablation |
| `fuzzysearch/configs.py` | The ablation configurations: name → stage options. Add a row per new optimisation |
| `corpus/` | acSen-style JSON texts, one per work |
| `tests/` | Regression, prefilter, differential and search-layer tests |
| `bench/bench_search.py` | Ablation benchmark: every configuration vs the naive scan, on a corpus text |
| `bench/eval_*.py` | Retrieval-effectiveness (Recall@N) experiment: dataset checks, run, summary, review traces; see below |

`run_search` takes a document's `word_array` and `anchors` directly instead of
loading a row through the Django ORM; everything else is behaviour-for-
behaviour identical to the original.

```python
from fuzzysearch import run_search

doc = [{"w": "ro", "sep": " "}, {"w": "gab", "sep": " "}, {"w": "in", "sep": " "},
       {"w": "talam", "sep": ""}, {"w": "trochull", "sep": ""}]

run_search(doc, "ro gab in", window_size_ratio=1.3, dissimilarity_threshold=0.5)
# [{'score': 0.0, 'snippet': 'ro gab in', 'word_start': 0, 'word_end': 3, ...}]
```

## Running it

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

.venv/bin/python -m fuzzysearch.vocab corpus index   # build the V×V table (~8 s, ~1.2 GB, not committed)
.venv/bin/python -m unittest discover -s tests      # tests; every configuration is checked against naive
.venv/bin/python bench/bench_search.py              # ablation benchmark (needs the index)
.venv/bin/python bench/bench_search.py --doc acSen --queries 8,16,32 --repeat 3
```

## Retrieval effectiveness (Recall@N)

Each aligned segment of one variety is a query, searched in the full text of
the other variety of the same work (one continuous word sequence, so windows
cross segment boundaries). Every window is scored (step 1, no threshold, no
pruning); windows are grouped into the segment they overlap most, and the
gold segment's rank is worst-case (placed after every tie). Two conditions:
`levenshtein` (the matcher) and `exact` (identical words only).

```bash
.venv/bin/python bench/eval_dataset.py --works acSen --out bench/results/acSen  # checks + statistics
.venv/bin/python bench/eval_recall.py  --works acSen --out bench/results/acSen  # per_query.csv, run.json
.venv/bin/python bench/eval_summary.py bench/results/acSen                      # summary.md
.venv/bin/python bench/eval_report.py  bench/results/acSen                      # examples/, samples.md, misses.md
```

`--works all` runs every distinct work; `--ratio 1.3` fixes the window ratio
(default: each work's whole-text length ratio); `--direction med2med` is the
self-search sanity check. Read a run in this order: `dataset.md`,
`examples/`, `samples.md` and `misses.md`, then `summary.md`.

## Baseline

Extraction baseline — 8000-word corpus, `step=1`, `threshold=0.5`, seed 42,
Python 3.9.6 / rapidfuzz 3.13, single run:

| Q | W | reference (naive) | current | speedup |
| --- | --- | --- | --- | --- |
| 8 | 10 | 405.9 ms | 34.5 ms | 11.8× |
| 16 | 20 | 1993.8 ms | 73.3 ms | 27.2× |

Where the current 73 ms at `Q=16` goes (cProfile, `tottime`):

- **~55 %** in `rapidfuzz` — 127 536 individual `normalized_distance` calls,
  and roughly half of *that* is per-call Python↔C marshalling overhead
  (`setupPandas`, `preprocess_strings`, `conv_sequence`), not edit distance.
- **~36 %** in the pure-Python body of `moving_window_similarity1` — the matrix
  build loop, the deque pass and the lower-bound loop.
- **~3 %** in `calculate_dissimilarity_score`; the prefilter means it runs on
  only 26 of 7981 windows.

So the cost is dominated by *per-call overhead and interpreter loops*, not by
the greedy scorer. Directions worth trying: batch the whole matrix through
`rapidfuzz.process.cdist` instead of a Python loop; deduplicate on the
document's unique vocabulary once rather than per query word; move `row_min`
and the lower bound into NumPy.

## Guardrails for optimisation work

The tests are the contract. Any change to `optimized.py` must keep them green:

- `test_similarity_regression.py` — fixed inputs, locked scores.
- `test_equivalence.py` — randomised differential test against
  `fuzzysearch/naive.py`. Unpruned output must match the naive scan
  *exactly*; pruning must never drop a window the naive scan scores at or under
  the threshold; and the two `run_search` pipelines must return the same hits.
- `test_prefilter.py`, `test_search.py` — the pruning and snippet contracts.

Two behaviours are load-bearing and easy to break by accident:

- **Sorting and ties.** Results are `sorted()` on `(score, index)`, so equal
  scores come back in index order.
- **Empty separators.** A snippet joins `w + sep` with no fallback; an empty
  `sep` means the source has nothing between the two words (uCeltic #145).

## Known defects carried over

Pinned as `@unittest.expectedFailure` in `tests/test_known_defects.py`, so the
suite stays green and reports an unexpected success the moment one is fixed.

- **The prefilter is unsound when `W < Q`** (`window_size_ratio < 1.0`, i.e.
  Match Length under 100 %, which the API and the UI slider both allow). The
  greedy assignment pairs each query word with a *distinct* window word, so
  with fewer columns than rows it produces only `W` terms and still divides by
  `Q`. The bound sums all `Q` row minima, so it can exceed the true score and
  prune a genuine match.
- **The no-qualifying-window fallback returns the smallest *bound*, not the
  smallest score.** Not pinned as a defect: `run_search` filters on score and
  returns `[]` either way, so nothing user-facing depends on it — but an
  optimisation must not start *relying* on `results[0]` being the true best
  when nothing passes the threshold.

## Provenance

Extracted 2026-09-21 from `uCeltic@ac3f1c6`:

| Here | Upstream |
| --- | --- |
| `fuzzysearch/optimized.py`, `fuzzysearch/common.py` | `backend/apps/search/services/similarity.py` |
| `fuzzysearch/optimized.py`, `fuzzysearch/common.py` | `backend/apps/search/services/run_search.py` |
| `tests/test_similarity_regression.py` | `backend/apps/search/tests/test_similarity_regression.py` |
| `tests/test_prefilter.py` | `backend/apps/search/tests/test_prefilter.py` |
| `tests/test_search.py` | `backend/apps/search/tests/test_snippet.py` (de-Djangoed) |
| `bench/bench_search.py` | `backend/scripts/bench_search.py` |

Left behind deliberately: the DRF view and serializers, the TEI parser, the
`TEIDocument` model, and `test_search_api.py` / `test_openapi.py` — all
transport and storage, none of it algorithm.
