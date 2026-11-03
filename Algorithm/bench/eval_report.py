"""Human-readable traces of a Recall@N run, for checking it by eye.

    python bench/eval_report.py bench/results/acSen

Writes to the run directory:

    examples/*.md  four queries worked through step by step: the distance
                   matrix of a window, each greedy pairing step, the score,
                   and the top distinct segments in both conditions
    samples.md     20 random queries (fixed seed), one line each
    misses.md      every query whose gold is not in the top 5 (levenshtein)
"""

import csv
import json
import random
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import eval_lib as E  # noqa: E402
from fuzzysearch.vocab import load_index  # noqa: E402

SAMPLE_SEED = 42
SAMPLES = 20
MAX_MISSES = 300


def esc(text):
    return text.replace("|", "\\|")


class Search:
    """One query re-run in one condition, keeping everything for display."""

    def __init__(self, index, work, condition, qid, ratio):
        self.index, self.work, self.condition = index, work, condition
        b = next(x for x in work.query_blocks if x["id"] == qid)
        self.q_ids = work.query_ids[b["start"]:b["end"]]
        self.gold = work.block_pos[qid]
        self.W = E.window_size(len(self.q_ids), ratio, work.N)
        self.D = E.distance_matrix(condition, index, self.q_ids, work.target_ids)
        self.scores = E.greedy_all_windows(self.D, self.W)
        self.assign = work.assignment(self.W)
        self.seg = E.segment_scores(self.scores, self.assign, len(work.block_ids))
        self.rank, self.tied = E.gold_rank(self.seg, self.gold)

    def words(self, start, end):
        return [self.index.words[i] for i in self.work.target_ids[start:end]]

    def overlap(self, start, segment):
        s, e = self.work.block_start[segment], self.work.block_end[segment]
        return max(0, min(e, start + self.W) - max(s, start))

    def top_table(self, k=5):
        L = ["| Rank shown | Score | Segment | Best window (word positions) | Words in the window | Words of the window in this segment | Gold? |",
             "|---:|---:|---|---|---|---:|:---:|"]
        for n, b in enumerate(E.top_segments(self.seg, k), 1):
            w = E.best_window_of(self.scores, self.assign, b)
            L.append(f"| {n} | {self.seg[b]:.4f} | {self.work.block_ids[b]} | "
                     f"{w}–{w + self.W - 1} | {esc(' '.join(self.words(w, w + self.W)))} | "
                     f"{self.overlap(w, b)} / {self.W} | {'✅' if b == self.gold else ''} |")
        return L

    def outcome(self):
        if self.rank is None:
            return "gold segment never ranked (no window counts as it)"
        tie = f", tied with {self.tied} other segment(s)" if self.tied else ""
        return f"gold segment rank {self.rank} (worst case{tie})"

    def window_trace(self, start, title):
        qw = [self.index.words[i] for i in self.q_ids]
        ww = self.words(start, start + self.W)
        block = self.D[:, start:start + self.W]
        steps, score = E.greedy_trace(block)
        picked = {(r, c) for r, c, _ in steps}
        L = [f"### {title}: window {start}–{start + self.W - 1}", "",
             "Distance matrix D for this window (rows: query words, columns: window "
             "words; 0 = identical, 1 = nothing in common). **Bold** cells are the pairs "
             "the greedy step picks.", "",
             "| query \\ window | " + " | ".join(f"{esc(w)} ({start + j})" for j, w in enumerate(ww)) + " |",
             "|---|" + "---:|" * len(ww)]
        for r, q in enumerate(qw):
            cells = [(f"**{block[r, c]:.2f}**" if (r, c) in picked else f"{block[r, c]:.2f}")
                     for c in range(len(ww))]
            L.append(f"| {esc(q)} | " + " | ".join(cells) + " |")
        L += ["", "Greedy pairing (repeatedly take the smallest remaining value, then strike "
              "out its row and column):", ""]
        for n, (r, c, v) in enumerate(steps, 1):
            L.append(f"{n}. `{qw[r]}` ↔ `{ww[c]}` = {v:.4f}")
        total = sum(v for _, _, v in steps)
        L += ["", f"Score = sum / Q = {total:.4f} / {len(qw)} = **{score:.4f}** "
              f"(the run recorded {self.scores[start]:.4f} for this window).", ""]
        return L


