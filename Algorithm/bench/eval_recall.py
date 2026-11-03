"""Run the Recall@N experiment and write one row per query and condition.

    python bench/eval_recall.py --works acSen --out bench/results/acSen
    python bench/eval_recall.py --works all --out bench/results/all
    python bench/eval_recall.py --works acSen --ratio 1.3 --out bench/results/acSen-r1.3

Every window of the target text is scored (step 1, no threshold, no
pruning); windows are grouped into segments and the gold segment's
worst-case rank is recorded (see `eval_lib`). Writes `per_query.csv` and
`run.json` to --out; `eval_summary.py` and `eval_report.py` read them.
"""

import argparse
import csv
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import eval_lib as E  # noqa: E402
from fuzzysearch.pipeline import moving_window  # noqa: E402
from fuzzysearch.vocab import load_index  # noqa: E402

FIELDS = ["work", "direction", "condition", "ratio", "query_id", "Q", "W", "N",
          "windows", "gold_rank", "gold_tied", "gold_score", "gold_window",
          "top5_segments", "top5_scores", "raw_top5_windows", "raw_top5_segments",
          "raw_top5_distinct"]


def file_sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:16]


def run_query(index, work, condition, q_ids, gold, ratio):
    W = E.window_size(len(q_ids), ratio, work.N)
    D = E.distance_matrix(condition, index, q_ids, work.target_ids)
    scores = E.greedy_all_windows(D, W)
    assign = work.assignment(W)
    seg = E.segment_scores(scores, assign, len(work.block_ids))
    rank, tied = E.gold_rank(seg, gold)
    top = E.top_segments(seg, 5)
    raw = E.raw_top_windows(scores, 5)
    return {
        "Q": len(q_ids), "W": W, "N": work.N, "windows": len(scores),
        "gold_rank": "" if rank is None else rank, "gold_tied": tied,
        "gold_score": "" if rank is None else f"{seg[gold]:.6f}",
        "gold_window": "" if rank is None else E.best_window_of(scores, assign, gold),
        "top5_segments": "|".join(work.block_ids[b] for b in top),
        "top5_scores": "|".join(f"{seg[b]:.6f}" for b in top),
        "raw_top5_windows": "|".join(map(str, raw)),
        "raw_top5_segments": "|".join(work.block_ids[assign[i]] for i in raw),
        "raw_top5_distinct": len({int(assign[i]) for i in raw}),
    }, scores, W


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--index", default="index")
    ap.add_argument("--works", default="acSen", help='work ID, comma list, or "all"')
    ap.add_argument("--direction", choices=E.DIRECTIONS, default="med2mod")
    ap.add_argument("--ratio", default="auto",
                    help='"auto" = whole-work length ratio, or a number')
    ap.add_argument("--conditions", default=",".join(E.CONDITIONS))
    ap.add_argument("--verify", type=int, default=20,
                    help="queries per work checked against pipeline.moving_window")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    index = load_index(args.index)
    conditions = args.conditions.split(",")
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    verified, ratios = 0, {}
    with open(out / "per_query.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for w_id in E.works_for(index, args.works):
            work = E.Work(index, w_id, args.direction)
            ratio = work.length_ratio() if args.ratio == "auto" else float(args.ratio)
            ratios[w_id] = ratio
            for n, (qid, q_ids, gold) in enumerate(work.queries()):
                for cond in conditions:
                    row, scores, W = run_query(index, work, cond, q_ids, gold, ratio)
                    if cond == "levenshtein" and n < args.verify:
                        # the package's own ranked list must equal ours
                        words = [index.words[i] for i in q_ids]
                        target = [index.words[i] for i in work.target_ids]
                        want = moving_window(words, target, W, distance="table",
                                             pruning="none", index=index,
                                             doc_ids=work.target_ids)
                        got = sorted(zip(scores.tolist(), range(len(scores))))
                        if got != want:
                            sys.exit(f"verification failed: {w_id} {qid}")
                        verified += 1
                    writer.writerow({"work": w_id, "direction": args.direction,
                                     "condition": cond, "ratio": f"{ratio:.4f}",
                                     "query_id": qid, **row})
            print(f"{w_id}: done ({time.time() - t0:.0f} s)", flush=True)

    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                            capture_output=True, text=True).stdout.strip()
    root = Path(args.index)
    (out / "run.json").write_text(json.dumps({
        "works": args.works, "direction": args.direction, "ratio": args.ratio,
        "ratios": ratios, "conditions": conditions, "step": 1, "threshold": None,
        "pruning": "none", "tie_rule": "worst-case (gold after every equal score)",
        "segment_rule": "most overlapping word positions; tie -> middle word's segment, else earlier",
        "verified_queries_against_moving_window": verified,
        "git_commit": commit, "seconds": round(time.time() - t0, 1),
        "index": {name: file_sha(root / name)
                  for name in ("vocab.json", "docs.json", "lengths.npy")},
    }, indent=2), encoding="utf-8")
    print(f"wrote {out / 'per_query.csv'}; verified {verified} queries")


if __name__ == "__main__":
    main()
