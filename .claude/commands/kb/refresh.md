---
description: Re-verify census tools at source (price/license/status) and propagate the update everywhere (note + table rows + log); deprecate if needed. Run on demand.
argument-hint: "[tool name | --stale | --all]  (default: --stale)"
allowed-tools: WebFetch, WebSearch, Bash(python3 tools/kb_staleness.py:*), Bash(tools/.venv/bin/python tools/kb_lint.py:*), Bash(python3 tools/build_index.py), Bash(curl:*), Read, Grep, Glob, Edit
---
Refresh the tool census from the **source**: $ARGUMENTS

> **Reference schema**: `process/SCHEMA.md` §4 (census, canonical legend, cost verification rule). ⚠️ **Verify at source, never assume** license/price/LLM cost; WebFetch/WebSearch — and `curl -A` (browser UA) if 403 — **from this thread** (subagents have no network here).

**Application level — "Mixed"**:
- ✅ **Auto** (without asking): re-date `*(verified on YYYY-MM-DD)*` when **nothing has changed**; propagate an **already confirmed** fact/status **consistently across all touchpoints**; fix broken links/anchors.
- ⏸️ **On your OK** (show the diff first): any **factual change** (price, license, business model, **LLM cost icons**) and any **deprecation** (acquisition, sunset, archival, 404).

1. **Targets** — `--stale` (or no argument) → `python3 tools/kb_staleness.py` (STALE > 90 days + UNDATED categories); a **name/slug** → that note alone; `--all` → all notes in `wiki/tools/`.
2. **For each target** — read the note (official URL + recorded facts: license, dated price, status, eco/LLM-cost icons), then **re-verify at source**: official page + **pricing**, **LICENSE file**, **GitHub API** (`api.github.com/repos/…`: `license.spdx_id`, `archived`, `full_name` redirect), repo/README. Cross-check the figures; invent nothing.
3. **Diff & verdict** per tool: `unchanged` · `to update` (specify *what*: price/license/eco/LLM cost) · `to deprecate` (dead / acquired / sunset / archived / 404).
4. **Touchpoints** — a tool's data lives in **its frontmatter** (`wiki/tools/<slug>.md`: `pricing_model`/`llm_cost`, `eco_icons`/`llm_cost_icons`, `summary`, `objectives`, `family`). The subject-page tables are **generated** from this frontmatter → update the **note** (not the tables). Also check the **cross-links** in other notes, `wiki/tools-hub.md` (legend/map) and `tool-candidates.md`. The ⚠️ sensitive-status marker goes in the `summary`.
5. **Apply** according to the Mixed level; **always re-date** the Source section of the touched notes. After editing: `tools/.venv/bin/python tools/kb_lint.py wiki/concepts/…` if a concept note is touched, and **`python3 tools/build_index.py`** to regenerate the index/MOC **and the tool tables of the subject pages** as soon as a frontmatter changes.
6. **Log** — one `UPDATE` entry (fact changed) or `DEPRECATE` (removal/acquisition) **per affected tool** in `wiki/log.md`. If everything is unchanged: a single recap `LINT`/`NOTE` (dates refreshed).
7. **Final digest** — `tool → verdict` table, distinguishing what was **auto-applied** from what **awaits your OK**, with the **sources consulted (dated)**.

Only deprecate/overwrite a fact on **proof at source**. Unresolvable doubt → mark `❓`/⚠️ and flag it to me, do not decide.
