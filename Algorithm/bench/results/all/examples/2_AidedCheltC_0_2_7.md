# Example: found at rank 2-5

Work `AidedCheltC`, segment `AidedCheltC_0_2_7`, shown condition **levenshtein**.

## Inputs

- Query (medieval, original): ocus clannaid Celtchar in gái trit
- Query words (lowercase `\w+`), Q = 6: `ocus clannaid celtchar in gái trit`
- Gold answer (modern, original): agus clanann Cealtchar ga tríd
- Gold words: positions 166–170 of 1073: `agus clanann cealtchar ga tríd`
- Window: W = int(Q × ratio) = int(6 × 1.051) = 6; 1068 windows scored

## Result: gold segment rank 2 (worst case)

### Best window of the gold segment: window 165–170

Distance matrix D for this window (rows: query words, columns: window words; 0 = identical, 1 = nothing in common). **Bold** cells are the pairs the greedy step picks.

| query \ window | eatarthu (165) | agus (166) | clanann (167) | cealtchar (168) | ga (169) | tríd (170) |
|---|---:|---:|---:|---:|---:|---:|
| ocus | 1.00 | **0.50** | 1.00 | 0.89 | 1.00 | 1.00 |
| clannaid | 1.00 | 0.88 | **0.38** | 0.78 | 0.88 | 0.88 |
| celtchar | 0.88 | 1.00 | 0.75 | **0.11** | 0.88 | 0.88 |
| in | **1.00** | 1.00 | 0.86 | 1.00 | 1.00 | 1.00 |
| gái | 1.00 | 0.75 | 1.00 | 1.00 | **0.67** | 1.00 |
| trit | 0.75 | 1.00 | 1.00 | 0.89 | 1.00 | **0.50** |

Greedy pairing (repeatedly take the smallest remaining value, then strike out its row and column):

1. `celtchar` ↔ `cealtchar` = 0.1111
2. `clannaid` ↔ `clanann` = 0.3750
3. `ocus` ↔ `agus` = 0.5000
4. `trit` ↔ `tríd` = 0.5000
5. `gái` ↔ `ga` = 0.6667
6. `in` ↔ `eatarthu` = 1.0000

Score = sum / Q = 3.1528 / 6 = **0.5255** (the run recorded 0.5255 for this window).

### Best window overall (segment AidedCheltC_0_2_6): window 163–168

Distance matrix D for this window (rows: query words, columns: window words; 0 = identical, 1 = nothing in common). **Bold** cells are the pairs the greedy step picks.

| query \ window | an (163) | fhichill (164) | eatarthu (165) | agus (166) | clanann (167) | cealtchar (168) |
|---|---:|---:|---:|---:|---:|---:|
| ocus | 1.00 | 0.88 | 1.00 | **0.50** | 1.00 | 0.89 |
| clannaid | 0.75 | 1.00 | 1.00 | 0.88 | **0.38** | 0.78 |
| celtchar | 0.88 | 0.88 | 0.88 | 1.00 | 0.75 | **0.11** |
| in | **0.50** | 0.88 | 1.00 | 1.00 | 0.86 | 1.00 |
| gái | 1.00 | **0.88** | 1.00 | 0.75 | 1.00 | 1.00 |
| trit | 1.00 | 0.88 | **0.75** | 1.00 | 1.00 | 0.89 |

Greedy pairing (repeatedly take the smallest remaining value, then strike out its row and column):

1. `celtchar` ↔ `cealtchar` = 0.1111
2. `clannaid` ↔ `clanann` = 0.3750
3. `ocus` ↔ `agus` = 0.5000
4. `in` ↔ `an` = 0.5000
5. `trit` ↔ `eatarthu` = 0.7500
6. `gái` ↔ `fhichill` = 0.8750

Score = sum / Q = 3.1111 / 6 = **0.5185** (the run recorded 0.5185 for this window).

## Top distinct segments, levenshtein

| Rank shown | Score | Segment | Best window (word positions) | Words in the window | Words of the window in this segment | Gold? |
|---:|---:|---|---|---|---:|:---:|
| 1 | 0.5185 | AidedCheltC_0_2_6 | 163–168 | an fhichill eatarthu agus clanann cealtchar | 3 / 6 |  |
| 2 | 0.5255 | AidedCheltC_0_2_7 | 165–170 | eatarthu agus clanann cealtchar ga tríd | 5 / 6 | ✅ |
| 3 | 0.5352 | AidedCheltC_0_10_19 | 768–773 | isan leith anall agus beireann cealtchar | 3 / 6 |  |
| 4 | 0.5503 | AidedCheltC_0_9_3 | 463–468 | cealtchar agus chuaigh dá agallaimh an | 5 / 6 |  |
| 5 | 0.5505 | AidedCheltC_0_10_9 | 664–669 | agus téann cealtchar i bhfiodhbha go | 6 / 6 |  |

## Same query, exact: gold segment rank 132 (worst case, tied with 128 other segment(s))

| Rank shown | Score | Segment | Best window (word positions) | Words in the window | Words of the window in this segment | Gold? |
|---:|---:|---|---|---|---:|:---:|
| 1 | 0.8333 | AidedCheltC_0_9_13 | 543–548 | chuige agus do rónadh amhlaigh ocus | 4 / 6 |  |
| 2 | 0.8333 | AidedCheltC_0_9_14 | 546–551 | rónadh amhlaigh ocus do chuas ar | 4 / 6 |  |
| 3 | 0.8333 | AidedCheltC_0_11_6 | 832–837 | dhubh rugadh an chú mhínbhreac in | 5 / 6 |  |
| 4 | 1.0000 | AidedCheltC_0_1_1 | 0–5 | cid de atá oidhe chealtchair mhic | 6 / 6 |  |
| 5 | 1.0000 | AidedCheltC_0_1_2 | 5–10 | mhic uitheachair ní hansa fear amhra | 2 / 6 |  |

Ranks shown here list tied segments in text order; the recorded rank puts the gold after all of its ties.
