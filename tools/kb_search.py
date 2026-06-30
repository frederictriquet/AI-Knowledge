#!/usr/bin/env python3
"""Local hybrid search in the corpus (concepts + tools), no LLM.

Combines two normalized signals (max→1) then summed, 100% local, no key:
  - lexical: in-house TF-IDF on title (over-weighted) + body;
  - semantic: cosine query↔note via the fastembed index (kb_embed).
A small bonus is added if the query overlaps a theme slug of the note.
The index covers both corpora (cf. kb_embed).

Usage:
    python3 tools/kb_search.py "how to limit token consumption"
    python3 tools/kb_search.py "vector database agent" --k 8
    python3 tools/kb_search.py "code review" --only tool --json
"""
# kb_embed/kb_common depend on the venv and on sibling imports, invisible to the hook.
# pyright: reportMissingImports=false
import re
import sys
import json
import math
import argparse
import unicodedata
from collections import defaultdict

import numpy as np
from kb_common import CONCEPTS, TOOLS, load_notes, note_body, cosine
from kb_embed import update_index, embed_texts

# Fusion weights (scores already normalized to [0,1] before weighting).
W_SEMANTIC = 0.55
W_LEXICAL = 0.45
W_THEME = 0.10          # small theme bonus, tie-breaker at the margin
TITLE_WEIGHT = 3.0      # one occurrence in the title counts as 3 in the body

# English function words with no discriminating value for the lexical signal.
STOPWORDS = {
    "the", "a", "an", "of", "to", "for", "and", "or", "in", "on", "at", "by",
    "with", "without", "from", "as", "is", "are", "be", "this", "that", "these",
    "those", "it", "its", "how", "what", "which", "who", "whom", "my", "i",
    "you", "your", "we", "our", "more", "less", "like", "into", "over", "than",
}


def normalize(text):
    """Lowercase + accent stripping (robust comparison)."""
    text = unicodedata.normalize("NFKD", text.lower())
    return "".join(c for c in text if not unicodedata.combining(c))


def strip_suffix(word):
    """Minimal stemming: unifies FR/EN singular/plural (token/tokens, agents/agent).

    Folds a few common suffixes to improve recall with no dependency.
    """
    for suf in ("aux", "es", "s", "x"):
        if len(word) - len(suf) >= 3 and word.endswith(suf):
            return word[: -len(suf)]
    return word


def tokens(text):
    """Tokenize into significant alphanumeric words (no stopwords, suffix-stripped)."""
    raw = re.findall(r"[a-z0-9]+", normalize(text))
    return [strip_suffix(t) for t in raw if t not in STOPWORDS and len(t) > 1]


def build_lexical(notes):
    """Pre-computes, per note, the token counts (title, body) + the global IDF."""
    docs = {}
    df = {}
    for f in notes:
        title = f["fm"].get("title", f["slug"])
        body = note_body(f["txt"])
        ct_title, ct_body = {}, {}
        for t in tokens(title):
            ct_title[t] = ct_title.get(t, 0) + 1
        for t in tokens(body):
            ct_body[t] = ct_body.get(t, 0) + 1
        docs[f["slug"]] = (ct_title, ct_body)
        for t in set(ct_title) | set(ct_body):
            df[t] = df.get(t, 0) + 1
    n = len(notes) or 1
    idf = {t: math.log(1 + n / c) for t, c in df.items()}
    return docs, idf


def score_lexical(qtok, ct_title, ct_body, idf):
    """TF-IDF lexical score of a note for the query tokens (title over-weighted)."""
    s = 0.0
    for t in qtok:
        weight = idf.get(t)
        if not weight:
            continue
        tf = ct_title.get(t, 0) * TITLE_WEIGHT + ct_body.get(t, 0)
        if tf:
            s += weight * (1 + math.log(tf))      # logarithmic saturation of TF
    return s


def theme_centroids(index):
    """Centroid (mean vector) of each theme, over all indexed notes."""
    by_theme = defaultdict(list)
    for meta in index.values():
        v = meta.get("vector")
        if v:
            for th in meta.get("themes", []):
                by_theme[th].append(v)
    return {th: np.mean(vs, axis=0) for th, vs in by_theme.items() if vs}


