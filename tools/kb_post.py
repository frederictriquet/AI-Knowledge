#!/usr/bin/env python3
"""Generates a post preview from a randomly drawn note.

The corpus is designed to produce short posts (internal messaging, LinkedIn):
each note carries an "In one sentence" hook + a "learn more" link.
This script assembles that material into a ready-to-copy draft — no LLM, pure
deterministic assembly of the note's content.

Usage:
    python3 tools/kb_post.py                 # a random note
    python3 tools/kb_post.py --slug react    # a specific note
    python3 tools/kb_post.py --theme security        # random within a theme
    python3 tools/kb_post.py --seed 42       # reproducible draw
    python3 tools/kb_post.py --format linkedin       # formatting variant
"""
# kb_common is a sibling module, invisible to the type-checker isolated from the hook.
# pyright: reportMissingImports=false
import re
import sys
import random
import argparse

from kb_common import load_notes, split_note, CONCEPTS, TOOLS

# H2 labels carrying the substance/context of the concept, by preference.
SUBSTANCE_SECTIONS = [
    r"In detail",
    r"What the source says",
    r"The idea",
    r"Key points",
]
# H2 labels carrying the "for a senior" insight, in order of preference.
INSIGHT_SECTIONS = [
    r"Tradeoff\s*/\s*insight \(for a senior\)",
    r"Tradeoff\s*/\s*when to use it",
    r"Tradeoff[^\n]*",
    r"Why it matters",
    r"Takeaways",
]


def extract_hook(body):
    """Return the text of the "In one sentence" hook, or '' if absent."""
    m = re.search(r"\*\*In one sentence\*\*\s*[—–-]*\s*(.+?)(?:\n\s*\n|\n#)", body, re.DOTALL)
    if not m:
        return ""
    return re.sub(r"\s+", " ", m.group(1)).strip()


def extract_section(body, patterns):
    """Return the 1st paragraph of the 1st H2 section whose title matches a pattern."""
    for pattern in patterns:
        m = re.search(rf"^##\s+{pattern}\s*\n+(.+?)(?:\n\s*\n|\n##|\Z)",
                      body, re.DOTALL | re.MULTILINE | re.IGNORECASE)
        if m:
            return re.sub(r"\s+", " ", m.group(1)).strip()
    return ""


def hashtags(fm):
    """Build a few hashtags from the tags or, failing that, from the theme."""
    tags = fm.get("tags")
    if isinstance(tags, list) and tags:
        base = tags
    else:
        base = [fm.get("theme", "").replace("-", " ")]
    out = []
    for t in base[:4]:
        word = re.sub(r"[^a-z0-9]", "", t.lower().replace(" ", ""))
        if word:
            out.append("#" + word)
    return " ".join(out)


def compose(note, style="internal"):
    """Assemble the post preview (str) from a loaded note."""
    fm, txt = note["fm"], note["txt"]
    _, body = split_note(txt)
    title = fm.get("title", note["slug"])
    hook = extract_hook(body) or '(no "In one sentence" hook in this note)'
    substance = extract_section(body, SUBSTANCE_SECTIONS)
    example = extract_section(body, [r"Example"])
    insight = extract_section(body, INSIGHT_SECTIONS)
    url = fm.get("source_url", "").strip()
    primary = fm.get("primary_source", "").strip()

    lines = []
    if style == "linkedin":
        lines.append(f"💡 {title}")
        lines.append("")
        lines.append(hook)
        if substance:
            lines.append("")
            lines.append(substance)
        if example:
            lines.append("")
            lines.append(f"Example — {example}")
        if insight:
            lines.append("")
            lines.append(f"👉 {insight}")
        lines.append("")
        if url:
            lines.append(f"🔗 Learn more: {url}")
        if primary:
            lines.append(f"📄 Primary source: {primary}")
        ht = hashtags(fm)
        if ht:
            lines.append("")
            lines.append(ht)
    else:  # internal messaging: shorter, more direct
        lines.append(f"**{title}** — {hook}")
        if substance:
            lines.append("")
            lines.append(substance)
        if example:
            lines.append("")
            lines.append(f"Example — {example}")
        if insight:
            lines.append("")
            lines.append(f"Takeaway: {insight}")
        if url:
            lines.append("")
            lines.append(f"→ Learn more: {url}")
    return "\n".join(lines)


def choose(notes, slug=None, theme=None):
    """Select a note (by slug, or at random, optionally filtered by theme)."""
    if slug:
        for f in notes:
            if f["slug"] == slug:
                return f
        sys.exit(f"❌ note not found: \"{slug}\"")
    pool = [f for f in notes if not theme or f["fm"].get("theme") == theme]
    if not pool:
        sys.exit(f"❌ no note for theme \"{theme}\"")
    # Purely editorial draw (post preview): no cryptographic stakes.
    return random.choice(pool)  # noqa: S311


def main():
    ap = argparse.ArgumentParser(description="Post preview from a note.")
    ap.add_argument("--slug", help="Specific note (otherwise a random draw).")
    ap.add_argument("--theme", help="Restrict the draw to a theme.")
    ap.add_argument("--seed", type=int, help="Seed for a reproducible draw.")
    ap.add_argument("--format", choices=["internal", "linkedin"], default="internal",
                    help="Formatting style (default: internal).")
    args = ap.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    # Posts can be drawn from concepts (concepts/) as well as tool notes
    # (tools/): both directories are scanned.
    notes = load_notes([CONCEPTS, TOOLS])
    if not notes:
        sys.exit("❌ no note in the corpus.")

    note = choose(notes, slug=args.slug, theme=args.theme)
    post = compose(note, style=args.format)

    # Decoration (header + bars) on stderr, bare post on stdout: a `> file`
    # or a pipe captures only the post, with no spurious prefix or border.
    # Explicit flush so the order stays correct on screen despite the double
    # buffering of stdout/stderr.
    bar = "─" * 60
    sys.stderr.write(f"preview ({args.format}) · {note['slug']}.md\n{bar}\n")
    sys.stderr.flush()
    sys.stdout.write(post + "\n")
    sys.stdout.flush()
    sys.stderr.write(bar + "\n")
    sys.stderr.flush()


if __name__ == "__main__":
    main()
