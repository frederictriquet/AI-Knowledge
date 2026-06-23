#!/usr/bin/env python3
"""Validation structurelle d'une fiche (gate qualité « conformité de structure »).

Vérifie, sans jugement sémantique :
  - frontmatter : titre, type (présent — OKF), theme (∈ taxonomie), niveau (∈ 🔴🟡🟢), source_url (présent, http)
  - corps : accroche « En une phrase » + section tradeoff/insight + section « Voir aussi »
  - wikilinks : chaque lien [..](slug.md) pointe vers une fiche existante

Exit code 0 si conforme, 1 sinon. Peut linter une fiche, plusieurs, ou tout le corpus.

Usage :
    python3 tools/kb_lint.py fiches/ma-fiche.md      # une fiche
    python3 tools/kb_lint.py --all                   # tout le corpus
    python3 tools/kb_lint.py --json fiches/x.md      # sortie JSON
"""
# kb_common est un module frère, invisible au type-checker isolé du hook.
# pyright: reportMissingImports=false
import os
import re
import sys
import glob
import json
import argparse

from kb_common import FICHES, THEMES, NIVEAUX, parse_frontmatter, split_fiche

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
        erreurs.append("frontmatter absent ou illisible")
        return erreurs, avert  # inutile de continuer sans frontmatter

    if not fm.get("titre", "").strip():
        erreurs.append("champ `titre` manquant")
    if not fm.get("type", "").strip():
        erreurs.append("champ `type` manquant (obligatoire OKF — ex. `Concept`)")
    theme = fm.get("theme", "").strip()
    if not theme:
        erreurs.append("champ `theme` manquant")
    elif theme not in THEMES:
        erreurs.append(f"thème hors taxonomie : « {theme} »")
    niveau = fm.get("niveau", "").strip()
    if niveau not in NIVEAUX:
        erreurs.append(f"niveau invalide : « {niveau} » (attendu 🔴/🟡/🟢)")
    url = fm.get("source_url", "").strip()
    if not url:
        erreurs.append("champ `source_url` manquant (obligatoire)")
    elif not url.startswith(("http://", "https://")):
        erreurs.append(f"source_url mal formé : « {url} »")

    # --- Corps : sections attendues (tolérant sur les libellés exacts) ---
    if "**En une phrase**" not in corps:
        erreurs.append("accroche « **En une phrase** » manquante")
    if not re.search(r"##\s+(Tradeoff|Insight)", corps, re.IGNORECASE):
        avert.append("section « Tradeoff / insight » non détectée")
    if not re.search(r"##\s+Voir aussi", corps, re.IGNORECASE):
        avert.append("section « Voir aussi » manquante")

    # --- Wikilinks vers d'autres fiches ---
    for m in re.finditer(r"\[[^\]]+\]\(([a-z0-9][a-z0-9\-]*)\.md\)", corps):
        cible = m.group(1)
        if cible not in slugs:
            erreurs.append(f"wikilink cassé : « {cible}.md » (fiche inexistante)")

    return erreurs, avert


def main():
    ap = argparse.ArgumentParser(description="Validation structurelle des fiches.")
    ap.add_argument("paths", nargs="*", help="Fiches à valider.")
    ap.add_argument("--all", action="store_true", help="Valider tout le corpus.")
    ap.add_argument("--json", action="store_true", help="Sortie JSON.")
    args = ap.parse_args()

    if args.all:
        cibles = sorted(glob.glob(os.path.join(FICHES, "*.md")))
    elif args.paths:
        cibles = args.paths
    else:
        ap.error("fournir des fiches ou --all.")

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
            sys.stdout.write(f"\n{total_err} erreur(s) sur {len(cibles)} fiches.\n")

    sys.exit(1 if total_err else 0)


if __name__ == "__main__":
    main()