def example(index, texts, work, ratio, row, label):
    qid = row["query_id"]
    lev = Search(index, work, "levenshtein", qid, ratio)
    exa = Search(index, work, "exact", qid, ratio)
    main = lev if row["condition"] == "levenshtein" else exa
    t = texts[work.id][qid]
    g = work.block_ids.index(qid)
    gs, ge = int(work.block_start[g]), int(work.block_end[g])
    L = [f"# Example: {label}", "",
         f"Work `{work.id}`, segment `{qid}`, shown condition **{main.condition}**.", "",
         "## Inputs", "",
         f"- Query ({work.source}, original): {t[work.source]}",
         f"- Query words (lowercase `\\w+`), Q = {len(main.q_ids)}: "
         f"`{' '.join(index.words[i] for i in main.q_ids)}`",
         f"- Gold answer ({work.target}, original): {t[work.target]}",
         f"- Gold words: positions {gs}–{ge - 1} of {work.N}: `{' '.join(main.words(gs, ge))}`",
         f"- Window: W = int(Q × ratio) = int({len(main.q_ids)} × {ratio:.3f}) = {main.W}; "
         f"{len(main.scores)} windows scored", "",
         f"## Result: {main.outcome()}", ""]
    if main.rank is not None:
        gw = E.best_window_of(main.scores, main.assign, main.gold)
        L += main.window_trace(gw, "Best window of the gold segment")
    top = E.top_segments(main.seg, 1)
    if top and top[0] != main.gold:
        L += main.window_trace(E.best_window_of(main.scores, main.assign, top[0]),
                               f"Best window overall (segment {work.block_ids[top[0]]})")
    L += [f"## Top distinct segments, {main.condition}", ""] + main.top_table() + [""]
    other = exa if main is lev else lev
    L += [f"## Same query, {other.condition}: {other.outcome()}", ""] + other.top_table() + [""]
    L += ["Ranks shown here list tied segments in text order; the recorded rank puts "
          "the gold after all of its ties.", ""]
    return "\n".join(L)


def pick_examples(rows):
    """(label, row) for: rank 1, rank 2-5, a miss, a tie that decides the outcome."""
    lev = [r for r in rows if r["condition"] == "levenshtein"]
    exa = [r for r in rows if r["condition"] == "exact"]
    readable = lambda r: 5 <= int(r["Q"]) <= 8  # noqa: E731
    rank = lambda r: int(r["gold_rank"]) if r["gold_rank"] else None  # noqa: E731

    used = set()

    def first(cands):
        cands = [r for r in cands if r["query_id"] not in used]
        r = next((r for r in cands if readable(r)), cands[0] if cands else None)
        if r:
            used.add(r["query_id"])
        return r

    picks = [
        ("found at rank 1", first([r for r in lev if rank(r) == 1 and r["gold_tied"] == "0"])),
        ("found at rank 2-5", first([r for r in lev if rank(r) and 2 <= rank(r) <= 5])),
        ("not found in the top 5", first([r for r in lev if not rank(r) or rank(r) > 5])),
        ("a tie decides the outcome (exact match)",
         first([r for r in exa if rank(r) and rank(r) > 5 and rank(r) - int(r["gold_tied"]) <= 5])),
    ]
    return [(label, r) for label, r in picks if r]