def search(query, only=None):
    """Return all notes carrying a signal, ranked by hybrid score."""
    notes = load_notes([CONCEPTS, TOOLS])
    index, _, _ = update_index()
    qtok = tokens(query)
    qvec = embed_texts([query])[0]
    docs, idf = build_lexical(notes)
    # Semantic proximity query↔theme: boosts notes of a theme close to the subject.
    theme_qsim = {th: cosine(qvec, c) for th, c in theme_centroids(index).items()}

    raw = []
    for f in notes:
        if only and f["corpus"] != only:
            continue
        meta = index.get(f["slug"])
        sem = cosine(qvec, meta["vector"]) if meta and meta.get("vector") else 0.0
        ct_title, ct_body = docs[f["slug"]]
        lex = score_lexical(qtok, ct_title, ct_body, idf)
        thm = max((theme_qsim.get(t, 0.0) for t in f["themes"]), default=0.0)
        raw.append({
            "slug": f["slug"], "corpus": f["corpus"], "themes": f["themes"],
            "title": f["fm"].get("title", f["slug"]),
            "_sem": sem, "_lex": lex, "_thm": thm,
        })

    # Max→1 normalization per signal, then weighted fusion.
    max_sem = max((b["_sem"] for b in raw), default=0.0) or 1.0
    max_lex = max((b["_lex"] for b in raw), default=0.0) or 1.0
    max_thm = max((b["_thm"] for b in raw), default=0.0) or 1.0
    for b in raw:
        b["score"] = round(
            W_SEMANTIC * (b["_sem"] / max_sem)
            + W_LEXICAL * (b["_lex"] / max_lex)
            + W_THEME * (b["_thm"] / max_thm), 4)
    raw.sort(key=lambda b: b["score"], reverse=True)
    # Keep only notes carrying a signal (avoids listing the whole corpus at 0).
    results = [b for b in raw if b["_lex"] > 0 or b["_sem"] > 0]
    for b in results:
        for key in ("_sem", "_lex", "_thm"):
            b.pop(key, None)
    return results


def main():
    ap = argparse.ArgumentParser(description="Local hybrid search (concepts + tools, 0 LLM).")
    ap.add_argument("query", nargs="?", help="Free-form query.")
    ap.add_argument("--k", type=int, default=8, help="Number of results per section (default 8).")
    ap.add_argument("--only", choices=["concept", "tool"], help="Restrict to one corpus (single list).")
    ap.add_argument("--json", action="store_true", help="Raw JSON output (merged list).")
    args = ap.parse_args()

    if args.query:
        query = args.query
    elif not sys.stdin.isatty():
        query = sys.stdin.read()
    else:
        ap.error("provide a query (argument or stdin).")
    query = query.strip()
    if not query:
        ap.error("empty query.")

    res = search(query, only=args.only)

    if args.json:
        json.dump(res[: args.k] if args.only else res, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return

    if not res:
        sys.stdout.write("No results.\n")
        return

    def line(b):
        th = (" · " + ", ".join(b["themes"])) if b["themes"] else ""
        return f"  {b['score']:.3f}  {b['title']}  ({b['slug']}){th}\n"

    sys.stdout.write(f'Search: "{query}"\n')
    if args.only:
        sys.stdout.write("\n")
        for b in res[: args.k]:
            sys.stdout.write(line(b))
        return
    # Two sections: guarantees the presence of both concepts AND tools.
    concepts = [b for b in res if b["corpus"] == "concept"][: args.k]
    tools = [b for b in res if b["corpus"] == "tool"][: args.k]
    sys.stdout.write(f"\n📄 Concepts ({len(concepts)})\n")
    for b in concepts:
        sys.stdout.write(line(b))
    sys.stdout.write(f"\n🛠️  Tools ({len(tools)})\n")
    for b in tools:
        sys.stdout.write(line(b))


if __name__ == "__main__":
    main()
