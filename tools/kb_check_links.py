#!/usr/bin/env python3
"""Check that every relative markdown link in the wiki resolves on disk.

Scans all `wiki/**/*.md`, resolves each relative link (decoding `%20`, stripping
any `#anchor`) against the file's own directory, and reports:
  - target file missing                 -> ERROR  (exit 1);
  - target outside `wiki/` (e.g. a root doc) -> WARNING (valid on GitHub, but
    the published Quartz site only builds `wiki/`, so the link 404s there);
  - `#anchor` matching no heading/id in the target `.md` -> WARNING (heading
    slugification differs across renderers, so this is advisory, not blocking).

Links into `sources/` are an intentional provenance pattern (each note cites
its archived raw source); they are tallied as one summary line, not warned
per occurrence.

Fenced and inline code spans are stripped before scanning, so illustrative
link examples written inside backticks are not treated as real links.
External links (`http`/`https`/`mailto`/`tel`/`data`), absolute paths and
pure same-page anchors are ignored.

Usage: python3 tools/kb_check_links.py
Exit code 1 if any broken link is found, else 0.
"""
# kb_common is a sibling module (tools/); its top-level imports are stdlib-only.
# pyright: reportMissingImports=false
import os
import re
import sys
import glob
from urllib.parse import unquote

from kb_common import WIKI, ROOT

SOURCES = os.path.join(ROOT, "sources")

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$", re.MULTILINE)
EXPLICIT_ID_RE = re.compile(r"""(?:id|name)\s*=\s*["']([^"']+)["']""")
CURLY_ID_RE = re.compile(r"\{#([A-Za-z0-9_-]+)\}")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "ftp://", "data:", "//")


def strip_code(text):
    """Remove fenced blocks then inline code spans (avoids matching example links)."""
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]*`", "", text)
    return text


def slugify(text):
    """Approximate the GitHub/Quartz heading anchor: drop formatting, lower, kebab."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)   # [label](url) -> label
    text = text.replace("`", "").replace("*", "").replace("_", "")
    text = text.lower()
    text = re.sub(r"[^a-z0-9 \-]", "", text)               # drops punctuation + emoji
    text = text.strip().replace(" ", "-")
    return re.sub(r"-+", "-", text)


def anchors_of(path):
    """Set of anchors a `.md` file exposes (heading slugs + explicit ids)."""
    try:
        txt = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return set()
    anchors = {slugify(h) for h in HEADING_RE.findall(txt)}
    anchors |= set(EXPLICIT_ID_RE.findall(txt))
    anchors |= set(CURLY_ID_RE.findall(txt))
    return anchors


def check_file(path, anchor_cache):
    """Return (errors, warnings, source_link_count) for one markdown file."""
    errors, warnings = [], []
    source_links = 0
    base = os.path.dirname(os.path.abspath(path))
    body = strip_code(open(path, encoding="utf-8", errors="replace").read())

    for raw in LINK_RE.findall(body):
        url = raw.strip()
        url = url.split()[0] if url.split() else url     # drop optional "title"
        url = url.strip("<>")
        if not url or url.startswith("#") or url.lower().startswith(SKIP_PREFIXES):
            continue
        if url.startswith("/"):
            warnings.append(f"absolute path (not portable): {url}")
            continue

        link, _, anchor = url.partition("#")
        link = unquote(link)
        if not link:                                     # pure same-page anchor
            continue
        resolved = os.path.normpath(os.path.join(base, link))

        if not os.path.exists(resolved):
            errors.append(f"broken link: {url} -> {os.path.relpath(resolved)}")
            continue

        if resolved == SOURCES or resolved.startswith(SOURCES + os.sep):
            source_links += 1                            # intentional provenance link
        elif not (resolved == WIKI or resolved.startswith(WIKI + os.sep)):
            warnings.append(f"target outside wiki/ (404 on the published site): {url}")

        if anchor and resolved.endswith(".md"):
            if resolved not in anchor_cache:
                anchor_cache[resolved] = anchors_of(resolved)
            if slugify(anchor) not in anchor_cache[resolved] \
                    and anchor not in anchor_cache[resolved]:
                warnings.append(f"unknown anchor: {url}")

    return errors, warnings, source_links


def main():
    targets = sorted(glob.glob(os.path.join(WIKI, "**", "*.md"), recursive=True))
    anchor_cache = {}
    total_errors = 0
    total_warnings = 0
    total_source_links = 0
    for path in targets:
        errors, warnings, source_links = check_file(path, anchor_cache)
        total_errors += len(errors)
        total_warnings += len(warnings)
        total_source_links += source_links
        if errors or warnings:
            sys.stdout.write(f"\n{os.path.relpath(path)}\n")
            for e in errors:
                sys.stdout.write(f"  ❌ {e}\n")
            for w in warnings:
                sys.stdout.write(f"  ⚠️  {w}\n")

    sys.stdout.write(
        f"\n{total_errors} broken link(s), {total_warnings} warning(s) "
        f"across {len(targets)} files.\n")
    if total_source_links:
        sys.stdout.write(
            f"({total_source_links} provenance link(s) into sources/ — "
            "intentional, not published.)\n")
    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
