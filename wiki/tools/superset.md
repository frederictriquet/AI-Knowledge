---
tool: "Superset (superset-sh)"
title: "Superset (superset-sh)"
themes: [multi-agent, frameworks-tooling]
type: "Desktop application (coding-agent orchestrator)"
url: https://github.com/superset-sh/superset
pricing_model: "Source-available (Elastic License 2.0) — downloadable app, commercial model unspecified"
llm_cost: "No LLM cost of its own (🟢) — orchestrates your existing agents (Claude Code, Codex…) that carry their own auth (subscription/login); no LLM key to give Superset"
objectives: [code-generation]
family: "Coding orchestrators & multi-agent systems"
eco_icons: "🔓🔒"
llm_cost_icons: "🟢"
summary: "Electron app, an 'IDE for the agent era': orchestrates several CLI coding agents (Claude Code, Codex, Cursor…) in parallel in isolated git worktrees. Source-available (Elastic License 2.0). **BYO agent**: drives your existing agents (no LLM key of its own). ⚠️ ≠ Apache Superset (BI)"
migrated_from: superset
---

# Superset (superset-sh)

**In one sentence** — a desktop app, an "IDE/terminal for the agent era", that lets you launch and drive in parallel an army of CLI coding agents (Claude Code, Codex, Cursor…), each isolated in its own git worktree.

> ⚠️ Name clash: **nothing to do with Apache Superset** (the BI/dataviz tool). This page is about **superset-sh/superset**, a coding-agent orchestrator.

## Type & integration
**Electron desktop application** (TypeScript 95%, React, TailwindCSS, Bun runtime, Turborepo). Works as an **orchestrator / agent manager**, not as an agent or an MCP server. **Agent-agnostic**: compatible with any coding agent that runs in a terminal (Claude Code, OpenCode, Cursor, Codex…).

Key features:
- **Parallel execution**: 10+ agents simultaneously on the machine.
- **Git worktree isolation**: each task has its own branch and working directory.
- **Agent monitoring**, integrated **diff viewer**, **workspace presets**, open-in-editor.

## Pricing model
**Source-available** under **Elastic License 2.0 (ELv2)**: public, usable code, but with **restrictions on commercial use** without an explicit license → *not open-source in the OSI sense*. Downloadable app; monetization model undetailed (likely an eventual commercial/cloud offering). Team based in San Francisco.

## LLM cost
**No LLM cost of its own** 🟢 — Superset **uses no LLM** itself: it **drives your existing agents** (Claude Code, Codex, Cursor…), which carry **their own authentication** (Claude subscription/login or key). The README confirms: "**No … third-party credentials needed**" at setup, and "**You choose which agents, providers, and integrations to connect**". So **no LLM key to give Superset** — same logic as [Orca](orca.md), [Conductor](conductor.md), [Supacode](supacode.md); the LLM cost is that of the underlying agents. *(LLM cost 🟢 verified against the README, 2026-06-16.)*

⚠️ Mind the cost in parallel mode: running 10+ agents simultaneously **multiplies** the token consumption of the underlying agents.

## What it's for
Coordinating the work of several autonomous agents: parallelizing tasks, avoiding context-switching cost, reviewing/merging the results. Relevant as tools move from chat to autonomous **CLI workers** run as a fleet.

## Notes
- "Coding agents & IDEs" family, but at a **meta** level: it doesn't code, it runs those who code (e.g. [Kilo Code](kilo-code.md) and other CLI agents).
- To distinguish from [MindFlight Orchestrator (MFO)](mindflight-orchestrator.md): MFO orchestrates agents for **enterprise business processes**; Superset orchestrates **coding agents** for developers.
- To dig into: pricing of a possible Pro/cloud offering, cost management under massively parallel execution.

## Source
- Repo: https://github.com/superset-sh/superset · Site: https://superset.sh/ · Docs: https://superset-sh-superset.mintlify.app/

*(verified on 2026-06-15 — GitHub README + web search)*
