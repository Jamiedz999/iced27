# Example: found at rank 1

Work `acSen`, segment `acSen_1_1_2`, shown condition **levenshtein**.

## Inputs

- Query (medieval, original): ocus ar ndíthugud na Féindi,
- Query words (lowercase `\w+`), Q = 5: `ocus ar ndíthugud na féindi`
- Gold answer (modern, original): agus ar ndíothú na Féinne,
- Gold words: positions 10–14 of 4007: `agus ar ndíothú na féinne`
- Window: W = int(Q × ratio) = int(5 × 1.033) = 5; 4003 windows scored

## Result: gold segment rank 1 (worst case)

### Best window of the gold segment: window 10–14

Distance matrix D for this window (rows: query words, columns: window words; 0 = identical, 1 = nothing in common). **Bold** cells are the pairs the greedy step picks.

| query \ window | agus (10) | ar (11) | ndíothú (12) | na (13) | féinne (14) |
|---|---:|---:|---:|---:|---:|
| ocus | **0.50** | 1.00 | 0.86 | 1.00 | 1.00 |
| ar | 0.75 | **0.00** | 1.00 | 1.00 | 1.00 |
| ndíthugud | 0.78 | 1.00 | **0.56** | 0.89 | 1.00 |
| na | 1.00 | 1.00 | 0.86 | **0.00** | 0.83 |
| féindi | 1.00 | 1.00 | 1.00 | 0.83 | **0.33** |

Greedy pairing (repeatedly take the smallest remaining value, then strike out its row and column):

1. `ar` ↔ `ar` = 0.0000
2. `na` ↔ `na` = 0.0000
3. `féindi` ↔ `féinne` = 0.3333
4. `ocus` ↔ `agus` = 0.5000
5. `ndíthugud` ↔ `ndíothú` = 0.5556

Score = sum / Q = 1.3889 / 5 = **0.2778** (the run recorded 0.2778 for this window).

## Top distinct segments, levenshtein

| Rank shown | Score | Segment | Best window (word positions) | Words in the window | Words of the window in this segment | Gold? |
|---:|---:|---|---|---|---:|:---:|
| 1 | 0.2778 | acSen_1_1_2 | 10–14 | agus ar ndíothú na féinne | 5 / 5 | ✅ |
| 2 | 0.3889 | acSen_3_4_6 | 2351–2355 | othrasa na féinne agus mar | 3 / 5 |  |
| 3 | 0.4111 | acSen_3_4_7 | 2352–2356 | na féinne agus mar do | 3 / 5 |  |
| 4 | 0.4222 | acSen_3_4_8 | 2380–2384 | ar thrí cathaibh na féinne | 5 / 5 |  |
| 5 | 0.4667 | acSen_1_3_10 | 346–350 | ag iomrá na féinne agus | 5 / 5 |  |

## Same query, exact: gold segment rank 6 (worst case, tied with 5 other segment(s))

| Rank shown | Score | Segment | Best window (word positions) | Words in the window | Words of the window in this segment | Gold? |
|---:|---:|---|---|---|---:|:---:|
| 1 | 0.6000 | acSen_1_1_2 | 9–13 | ollarba agus ar ndíothú na | 4 / 5 | ✅ |
| 2 | 0.6000 | acSen_1_6_9 | 715–719 | chroitheadh uisce choiscricthe ar na | 5 / 5 |  |
| 3 | 0.6000 | acSen_2_1_11 | 1370–1374 | insíd na seanlaoich úd ar | 4 / 5 |  |
| 4 | 0.6000 | acSen_3_4_7 | 2358–2362 | an iníon ar mhnáibh na | 5 / 5 |  |
| 5 | 0.6000 | acSen_3_4_8 | 2379–2383 | ngaisce ar thrí cathaibh na | 5 / 5 |  |

Ranks shown here list tied segments in text order; the recorded rank puts the gold after all of its ties.
