---
description: Ingest a source (URL/article) into the concept corpus (wiki/concepts/) via the enrichment pipeline.
argument-hint: <source URL or path>
---
Ingest the following source into the **concepts** knowledge base (`wiki/concepts/`): $ARGUMENTS

> **Reference schema**: `process/SCHEMA.md` §3 (concept note format, 14 themes, levels) and §1 (3-layer model).

Start by **reading `process/ENRICHMENT.md`** and follow its 7-step pipeline **strictly**. **Prerequisite**: check that `tools/.venv` exists (otherwise, create it via the setup in `ENRICHMENT.md` — steps 3/5/7 depend on it).

1. **INGEST** — fetch the clean text (WebFetch); archive the raw markdown in `sources/<hub>/`; record the canonical URL + the title (→ `source_url`, `source_title`).
2. **EXTRACT** — split into **atomic** concepts; for each one: a theme (among the 14), a level (🔴 substance / 🟡 tradeoff / 🟢 overview), an optional primary source. Discard out-of-scope material (the corpus = AI agents & prompt engineering).
3. **DEDUP** — for **each** concept: `tools/.venv/bin/python tools/kb_dedup.py --json "dense text of the concept"`. The score is only a pre-filter → open the candidate notes and judge note-by-note. Verdict: NEW / MERGE into <slug> / DUPLICATE (discarded).
4. **DRAFT** — write each NEW note in the corpus format (complete frontmatter with mandatory `source_url`, self-sufficient **In one sentence**, dense, "See also" pointing to **existing notes**). For a MERGE, prepare a patch of the target note, not a new note.
5. **QUALITY GATE** — `tools/.venv/bin/python tools/kb_lint.py wiki/concepts/<slug>.md` then `tools/.venv/bin/python tools/kb_check_sources.py wiki/concepts/<slug>.md`. **Never invent an arXiv identifier**: unverifiable → remove `primary_source`. Judge density/non-redundancy.
6. **REVIEW** — present a report (concepts, dedup verdicts with scores + candidate notes, complete drafts, result of the 3 gates) and **wait for my explicit approval**. Write nothing beforehand.
7. **COMMIT** — after approval: write the notes into `wiki/concepts/` (and merge patches), then `python3 tools/build_index.py` and `tools/.venv/bin/python tools/kb_embed.py`. Add an `INGEST` entry in `wiki/log.md`. Only commit (git) if I ask for it.

Everything is reversible up to step 6; the human has the final word.
