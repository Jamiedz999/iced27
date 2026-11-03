"""The search layer: query tokenizing, snippet rebuilding, anchor lookup.

The snippet cases come from uCeltic #145 — snippets are rebuilt from the word
array, so `sep or " "` invented a space wherever a separator was empty and put
a visible gap at every fragment boundary. On a faithful index an empty
separator means the source has nothing there, and the snippet must say so.
"""

import unittest

from fuzzysearch.common import tokenize_query
from fuzzysearch.optimized import run_search


def words(*pairs, anchor="l-1"):
    """Build a word_array from (word, separator) pairs."""
    return [{"w": w, "sep": sep, "a": anchor} for w, sep in pairs]


# `ro gab i<expan>n</expan> tal<expan>am</expan><note>Sic.</note>trochull`
# The note sits flush against `talam`, so the two words it separates end up
# genuinely adjacent — the one case where an empty separator survives.
FLUSH_NOTE_WORDS = words(
    ("ro", " "), ("gab", " "), ("in", " "), ("talam", ""), ("trochull", ""),
)
ANCHORS = [{"id": "l-1", "tag": "l", "line_no": 1}]


class SnippetTests(unittest.TestCase):

    def test_a_word_split_by_an_element_is_searchable(self):
        results = run_search(FLUSH_NOTE_WORDS, "talam", anchors=ANCHORS)

        self.assertTrue(results)
        self.assertIn("talam", results[0]["snippet"])

    def test_an_empty_separator_is_not_turned_into_a_space(self):
        results = run_search(FLUSH_NOTE_WORDS, "talam trochull", anchors=ANCHORS)

        self.assertEqual(results[0]["snippet"], "talamtrochull")

    def test_a_snippet_keeps_the_separators_the_source_has(self):
        results = run_search(FLUSH_NOTE_WORDS, "ro gab in", anchors=ANCHORS)

        self.assertEqual(results[0]["snippet"], "ro gab in")


class RunSearchTests(unittest.TestCase):

    def test_empty_query_and_empty_document_return_nothing(self):
        self.assertEqual(run_search(FLUSH_NOTE_WORDS, "   "), [])
        self.assertEqual(run_search([], "talam"), [])

    def test_a_hit_carries_its_word_range_and_anchor(self):
        hit = run_search(FLUSH_NOTE_WORDS, "talam trochull", anchors=ANCHORS)[0]

        self.assertEqual(hit["word_start"], 3)
        self.assertEqual(hit["word_end"], 5)
        self.assertEqual(hit["anchor_id"], "l-1")
        self.assertEqual(hit["anchor_tag"], "l")
        self.assertEqual(hit["line_no"], 1)

    def test_a_missing_anchor_leaves_the_fields_null(self):
        hit = run_search(FLUSH_NOTE_WORDS, "talam trochull")[0]

        self.assertIsNone(hit["anchor_id"])
        self.assertIsNone(hit["anchor_tag"])
        self.assertIsNone(hit["line_no"])

    def test_results_above_the_threshold_are_dropped(self):
        self.assertEqual(
            run_search(FLUSH_NOTE_WORDS, "zzzzzzz", dissimilarity_threshold=0.1), [],
        )

    def test_top_k_caps_the_result_count(self):
        doc = words(*[("find", " ")] * 20)
        self.assertEqual(len(run_search(doc, "find", top_k=3)), 3)

    def test_the_window_is_the_ratio_times_the_query_length(self):
        """window_size_ratio 1.3 over a 3-word query gives a 3-word window
        (int(3.9)); 2.0 gives 6, leaving room for inserted words."""
        doc = words(*[(w, " ") for w in
                      ["ro", "gab", "in", "talam", "trochull", "agus", "find"]])

        narrow = run_search(doc, "ro gab in", window_size_ratio=1.3)[0]
        wide = run_search(doc, "ro gab in", window_size_ratio=2.0)[0]

        self.assertEqual(narrow["word_end"] - narrow["word_start"], 3)
        self.assertEqual(wide["word_end"] - wide["word_start"], 6)


class TokenizeTests(unittest.TestCase):

    def test_punctuation_is_dropped_and_diacritics_are_kept(self):
        self.assertEqual(tokenize_query("Find, mac Cumaill."), ["Find", "mac", "Cumaill"])
        self.assertEqual(tokenize_query("Senórach"), ["Senórach"])


if __name__ == "__main__":
    unittest.main()
