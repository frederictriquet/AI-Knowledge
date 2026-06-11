#!/usr/bin/env python3
"""Construit et maintient l'index d'embeddings des fiches (cache local, incrémental).

Modèle : paraphrase-multilingual-MiniLM-L12-v2 (local, ONNX via fastembed).
Multilingue — adapté au corpus français. Vecteurs de dimension 384.

Le cache (tools/.cache/embeddings.json) ne recalcule que les fiches dont le
contenu a changé (comparaison de hash). Changer de modèle invalide tout le cache.

Usage :
    python3 tools/kb_embed.py              # met à jour l'index (incrémental)
    python3 tools/kb_embed.py --rebuild    # recalcule tout
"""
# fastembed vit dans tools/.venv et kb_common est un module frère : tous deux sont
# résolus à l'exécution mais invisibles au type-checker isolé du hook.
# pyright: reportMissingImports=false
import os
import sys
import json

from kb_common import CACHE_DIR, charger_fiches, contenu_hash

MODELE = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
CACHE_PATH = os.path.join(CACHE_DIR, "embeddings.json")

_modele = None


def _get_modele():
    """Instancie le modèle fastembed une seule fois (téléchargement au 1er appel)."""
    global _modele
    if _modele is None:
        from fastembed import TextEmbedding
        _modele = TextEmbedding(model_name=MODELE)
    return _modele


def embed_texts(textes):
    """Encode une liste de textes en vecteurs (liste de listes de float)."""
    if not textes:
        return []
    modele = _get_modele()
    return [vec.tolist() for vec in modele.embed(textes)]


def charger_cache():
    """Charge le cache d'embeddings, ou une structure vide si absent/modèle changé."""
    if not os.path.exists(CACHE_PATH):
        return {"model": MODELE, "fiches": {}}
    try:
        data = json.load(open(CACHE_PATH, encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        # Cache corrompu : on le reconstruit, mais on trace la cause.
        sys.stderr.write(f"⚠️  cache illisible ({e}), reconstruction complète.\n")
        return {"model": MODELE, "fiches": {}}
    if data.get("model") != MODELE:
        sys.stderr.write("⚠️  modèle changé, invalidation du cache.\n")
        return {"model": MODELE, "fiches": {}}
    return data


def maj_index(rebuild=False):
    """Met à jour l'index d'embeddings. Retourne le dict {slug: {...}} des fiches."""
    cache = {"model": MODELE, "fiches": {}} if rebuild else charger_cache()
    ancien = cache["fiches"]
    fiches = charger_fiches()

    a_calculer = []     # (slug, texte)
    resultat = {}
    for f in fiches:
        h = contenu_hash(f["texte_embed"])
        precedent = ancien.get(f["slug"])
        if precedent and precedent.get("hash") == h:
            resultat[f["slug"]] = precedent              # inchangé → réutilise
        else:
            a_calculer.append((f["slug"], f["texte_embed"]))
            resultat[f["slug"]] = {
                "hash": h,
                "titre": f["fm"].get("titre", f["slug"]),
                "theme": f["fm"].get("theme", ""),
                "vector": None,                          # rempli ci-dessous
            }

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
        f"OK — {total} fiches indexées ({recalcules} (re)calculées, "
        f"{reutilises} réutilisées du cache).\n"
        f"→ {os.path.relpath(CACHE_PATH)}\n")


if __name__ == "__main__":
    main()
