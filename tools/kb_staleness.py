#!/usr/bin/env python3
"""Flags tool notes whose source-verification date is old or missing.

Each tool note (`wiki/tools/*.md`) ends with a `## Source` section, one line of
which carries a date such as *(verified on YYYY-MM-DD)*. This tool:
  - extracts that date via the regex `verified on (\\d{4}-\\d{2}-\\d{2})`;
  - computes its age in days against today (or `--today` for reproducible runs);
  - sorts each note into three buckets:
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

from kb_common import ROOT, TOOLS, CONCEPTS

DATE_RE = re.compile(r"verified on (\d{4}-\d{2}-\d{2})")


def extract_date(path):
    """Return the verification date (datetime.date) or None if missing/unreadable."""
    txt = open(path, encoding="utf-8", errors="replace").read()
    m = DATE_RE.search(txt)
    if not m:
        return None
    try:
        return datetime.date.fromisoformat(m.group(1))
    except ValueError:
        return None


def targets(include_concepts):
    """List of notes to analyze, excluding _TEMPLATE.md."""
    paths = glob.glob(os.path.join(TOOLS, "*.md"))
    if include_concepts:
        paths += glob.glob(os.path.join(CONCEPTS, "*.md"))
    return sorted(p for p in paths if os.path.basename(p) != "_TEMPLATE.md")


def main():
    ap = argparse.ArgumentParser(
        description="Flags notes whose source verification is old or missing."
    )
    ap.add_argument("--days", type=int, default=90,
                    help="Staleness threshold in days (default: 90).")
    ap.add_argument("--today", metavar="YYYY-MM-DD",
                    help="Frozen reference date (for reproducible runs).")
    ap.add_argument("--all", action="store_true",
                    help="Also analyze concept notes (concepts/).")
    args = ap.parse_args()

    if args.today:
        try:
            today = datetime.date.fromisoformat(args.today)
        except ValueError:
            ap.error(f"malformed --today: '{args.today}' (expected YYYY-MM-DD).")
    else:
        today = datetime.date.today()

    stale = []        # (path, date, age_days)
    undated = []      # paths
    nb_ok = 0

    for path in targets(args.all):
        d = extract_date(path)
        if d is None:
            undated.append(path)
            continue
        age = (today - d).days
        if age > args.days:
            stale.append((path, d, age))
        else:
            nb_ok += 1

    total = len(stale) + len(undated) + nb_ok

    print(f"Freshness check — reference {today.isoformat()}, "
          f"threshold {args.days} d, {total} note(s) analyzed.\n")

    stale.sort(key=lambda t: t[1])  # oldest first
    if stale:
        print(f"STALE ({len(stale)}) — older than {args.days} d:")
        for path, d, age in stale:
            print(f"  {os.path.relpath(path, ROOT)} — {d.isoformat()} — {age} d")
        print()

    if undated:
        print(f"UNDATED ({len(undated)}) — no 'verified on' date found:")
        for path in sorted(undated):
            print(f"  {os.path.relpath(path, ROOT)}")
        print()

    print(f"Summary: {nb_ok} OK · {len(stale)} stale · "
          f"{len(undated)} undated out of {total} note(s).")


if __name__ == "__main__":
    main()
