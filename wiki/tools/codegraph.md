---
tool: "CodeGraph"
title: "CodeGraph"
themes: [rag-context]
type: "MCP server / CLI"
url: https://colbymchenry.github.io/codegraph/
pricing_model: "Open-source (MIT), free"
llm_cost: "No LLM cost of its own — uses no LLM, runs inside the agent (reduces token consumption)"
objectives: [code-generation]
family: "Codebase knowledge: graphs, search & memory"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Indexes a codebase into a local knowledge graph (tree-sitter + SQLite) exposed to agents via MCP; deterministic, no LLM, reduces tool calls and tokens"
---

# CodeGraph

**In one sentence** — open-source tool that turns any codebase into a local, queryable knowledge graph, exposed to AI coding agents via MCP, so they explore the code with far fewer tool calls and tokens.

## Type & integration
Both a **CLI** (`npx @colbymchenry/codegraph`) and an **MCP server**, compatible with Claude Code, Cursor, Codex CLI, OpenCode, Gemini, etc. It parses code with **tree-sitter**, stores symbols / edges / files in **SQLite (FTS5)**, and exposes that graph (symbols, call graph, structure) to agents via MCP. Auto-sync via the OS's native file watchers. npm install (`@colbymchenry/codegraph`). 19+ languages supported, "framework-aware" route detection for ~13 frameworks.

## Pricing model
**Open-source, MIT license**, free. No apparent paid offering — a community project on GitHub.

## LLM cost
**No LLM cost of its own** 🟢. It's a special case of the "Built-in" category: CodeGraph **calls no LLM** — extraction is *deterministic*, derived from the AST (no LLM summarization), and runs **100% locally with no API key**. Better still: it *lowers* the LLM bill of the agent using it, by replacing costly file scans with queries against the pre-indexed graph.

Measured benefit (benchmarks claimed on 6 real codebases): ~**92% fewer tool calls** and ~**71% faster exploration** on average → so fewer tokens consumed on the agent side.

## What it's for
Give a coding agent a structured map of the repo: symbol/reference navigation, **impact analysis** (tracing how a change propagates), quick understanding of a large codebase — without re-reading files every time. Complementary to agents like [Kilo Code](kilo-code.md) or Claude Code: it's an indexing layer, not an agent.

## Notes
- Deterministic (AST) ≠ semantic search by embeddings: no LLM "approximation", but also no meaning-similarity.
- 100% local → good for privacy (no data sent to a third party).
- Plugs in via MCP: interesting to pair with any MCP-compatible agent to reduce cost/latency.
- ⚠️ "~92% fewer tool calls / ~71% faster" benchmarks are self-declared by the author (not independently reproduced); quality depends on the language's tree-sitter coverage — to be measured on your own repo.

## Source
- Site/landing: https://colbymchenry.github.io/codegraph/
- Repo: https://github.com/colbymchenry/codegraph

*(verified on 2026-06-15 — official landing + GitHub + web search)*
