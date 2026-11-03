# Dataset: all (medieval → modern)

Queries are the non-empty medieval segments; each is searched in the full modern text of the same work, which is one continuous word sequence (segments joined in source order, tokenized as lowercase `\w+` words). The gold answer is the modern segment with the same ID.

## Consistency checks: all passed

Works whose checks all passed are not listed individually (49 of 49).

Excluded works: `aidedCho` (same text as `aidedChonch`); `buileShuib` (no segments).

## Statistics

| Work | Segments | Queries | medieval words | modern words | Length ratio | Segment ratio median (IQR) | Exact shared words | Query length min / median / max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AidedCheltC | 133 | 133 | 1,021 | 1,073 | 1.051 | 1.00 (1.00–1.14) | 25.9% | 1 / 7 / 15 |
| abbot | 94 | 94 | 831 | 929 | 1.118 | 1.08 (0.98–1.29) | 16.0% | 4 / 9 / 16 |
| acSen | 522 | 522 | 3,879 | 4,007 | 1.033 | 1.00 (1.00–1.00) | 32.3% | 2 / 6 / 28 |
| aidedBres | 43 | 43 | 284 | 335 | 1.180 | 1.17 (1.00–1.33) | 15.8% | 3 / 6 / 13 |
| aidedCheitM | 101 | 101 | 721 | 745 | 1.033 | 1.00 (1.00–1.10) | 32.7% | 2 / 7 / 14 |
| aidedChel | 133 | 133 | 1,020 | 1,073 | 1.052 | 1.00 (1.00–1.14) | 25.9% | 1 / 7 / 15 |
| aidedChonch | 128 | 128 | 858 | 996 | 1.161 | 1.14 (1.00–1.33) | 11.3% | 2 / 6 / 13 |
| aidedConr | 323 | 323 | 1,614 | 2,084 | 1.291 | 1.25 (1.00–1.50) | 8.5% | 1 / 5 / 14 |
| aidedDiar | 545 | 545 | 4,003 | 4,536 | 1.133 | 1.09 (1.00–1.30) | 17.5% | 1 / 7 / 21 |
| aidedFerg | 54 | 54 | 440 | 453 | 1.030 | 1.00 (1.00–1.10) | 28.2% | 2 / 7.5 / 18 |
| aidedLoeg | 29 | 29 | 210 | 220 | 1.048 | 1.14 (1.00–1.24) | 25.7% | 2 / 6 / 23 |
| aidedMael | 104 | 104 | 688 | 791 | 1.150 | 1.12 (1.00–1.40) | 11.5% | 2 / 6 / 15 |
| aidedOenfir | 189 | 189 | 1,102 | 1,251 | 1.135 | 1.00 (1.00–1.25) | 20.9% | 1 / 5 / 15 |
| aislOeng | 207 | 207 | 1,441 | 1,598 | 1.109 | 1.11 (1.00–1.29) | 9.3% | 1 / 6 / 17 |
| baileBinn | 109 | 109 | 547 | 680 | 1.243 | 1.17 (1.00–1.50) | 14.1% | 1 / 5 / 10 |
| boroma | 845 | 844 | 5,665 | 6,230 | 1.100 | 1.00 (1.00–1.20) | 17.6% | 1 / 6 / 16 |
| cathAlma | 330 | 330 | 2,062 | 2,369 | 1.149 | 1.04 (1.00–1.33) | 15.7% | 2 / 6 / 20 |
| cathCairnn | 216 | 216 | 1,453 | 1,753 | 1.206 | 1.17 (1.00–1.40) | 14.8% | 1 / 6 / 23 |
| cathMaige | 638 | 638 | 3,781 | 4,227 | 1.118 | 1.06 (1.00–1.33) | 14.2% | 1 / 6 / 17 |
| ceartCla | 113 | 113 | 798 | 994 | 1.246 | 1.17 (1.00–1.56) | 12.8% | 3 / 7 / 16 |
| compertMon | 603 | 603 | 4,278 | 4,371 | 1.022 | 1.00 (0.88–1.17) | 25.6% | 1 / 7 / 20 |
| comracLiad | 185 | 185 | 888 | 964 | 1.086 | 1.00 (1.00–1.20) | 28.3% | 1 / 4 / 14 |
| echtraCho | 111 | 111 | 613 | 786 | 1.282 | 1.29 (1.00–2.00) | 9.0% | 1 / 5 / 22 |
| echtraCorm | 217 | 217 | 1,397 | 1,755 | 1.256 | 1.25 (1.00–1.50) | 14.7% | 2 / 6 / 15 |
| echtraFer | 156 | 156 | 814 | 1,053 | 1.294 | 1.25 (1.00–1.50) | 12.7% | 1 / 5 / 11 |
| echtraMac | 291 | 291 | 1,636 | 1,813 | 1.108 | 1.00 (1.00–1.25) | 14.4% | 1 / 5 / 14 |
| esnadaTige | 126 | 126 | 803 | 1,022 | 1.273 | 1.25 (1.00–1.50) | 13.0% | 2 / 6 / 16 |
| feisTighe | 106 | 106 | 913 | 907 | 0.993 | 1.00 (0.91–1.08) | 39.5% | 3 / 8 / 25 |
| fingalRon | 333 | 333 | 2,156 | 2,509 | 1.164 | 1.14 (1.00–1.40) | 13.5% | 1 / 6 / 19 |
| forbDroma | 2295 | 2295 | 17,581 | 20,196 | 1.149 | 1.12 (1.00–1.40) | 11.5% | 1 / 7 / 27 |
| genChor | 259 | 259 | 1,511 | 1,654 | 1.095 | 1.00 (1.00–1.25) | 14.6% | 2 / 5 / 15 |
| immBrain | 318 | 318 | 1,792 | 1,996 | 1.114 | 1.11 (1.00–1.25) | 14.3% | 3 / 5 / 15 |
| longesMac | 399 | 399 | 2,428 | 2,600 | 1.071 | 1.00 (1.00–1.25) | 11.6% | 1 / 6 / 15 |
| mescaUlad | 1098 | 1097 | 8,073 | 9,620 | 1.192 | 1.17 (1.00–1.40) | 13.0% | 1 / 7 / 21 |
| noínUlad | 71 | 71 | 457 | 575 | 1.258 | 1.25 (1.00–1.40) | 12.9% | 2 / 6 / 15 |
| oenachInd | 216 | 216 | 1,079 | 1,285 | 1.191 | 1.20 (1.00–1.40) | 15.5% | 3 / 5 / 7 |
| oidheChlo | 873 | 873 | 6,154 | 6,513 | 1.058 | 1.00 (1.00–1.14) | 58.2% | 2 / 6 / 20 |
| orgTri | 99 | 99 | 656 | 810 | 1.235 | 1.20 (1.00–1.50) | 14.5% | 1 / 6 / 14 |
| scelaCano | 594 | 594 | 3,859 | 4,482 | 1.161 | 1.17 (1.00–1.34) | 13.3% | 1 / 6 / 23 |
| scelaCol | 78 | 78 | 600 | 694 | 1.157 | 1.20 (1.00–1.33) | 21.2% | 1 / 8 / 16 |
| scelaGu | 129 | 129 | 771 | 964 | 1.250 | 1.25 (1.00–1.50) | 12.8% | 1 / 5 / 15 |
| scelaGua | 34 | 34 | 215 | 261 | 1.214 | 1.13 (1.00–1.54) | 23.7% | 3 / 6 / 12 |
| scelaMon | 96 | 96 | 632 | 771 | 1.220 | 1.22 (1.00–1.50) | 15.0% | 1 / 6 / 15 |
| scelaMuc | 374 | 374 | 2,412 | 2,725 | 1.130 | 1.09 (1.00–1.33) | 11.4% | 1 / 6 / 16 |
| tainBo | 903 | 902 | 7,731 | 8,585 | 1.110 | 1.11 (1.00–1.25) | 16.3% | 2 / 8 / 32 |
| tochEm | 567 | 565 | 4,436 | 5,413 | 1.220 | 1.18 (1.00–1.44) | 12.7% | 2 / 8 / 18 |
| tochmEm | 209 | 209 | 1,366 | 1,768 | 1.294 | 1.25 (1.00–1.60) | 12.2% | 1 / 6 / 15 |
| tochmEt | 999 | 999 | 6,684 | 7,758 | 1.161 | 1.14 (1.00–1.31) | 13.4% | 2 / 6 / 21 |
| toruig | 205 | 201 | 1,778 | 1,770 | 0.996 | 1.00 (0.89–1.17) | 47.4% | 3 / 8 / 19 |
| **total** | 16800 | 16791 | 116,131 | 131,964 | 1.136 | | | |

