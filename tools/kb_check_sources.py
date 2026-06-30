#!/usr/bin/env python3
"""Factual verification of a concept's sources (the "sources" quality gate).

For each concept:
  - `source_url`: does the page respond (HTTP < 400)?
  - cited arXiv identifier (frontmatter or body, e.g. arXiv:2210.03629): does the
    page https://arxiv.org/abs/<id> exist, and is its title consistent with the
    paper title cited in the concept? (same logic as SOURCES-PRIMAIRES.md)

Network required. Requests have a timeout; a network failure is reported without
hiding the result (never a silent except).

Usage:
    python3 tools/kb_check_sources.py wiki/concepts/react.md
    python3 tools/kb_check_sources.py --all --json
"""
# kb_common is a sibling module; requests lives in tools/.venv. Invisible to the hook.
# pyright: reportMissingImports=false
import os
import re
import sys
import glob
import json
import html
import argparse

import requests

from kb_common import CONCEPTS, parse_frontmatter

TIMEOUT = 12
HEADERS = {"User-Agent": "AI-Knowledge-source-checker/1.0"}
ARXIV_RE = re.compile(r"arxiv[:/]?\s*(\d{4}\.\d{4,5})", re.IGNORECASE)


def _norm(s):
    """Normalise a title for loose comparison (lowercase, collapsed spaces)."""
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", s.lower())).strip()


def verify_url(url):
    """Return (ok: bool, detail: str). Try HEAD then GET as a fallback."""
    try:
        r = requests.head(url, timeout=TIMEOUT, headers=HEADERS, allow_redirects=True)
        if r.status_code >= 400:  # some servers reject HEAD → fall back to GET
            r = requests.get(url, timeout=TIMEOUT, headers=HEADERS, allow_redirects=True)
        return (r.status_code < 400, f"HTTP {r.status_code}")
    except requests.RequestException as e:
        return (False, f"network: {type(e).__name__}")


def arxiv_title(arxiv_id):
    """Return (ok, title_or_error) for an arXiv identifier via the official API."""
    api = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    try:
        r = requests.get(api, timeout=TIMEOUT, headers=HEADERS)
    except requests.RequestException as e:
        return (False, f"network: {type(e).__name__}")
    if r.status_code >= 400:
        return (False, f"HTTP {r.status_code}")
    m = re.search(r"<entry>.*?<title>(.*?)</title>", r.text, re.DOTALL)
    if not m:
        return (False, "id not found on arXiv")
    return (True, html.unescape(m.group(1).strip()))


def verify_note(path):
    """Verify source_url + arXiv of a concept. Return a dict of results."""
    txt = open(path, encoding="utf-8", errors="replace").read()
    fm = parse_frontmatter(txt)
    res = {"slug": os.path.basename(path)[:-3], "checks": []}

    url = fm.get("source_url", "").strip()
    if url:
        ok, detail = verify_url(url)
        res["checks"].append({"type": "source_url", "ok": ok, "detail": detail, "ref": url})
    else:
        res["checks"].append({"type": "source_url", "ok": False, "detail": "missing", "ref": ""})

    # arXiv: take the first id found (frontmatter primary_source or body).
    m = ARXIV_RE.search(txt)
    if m:
        arxiv_id = m.group(1)
        ok, title = arxiv_title(arxiv_id)
        check = {"type": "arxiv", "ok": ok, "detail": title, "ref": arxiv_id}
        # Title consistency: does the real arXiv title appear in the concept?
        if ok:
            title_norm = _norm(title)
            # Compare against the significant words of the arXiv title present in the concept.
            words = [w for w in title_norm.split() if len(w) > 4]
            present = sum(1 for w in words if w in _norm(txt))
            ratio = present / len(words) if words else 0
            check["coherence"] = round(ratio, 2)
            if ratio < 0.5:
                check["ok"] = False
                check["detail"] = f"arXiv title \"{title}\" weakly consistent with the concept (coverage {ratio:.0%})"
        res["checks"].append(check)

    res["ok"] = all(c["ok"] for c in res["checks"])
    return res


def main():
    ap = argparse.ArgumentParser(description="Factual verification of sources.")
    ap.add_argument("paths", nargs="*", help="Concepts to verify.")
    ap.add_argument("--all", action="store_true", help="Verify the whole corpus.")
    ap.add_argument("--json", action="store_true", help="JSON output.")
    args = ap.parse_args()

    if args.all:
        targets = sorted(glob.glob(os.path.join(CONCEPTS, "*.md")))
    elif args.paths:
        targets = args.paths
    else:
        ap.error("provide concepts or --all.")

    report = [verify_note(p) for p in targets]
    nb_ko = sum(1 for r in report if not r["ok"])

    if args.json:
        json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        for r in report:
            mark = "✅" if r["ok"] else "❌"
            sys.stdout.write(f"{mark} {r['slug']}\n")
            for c in r["checks"]:
                cm = "✅" if c["ok"] else "❌"
                sys.stdout.write(f"    {cm} {c['type']}: {c['detail']} [{c['ref']}]\n")
        sys.stdout.write(f"\n{nb_ko} concept(s) failed out of {len(targets)}.\n")

    sys.exit(1 if nb_ko else 0)


if __name__ == "__main__":
    main()
