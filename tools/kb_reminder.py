#!/usr/bin/env python3
"""Short (one-liner) reminder if tool fiches need refreshing.

Designed for a **SessionStart** hook: prints **nothing** if there is nothing to
report (empty output = no noise). Reuses the logic of `kb_staleness.py`
(no duplication): stale = "verified on" older than the threshold, or missing.

Usage: python3 tools/kb_reminder.py   (threshold 90 d, fiches outils/ only)
"""
import os
import sys
import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_staleness import extraire_date, cibles  # noqa: E402

SEUIL = 90


def main():
    today = datetime.date.today()
    perimes = non_dates = 0
    for path in cibles(False):  # fiches outils/ only
        d = extraire_date(path)
        if d is None:
            non_dates += 1
        elif (today - d).days > SEUIL:
            perimes += 1
    n = perimes + non_dates
    if n:
        print(
            f"⚠️ KB — {n} fiche(s) outil à rafraîchir "
            f"({perimes} périmée(s) >{SEUIL} j, {non_dates} non datée(s)) "
            f"→ lance /kb:refresh"
        )


if __name__ == "__main__":
    main()
