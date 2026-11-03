"""Word IDs and a precomputed V x V Levenshtein table for a corpus of
acSen-style JSON files, so distances are looked up instead of computed.

Medieval and Modern Irish share one vocabulary: every distinct word from
either variety, across every file, gets one ID, and the table holds the
distance between every pair of words (med-med, mod-mod and med-mod alike).

Words are compared as written, apart from case: tokens are `\\w+` runs,
lowercased, with no other normalization (no Irish mutation rules).

Index layout (a directory):

    vocab.json     {"words": [...], "sources": [...]}; a word's ID is its
                   index in `words` (sorted, so IDs are reproducible).
                   sources[i]: 1 = medieval, 2 = modern, 3 = both.
    distances.npy  uint8 V x V, raw Levenshtein distance between word IDs.
                   Opened memory-mapped: the full corpus table is ~1.2 GB.
    lengths.npy    uint16 V, word lengths. The normalized distance used by
                   the matcher is distances[a, b] / max(lengths[a], lengths[b]).
    docs.json      {doc_id: {variety: {"ids": [...], "blocks": [{"id",
                   "start", "end"}, ...]}}}: each text as word IDs, and the
                   half-open range each block occupies in it.

Build from the command line:

    python -m fuzzysearch.vocab ../corpus index
"""

import json
import re
import sys
from pathlib import Path

import numpy as np
from rapidfuzz.distance import Levenshtein
from rapidfuzz.process import cdist

_WORD_RE = re.compile(r"\w+", re.UNICODE)

# variety name -> (block field, bit in vocab "sources")
VARIETIES = {
    "medieval": ("clnMedIrish", 1),
    "modern": ("clnModIrish", 2),
}

# Rows of the table computed per cdist call; bounds peak memory while the
# output itself is written straight to a memory-mapped file.
_CHUNK_ROWS = 2000

__all__ = ["tokenize", "build_index", "load_index", "VocabIndex"]


def tokenize(text):
    """Split text into lowercased `\\w+` words; nothing else is normalized."""
    return [w.lower() for w in _WORD_RE.findall(text)]


def _read_corpus(corpus_dir):
    """Yield (doc_id, {variety: [(block_id, words), ...]}) per JSON file."""
    for path in sorted(Path(corpus_dir).glob("*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        blocks = doc.get("blocks") or []
        if not blocks:
            continue
        yield doc.get("id") or path.stem, {
            name: [(b["id"], tokenize(b.get(field) or "")) for b in blocks]
            for name, (field, _) in VARIETIES.items()
        }


def build_index(corpus_dir, out_dir):
    """Tokenize every file in `corpus_dir` and write the index to `out_dir`."""
    corpus = list(_read_corpus(corpus_dir))

    source_bits = {}
    for _, varieties in corpus:
        for name, (_, bit) in VARIETIES.items():
            for _, words in varieties[name]:
                for w in words:
                    source_bits[w] = source_bits.get(w, 0) | bit
    words = sorted(source_bits)
    ids = {w: i for i, w in enumerate(words)}

    lengths = np.array([len(w) for w in words], dtype=np.uint16)
    if len(words) and lengths.max() > np.iinfo(np.uint8).max:
        raise ValueError("a word is too long for a uint8 distance table")

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    distances = np.lib.format.open_memmap(
        out / "distances.npy", mode="w+", dtype=np.uint8,
        shape=(len(words), len(words)))
    for start in range(0, len(words), _CHUNK_ROWS):
        rows = words[start:start + _CHUNK_ROWS]
        distances[start:start + len(rows)] = cdist(
            rows, words, scorer=Levenshtein.distance,
            dtype=np.uint8, workers=-1)
    distances.flush()
    del distances

    np.save(out / "lengths.npy", lengths)
    (out / "vocab.json").write_text(
        json.dumps({"words": words,
                    "sources": [source_bits[w] for w in words]},
                   ensure_ascii=False),
        encoding="utf-8")

    docs = {}
    for doc_id, varieties in corpus:
        docs[doc_id] = {}
        for name, per_block in varieties.items():
            seq, ranges = [], []
            for block_id, block_words in per_block:
                start = len(seq)
                seq.extend(ids[w] for w in block_words)
                ranges.append({"id": block_id, "start": start, "end": len(seq)})
            docs[doc_id][name] = {"ids": seq, "blocks": ranges}
    (out / "docs.json").write_text(json.dumps(docs), encoding="utf-8")

    return load_index(out)


class VocabIndex:
    """A loaded index: word <-> ID maps, the distance table and the docs."""

    def __init__(self, words, sources, distances, lengths, docs):
        self.words = words
        self.sources = sources
        self.ids = {w: i for i, w in enumerate(words)}
        self.distances = distances
        self.lengths = lengths
        self.docs = docs

    def word_id(self, word):
        """ID of `word` (lowercased), or None if it is not in the corpus."""
        return self.ids.get(word.lower())

    def distance(self, a, b):
        """Raw Levenshtein distance between word IDs `a` and `b`."""
        return int(self.distances[a, b])

    def normalized_distance(self, a, b):
        """Levenshtein distance / length of the longer word, as the matcher
        scores it; 0.0 for two empty words."""
        longest = max(int(self.lengths[a]), int(self.lengths[b]))
        return self.distance(a, b) / longest if longest else 0.0


def load_index(index_dir):
    """Open an index written by `build_index`; the table is memory-mapped."""
    root = Path(index_dir)
    vocab = json.loads((root / "vocab.json").read_text(encoding="utf-8"))
    return VocabIndex(
        words=vocab["words"],
        sources=vocab["sources"],
        distances=np.load(root / "distances.npy", mmap_mode="r"),
        lengths=np.load(root / "lengths.npy"),
        docs=json.loads((root / "docs.json").read_text(encoding="utf-8")),
    )


def main(argv):
    if len(argv) != 2:
        sys.exit("usage: python -m fuzzysearch.vocab CORPUS_DIR OUT_DIR")
    index = build_index(argv[0], argv[1])
    shared = sum(1 for s in index.sources if s == 3)
    tokens = {name: sum(len(d[name]["ids"]) for d in index.docs.values())
              for name in VARIETIES}
    print(f"{len(index.docs)} documents, {len(index.words)} words "
          f"({shared} in both varieties), table {index.distances.shape}, "
          + ", ".join(f"{n} {t} tokens" for n, t in tokens.items()))


if __name__ == "__main__":
    main(sys.argv[1:])
