---
tool: "Agent Booster"
title: "Agent Booster"
themes: [efficiency-cost, rag-context]
type: "MCP server / CLI"
url: https://github.com/sseshachala/agent-booster
pricing_model: "Open-source"
llm_cost: "Built-in"
objectives: [code-generation]
family: "Codebase knowledge: graphs, search & memory"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Index of **symbols** (tree-sitter + **local** `all-MiniLM-L6-v2` embeddings) that intercepts the agent's *Read* calls: returns the relevant symbols instead of the whole file → 60–90% fewer tokens. Hooks for Claude Code/Cursor/Windsurf/Codex; MIT, no LLM or key. ⚠️ Namesake of ruvnet's `agent-booster` (a different product)"
migrated_from: agent-booster
---

# Agent Booster

**In one sentence** — open-source MCP server (MIT, Python) that indexes a codebase into **symbols** (tree-sitter + **local** embeddings) and, when the agent wants to read a file, returns only the **relevant symbols** instead of the whole file → 60–90% fewer tokens (5–15× cost reduction claimed), with **no LLM or key of its own**.

## Type & integration
**MCP server** + **CLI**. `booster init <platform>` writes **hooks** that redirect the agent's *Read* operations to the `smart_read` tool, which runs a per-file vector search and returns only the matching functions/classes (by line range). Platforms: **Claude Code, Cursor, Windsurf, OpenAI Codex**.

Commands: `init` (configure the tool) · `index` (parse/extract symbols) · `embed` (build embeddings) · `search` (keyword search) · `route` (recommends model size haiku/sonnet/opus) · `serve` (start the MCP server) · `gain` (track token savings).

## Pricing model
**Open-source, free**, **MIT** license (© 2026 conductai). No identified commercial offering.

## LLM cost
**🟢 Built-in.** Agent Booster **uses no LLM** and **takes no key**: it optimizes the consumption of **your existing agent** (whose key/subscription you already provide to its platform). Embeddings are **local and offline**: *"Uses `all-MiniLM-L6-v2` (local, no data leaves your machine)"* via `sentence-transformers`, built at the `booster embed` step. No paid network calls for indexing. A typical "drives the existing agent" case → 🟢, not 🔑.

## What it's for
Reduce the context the agent loads on each read: instead of swallowing whole files, it receives only the semantically useful symbols → fewer tokens, less "context rot", lower agent cost. A neighbor of [CodeGraph](codegraph.md) and [Polaris](polaris.md) (local, deterministic code index that reduces tokens); the `route` bonus adds a model-size recommendation.

## Notes
- ⚠️ **Namesake clash**: don't confuse with the other **`agent-booster`** (ruvnet, Rust/WASM, an accelerator for *applying* code edits) — a different product with the same name.
- ⚠️ **Read-before-write friction (especially Claude Code)**: the `PreToolUse` hook **blocks the native `Read`** on indexed files and forces the `smart_read` MCP tool. But on Claude Code, `Edit`/`Write` require a **prior native `Read`** of the file (otherwise "File has not been read yet") — a partial `offset`/`limit` read is enough, but an MCP tool **does not set** that flag. So `smart_read` mainly covers **exploration/comprehension** reads (the bulk of an agent's reads); the **read-to-edit** cycle hits this precondition, and the "full Read" fallback planned for the no-match case falls back to a `Read`… which is itself blocked. The README **does not address** this point. Agents that edit by *diff/patch* (Cursor/Windsurf/Codex) have a different model → friction is mainly on the Claude Code side. *(verified against the README, 2026-06-23)*
- "60–90%" / "5–15×" claims: vendor orders of magnitude, to be measured on your own repo (`booster gain`).
- Symbol granularity: relevant mostly for languages well covered by tree-sitter; `smart_read` quality depends on the quality of the MiniLM embeddings (a lightweight model).

## Source
- Repo: https://github.com/sseshachala/agent-booster — README (hooks/`smart_read` mechanics, local `all-MiniLM-L6-v2` embeddings, commands, platforms), LICENSE (MIT, © 2026 conductai). *(verified on 2026-06-23)*
