"""Dataset preparation and checks for the Recall@N experiment.

The target side of each work is one continuous word sequence (segments
joined in source order), so windows can cross segment boundaries; segment
ranges are used only to judge hits. `vocab.build_index` already stores
that sequence and the ranges in `index/docs.json`; this script checks them
against the corpus and writes the statistics a reader needs:

    python bench/eval_dataset.py --works acSen --out bench/results/acSen
    python bench/eval_dataset.py --works all   --out bench/results/all

Writes `dataset.md` and `dataset_stats.json` to --out.
"""

import argparse
import hashlib
import json
import statistics as st
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from eval_lib import DIRECTIONS, DUPLICATE_WORKS, works_for  # noqa: E402
from fuzzysearch.vocab import VARIETIES, load_index, tokenize  # noqa: E402

LENGTH_BANDS = ((1, 4), (5, 8), (9, 14), (15, 10**9))


def band_name(lo, hi):
    return f"{lo}+" if hi >= 10**9 else f"{lo}–{hi}"


def check_work(index, work, corpus_doc, manifest_doc, source, target):
    """List of (check, passed, detail) for one work."""
    out = []
    doc = index.docs[work]
    for side in (source, target):
        ids, blocks = doc[side]["ids"], doc[side]["blocks"]
        contiguous = blocks[0]["start"] == 0 and all(
            a["end"] == b["start"] for a, b in zip(blocks, blocks[1:]))
        covers = blocks[-1]["end"] == len(ids)
        out.append((f"{side}: segments are contiguous, in order, without overlap",
                    contiguous, f"{len(blocks)} segments"))
        out.append((f"{side}: segments cover the whole sequence",
                    covers, f"last end {blocks[-1]['end']} vs {len(ids)} words"))
        field = VARIETIES[side][0]
        src = {b["id"]: b.get(field) or "" for b in corpus_doc["blocks"]}
        bad = [b["id"] for b in blocks
               if [index.words[i] for i in ids[b["start"]:b["end"]]] != tokenize(src[b["id"]])]
        out.append((f"{side}: every segment's words equal its corpus text tokenized (lowercase \\w+)",
                    not bad, f"{len(bad)} mismatches" + (f", e.g. {bad[:3]}" if bad else "")))
        if manifest_doc:
            want = manifest_doc["texts"][side]["tokens"]
            out.append((f"{side}: word count equals corpus/extracted/manifest.json",
                        want == len(ids), f"{len(ids)} vs {want}"))
    same = [b["id"] for b in doc[source]["blocks"]] == [b["id"] for b in doc[target]["blocks"]]
    out.append(("query and answer segment IDs correspond one-to-one, same order", same,
                f"{len(doc[source]['blocks'])} / {len(doc[target]['blocks'])}"))
    return out


