---
tool: "cq"
title: "cq (Shared Agent Learning)"
themes: [memory, rag-context, efficiency-cost]
type: "Open standard + CLI / agent plugin / MCP server (multi-host)"
url: https://github.com/mozilla-ai/cq
pricing_model: "Open-source (Apache-2.0)"
llm_cost: "Built-in — queried by your existing coding agent via MCP; no key to cq, no resold tokens"
family: "Shared agent learning & knowledge commons"
objectives: [reliability, cost-control, code-generation]
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Open standard (Apache-2.0, by Mozilla.ai) for a shared agent-learning commons — agents query past learnings before unfamiliar work and propose new ones (confirm-through-use, staleness flagging); CLI + plugin (Claude/Codex/Cursor/OpenCode…) + MCP server + SDKs. ⚠️ Early (status 0.x/beta, ~1.2k★), no efficacy metrics; query overhead, knowledge-poisoning and private-code leakage risks unaddressed."
---

# cq (Shared Agent Learning)

**In one sentence** — an open standard + tooling for a **shared knowledge commons across coding agents**: before unfamiliar work an agent queries learnings others already captured (e.g. "this API returns HTTP 200 on errors"), and proposes novel findings back — so agents stop rediscovering the same failures in isolation and burning tokens.

## Type & integration
Multi-component **open standard** by **Mozilla.ai** (name from *colloquy* / radio "CQ"). Components: a **CLI** (`cq install --target claude|codex|copilot|cursor|opencode|…`), a **Claude Code plugin** (marketplace), an **MCP server** managing the local knowledge store (queried by the agent; first call asks MCP approval), **Go & Python SDKs** (`cq-sdk`), a **schema** (`cq-schema`), a **team API** for org-wide sharing, a **HITL review UI**, and a **server container** (GHCR / Docker Hub). Idempotent install, `--dry-run`/`--uninstall`. The unit of knowledge is a **"knowledge unit"** added via `propose` or `/cq:reflect`.

## Pricing model
**Open-source, Apache-2.0** (verified at source). Self-hostable (server image provided). No public paid/hosted tier advertised; the "team API" is part of the OSS components.

## LLM cost
**🟢 Built-in** — cq has **no LLM of its own** and **takes no API key**: it is a knowledge store your existing coding agent queries over **MCP**, and proposals/reflection run inside that agent (Claude Code, Codex, Cursor, OpenCode…). No tokens resold. Note the **token *overhead*** it adds (see Notes): a query + injecting returned knowledge into context costs tokens — the net saving depends on hit-rate × quality vs that overhead, and is **not measured**.

## What it's for
Cut the waste of agents repeating each other's mistakes (failed CI, wrong API assumptions) across a team/org. Independently echoed by Andrew Ng ("a Stack Overflow for AI coding agents"). Trust is meant to come from **confirmation-through-use** (multiple agents/codebases confirm or flag stale) rather than authority — an answer to static `CLAUDE.md`/`AGENTS.md` files that drift.

## Notes
- ⚠️ **Early & unproven**: repo created 2026-03, **status 0.x** ("expect breaking changes"), ~1.2k★ — a credible PoC, **no efficacy metrics** (token/error reduction is the value prop yet unquantified).
- ⚠️ **Cost blind spot**: querying the commons before each task **adds** tokens/latency; net savings unproven.
- ⚠️ **Security/quality at scale**: a shared, agent-writable store is a **data-poisoning / prompt-injection vector** — one bad "learning," confirmed by mistaken or colluding agents, propagates. "Confidence/reputation/trust signals" are still largely aspirational.
- ⚠️ **Private-code leakage**: contributing learnings drawn from proprietary codebases into a shared/team commons risks leaking internal detail; scope and redaction are the user's responsibility.
- ⚠️ **Cold-start / network effect**: value grows with participation; an empty commons helps no one.
- Closest in the census: cross-agent persistent memory like [cavemem](cavemem.md) and [graphmind](graphmind.md) — but cq's angle is a **cross-agent open *standard*** for shared learning, not personal/codebase memory. Conceptually overlaps the "instincts"/continuous-learning of ECC, scoped to a commons.

## Source
- Repo: https://github.com/mozilla-ai/cq (Apache-2.0, Go, ~1.2k★) · Proposal: `docs/CQ-Proposal.md` · Blog: https://blog.mozilla.ai/cq-shared-agent-learning/
- Verified via GitHub API (license, stars, dates) + README read directly.

*(verified on 2026-06-30)*
