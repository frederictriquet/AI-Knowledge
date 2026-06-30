---
tool: "Graphify"
title: "Graphify"
themes: [rag-context]
type: "Skill (AI coding assistants / Claude Code)"
url: https://graphify.net/
pricing_model: "Open-source (MIT), free"
llm_cost: "Built-in (runs in Claude Code) — but consumes tokens at indexing time (LLM semantic extraction)"
objectives: [code-generation]
family: "Codebase knowledge: graphs, search & memory"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Open-source skill (Claude Code) building a multi-modal knowledge graph (code, docs, PDF, images) via tree-sitter + LLM semantic extraction; consumes tokens at indexing time"
---

# Graphify

**In one sentence** — open-source skill that turns an entire repository (code, docs, articles, diagrams) into a multi-modal, queryable knowledge graph, to help AI coding assistants understand *what* the code does and *why* it is designed that way.

> ⚠️ Name clash: several products are called "Graphify" (graphify.ai, getgraphify.com, graphy.app…). This page is about **graphify.net**, the open-source skill by Safi Shamsi.

## Type & integration
**Skill** for AI coding assistants (Claude Code as the primary target). Combines **tree-sitter** (static analysis: AST, call graphs, docstrings) with **LLM-driven semantic extraction**. Multi-modal: parses code (.py, .js, .go, .java…), Markdown, **PDF** and **images**. Produces an interactive `graph.html`, a queryable `graph.json` and a readable `GRAPH_REPORT.md` (audit report).

## Pricing model
**Open-source, MIT license**, free. Maintained by Safi Shamsi.

## LLM cost
**Built-in** 🟢 — the skill runs in Claude Code and uses the agent's LLM, no separate API key. **Important nuance vs [CodeGraph](codegraph.md)**: Graphify does **LLM semantic extraction** when building the graph → indexing **consumes tokens** (unlike CodeGraph, which is 100% deterministic and free). The bet: this one-off indexing cost is largely amortized afterwards (the marketing communication mentions up to "70×" cost reduction on large codebases, the graph avoiding re-reading the repo on each query).

Order of magnitude: LLM cost depends on the indexed volume and the model, at Claude Code usage (no separate bill). Indexing = token spike; queries afterwards = savings.

## What it's for
Giving an agent a rich, multi-modal understanding of a project (not just the code, but also docs/PDF/diagrams — the "why"). Useful on large repos where re-reading files is costly. Inspired by Karpathy-style ideas on knowledge graphs for code.

## Notes
- Key difference with [CodeGraph](codegraph.md): Graphify = static **+ LLM semantics** + multi-modal (consumes tokens); CodeGraph = purely deterministic/AST, local, zero LLM. Choose depending on whether you want the raw "what" (CodeGraph) or the enriched "why" (Graphify).
- Exportable outputs (html/json/md) → usable outside the agent.
- ⚠️ The "70× cost reduction" is a **marketing (MindStudio) figure, unverified**; on a large monorepo, LLM indexing can be expensive before any amortization — prefer [CodeGraph](codegraph.md) (deterministic, zero LLM tokens) if the semantic "why" is not essential.

## Source
- Official site: https://graphify.net/ (HTTP 403 on automated fetch on 2026-06-15; info via web search)
- Third-party analysis: MindStudio ("Karpathy-Inspired Knowledge Graph … 70x")

*(verified on 2026-06-15 — web search; official landing page not retrievable automatically, to be reconfirmed by a direct visit)*
