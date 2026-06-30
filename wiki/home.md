# 🗺️ Home — map of the knowledge base

Entry note for **browsing in Obsidian**. (On GitHub, the entry point remains the repository `README`.)

This base is meant to be **consulted**, not read end to end. You enter it at **four altitudes**, from broad to precise — choose according to your need.

## 🧭 "I want to do…" — objective guides (L3)

Paths that cut across themes, task-oriented. The best entry point when you start from a **goal**.

- [Generating code with AI](guides/generate-code-with-ai.md)
- [Making an LLM system reliable & evaluating it](guides/build-reliable-llm-systems.md)
- [Mastering token cost](guides/control-token-cost.md)
- [Putting AI into production](guides/ai-in-production.md)

## 📚 "I'm exploring a topic" — by theme (L2)

- [themes-index.md](themes-index.md) — the 14 themes, each opening a per-theme hub page of concepts + tools · corpus state: [corpus-report.md](corpus-report.md)

## 🧰 "I'm looking for a tool" — census

- [tools-hub.md](tools-hub.md) (index + icon legend). Tools live in the topic pages: [generating code](guides/generate-code-with-ai.md) · [AI in a product](guides/ai-in-production.md) · [for people who don't code](guides/ai-for-non-coders.md) · still to be triaged: `tool-candidates.md` (repo root)

## ❓ "I have a precise question" (L1)

- Ask the question via the agent — `/kb:query` command: it reads the right notes and **cites its sources**.
- Otherwise: search, graph view, backlinks, or pick a "**In one sentence**" hook + its source link for a post.

- 🪵 **Log** — [log.md](log.md) · ⚙️ **Process & commands** — repository `README` (`/kb:*` slash commands)

> Internal links are in **markdown** (`[text](note.md)`) **by choice**: clickable on GitHub *and* used by Obsidian's graph/backlinks (wikilinks `[[ ]]`, by contrast, do not render on GitHub). See the decision entry in [log.md](log.md).

## Dataview queries

> Requires the community plugin **Dataview**. Without it, these blocks display as code (with no effect).

**Concepts 🔴 (substance), by theme:**
```dataview
TABLE level, theme FROM "wiki/concepts" WHERE level = "🔴" SORT theme ASC
```

**All notes of a theme (adapt the value):**
```dataview
LIST FROM "wiki/concepts" WHERE theme = "security"
```

**Tools — type, economic model, LLM cost:**
```dataview
TABLE type, pricing_model AS "eco", llm_cost AS "LLM cost" FROM "wiki/tools" SORT tool ASC
```

**Tools in BYOK (API key to provide):**
```dataview
LIST FROM "wiki/tools" WHERE contains(llm_cost, "BYOK")
```

## Recommended Obsidian settings (optional)

- **Exclude non-note folders** from the graph/search: `Settings → Files and links → Excluded filters` → add `tools/`, `sources/`, `.claude/`.
- **Link format**: keep "relative path" (not "wikilink") → GitHub compatibility preserved.
- `tools/_TEMPLATE.md` can be declared as a template (**Templates** plugin) to create a new tool note.
