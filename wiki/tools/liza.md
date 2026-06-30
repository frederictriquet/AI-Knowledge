---
tool: "Liza"
title: "Liza"
themes: [multi-agent]
type: "CLI (Go) — multi-agent coding system"
url: https://github.com/liza-mas/liza
pricing_model: "Open-source (Apache 2.0), free"
llm_cost: "Built-in — wraps existing CLI agents (BYO agent); no per-token billing via Liza"
objectives: [code-generation]
family: "Coding orchestrators & multi-agent systems"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "*Disciplined* multi-agent coding system (Apache 2.0, Go): frames existing agents (Claude Code, Codex, Gemini…) with behavioral contracts, adversarial doer/reviewer pairs and deterministic supervisors; neutralizes 55+ LLM failure modes, autonomous spec→code pipeline. BYO agent"
---

# Liza

**In one sentence** — "Disciplined Multi Coding Agent System": an orchestrator that *mechanically frames* existing coding agents to ship production-quality code on the first pass, by enforcing best practices through code rather than hoping the agent obeys.

## Type & integration
**CLI (`liza` binary)** written in **Go** (~35,000 lines + ~92,000 lines of tests), open-source. Neither an MCP server nor a library: a standalone orchestrator/framework installed and run locally. It **wraps existing agent CLIs** — Claude Code, Codex, Kimi, Mistral, Gemini, OpenCode — rather than calling the APIs directly.

Hybrid architecture: **deterministic supervisors in Go** mechanically enforce state transitions, role boundaries, merge authority and TDD gates; the **LLM agents** handle only judgment, under a **behavioral contract**. Auditable state in `.liza/state.yaml` and `.liza/log.yaml`.

Three modes: **Pairing**, **Adversarial Pairing**, and **Multi-Agent** (autonomous spec→code pipeline, 13 roles across 4 phases: specification, architecture, coding, integration).

## Pricing model
**Open-source, Apache 2.0 license**, free. Community project (⚠️ "single-maintainer" risk: one main author, no formal contribution pipeline at this stage).

## LLM cost
**Built-in** 🟢 — no per-token billing via Liza: it relies on your **personal** agent **configuration** ("your personal setup is used"), so your existing subscriptions (BYO agent). Notable point: multi-reviewer mode requires a **provider-diversity quorum** (≥2 distinct LLMs) to avoid single-provider bias → you need **several provider credentials**. Weak models can fail the "contract capability test".

## What it's for
Bridging the "it worked in the demo" gap: neutralizing **55+ documented LLM failure modes** (sycophancy, fake fixes/"phantom fixes", scope creep, test corruption, hallucinated completions), each mapped to a countermeasure. Adversarial **doer/reviewer** pairs with *binding* authority (the reviewer can block the merge), autonomous sprints, the human acting as a "circuit-breaker" between sprints.

## Competitive positioning
*(from the repo's `specs/architecture/competition-survey`)*

Liza claims to be alone in the **"behavioral enforcement"** category: trust through *mechanical* constraint (code), not through prompting. Key comparisons:

- **BMAD-METHOD** (~45k★, JS) — full-lifecycle agile methodology (Analysis → Planning → Solutioning → Implementation). A philosophical neighbor, judged **complementary**: BMAD upstream (methodology, PRD, architecture, UX) feeds Liza's disciplined execution downstream. BMAD = human-in-the-loop; Liza = constrained autonomous execution.
- **GSD** (~37k★) — the closest direct competitor by traction; it solves context degradation (fresh sub-agents), Liza solves *behavioral* failures (even with fresh context).
- **gstack** (~100k★) — broad workflow suite; no binding review authority or crash recovery, where Liza adds supervisor-owned task state.
- **CrewAI** (~45k★) — general framework; its guardrails are post-hoc, Liza prevents structurally.
- **Symphony** (OpenAI, preview) — scheduler without approval/sandbox; Liza = the supervision you add on top.
- **Paperclip** (~14k★, business ops) and **Ruflo** (breadth: 60+ agent types, 215+ tools, ML routing) — Liza makes the opposite bet: **depth** (few roles, behavioral enforcement).

Strategic insight from the document: "the scheduler/orchestrator layer is becoming commoditized" while "enterprise trust remains unsolved". **Acknowledged weaknesses**: trivial tasks (disproportionate ceremony), fuzzy needs (no product-discovery workflows), models too weak, setup cost (multi-terminal, multi-credential).

## Notes
- Family 1b, but with a distinct **"discipline/quality" flavor** from the parallel runners ([Superset (superset-sh)](superset.md), [Conductor](conductor.md), [Supacode](supacode.md), [Orca](orca.md)) that mainly target **throughput**. Liza targets **reliability** through enforcement.
- Also overlaps **spec-driven** ([Cavekit](cavekit.md)) via its spec→code pipeline, but with an added mechanical enforcement layer.
- Cited competitors = candidate notes: **BMAD**, **GSD**, **gstack**, **CrewAI**, **Ruflo**, **Paperclip**.
- ⚠️ The entire competitive comparison comes from Liza's own repo (self-assessment) — including the ★ attributed to competitors and the "55+ documented failure modes": to be cross-checked against third-party sources. And Liza itself is **tiny (~274★ actual, GitHub API)**: the category-pioneer tone reflects no broad adoption.

## Source
- Repository: https://github.com/liza-mas/liza · Docs: https://lizamas.mintlify.app/
- Comparison: https://github.com/liza-mas/liza/tree/main/specs/architecture/competition-survey

*(verified on 2026-06-15 — README + repo competition-survey + web search)*
