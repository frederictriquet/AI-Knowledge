---
tool: "Cavemem"
title: "Cavemem"
themes: [memory]
type: "MCP server / CLI (+ IDE hooks)"
url: https://github.com/JuliusBrussee/cavemem
pricing_model: "Open-source (MIT), free"
llm_cost: "🟢🔑 — no generative LLM; local embeddings by default (🟢, no key); optional remote OpenAI provider = key required (🔑), local Ollama also possible"
objectives: [code-generation]
family: "Codebase knowledge: graphs, search & memory"
eco_icons: "🔓"
llm_cost_icons: "🟢🔑"
summary: "Persistent cross-agent memory (CLI + MCP + IDE hooks); compressed session events (~75%), local SQLite, queryable via MCP. No generative LLM; **local embeddings by default** (🟢), optional remote **OpenAI** provider = key required (🔑)"
---

# Cavemem

**In one sentence** — persistent cross-agent memory system for coding assistants: it captures session events, compresses them, and lets agents query their history via MCP — local by default, no network or cloud.

## Type & integration
**CLI + MCP server + IDE hooks** (globally installable via npm). Hooks fire at session boundaries to compress observations; agents then query their own history via MCP tools. Written in **TypeScript** (88.8%) + JS/Shell. Same author as [Caveman](caveman.md) and [Cavekit](cavekit.md).

## Pricing model
**Open-source, MIT license**, free; community project.

## LLM cost
**🟢🔑** — no **generative LLM**: storage and search via **SQLite FTS5 + vector index**, with **local embeddings by default** (`embedding.provider: local`) → **no key, no network** (🟢, "No network. No cloud."). Option (verified in the README): a **remote** embeddings provider — `ollama` (local) or **`openai`** → the latter **requires a key** (🔑, BYOK on embeddings). This is **not the default** mode.

Order of magnitude: zero LLM cost in standard mode; deterministic event compression (~75%) also reduces tokens when the agent reloads its memory.

## What it's for
Give agents a **durable memory shared across sessions/tools**: what was done, decided, observed, retrieved quickly and compactly — without depending on the cloud. Targets privacy (local-first) and token economy.

## Notes
- Same "token / context reduction" family as [CodeGraph](codegraph.md), [Polaris (polarismcp.com)](polaris.md), [Graphify](graphify.md): Cavemem brings the **persistent memory** angle (across sessions), where the others index code/docs.
- Strict local-first → a good privacy argument, like [Polaris (polarismcp.com)](polaris.md).
- Natural complement to [Caveman](caveman.md)/[Cavekit](cavekit.md) in the cave\* ecosystem.

## Source
- Repo: https://github.com/JuliusBrussee/cavemem

*(verified on 2026-06-15 — GitHub README)*
