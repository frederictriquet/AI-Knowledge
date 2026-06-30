#!/usr/bin/env python3
"""Builds and maintains the fiches' embedding index (local cache, incremental).

Model: paraphrase-multilingual-MiniLM-L12-v2 (local, ONNX via fastembed).
Multilingual — suited to the French corpus. Vectors of dimension 384.

The cache (tools/.cache/embeddings.json) only recomputes fiches whose content
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

from kb_common import CACHE_DIR, FICHES, FICHES_OUTILS, charger_fiches, contenu_hash

MODELE = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
CACHE_PATH = os.path.join(CACHE_DIR, "embeddings.json")

_modele = None


def _get_modele():
    """Instantiates the fastembed model only once (download on first call)."""
    global _modele
    if _modele is None:
        from fastembed import TextEmbedding
        _modele = TextEmbedding(model_name=MODELE)
    return _modele


def embed_texts(textes):
    """Encodes a list of texts into vectors (list of lists of float)."""
    if not textes:
        return []
    modele = _get_modele()
    return [vec.tolist() for vec in modele.embed(textes)]


def charger_cache():
    """Loads the embedding cache, or an empty structure if absent/model changed."""
    if not os.path.exists(CACHE_PATH):
        return {"model": MODELE, "fiches": {}}
    try:
        data = json.load(open(CACHE_PATH, encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        # Corrupted cache: we rebuild it, but we trace the cause.
        sys.stderr.write(f"⚠️  unreadable cache ({e}), full rebuild.\n")
        return {"model": MODELE, "fiches": {}}
    if data.get("model") != MODELE:
        sys.stderr.write("⚠️  model changed, invalidating cache.\n")
        return {"model": MODELE, "fiches": {}}
    return data


def maj_index(rebuild=False):
    """Updates the embedding index. Returns the {slug: {...}} dict of fiches."""
    cache = {"model": MODELE, "fiches": {}} if rebuild else charger_cache()
    ancien = cache["fiches"]
    # Indexes both corpora: concepts (fiches/) and tools (fiches outils/).
    fiches = charger_fiches([FICHES, FICHES_OUTILS])

    a_calculer = []     # (slug, text)
    resultat = {}
    for f in fiches:
        h = contenu_hash(f["texte_embed"])
        precedent = ancien.get(f["slug"])
        # Metadata re-read from the fiche; vector reused from cache if hash identical.
        entree = {
            "hash": h,
            "titre": f["fm"].get("title", f["slug"]),
            "theme": ", ".join(f["themes"]),
            "themes": f["themes"],
            "corpus": f["corpus"],
            "vector": None,
        }
        if precedent and precedent.get("hash") == h and precedent.get("vector"):
            entree["vector"] = precedent["vector"]       # unchanged → reuse
        else:
            a_calculer.append((f["slug"], f["texte_embed"]))
        resultat[f["slug"]] = entree

    if a_calculer:
        vecteurs = embed_texts([t for _, t in a_calculer])
        for (slug, _), vec in zip(a_calculer, vecteurs):
            resultat[slug]["vector"] = vec

    os.makedirs(CACHE_DIR, exist_ok=True)
    json.dump({"model": MODELE, "fiches": resultat},
              open(CACHE_PATH, "w", encoding="utf-8"))
    return resultat, len(a_calculer), len(fiches)


def main():
    rebuild = "--rebuild" in sys.argv
    _, recalcules, total = maj_index(rebuild=rebuild)
    reutilises = total - recalcules
    sys.stdout.write(
        f"OK — {total} notes indexed ({recalcules} (re)computed, "
        f"{reutilises} reused from cache).\n"
        f"→ {os.path.relpath(CACHE_PATH)}\n")


if __name__ == "__main__":
    main()
