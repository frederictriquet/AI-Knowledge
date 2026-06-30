#!/usr/bin/env python3
"""Shared helpers for the knowledge base enrichment process.

Centralizes: the theme taxonomy, frontmatter parsing, note loading,
text preparation for embeddings and cosine similarity.
Imported by kb_embed.py, kb_dedup.py, kb_lint.py and kb_check_sources.py.
"""
# numpy lives in tools/.venv, invisible to the hook's isolated type-checker.
# pyright: reportMissingImports=false
import os
import re
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")
CONCEPTS = os.path.join(WIKI, "concepts")
TOOLS = os.path.join(WIKI, "tools")
CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".cache")

# The 14 valid themes (slug). Single source of truth, aligned with build_index.py.
THEMES = [
    "agent-fundamentals",
    "reasoning-planning",
    "prompting",
    "tools-function-calling",
    "rag-context",
    "memory",
    "multi-agent",
    "interop-protocols",
    "frameworks-tooling",
    "evaluation",
    "benchmarks",
    "security",
    "efficiency-cost",
    "governance-alignment-ops",
]
LEVELS = {"🔴", "🟡", "🟢"}

# "Objective" axis (L3 — guides by objective). Optional, multi-valued on
# concepts: slug → human label. Used to generate the wiki/guides/ guides.
# Orthogonal to the theme (theme = what it is about; objective = for what purpose).
OBJECTIVES = {
    "code-generation": "Generate code with AI",
    "reliability": "Reliability & evaluation of an LLM system",
    "cost-control": "Control token cost",
    "production": "Put AI in production",
    "non-coder-practices": "AI for people who don't code",
}


def split_note(txt):
    """Split a note into (raw_frontmatter, body). Empty frontmatter if absent."""
    if not txt.startswith("---"):
        return "", txt
    parts = txt.split("---", 2)
    if len(parts) < 3:
        return "", txt
    return parts[1], parts[2]


def parse_frontmatter(txt_or_path):
    """Parse simple YAML frontmatter. Accepts a file path or a text.

    Handles scalar values (`key: value`) and inline lists
    (`tags: [a, b]`). Returns a dict; {} if no frontmatter.
    """
    if "\n" not in txt_or_path and txt_or_path.endswith(".md"):
        txt = open(txt_or_path, encoding="utf-8", errors="replace").read()
    else:
        txt = txt_or_path
    block, _ = split_note(txt)
    if not block:
        return {}
    d = {}
    for line in block.splitlines():
        m = re.match(r"([A-Za-z_]+):\s*(.*)", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            d[key] = [x.strip().strip('"') for x in val[1:-1].split(",") if x.strip()]
        else:
            d[key] = val.strip('"')
    return d


def note_body(txt):
    """Return the Markdown body (without frontmatter), cleaned for embedding.

    Strips structural Markdown markers (headings, bold, lists, links)
    so as to keep only the meaning, without the formatting noise.
    """
    _, body = split_note(txt)
    body = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", body)  # links → text only
    body = re.sub(r"[#*`>_]", " ", body)                  # MD markers
    body = re.sub(r"\s+", " ", body)
    return body.strip()


def note_themes(fm):
    """Return the list of themes of a note, whether it carries `theme` or `themes`.

    Concepts: `theme` (single slug). Tools: `themes` (multi-valued list).
    """
    th = fm.get("themes")
    if isinstance(th, list):
        return [t for t in th if t]
    if isinstance(th, str) and th:
        return [th]
    t = fm.get("theme", "")
    return [t] if t else []


def note_objectives(fm):
    """Return the list of objectives (L3 axis) of a concept note. [] if absent."""
    o = fm.get("objectives")
    if isinstance(o, list):
        return [x for x in o if x]
    if isinstance(o, str) and o:
        return [o]
    return []


def embedding_text(fm, txt):
    """Build the representative text of a note for the embedding.

    Combines title + theme(s) + body: the title carries the concept, the body the meaning.
    Reads `theme` (concepts) as well as `themes` (tools) via note_themes().
    """
    title = fm.get("title", "")
    themes = ", ".join(note_themes(fm))
    return f"{title}. Theme: {themes}. {note_body(txt)}"


def load_notes(dirs=None):
    """Load all notes. Return a list of dicts.

    Each dict: {slug, path, fm (frontmatter), txt (raw), embed_text}.

    `dirs`: iterable of directories to scan. By default, only ``concepts/``
    (default behavior of the enrichment scripts). Notes are
    deduplicated by slug — the 1st directory in the list wins.
    """
    if dirs is None:
        dirs = [CONCEPTS]
    out = []
    seen = set()
    for d in dirs:
        corpus = "tool" if os.path.abspath(d) == os.path.abspath(TOOLS) else "concept"
        for path in sorted(glob.glob(os.path.join(d, "*.md"))):
            slug = os.path.basename(path)[:-3]
            if slug in seen:
                continue
            seen.add(slug)
            txt = open(path, encoding="utf-8", errors="replace").read()
            fm = parse_frontmatter(txt)
            out.append({
                "slug": slug,
                "path": path,
                "fm": fm,
                "txt": txt,
                "corpus": corpus,
                "themes": note_themes(fm),
                "embed_text": embedding_text(fm, txt),
            })
    return out


def content_hash(text):
    """Stable hash of the embedding text, to invalidate the cache on change."""
    import hashlib
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def cosine(a, b):
    """Cosine similarity between two vectors (lists or np.ndarray)."""
    import numpy as np
    a, b = np.asarray(a, dtype="float32"), np.asarray(b, dtype="float32")
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return float(np.dot(a, b) / (na * nb))
