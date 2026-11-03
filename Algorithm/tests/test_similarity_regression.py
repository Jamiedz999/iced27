"""Regression nails for `moving_window_similarity1`.

Fixed inputs, locked outputs: these assert *behaviour*, not implementation, so
every optimisation applied to the matcher has to leave them green. The expected
values were recorded against the original uCeltic implementation.
"""

import unittest

from fuzzysearch.optimized import moving_window_similarity1


class MovingWindowSimilarityRegressionTests(unittest.TestCase):

    # -- basic hit ----------------------------------------------------------
    def test_exact_match_scores_zero(self):
        """An exact match scores 0.0 dissimilarity."""
        query = ["Fionn", "mac", "Cumaill"]
        doc = ["Fionn", "mac", "Cumaill"]
        results = moving_window_similarity1(query, doc, actual_window_size=3, step=1, top_k=1)

        best_score, best_idx = results[0]
        self.assertAlmostEqual(best_score, 0.0, delta=1e-9)
        self.assertEqual(best_idx, 0)

    def test_no_match_scores_high(self):
        """Unrelated words score well above 0."""
        query = ["Fionn"]
        doc = ["zzzzz", "qqqqq", "xxxxx"]
        results = moving_window_similarity1(query, doc, actual_window_size=1, step=1, top_k=1)

        best_score, _ = results[0]
        self.assertGreater(best_score, 0.5)

    # -- fixed score regression (core) --------------------------------------
    def test_known_scores_do_not_drift(self):
        query = ["find", "mac"]
        doc = ["find", "mac", "cumaill", "agus", "find", "mor"]
        results = moving_window_similarity1(query, doc, actual_window_size=2, step=1, top_k=10)

        by_idx = {idx: score for score, idx in results}

        # window [0,2): ["find","mac"] vs ["find","mac"] -> identical
        self.assertAlmostEqual(by_idx[0], 0.0, delta=1e-6)
        # window [4,6): "mac" vs "mor" -> normalized distance 1/3, averaged over Q=2
        self.assertAlmostEqual(by_idx[4], 0.333, delta=1e-3)

    # -- ordering -----------------------------------------------------------
    def test_results_are_sorted_best_first(self):
        query = ["abc"]
        doc = ["abc", "xyz", "abc", "ijk", "abc"]
        results = moving_window_similarity1(query, doc, actual_window_size=1, step=1, top_k=2)

        scores = [s for s, _ in results]
        self.assertEqual(scores, sorted(scores))
        self.assertAlmostEqual(scores[0], 0.0, delta=1e-9)

    # -- degenerate input ---------------------------------------------------
    def test_empty_document_returns_the_sentinel(self):
        self.assertEqual(moving_window_similarity1(["find"], [], 3), [(0, 1.0)])

    def test_window_larger_than_document_is_clamped(self):
        """W > N collapses to a single window covering the whole document."""
        results = moving_window_similarity1(["find", "mac"], ["find", "mac"], 10, step=1)
        self.assertEqual(len(results), 1)
        self.assertAlmostEqual(results[0][0], 0.0, delta=1e-9)
        self.assertEqual(results[0][1], 0)


if __name__ == "__main__":
    unittest.main()
