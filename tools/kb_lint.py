#!/usr/bin/env python3
"""Validation structurelle d'une fiche (gate qualité « conformité de structure »).

Vérifie, sans jugement sémantique :
  - frontmatter : title, type (présent — OKF), theme (∈ taxonomie), level (∈ 🔴🟡🟢), source_url (présent, http)
  - corps : accroche « In one sentence » + section de jugement + section « See also »
  - wikilinks : chaque lien [..](slug.md) pointe vers une fiche existante

Exit code 0 si conforme, 1 sinon. Peut linter une fiche, plusieurs, ou tout le corpus.

Usage :
    python3 tools/kb_lint.py wiki/concepts/ma-fiche.md   # une fiche
    python3 tools/kb_lint.py --all                       # tout le corpus
    python3 tools/kb_lint.py --json wiki/concepts/x.md   # sortie JSON
"""
# kb_common est un module frère, invisible au type-checker isolé du hook.
# pyright: reportMissingImports=false
import os
import re
import sys
import glob
import json
import argparse

from kb_common import (FICHES, THEMES, NIVEAUX, OBJECTIVES,
                       parse_frontmatter, split_fiche, objectives_fiche)

# Slugs existants, pour valider les wikilinks (calculé à la demande).
def slugs_existants():
    return {os.path.basename(p)[:-3] for p in glob.glob(os.path.join(FICHES, "*.md"))}


def lint_fiche(path, slugs=None):
    """Valide une fiche. Retourne (erreurs, avertissements) — listes de str."""
    if slugs is None:
        slugs = slugs_existants()
    erreurs, avert = [], []
    txt = open(path, encoding="utf-8", errors="replace").read()
    fm = parse_frontmatter(txt)
    _, corps = split_fiche(txt)

    # --- Frontmatter ---
    if not fm:
        erreurs.append("missing or unreadable frontmatter")
        return erreurs, avert  # inutile de continuer sans frontmatter

    if not fm.get("title", "").strip():
        erreurs.append("missing `title` field")
    if not fm.get("type", "").strip():
        erreurs.append("missing `type` field (required OKF — e.g. `Concept`)")
    theme = fm.get("theme", "").strip()
    if not theme:
        erreurs.append("missing `theme` field")
    elif theme not in THEMES:
        erreurs.append(f"theme outside taxonomy: « {theme} »")
    level = fm.get("level", "").strip()
    if level not in NIVEAUX:
        erreurs.append(f"invalid level: « {level} » (expected 🔴/🟡/🟢)")
    url = fm.get("source_url", "").strip()
    if not url:
        erreurs.append("missing `source_url` field (required)")
    elif not url.startswith(("http://", "https://")):
        erreurs.append(f"malformed source_url: « {url} »")
    for obj in objectives_fiche(fm):
        if obj not in OBJECTIVES:
            erreurs.append(f"objective outside vocabulary: « {obj} » (see OBJECTIVES in kb_common.py)")

    # --- Corps : sections attendues (tolérant sur les libellés exacts) ---
    if "**In one sentence**" not in corps:
        erreurs.append("missing « **In one sentence** » hook")
    # Section de jugement (le « so what »), tolérante aux libellés maison.
    if not re.search(r"##\s+(tradeoff|insight|why it matters|key points?|"
                     r"takeaways|when to use|summary)", corps, re.IGNORECASE):
        avert.append("judgement section (Tradeoff/Insight/Why it matters/"
                     "Key points/Takeaways/When to use/Summary) not detected")
    if not re.search(r"##\s+See also", corps, re.IGNORECASE):
        avert.append("missing « See also » section")

    # --- Wikilinks vers d'autres fiches ---
    for m in re.finditer(r"\[[^\]]+\]\(([a-z0-9][a-z0-9\-]*)\.md\)", corps):
        cible = m.group(1)
        if cible not in slugs:
            erreurs.append(f"broken wikilink: « {cible}.md » (no such fiche)")

    return erreurs, avert


def main():
    ap = argparse.ArgumentParser(description="Structural validation of fiches.")
    ap.add_argument("paths", nargs="*", help="Fiches to validate.")
    ap.add_argument("--all", action="store_true", help="Validate the whole corpus.")
    ap.add_argument("--json", action="store_true", help="JSON output.")
    args = ap.parse_args()

    if args.all:
        cibles = sorted(glob.glob(os.path.join(FICHES, "*.md")))
    elif args.paths:
        cibles = args.paths
    else:
        ap.error("provide fiches or --all.")

    slugs = slugs_existants()
    rapport = {}
    total_err = 0
    for path in cibles:
        err, avert = lint_fiche(path, slugs)
        rapport[path] = {"erreurs": err, "avertissements": avert}
        total_err += len(err)

    if args.json:
        json.dump(rapport, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        for path, r in rapport.items():
            if not r["erreurs"] and not r["avertissements"]:
                if not args.all:
                    sys.stdout.write(f"✅ {os.path.relpath(path)} — conforme\n")
                continue
            sys.stdout.write(f"\n{os.path.relpath(path)}\n")
            for e in r["erreurs"]:
                sys.stdout.write(f"  ❌ {e}\n")
            for a in r["avertissements"]:
                sys.stdout.write(f"  ⚠️  {a}\n")
        if args.all:
            sys.stdout.write(f"\n{total_err} error(s) across {len(cibles)} fiches.\n")

    sys.exit(1 if total_err else 0)


if __name__ == "__main__":
    main()
