"""Every configuration in `configs.CONFIGS` against the naive scan.

Randomised with a fixed seed, over mixed-case words drawn partly from a
small vocabulary index and partly from outside it, so the table lookup and
its compute fallback are both exercised. The pipeline is case-insensitive,
so the naive scan is given lowercased input.

A configuration without pruning must reproduce the naive scan exactly; one
with pruning must be lossless: it keeps every window the naive scan scores
at or under the threshold, with the same score, and the best one when it
qualifies.
"""

import json
import random
import tempfile
import unittest
from pathlib import Path

from fuzzysearch.configs import CONFIGS
from fuzzysearch.naive import full_scan
from fuzzysearch.pipeline import moving_window
from fuzzysearch.vocab import build_index

SEED = 4242
ALPHABET = "abcdeAB"  # small, so near-misses, repeats and case pairs happen
THRESHOLD = 0.5
CASES = 150


def random_word(rng):
    return "".join(rng.choices(ALPHABET, k=rng.randint(1, 5)))


def lower(words):
    return [w.lower() for w in words]


class ConfigurationTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        root = Path(cls._tmp.name)
        rng = random.Random(SEED)
        in_vocab = " ".join(random_word(rng) for _ in range(150))
        (root / "corpus").mkdir()
        (root / "corpus" / "doc.json").write_text(json.dumps({"id": "doc", "blocks": [
            {"id": "b1", "clnMedIrish": in_vocab, "clnModIrish": ""},
        ]}), encoding="utf-8")
        cls.index = build_index(root / "corpus", root / "index")

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def cases(self, seed, window_at_least_query):
        """(query, doc, window, step, doc_ids) tuples; doc_ids is given for
        about half the cases, as a caller holding docs.json would."""
        rng = random.Random(seed)
        vocab = self.index.words
        for _ in range(CASES):
            def word():
                w = rng.choice(vocab) if rng.random() < 0.7 else random_word(rng)
                return w.upper() if rng.random() < 0.2 else w
            doc = [word() for _ in range(rng.randint(1, 40))]
            query = [word() for _ in range(rng.randint(1, 6))]
            if window_at_least_query:
                window = rng.randint(len(query), len(query) + 4)
            else:
                window = rng.randint(1, 8)
            step = rng.choice([1, 1, 2, 3])
            doc_ids = None
            if all(self.index.word_id(w) is not None for w in doc) and rng.random() < 0.5:
                doc_ids = [self.index.word_id(w) for w in doc]
            yield query, doc, window, step, doc_ids

    def run_config(self, components, query, doc, window, step, doc_ids,
                   threshold=float("inf")):
        return moving_window(query, doc, window, step, threshold,
                             index=self.index, doc_ids=doc_ids, **components)

    def test_unpruned_configs_match_the_naive_scan_exactly(self):
        for name, components in CONFIGS.items():
            if components["pruning"] != "none":
                continue
            with self.subTest(config=name):
                for query, doc, window, step, doc_ids in self.cases(SEED + 1, False):
                    ctx = (name, query, doc, window, step)
                    expected = full_scan(lower(query), lower(doc), window, step)
                    actual = self.run_config(components, query, doc, window, step, doc_ids)
                    self.assertEqual([i for _, i in actual], [i for _, i in expected], ctx)
                    for (a, _), (e, _) in zip(actual, expected):
                        self.assertAlmostEqual(a, e, delta=1e-12, msg=ctx)

    def test_pruned_configs_are_lossless(self):
        # Window >= query length: the regime the lower bound is valid in
        # (see test_known_defects.py for W < Q).
        for name, components in CONFIGS.items():
            if components["pruning"] == "none":
                continue
            with self.subTest(config=name):
                for query, doc, window, step, doc_ids in self.cases(SEED + 2, True):
                    ctx = (name, query, doc, window, step)
                    expected = full_scan(lower(query), lower(doc), window, step)
                    actual = self.run_config(components, query, doc, window, step,
                                             doc_ids, THRESHOLD)
                    self.assertTrue(actual, ctx)
                    by_idx = {i: s for s, i in actual}
                    for score, idx in expected:
                        if score <= THRESHOLD:
                            self.assertIn(idx, by_idx, ctx)
                            self.assertAlmostEqual(by_idx[idx], score, delta=1e-12, msg=ctx)
                    if expected[0][0] <= THRESHOLD:
                        self.assertAlmostEqual(actual[0][0], expected[0][0],
                                               delta=1e-12, msg=ctx)

    def test_configs_ignore_case(self):
        for name, components in CONFIGS.items():
            with self.subTest(config=name):
                result = self.run_config(components, ["OCUS", "Mac"],
                                         ["ocus", "mac", "find"], 2, 1, None, THRESHOLD)
                self.assertEqual(result[0], (0.0, 0))


if __name__ == "__main__":
    unittest.main()
