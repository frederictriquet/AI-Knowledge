---
tool: "TRIP-workflow"
title: "TRIP-workflow"
themes: [frameworks-tooling, multi-agent, efficiency-cost]
type: "Skills pack / dev workflow (SKILL.md) for AI coding agents"
url: https://github.com/PiLastDigit/TRIP-workflow
pricing_model: "Free / source-available — ⚠️ MIT claimed (badge) but no LICENSE file"
llm_cost: "🟢 drives your existing coding agents (Claude Code + Codex CLI); takes no key of its own"
family: "Workflow, methodology & spec-driven development"
objectives: [code-generation]
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Deliberately minimal 3-command dev workflow (Plan → Implement → Release) as a SKILL.md pack; central `ARCHI.md` architecture-memory file; default cross-model review (Claude writes, Codex reviews). ⚠️ **MIT claimed but no LICENSE file**; young (v2.1.0), single-author, model-name jargon that dates fast; needs two agent accesses"
---

# TRIP-workflow

**In one sentence** — A deliberately minimal, opinionated skills pack (`SKILL.md`) that wraps AI-agent coding into three commands (Plan → Implement → Release) around a single `ARCHI.md` architecture-memory file, with cross-model review (one model writes, a different one reviews) as the default.

## Type & integration
A **pack of 14 skills** you copy into `.claude/skills/` (or equivalent), then bootstrap with `/TRIP-init`. Core: `/TRIP-1-plan`, `/TRIP-2-implement`, `/TRIP-3-release`; support skills for review/test/upgrade/hotfix/research/compact and Codex delegation. Skills are Markdown "instructions in human language" plus Shell helper scripts — **interpreted by the agent, so behaviour is non-deterministic** (reliability rides on the model). Primary target Claude Code (Agent Skills standard); claims compatibility with OpenCode, Codex CLI, Mistral Vibe (a `AskUserQuestion` shim is needed for Mistral — a sign of rough edges).

## Pricing model
Free, public source. **⚠️ License gap (verified 2026-07-15)**: the README shows an "MIT" badge, but there is **no LICENSE file** in the repo and GitHub detects no license → by default **all rights reserved**. Treat as *source-available*, not open-source, until the author actually adds a license — matters before any fork/commercial reliance.

## LLM cost
**🟢** — TRIP is skills + shell scripts that **orchestrate your existing agents**: the main session runs in Claude Code, and `TRIP-2-implement` delegates the actual edits to the **Codex CLI** (`codex-implement` shells out to `codex` in a workspace-write sandbox). It **takes no API key of its own** and resells nothing; cost is borne by your existing Claude Code + Codex access.
> ⚠️ The **default flow needs two paid agent accesses** (Claude *and* Codex), and the cross-model review loops (`codex-plan-review`, `codex-code-review`, `codex-ask`) **add** calls on the second provider. The README touts `ARCHI.md` token *savings* (one read vs re-globbing) — plausible but **unmeasured** — while staying silent on the token cost those review loops add. Net token effect: **unverified**.

## What it's for
Shipping features with an agent while keeping the ceremony near zero — an explicit reaction against heavier frameworks ([BMAD](bmad-method.md), Superpowers, Gastown) it calls "overwhelming". Two ideas carry real value: (1) **`ARCHI.md`**, a tool-agnostic architecture memory read at the start of each task (persistent context across sessions, less re-exploration); (2) **cross-model review by default** — writer and reviewer are never the same thread *or model* ("you wouldn't smell your own fart"), which is a sound take on independent verification.

## Notes
- **Maturity — be skeptical**: v2.1.0, **single author**, ~361 stars, no tests/eval of the workflow itself, playful "BS-free" marketing tone. Treat claims as self-declared.
- **Perishable jargon**: hard-codes current model names/opinions (e.g. "Fable writes, GPT-5.6 reviews… peak as of mid-July 2026") — will age fast and needs re-reading against whatever models exist when you use it.
- **Non-determinism**: "init = a script written in human language" and Markdown skills mean an LLM interprets the steps; robustness depends on the agent, not on code.
- **When NOT to use**: if you can't/won't run two agent providers; if you need a licensed (legally clear) dependency today; if you want deterministic, testable tooling.
- **Neighbours / alternatives**: [BMAD-METHOD](bmad-method.md), [gstack](gstack.md), [gsd](gsd.md), Superpowers. Recommends only two MCP servers ([Context7](context7.md) for docs, [Exa](exa-mcp.md) for search) — a defensibly minimal stance.

## Source
https://github.com/PiLastDigit/TRIP-workflow (README v2.1.0; `skills/` = 14 SKILL.md packs; **no LICENSE file** — GitHub API license = none, `/LICENSE` returns 404). *(verified on 2026-07-15)*
