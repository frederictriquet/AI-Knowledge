#!/usr/bin/env python3
"""Détection de doublons par similarité sémantique (étage 1 du process).

Prend un texte de concept candidat (issu d'un nouvel article) et retourne les
fiches existantes les plus proches, avec un verdict indicatif basé sur des seuils.
Ce verdict est un PRÉ-FILTRE : le jugement final de recouvrement est délégué au
skill /enrich qui lit réellement les fiches candidates.

Seuils (similarité cosinus), CALIBRÉS empiriquement sur la distribution des plus
proches voisins du corpus pour le modèle MiniLM multilingue (médiane du NN ≈ 0.70,
paires les plus liées du corpus ≈ 0.87) :
    >= 0.85   DOUBLON probable    — au niveau des paires les plus liées du corpus
    0.75-0.85 RECOUVREMENT        — sujet voisin, à juger (fusion ? complément ?)
    <  0.75   NOUVEAU             — aucun proche, fiche inédite probable
Ces seuils dépendent du modèle : les recalibrer si MODELE change (cf. kb_embed.py).
Le verdict n'est qu'un pré-filtre — le jugement final revient au skill /enrich.

Usage :
    python3 tools/kb_dedup.py "texte du concept candidat"
    python3 tools/kb_dedup.py --file concept.txt --k 5
    echo "texte" | python3 tools/kb_dedup.py --json
"""
# kb_embed/kb_common dépendent du venv et d'imports frères, invisibles au hook.
# pyright: reportMissingImports=false
import sys
import json
import argparse

from kb_common import cosine
from kb_embed import maj_index, embed_texts

SEUIL_DOUBLON = 0.85
SEUIL_RECOUVREMENT = 0.75


def verdict(score):
    if score >= SEUIL_DOUBLON:
        return "DOUBLON"
    if score >= SEUIL_RECOUVREMENT:
        return "RECOUVREMENT"
    return "NOUVEAU"


def candidats_proches(texte, k=5):
    """Retourne les k fiches les plus proches du texte candidat.

    Met l'index d'embeddings à jour au passage (incrémental), puis encode le
    candidat et calcule la similarité cosinus contre toutes les fiches.
    """
    index, _, _ = maj_index()
    vec = embed_texts([texte])[0]
    scores = []
    for slug, meta in index.items():
        if not meta.get("vector"):
            continue
        scores.append({
            "slug": slug,
            "titre": meta.get("titre", slug),
            "theme": meta.get("theme", ""),
            "score": round(cosine(vec, meta["vector"]), 4),
        })
    scores.sort(key=lambda x: x["score"], reverse=True)
    return scores[:k]


def analyser(texte, k=5):
    """Analyse complète d'un concept : top-k candidats + verdict global."""
    top = candidats_proches(texte, k=k)
    meilleur = top[0]["score"] if top else 0.0
    return {
        "verdict": verdict(meilleur),
        "meilleur_score": meilleur,
        "candidats": top,
    }


def main():
    ap = argparse.ArgumentParser(description="Détection de doublons sémantiques.")
    ap.add_argument("texte", nargs="?", help="Texte du concept candidat.")
    ap.add_argument("--file", help="Lire le texte depuis un fichier.")
    ap.add_argument("--k", type=int, default=5, help="Nombre de candidats (défaut 5).")
    ap.add_argument("--json", action="store_true", help="Sortie JSON brute.")
    args = ap.parse_args()

    if args.file:
        texte = open(args.file, encoding="utf-8").read()
    elif args.texte:
        texte = args.texte
    elif not sys.stdin.isatty():
        texte = sys.stdin.read()
    else:
        ap.error("fournir un texte, --file, ou un texte sur stdin.")

    texte = texte.strip()
    if not texte:
        ap.error("texte vide.")

    res = analyser(texte, k=args.k)

    if args.json:
        json.dump(res, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return

    sys.stdout.write(f"Verdict : {res['verdict']} (meilleur score {res['meilleur_score']})\n")
    sys.stdout.write(f"\n{args.k} fiches les plus proches :\n")
    for c in res["candidats"]:
        sys.stdout.write(f"  {c['score']:.4f}  [{c['theme']}]  {c['titre']}  ({c['slug']}.md)\n")


if __name__ == "__main__":
    main()
