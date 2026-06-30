---
description: Corpus health checks (structure, sources, freshness, duplicates) + optional audit.
allowed-tools: Bash(python3 tools/build_index.py), Bash(python3 tools/kb_check_links.py), Bash(python3 tools/kb_staleness.py:*), Bash(tools/.venv/bin/python tools/kb_lint.py:*), Bash(tools/.venv/bin/python tools/kb_check_sources.py:*), Read, Grep, Glob, Agent, Edit
---
**Prerequisite**: the deterministic checks use the `tools/.venv` venv (gitignored). If it is missing → follow the setup in `process/ENRICHMENT.md` (`python3 -m venv tools/.venv` + `pip install -r tools/requirements.txt`) before running; otherwise the `kb_*.py` scripts fail.

> **Reference schema**: `process/SCHEMA.md` §3 (note structure rules) & §6 (tooling).

Run the knowledge base health checks, then give me a `✅ / ⚠️ / ❌` summary per check with the list of notes to fix.

1. **Structure** (deterministic): `tools/.venv/bin/python tools/kb_lint.py --all`
2. **Internal links** (deterministic): `python3 tools/kb_check_links.py` — resolves every relative markdown link across `wiki/`; broken target = ❌ (non-zero exit), target outside `wiki/` (404 on the published site) = ⚠️, `sources/` provenance links summarized.
3. **Index & title duplicates**: `python3 tools/build_index.py` — ⚠️ **regenerates** `wiki/themes-index.md` and `wiki/corpus-report.md` (this is not just a read); read the generated report.
4. **Freshness of tool notes**: `python3 tools/kb_staleness.py` (notes "verified on > 90 days ago" or undated)
5. **Sources**: `tools/.venv/bin/python tools/kb_check_sources.py wiki/concepts/<slug>.md` on recently modified notes (otherwise, mention that you are skipping this check).

Then, **propose** (without running it by default) a deeper **contradictions audit**: a subagent reads `wiki/concepts/`, `wiki/tools/`, the per-domain tables and `wiki/tools-hub.md` to spot contradictory facts, stale statuses not propagated, and broken links/anchors `#fam-N`. If I say yes: run it, apply the **real** fixes (with my approval for non-trivial ones), and add a `LINT` entry in `wiki/log.md`.