def main(run_dir, index_dir="index", corpus_dir="../corpus"):
    run_dir = Path(run_dir)
    run = json.loads((run_dir / "run.json").read_text())
    rows = list(csv.DictReader(open(run_dir / "per_query.csv", encoding="utf-8")))
    index = load_index(index_dir)
    texts = E.load_texts(corpus_dir)
    works = {}

    def work_of(w):
        if w not in works:
            works[w] = E.Work(index, w, run["direction"])
        return works[w]

    ex_dir = run_dir / "examples"
    ex_dir.mkdir(exist_ok=True)
    for n, (label, row) in enumerate(pick_examples(rows), 1):
        w = work_of(row["work"])
        md = example(index, texts, w, run["ratios"][row["work"]], row, label)
        (ex_dir / f"{n}_{row['query_id']}.md").write_text(md, encoding="utf-8")

    by_key = {(r["work"], r["query_id"], r["condition"]): r for r in rows}
    lev = [r for r in rows if r["condition"] == "levenshtein"]
    src, tgt = E.DIRECTIONS[run["direction"]]

    def top1_words(r):
        w = work_of(r["work"])
        if not r["raw_top5_windows"]:
            return ""
        start = int(r["raw_top5_windows"].split("|")[0])
        return " ".join(index.words[i] for i in w.target_ids[start:start + int(r["W"])])

    def rank_txt(r):
        if not r["gold_rank"]:
            return "never"
        return r["gold_rank"] + (f" (tied {r['gold_tied']})" if r["gold_tied"] != "0" else "")

    sample = random.Random(SAMPLE_SEED).sample(lev, min(SAMPLES, len(lev)))
    L = [f"# {len(sample)} random queries (seed {SAMPLE_SEED})", "",
         "Top-1 window = the package's best-scoring window, lowercase words as compared.", "",
         "| Segment | Q | Query (" + src + ") | Gold (" + tgt + ") | Top-1 window (levenshtein) | Rank: levenshtein | Rank: exact |",
         "|---|---:|---|---|---|---:|---:|"]
    for r in sample:
        t = texts[r["work"]][r["query_id"]]
        e = by_key.get((r["work"], r["query_id"], "exact"))
        L.append(f"| {r['query_id']} | {r['Q']} | {esc(t[src])} | {esc(t[tgt])} | "
                 f"{esc(top1_words(r))} | {rank_txt(r)} | {rank_txt(e) if e else ''} |")
    (run_dir / "samples.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    misses = [r for r in lev if not r["gold_rank"] or int(r["gold_rank"]) > 5]
    L = [f"# Queries not found in the top 5 (levenshtein): {len(misses)} of {len(lev)}", "",
         "Read each row and ask: is the gold alignment right? Is the top-1 window a "
         "genuinely similar passage (a repeated formula, say)? Or is it noise?", ""]
    if len(misses) > MAX_MISSES:
        L += [f"Showing the first {MAX_MISSES}; all are in `per_query.csv`.", ""]
    L += ["| Segment | Q | Query (" + src + ") | Gold (" + tgt + ") | Gold score / rank | Top-1 segment | Top-1 score | Top-1 window |",
          "|---|---:|---|---|---|---|---:|---|"]
    for r in misses[:MAX_MISSES]:
        t = texts[r["work"]][r["query_id"]]
        top_seg = r["top5_segments"].split("|")[0] if r["top5_segments"] else ""
        top_sc = r["top5_scores"].split("|")[0] if r["top5_scores"] else ""
        gold = f"{float(r['gold_score']):.4f} / {rank_txt(r)}" if r["gold_score"] else "never ranked"
        L.append(f"| {r['query_id']} | {r['Q']} | {esc(t[src])} | {esc(t[tgt])} | {gold} | "
                 f"{top_seg} | {float(top_sc):.4f} | {esc(top1_words(r))} |")
    (run_dir / "misses.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"wrote examples/ ({len(list(ex_dir.glob('*.md')))}), samples.md, misses.md "
          f"({len(misses)} misses) in {run_dir}")


if __name__ == "__main__":
    main(sys.argv[1])
