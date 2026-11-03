"""Extract paired Irish texts and block ranges using only the standard library."""

import argparse
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
FIELDS = {"medieval": "clnMedIrish", "modern": "clnModIrish"}
WORD_RE = re.compile(r"\w+", re.UNICODE)


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")


def extract(corpus_dir, output_dir):
    paths = sorted(corpus_dir.glob("*.json"))
    if not paths:
        raise ValueError(f"No corpus JSON files found in {corpus_dir}")

    # Validate the full input before writing any outputs.
    documents = []
    for path in paths:
        raw = path.read_bytes()
        doc = json.loads(raw)
        blocks = doc["blocks"]
        for block in blocks:
            for field in FIELDS.values():
                if not isinstance(block[field], str):
                    raise ValueError(f"{path.name}: {block['id']}: {field} is not text")
        documents.append((path, raw, doc))

    output_dir.mkdir(parents=True, exist_ok=True)
    for directory in (*FIELDS, "alignment"):
        (output_dir / directory).mkdir(exist_ok=True)

    manifest = {
        "format_version": 1,
        "join_separator": " ",
        "text_encoding": "UTF-8",
        "token_pattern": WORD_RE.pattern,
        "range_convention": "zero-based, start inclusive, end exclusive",
        "character_units": "Unicode code points (Python string indices)",
        "documents": [],
    }
    for path, raw, doc in documents:
        blocks = doc["blocks"]
        alignment = {
            "document_id": doc.get("id", path.stem),
            "blocks": [{"id": b["id"], "index": i}
                       for i, b in enumerate(blocks)],
        }
        entry = {
            "id": doc.get("id", path.stem),
            "title": doc.get("title"),
            "url": doc.get("url"),
            "source_file": path.name,
            "source_sha256": hashlib.sha256(raw).hexdigest(),
            "block_count": len(blocks),
            "alignment_file": f"alignment/{path.stem}.json",
            "texts": {},
        }
        for variety, field in FIELDS.items():
            pieces = [block[field] for block in blocks]
            text = " ".join(pieces)
            relative = f"{variety}/{path.stem}_{field}_extracted.txt"
            (output_dir / relative).write_bytes(text.encode("utf-8"))
            char_offset = token_offset = 0
            for i, piece in enumerate(pieces):
                count = len(WORD_RE.findall(piece))
                alignment["blocks"][i][variety] = {
                    "char_start": char_offset,
                    "char_end": char_offset + len(piece),
                    "token_start": token_offset,
                    "token_end": token_offset + count,
                }
                char_offset += len(piece) + 1
                token_offset += count
            entry["texts"][variety] = {
                "field": field,
                "file": relative,
                "characters": len(text),
                "tokens": token_offset,
                "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            }
        write_json(output_dir / entry["alignment_file"], alignment)
        manifest["documents"].append(entry)

    manifest["document_count"] = len(documents)
    manifest["block_count"] = sum(d["block_count"] for d in manifest["documents"])
    manifest["combined_texts"] = {}
    for variety, field in FIELDS.items():
        text = " ".join(block[field] for _, _, doc in documents
                        for block in doc["blocks"])
        relative = f"{field}_extracted.txt"
        raw_text = text.encode("utf-8")
        (output_dir / relative).write_bytes(raw_text)
        manifest["combined_texts"][variety] = {
            "field": field,
            "file": relative,
            "characters": len(text),
            "tokens": len(WORD_RE.findall(text)),
            "sha256": hashlib.sha256(raw_text).hexdigest(),
        }
    write_json(output_dir / "manifest.json", manifest)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=ROOT / "corpus")
    parser.add_argument("--output", type=Path, default=ROOT / "corpus" / "extracted")
    args = parser.parse_args()
    manifest = extract(args.corpus, args.output)
    print(f"Extracted {manifest['document_count']} documents, "
          f"{manifest['block_count']} paired blocks into {args.output}")


if __name__ == "__main__":
    main()
