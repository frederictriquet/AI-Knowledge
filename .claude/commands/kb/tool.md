---
description: Add an AI tool to the tool census (verify at source → note + frontmatter → regenerate tables → log).
argument-hint: <tool name and/or URL>
---
Add this tool to the AI tool census: $ARGUMENTS

> **Reference schema**: `process/SCHEMA.md` §4 (families, tool note format, canonical icon legend, cost verification rule).

Process (project convention — see the memories `outils-ia-recensement` and `verifier-couts-outils-ia`):

1. **Verify at source** — WebFetch / WebSearch **from this thread** (⚠️ subagents have no network access here): official URL, type, **exact license**, business model + **dated pricing figures**, and above all the **LLM cost mechanism**. **Never assume** (license/price/cost) — always go to the source (LICENSE, pricing page, code).
2. **Classify** — choose the **`objectives`** (among `OBJECTIVES`: code-generation · reliability · cost-control · production · non-coder-practices; **multi-valued**, a tool can serve several goals) and the **`family`** (see the map in `wiki/tools-hub.md`). New family → create it and add its prose (intro + optional "reading key") in `tools/families.json`. Also choose 1–3 **`themes`** (the 14-theme taxonomy, §3.1) — topical axis shared with the concepts.
3. **Icons** — **single source = the legend in [`wiki/tools-hub.md`](wiki/tools-hub.md)**. eco 🔓🎁🔁💳🔒; LLM cost 🟢📦💸🔑❓ (combine if needed, e.g. 🟢🔑).
   - ⚠️ **Recurring LLM-cost pitfall**: a tool that **drives your existing agents/subscriptions** (Claude Code, Codex…) without taking a key = **🟢**, *not* 🔑. **🔑 (BYOK)** = you provide a **key to the tool itself**. **💸** = the vendor **resells** the tokens. Unresolvable doubt → **❓**.
4. **Note + frontmatter** — create `wiki/tools/<slug-kebab>.md` in the format of `wiki/tools/_TEMPLATE.md`. Fill in the **complete** frontmatter, including the keys that drive table generation: `objectives: [...]`, `family: "..."`, `eco_icons: "..."`, `llm_cost_icons: "..."`, `summary: "one-line summary"` (+ `themes`). The **`summary`** carries the ⚠️ if the status is sensitive (deprecated, acquired, beta). End the Source section with `*(verified on YYYY-MM-DD)*`.
5. **Regenerate** — `python3 tools/build_index.py`: the **tool's table row is generated automatically** in the subject page(s) of its `objectives` (grouped by `family`) — **do not edit any table by hand**. Then `tools/.venv/bin/python tools/kb_embed.py` (makes the tool searchable via `kb_search`).
6. **Log** — add a `TOOL` entry in `wiki/log.md`.

Do not confuse `wiki/concepts/` (concepts) and `wiki/tools/` (tools).

**Freshness reminder**: if the session context (hook `SessionStart` → `kb_reminder.py`) flags stale notes, slip in a short `→ /kb:refresh` at the close (maintenance of existing data).
