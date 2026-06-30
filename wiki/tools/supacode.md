---
tool: "Supacode"
title: "Supacode"
themes: [multi-agent, frameworks-tooling]
type: "Native macOS desktop application (coding-agent orchestrator)"
url: https://supacode.sh/
pricing_model: "Source-available (FSL-1.1-ALv2: anti-competition clause, converts to Apache-2.0 after 2 years) — free beta (DMG / Homebrew). Vendor: Supabit, LLC"
llm_cost: "Built-in — BYO agent; uses your existing CLI subscriptions (Claude Code, Codex…), no LLM cost of its own"
objectives: [code-generation]
family: "Coding orchestrators & multi-agent systems"
eco_icons: "🔓🔒"
llm_cost_icons: "🟢"
summary: "Native macOS app (on libghostty, not Electron) orchestrating 50+ coding agents in parallel in isolated worktrees; an 'infinite canvas terminal board'. **Source-available (FSL-1.1, becomes Apache-2.0 at 2 years)**, free beta, BYO agent. macOS 26 Tahoe required"
---

# Supacode

**In one sentence** — a native macOS app, an "infinite canvas terminal board", that orchestrates dozens of CLI coding agents in parallel, each in its own isolated environment.

## Type & integration
**Native macOS app**, built on **libghostty / GhosttyKit** (the engine of the Ghostty terminal) — **not Electron**, hence a **native performance** argument. Agents run directly in the integrated terminal, "no translation layer". **Agent-agnostic**: Claude Code, OpenAI Codex, Opencode, any CLI agent. Isolation via **git worktrees**. GitHub integration (PRs, CI checks). ⚠️ Requires **macOS 26 Tahoe**.

## Pricing model
⚠️ **Not open-source in the OSI sense**: **Functional Source License v1.1 (FSL-1.1-ALv2)** license verified in the LICENSE file (Copyright 2026 **Supabit, LLC**). It is **source-available** with an **anti-competition clause** (forbids reselling/substituting the software as a competing product), which **automatically converts to Apache-2.0 after 2 years**. The landing page says "Fully open on GitHub" but the code is under FSL, not an OSI license. Distributed as a **free beta** (DMG / Homebrew). Repo: `supabitapp/supacode`.

## LLM cost
**Built-in** 🟢 — Supacode neither embeds nor manages an LLM: a **bring-your-own-agent** philosophy. You run your CLI agents with **their own subscriptions/credentials** (Claude Code Pro/Max, Codex…), and you manage those costs independently. Supacode = the orchestration/UI layer, with no model surcharge.

⚠️ Like [Superset (superset-sh)](superset.md) and [Conductor](conductor.md), running **50+ agents in parallel** multiplies the real usage of the agents → watch the quotas/rate limits of your subscriptions.

## What it's for
For "bleeding edge" macOS power users: driving a **massive fleet** of coding agents on a visual canvas, heavily parallelizing tasks, keeping each agent isolated. Still a young tool (early-stage) but ambitious on volume (50+).

## Notes
- **Third parallel coding-agent orchestrator** in the census, alongside [Conductor](conductor.md) and [Superset (superset-sh)](superset.md). Supacode's positioning: **native (libghostty, not Electron)**, **open-source/free**, **50+ agents** volume, **infinite canvas**; but **macOS 26 Tahoe required** (entry barrier).
- Quick comparison of the sub-cluster:
  - **Supacode** — native macOS, source-available (FSL-1.1, → Apache-2.0 at 2 years), 50+ agents, Tahoe required.
  - **Conductor** — Mac, free proprietary, BYO subscription, GitHub only.
  - **Superset** — cross-platform (Electron), source-available ELv2, BYOK keys.
- Distinct from [MindFlight Orchestrator (MFO)](mindflight-orchestrator.md) (business-process orchestration, not coding).

## Source
- Official site: https://supacode.sh/
- Reviews: everydev.ai, Ry Walker Research

*(verified on 2026-06-15 — official landing page + web search)*
