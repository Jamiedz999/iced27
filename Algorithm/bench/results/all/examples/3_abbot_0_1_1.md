# Example: not found in the top 5

Work `abbot`, segment `abbot_0_1_1`, shown condition **levenshtein**.

## Inputs

- Query (medieval, original): Aroile hóclach ro baei a n-abduine Druimenaigh
- Query words (lowercase `\w+`), Q = 8: `aroile hóclach ro baei a n abduine druimenaigh`
- Gold answer (modern, original): Bhí ógfhear áirithe ina ab ar Dhroimeanach
- Gold words: positions 0–6 of 929: `bhí ógfhear áirithe ina ab ar dhroimeanach`
- Window: W = int(Q × ratio) = int(8 × 1.118) = 8; 922 windows scored

## Result: gold segment rank 63 (worst case)

### Best window of the gold segment: window 1–8

Distance matrix D for this window (rows: query words, columns: window words; 0 = identical, 1 = nothing in common). **Bold** cells are the pairs the greedy step picks.

| query \ window | ógfhear (1) | áirithe (2) | ina (3) | ab (4) | ar (5) | dhroimeanach (6) | agus (7) | bheartaigh (8) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| aroile | 1.00 | 0.71 | 0.83 | 0.83 | **0.67** | 0.67 | 0.83 | 0.70 |
| hóclach | 1.00 | 1.00 | 0.86 | 0.86 | 0.86 | 0.67 | 1.00 | **0.70** |
| ro | 1.00 | **0.86** | 1.00 | 1.00 | 1.00 | 0.83 | 1.00 | 0.90 |
| baei | **0.86** | 0.86 | 1.00 | 0.75 | 0.75 | 0.92 | 1.00 | 0.70 |
| a | 0.86 | 1.00 | 0.67 | **0.50** | 0.50 | 0.92 | 0.75 | 0.90 |
| n | 1.00 | 1.00 | **0.67** | 1.00 | 1.00 | 0.92 | 1.00 | 1.00 |
| abduine | 1.00 | 0.86 | 0.71 | 0.71 | 0.86 | 0.83 | **0.71** | 0.80 |
| druimenaigh | 0.82 | 0.82 | 0.73 | 0.91 | 0.91 | **0.42** | 0.91 | 0.64 |

Greedy pairing (repeatedly take the smallest remaining value, then strike out its row and column):

1. `druimenaigh` ↔ `dhroimeanach` = 0.4167
2. `a` ↔ `ab` = 0.5000
3. `aroile` ↔ `ar` = 0.6667
4. `n` ↔ `ina` = 0.6667
5. `hóclach` ↔ `bheartaigh` = 0.7000
6. `abduine` ↔ `agus` = 0.7143
7. `ro` ↔ `áirithe` = 0.8571
8. `baei` ↔ `ógfhear` = 0.8571

Score = sum / Q = 5.3786 / 8 = **0.6723** (the run recorded 0.6723 for this window).

### Best window overall (segment abbot_0_4_5): window 269–276

Distance matrix D for this window (rows: query words, columns: window words; 0 = identical, 1 = nothing in common). **Bold** cells are the pairs the greedy step picks.

| query \ window | dhubhach (269) | dheorach (270) | dhobrónach (271) | a (272) | bhí (273) | an (274) | duine (275) | eile (276) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| aroile | 1.00 | 0.88 | 0.90 | 0.83 | 1.00 | 0.83 | 0.67 | **0.50** |
| hóclach | **0.50** | 0.50 | 0.60 | 0.86 | 1.00 | 0.86 | 1.00 | 0.86 |
| ro | 1.00 | **0.88** | 0.90 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| baei | 0.75 | 0.88 | 0.80 | 0.75 | **0.75** | 0.75 | 1.00 | 1.00 |
| a | 0.88 | 0.88 | 0.90 | **0.00** | 1.00 | 0.50 | 1.00 | 1.00 |
| n | 1.00 | 1.00 | 0.90 | 1.00 | 1.00 | **0.50** | 0.80 | 1.00 |
| abduine | 1.00 | 1.00 | 0.90 | 0.86 | 0.86 | 0.71 | **0.29** | 0.71 |
| druimenaigh | 0.64 | 0.73 | **0.64** | 0.91 | 1.00 | 0.91 | 0.64 | 0.82 |

Greedy pairing (repeatedly take the smallest remaining value, then strike out its row and column):

1. `a` ↔ `a` = 0.0000
2. `abduine` ↔ `duine` = 0.2857
3. `aroile` ↔ `eile` = 0.5000
4. `hóclach` ↔ `dhubhach` = 0.5000
5. `n` ↔ `an` = 0.5000
6. `druimenaigh` ↔ `dhobrónach` = 0.6364
7. `baei` ↔ `bhí` = 0.7500
8. `ro` ↔ `dheorach` = 0.8750

Score = sum / Q = 4.0471 / 8 = **0.5059** (the run recorded 0.5059 for this window).

## Top distinct segments, levenshtein

| Rank shown | Score | Segment | Best window (word positions) | Words in the window | Words of the window in this segment | Gold? |
|---:|---:|---|---|---|---:|:---:|
| 1 | 0.5059 | abbot_0_4_5 | 269–276 | dhubhach dheorach dhobrónach a bhí an duine eile | 8 / 8 |  |
| 2 | 0.5749 | abbot_0_3_12 | 214–221 | imríodh air a tharla an claochlú ina dhiaidh | 6 / 8 |  |
| 3 | 0.5872 | abbot_0_3_2 | 128–135 | breith ar a chlaíomh ní bhfuair ach uirlis | 4 / 8 |  |
| 4 | 0.5881 | abbot_0_5_3 | 512–519 | a bhí ar an taobh thiar de dhroimeanach | 8 / 8 |  |
| 5 | 0.5888 | abbot_0_5_12 | 606–613 | nó gearr iad i bhfochair a chéile cuirfidh | 7 / 8 |  |

## Same query, exact: gold segment rank 94 (worst case, tied with 36 other segment(s))

| Rank shown | Score | Segment | Best window (word positions) | Words in the window | Words of the window in this segment | Gold? |
|---:|---:|---|---|---|---:|:---:|
| 1 | 0.8750 | abbot_0_1_2 | 7–14 | agus bheartaigh sé ar fhleá mhór thaitneamhach a | 8 / 8 |  |
| 2 | 0.8750 | abbot_0_2_1 | 18–25 | cháisc a cheiliúradh tar éis dó an fhleá | 5 / 8 |  |
| 3 | 0.8750 | abbot_0_2_2 | 25–32 | fhleá a ullmhú chuaigh an t ógfhear amach | 5 / 8 |  |
| 4 | 0.8750 | abbot_0_2_3 | 36–43 | agus shuigh sé ar úrchnoc ard aoibhinn a | 8 / 8 |  |
| 5 | 0.8750 | abbot_0_2_4 | 46–53 | cionn an bhaile agus is mar seo a | 5 / 8 |  |

Ranks shown here list tied segments in text order; the recorded rank puts the gold after all of its ties.
