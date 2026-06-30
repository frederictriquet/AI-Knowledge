---
tool: "Cavekit"
title: "Cavekit"
themes: [efficiency-cost, frameworks-tooling]
type: "Plugin (Claude Code) + skills"
url: https://github.com/JuliusBrussee/cavekit
pricing_model: "Open-source (MIT), free"
llm_cost: "Built-in — runs inside Claude Code, no separate LLM cost"
objectives: [code-generation]
family: "Workflow, methodology & spec-driven development"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Spec-driven development plugin for Claude Code: durable specs that survive context resets, backprop of test failures; 'caveman' encoding to reduce tokens"
---

# Cavekit

**In one sentence** — *spec-driven* development plugin for Claude Code: it turns a natural-language intent into durable specifications, then executes them, with specs that survive context resets.

## Type & integration
**Claude Code plugin** (installable via the marketplace) and a **skills framework**. Specs in **Markdown** + shell commands. Runs entirely inside Claude Code. Same author as [Caveman](caveman.md) and [Cavemem](cavemem.md) (Julius Brussee).

## Pricing model
**Open-source, MIT license**, free; community project.

## LLM cost
**Built-in** 🟢 — uses Claude via Claude Code, no API key or separate cost. Emphasizes **token efficiency** through "caveman encoding" (compressed specs, ~75% fewer tokens vs prose specs).

## What it's for
Bridge the gap between **planning and execution** in AI-assisted dev: maintain **durable specifications** that survive context resets, and **automatically backpropagate** test failures into the specs (less manual tracking). v4 philosophy: "one spec, three commands, no orchestration".

## Notes
- v3.1.0 included a **cross-model peer review** (via Codex); **v4 removed it** in favor of simplicity.
- Julius Brussee's "cave\*" ecosystem: [Caveman](caveman.md) (output compression), [Cavemem](cavemem.md) (persistent memory), Cavekit (spec-driven). Caveman encoding is the common thread.
- ⚠️ Specific to Claude Code (lock-in); the "~75% tokens" gain (caveman encoding) is self-declared, not independently measured; a spec-driven workflow adds unjustified ceremony on simple tasks.

## Source
- Repo: https://github.com/JuliusBrussee/cavekit

*(verified on 2026-06-15 — GitHub README)*
