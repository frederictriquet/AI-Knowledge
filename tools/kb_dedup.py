#!/usr/bin/env python3
"""Duplicate detection by semantic similarity (stage 1 of the process).

Takes a candidate concept text (from a new article) and returns the closest
existing notes, with an indicative verdict based on thresholds. This verdict is
a PRE-FILTER: the final overlap judgement is delegated to the /enrich skill which
actually reads the candidate notes.

Thresholds (cosine similarity), empirically CALIBRATED on the corpus's nearest-
neighbour distribution for the multilingual MiniLM model (NN median ≈ 0.70,
most related corpus pairs ≈ 0.87):
    >= 0.85   probable DUPLICATE  — at the level of the most related corpus pairs
    0.75-0.85 OVERLAP             — neighbouring topic, to judge (merge? complement?)
    <  0.75   NEW                 — no close match, probably an original note
These thresholds depend on the model: recalibrate them if MODEL changes (see kb_embed.py).
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
from kb_embed import update_index, embed_texts

DUPLICATE_THRESHOLD = 0.85
OVERLAP_THRESHOLD = 0.75


def verdict(score):
    if score >= DUPLICATE_THRESHOLD:
        return "DUPLICATE"
    if score >= OVERLAP_THRESHOLD:
        return "OVERLAP"
    return "NEW"


def nearest_candidates(text, k=5):
    """Returns the k closest notes to the candidate text.

    Updates the embedding index along the way (incremental), then encodes the
    candidate and computes the cosine similarity against all notes.
    """
    index, _, _ = update_index()
    vec = embed_texts([text])[0]
    scores = []
    for slug, meta in index.items():
        if not meta.get("vector"):
            continue
        # Dedup = concept notes only (the index also covers tools).
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


def analyze(text, k=5):
    """Complete analysis of a concept: top-k candidates + global verdict."""
    top = nearest_candidates(text, k=k)
    best = top[0]["score"] if top else 0.0
    return {
        "verdict": verdict(best),
        "best_score": best,
        "candidates": top,
    }


def main():
    ap = argparse.ArgumentParser(description="Semantic duplicate detection.")
    ap.add_argument("text", nargs="?", help="Candidate concept text.")
    ap.add_argument("--file", help="Read the text from a file.")
    ap.add_argument("--k", type=int, default=5, help="Number of candidates (default 5).")
    ap.add_argument("--json", action="store_true", help="Raw JSON output.")
    args = ap.parse_args()

    if args.file:
        text = open(args.file, encoding="utf-8").read()
    elif args.text:
        text = args.text
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        ap.error("provide a text, --file, or text on stdin.")

    text = text.strip()
    if not text:
        ap.error("empty text.")

    res = analyze(text, k=args.k)

    if args.json:
        json.dump(res, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return

    sys.stdout.write(f"Verdict: {res['verdict']} (best score {res['best_score']})\n")
    sys.stdout.write(f"\nTop {args.k} closest notes:\n")
    for c in res["candidates"]:
        sys.stdout.write(f"  {c['score']:.4f}  [{c['theme']}]  {c['titre']}  ({c['slug']}.md)\n")


if __name__ == "__main__":
    main()
