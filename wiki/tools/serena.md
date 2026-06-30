---
tool: "Serena"
title: "Serena"
themes: [frameworks-tooling, tools-function-calling]
type: "MCP server / coding-agent toolkit"
url: https://github.com/oraios/serena
pricing_model: "Open-source (MIT), free; optional paid JetBrains plugin (free trial)"
llm_cost: "No LLM of its own — a tool for LLMs, BYO client; relies on LSP (deterministic), no inference"
objectives: [code-generation]
family: "Codebase knowledge: graphs, search & memory"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "MCP toolkit (Python, Oraios) giving agents IDE-grade capabilities via LSP: semantic search **and editing/refactoring** at the symbol level across 40+ languages (not grep). MIT open-source (optional paid JetBrains plugin), BYO client"
---

# Serena

**In one sentence** — "your agent's IDE": an MCP toolkit that gives coding agents IDE-grade capabilities — **symbol-level semantic** search, editing, refactoring and debugging via the Language Server Protocol — instead of plain text search.

## Type & integration
**MCP server** (and CLI), written in **Python** (~90%), by **Oraios AI**. Plugs into MCP-compatible clients by providing a launch command or an HTTP URL: Claude Code, Claude Desktop, Cursor, Cline, VS Code extensions, JetBrains, terminal tools… Supports **40+ languages** via **LSP** backends (or JetBrains IDE analysis). Also has **Agno** integration (to use it with open-weight models).

## Pricing model
- **Open-source core, MIT license**, free.
- **Paid JetBrains plugin** (with free trial) for enhanced capabilities.

A "lightweight open-core" model: the core is free/MIT, the JetBrains extension is the commercial option.

## LLM cost
**No LLM of its own** 🟢 — Serena is a **tool *for* LLMs**, not a model: you need an LLM (via your client) to orchestrate the use of the tools. No LLM cost on Serena's side; you bring your own client (Claude Code, Cursor…). The analysis work relies on **LSP** (deterministic, symbol-level), not on embeddings or inference. Note: available even with Claude's free tier (MCP support), and usable with open-weight models via Agno.

## What it's for
Filling agents' lack of "IDE-grade" code understanding: navigating code by symbols, finding definitions/references, editing and refactoring precisely, debugging — including on large complex projects, where text grep/RAG struggles. It exploits the **relational structure** of code (symbols, references) rather than raw text.

## Notes
- **Family 2 (codebase knowledge)**, but a distinct angle: Serena = **LSP, symbol-level, with editing/refactoring**; [CodeGraph](codegraph.md) and [GraphMind](graphmind.md) = tree-sitter graph (mostly reading/navigation); [Polaris (polarismcp.com)](polaris.md) = semantic doc search; [Cavemem](cavemem.md) = memory. Serena is the most "active IDE" (it modifies code, not just understands it).
- LSP-based → precision on real code (no approximation), at the cost of depending on a language server per language.
- Very widely used as the "Swiss army knife" MCP for code understanding by agents.

## Source
- Repo: https://github.com/oraios/serena
- Docs/lobehub, mcpservers.org, apidog (Serena MCP guides)

*(verified on 2026-06-15 — GitHub README + web search)*
