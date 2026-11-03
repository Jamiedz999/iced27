# Dataset: acSen (medieval → modern)

Queries are the non-empty medieval segments; each is searched in the full modern text of the same work, which is one continuous word sequence (segments joined in source order, tokenized as lowercase `\w+` words). The gold answer is the modern segment with the same ID.

## Consistency checks: all passed

**acSen**

| | Check | Detail |
|---|---|---|
| ✅ | medieval: segments are contiguous, in order, without overlap | 522 segments |
| ✅ | medieval: segments cover the whole sequence | last end 3879 vs 3879 words |
| ✅ | medieval: every segment's words equal its corpus text tokenized (lowercase \w+) | 0 mismatches |
| ✅ | medieval: word count equals corpus/extracted/manifest.json | 3879 vs 3879 |
| ✅ | modern: segments are contiguous, in order, without overlap | 522 segments |
| ✅ | modern: segments cover the whole sequence | last end 4007 vs 4007 words |
| ✅ | modern: every segment's words equal its corpus text tokenized (lowercase \w+) | 0 mismatches |
| ✅ | modern: word count equals corpus/extracted/manifest.json | 4007 vs 4007 |
| ✅ | query and answer segment IDs correspond one-to-one, same order | 522 / 522 |

## Statistics

| Work | Segments | Queries | medieval words | modern words | Length ratio | Segment ratio median (IQR) | Exact shared words | Query length min / median / max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| acSen | 522 | 522 | 3,879 | 4,007 | 1.033 | 1.00 (1.00–1.00) | 32.3% | 2 / 6 / 28 |

- **Length ratio** = modern words / medieval words over the whole work; it uses no alignment and sets the window length (W = int(Q × ratio)).
- **Exact shared words** = query words that also occur (same spelling, counted with multiplicity) in the aligned answer segment, as a share of all query words.
- Empty segments: none

## Query length (words)

| Band | Queries |
|---|---:|
| 1–4 | 88 |
| 5–8 | 284 |
| 9–14 | 125 |
| 15+ | 25 |

## How the modern text of `acSen` is laid out (first 10 segments)

| Segment | Word positions | Words |
|---|---|---|
| acSen_1_1_1 | 0–9 | ar dtabhairt chatha chomair agus chatha ghabhra agus chatha ollarba |
| acSen_1_1_2 | 10–14 | agus ar ndíothú na féinne |
| acSen_1_1_3 | 15–25 | do scaoileadar iar sin ina ndrongaibh agus ina mbuínibh fá éirinn |
| acSen_1_1_4 | 26–42 | go nár mhair le ham na huaire sin díobh ach dhá óglach mhaithe de dheireadh na féinne |
| acSen_1_1_5 | 43–46 | i oisín mac fhinn |
| acSen_1_1_6 | 47–52 | agus caoilte mac chrunnchon mhic rónáin |
| acSen_1_1_7 | 53–59 | ar scíth a lúith agus a lámhaigh |
| acSen_1_1_8 | 60–66 | agus dhá naonúr óglach mar aon leo |
| acSen_1_1_9 | 67–79 | agus thángadar an dá naonúr laoch sin a himeallaibh shléibhe fuaid fhonnscothaigh fhoithriúil |
| acSen_1_1_10 | 80–90 | go lughbhartaibh bána amach lena n abairtear lú sa tan seo |

Positions run on across segments: a window can start inside one segment and end inside the next.

## Shortest and longest queries in `acSen`

| Segment | Words | Query |
|---|---:|---|
| acSen_3_5_12 | 2 | luinche corr |
| acSen_3_5_52 | 2 | caince corr |
| acSen_3_5_7 | 2 | geisid cuan |
| acSen_1_10_7 | 3 | ro thidhluicfed find |
| acSen_1_11_3 | 3 | fírinde inár croidhedhaibh |
| acSen_3_4_5 | 20 | ocus as í an ingen ros biath d as ocus d fírleamhnacht iat céin ro bás ag cur in chatha |
| acSen_1_6_11 | 22 | ocus dochuatar na demhna i cnocaibh ocus i scalpaibh ocus i n imlibh na críche ocus ind orba uatha ar cach leath |
| acSen_1_4_2 | 23 | iná mar as éicin dúind in dá nónbar itamáit do deredh na muindtire móire maithi sin do scaradh ocus do scáiledh ó chéile |
| acSen_1_7_5 | 23 | ocus ní roiched acht co tana a tháibh nó co formna a ghualand in bhfer ba mó dona cléirchibh don fhir dhibh sin |
| acSen_1_6_8 | 28 | is and sin do éirigh in t éo flaithemhnais ocus in t uaithne airechais ocus in t aingil talmaide i pátraic mac alprainn i apstal na n gaoidhel |
