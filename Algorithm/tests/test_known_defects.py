"""Defects found while extracting the algorithm, pinned as expected failures.

Each test states the behaviour the algorithm *should* have. It is marked
`expectedFailure`, so the suite stays green today and reports an "unexpected
success" the moment an optimisation fixes it — at which point drop the
decorator and move the test to its proper home.
"""

import unittest

from fuzzysearch.naive import full_scan
from fuzzysearch.optimized import moving_window_similarity1, run_search


class PrefilterIsUnsoundBelowFullMatchLength(unittest.TestCase):
    """The lower bound LB(i) = (sum of the Q per-row window minima) / Q is only
    a lower bound when the window is at least as long as the query.

    The greedy assignment pairs each query word with a *distinct* window word,
    so with W < Q it can only produce W terms before it runs out of columns —
    it sums W values and still divides by Q. The bound sums all Q minima and
    divides by Q, so it can come out *above* the true score, and a true match
    gets pruned.

    Reachable in production: `window_size_ratio` is accepted down to 0.1, and
    the Match Length slider goes to 10 %, so any setting below 100 % can drop
    real hits when a dissimilarity threshold is set.
    """

    QUERY = ["a", "ec", "aaa", "c", "bd"]
    DOC = ["cada", "b", "gafad", "dfd", "bae", "ce", "dd",
           "cab", "ecc", "g", "geca", "eaec", "ce", "fbd", "de"]
    WINDOW = 4  # < len(QUERY) == 5
    THRESHOLD = 0.5

    @unittest.expectedFailure
    def test_a_true_match_below_the_threshold_survives_the_prefilter(self):
        full = full_scan(self.QUERY, self.DOC, self.WINDOW)
        pruned = moving_window_similarity1(
            self.QUERY, self.DOC, self.WINDOW,
            dissimilarity_threshold=self.THRESHOLD,
        )
        pruned_by_idx = {idx: s for s, idx in pruned}

        # Window 10 truly scores ~0.417, well under the threshold, yet its
        # lower bound is higher and the prefilter never scores it.
        for score, idx in full:
            if score <= self.THRESHOLD:
                self.assertIn(idx, pruned_by_idx)

    @unittest.expectedFailure
    def test_a_short_match_length_does_not_lose_hits(self):
        """The same defect as run_search sees it: a ratio under 1.0 returns
        fewer hits than the same search with pruning switched off."""
        doc = [{"w": w, "sep": " "} for w in self.DOC]

        pruned = run_search(doc, " ".join(self.QUERY),
                            window_size_ratio=0.8, dissimilarity_threshold=0.5)
        unpruned = run_search(doc, " ".join(self.QUERY),
                              window_size_ratio=0.8, dissimilarity_threshold=1.0)
        kept = [h for h in unpruned if h["score"] <= 0.5]

        self.assertEqual(len(pruned), len(kept))


if __name__ == "__main__":
    unittest.main()
