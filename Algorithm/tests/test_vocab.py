"""The precomputed vocabulary index must reproduce, by lookup, exactly the
distances the matcher would compute, over one vocabulary shared by both
varieties.
"""

import json
import tempfile
import unittest
from pathlib import Path

import numpy as np
from rapidfuzz.distance import Levenshtein

from fuzzysearch.vocab import build_index, load_index, tokenize


def _block(block_id, med, mod):
    return {"id": block_id, "clnMedIrish": med, "clnModIrish": mod}


CORPUS = {
    "acSen.json": {"id": "acSen", "blocks": [
        _block("acSen_1", "Ar tabhuirtt chatha Chomuir ocus",
               "Ar dtabhairt chatha Chomair agus"),
        _block("acSen_2", "ro scáilset iar sin", "do scaoileadar iar sin"),
    ]},
    "abbot.json": {"id": "abbot", "blocks": [
        _block("abbot_1", "OCUS ro baei", "agus bhí"),
    ]},
    "empty.json": {"id": "empty", "blocks": []},
}


class VocabIndexTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        root = Path(cls._tmp.name)
        corpus = root / "corpus"
        corpus.mkdir()
        for name, doc in CORPUS.items():
            (corpus / name).write_text(json.dumps(doc, ensure_ascii=False),
                                       encoding="utf-8")
        build_index(corpus, root / "index")
        cls.index = load_index(root / "index")

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def test_tokenize_lowercases_and_nothing_else(self):
        self.assertEqual(tokenize("Chatha, ḟer n-abar scáilset!"),
                         ["chatha", "ḟer", "n", "abar", "scáilset"])

    def test_one_vocabulary_across_varieties_files_and_case(self):
        idx = self.index
        self.assertEqual(idx.words, sorted(set(idx.words)))
        # "iar" and "sin" occur in both varieties; "ocus"/"OCUS" is one word.
        self.assertEqual(idx.sources[idx.word_id("iar")], 3)
        self.assertEqual(idx.sources[idx.word_id("ocus")], 1)
        self.assertEqual(idx.sources[idx.word_id("agus")], 2)
        self.assertEqual(idx.word_id("OCUS"), idx.word_id("ocus"))
        self.assertIsNone(idx.word_id("absent"))

    def test_table_covers_every_pair_and_matches_levenshtein(self):
        idx = self.index
        v = len(idx.words)
        self.assertEqual(idx.distances.shape, (v, v))
        for a, wa in enumerate(idx.words):
            for b, wb in enumerate(idx.words):
                self.assertEqual(idx.distance(a, b),
                                 Levenshtein.distance(wa, wb))
                self.assertEqual(idx.normalized_distance(a, b),
                                 Levenshtein.normalized_distance(wa, wb))
        self.assertTrue((idx.distances == idx.distances.T).all())
        self.assertTrue((np.diag(idx.distances) == 0).all())

    def test_docs_round_trip_to_block_tokens(self):
        idx = self.index
        self.assertEqual(set(idx.docs), {"acSen", "abbot"})
        for name, doc in CORPUS.items():
            if not doc["blocks"]:
                continue
            for variety, field in (("medieval", "clnMedIrish"),
                                   ("modern", "clnModIrish")):
                entry = idx.docs[doc["id"]][variety]
                for block, rng in zip(doc["blocks"], entry["blocks"]):
                    self.assertEqual(rng["id"], block["id"])
                    ids = entry["ids"][rng["start"]:rng["end"]]
                    self.assertEqual([idx.words[i] for i in ids],
                                     tokenize(block[field]))


if __name__ == "__main__":
    unittest.main()
