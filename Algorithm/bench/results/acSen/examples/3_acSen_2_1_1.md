# Example: not found in the top 5

Work `acSen`, segment `acSen_2_1_1`, shown condition **levenshtein**.

## Inputs

- Query (medieval, original): Ocus do bhátur annsin co táinic maden arnamárach,
- Query words (lowercase `\w+`), Q = 8: `ocus do bhátur annsin co táinic maden arnamárach`
- Gold answer (modern, original): Do bhíodar ann gur tháinig mochshoilse arna mhárach, ag idirmholadh an Dúileamhan.
- Gold words: positions 1258–1269 of 4007: `do bhíodar ann gur tháinig mochshoilse arna mhárach ag idirmholadh an dúileamhan`
- Window: W = int(Q × ratio) = int(8 × 1.033) = 8; 4000 windows scored

## Result: gold segment rank 12 (worst case)

### Best window of the gold segment: window 1258–1265

Distance matrix D for this window (rows: query words, columns: window words; 0 = identical, 1 = nothing in common). **Bold** cells are the pairs the greedy step picks.

| query \ window | do (1258) | bhíodar (1259) | ann (1260) | gur (1261) | tháinig (1262) | mochshoilse (1263) | arna (1264) | mhárach (1265) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ocus | 1.00 | 0.86 | 1.00 | 0.75 | 1.00 | **0.73** | 1.00 | 1.00 |
| do | **0.00** | 0.86 | 1.00 | 1.00 | 1.00 | 0.91 | 1.00 | 1.00 |
| bhátur | 1.00 | **0.57** | 1.00 | 0.67 | 0.71 | 0.91 | 1.00 | 0.71 |
| annsin | 1.00 | 1.00 | **0.50** | 1.00 | 0.86 | 0.82 | 0.67 | 1.00 |
| co | 0.50 | 0.86 | 1.00 | **1.00** | 1.00 | 0.82 | 1.00 | 0.86 |
| táinic | 1.00 | 1.00 | 0.83 | 1.00 | **0.29** | 0.91 | 0.83 | 0.86 |
| maden | 0.80 | 0.86 | 0.60 | 1.00 | 0.86 | 0.91 | **0.80** | 0.86 |
| arnamárach | 1.00 | 0.90 | 0.80 | 0.90 | 0.90 | 1.00 | 0.60 | **0.50** |

Greedy pairing (repeatedly take the smallest remaining value, then strike out its row and column):

1. `do` ↔ `do` = 0.0000
2. `táinic` ↔ `tháinig` = 0.2857
3. `annsin` ↔ `ann` = 0.5000
4. `arnamárach` ↔ `mhárach` = 0.5000
5. `bhátur` ↔ `bhíodar` = 0.5714
6. `ocus` ↔ `mochshoilse` = 0.7273
7. `maden` ↔ `arna` = 0.8000
8. `co` ↔ `gur` = 1.0000

Score = sum / Q = 4.3844 / 8 = **0.5481** (the run recorded 0.5481 for this window).

### Best window overall (segment acSen_3_5_1): window 2469–2476

Distance matrix D for this window (rows: query words, columns: window words; 0 = identical, 1 = nothing in common). **Bold** cells are the pairs the greedy step picks.

| query \ window | chaoil (2469) | tháinig (2470) | an (2471) | iníon (2472) | ansin (2473) | agus (2474) | do (2475) | shín (2476) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ocus | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | **0.50** | 1.00 | 1.00 |
| do | 0.83 | 1.00 | 1.00 | 0.80 | 1.00 | 1.00 | **0.00** | 1.00 |
| bhátur | 0.83 | 0.71 | 1.00 | 1.00 | 1.00 | 0.83 | 1.00 | **0.83** |
| annsin | 0.83 | 0.86 | 0.67 | 0.67 | **0.17** | 0.67 | 1.00 | 0.83 |
| co | **0.67** | 1.00 | 1.00 | 0.80 | 1.00 | 1.00 | 0.50 | 1.00 |
| táinic | 0.83 | **0.29** | 0.83 | 0.83 | 0.83 | 1.00 | 1.00 | 0.83 |
| maden | 0.83 | 0.86 | **0.60** | 0.80 | 0.80 | 0.80 | 0.80 | 0.80 |
| arnamárach | 0.90 | 0.90 | 0.80 | **0.90** | 0.80 | 0.90 | 1.00 | 1.00 |

Greedy pairing (repeatedly take the smallest remaining value, then strike out its row and column):

1. `do` ↔ `do` = 0.0000
2. `annsin` ↔ `ansin` = 0.1667
3. `táinic` ↔ `tháinig` = 0.2857
4. `ocus` ↔ `agus` = 0.5000
5. `maden` ↔ `an` = 0.6000
6. `co` ↔ `chaoil` = 0.6667
7. `bhátur` ↔ `shín` = 0.8333
8. `arnamárach` ↔ `iníon` = 0.9000

Score = sum / Q = 3.9524 / 8 = **0.4940** (the run recorded 0.4940 for this window).

## Top distinct segments, levenshtein

| Rank shown | Score | Segment | Best window (word positions) | Words in the window | Words of the window in this segment | Gold? |
|---:|---:|---|---|---|---:|:---:|
| 1 | 0.4940 | acSen_3_5_1 | 2469–2476 | chaoil tháinig an iníon ansin agus do shín | 7 / 8 |  |
| 2 | 0.5131 | acSen_4_7_11 | 3654–3661 | teamhrach agus do chonaic fionn sin agus do | 5 / 8 |  |
| 3 | 0.5146 | acSen_4_3_1 | 3179–3186 | bhruín is ansin ráinig a chorn dála do | 7 / 8 |  |
| 4 | 0.5167 | acSen_1_5_3 | 466–473 | ansin agus do cheiliúradar do chámha iar sin | 7 / 8 |  |
| 5 | 0.5292 | acSen_3_1_7 | 1470–1477 | bhuime féin do chuas ann arsa caol cad | 7 / 8 |  |

## Same query, exact: gold segment rank 287 (worst case, tied with 286 other segment(s))

| Rank shown | Score | Segment | Best window (word positions) | Words in the window | Words of the window in this segment | Gold? |
|---:|---:|---|---|---|---:|:---:|
| 1 | 0.8750 | acSen_1_1_2 | 8–15 | chatha ollarba agus ar ndíothú na féinne do | 5 / 8 |  |
| 2 | 0.8750 | acSen_1_1_3 | 12–19 | ndíothú na féinne do scaoileadar iar sin ina | 5 / 8 |  |
| 3 | 0.8750 | acSen_1_1_10 | 85–92 | n abairtear lú sa tan seo agus do | 6 / 8 |  |
| 4 | 0.8750 | acSen_1_1_11 | 88–95 | sa tan seo agus do bhíodar go dubhach | 5 / 8 |  |
| 5 | 0.8750 | acSen_1_2_1 | 112–119 | maith a anam a oisín cá conair do | 5 / 8 |  |

Ranks shown here list tied segments in text order; the recorded rank puts the gold after all of its ties.
