#!/usr/bin/env python3
"""Duplicate detection by semantic similarity (stage 1 of the process).

Takes a candidate concept text (from a new article) and returns the closest
existing fiches, with an indicative verdict based on thresholds. This verdict is
a PRE-FILTER: the final overlap judgement is delegated to the /enrich skill which
actually reads the candidate fiches.

Thresholds (cosine similarity), empirically CALIBRATED on the corpus's nearest-
neighbour distribution for the multilingual MiniLM model (NN median ≈ 0.70,
most related corpus pairs ≈ 0.87):
    >= 0.85   probable DUPLICATE  — at the level of the most related corpus pairs
    0.75-0.85 OVERLAP             — neighbouring topic, to judge (merge? complement?)
    <  0.75   NEW                 — no close match, probably an original fiche
These thresholds depend on the model: recalibrate them if MODELE changes (see kb_embed.py).
The verdict is only a pre-filter — the final judgement belongs to the /enrich skill.

Usage:
    python3 tools/kb_dedup.py "candidate concept text"
    python3 tools/kb_dedup.py --file concept.txt --k 5
    echo "text" | python3 tools/kb_dedup.py --json
"""
# kb_embed/kb_common depend on the venv and sibling imports, invisible to the hook.
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
        return "DUPLICATE"
    if score >= SEUIL_RECOUVREMENT:
        return "OVERLAP"
    return "NEW"


def candidats_proches(texte, k=5):
    """Returns the k closest fiches to the candidate text.

    Updates the embedding index along the way (incremental), then encodes the
    candidate and computes the cosine similarity against all fiches.
    """
    index, _, _ = maj_index()
    vec = embed_texts([texte])[0]
    scores = []
    for slug, meta in index.items():
        if not meta.get("vector"):
            continue
        # Dedup = concept fiches only (the index also covers tools).
        if meta.get("corpus", "concept") != "concept":
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
    """Complete analysis of a concept: top-k candidates + global verdict."""
    top = candidats_proches(texte, k=k)
    meilleur = top[0]["score"] if top else 0.0
    return {
        "verdict": verdict(meilleur),
        "meilleur_score": meilleur,
        "candidats": top,
    }


def main():
    ap = argparse.ArgumentParser(description="Semantic duplicate detection.")
    ap.add_argument("texte", nargs="?", help="Candidate concept text.")
    ap.add_argument("--file", help="Read the text from a file.")
    ap.add_argument("--k", type=int, default=5, help="Number of candidates (default 5).")
    ap.add_argument("--json", action="store_true", help="Raw JSON output.")
    args = ap.parse_args()

    if args.file:
        texte = open(args.file, encoding="utf-8").read()
    elif args.texte:
        texte = args.texte
    elif not sys.stdin.isatty():
        texte = sys.stdin.read()
    else:
        ap.error("provide a text, --file, or text on stdin.")

    texte = texte.strip()
    if not texte:
        ap.error("empty text.")

    res = analyser(texte, k=args.k)

    if args.json:
        json.dump(res, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return

    sys.stdout.write(f"Verdict: {res['verdict']} (best score {res['meilleur_score']})\n")
    sys.stdout.write(f"\nTop {args.k} closest fiches:\n")
    for c in res["candidats"]:
        sys.stdout.write(f"  {c['score']:.4f}  [{c['theme']}]  {c['titre']}  ({c['slug']}.md)\n")


if __name__ == "__main__":
    main()
