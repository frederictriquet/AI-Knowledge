---
tool: "Paperclip"
title: "Paperclip"
themes: [multi-agent, governance-alignment-ops]
type: "Open-source AI-agent orchestration and governance platform (\"zero-human companies\")"
url: https://github.com/paperclipai/paperclip
pricing_model: "Open-source (MIT), self-hosted, free — no account or paid tier; you supply your own agents/keys"
llm_cost: "No own LLM cost (🟢) — \"Bring Your Own Agent\": orchestrates your existing agents (Claude Code, Codex, Cursor…) that carry their own auth; Paperclip takes no LLM key. Per-agent budget tracking"
objectives: [production]
family: "Multi-agent orchestration & enterprise automation"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Open-source platform (MIT) modeling a team of AI agents as a company — org chart, budgets, approval gates — for human-controlled \"zero-human companies\". **BYO Agent**: orchestrates your existing agents (Claude Code, Codex, Cursor…) that carry their own auth → no LLM key of Paperclip's own; per-agent budget tracking. Self-hostable"
migrated_from: paperclip
---

# Paperclip

**In one sentence** — Open-source platform that models a team of AI agents as a company (org chart, roles, budgets, approval governance) to run "zero-human companies" under human control.

## Type & integration
Self-hosted multi-agent orchestration platform (Node.js 20+ / React / PostgreSQL, ~98% TypeScript). "Agent-agnostic": it does not provide the model, it coordinates external agents (Claude Code, OpenAI Codex, Google Gemini, Cursor, etc.) around a shared org chart, shared goals, tickets/issues and scheduled heartbeats. Multi-tenant (isolation per "company").

## Pricing model
Open-source project under MIT license, free and self-hosted. No Paperclip account required, no paid tier announced to date: control and costs stay on the user's side. Official site: https://paperclip.ing — canonical repo: https://github.com/paperclipai/paperclip.

## LLM cost
**No own LLM cost** 🟢 — "**Bring Your Own Agent**" (verified in README): Paperclip neither resells nor embeds an LLM; it **drives your existing agents** (Claude Code, Codex, Cursor, OpenClaw…), which carry **their own auth/subscription**. Paperclip does **not** ask for an LLM key — same logic as the orchestrators [Superset (superset-sh)](superset.md) / [Multica](multica.md) (and not direct BYOK). Cost control is done via **monthly budget per agent** (warning at 80%, block/auto-pause at 100%), with token/cost tracking per company, agent, project, goal, issue, provider and model. *(LLM cost 🟢 verified on 2026-06-16.)*

## What it's for
Run near-autonomous AI-agent companies while keeping the human as the "board of directors". Product core: org charts and hierarchical roles, alignment on goals, work tracking via tickets (atomic checkout to avoid duplicates), recurring heartbeats, and above all a governance layer — hard budget caps, approval gates (an agent cannot "hire" another or execute a strategy without validation), agent lifecycle (pause/resume/stop) and an append-only audit log.

## Notes
- Very homonymous name: not to be confused with the "Paperclip" clipboard manager, the `paperclip` Rails ActiveStorage gem, etc. The intended identity here is indeed the AI-agent platform for business operations (verified).
- On stars: the Liza comparison cites "~14k★ … 14k stars in days" (snapshot at launch). The canonical repo `paperclipai/paperclip` shows ≈70k★ (recorded 2026-06-15), a sign of very fast traction. A repo `agencyenterprise/paperclip-ai` also exists (≈3★) — probably origin/mirror from the publisher (Agency Enterprise / Ry Walker).
- "Narrative" positioning competing with [Liza](liza.md): Paperclip = "zero-human companies" (business operations) vs Liza = "zero-trust agent sessions" (software engineering). Direct functional overlap is low but head-on on the narrative. See also [MindFlight Orchestrator (MFO)](mindflight-orchestrator.md) on the enterprise-automation side.

## Source
- https://github.com/paperclipai/paperclip *(verified on 2026-06-15)*
- https://paperclip.ing/ *(verified on 2026-06-15)*
- https://github.com/agencyenterprise/paperclip-ai *(verified on 2026-06-15)*
- Liza comparison — specs/architecture/competition-survey/mas-survey.md *(verified on 2026-06-15)*
