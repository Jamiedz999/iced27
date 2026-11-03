"""The optimised pipeline: precompute the distance matrix once, take per-row
sliding-window minima, and run the greedy scorer only on windows whose lower
bound passes the threshold. **The thing being optimised.**

Extracted behaviour-for-behaviour from uCeltic
`backend/apps/search/services/similarity.py`. Vocabulary (Q, N, W, D) is
defined in `common.py`.
"""

from collections import deque

from rapidfuzz.distance import Levenshtein

from .common import (
    build_hits,
    calculate_dissimilarity_score,
    tokenize_query,
    window_size_for,
)

# rapidfuzz rather than python-Levenshtein: normalized_distance(a, b) is
# Levenshtein.distance(a, b) / max(len(a), len(b)) without the manual division,
# and is markedly faster.

__all__ = ["run_search", "moving_window_similarity1"]


def run_search(
    word_array,
    query,
    *,
    anchors=None,
    window_size_ratio: float = 1.3,
    step_size: int = 1,
    dissimilarity_threshold: float = 0.5,
    top_k: int = 10,
) -> list:
    """Run a fuzzy passage search over one document.

    Returns up to `top_k` hits, best first, each a dict with the score, the
    rebuilt snippet, the half-open word range and the enclosing anchor.
    """
    word_array = word_array or []
    query_words = tokenize_query(query)
    if not query_words or not word_array:
        return []

    # The index into this list *is* the global word index in the document:
    #   article_words[0] = "Find"     (global word index 0)
    #   article_words[3] = "Find"     (global word index 3) — same word, different index
    article_words = [item["w"] for item in word_array]
    window_size = window_size_for(query_words, window_size_ratio)

    top = moving_window_similarity1(
        query_words,
        article_words,
        window_size,
        step_size,
        top_k,
        dissimilarity_threshold=dissimilarity_threshold,
    )
    return build_hits(word_array, anchors, top, window_size, top_k,
                      dissimilarity_threshold)


def moving_window_similarity1(
    target_words,
    total_words,
    actual_window_size,
    step=1,
    top_k=1,
    dissimilarity_threshold=float("inf"),
):
    """Score every window of `total_words` against `target_words`.

    Returns a list of `(score, window_start_index)` sorted best (lowest
    dissimilarity) first. `top_k` is accepted for call-site compatibility but
    does not truncate — the caller slices.
    """
    if actual_window_size > len(total_words):
        actual_window_size = len(total_words)
    if len(total_words) == 0 or actual_window_size == 0:
        return [(0, 1.0)]
    Q = len(target_words)
    N = len(total_words)
    W = actual_window_size
    last_start = N - W  # starting index of the last window

    # (1) Precompute the Q x N normalized-distance matrix once, deduping
    #     identical doc words via a per-query-word cache. This removes the
    #     ~W-times redundant recompute caused by overlapping windows.
    #     D = [
    #     [0.0, 0.25, 0.8, ...],  # distance between target_words[0] and each doc word
    #     [0.5, 0.0, 0.7, ...],   # distance between target_words[1] and each doc word
    #     ...
    # ]
    D = []
    for k in range(Q):
        cache = {}
        qk = target_words[k]
        row = []
        for w in total_words:
            d = cache.get(w)
            if d is None:
                d = Levenshtein.normalized_distance(qk, w)
                cache[w] = d
            row.append(d)
        D.append(row)

    # (2) Per-row sliding-window minimum via a monotonic deque.
    #     row_min[k][i] = min(D[k][i .. i+W-1]) for each window start i.
    row_min = [[0.0] * (last_start + 1) for _ in range(Q)]
    for k in range(Q):
        dk = D[k]
        dq = deque()  # indices, values non-decreasing from the front
        for j in range(N):
            while dq and dk[dq[-1]] >= dk[j]:
                dq.pop()
            dq.append(j)
            start = j - W + 1  # which window this position closes
            if start >= 0:
                while dq[0] < start:
                    dq.popleft()
                row_min[k][start] = dk[dq[0]]

    # (3) Per-window lower bound LB(i) = (sum_k row_min[k][i]) / Q. The greedy
    #     assignment picks distinct columns, so its score >= the sum of the
    #     per-row minima => LB is a provable lower bound. Run the (expensive)
    #     greedy only on windows whose LB <= threshold; subsample by `step`.
    best_i = None
    best_lb = float("inf")
    selected = []
    for i in range(0, last_start + 1, step):
        lb = 0.0
        for k in range(Q):
            lb += row_min[k][i]
        lb /= Q
        if lb < best_lb:
            best_lb = lb
            best_i = i
        if lb <= dissimilarity_threshold:
            selected.append(i)

    # Always keep the global-best window (smallest lower bound) as a fallback
    # so results[0] is never empty even when nothing passes the threshold.
    if not selected and best_i is not None:
        selected = [best_i]

    top_results = []
    for i in selected:
        # sub is the Q x W distance sub-matrix for window i, fed to the greedy
        # assignment below.
        sub = [[D[k][i + c] for c in range(W)] for k in range(Q)]
        dissimilarity_scores = calculate_dissimilarity_score(sub, W)
        score = sum(dissimilarity_scores) / Q
        top_results.append((score, i))
    return sorted(top_results)

