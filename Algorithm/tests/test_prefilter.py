"""The lower-bound prefilter must be *lossless*: pruning may keep extra
windows, but it may never drop or alter a true match.

These are the correctness contract any further optimisation inherits.
"""

import unittest

from fuzzysearch.optimized import moving_window_similarity1


class PrefilterTests(unittest.TestCase):

    def test_finite_threshold_keeps_best_window(self):
        """A finite threshold must not change the best match: results[0] is
        identical to the unpruned (infinite-threshold) full scan."""
        query = ["find", "mac"]
        doc = ["agus", "find", "mac", "cumaill", "agus", "find", "mor"]

        full = moving_window_similarity1(query, doc, actual_window_size=2, step=1, top_k=10)
        pruned = moving_window_similarity1(
            query, doc, actual_window_size=2, step=1, top_k=10,
            dissimilarity_threshold=0.5,
        )

        self.assertAlmostEqual(pruned[0][0], full[0][0], delta=1e-9)
        self.assertEqual(pruned[0][1], full[0][1])

    def test_pruned_keeps_every_true_match_with_identical_scores(self):
        """No false negatives: every window the full scan scores <= threshold
        reappears in the pruned output with the same score. (The prefilter may
        keep extra windows whose bound passes but whose true score does not —
        run_search filters those.)"""
        query = ["find", "mac"]
        doc = ["find", "mac", "cumaill", "agus", "find", "mor", "ocus", "find", "mac"]
        threshold = 0.5

        full = moving_window_similarity1(query, doc, 2, step=1, top_k=99)
        pruned = moving_window_similarity1(
            query, doc, 2, step=1, top_k=99, dissimilarity_threshold=threshold,
        )
        pruned_by_idx = {idx: s for s, idx in pruned}

        for score, idx in full:
            if score <= threshold:
                self.assertIn(idx, pruned_by_idx)
                self.assertAlmostEqual(pruned_by_idx[idx], score, delta=1e-9)

    def test_step_size_matches_full_scan_with_same_step(self):
        """step > 1 subsamples window starts: every emitted index is on the
        step grid, and no true match is dropped against the same-step scan."""
        query = ["find", "mac"]
        doc = ["find", "mac", "cumaill", "agus", "find", "mor", "ocus", "find", "mac", "beg"]
        step = 2
        threshold = 0.5

        full = moving_window_similarity1(query, doc, 2, step=step, top_k=99)
        pruned = moving_window_similarity1(
            query, doc, 2, step=step, top_k=99, dissimilarity_threshold=threshold,
        )
        pruned_by_idx = {idx: s for s, idx in pruned}

        for _, idx in pruned:
            self.assertEqual(idx % step, 0)
        for score, idx in full:
            if score <= threshold:
                self.assertIn(idx, pruned_by_idx)
                self.assertAlmostEqual(pruned_by_idx[idx], score, delta=1e-9)

    def test_unreachable_threshold_still_returns_best_window(self):
        """When no window's bound passes, the global-best window is kept as a
        fallback so results[0] never raises IndexError."""
        query = ["find", "mac"]
        doc = ["zzzzz", "qqqqq", "xxxxx", "wwwww"]
        results = moving_window_similarity1(
            query, doc, 2, step=1, top_k=10, dissimilarity_threshold=-1.0,
        )
        self.assertEqual(len(results), 1)
        score, idx = results[0]
        self.assertGreaterEqual(idx, 0)
        self.assertGreater(score, 0.0)


if __name__ == "__main__":
    unittest.main()
