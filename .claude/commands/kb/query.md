---
description: Answer a question from the wiki (notes + tool census), with citations.
argument-hint: <question>
---
Answer this question **from the knowledge base**: $ARGUMENTS

> **Corpus map** (where to look): `process/SCHEMA.md` §2.

1. **Search** the relevant pages: `wiki/concepts/` (concepts — rely on `wiki/themes-index.md`), `wiki/tools/` + per-domain tables + `wiki/tools-hub.md` (tools). Use grep; if needed `tools/.venv/bin/python tools/kb_dedup.py --json "rephrasing of the question"` to find semantically close notes.
2. **Synthesize** a dense answer, **citing the notes** used (path `wiki/concepts/<slug>.md` or `wiki/tools/<slug>.md`).
3. **Distinguish** what comes from the corpus from what you add yourself; explicitly flag the **gaps** (topic not/poorly covered).
4. If the exploration produced a reusable synthesis, **propose** to feed it back into the corpus (`/kb:ingest` or a new note). Do not write it without my approval.
5. **Freshness reminder**: if a reminder already appears in the session context (hook `SessionStart` → `kb_reminder.py`) — or, failing that, if `python3 tools/kb_staleness.py` flags STALE/UNDATED notes — end with a short line `→ run /kb:refresh to re-verify N note(s)`.
