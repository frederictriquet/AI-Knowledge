---
tool: "Conductor"
title: "Conductor"
themes: [multi-agent, frameworks-tooling]
type: "Mac desktop app (coding-agent orchestrator)"
url: https://www.conductor.build/
pricing_model: "Free app (proprietary); Enterprise section — BYO Claude/Codex subscription"
llm_cost: "Built-in — uses your existing Claude Code (or Codex) subscription/login, no separate LLM cost"
objectives: [code-generation]
family: "Coding orchestrators & multi-agent systems"
eco_icons: "🔒"
llm_cost_icons: "🟢"
summary: "Mac app (Melty Labs, YC) that runs several Claude Code/Codex/Cursor agents in parallel in isolated git worktrees; centralized review and merge. **Free but proprietary** (Enterprise coming), uses your existing Claude/Codex subscription. macOS + GitHub only"
---

# Conductor

**In one sentence** — Mac app that runs several Claude Code (and Codex, Cursor) agents in parallel, each in an isolated copy of the repo, to view, review and merge their changes in one place.

## Type & integration
**macOS-only desktop application**, developed by **Melty Labs** (Y Combinator alumnus). A coding-agent orchestrator: each task gets its dedicated **workspace = git worktree** (branch, files, terminal, diff, review flow). Conductor copies only **git-tracked** files (no duplication of `node_modules`/`.env`). Works with your **local Claude Code login**; **GitHub-compatible repos** only at this stage.

## Pricing model
**Free app**, **proprietary** (closed-source). **No public pricing page** (/pricing is 404): no current paid offering; an **Enterprise/teams offering is announced as coming** (roadmap, unpriced). You bring your own Claude or Codex subscription.

## LLM cost
**Built-in** 🟢 — Conductor adds no model cost: it leans on your **existing Claude/Codex subscription** (Claude Code login), not on separately-billed API keys. You already pay the agent's subscription; Conductor is only the orchestration layer.

⚠️ As with [Superset (superset-sh)](superset.md), massively **parallel** execution multiplies the agents' real usage → watch out for your subscription's **rate limits/quotas** when 5–10 agents run together.

## What it's for
Parallelize coding work: launch several agents on different tasks (or the same one, as variants), see at a glance what each is doing, then review/merge. Targets Mac developers already using Claude Code who want to go from one agent to a **fleet**.

## Notes
- **Direct competitor of [Superset (superset-sh)](superset.md)**: same promise (parallel coding agents, isolated worktrees). Differences: Conductor = **Mac only, free, proprietary, BYO subscription**; Superset = **cross-platform (Electron), source-available ELv2, BYOK keys**. Existing comparisons: Conductor vs Intent (another macOS orchestrator).
- Distinct from [MindFlight Orchestrator (MFO)](mindflight-orchestrator.md) (enterprise business-process orchestration, not coding).
- To dig into: content/price of the Enterprise offering, non-GitHub support, Linux/Windows support.

## Source
- Official site: https://www.conductor.build/ · Docs: https://docs.conductor.build/
- Review: The New Stack ("Hands-On Review of Conductor")

*(verified on 2026-06-15 — official site + web search)*
