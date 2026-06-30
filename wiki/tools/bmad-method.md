---
tool: "BMAD-METHOD"
title: "BMAD-METHOD"
themes: [frameworks-tooling]
type: "Framework / methodology (AI agents for the IDE)"
url: https://github.com/bmad-code-org/BMAD-METHOD
pricing_model: "Open-source (MIT license) — 100% free, no paywall or gated content"
llm_cost: "Built-in (🟢) — runs INSIDE your AI client (Claude Code, Cursor…), no dedicated LLM API key required; the LLM cost is your client's"
objectives: [code-generation]
family: "Workflow, methodology & spec-driven development"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Open-source methodology (MIT, ~49k★) for AI-driven agile development: 21 agent-personas and 50+ guided workflows, from brainstorming to deployment, inside your IDE (Claude Code, Cursor). BYOK"
---

# BMAD-METHOD

**In one sentence** — open-source framework for AI-driven agile development ("Breakthrough Method for Agile AI-Driven Development") that orchestrates around twenty specialized agent-personas (PM, Architect, Dev, UX…) through guided workflows covering the whole product cycle, from brainstorming to deployment.

## Type & integration
It's not a standalone application but a **methodology + a set of agents and workflows** installed into your project (via `npx bmad-method install`) and then driven from your usual IDE/AI agent (Claude Code, Cursor, etc.). Written mostly in JavaScript/Node (with HTML for docs and Python for some tools; prerequisites Node ≥ 20.12, Python ≥ 3.10, `uv`). It provides 21 specialized agents and 50+ guided workflows, plus a "Party Mode" gathering several personas in one session. Current version v6.8.0 (mid-2026).

The cycle is structured in four major phases: **Analysis → Planning → Solutioning → Implementation**, with "scale-adaptive" intelligence adjusting from a simple bug-fix to an enterprise system.

## Pricing model
**Open-source under MIT license**, fully free. The project claims no paywall, no gated content, no closed Discord. Strong community traction: ~49k★, ~5.7k forks, over a hundred contributors, a multilingual docs site (5 languages) and a "marketplace" system. Some ecosystem resources around the author (bmadcode.com, YouTube channel, community Discord).

## LLM cost
**Built-in 🟢 — no LLM API key required** (verified: 0 mentions of key/BYOK in the README; prerequisites = only Node/Python for the installer). BMAD is a set of Markdown prompts/agents that **runs INSIDE your AI client** (Claude Code, Cursor…) and therefore consumes the LLM via **that client** (your existing subscription), with no key of its own and no surcharge. A "web bundles" option (Gemini Gems / Custom GPTs) lets you plan on a flat web subscription. The LLM cost depends on your own consumption client-side. Since the method multiplies agents and workflows (analysis, planning, architecture, implementation, review…) over long sessions, token usage can be substantial in order of magnitude, but it remains your direct LLM bill.

## What it's for
Frame and run a software (or game) project end to end with the AI as an expert collaborator rather than an autonomous executor: brainstorming, market/domain research, PRFAQ (Amazon's Working Backwards), UX design, PRD, architecture, then implementation, testing, security, DevOps and documentation treated as first-class phases. The stated philosophy: the AI "guides you through a structured process to surface your best thinking", without thinking for you.

## Notes
- BMAD appears in [Liza](liza.md)'s competitive comparison (`liza-vs-bmad-comparison.md`). The document presents them as **architecturally complementary** rather than competitors: BMAD is strong on **upstream product discovery** (ideation, planning, broad organizational scope), where Liza stays deliberately lightweight; conversely, Liza bets on **downstream execution** and **mechanical enforcement** of constraints.
- Limits flagged by the Liza comparison (to verify independently, biased source): (1) discipline **at the prompt level** with no mechanical safeguards (nothing technically stops an agent from bypassing the workflow or merging without review); (2) **state loss between sessions** (fresh chat per workflow, no cross-workflow persistence); (3) **sequential execution** by design — no coordination of parallel agents on the same code.
- Several community forks exist (namesakes: `macelik/bmad-method`, `ResourcefulAI/bmad-method`, `EvolutionAPI/BMAD-METHOD-BY-EVOLUTION`, etc.); the reference repo is indeed **`bmad-code-org/BMAD-METHOD`**.
- Notable branches: `v6-alpha`, `V4` — active versioning.
- ⚠️ Traction (~49k★) and the "scale-adaptive" / "no paywall" claims are self-declared by the vendor, not proof of quality; the only documented limits in the corpus come from a competitor (Liza, biased source) — validate independently on a real project.

## Source
- Official repo: https://github.com/bmad-code-org/BMAD-METHOD *(verified on 2026-06-15)*
- Site: https://bmadcode.com — Docs: https://docs.bmad-method.org *(references cited by the repo; not re-fetched one by one)*
- Liza comparison: https://raw.githubusercontent.com/liza-mas/liza/main/specs/architecture/competition-survey/liza-vs-bmad-comparison.md *(verified on 2026-06-15; biased source, competitor's viewpoint)*
