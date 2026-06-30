#!/usr/bin/env python3
"""Generates a post preview from a randomly drawn fiche.

The corpus is designed to produce short posts (internal messaging, LinkedIn):
each fiche carries an "In one sentence" hook + a "learn more" link.
This script assembles that material into a ready-to-copy draft — no LLM, pure
deterministic assembly of the fiche's content.

Usage:
    python3 tools/kb_post.py                 # a random fiche
    python3 tools/kb_post.py --slug react    # a specific fiche
    python3 tools/kb_post.py --theme securite        # random within a theme
    python3 tools/kb_post.py --seed 42       # reproducible draw
    python3 tools/kb_post.py --format linkedin       # formatting variant
"""
# kb_common is a sibling module, invisible to the type-checker isolated from the hook.
# pyright: reportMissingImports=false
import re
import sys
import random
import argparse

from kb_common import charger_fiches, split_fiche, FICHES, FICHES_OUTILS

# H2 labels carrying the substance/context of the concept, by preference.
SECTIONS_SUBSTANCE = [
    r"In detail",
    r"What the source says",
    r"The idea",
    r"Key points",
]
# H2 labels carrying the "for a senior" insight, in order of preference.
SECTIONS_INSIGHT = [
    r"Tradeoff\s*/\s*insight \(for a senior\)",
    r"Tradeoff\s*/\s*when to use it",
    r"Tradeoff[^\n]*",
    r"Why it matters",
    r"Takeaways",
]


def extraire_accroche(corps):
    """Return the text of the "In one sentence" hook, or '' if absent."""
    m = re.search(r"\*\*In one sentence\*\*\s*[—–-]*\s*(.+?)(?:\n\s*\n|\n#)", corps, re.DOTALL)
    if not m:
        return ""
    return re.sub(r"\s+", " ", m.group(1)).strip()


def extraire_section(corps, motifs):
    """Return the 1st paragraph of the 1st H2 section whose title matches a pattern."""
    for motif in motifs:
        m = re.search(rf"^##\s+{motif}\s*\n+(.+?)(?:\n\s*\n|\n##|\Z)",
                      corps, re.DOTALL | re.MULTILINE | re.IGNORECASE)
        if m:
            return re.sub(r"\s+", " ", m.group(1)).strip()
    return ""


def hashtags(fm):
    """Build a few hashtags from the tags or, failing that, from the theme."""
    tags = fm.get("tags")
    if isinstance(tags, list) and tags:
        base = tags
    else:
        base = [fm.get("theme", "").replace("-", " ")]
    out = []
    for t in base[:4]:
        mot = re.sub(r"[^a-z0-9]", "", t.lower().replace(" ", ""))
        if mot:
            out.append("#" + mot)
    return " ".join(out)


def composer(fiche, style="interne"):
    """Assemble the post preview (str) from a loaded fiche."""
    fm, txt = fiche["fm"], fiche["txt"]
    _, corps = split_fiche(txt)
    titre = fm.get("title", fiche["slug"])
    accroche = extraire_accroche(corps) or "(no « In one sentence » hook in this fiche)"
    substance = extraire_section(corps, SECTIONS_SUBSTANCE)
    exemple = extraire_section(corps, [r"Example"])
    insight = extraire_section(corps, SECTIONS_INSIGHT)
    url = fm.get("source_url", "").strip()
    primaire = fm.get("primary_source", "").strip()

    lignes = []
    if style == "linkedin":
        lignes.append(f"💡 {titre}")
        lignes.append("")
        lignes.append(accroche)
        if substance:
            lignes.append("")
            lignes.append(substance)
        if exemple:
            lignes.append("")
            lignes.append(f"Example — {exemple}")
        if insight:
            lignes.append("")
            lignes.append(f"👉 {insight}")
        lignes.append("")
        if url:
            lignes.append(f"🔗 Learn more: {url}")
        if primaire:
            lignes.append(f"📄 Primary source: {primaire}")
        ht = hashtags(fm)
        if ht:
            lignes.append("")
            lignes.append(ht)
    else:  # internal messaging: shorter, more direct
        lignes.append(f"**{titre}** — {accroche}")
        if substance:
            lignes.append("")
            lignes.append(substance)
        if exemple:
            lignes.append("")
            lignes.append(f"Example — {exemple}")
        if insight:
            lignes.append("")
            lignes.append(f"Takeaway: {insight}")
        if url:
            lignes.append("")
            lignes.append(f"→ Learn more: {url}")
    return "\n".join(lignes)


def choisir(fiches, slug=None, theme=None):
    """Select a fiche (by slug, or at random, optionally filtered by theme)."""
    if slug:
        for f in fiches:
            if f["slug"] == slug:
                return f
        sys.exit(f"❌ fiche not found: « {slug} »")
    pool = [f for f in fiches if not theme or f["fm"].get("theme") == theme]
    if not pool:
        sys.exit(f"❌ no fiche for theme « {theme} »")
    # Purely editorial draw (post preview): no cryptographic stakes.
    return random.choice(pool)  # noqa: S311


def main():
    ap = argparse.ArgumentParser(description="Preview de post depuis une fiche.")
    ap.add_argument("--slug", help="Fiche précise (sinon tirage au hasard).")
    ap.add_argument("--theme", help="Restreindre le tirage à un thème.")
    ap.add_argument("--seed", type=int, help="Graine pour un tirage reproductible.")
    ap.add_argument("--format", choices=["interne", "linkedin"], default="interne",
                    help="Style de mise en forme (défaut : interne).")
    args = ap.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    # Posts can be drawn from concepts (fiches/) as well as tool fiches
    # (fiches outils/): both directories are scanned.
    fiches = charger_fiches([FICHES, FICHES_OUTILS])
    if not fiches:
        sys.exit("❌ no fiche in the corpus.")

    fiche = choisir(fiches, slug=args.slug, theme=args.theme)
    post = composer(fiche, style=args.format)

    # Decoration (header + bars) on stderr, bare post on stdout: a `> file`
    # or a pipe captures only the post, with no spurious prefix or border.
    # Explicit flush so the order stays correct on screen despite the double
    # buffering of stdout/stderr.
    barre = "─" * 60
    sys.stderr.write(f"preview ({args.format}) · {fiche['slug']}.md\n{barre}\n")
    sys.stderr.flush()
    sys.stdout.write(post + "\n")
    sys.stdout.flush()
    sys.stderr.write(barre + "\n")
    sys.stderr.flush()


if __name__ == "__main__":
    main()
