#!/usr/bin/env python3
"""Structural validation of a note (quality gate "structure conformance").

Checks, without semantic judgement:
  - frontmatter: title, type (present — OKF), theme (∈ taxonomy), level (∈ 🔴🟡🟢), source_url (present, http)
  - body: "In one sentence" hook + judgement section + "See also" section
  - wikilinks: every link [..](slug.md) points to an existing note

Exit code 0 if compliant, 1 otherwise. Can lint one note, several, or the whole corpus.

Usage:
    python3 tools/kb_lint.py wiki/concepts/my-note.md   # one note
    python3 tools/kb_lint.py --all                      # whole corpus
    python3 tools/kb_lint.py --json wiki/concepts/x.md  # JSON output
"""
# kb_common is a sibling module, invisible to the hook's isolated type-checker.
# pyright: reportMissingImports=false
import os
import re
import sys
import glob
import json
import argparse

from kb_common import (CONCEPTS, THEMES, LEVELS, OBJECTIVES,
                       parse_frontmatter, split_note, note_objectives)

# Existing slugs, to validate wikilinks (computed on demand).
def existing_slugs():
    return {os.path.basename(p)[:-3] for p in glob.glob(os.path.join(CONCEPTS, "*.md"))}


def lint_note(path, slugs=None):
    """Validates a note. Returns (errors, warnings) — lists of str."""
    if slugs is None:
        slugs = existing_slugs()
    errors, warnings = [], []
    txt = open(path, encoding="utf-8", errors="replace").read()
    fm = parse_frontmatter(txt)
    _, body = split_note(txt)

    # --- Frontmatter ---
    if not fm:
        errors.append("missing or unreadable frontmatter")
        return errors, warnings  # pointless to continue without frontmatter

    if not fm.get("title", "").strip():
        errors.append("missing `title` field")
    if not fm.get("type", "").strip():
        errors.append("missing `type` field (required OKF — e.g. `Concept`)")
    theme = fm.get("theme", "").strip()
    if not theme:
        errors.append("missing `theme` field")
    elif theme not in THEMES:
        errors.append(f"off-taxonomy theme: \"{theme}\"")
    level = fm.get("level", "").strip()
    if level not in LEVELS:
        errors.append(f"invalid level: \"{level}\" (expected 🔴/🟡/🟢)")
    url = fm.get("source_url", "").strip()
    if not url:
        errors.append("missing `source_url` field (required)")
    elif not url.startswith(("http://", "https://")):
        errors.append(f"malformed source_url: \"{url}\"")
    for obj in note_objectives(fm):
        if obj not in OBJECTIVES:
            errors.append(f"off-vocabulary objective: \"{obj}\" (see OBJECTIVES in kb_common.py)")

    # --- Body: expected sections (tolerant of exact labels) ---
    if "**In one sentence**" not in body:
        errors.append('missing "**In one sentence**" hook')
    # Judgement section (the "so what"), tolerant of custom labels.
    if not re.search(r"##\s+(tradeoff|insight|why it matters|key points?|"
                     r"takeaways|when to use|summary)", body, re.IGNORECASE):
        warnings.append("judgement section (Tradeoff/Insight/Why it matters/"
                        "Key points/Takeaways/When to use/Summary) not detected")
    if not re.search(r"##\s+See also", body, re.IGNORECASE):
        warnings.append('missing "See also" section')

    # --- Wikilinks to other notes ---
    for m in re.finditer(r"\[[^\]]+\]\(([a-z0-9][a-z0-9\-]*)\.md\)", body):
        target = m.group(1)
        if target not in slugs:
            errors.append(f"broken wikilink: \"{target}.md\" (no such note)")

    return errors, warnings


def main():
    ap = argparse.ArgumentParser(description="Structural validation of notes.")
    ap.add_argument("paths", nargs="*", help="Notes to validate.")
    ap.add_argument("--all", action="store_true", help="Validate the whole corpus.")
    ap.add_argument("--json", action="store_true", help="JSON output.")
    args = ap.parse_args()

    if args.all:
        targets = sorted(glob.glob(os.path.join(CONCEPTS, "*.md")))
    elif args.paths:
        targets = args.paths
    else:
        ap.error("provide notes or --all.")

    slugs = existing_slugs()
    report = {}
    total_errors = 0
    for path in targets:
        err, warnings = lint_note(path, slugs)
        report[path] = {"errors": err, "warnings": warnings}
        total_errors += len(err)

    if args.json:
        json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        for path, r in report.items():
            if not r["errors"] and not r["warnings"]:
                if not args.all:
                    sys.stdout.write(f"✅ {os.path.relpath(path)} — compliant\n")
                continue
            sys.stdout.write(f"\n{os.path.relpath(path)}\n")
            for e in r["errors"]:
                sys.stdout.write(f"  ❌ {e}\n")
            for a in r["warnings"]:
                sys.stdout.write(f"  ⚠️  {a}\n")
        if args.all:
            sys.stdout.write(f"\n{total_errors} error(s) across {len(targets)} notes.\n")

    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
