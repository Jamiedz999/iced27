"""Shared pieces of the retrieval-effectiveness (Recall@N) experiment.

Task: each aligned segment of one variety of a work is a query, searched
in the full text of the other variety. The search is the package matcher
(`pipeline.moving_window` with no pruning and no threshold): every window
of W words is scored, and the gold answer is the aligned segment of the
other variety.

Two conditions differ only in how D is filled:

    levenshtein  normalized Levenshtein distance (`pipeline.table_matrix`)
    exact        0 if the two words are identical, else 1 (the baseline)

Ranking works on distinct segments, not on windows. A window counts as
the segment it shares the most word positions with (a tie goes to the
segment holding the window's middle word, else to the earlier segment); a
segment's score is its best window's score. The gold segment's rank is
worst-case: it is placed after every other segment with the same score.

Vocabulary: Q query words, N target words, W window length (as in
`common.py`).
"""

import json
from pathlib import Path

import numpy as np

from fuzzysearch.common import calculate_dissimilarity_score
from fuzzysearch.pipeline import table_matrix
from fuzzysearch.vocab import VARIETIES, tokenize

DIRECTIONS = {
    "med2mod": ("medieval", "modern"),
    "mod2med": ("modern", "medieval"),
    "med2med": ("medieval", "medieval"),  # self-search sanity check
}
CONDITIONS = ("levenshtein", "exact")

# Same text under two file names; keep the first, skip the other.
DUPLICATE_WORKS = {"aidedCho": "aidedChonch"}


# ---- Data -------------------------------------------------------------------


class Work:
    """One work in one search direction: queries and the target text."""

    def __init__(self, index, work_id, direction):
        source, target = DIRECTIONS[direction]
        doc = index.docs[work_id]
        self.id = work_id
        self.direction = direction
        self.source, self.target = source, target
        self.query_ids = doc[source]["ids"]
        self.query_blocks = doc[source]["blocks"]
        self.target_ids = np.asarray(doc[target]["ids"], dtype=np.int64)
        blocks = doc[target]["blocks"]
        self.block_ids = [b["id"] for b in blocks]
        self.block_pos = {b["id"]: k for k, b in enumerate(blocks)}
        self.block_start = np.array([b["start"] for b in blocks], dtype=np.int64)
        self.block_end = np.array([b["end"] for b in blocks], dtype=np.int64)
        self._assign_cache = {}

    @property
    def N(self):
        return len(self.target_ids)

    def length_ratio(self):
        """Target tokens / source tokens over the whole work; uses no alignment."""
        return self.N / max(1, len(self.query_ids))

    def queries(self):
        """(segment id, query word IDs, gold segment position) per non-empty query."""
        for b in self.query_blocks:
            q = self.query_ids[b["start"]:b["end"]]
            if q:
                yield b["id"], q, self.block_pos[b["id"]]

    def assignment(self, W):
        """Segment position of every window start for window length W (cached)."""
        if W not in self._assign_cache:
            self._assign_cache[W] = assign_windows(
                self.N, W, self.block_start, self.block_end)
        return self._assign_cache[W]


def works_for(index, which):
    """Work IDs to run: one ID, a comma list, or "all" (duplicates removed)."""
    if which == "all":
        return [w for w in sorted(index.docs) if w not in DUPLICATE_WORKS]
    return which.split(",")


