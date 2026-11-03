# Recall@N results: all (med2mod)

16791 queries per condition. Window W = int(Q × ratio), ratio auto (AidedCheltC 1.051, abbot 1.118, acSen 1.033, …); step 1; no threshold; every window scored.

**How a query is scored.** Every window gets the matcher's score (lower = more similar). Each window counts as the segment it shares the most word positions with; a segment's score is its best window's score. The gold segment's rank is the number of distinct segments whose score is **≤** the gold's score, so the gold is placed after every segment it ties with (worst case). Recall@k = queries with rank ≤ k / all queries. MRR = mean of 1 / rank (0 when the gold is never ranked).

## Main results

| Condition | Recall@1 (95% CI) | Recall@3 (95% CI) | Recall@5 (95% CI) | MRR |
|---|---|---|---|---|
| levenshtein | 7915 / 16791 = 47.1% (46.4%–47.9%) | 9904 / 16791 = 59.0% (58.2%–59.7%) | 10682 / 16791 = 63.6% (62.9%–64.3%) | 0.550 |
| exact | 2094 / 16791 = 12.5% (12.0%–13.0%) | 3328 / 16791 = 19.8% (19.2%–20.4%) | 3868 / 16791 = 23.0% (22.4%–23.7%) | 0.180 |

## Paired comparison: levenshtein vs exact (exact McNemar test)

| k | both hit | only levenshtein | only exact | neither | p |
|---|---:|---:|---:|---:|---:|
| 1 | 2064 | 5851 | 30 | 8846 | 0 |
| 5 | 3831 | 6851 | 37 | 6072 | 0 |

## Recall@5 by query length (words)

| Length | levenshtein | exact |
|---|---:|---:|
| 1–4 | 1939 / 3637 = 53.3% | 542 / 3637 = 14.9% |
| 5–8 | 5594 / 8728 = 64.1% | 1985 / 8728 = 22.7% |
| 9–14 | 2907 / 4075 = 71.3% | 1232 / 4075 = 30.2% |
| 15+ | 242 / 351 = 68.9% | 109 / 351 = 31.1% |

## Ties and unreachable answers

| Condition | Queries whose gold ties with other segments | Ties that turn a Recall@5 hit into a miss | Ties that turn a Recall@1 hit into a miss | Recall@1 / @5 with ties in random order (expected) | Recall@5 if gold were first among its ties | Gold never ranked |
|---|---:|---:|---:|---:|---:|---:|
| levenshtein | 3419 / 16791 = 20.4% | 127 / 16791 = 0.8% | 438 / 16791 = 2.6% | 48.3% / 64.0% | 10809 / 16791 = 64.4% | 19 / 16791 = 0.1% |
| exact | 14666 / 16791 = 87.3% | 8015 / 16791 = 47.7% | 7839 / 16791 = 46.7% | 17.6% / 29.7% | 11883 / 16791 = 70.8% | 19 / 16791 = 0.1% |

"Turns a hit into a miss": the gold would be within the top k if it were placed first among its ties, but is beyond k under the worst-case rule. The expected column orders each query's ties at random: the gold is equally likely to take any position among them. The best-case column is an upper bound (an oracle that always puts the gold first); with the worst case it brackets every tie-breaking order. "Gold never ranked": no window counts as the gold segment (it is too short to be the majority of any window).

## The raw top-5 list (what the package returns), levenshtein

Overlapping windows mean the package's own top 5 often repeats one place.

| Distinct segments among the raw top-5 windows | Queries |
|---:|---:|
| 1 | 3092 / 16791 = 18.4% |
| 2 | 3842 / 16791 = 22.9% |
| 3 | 4288 / 16791 = 25.5% |
| 4 | 3659 / 16791 = 21.8% |
| 5 | 1910 / 16791 = 11.4% |

Gold segment among the raw top-5 windows: 10147 / 16791 = 60.4% (compare Recall@5 over distinct segments above).

## Per work