- **Length ratio** = modern words / medieval words over the whole work; it uses no alignment and sets the window length (W = int(Q × ratio)).
- **Exact shared words** = query words that also occur (same spelling, counted with multiplicity) in the aligned answer segment, as a share of all query words.
- Empty segments: aidedCheitM: 0 query / 1 answer, aidedConr: 0 query / 1 answer, baileBinn: 0 query / 1 answer, boroma: 1 query / 0 answer, fingalRon: 0 query / 1 answer, forbDroma: 0 query / 1 answer, genChor: 0 query / 1 answer, mescaUlad: 1 query / 2 answer, scelaCano: 0 query / 1 answer, tainBo: 1 query / 0 answer, tochEm: 2 query / 2 answer, toruig: 4 query / 4 answer (empty queries are skipped)

## Query length (words)

| Band | Queries |
|---|---:|
| 1–4 | 3637 |
| 5–8 | 8728 |
| 9–14 | 4075 |
| 15+ | 351 |

## How the modern text of `AidedCheltC` is laid out (first 10 segments)

| Segment | Word positions | Words |
|---|---|---|
| AidedCheltC_0_1_1 | 0–6 | cid de atá oidhe chealtchair mhic uitheachair |
| AidedCheltC_0_1_2 | 7–8 | ní hansa |
| AidedCheltC_0_1_3 | 9–17 | fear amhra do bhí de ultaibh i blaoi brughaidh |
| AidedCheltC_0_1_4 | 18–21 | seacht n airgeda leis |
| AidedCheltC_0_1_5 | 22–27 | seacht fichid bó le gacha airge |
| AidedCheltC_0_1_6 | 28–32 | agus seisreach le gacha airge |
| AidedCheltC_0_1_7 | 33–36 | teach n aíochta aige |
| AidedCheltC_0_1_8 | 37–40 | ba geis dó áfach |
| AidedCheltC_0_1_9 | 41–45 | bean ar dhamhra dá thigh |
| AidedCheltC_0_1_10 | 46–50 | gan feis dó san léi |

Positions run on across segments: a window can start inside one segment and end inside the next.

## Shortest and longest queries in `AidedCheltC`

| Segment | Words | Query |
|---|---:|---|
| AidedCheltC_0_12_17 | 1 | finit |
| AidedCheltC_0_1_2 | 2 | ní hansa |
| AidedCheltC_0_3_8 | 2 | atrulla celtchar |
| AidedCheltC_0_6_1 | 2 | dogníther ón |
| AidedCheltC_0_1_7 | 3 | tech n óiged |
| AidedCheltC_0_11_6 | 13 | rucad in cú minbrec a n ascaid do mac da thó do laignib |
| AidedCheltC_0_11_7 | 13 | ocus is impi dotuit sochaidi do feraib érenn a tig maic da thó |
| AidedCheltC_0_12_12 | 13 | gur féimid bróen fola d fuil na con cuici ar fut an gái |
| AidedCheltC_0_12_14 | 13 | ocus rolaad a gáir guil ocus rotógbad a lia ocus a lecht ann |
| AidedCheltC_0_10_4 | 15 | fadeoigh dono dofell ar dofell ar evidently stands for do ell for cóerchu na bantrebthaigi |