def work_stats(index, work, source, target):
    doc = index.docs[work]
    qs, ts = doc[source], doc[target]
    q_len, ratios, shared, q_total = [], [], 0, 0
    empty_q = empty_t = 0
    for qb, tb in zip(qs["blocks"], ts["blocks"]):
        q = qs["ids"][qb["start"]:qb["end"]]
        t = ts["ids"][tb["start"]:tb["end"]]
        empty_q += not q
        empty_t += not t
        if q:
            q_len.append(len(q))
            q_total += len(q)
            shared += sum((Counter(q) & Counter(t)).values())
            ratios.append(len(t) / len(q))
    quart = st.quantiles(ratios, n=4) if len(ratios) > 1 else [ratios[0]] * 3
    return {
        "segments": len(qs["blocks"]),
        "queries": len(q_len),
        "empty_query_segments": empty_q,
        "empty_answer_segments": empty_t,
        "query_tokens": len(qs["ids"]),
        "target_tokens": len(ts["ids"]),
        "length_ratio": len(ts["ids"]) / max(1, len(qs["ids"])),
        "segment_ratio_median": st.median(ratios),
        "segment_ratio_iqr": [quart[0], quart[2]],
        "shared_token_share": shared / max(1, q_total),
        "query_len_min": min(q_len), "query_len_median": st.median(q_len),
        "query_len_max": max(q_len),
        "query_len_bands": {band_name(lo, hi): sum(lo <= n <= hi for n in q_len)
                            for lo, hi in LENGTH_BANDS},
        "target_sha256": hashlib.sha256(json.dumps(ts["ids"]).encode()).hexdigest()[:12],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--index", default="index")
    ap.add_argument("--corpus", default="../corpus")
    ap.add_argument("--works", default="acSen")
    ap.add_argument("--direction", choices=DIRECTIONS, default="med2mod")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    index = load_index(args.index)
    corpus_dir = Path(args.corpus)
    manifest_path = corpus_dir / "extracted" / "manifest.json"
    manifest = {}
    if manifest_path.exists():
        manifest = {d["id"]: d for d in json.loads(manifest_path.read_text())["documents"]}
    corpus = {}
    for p in sorted(corpus_dir.glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        corpus[d.get("id") or p.stem] = d
    source, target = DIRECTIONS[args.direction]
    works = works_for(index, args.works)

    checks, stats = {}, {}
    for w in works:
        checks[w] = check_work(index, w, corpus[w], manifest.get(w), source, target)
        stats[w] = work_stats(index, w, source, target)
    skipped_empty = sorted(k for k, d in corpus.items() if not d.get("blocks"))

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "dataset_stats.json").write_text(json.dumps(
        {"direction": args.direction, "works": stats,
         "checks": {w: [{"check": c, "passed": ok, "detail": d} for c, ok, d in cs]
                    for w, cs in checks.items()}},
        ensure_ascii=False, indent=2), encoding="utf-8")

    L = [f"# Dataset: {args.works} ({source} → {target})", ""]
    L += ["Queries are the non-empty " + source + " segments; each is searched in the full "
          + target + " text of the same work, which is one continuous word sequence "
          "(segments joined in source order, tokenized as lowercase `\\w+` words). "
          "The gold answer is the " + target + " segment with the same ID.", ""]
    n_fail = sum(not ok for cs in checks.values() for _, ok, _ in cs)
    L += [f"## Consistency checks: {'all passed' if not n_fail else f'{n_fail} FAILED'}", ""]
    for w in works:
        if len(works) > 1 and all(ok for _, ok, _ in checks[w]):
            continue
        L += [f"**{w}**", "", "| | Check | Detail |", "|---|---|---|"]
        L += [f"| {'✅' if ok else '❌'} | {c} | {d} |" for c, ok, d in checks[w]]
        L.append("")
    if len(works) > 1:
        L += [f"Works whose checks all passed are not listed individually "
              f"({sum(all(ok for _, ok, _ in checks[w]) for w in works)} of {len(works)}).", ""]
    excluded = [f"`{k}` (same text as `{v}`)" for k, v in DUPLICATE_WORKS.items()]
    excluded += [f"`{k}` (no segments)" for k in skipped_empty]
    if args.works == "all":
        L += ["Excluded works: " + "; ".join(excluded) + ".", ""]

    tot_q = sum(s["queries"] for s in stats.values())
    tot_qt = sum(s["query_tokens"] for s in stats.values())
    tot_tt = sum(s["target_tokens"] for s in stats.values())
    L += ["## Statistics", "",
          "| Work | Segments | Queries | " + source + " words | " + target + " words "
          "| Length ratio | Segment ratio median (IQR) | Exact shared words | Query length min / median / max |",
          "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for w in works:
        s = stats[w]
        L.append(f"| {w} | {s['segments']} | {s['queries']} | {s['query_tokens']:,} | "
                 f"{s['target_tokens']:,} | {s['length_ratio']:.3f} | "
                 f"{s['segment_ratio_median']:.2f} ({s['segment_ratio_iqr'][0]:.2f}–"
                 f"{s['segment_ratio_iqr'][1]:.2f}) | {s['shared_token_share']:.1%} | "
                 f"{s['query_len_min']} / {s['query_len_median']:g} / {s['query_len_max']} |")
    if len(works) > 1:
        L.append(f"| **total** | {sum(s['segments'] for s in stats.values())} | {tot_q} | "
                 f"{tot_qt:,} | {tot_tt:,} | {tot_tt / tot_qt:.3f} | | | |")
    L += ["", "- **Length ratio** = " + target + " words / " + source + " words over the "
          "whole work; it uses no alignment and sets the window length (W = int(Q × ratio)).",
          "- **Exact shared words** = query words that also occur (same spelling, counted "
          "with multiplicity) in the aligned answer segment, as a share of all query words.",
          "- Empty segments: " + ", ".join(
              f"{w}: {stats[w]['empty_query_segments']} query / "
              f"{stats[w]['empty_answer_segments']} answer"
              for w in works if stats[w]['empty_query_segments'] or stats[w]['empty_answer_segments'])
          + (" (empty queries are skipped)" if any(
              stats[w]['empty_query_segments'] for w in works) else "none"), ""]

    bands = Counter()
    for s in stats.values():
        bands.update(s["query_len_bands"])
    L += ["## Query length (words)", "", "| Band | Queries |", "|---|---:|"]
    L += [f"| {band_name(lo, hi)} | {bands[band_name(lo, hi)]} |" for lo, hi in LENGTH_BANDS]
    L.append("")

    first = works[0]
    doc = index.docs[first]
    L += [f"## How the {target} text of `{first}` is laid out (first 10 segments)", "",
          "| Segment | Word positions | Words |", "|---|---|---|"]
    for b in doc[target]["blocks"][:10]:
        ws = [index.words[i] for i in doc[target]["ids"][b["start"]:b["end"]]]
        L.append(f"| {b['id']} | {b['start']}–{b['end'] - 1} | {' '.join(ws)} |")
    L += ["", "Positions run on across segments: a window can start inside one segment "
          "and end inside the next.", ""]
    qs = sorted(((b["end"] - b["start"], b["id"]) for b in doc[source]["blocks"]
                 if b["end"] > b["start"]))
    L += [f"## Shortest and longest queries in `{first}`", "",
          "| Segment | Words | Query |", "|---|---:|---|"]
    for n, bid in qs[:5] + qs[-5:]:
        b = next(x for x in doc[source]["blocks"] if x["id"] == bid)
        L.append(f"| {bid} | {n} | {' '.join(index.words[i] for i in doc[source]['ids'][b['start']:b['end']])} |")
    (out / "dataset.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{len(works)} works, {tot_q} queries, checks failed: {n_fail} -> {out / 'dataset.md'}")


if __name__ == "__main__":
    main()
