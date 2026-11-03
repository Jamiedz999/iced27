# Example: a tie decides the outcome (exact match)

Work `AidedCheltC`, segment `AidedCheltC_0_1_9`, shown condition **exact**.

## Inputs

- Query (medieval, original): ben for dámrud dia thig
- Query words (lowercase `\w+`), Q = 5: `ben for dámrud dia thig`
- Gold answer (modern, original): bean ar dhamhra dá thigh
- Gold words: positions 41–45 of 1073: `bean ar dhamhra dá thigh`
- Window: W = int(Q × ratio) = int(5 × 1.051) = 5; 1069 windows scored

## Result: gold segment rank 132 (worst case, tied with 131 other segment(s))

### Best window of the gold segment: window 39–43

Distance matrix D for this window (rows: query words, columns: window words; 0 = identical, 1 = nothing in common). **Bold** cells are the pairs the greedy step picks.

| query \ window | dó (39) | áfach (40) | bean (41) | ar (42) | dhamhra (43) |
|---|---:|---:|---:|---:|---:|
| ben | **1.00** | 1.00 | 1.00 | 1.00 | 1.00 |
| for | 1.00 | **1.00** | 1.00 | 1.00 | 1.00 |
| dámrud | 1.00 | 1.00 | **1.00** | 1.00 | 1.00 |
| dia | 1.00 | 1.00 | 1.00 | **1.00** | 1.00 |
| thig | 1.00 | 1.00 | 1.00 | 1.00 | **1.00** |

Greedy pairing (repeatedly take the smallest remaining value, then strike out its row and column):

1. `ben` ↔ `dó` = 1.0000
2. `for` ↔ `áfach` = 1.0000
3. `dámrud` ↔ `bean` = 1.0000
4. `dia` ↔ `ar` = 1.0000
5. `thig` ↔ `dhamhra` = 1.0000

Score = sum / Q = 5.0000 / 5 = **1.0000** (the run recorded 1.0000 for this window).

### Best window overall (segment AidedCheltC_0_1_1): window 0–4

Distance matrix D for this window (rows: query words, columns: window words; 0 = identical, 1 = nothing in common). **Bold** cells are the pairs the greedy step picks.

| query \ window | cid (0) | de (1) | atá (2) | oidhe (3) | chealtchair (4) |
|---|---:|---:|---:|---:|---:|
| ben | **1.00** | 1.00 | 1.00 | 1.00 | 1.00 |
| for | 1.00 | **1.00** | 1.00 | 1.00 | 1.00 |
| dámrud | 1.00 | 1.00 | **1.00** | 1.00 | 1.00 |
| dia | 1.00 | 1.00 | 1.00 | **1.00** | 1.00 |
| thig | 1.00 | 1.00 | 1.00 | 1.00 | **1.00** |

Greedy pairing (repeatedly take the smallest remaining value, then strike out its row and column):

1. `ben` ↔ `cid` = 1.0000
2. `for` ↔ `de` = 1.0000
3. `dámrud` ↔ `atá` = 1.0000
4. `dia` ↔ `oidhe` = 1.0000
5. `thig` ↔ `chealtchair` = 1.0000

Score = sum / Q = 5.0000 / 5 = **1.0000** (the run recorded 1.0000 for this window).

## Top distinct segments, exact

| Rank shown | Score | Segment | Best window (word positions) | Words in the window | Words of the window in this segment | Gold? |
|---:|---:|---|---|---|---:|:---:|
| 1 | 1.0000 | AidedCheltC_0_1_1 | 0–4 | cid de atá oidhe chealtchair | 5 / 5 |  |
| 2 | 1.0000 | AidedCheltC_0_1_2 | 5–9 | mhic uitheachair ní hansa fear | 2 / 5 |  |
| 3 | 1.0000 | AidedCheltC_0_1_3 | 7–11 | ní hansa fear amhra do | 3 / 5 |  |
| 4 | 1.0000 | AidedCheltC_0_1_4 | 16–20 | blaoi brughaidh seacht n airgeda | 3 / 5 |  |
| 5 | 1.0000 | AidedCheltC_0_1_5 | 20–24 | airgeda leis seacht fichid bó | 3 / 5 |  |

## Same query, levenshtein: gold segment rank 1 (worst case)

| Rank shown | Score | Segment | Best window (word positions) | Words in the window | Words of the window in this segment | Gold? |
|---:|---:|---|---|---|---:|:---:|
| 1 | 0.4995 | AidedCheltC_0_1_9 | 41–45 | bean ar dhamhra dá thigh | 5 / 5 | ✅ |
| 2 | 0.5552 | AidedCheltC_0_1_12 | 61–65 | bean chealtchair dá thigh sean | 5 / 5 |  |
| 3 | 0.5857 | AidedCheltC_0_9_18 | 584–588 | fir thánaig ann agus is | 3 / 5 |  |
| 4 | 0.5900 | AidedCheltC_0_1_10 | 44–48 | dá thigh gan feis dó | 3 / 5 |  |
| 5 | 0.6310 | AidedCheltC_0_9_10 | 524–528 | lena hathair go ndearnta dhá | 5 / 5 |  |

Ranks shown here list tied segments in text order; the recorded rank puts the gold after all of its ties.
