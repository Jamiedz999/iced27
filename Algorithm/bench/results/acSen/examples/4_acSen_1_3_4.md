# Example: a tie decides the outcome (exact match)

Work `acSen`, segment `acSen_1_3_4`, shown condition **exact**.

## Inputs

- Query (medieval, original): ocus ro fhiarfaigset scéla d’aroile ainnséin,
- Query words (lowercase `\w+`), Q = 7: `ocus ro fhiarfaigset scéla d aroile ainnséin`
- Gold answer (modern, original): agus d’fhiafraíodar scéala d’araile ansin,
- Gold words: positions 268–274 of 4007: `agus d fhiafraíodar scéala d araile ansin`
- Window: W = int(Q × ratio) = int(7 × 1.033) = 7; 4001 windows scored

## Result: gold segment rank 112 (worst case, tied with 111 other segment(s))

### Best window of the gold segment: window 265–271

Distance matrix D for this window (rows: query words, columns: window words; 0 = identical, 1 = nothing in common). **Bold** cells are the pairs the greedy step picks.

| query \ window | frasa (265) | díochra (266) | déar (267) | agus (268) | d (269) | fhiafraíodar (270) | scéala (271) |
|---|---:|---:|---:|---:|---:|---:|---:|
| ocus | **1.00** | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| ro | 1.00 | **1.00** | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| fhiarfaigset | 1.00 | 1.00 | **1.00** | 1.00 | 1.00 | 1.00 | 1.00 |
| scéla | 1.00 | 1.00 | 1.00 | **1.00** | 1.00 | 1.00 | 1.00 |
| d | 1.00 | 1.00 | 1.00 | 1.00 | **0.00** | 1.00 | 1.00 |
| aroile | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | **1.00** | 1.00 |
| ainnséin | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | **1.00** |

Greedy pairing (repeatedly take the smallest remaining value, then strike out its row and column):

1. `d` ↔ `d` = 0.0000
2. `ocus` ↔ `frasa` = 1.0000
3. `ro` ↔ `díochra` = 1.0000
4. `fhiarfaigset` ↔ `déar` = 1.0000
5. `scéla` ↔ `agus` = 1.0000
6. `aroile` ↔ `fhiafraíodar` = 1.0000
7. `ainnséin` ↔ `scéala` = 1.0000

Score = sum / Q = 6.0000 / 7 = **0.8571** (the run recorded 0.8571 for this window).

### Best window overall (segment acSen_1_2_2): window 118–124

Distance matrix D for this window (rows: query words, columns: window words; 0 = identical, 1 = nothing in common). **Bold** cells are the pairs the greedy step picks.

| query \ window | conair (118) | do (119) | rachaimis (120) | roimh (121) | dheoidh (122) | lae (123) | d (124) |
|---|---:|---:|---:|---:|---:|---:|---:|
| ocus | **1.00** | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| ro | 1.00 | **1.00** | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| fhiarfaigset | 1.00 | 1.00 | **1.00** | 1.00 | 1.00 | 1.00 | 1.00 |
| scéla | 1.00 | 1.00 | 1.00 | **1.00** | 1.00 | 1.00 | 1.00 |
| d | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | **0.00** |
| aroile | 1.00 | 1.00 | 1.00 | 1.00 | **1.00** | 1.00 | 1.00 |
| ainnséin | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | **1.00** | 1.00 |

Greedy pairing (repeatedly take the smallest remaining value, then strike out its row and column):

1. `d` ↔ `d` = 0.0000
2. `ocus` ↔ `conair` = 1.0000
3. `ro` ↔ `do` = 1.0000
4. `fhiarfaigset` ↔ `rachaimis` = 1.0000
5. `scéla` ↔ `roimh` = 1.0000
6. `aroile` ↔ `dheoidh` = 1.0000
7. `ainnséin` ↔ `lae` = 1.0000

Score = sum / Q = 6.0000 / 7 = **0.8571** (the run recorded 0.8571 for this window).

## Top distinct segments, exact

| Rank shown | Score | Segment | Best window (word positions) | Words in the window | Words of the window in this segment | Gold? |
|---:|---:|---|---|---|---:|:---:|
| 1 | 0.8571 | acSen_1_2_2 | 118–124 | conair do rachaimis roimh dheoidh lae d | 7 / 7 |  |
| 2 | 0.8571 | acSen_1_2_13 | 229–235 | thug moiriath iníon rí mhara gréag d | 7 / 7 |  |
| 3 | 0.8571 | acSen_1_3_1 | 245–251 | na hoíche sin ag cámha agus d | 5 / 7 |  |
| 4 | 0.8571 | acSen_1_3_2 | 247–253 | sin ag cámha agus d fhiafraigh díobh | 4 / 7 |  |
| 5 | 0.8571 | acSen_1_3_3 | 254–260 | a n ainmneacha agus d insíodar di | 4 / 7 |  |

## Same query, levenshtein: gold segment rank 1 (worst case)

| Rank shown | Score | Segment | Best window (word positions) | Words in the window | Words of the window in this segment | Gold? |
|---:|---:|---|---|---|---:|:---:|
| 1 | 0.3988 | acSen_1_3_4 | 268–274 | agus d fhiafraíodar scéala d araile ansin | 7 / 7 | ✅ |
| 2 | 0.5080 | acSen_2_1_2 | 1269–1275 | dúileamhan d éirigh padraig ansin agus do | 6 / 7 |  |
| 3 | 0.5131 | acSen_1_3_5 | 272–278 | d araile ansin agus thángadar iar sin | 4 / 7 |  |
| 4 | 0.5131 | acSen_1_3_9 | 332–338 | go minic roimhe sin agus d éirigh | 4 / 7 |  |
| 5 | 0.5131 | acSen_1_3_10 | 334–340 | roimhe sin agus d éirigh sí go | 5 / 7 |  |

Ranks shown here list tied segments in text order; the recorded rank puts the gold after all of its ties.
