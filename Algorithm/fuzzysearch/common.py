"""Shared pieces of the fuzzy passage search, used by both pipelines
(`naive.py` and `optimized.py`).

Extracted from uCeltic `backend/apps/search/services/similarity.py` and
`run_search.py`, with the Django ORM lookup replaced by plain arguments.
Nothing here knows about Django, HTTP or TEI.

The first half is the algorithm's definition; the second half is the
engineering layer that turns scored windows back into readable hits.

Vocabulary used throughout:

    Q  number of query words
    N  number of document words
    W  window size (words), = max(1, int(Q * window_size_ratio))
    D  the Q x N matrix of normalized Levenshtein distances

A *score* is a dissimilarity in [0, 1]: 0 means identical, 1 means nothing
in common.

The definitions are shared, not tuned: the naive pipeline is the oracle and
must keep scoring with exactly this code. To speed one of them up, write the
fast version in `optimized.py` and let the differential test prove it matches.
"""

import re

_QUERY_WORD_RE = re.compile(r"\w+", re.UNICODE)

__all__ = [
    "tokenize_query",
    "window_size_for",
    "calculate_dissimilarity_score",
    "build_hits",
]


# ---- Algorithm definition -------------------------------------------------


def tokenize_query(query):
    """Split a free-text query into the words the matcher compares."""
    return _QUERY_WORD_RE.findall(query)


def window_size_for(query_words, window_size_ratio):
    """W = max(1, int(Q * ratio)); the headroom lets a match absorb inserts."""
    return max(1, int(len(query_words) * window_size_ratio))


def calculate_dissimilarity_score(matrix, actual_window_size):
    """Greedy pairing: repeatedly take the global minimum, then strike out its
    row and column so each query word is matched to a distinct doc word.

    Mutates `matrix` in place.
    """
    results = []
    for _ in range(len(matrix)):
        current_min_val = float("inf")
        min_row, min_col = -1, -1
        for r in range(len(matrix)):
            for c in range(actual_window_size):
                if matrix[r][c] < current_min_val:
                    current_min_val = matrix[r][c]
                    min_row = r
                    min_col = c
        if min_row == -1:
            break
        results.append(current_min_val)

        # Mark the row and column used; they take no part in later rounds.
        for c in range(actual_window_size):
            matrix[min_row][c] = float("inf")
        for r in range(len(matrix)):
            matrix[r][min_col] = float("inf")
    return results


# ---- Engineering layer: scored windows -> readable hits -------------------
#
# Document shape (unchanged from uCeltic's TEI index):
#
#     word_array  [{"w": "talam", "sep": " ", "a": "anchor-3"}, ...]
#     anchors     [{"id": "anchor-3", "tag": "l", "line_no": 1}, ...]
#
# `sep` is what the source has *between* this word and the next. An empty
# separator means the source has nothing there and the snippet must say so —
# inventing a space is the #145 defect.


def build_hits(word_array, anchors, top, window_size, top_k,
               dissimilarity_threshold):
    """Turn sorted `(score, window_start)` pairs into up to `top_k` hits, each
    a dict with the score, the rebuilt snippet, the half-open word range and
    the enclosing anchor.
    """
    anchors_by_id = {a["id"]: a for a in (anchors or [])}

    results = []
    for score, word_idx in top[:top_k]:
        if score > dissimilarity_threshold:
            continue

        word_end = min(word_idx + window_size, len(word_array))

        snippet = "".join(
            word_array[i]["w"] + word_array[i].get("sep", "")
            for i in range(word_idx, word_end)
        ).strip()

        anchor = anchors_by_id.get(word_array[word_idx].get("a"))
        results.append({
            "score": score,
            "snippet": snippet,
            "word_start": word_idx,
            "word_end": word_end,
            "anchor_id": anchor["id"] if anchor else None,
            "anchor_tag": anchor["tag"] if anchor else None,
            "line_no": anchor.get("line_no") if anchor else None,
        })
    return results
