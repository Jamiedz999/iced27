"""The naive pipeline: rebuild the Q x W distance matrix for every window and
score it. No caching, no prefilter, no pruning.

This is the pre-optimisation uCeltic behaviour, kept as the oracle every
optimisation is measured and checked against — the benchmark times it and the
differential test compares against it. Never make this one faster.
"""

from rapidfuzz.distance import Levenshtein

from .common import (
    build_hits,
    calculate_dissimilarity_score,
    tokenize_query,
    window_size_for,
)

__all__ = ["run_search", "full_scan"]


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
    """Run a fuzzy passage search over one document with the naive scan.

    Same signature and output as `optimized.run_search`.
    """
    word_array = word_array or []
    query_words = tokenize_query(query)
    if not query_words or not word_array:
        return []

    article_words = [item["w"] for item in word_array]
    window_size = window_size_for(query_words, window_size_ratio)
    top = full_scan(query_words, article_words, window_size, step_size)
    return build_hits(word_array, anchors, top, window_size, top_k,
                      dissimilarity_threshold)


def full_scan(target_words, total_words, actual_window_size, step=1):
    """Score every window on the step grid, best first."""
    if actual_window_size > len(total_words):
        actual_window_size = len(total_words)
    if not total_words or actual_window_size == 0:
        return [(0, 1.0)]

    W = actual_window_size
    Q = len(target_words)
    results = []
    for i in range(0, len(total_words) - W + 1, step):
        src = total_words[i:i + W]
        matrix = [[Levenshtein.normalized_distance(t, s) for s in src]
                  for t in target_words]
        scores = calculate_dissimilarity_score(matrix, W)
        results.append((sum(scores) / Q, i))
    return sorted(results)
