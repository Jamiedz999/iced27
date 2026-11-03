# Example: found at rank 1

Work `AidedCheltC`, segment `AidedCheltC_0_1_1`, shown condition **levenshtein**.

## Inputs

- Query (medieval, original): Cid diatá Aided Cheltchair maic Uthechair?
- Query words (lowercase `\w+`), Q = 6: `cid diatá aided cheltchair maic uthechair`
- Gold answer (modern, original): Cid de atá Oidhe Chealtchair mhic Uitheachair?
- Gold words: positions 0–6 of 1073: `cid de atá oidhe chealtchair mhic uitheachair`
- Window: W = int(Q × ratio) = int(6 × 1.051) = 6; 1068 windows scored

## Result: gold segment rank 1 (worst case)

### Best window of the gold segment: window 1–6

Distance matrix D for this window (rows: query words, columns: window words; 0 = identical, 1 = nothing in common). **Bold** cells are the pairs the greedy step picks.

| query \ window | de (1) | atá (2) | oidhe (3) | chealtchair (4) | mhic (5) | uitheachair (6) |
|---|---:|---:|---:|---:|---:|---:|
| cid | 1.00 | 1.00 | **0.60** | 0.82 | 0.75 | 0.82 |
| diatá | 0.80 | **0.40** | 0.80 | 0.82 | 1.00 | 0.82 |
| aided | **0.60** | 0.80 | 0.60 | 0.91 | 1.00 | 0.82 |
| cheltchair | 0.90 | 0.90 | 0.90 | **0.09** | 0.80 | 0.45 |
| maic | 1.00 | 0.75 | 1.00 | 0.82 | **0.25** | 0.82 |
| uthechair | 0.89 | 0.89 | 0.89 | 0.45 | 0.78 | **0.18** |

Greedy pairing (repeatedly take the smallest remaining value, then strike out its row and column):

1. `cheltchair` ↔ `chealtchair` = 0.0909
2. `uthechair` ↔ `uitheachair` = 0.1818
3. `maic` ↔ `mhic` = 0.2500
4. `diatá` ↔ `atá` = 0.4000
5. `cid` ↔ `oidhe` = 0.6000
6. `aided` ↔ `de` = 0.6000

Score = sum / Q = 2.1227 / 6 = **0.3538** (the run recorded 0.3538 for this window).

## Top distinct segments, levenshtein

| Rank shown | Score | Segment | Best window (word positions) | Words in the window | Words of the window in this segment | Gold? |
|---:|---:|---|---|---|---:|:---:|
| 1 | 0.3538 | AidedCheltC_0_1_1 | 1–6 | de atá oidhe chealtchair mhic uitheachair | 6 / 6 | ✅ |
| 2 | 0.5066 | AidedCheltC_0_12_16 | 1067–1072 | chonganchnis agus chealtchair mhic uitheachair finit | 4 / 6 |  |
| 3 | 0.5925 | AidedCheltC_0_4_4 | 267–272 | tigeadh cealtchar dá thír ar ulaidh | 6 / 6 |  |
| 4 | 0.5957 | AidedCheltC_0_9_5 | 483–488 | niamh iníon chealtchair agus proinn céid | 3 / 6 |  |
| 5 | 0.5972 | AidedCheltC_0_9_17 | 567–572 | dtorchair leis agus bhain cealtchar a | 4 / 6 |  |

## Same query, exact: gold segment rank 5 (worst case, tied with 4 other segment(s))

| Rank shown | Score | Segment | Best window (word positions) | Words in the window | Words of the window in this segment | Gold? |
|---:|---:|---|---|---|---:|:---:|
| 1 | 0.8333 | AidedCheltC_0_1_1 | 0–5 | cid de atá oidhe chealtchair mhic | 6 / 6 | ✅ |
| 2 | 0.8333 | AidedCheltC_0_4_11 | 307–312 | dá ghairm go mbí theas cid | 5 / 6 |  |
| 3 | 0.8333 | AidedCheltC_0_5_1 | 310–315 | mbí theas cid a thug tú | 4 / 6 |  |
| 4 | 0.8333 | AidedCheltC_0_5_2 | 323–328 | dod thír ar an giolla cid | 5 / 6 |  |
| 5 | 0.8333 | AidedCheltC_0_5_3 | 326–331 | an giolla cid é an coimirce | 4 / 6 |  |

Ranks shown here list tied segments in text order; the recorded rank puts the gold after all of its ties.
