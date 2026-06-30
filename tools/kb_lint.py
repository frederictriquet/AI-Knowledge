#!/usr/bin/env python3
"""Structural validation of a fiche (quality gate « structure conformance »).

Checks, without semantic judgement:
  - frontmatter: title, type (present — OKF), theme (∈ taxonomy), level (∈ 🔴🟡🟢), source_url (present, http)
  - body: « In one sentence » hook + judgement section + « See also » section
  - wikilinks: every link [..](slug.md) points to an existing fiche

Exit code 0 if conformant, 1 otherwise. Can lint one fiche, several, or the whole corpus.

Usage:
    python3 tools/kb_lint.py wiki/concepts/ma-fiche.md   # one fiche
    python3 tools/kb_lint.py --all                       # whole corpus
    python3 tools/kb_lint.py --json wiki/concepts/x.md   # JSON output
"""
# kb_common is a sibling module, invisible to the hook's isolated type-checker.
# pyright: reportMissingImports=false
import os
import re
import sys
import glob
import json
import argparse

from kb_common import (FICHES, THEMES, NIVEAUX, OBJECTIVES,
                       parse_frontmatter, split_fiche, objectives_fiche)

# Existing slugs, to validate wikilinks (computed on demand).
def slugs_existants():
    return {os.path.basename(p)[:-3] for p in glob.glob(os.path.join(FICHES, "*.md"))}


def lint_fiche(path, slugs=None):
    """Validates a fiche. Returns (errors, warnings) — lists of str."""
    if slugs is None:
        slugs = slugs_existants()
    erreurs, avert = [], []
    txt = open(path, encoding="utf-8", errors="replace").read()
    fm = parse_frontmatter(txt)
    _, corps = split_fiche(txt)

    # --- Frontmatter ---
    if not fm:
        erreurs.append("missing or unreadable frontmatter")
        return erreurs, avert  # pointless to continue without frontmatter

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

    # --- Body: expected sections (tolerant of exact labels) ---
    if "**In one sentence**" not in corps:
        erreurs.append("missing « **In one sentence** » hook")
    # Judgement section (the « so what »), tolerant of custom labels.
    if not re.search(r"##\s+(tradeoff|insight|why it matters|key points?|"
                     r"takeaways|when to use|summary)", corps, re.IGNORECASE):
        avert.append("judgement section (Tradeoff/Insight/Why it matters/"
                     "Key points/Takeaways/When to use/Summary) not detected")
    if not re.search(r"##\s+See also", corps, re.IGNORECASE):
        avert.append("missing « See also » section")

    # --- Wikilinks to other fiches ---
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
