---
tool: "gstack"
title: "gstack"
themes: [frameworks-tooling]
type: "Open-source skill/workflow suite for AI coding agents (Claude Code and compatibles)"
url: https://github.com/garrytan/gstack
pricing_model: "Open-source free (MIT license) — no paid tier; you only pay for your AI agent (Claude Code subscription, API, etc.)"
llm_cost: "Built-in — gstack embeds no LLM; it runs in/with your existing agent (Claude Code, Codex, Cursor...) and consumes its subscription / API key (BYOK on the agent side)"
objectives: [code-generation]
family: "Workflow, methodology & spec-driven development"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Open-source Claude Code config by Garry Tan (YC): 23+ \"opinionated\" skills making the agent play the roles of a team (CEO, Designer, QA…) to leverage solo dev"
---

# gstack

**In one sentence** — Garry Tan's (CEO of Y Combinator) personal open-source configuration for Claude Code: a suite of "opinionated" skills / slash-commands that make the AI agent play the roles of a complete team (CEO, Designer, Eng Manager, Release Manager, Doc Engineer, QA) to give a solo developer team-scale leverage.

## Type & integration
A collection of skills (slash-commands) and helper tools (Bun/TypeScript, a persistent Chromium daemon for browser QA) to install in an AI coding agent. Designed first for **Claude Code**, but portable to about a dozen other hosts via the `SKILL.md` standard: OpenAI Codex CLI, GitHub Copilot, VS Code, Cursor, etc. The skills cover the whole cycle: product/planning, implementation, review, browser QA, design, release/deploy, memory management and security safeguards. An imposed "sprint" methodology: think → plan → build → review → test → ship → reflect, in parallel across several projects.

## Pricing model
**Open-source project, MIT license, entirely free**. No premium tier, no waitlist, no resale. The repo saw viral growth (≈90k★ in under two months, ≈110k★ by mid-2026). Garry Tan claims to have shipped 600,000+ lines of production code in 60 days with this configuration while running YC full-time.

## LLM cost
**Built-in** in the sense of our grid: gstack neither embeds nor bills any LLM. It is a workflow layer that runs *inside* an already installed AI coding agent and consumes its engine. The inference cost is therefore borne by the host agent (Claude Code subscription, Anthropic API key, etc.) — i.e. BYOK / subscription on the agent side, not on gstack's side.

## What it's for
Giving a lone developer maximal leverage by turning a general-purpose coding agent into a team of specialists governed by a process. The central idea: AI agents need a *process* (roles, reviews, QA, safeguards) and not just prompts. Concretely you run commands like `/plan-ceo-review`, `/review`, `/browse`, `/qa`, `/codex` to orchestrate planning, implementation, code review (including flaw detection), browser testing and release.

## Notes
- Appears in [Liza](liza.md)'s competitive survey (`specs/architecture/competition-survey/mas-survey.md`) as an example of a "broad suite/workflow optimizing solo-developer productivity". Claimed philosophy (ETHOS.md): *Boil the Lake*, *Search Before Building*, *User Sovereignty* — "optimize to give an active human a broad bench of specialized workflows and fast feedback loops".
- Often compared to other orchestration frameworks for Claude Code: **Superpowers**, **GSD**, **GSTACK** (cf. Pulumi blog).
- Name clash resolved: there are other unrelated "gstack" (various GitHub topics, `gstack-opencode` which is a third-party port). The tool meant here is indeed `garrytan/gstack`, tied to AI coding agents.
- ⚠️ "600,000+ lines in 60 days" and the ~114k★ are **self-declared/viral** figures, not proof of quality; an "opinionated" solo config (fixed roles, imposed sprint) — poorly suited if your process differs, and largely redundant with Superpowers/GSD.

## Source
- https://github.com/garrytan/gstack — official repo (README, MIT license, ≈110k★) *(verified on 2026-06-15)*
- https://raw.githubusercontent.com/liza-mas/liza/main/specs/architecture/competition-survey/mas-survey.md — positioning in the Liza survey *(verified on 2026-06-15)*
- https://www.pulumi.com/blog/claude-code-orchestration-frameworks/ — Superpowers / GSD / GSTACK comparison *(verified on 2026-06-15)*
