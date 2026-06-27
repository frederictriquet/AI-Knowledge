#!/usr/bin/env python3
"""Génère une preview de post à partir d'une fiche tirée au hasard.

Le corpus est pensé pour produire des posts courts (messagerie interne, LinkedIn) :
chaque fiche porte une accroche « In one sentence » + un lien « learn more ».
Ce script assemble cette matière en un brouillon prêt à copier — sans LLM, pur
montage déterministe du contenu de la fiche.

Usage :
    python3 tools/kb_post.py                 # une fiche au hasard
    python3 tools/kb_post.py --slug react    # une fiche précise
    python3 tools/kb_post.py --theme securite        # au hasard dans un thème
    python3 tools/kb_post.py --seed 42       # tirage reproductible
    python3 tools/kb_post.py --format linkedin       # variante de mise en forme
"""
# kb_common est un module frère, invisible au type-checker isolé du hook.
# pyright: reportMissingImports=false
import re
import sys
import random
import argparse

from kb_common import charger_fiches, split_fiche, FICHES, FICHES_OUTILS

# Libellés H2 qui portent la substance/contexte du concept, par préférence.
SECTIONS_SUBSTANCE = [
    r"In detail",
    r"What the source says",
    r"The idea",
    r"Key points",
]
# Libellés H2 qui portent l'insight « pour senior », par ordre de préférence.
SECTIONS_INSIGHT = [
    r"Tradeoff\s*/\s*insight \(for a senior\)",
    r"Tradeoff\s*/\s*when to use it",
    r"Tradeoff[^\n]*",
    r"Why it matters",
    r"Takeaways",
]


def extraire_accroche(corps):
    """Retourne le texte de l'accroche « In one sentence », ou '' si absente."""
    m = re.search(r"\*\*In one sentence\*\*\s*[—–-]*\s*(.+?)(?:\n\s*\n|\n#)", corps, re.DOTALL)
    if not m:
        return ""
    return re.sub(r"\s+", " ", m.group(1)).strip()


def extraire_section(corps, motifs):
    """Retourne le 1er paragraphe de la 1re section H2 dont le titre matche un motif."""
    for motif in motifs:
        m = re.search(rf"^##\s+{motif}\s*\n+(.+?)(?:\n\s*\n|\n##|\Z)",
                      corps, re.DOTALL | re.MULTILINE | re.IGNORECASE)
        if m:
            return re.sub(r"\s+", " ", m.group(1)).strip()
    return ""


def hashtags(fm):
    """Construit quelques hashtags à partir des tags ou, à défaut, du thème."""
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
    """Assemble la preview de post (str) à partir d'une fiche chargée."""
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
    else:  # messagerie interne : plus court, plus direct
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
    """Sélectionne une fiche (par slug, ou au hasard, éventuellement filtrée par thème)."""
    if slug:
        for f in fiches:
            if f["slug"] == slug:
                return f
        sys.exit(f"❌ fiche not found: « {slug} »")
    pool = [f for f in fiches if not theme or f["fm"].get("theme") == theme]
    if not pool:
        sys.exit(f"❌ no fiche for theme « {theme} »")
    # Tirage purement éditorial (preview de post) : aucun enjeu cryptographique.
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

    # Les posts peuvent être tirés des concepts (fiches/) comme des fiches outils
    # (fiches outils/) : on scanne les deux répertoires.
    fiches = charger_fiches([FICHES, FICHES_OUTILS])
    if not fiches:
        sys.exit("❌ no fiche in the corpus.")

    fiche = choisir(fiches, slug=args.slug, theme=args.theme)
    post = composer(fiche, style=args.format)

    # Décor (en-tête + barres) sur stderr, post nu sur stdout : un `> fichier`
    # ou un pipe ne capture que le post, sans préfixe ni bordure parasites.
    # Flush explicite pour que l'ordre reste correct à l'écran malgré le double
    # buffering stdout/stderr.
    barre = "─" * 60
    sys.stderr.write(f"preview ({args.format}) · {fiche['slug']}.md\n{barre}\n")
    sys.stderr.flush()
    sys.stdout.write(post + "\n")
    sys.stdout.flush()
    sys.stderr.write(barre + "\n")
    sys.stderr.flush()


if __name__ == "__main__":
    main()
