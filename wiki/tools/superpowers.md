---
tool: "Superpowers"
title: "Superpowers"
themes: [frameworks-tooling]
type: "Agentic-skills plugin / framework (cross-platform)"
url: https://github.com/obra/superpowers
pricing_model: "Open-source (MIT), free (GitHub sponsorships)"
llm_cost: "Built-in — runs inside your agent (Claude Code…), BYO LLM, no separate cost"
objectives: [code-generation]
family: "Workflow, methodology & spec-driven development"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Agentic-skills framework + dev methodology by Jesse Vincent (obra), ~93k★, #1 Claude Code plugin: enforces brainstorming, worktrees, TDD, sub-agent review. Cross-platform, MIT, runs inside your agent"
---

# Superpowers

**In one sentence** — a framework of *composable* agentic skills paired with a complete software-development methodology, which stops the agent from charging head-first into the code and forces design review, TDD and systematic planning on it.

## Type & integration
**Skills plugin / framework**, created by **Jesse Vincent (`obra`)** and the **Prime Radiant** team. Cross-platform: Claude Code (official Anthropic marketplace), Codex CLI/App, Cursor, GitHub Copilot CLI, Gemini CLI, Factory Droid, OpenCode. Typical Claude Code install: `/plugin install superpowers@claude-plugins-official`.

It relies on **composable skills** that trigger automatically depending on context, and structures the work in ~7 steps: brainstorming → git worktrees → planning → execution → TDD → code review (by sub-agents) → branch finishing. Includes the ability to **write new skills**.

## Pricing model
**Open-source, MIT license**, free. The author accepts **sponsorships** (GitHub Sponsors); no announced commercial tier. Very popular (**~237k★**, GitHub API), often presented as the flagship skills plugin of the Claude Code ecosystem — popularity ≠ fit for your need (see the limitation below).

## LLM cost
**Built-in** 🟢 — no embedded LLM: Superpowers runs inside your agent (Claude Code and others) and uses **your own subscription / your keys** (BYO). No separate LLM cost; the actual spend depends on the underlying agent. Note: a more rigorous methodology (TDD, review sub-agents) can increase the number of steps/tokens, in exchange for better quality.

## What it's for
Imposing a real engineering methodology on an agent: without it, a "vanilla" Claude Code on a complex project writes code without tests, mixes responsibilities and produces a fragile prototype. Superpowers forces TDD, breaking work into 2–5 min tasks with explicit specs, sub-agent review, systematic debugging. Adopted/documented by well-known practitioners (e.g. Simon Willison).

## Notes
- ⚠️ **When NOT to use it**: on a simple fix or a throwaway script, imposing brainstorming + worktrees + TDD + sub-agent review is **over-engineering** — extra latency and tokens (multiplied steps/sub-agents) for no gain. The benefit concentrates on complex, durable projects.
- **Family 4 (workflow/methodology)**: same category as [Cavekit](cavekit.md), [BMAD-METHOD](bmad-method.md), [GSD (Get Shit Done)](gsd.md) and [gstack](gstack.md) — layers that structure *how* the agent works. Superpowers is the most popular and the most "complete methodology" of the group (TDD + sub-agents + extensible skills).
- Overlaps the 1b sub-cluster through its use of **sub-agents** for review, but remains a **methodology/skill** (not a fleet runner like [Orca](orca.md)/[Superset (superset-sh)](superset.md)).
- Extensible skills → you can write your own; an ecosystem of third-party skills.

## Source
- Repo: https://github.com/obra/superpowers · Claude plugin: https://claude.com/plugins/superpowers
- Analysis: Simon Willison, "Superpowers: How I'm using coding agents in October 2025" (simonwillison.net)

*(verified on 2026-06-15 — GitHub README + web search)*
