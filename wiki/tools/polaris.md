---
tool: "Polaris (polarismcp.com)"
title: "Polaris (polarismcp.com)"
themes: [rag-context]
type: "MCP server / CLI"
url: https://polarismcp.com/
pricing_model: "Open-source (MIT); paid Pro offering in preparation"
llm_cost: "No own LLM cost — local embeddings (ONNX), no LLM inference (reduces token consumption)"
objectives: [code-generation]
family: "Codebase knowledge: graphs, search & memory"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Local semantic-search MCP server over project docs (ONNX embeddings, hybrid vector+BM25); no LLM, no cloud, cuts tokens 10–40×. MIT core, paid Pro in preparation"
---

# Polaris

**In one sentence** — local-first semantic-search MCP server: it indexes a project's documentation and lets coding agents retrieve ranked answers, with no cloud or API key.

> ⚠️ Homonym: not to be confused with **Apache Polaris** (data lakehouse catalog) and its own "Polaris MCP Server". This page is about **polarismcp.com**.

## Type & integration
**MCP server / CLI tool**: a standalone binary that runs **locally** and integrates with Claude Code, Cursor, Codex via the Model Context Protocol. It replaces grep-based doc retrieval with **hybrid search**: vector (embeddings) + BM25 + ranking.

## Pricing model
- **Polaris (core)**: open-source, **MIT license**, free, on GitHub.
- **Polaris Pro**: paid subscription **in development** (−50% launch discount for waitlist signups).

→ Freemium trajectory: free open core + Pro offering to come.

## LLM cost
**No own LLM cost** 🟢. Polaris **does no LLM inference**: it uses an **embedded ONNX model** to compute embeddings locally — no API key, no cloud service, no telemetry. Like [CodeGraph](codegraph.md), it *reduces* the agent's bill by avoiding costly grep-then-read cycles: claimed demo at **10–40× fewer tokens** consumed.

Order of magnitude: zero LLM inference cost on Polaris's side; net token savings on the agent's side.

## What it's for
Give an agent efficient, relevant access to a project's **local documentation** (and other docs) without re-reading everything. Target: developers on Claude Code / Cursor / Codex who want fast search that is **100% local and private** (no cloud dependency).

## Notes
- Family close to [CodeGraph](codegraph.md) (code graph, local, no LLM) and [Graphify](graphify.md) (multi-modal graph, *with* LLM): all aim to reduce agent tokens/tool-calls, by different means. Polaris focuses on **semantic doc search**, locally.
- Local-first + ONNX → good privacy argument.
- Watch Polaris Pro's content/pricing at release.
- ⚠️ Local search (ONNX) suited to project docs, but **not a substitute for a dedicated vector database** on large corpora (limited local ANN quality/scale); young project, and the MIT core could be hollowed out in favor of the upcoming "Pro".

## Source
- Official site: https://polarismcp.com/
- GitHub repo (MIT core) — see link from the site

*(verified on 2026-06-15 — official landing page + web search)*
