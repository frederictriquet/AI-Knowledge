#!/usr/bin/env python3
"""Short (one-liner) reminder if tool notes need refreshing.

Designed for a **SessionStart** hook: prints **nothing** if there is nothing to
report (empty output = no noise). Reuses the logic of `kb_staleness.py`
(no duplication): stale = "verified on" older than the threshold, or missing.

Usage: python3 tools/kb_reminder.py   (threshold 90 d, tools/ only)
"""
import os
import sys
import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_staleness import extract_date, targets  # noqa: E402

THRESHOLD = 90


def main():
    today = datetime.date.today()
    stale = undated = 0
    for path in targets(False):  # tools/ only
        d = extract_date(path)
        if d is None:
            undated += 1
        elif (today - d).days > THRESHOLD:
            stale += 1
    n = stale + undated
    if n:
        print(
            f"⚠️ KB — {n} tool note(s) to refresh "
            f"({stale} stale >{THRESHOLD} d, {undated} undated) "
            f"→ run /kb:refresh"
        )


if __name__ == "__main__":
    main()
