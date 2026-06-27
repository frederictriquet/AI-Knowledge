#!/usr/bin/env python3
"""Flags tool fiches whose source-verification date is old or missing.

Each tool fiche (`wiki/tools/*.md`) ends with a `## Source` section, one line of
which carries a date such as *(verified on YYYY-MM-DD)*. This tool:
  - extracts that date via the regex `verified on (\\d{4}-\\d{2}-\\d{2})`;
  - computes its age in days against today (or `--today` for reproducible runs);
  - sorts each fiche into three buckets:
      STALE     — date older than the threshold (`--days`, default 90);
      UNDATED   — no verification date found;
      OK        — date present and recent (counted only).

Purely informational tool: exit code is always 0.

Usage:
    python3 tools/kb_staleness.py                          # threshold 90 d, today's date
    python3 tools/kb_staleness.py --days 30                # custom threshold
    python3 tools/kb_staleness.py --today 2026-06-17       # frozen reference date
    python3 tools/kb_staleness.py --all                    # also include concepts/
"""
import os
import re
import glob
import argparse
import datetime

from kb_common import ROOT, FICHES_OUTILS, FICHES

DATE_RE = re.compile(r"verified on (\d{4}-\d{2}-\d{2})")


def extraire_date(path):
    """Retourne la date de vérification (datetime.date) ou None si absente/illisible."""
    txt = open(path, encoding="utf-8", errors="replace").read()
    m = DATE_RE.search(txt)
    if not m:
        return None
    try:
        return datetime.date.fromisoformat(m.group(1))
    except ValueError:
        return None


def cibles(inclure_concepts):
    """Liste des fiches à analyser, hors _TEMPLATE.md."""
    paths = glob.glob(os.path.join(FICHES_OUTILS, "*.md"))
    if inclure_concepts:
        paths += glob.glob(os.path.join(FICHES, "*.md"))
    return sorted(p for p in paths if os.path.basename(p) != "_TEMPLATE.md")


def main():
    ap = argparse.ArgumentParser(
        description="Flags fiches whose source verification is old or missing."
    )
    ap.add_argument("--days", type=int, default=90,
                    help="Staleness threshold in days (default: 90).")
    ap.add_argument("--today", metavar="YYYY-MM-DD",
                    help="Frozen reference date (for reproducible runs).")
    ap.add_argument("--all", action="store_true",
                    help="Also analyze concept fiches (concepts/).")
    args = ap.parse_args()

    if args.today:
        try:
            aujourdhui = datetime.date.fromisoformat(args.today)
        except ValueError:
            ap.error(f"malformed --today: '{args.today}' (expected YYYY-MM-DD).")
    else:
        aujourdhui = datetime.date.today()

    perimes = []      # (chemin, date, age_jours)
    non_dates = []    # chemins
    nb_ok = 0

    for path in cibles(args.all):
        d = extraire_date(path)
        if d is None:
            non_dates.append(path)
            continue
        age = (aujourdhui - d).days
        if age > args.days:
            perimes.append((path, d, age))
        else:
            nb_ok += 1

    total = len(perimes) + len(non_dates) + nb_ok

    print(f"Freshness check — reference {aujourdhui.isoformat()}, "
          f"threshold {args.days} d, {total} fiche(s) analyzed.\n")

    perimes.sort(key=lambda t: t[1])  # plus anciennes d'abord
    if perimes:
        print(f"STALE ({len(perimes)}) — older than {args.days} d:")
        for path, d, age in perimes:
            print(f"  {os.path.relpath(path, ROOT)} — {d.isoformat()} — {age} d")
        print()

    if non_dates:
        print(f"UNDATED ({len(non_dates)}) — no 'verified on' date found:")
        for path in sorted(non_dates):
            print(f"  {os.path.relpath(path, ROOT)}")
        print()

    print(f"Summary: {nb_ok} OK · {len(perimes)} stale · "
          f"{len(non_dates)} undated out of {total} fiche(s).")


if __name__ == "__main__":
    main()
