# Recall@N results: acSen (med2mod)

522 queries per condition. Window W = int(Q × ratio), ratio 1.3 (acSen 1.300); step 1; no threshold; every window scored.

**How a query is scored.** Every window gets the matcher's score (lower = more similar). Each window counts as the segment it shares the most word positions with; a segment's score is its best window's score. The gold segment's rank is the number of distinct segments whose score is **≤** the gold's score, so the gold is placed after every segment it ties with (worst case). Recall@k = queries with rank ≤ k / all queries. MRR = mean of 1 / rank (0 when the gold is never ranked).

## Main results

| Condition | Recall@1 (95% CI) | Recall@3 (95% CI) | Recall@5 (95% CI) | MRR |
|---|---|---|---|---|
| levenshtein | 485 / 522 = 92.9% (90.4%–94.8%) | 503 / 522 = 96.4% (94.4%–97.7%) | 507 / 522 = 97.1% (95.3%–98.3%) | 0.950 |

## Recall@5 by query length (words)

| Length | levenshtein |
|---|---:|
| 1–4 | 82 / 88 = 93.2% |
| 5–8 | 276 / 284 = 97.2% |
| 9–14 | 124 / 125 = 99.2% |
| 15+ | 25 / 25 = 100.0% |

## Ties and unreachable answers

| Condition | Queries whose gold ties with other segments | Ties that turn a Recall@5 hit into a miss | Ties that turn a Recall@1 hit into a miss | Recall@5 if gold were first among its ties | Gold never ranked |
|---|---:|---:|---:|---:|---:|
| levenshtein | 14 / 522 = 2.7% | 0 / 522 = 0.0% | 7 / 522 = 1.3% | 507 / 522 = 97.1% | 0 / 522 = 0.0% |

"Turns a hit into a miss": the gold would be within the top k if it were placed first among its ties, but is beyond k under the worst-case rule. The best-case column is an upper bound: the reported Recall@5 (worst case) and it bracket what any tie-breaking order could give. "Gold never ranked": no window counts as the gold segment (it is too short to be the majority of any window).

## The raw top-5 list (what the package returns), levenshtein

Overlapping windows mean the package's own top 5 often repeats one place.

| Distinct segments among the raw top-5 windows | Queries |
|---:|---:|
| 1 | 296 / 522 = 56.7% |
| 2 | 154 / 522 = 29.5% |
| 3 | 46 / 522 = 8.8% |
| 4 | 20 / 522 = 3.8% |
| 5 | 6 / 522 = 1.1% |

Gold segment among the raw top-5 windows: 507 / 522 = 97.1% (compare Recall@5 over distinct segments above).

## Run

- git commit `42ee1a8`, 4.1 s
- 5 queries checked: the full ranked window list equals `pipeline.moving_window(..., pruning="none")`
- index hashes: {'vocab.json': '5c98366fa98e5faf', 'docs.json': '3ff6fa9ca988ab2a', 'lengths.npy': 'eb7e9b8a64cc77b4'}
