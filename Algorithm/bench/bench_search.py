"""Ablation benchmark: times every configuration in `fuzzysearch.configs`
against the naive scan, on a real text from the corpus index.

The document is one variety of one corpus text (default: the modern text of
the longest document); each query is a run of Q words from the *other*
variety of the same text, so every search is a cross-variety one. Every
configuration gets the same queries, window ratio, threshold and step.

Build the index first, then run by hand:

    python -m fuzzysearch.vocab corpus index
    python bench/bench_search.py
    python bench/bench_search.py --doc acSen --queries 8,16,32 --repeat 3

The naive scan is never optimised, so its time is a stable yardstick across
every optimisation round.
"""

import argparse
import random
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fuzzysearch.configs import CONFIGS  # noqa: E402
from fuzzysearch.naive import full_scan  # noqa: E402
from fuzzysearch.pipeline import moving_window  # noqa: E402
from fuzzysearch.vocab import load_index  # noqa: E402

SEED = 42
QUERY_SIZES = (8, 16)
STEP = 1
THRESHOLD = 0.5           # run_search's default interactive threshold
WINDOW_RATIO = 1.3        # matches run_search's window_size_ratio
VARIETIES = ("medieval", "modern")


def timed(fn, repeat):
    """Best of `repeat` runs — the least noisy estimate of the true cost."""
    best = float("inf")
    result = None
    for _ in range(repeat):
        start = time.perf_counter()
        result = fn()
        best = min(best, time.perf_counter() - start)
    return best, result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", default="index", help="index directory")
    parser.add_argument("--doc", help="document id (default: the longest)")
    parser.add_argument("--target", choices=VARIETIES, default="modern",
                        help="variety searched in; queries come from the other")
    parser.add_argument("--queries", default=",".join(str(q) for q in QUERY_SIZES),
                        help="comma-separated query word counts")
    parser.add_argument("--step", type=int, default=STEP)
    parser.add_argument("--threshold", type=float, default=THRESHOLD)
    parser.add_argument("--repeat", type=int, default=1, help="runs per measurement")
    parser.add_argument("--skip-naive", action="store_true",
                        help="time only the configurations")
    args = parser.parse_args()

    load_t, index = timed(lambda: load_index(args.index), 1)
    source = VARIETIES[1 - VARIETIES.index(args.target)]
    doc_id = args.doc or max(index.docs,
                             key=lambda d: len(index.docs[d][args.target]["ids"]))
    doc_ids = index.docs[doc_id][args.target]["ids"]
    doc_words = [index.words[i] for i in doc_ids]
    source_ids = index.docs[doc_id][source]["ids"]

    query_sizes = [int(q) for q in args.queries.split(",") if q]
    rng = random.Random(SEED)
    print(f"doc={doc_id} ({args.target}, N={len(doc_words)}), queries from "
          f"{source}, step={args.step}, threshold={args.threshold}, "
          f"repeat={args.repeat}, seed={SEED}, index load {load_t * 1000:.0f} ms\n")

    names = list(CONFIGS)
    reference = "baseline" if args.skip_naive else "naive"
    print(f"{'Q':>3} {'W':>3}  {'config':<18} {'time':>10}  "
          f"{'vs ' + reference:>11}  best_idx_match")
    for q in query_sizes:
        start = rng.randint(0, len(source_ids) - q)
        query = [index.words[i] for i in source_ids[start:start + q]]
        window = max(1, int(q * WINDOW_RATIO))

        rows = {}
        if not args.skip_naive:
            rows["naive"] = timed(
                lambda: full_scan(query, doc_words, window, args.step), args.repeat)
        for name in names:
            rows[name] = timed(
                lambda: moving_window(query, doc_words, window, args.step,
                                      args.threshold, index=index,
                                      doc_ids=doc_ids, **CONFIGS[name]),
                args.repeat)

        ref_t, ref_r = rows[reference]
        for name, (t, r) in rows.items():
            speedup = ref_t / t if t else float("inf")
            print(f"{q:>3} {window:>3}  {name:<18} {t * 1000:8.1f} ms  "
                  f"{speedup:10.1f}x  {r[0][1] == ref_r[0][1]}")
        print()


if __name__ == "__main__":
    main()
