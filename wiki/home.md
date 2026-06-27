# 🗺️ Home — map of the knowledge base

Entry note for **browsing in Obsidian**. (On GitHub, the entry point remains [README.md](README.md).)

This base is meant to be **consulted**, not read end to end. You enter it at **four altitudes**, from broad to precise — choose according to your need.

## 🧭 "I want to do…" — objective guides (L3)

Paths that cut across themes, task-oriented. The best entry point when you start from a **goal**.

- [Generating code with AI](guides/generer-du-code-avec-l-ia.md)
- [Making an LLM system reliable & evaluating it](guides/fiabiliser-evaluer-un-systeme-llm.md)
- [Mastering token cost](guides/maitriser-le-cout-en-tokens.md)
- [Putting AI into production](guides/mettre-de-l-ia-en-production.md)

## 📚 "I'm exploring a topic" — by theme (L2)

- [INDEX-THEMATIQUE.md](INDEX-THEMATIQUE.md) — the 14 themes, each opening a per-theme hub page of concepts + tools · corpus state: [RAPPORT-CORPUS.md](RAPPORT-CORPUS.md)

## 🧰 "I'm looking for a tool" — census

- [tools-hub.md](tools-hub.md) (index + icon legend). Tools live in the topic pages: [generating code](guides/generer-du-code-avec-l-ia.md) · [AI in a product](guides/mettre-de-l-ia-en-production.md) · [for people who don't code](guides/ia-pour-ceux-qui-ne-codent-pas.md) · still to be triaged: [outils candidats.md](outils%20candidats.md)

## ❓ "I have a precise question" (L1)

- Ask the question via the agent — `/kb:query` command: it reads the right cards and **cites its sources**.
- Otherwise: search, graph view, backlinks, or pick a "**In one sentence**" hook + its source link for a post.

- 🪵 **Log** — [log.md](log.md) · ⚙️ **Process & commands** — [README.md](README.md) (`/kb:*` slash commands)

> Internal links are in **markdown** (`[text](note.md)`) **by choice**: clickable on GitHub *and* used by Obsidian's graph/backlinks (wikilinks `[[ ]]`, by contrast, do not render on GitHub). See the decision entry in [log.md](log.md).

## Dataview queries

> Requires the community plugin **Dataview**. Without it, these blocks display as code (with no effect).

**Concepts 🔴 (substance), by theme:**
```dataview
TABLE niveau, theme FROM "wiki/fiches" WHERE niveau = "🔴" SORT theme ASC
```

**All cards of a theme (adapt the value):**
```dataview
LIST FROM "wiki/fiches" WHERE theme = "securite"
```

**Tools — type, economic model, LLM cost:**
```dataview
TABLE type, modele_economique AS "eco", cout_llm AS "LLM cost" FROM "wiki/fiches outils" SORT outil ASC
```

**Tools in BYOK (API key to provide):**
```dataview
LIST FROM "wiki/fiches outils" WHERE contains(cout_llm, "BYOK")
```

## Recommended Obsidian settings (optional)

- **Exclude non-card folders** from the graph/search: `Settings → Files and links → Excluded filters` → add `tools/`, `sources/`, `.claude/`.
- **Link format**: keep "relative path" (not "wikilink") → GitHub compatibility preserved.
- `tools/_TEMPLATE.md` can be declared as a template (**Templates** plugin) to create a new tool card.
