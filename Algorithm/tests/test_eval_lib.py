"""The Recall@N experiment helpers in `bench/eval_lib.py`.

The batched greedy must reproduce the package scorer exactly, and the
segment assignment and worst-case rank must follow their stated rules.
"""

import random
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "bench"))

import eval_lib  # noqa: E402
from fuzzysearch.common import calculate_dissimilarity_score  # noqa: E402
from fuzzysearch.pipeline import compute_matrix, moving_window  # noqa: E402

SEED = 7


class GreedyTests(unittest.TestCase):

    def test_matches_package_greedy_on_random_blocks_with_ties(self):
        rng = np.random.default_rng(SEED)
        for _ in range(300):
            Q, N = int(rng.integers(1, 7)), int(rng.integers(1, 15))
            W = int(rng.integers(1, N + 1))
            D = rng.choice([0.0, 0.25, 0.5, 1.0], size=(Q, N))  # many ties
            got = eval_lib.greedy_all_windows(D, W)
            for i in range(N - W + 1):
                block = [list(D[k, i:i + W]) for k in range(Q)]
                want = sum(calculate_dissimilarity_score(block, W)) / Q
                self.assertEqual(got[i], want)

    def test_matches_moving_window_on_words(self):
        rng = random.Random(SEED)
        for _ in range(100):
            words = ["".join(rng.choice("abcd") for _ in range(rng.randint(1, 4)))
                     for _ in range(rng.randint(3, 25))]
            query = rng.sample(words, rng.randint(1, min(5, len(words))))
            W = rng.randint(1, len(words))
            D = np.array(compute_matrix(query, words))
            got = eval_lib.greedy_all_windows(D, W)
            want = moving_window(query, words, W, distance="compute", pruning="none")
            self.assertEqual(sorted(zip(got.tolist(), range(len(got)))), want)

    def test_trace_agrees_with_score(self):
        D = np.array([[0.0, 1.0, 1.0], [1.0, 0.0, 0.33], [1.0, 0.8, 0.33]])
        steps, score = eval_lib.greedy_trace(D)
        self.assertEqual([(r, c) for r, c, _ in steps], [(0, 0), (1, 1), (2, 2)])
        self.assertEqual(score, eval_lib.greedy_all_windows(D, 3)[0])


class AssignmentTests(unittest.TestCase):
    # Segments: [0,3) [3,5) [5,9)
    START = np.array([0, 3, 5])
    END = np.array([3, 5, 9])

    def test_most_overlapping_segment_wins(self):
        a = eval_lib.assign_windows(9, 4, self.START, self.END)
        self.assertEqual(a[0], 0)  # 0-3: 3 words in segment 0
        self.assertEqual(a[2], 1)  # 2-5: 1 / 2 / 1 words
        self.assertEqual(a[5], 2)  # 5-8: all in segment 2

    def test_tie_goes_to_middle_word_segment(self):
        a = eval_lib.assign_windows(9, 4, self.START, self.END)
        # window 1-4 has 2 words in segment 0 and 2 in segment 1; its
        # middle word is position 1 + (4-1)//2 = 2, in segment 0
        self.assertEqual(a[1], 0)
        # window 3-6 has 2 words in segment 1 and 2 in segment 2; middle
        # word is position 4, in segment 1
        self.assertEqual(a[3], 1)

    def test_empty_segment_is_never_assigned(self):
        start, end = np.array([0, 2, 2]), np.array([2, 2, 5])
        a = eval_lib.assign_windows(5, 2, start, end)
        self.assertNotIn(1, set(a.tolist()))


class RankTests(unittest.TestCase):

    def test_worst_case_rank_places_gold_after_its_ties(self):
        seg = np.array([0.1, 0.1, 0.1, 0.3])
        self.assertEqual(eval_lib.gold_rank(seg, 0), (3, 2))
        self.assertEqual(eval_lib.gold_rank(seg, 3), (4, 0))

    def test_gold_with_no_window_is_unreachable(self):
        seg = np.array([0.1, np.inf, 0.2])
        self.assertEqual(eval_lib.gold_rank(seg, 1), (None, 0))

    def test_exact_self_search_ranks_gold_first(self):
        target = np.arange(12)  # 4 segments of 3 distinct words
        start, end = np.array([0, 3, 6, 9]), np.array([3, 6, 9, 12])
        D = eval_lib.distance_matrix("exact", None, [6, 7, 8], target)
        scores = eval_lib.greedy_all_windows(D, 3)
        seg = eval_lib.segment_scores(scores, eval_lib.assign_windows(12, 3, start, end), 4)
        self.assertEqual(eval_lib.gold_rank(seg, 2), (1, 0))


if __name__ == "__main__":
    unittest.main()
