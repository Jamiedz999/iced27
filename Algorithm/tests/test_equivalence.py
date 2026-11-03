"""Differential test: the optimised matcher against the naive reference.

Randomised over many small corpora with a fixed seed, so it is reproducible
but still covers far more shapes than the hand-written regression cases. This
is the test that catches an optimisation that is *almost* right.
"""

import random
import string
import unittest

from fuzzysearch import naive, optimized
from fuzzysearch.naive import full_scan
from fuzzysearch.optimized import moving_window_similarity1

SEED = 1729
ALPHABET = "abcdefg"  # small, so near-misses and exact repeats both happen


def random_word(rng):
    return "".join(rng.choices(ALPHABET, k=rng.randint(1, 5)))


class EquivalenceTests(unittest.TestCase):

    def test_unpruned_scan_matches_the_reference_exactly(self):
        rng = random.Random(SEED)
        for _ in range(200):
            n = rng.randint(1, 40)
            q = rng.randint(1, 6)
            doc = [random_word(rng) for _ in range(n)]
            query = [random_word(rng) for _ in range(q)]
            window = rng.randint(1, 8)
            step = rng.choice([1, 1, 2, 3])

            expected = full_scan(query, doc, window, step)
            actual = moving_window_similarity1(query, doc, window, step=step)

            self.assertEqual(len(actual), len(expected), (query, doc, window, step))
            for (as_, ai), (es, ei) in zip(actual, expected):
                self.assertEqual(ai, ei, (query, doc, window, step))
                self.assertAlmostEqual(as_, es, delta=1e-12, msg=(query, doc, window, step))

    def test_the_prefilter_never_drops_a_true_match(self):
        rng = random.Random(SEED + 1)
        threshold = 0.5
        for _ in range(200):
            n = rng.randint(1, 40)
            q = rng.randint(1, 6)
            doc = [random_word(rng) for _ in range(n)]
            query = [random_word(rng) for _ in range(q)]
            window = rng.randint(q, q + 4)  # the regime the bound is valid in

            expected = full_scan(query, doc, window)
            pruned = moving_window_similarity1(
                query, doc, window, dissimilarity_threshold=threshold,
            )
            pruned_by_idx = {idx: s for s, idx in pruned}

            for score, idx in expected:
                if score <= threshold:
                    self.assertIn(idx, pruned_by_idx, (query, doc, window))
                    self.assertAlmostEqual(pruned_by_idx[idx], score, delta=1e-12)

    def test_the_prefilter_keeps_the_best_window_whenever_one_qualifies(self):
        """When the true best window is at or under the threshold, pruning must
        return it unchanged. When nothing qualifies, the result is the fallback
        window (smallest *bound*, not smallest score), which need only be
        non-empty — run_search drops it on score anyway."""
        rng = random.Random(SEED + 2)
        threshold = 0.5
        for _ in range(200):
            doc = [random_word(rng) for _ in range(rng.randint(1, 40))]
            query = [random_word(rng) for _ in range(rng.randint(1, 6))]
            window = rng.randint(len(query), len(query) + 4)

            expected = full_scan(query, doc, window)
            pruned = moving_window_similarity1(
                query, doc, window, dissimilarity_threshold=threshold,
            )

            self.assertTrue(pruned, (query, doc, window))
            if expected[0][0] <= threshold:
                self.assertAlmostEqual(pruned[0][0], expected[0][0], delta=1e-12,
                                       msg=(query, doc, window))

    def test_the_two_pipelines_return_the_same_hits(self):
        """End to end: `naive.run_search` and `optimized.run_search` agree on
        every hit, snippet and anchor included."""
        rng = random.Random(SEED + 3)
        for _ in range(200):
            words = [random_word(rng) for _ in range(rng.randint(1, 40))]
            word_array = [{"w": w, "sep": " "} for w in words]
            query = " ".join(random_word(rng) for _ in range(rng.randint(1, 6)))
            step = rng.choice([1, 1, 2, 3])

            expected = naive.run_search(word_array, query, step_size=step)
            actual = optimized.run_search(word_array, query, step_size=step)

            self.assertEqual(len(actual), len(expected), (query, words, step))
            for a, e in zip(actual, expected):
                self.assertAlmostEqual(a.pop("score"), e.pop("score"), delta=1e-12)
                self.assertEqual(a, e, (query, words, step))


if __name__ == "__main__":
    unittest.main()
