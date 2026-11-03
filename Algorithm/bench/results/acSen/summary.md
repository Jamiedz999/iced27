# Recall@N results: acSen (med2mod)

522 queries per condition. Window W = int(Q × ratio), ratio auto (acSen 1.033); step 1; no threshold; every window scored.

**How a query is scored.** Every window gets the matcher's score (lower = more similar). Each window counts as the segment it shares the most word positions with; a segment's score is its best window's score. The gold segment's rank is the number of distinct segments whose score is **≤** the gold's score, so the gold is placed after every segment it ties with (worst case). Recall@k = queries with rank ≤ k / all queries. MRR = mean of 1 / rank (0 when the gold is never ranked).

## Main results

| Condition | Recall@1 (95% CI) | Recall@3 (95% CI) | Recall@5 (95% CI) | MRR |
|---|---|---|---|---|
| levenshtein | 490 / 522 = 93.9% (91.5%–95.6%) | 504 / 522 = 96.6% (94.6%–97.8%) | 512 / 522 = 98.1% (96.5%–99.0%) | 0.957 |
| exact | 210 / 522 = 40.2% (36.1%–44.5%) | 275 / 522 = 52.7% (48.4%–56.9%) | 299 / 522 = 57.3% (53.0%–61.5%) | 0.485 |

## Paired comparison: levenshtein vs exact (exact McNemar test)

| k | both hit | only levenshtein | only exact | neither | p |
|---|---:|---:|---:|---:|---:|
| 1 | 210 | 280 | 0 | 32 | 1e-84 |
| 5 | 299 | 213 | 0 | 10 | 1.5e-64 |

## Recall@5 by query length (words)

| Length | levenshtein | exact |
|---|---:|---:|
| 1–4 | 84 / 88 = 95.5% | 32 / 88 = 36.4% |
| 5–8 | 278 / 284 = 97.9% | 151 / 284 = 53.2% |
| 9–14 | 125 / 125 = 100.0% | 94 / 125 = 75.2% |
| 15+ | 25 / 25 = 100.0% | 22 / 25 = 88.0% |

## Ties and unreachable answers

| Condition | Queries whose gold ties with other segments | Ties that turn a Recall@5 hit into a miss | Ties that turn a Recall@1 hit into a miss | Recall@1 / @5 with ties in random order (expected) | Recall@5 if gold were first among its ties | Gold never ranked |
|---|---:|---:|---:|---:|---:|---:|
| levenshtein | 8 / 522 = 1.5% | 0 / 522 = 0.0% | 5 / 522 = 1.0% | 94.3% / 98.1% | 512 / 522 = 98.1% | 0 / 522 = 0.0% |
| exact | 312 / 522 = 59.8% | 178 / 522 = 34.1% | 235 / 522 = 45.0% | 48.2% / 64.1% | 477 / 522 = 91.4% | 0 / 522 = 0.0% |

"Turns a hit into a miss": the gold would be within the top k if it were placed first among its ties, but is beyond k under the worst-case rule. The expected column orders each query's ties at random: the gold is equally likely to take any position among them. The best-case column is an upper bound (an oracle that always puts the gold first); with the worst case it brackets every tie-breaking order. "Gold never ranked": no window counts as the gold segment (it is too short to be the majority of any window).

## The raw top-5 list (what the package returns), levenshtein

Overlapping windows mean the package's own top 5 often repeats one place.

| Distinct segments among the raw top-5 windows | Queries |
|---:|---:|
| 1 | 257 / 522 = 49.2% |
| 2 | 148 / 522 = 28.4% |
| 3 | 75 / 522 = 14.4% |
| 4 | 31 / 522 = 5.9% |
| 5 | 11 / 522 = 2.1% |

Gold segment among the raw top-5 windows: 508 / 522 = 97.3% (compare Recall@5 over distinct segments above).

## Run

- git commit `42ee1a8`, 8.8 s
- 20 queries checked: the full ranked window list equals `pipeline.moving_window(..., pruning="none")`
- index hashes: {'vocab.json': '5c98366fa98e5faf', 'docs.json': '3ff6fa9ca988ab2a', 'lengths.npy': 'eb7e9b8a64cc77b4'}