def load_texts(corpus_dir):
    """{work: {segment id: {variety: original cleaned text}}} for reports."""
    texts = {}
    for path in sorted(Path(corpus_dir).glob("*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        texts[doc.get("id") or path.stem] = {
            b["id"]: {name: b.get(field) or "" for name, (field, _) in VARIETIES.items()}
            for b in doc.get("blocks") or []
        }
    return texts


# ---- Distances and window scores -------------------------------------------


def distance_matrix(condition, index, q_ids, target_ids):
    """Q x N matrix D for one condition."""
    q = np.asarray(q_ids, dtype=np.int64)
    if condition == "exact":
        return (q[:, None] != target_ids[None, :]).astype(np.float64)
    if condition == "levenshtein":
        words = [index.words[i] for i in q_ids]
        return np.array(table_matrix(words, None, index=index,
                                     doc_ids=target_ids))
    raise ValueError(f"unknown condition {condition!r}")


def window_size(Q, ratio, N):
    """W = max(1, int(Q * ratio)) as in `common.window_size_for`, capped at N."""
    return min(max(1, int(Q * ratio)), N)


def greedy_all_windows(D, W, max_elems=4_000_000):
    """Score of every window start 0 .. N-W, exactly as the package does.

    Batched form of `common.calculate_dissimilarity_score`: each round takes
    the first minimum in row-major order of every window's Q x W block,
    adds it and strikes out its row and column; the sum is divided by Q.
    """
    Q, N = D.shape
    starts = np.arange(N - W + 1)
    scores = np.empty(len(starts))
    chunk = max(1, max_elems // (Q * W))
    rounds = min(Q, W)
    for a in range(0, len(starts), chunk):
        s = starts[a:a + chunk]
        M = D[:, s[:, None] + np.arange(W)].transpose(1, 0, 2).copy()  # (S, Q, W)
        rows = np.arange(len(s))
        total = np.zeros(len(s))
        for _ in range(rounds):
            r, c = np.divmod(M.reshape(len(s), -1).argmin(axis=1), W)
            total += M[rows, r, c]
            M[rows, r, :] = np.inf
            M[rows, :, c] = np.inf
        scores[a:a + chunk] = total / Q
    return scores


def greedy_trace(block):
    """The greedy pairing of one Q x W block, step by step, for reports.

    Returns (steps, score) with steps = [(row, col, value), ...]; the result
    equals `calculate_dissimilarity_score` on the same block.
    """
    M = [list(map(float, row)) for row in block]
    Q, W = len(M), len(M[0])
    steps = []
    for _ in range(Q):
        best, br, bc = float("inf"), -1, -1
        for r in range(Q):
            for c in range(W):
                if M[r][c] < best:
                    best, br, bc = M[r][c], r, c
        if br == -1:
            break
        steps.append((br, bc, best))
        for c in range(W):
            M[br][c] = float("inf")
        for r in range(Q):
            M[r][bc] = float("inf")
    expected = calculate_dissimilarity_score([list(map(float, r)) for r in block], W)
    assert [v for _, _, v in steps] == expected
    return steps, sum(v for _, _, v in steps) / Q


# ---- Windows to segments ----------------------------------------------------


def assign_windows(N, W, block_start, block_end):
    """Segment position for every window start 0 .. N-W.

    The segment sharing the most word positions with the window wins; a tie
    goes to the segment holding the middle word (position i + (W-1)//2),
    else to the earliest tied segment.
    """
    i = np.arange(N - W + 1)
    first = np.searchsorted(block_end, i, side="right")  # segment holding i
    k = np.arange(W)  # a window spans at most W segments
    B = first[:, None] + k[None, :]
    valid = B < len(block_start)
    B = np.minimum(B, len(block_start) - 1)
    OV = np.minimum(block_end[B], (i + W)[:, None]) - np.maximum(block_start[B], i[:, None])
    OV = np.where(valid, np.maximum(OV, 0), 0)
    top = (OV == OV.max(axis=1)[:, None]) & (OV > 0)
    earliest = B[np.arange(len(i)), top.argmax(axis=1)]
    mid = np.searchsorted(block_end, i + (W - 1) // 2, side="right")
    mid_is_top = (top & (B == mid[:, None])).any(axis=1)
    return np.where(mid_is_top, mid, earliest)


def segment_scores(scores, assignment, n_segments):
    """Best (lowest) window score per segment; inf if no window counts as it."""
    best = np.full(n_segments, np.inf)
    np.minimum.at(best, assignment, scores)
    return best


def gold_rank(seg_scores, gold):
    """(worst-case rank, number of other segments tied with gold); rank None
    when no window counts as the gold segment (it can never be retrieved)."""
    g = seg_scores[gold]
    if not np.isfinite(g):
        return None, 0
    rank = int(np.sum(seg_scores <= g))
    tied = int(np.sum(seg_scores == g)) - 1
    return rank, tied


def top_segments(seg_scores, k):
    """The k best distinct segments, for display; ties shown in text order."""
    order = np.lexsort((np.arange(len(seg_scores)), seg_scores))
    return [int(b) for b in order[:k] if np.isfinite(seg_scores[b])]


def raw_top_windows(scores, k):
    """The package's own top-k windows: sorted by (score, start)."""
    order = np.lexsort((np.arange(len(scores)), scores))
    return [int(i) for i in order[:k]]


def best_window_of(scores, assignment, segment):
    """Start of the best-scoring window that counts as `segment`."""
    idx = np.nonzero(assignment == segment)[0]
    return int(idx[np.lexsort((idx, scores[idx]))[0]])
