#!/usr/bin/env python3
"""Builds and maintains the notes' embedding index (local cache, incremental).

Model: paraphrase-multilingual-MiniLM-L12-v2 (local, ONNX via fastembed).
Multilingual — suited to the corpus. Vectors of dimension 384.

The cache (tools/.cache/embeddings.json) only recomputes notes whose content
has changed (hash comparison). Changing the model invalidates the whole cache.

Usage:
    python3 tools/kb_embed.py              # update the index (incremental)
    python3 tools/kb_embed.py --rebuild    # recompute everything
"""
# fastembed lives in tools/.venv and kb_common is a sibling module: both are
# resolved at runtime but invisible to the hook's isolated type-checker.
# pyright: reportMissingImports=false
import os
import sys
import json

from kb_common import CACHE_DIR, CONCEPTS, TOOLS, load_notes, content_hash

MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
CACHE_PATH = os.path.join(CACHE_DIR, "embeddings.json")

_model = None


def _get_model():
    """Instantiates the fastembed model only once (download on first call)."""
    global _model
    if _model is None:
        from fastembed import TextEmbedding
        _model = TextEmbedding(model_name=MODEL)
    return _model


def embed_texts(texts):
    """Encodes a list of texts into vectors (list of lists of float)."""
    if not texts:
        return []
    model = _get_model()
    return [vec.tolist() for vec in model.embed(texts)]


def load_cache():
    """Loads the embedding cache, or an empty structure if absent/model changed."""
    if not os.path.exists(CACHE_PATH):
        return {"model": MODEL, "fiches": {}}
    try:
        data = json.load(open(CACHE_PATH, encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        # Corrupted cache: we rebuild it, but we trace the cause.
        sys.stderr.write(f"⚠️  unreadable cache ({e}), full rebuild.\n")
        return {"model": MODEL, "fiches": {}}
    if data.get("model") != MODEL:
        sys.stderr.write("⚠️  model changed, invalidating cache.\n")
        return {"model": MODEL, "fiches": {}}
    return data


def update_index(rebuild=False):
    """Updates the embedding index. Returns the {slug: {...}} dict of notes."""
    cache = {"model": MODEL, "fiches": {}} if rebuild else load_cache()
    previous = cache["fiches"]
    # Indexes both corpora: concepts (concepts/) and tools (tools/).
    notes = load_notes([CONCEPTS, TOOLS])

    to_compute = []     # (slug, text)
    result = {}
    for n in notes:
        h = content_hash(n["embed_text"])
        prev = previous.get(n["slug"])
        # Metadata re-read from the note; vector reused from cache if hash identical.
        entry = {
            "hash": h,
            "titre": n["fm"].get("title", n["slug"]),
            "theme": ", ".join(n["themes"]),
            "themes": n["themes"],
            "corpus": n["corpus"],
            "vector": None,
        }
        if prev and prev.get("hash") == h and prev.get("vector"):
            entry["vector"] = prev["vector"]       # unchanged → reuse
        else:
            to_compute.append((n["slug"], n["embed_text"]))
        result[n["slug"]] = entry

    if to_compute:
        vectors = embed_texts([t for _, t in to_compute])
        for (slug, _), vec in zip(to_compute, vectors):
            result[slug]["vector"] = vec

    os.makedirs(CACHE_DIR, exist_ok=True)
    json.dump({"model": MODEL, "fiches": result},
              open(CACHE_PATH, "w", encoding="utf-8"))
    return result, len(to_compute), len(notes)


def main():
    rebuild = "--rebuild" in sys.argv
    _, recomputed, total = update_index(rebuild=rebuild)
    reused = total - recomputed
    sys.stdout.write(
        f"OK — {total} notes indexed ({recomputed} (re)computed, "
        f"{reused} reused from cache).\n"
        f"→ {os.path.relpath(CACHE_PATH)}\n")


if __name__ == "__main__":
    main()
