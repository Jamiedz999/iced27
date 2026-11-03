"""One configurable matcher for ablation: every optimisation is a stage
option, chosen by name, so configurations differ in exactly the stages they
name and nothing else. `configs.py` lists the configurations to compare.

Stages:

    distance  how the Q x N distance matrix D is filled
              "compute"  rapidfuzz, once per distinct (query word, doc word)
              "table"    look up the precomputed V x V table (`vocab.py`);
                         words missing from the table fall back to compute
    pruning   which windows get the (expensive) greedy scorer
              "none"         every window on the step grid
              "lower_bound"  only windows whose lower bound passes the
                             threshold (sliding-window row minima)

Words are compared case-insensitively: query and document words are
lowercased on entry, as the vocabulary table is. `naive.py` and
`optimized.py` are left case-sensitive; compare against them on lowercased
input.

Vocabulary (Q, N, W, D) is defined in `common.py`.
"""

from collections import deque

import numpy as np
from rapidfuzz.distance import Levenshtein

from .common import calculate_dissimilarity_score

__all__ = ["DISTANCES", "PRUNINGS", "moving_window"]


# ---- Stage 1: distance matrix ---------------------------------------------


def compute_matrix(query_words, doc_words, **_):
    """D[k][j] by rapidfuzz, caching repeated doc words per query word."""
    D = []
    for qk in query_words:
        cache = {}
        row = []
        for w in doc_words:
            d = cache.get(w)
            if d is None:
                d = Levenshtein.normalized_distance(qk, w)
                cache[w] = d
            row.append(d)
        D.append(row)
    return D


def table_matrix(query_words, doc_words, *, index, doc_ids=None, **_):
    """D[k][j] by lookup in `index` (a `vocab.VocabIndex`).

    `doc_ids` is the document already mapped to word IDs (as `docs.json`
    stores it); without it the words are mapped here. Words the table does
    not know get a local ID past the table's end and are computed.
    """
    if index is None:
        raise ValueError('distance="table" needs an index')
    V = len(index.words)
    unknown = {}  # word -> local ID >= V

    def to_id(w):
        i = index.ids.get(w)
        if i is None:
            i = unknown.setdefault(w, V + len(unknown))
        return i

    q_ids = np.array([to_id(w) for w in query_words], dtype=np.int64)
    if doc_ids is None:
        d_ids = np.array([to_id(w) for w in doc_words], dtype=np.int64)
    else:
        d_ids = np.asarray(doc_ids, dtype=np.int64)
    cols, inverse = np.unique(d_ids, return_inverse=True)

    M = np.empty((len(q_ids), len(cols)), dtype=np.float64)
    known_q = q_ids < V
    known_c = cols < V
    if known_q.any() and known_c.any():
        qk, ck = q_ids[known_q], cols[known_c]
        longest = np.maximum.outer(index.lengths[qk], index.lengths[ck])
        M[np.ix_(known_q, known_c)] = index.distances[np.ix_(qk, ck)] / longest

    if not (known_q.all() and known_c.all()):
        words_by_id = {i: w for w, i in unknown.items()}

        def word(i):
            return index.words[i] if i < V else words_by_id[i]

        for k, qi in enumerate(q_ids):
            for c, ci in enumerate(cols):
                if not (known_q[k] and known_c[c]):
                    M[k, c] = Levenshtein.normalized_distance(word(qi), word(ci))

    return M[:, inverse].tolist()


DISTANCES = {
    "compute": compute_matrix,
    "table": table_matrix,
}


# ---- Stage 2: which windows to score --------------------------------------


def _greedy_score(D, i, Q, W):
    sub = [[D[k][i + c] for c in range(W)] for k in range(Q)]
    return sum(calculate_dissimilarity_score(sub, W)) / Q


def score_all(D, Q, N, W, step, dissimilarity_threshold):
    """Greedy-score every window on the step grid."""
    return sorted((_greedy_score(D, i, Q, W), i)
                  for i in range(0, N - W + 1, step))


def score_lower_bound(D, Q, N, W, step, dissimilarity_threshold):
    """Greedy-score only windows whose lower bound passes the threshold.

    LB(i) = (sum_k min(D[k][i .. i+W-1])) / Q, the row minima taken with a
    monotonic deque. When nothing passes, the window with the smallest bound
    is scored so the result is never empty.
    """
    last_start = N - W
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
    if not selected and best_i is not None:
        selected = [best_i]

    return sorted((_greedy_score(D, i, Q, W), i) for i in selected)


PRUNINGS = {
    "none": score_all,
    "lower_bound": score_lower_bound,
}


# ---- The matcher ----------------------------------------------------------


def moving_window(
    query_words,
    doc_words,
    window_size,
    step=1,
    dissimilarity_threshold=float("inf"),
    *,
    distance,
    pruning,
    index=None,
    doc_ids=None,
):
    """Score windows of `doc_words` against `query_words` with the named
    stage options; returns `(score, window_start)` pairs, best first.

    `distance` and `pruning` come from a configuration in `configs.py`;
    `index` and `doc_ids` are what the "table" option looks up.
    """
    query_words = [w.lower() for w in query_words]
    doc_words = [w.lower() for w in doc_words]
    Q, N = len(query_words), len(doc_words)
    W = min(window_size, N)
    if N == 0 or W == 0:
        return [(0, 1.0)]

    D = DISTANCES[distance](query_words, doc_words,
                            index=index, doc_ids=doc_ids)
    return PRUNINGS[pruning](D, Q, N, W, step, dissimilarity_threshold)
