---
tool: "GitHub Spec Kit"
title: "GitHub Spec Kit"
themes: [frameworks-tooling, prompting]
type: "CLI toolkit (spec-driven development)"
url: https://github.com/github/spec-kit
pricing_model: "Open-source (MIT)"
llm_cost: "Built-in (runs inside your existing agent)"
objectives: [code-generation]
family: "Workflow, methodology & spec-driven development"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "**Official GitHub** toolkit (MIT) for spec-driven dev: the `Specify` CLI + `/speckit.*` commands (constitution→spec→plan→tasks→implement) on top of your agent (Claude Code, Copilot, Cursor, Gemini, Codex, 24+). No LLM of its own"
---

# GitHub Spec Kit

**In one sentence** — an open-source **spec-driven development** toolkit (GitHub): the written spec becomes the executable artifact that generates the code, via a `Specify` CLI and commands orchestrated on top of your coding agent.

## Type & integration
A **Specify** CLI (installed via `uv`/`pipx`, requires Python 3.11+ and Git) that lays down a sequential slash-command workflow: `/speckit.constitution` → `/speckit.specify` → `/speckit.plan` → `/speckit.tasks` → `/speckit.implement`. **Provides no LLM**: it is a methodology layer executed by an existing agent — Claude Code, GitHub Copilot, Cursor, Gemini CLI, Codex and 24+ others.

## Pricing model
**Open-source MIT**, free.

## LLM cost
**🟢 Built-in**: it runs inside your agent (Claude Code, etc.) → no key or LLM cost of its own; consumption is that of the agent you already use.

## What it's for
Structuring AI-assisted dev around durable specs (constitution → spec → plan → tasks → implementation) rather than ad-hoc prompting. Same family as BMAD-METHOD, GSD, Superpowers.

## Notes
- **Official GitHub** project → good longevity a priori.
- Direct competitor to Kiro's (AWS) spec-driven methodology and to OpenSpec.
- ⚠️ A methodology layer, not a magic gain: on simple tasks the spec→plan→tasks ceremony adds friction and tokens; mostly relevant on durable multi-step projects. Being "official GitHub" guarantees neither traction nor maintenance.

## Source
https://github.com/github/spec-kit (LICENSE = MIT). *(verified on 2026-06-17)*
