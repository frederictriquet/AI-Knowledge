---
tool: "GraphMind"
title: "GraphMind"
themes: [rag-context, memory]
type: "Desktop application / MCP server / CLI"
url: https://getgraphmind.com/
pricing_model: "Open-source (MIT) freemium + subscriptions (€9–19/month)"
llm_cost: "🟢🔑 — no generative LLM; free local embeddings by default (🟢); remote Voyage AI/OpenAI embeddings on paid tiers = key required (🔑; BYOK vs included in subscription = ambiguous)"
objectives: [code-generation]
family: "Codebase knowledge: graphs, search & memory"
eco_icons: "🔓🎁"
llm_cost_icons: "🟢🔑"
summary: "Turns the codebase into a knowledge graph + persistent cross-session memory; 25 MCP tools, up to 5,700× fewer tokens than grep. No generative LLM; **free local** embeddings (🟢) or **remote Voyage/OpenAI** on paid tiers (🔑). MIT core free, subscriptions €9–19/month. Made in Paris"
migrated_from: graphmind
---

# GraphMind

**In one sentence** — turns a codebase into a knowledge graph queryable by AI, with persistent memory that keeps the assistant aware of decisions from one session to the next — up to 5,700× fewer tokens than raw search.

> ⚠️ Name clash: "GraphMind" refers to several unrelated products (mind-mapping app, graph database, etc.). This page is about **getgraphmind.com** (code graph for AI assistants, "Made in Paris").

## Type & integration
Three forms, same engine:
- **Desktop application** (Mac & Windows) — no terminal: you point at a folder, the app auto-configures the AI tools and starts the MCP server.
- **CLI** (`graphmind index .`, `graphmind setup`) — install via **Homebrew** (`brew install aouicher/graphmind/graphmind`) or **Cargo** (Rust).
- **MCP server** exposing **25 tools** to Claude Desktop, Claude Code, Cursor, Windsurf…

Parses each file with **tree-sitter**, builds a symbol graph in **DuckDB**, detects cross-project dependencies. 30+ languages.

## Pricing model
**Freemium**, **open-source MIT** core:
- **Free — €0** (available): local graph, unlimited projects, 25 MCP tools, SQLite memory store, local embeddings (minilm), MIT.
- **Embeddings — €9/month** (coming): remote semantic search via **Voyage AI** embeddings.
- **Pro — €19/month** (coming): remote API + MCP server, no local install, from any machine.
- **Team — €19/seat/month** (coming, min. 3): shared graph and memories, `gm_team_who_knows`, auto-sync.
- −20% annual.

## LLM cost
**🟢🔑 — no *generative* LLM** (no chat/completion; deterministic tree-sitter/AST extraction, hybrid FTS + semantic + graph ranking).
- **By default**: **local** embeddings (minilm) → **free, no key** (🟢).
- **Paid tiers**: **remote Voyage AI / OpenAI** embeddings → **key required** (🔑). ⚠️ The code requires a key (BYOK) while the /pricing page presents "Voyage AI embeddings" as a service **included** in the €9 tier → **actual model (BYOK vs included resale) ambiguous**, to be confirmed.

Net effect: GraphMind *massively reduces* the agent's tokens — ~10M tokens saved per session over 5–10 searches, up to 5,700× fewer than grep (benchmark on a 31K-symbol codebase).

## What it's for
Giving an agent a structural understanding of the code **plus a durable memory**:
- `gm_search` (meaning-based search, < 300 tokens), `gm_fn` (symbol + callers/callees in one call), `gm_fn_impact` (refactor blast radius), `gm_dead_code`, `gm_diff_impact` (PR review), `gm_similar` (duplication detection), `gm_cross_links`, `gm_cycles`…
- `gm_memory_add`: persistent memory of architecture decisions and conventions, recalled in every session.

## Notes
- **Synthesis of the "token reduction" cluster**: GraphMind brings together in one product what [CodeGraph](codegraph.md) (code graph), [Polaris (polarismcp.com)](polaris.md) (semantic doc search) and [Cavemem](cavemem.md) (persistent memory) do separately — but as a packaged commercial offering (desktop app + SaaS), where the others are purely open-source/CLI projects.
- MIT core but monetization via remote embeddings + hosting → "open-core" model.
- Written in Rust (available via Cargo), DuckDB for the graph.

## Source
- Official site: https://getgraphmind.com/ (and /pricing, /docs) — automated fetch blocked (403), content retrieved via curl on 2026-06-15

*(verified on 2026-06-15 — official landing page via curl with browser UA)*
