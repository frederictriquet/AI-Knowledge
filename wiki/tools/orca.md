---
tool: "Orca"
title: "Orca"
themes: [multi-agent, frameworks-tooling]
type: "Desktop app (Mac/Win/Linux) + mobile — Agent Development Environment (ADE)"
url: https://www.onorca.dev/
pricing_model: "Open-source (MIT), free"
llm_cost: "Built-in — BYO agent; uses your existing subscriptions/keys (Claude Code, Codex, Gemini… 25+)"
objectives: [code-generation]
family: "Coding orchestrators & multi-agent systems"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Open-source \"Agent Development Environment\" (stablyai, YC) to drive a fleet of coding agents in parallel: Kanban board, isolated git worktrees, WebGL terminals, built-in Chromium browser, SSH worktrees, GitHub/Linear integrations. Free MIT, BYO agent (25+)"
---

# Orca

**In one sentence** — open-source "Agent Development Environment" (ADE): an IDE built to drive a **fleet of coding agents in parallel**, where each agent becomes a Kanban card in its isolated git worktree.

## Type & integration
**Cross-platform desktop app** (macOS, Windows, **Linux**) — and **mobile** — built by **stablyai** (YC W2026). IDE-style environment for agents: terminal, file editor, built-in browser. **Agent-agnostic**: Claude Code, Codex, OpenCode, Gemini, Grok, Cursor CLI… 25+ CLI agents.

Notable features:
- **Kanban board** to track each agent's progress via drag-and-drop.
- **Isolated git worktrees** (no stash, no branch switching), one prompt → **5 agents in parallel**, then comparison and merge.
- **WebGL terminals** inspired by Ghostty (with splits).
- **Built-in Chromium browser** with "Design Mode".
- **Remote SSH worktrees**, **account switching** across multiple agent subscriptions.
- **GitHub** and **Linear** integrations, diff annotation.

## Pricing model
**Open-source, MIT license**, **free**, no subscription. Downloadable from onorca.dev or via GitHub Releases (github.com/stablyai/orca).

## LLM cost
**Built-in** 🟢 — Orca embeds no LLM: **bring-your-own-agent** philosophy. You use your **existing subscriptions/keys** on the agents (Claude Code Pro/Max, Codex, etc.; API via BYOK possible). Orca = orchestration layer + UI, with no model surcharge. `account switching` helps juggle multiple subscriptions.

⚠️ As with the whole sub-cluster, running a **fleet of agents in parallel** multiplies real usage → watch quotas and rate limits.

## What it's for
Manage the work of several agents as a dashboard: launch, compare, annotate, merge. Positioning "control center for parallel AI agents", "ship 100x" claim. The most feature-rich of the sub-cluster (Kanban, browser, SSH, Linear, mobile).

## Notes
- **Fourth parallel coding-agent orchestrator** in the census, alongside [Superset (superset-sh)](superset.md), [Conductor](conductor.md), [Supacode](supacode.md). Orca's positioning: **cross-platform (Mac/Win/Linux) + mobile**, **MIT open-source/free**, broadest feature set (Kanban, Design Mode browser, SSH worktrees, Linear).
- Quick sub-cluster comparison:
  - **Orca** — Mac/Win/Linux + mobile, MIT, Kanban + browser + SSH + Linear, 25+ agents.
  - **Supacode** — native macOS (libghostty), open-source, 50+ agents, Tahoe required.
  - **Conductor** — Mac, free proprietary, BYO subscription, GitHub only.
  - **Superset** — cross-platform (Electron), source-available ELv2, BYOK keys.
- Distinct from [MindFlight Orchestrator (MFO)](mindflight-orchestrator.md) (enterprise business-process orchestration, not coding).
- ⚠️ Very recent project (YC W2026): maturity and longevity unproven, "most feature-rich"/"ship 100x" claims taken from marketing — validate stability before industrializing a fleet of parallel agents.

## Source
- Official site: https://www.onorca.dev/ (and orcabuild.ai) · Docs: https://www.onorca.dev/docs
- Repo: https://github.com/stablyai/orca

*(verified on 2026-06-15 — official site + GitHub + web search)*
