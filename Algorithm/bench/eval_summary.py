"""Summarise a Recall@N run into `summary.md` (and `summary.json`).

    python bench/eval_summary.py bench/results/acSen

Every percentage is printed with its numerator and denominator.
"""

import csv
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

KS = (1, 3, 5)
BANDS = ((1, 4), (5, 8), (9, 14), (15, 10**9))


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return (max(0.0, centre - half), min(1.0, centre + half))


def mcnemar_exact(b, c):
    """Two-sided exact McNemar p-value from the discordant counts b and c."""
    n = b + c
    if n == 0:
        return 1.0
    tail = sum(math.comb(n, i) for i in range(min(b, c) + 1)) / 2 ** n
    return min(1.0, 2 * tail)


def rank_of(row):
    return int(row["gold_rank"]) if row["gold_rank"] else None


def hit(row, k):
    r = rank_of(row)
    return r is not None and r <= k


def frac(k, n):
    return f"{k} / {n} = {k / n:.1%}" if n else "–"


def band(q):
    for lo, hi in BANDS:
        if lo <= q <= hi:
            return f"{lo}+" if hi >= 10**9 else f"{lo}–{hi}"


def main(run_dir):
    run_dir = Path(run_dir)
    rows = list(csv.DictReader(open(run_dir / "per_query.csv", encoding="utf-8")))
    run = json.loads((run_dir / "run.json").read_text())
    conds = run["conditions"]
    by = defaultdict(list)
    for r in rows:
        by[r["condition"]].append(r)
    n = len(by[conds[0]])
    res = {"queries": n, "conditions": {}}

    L = [f"# Recall@N results: {run['works']} ({run['direction']})", "",
         f"{n} queries per condition. Window W = int(Q × ratio), ratio "
         f"{run['ratio']} ({', '.join(f'{w} {v:.3f}' for w, v in list(run['ratios'].items())[:3])}"
         f"{', …' if len(run['ratios']) > 3 else ''}); step 1; no threshold; every window scored.", "",
         "**How a query is scored.** Every window gets the matcher's score (lower = more "
         "similar). Each window counts as the segment it shares the most word positions "
         "with; a segment's score is its best window's score. The gold segment's rank is "
         "the number of distinct segments whose score is **≤** the gold's score, so the "
         "gold is placed after every segment it ties with (worst case). "
         "Recall@k = queries with rank ≤ k / all queries. "
         "MRR = mean of 1 / rank (0 when the gold is never ranked).", "",
         "## Main results", "",
         "| Condition | " + " | ".join(f"Recall@{k} (95% CI)" for k in KS) + " | MRR |",
         "|---|" + "---|" * (len(KS) + 1)]
    for c in conds:
        R = by[c]
        cells, cres = [], {}
        for k in KS:
            h = sum(hit(r, k) for r in R)
            lo, hi = wilson(h, len(R))
            cells.append(f"{frac(h, len(R))} ({lo:.1%}–{hi:.1%})")
            cres[f"recall@{k}"] = {"hits": h, "n": len(R), "ci95": [lo, hi]}
        mrr = sum(1 / rank_of(r) for r in R if rank_of(r)) / len(R)
        cres["mrr"] = mrr
        res["conditions"][c] = cres
        L.append(f"| {c} | " + " | ".join(cells) + f" | {mrr:.3f} |")
    L.append("")

    if len(conds) == 2:
        a, b = conds
        pair = {r["work"] + r["query_id"]: r for r in by[b]}
        L += [f"## Paired comparison: {a} vs {b} (exact McNemar test)", "",
              f"| k | both hit | only {a} | only {b} | neither | p |", "|---|---:|---:|---:|---:|---:|"]
        for k in (1, 5):
            cnt = Counter((hit(r, k), hit(pair[r["work"] + r["query_id"]], k)) for r in by[a])
            p = mcnemar_exact(cnt[(True, False)], cnt[(False, True)])
            L.append(f"| {k} | {cnt[(True, True)]} | {cnt[(True, False)]} | "
                     f"{cnt[(False, True)]} | {cnt[(False, False)]} | {p:.2g} |")
        L.append("")

    L += ["## Recall@5 by query length (words)", "",
          "| Length | " + " | ".join(conds) + " |", "|---|" + "---:|" * len(conds)]
    for lo, hi in BANDS:
        name = f"{lo}+" if hi >= 10**9 else f"{lo}–{hi}"
        cells = []
        for c in conds:
            R = [r for r in by[c] if band(int(r["Q"])) == name]
            cells.append(frac(sum(hit(r, 5) for r in R), len(R)))
        L.append(f"| {name} | " + " | ".join(cells) + " |")
    L.append("")

    L += ["## Ties and unreachable answers", "",
          "| Condition | Queries whose gold ties with other segments | Ties that turn a Recall@5 hit into a miss | Ties that turn a Recall@1 hit into a miss | Recall@1 / @5 with ties in random order (expected) | Recall@5 if gold were first among its ties | Gold never ranked |",
          "|---|---:|---:|---:|---:|---:|---:|"]
    for c in conds:
        R = by[c]
        tied = sum(int(r["gold_tied"]) > 0 for r in R)
        lost = {k: sum(1 for r in R if rank_of(r) and rank_of(r) > k
                       and rank_of(r) - int(r["gold_tied"]) <= k) for k in (5, 1)}
        unreach = sum(rank_of(r) is None for r in R)
        best5 = sum(1 for r in R if rank_of(r) and rank_of(r) - int(r["gold_tied"]) <= 5)
        expected = {k: sum(min(1.0, max(0.0, (k - rank_of(r) + int(r["gold_tied"]) + 1)
                                       / (int(r["gold_tied"]) + 1)))
                           for r in R if rank_of(r)) / len(R) for k in (1, 5)}
        L.append(f"| {c} | {frac(tied, len(R))} | {frac(lost[5], len(R))} | "
                 f"{frac(lost[1], len(R))} | {expected[1]:.1%} / {expected[5]:.1%} | "
                 f"{frac(best5, len(R))} | {frac(unreach, len(R))} |")
    L += ["", "\"Turns a hit into a miss\": the gold would be within the top k if it were "
          "placed first among its ties, but is beyond k under the worst-case rule. "
          "The expected column orders each query's ties at random: the gold is equally "
          "likely to take any position among them. The best-case column is an upper bound "
          "(an oracle that always puts the gold first); with the worst case it brackets "
          "every tie-breaking order. "
          "\"Gold never ranked\": no window counts as the gold segment (it is too short "
          "to be the majority of any window).", ""]

    c0 = conds[0]
    dist = Counter(int(r["raw_top5_distinct"]) for r in by[c0])
    raw_hit = sum(r["query_id"] in r["raw_top5_segments"].split("|") for r in by[c0])
    L += [f"## The raw top-5 list (what the package returns), {c0}", "",
          "Overlapping windows mean the package's own top 5 often repeats one place.", "",
          "| Distinct segments among the raw top-5 windows | Queries |", "|---:|---:|"]
    L += [f"| {d} | {frac(dist[d], len(by[c0]))} |" for d in sorted(dist)]
    L += ["", f"Gold segment among the raw top-5 windows: {frac(raw_hit, len(by[c0]))} "
          f"(compare Recall@5 over distinct segments above).", ""]

    works = sorted({r["work"] for r in rows})
    if len(works) > 1:
        L += ["## Per work", "", "| Work | Queries | " + " | ".join(
            f"{c} R@1 | {c} R@5" for c in conds) + " |",
              "|---|---:|" + "---:|" * (2 * len(conds))]
        for w in works:
            cells = []
            for c in conds:
                R = [r for r in by[c] if r["work"] == w]
                cells += [f"{sum(hit(r, 1) for r in R) / len(R):.2f}",
                          f"{sum(hit(r, 5) for r in R) / len(R):.2f}"]
            L.append(f"| {w} | {sum(r['work'] == w for r in by[c0])} | " + " | ".join(cells) + " |")
        L.append("")

    L += ["## Run", "", f"- git commit `{run['git_commit']}`, {run['seconds']} s",
          f"- {run['verified_queries_against_moving_window']} queries checked: the full ranked "
          "window list equals `pipeline.moving_window(..., pruning=\"none\")`",
          f"- index hashes: {run['index']}", ""]
    (run_dir / "summary.md").write_text("\n".join(L), encoding="utf-8")
    (run_dir / "summary.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    print(f"wrote {run_dir / 'summary.md'}")


if __name__ == "__main__":
    main(sys.argv[1])
