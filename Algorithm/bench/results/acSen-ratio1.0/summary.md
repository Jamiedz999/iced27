# Recall@N results: acSen (med2mod)

522 queries per condition. Window W = int(Q × ratio), ratio 1.0 (acSen 1.000); step 1; no threshold; every window scored.

**How a query is scored.** Every window gets the matcher's score (lower = more similar). Each window counts as the segment it shares the most word positions with; a segment's score is its best window's score. The gold segment's rank is the number of distinct segments whose score is **≤** the gold's score, so the gold is placed after every segment it ties with (worst case). Recall@k = queries with rank ≤ k / all queries. MRR = mean of 1 / rank (0 when the gold is never ranked).

## Main results

| Condition | Recall@1 (95% CI) | Recall@3 (95% CI) | Recall@5 (95% CI) | MRR |
|---|---|---|---|---|
| levenshtein | 490 / 522 = 93.9% (91.5%–95.6%) | 504 / 522 = 96.6% (94.6%–97.8%) | 512 / 522 = 98.1% (96.5%–99.0%) | 0.957 |

## Recall@5 by query length (words)

| Length | levenshtein |
|---|---:|
| 1–4 | 84 / 88 = 95.5% |
| 5–8 | 278 / 284 = 97.9% |
| 9–14 | 125 / 125 = 100.0% |
| 15+ | 25 / 25 = 100.0% |

## Ties and unreachable answers

| Condition | Queries whose gold ties with other segments | Ties that turn a Recall@5 hit into a miss | Ties that turn a Recall@1 hit into a miss | Recall@5 if gold were first among its ties | Gold never ranked |
|---|---:|---:|---:|---:|---:|
| levenshtein | 8 / 522 = 1.5% | 0 / 522 = 0.0% | 5 / 522 = 1.0% | 512 / 522 = 98.1% | 0 / 522 = 0.0% |

"Turns a hit into a miss": the gold would be within the top k if it were placed first among its ties, but is beyond k under the worst-case rule. The best-case column is an upper bound: the reported Recall@5 (worst case) and it bracket what any tie-breaking order could give. "Gold never ranked": no window counts as the gold segment (it is too short to be the majority of any window).

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

- git commit `42ee1a8`, 3.6 s
- 5 queries checked: the full ranked window list equals `pipeline.moving_window(..., pruning="none")`
- index hashes: {'vocab.json': '5c98366fa98e5faf', 'docs.json': '3ff6fa9ca988ab2a', 'lengths.npy': 'eb7e9b8a64cc77b4'}