| Work | Queries | levenshtein R@1 | levenshtein R@5 | exact R@1 | exact R@5 |
|---|---:|---:|---:|---:|---:|
| AidedCheltC | 133 | 0.91 | 0.98 | 0.33 | 0.55 |
| abbot | 94 | 0.65 | 0.82 | 0.14 | 0.32 |
| acSen | 522 | 0.94 | 0.98 | 0.40 | 0.57 |
| aidedBres | 43 | 0.65 | 0.86 | 0.14 | 0.33 |
| aidedCheitM | 101 | 0.89 | 0.98 | 0.36 | 0.63 |
| aidedChel | 133 | 0.91 | 0.98 | 0.33 | 0.55 |
| aidedChonch | 128 | 0.48 | 0.74 | 0.05 | 0.24 |
| aidedConr | 323 | 0.21 | 0.37 | 0.03 | 0.08 |
| aidedDiar | 545 | 0.52 | 0.68 | 0.11 | 0.21 |
| aidedFerg | 54 | 0.94 | 1.00 | 0.39 | 0.65 |
| aidedLoeg | 29 | 0.93 | 0.93 | 0.38 | 0.59 |
| aidedMael | 104 | 0.47 | 0.70 | 0.05 | 0.18 |
| aidedOenfir | 189 | 0.69 | 0.84 | 0.15 | 0.33 |
| aislOeng | 207 | 0.38 | 0.60 | 0.05 | 0.10 |
| baileBinn | 109 | 0.50 | 0.75 | 0.11 | 0.28 |
| boroma | 844 | 0.67 | 0.83 | 0.12 | 0.23 |
| cathAlma | 330 | 0.51 | 0.69 | 0.08 | 0.24 |
| cathCairnn | 216 | 0.45 | 0.66 | 0.06 | 0.16 |
| cathMaige | 638 | 0.37 | 0.54 | 0.05 | 0.12 |
| ceartCla | 113 | 0.45 | 0.64 | 0.09 | 0.19 |
| compertMon | 603 | 0.61 | 0.76 | 0.16 | 0.36 |
| comracLiad | 185 | 0.85 | 0.95 | 0.24 | 0.44 |
| echtraCho | 111 | 0.28 | 0.46 | 0.04 | 0.13 |
| echtraCorm | 217 | 0.41 | 0.67 | 0.06 | 0.18 |
| echtraFer | 156 | 0.38 | 0.58 | 0.04 | 0.13 |
| echtraMac | 291 | 0.53 | 0.72 | 0.07 | 0.19 |
| esnadaTige | 126 | 0.40 | 0.68 | 0.06 | 0.17 |
| feisTighe | 106 | 0.92 | 0.98 | 0.58 | 0.84 |
| fingalRon | 333 | 0.29 | 0.49 | 0.05 | 0.14 |
| forbDroma | 2295 | 0.20 | 0.32 | 0.03 | 0.07 |
| genChor | 259 | 0.41 | 0.62 | 0.09 | 0.16 |
| immBrain | 318 | 0.47 | 0.67 | 0.09 | 0.22 |
| longesMac | 399 | 0.45 | 0.65 | 0.05 | 0.12 |
| mescaUlad | 1097 | 0.34 | 0.51 | 0.02 | 0.08 |
| noínUlad | 71 | 0.48 | 0.79 | 0.07 | 0.30 |
| oenachInd | 216 | 0.62 | 0.80 | 0.12 | 0.26 |
| oidheChlo | 873 | 0.88 | 0.97 | 0.66 | 0.82 |
| orgTri | 99 | 0.53 | 0.72 | 0.11 | 0.27 |
| scelaCano | 594 | 0.39 | 0.56 | 0.07 | 0.14 |
| scelaCol | 78 | 0.59 | 0.78 | 0.23 | 0.42 |
| scelaGu | 129 | 0.44 | 0.68 | 0.05 | 0.12 |
| scelaGua | 34 | 0.56 | 0.79 | 0.21 | 0.41 |
| scelaMon | 96 | 0.32 | 0.61 | 0.07 | 0.24 |
| scelaMuc | 374 | 0.36 | 0.50 | 0.05 | 0.13 |
| tainBo | 902 | 0.42 | 0.69 | 0.05 | 0.13 |
| tochEm | 565 | 0.33 | 0.49 | 0.05 | 0.12 |
| tochmEm | 209 | 0.35 | 0.60 | 0.05 | 0.15 |
| tochmEt | 999 | 0.41 | 0.57 | 0.04 | 0.13 |
| toruig | 201 | 0.79 | 0.93 | 0.55 | 0.76 |

## Run

- git commit `42ee1a8`, 210.9 s
- 245 queries checked: the full ranked window list equals `pipeline.moving_window(..., pruning="none")`
- index hashes: {'vocab.json': '5c98366fa98e5faf', 'docs.json': '3ff6fa9ca988ab2a', 'lengths.npy': 'eb7e9b8a64cc77b4'}
