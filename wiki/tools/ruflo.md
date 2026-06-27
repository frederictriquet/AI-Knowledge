---
tool: "Ruflo"
title: "Ruflo"
themes: [multi-agent]
type: "Multi-agent orchestration meta-harness / framework for Claude (open source, npm)"
url: https://github.com/ruvnet/ruflo
pricing_model: "Open source MIT, free — no subscription; you bring your own LLM keys (BYOK)"
llm_cost: "🟢🔑 — Claude Code plugin mode: via your Claude Code (no key, 🟢); autonomous multi-provider mode: BYOK (Claude/GPT/Gemini/Ollama via OpenRouter or OpenAI-compatible endpoint, 🔑)"
objectives: [code-generation]
family: "Coding orchestrators & multi-agent systems"
eco_icons: "🔓"
llm_cost_icons: "🟢🔑"
summary: "Open-source multi-agent meta-harness (MIT, ex-Claude Flow) that turns Claude Code into a swarm: 60–100+ agents, ~215 MCP tools, ML routing, HNSW memory. 🟢 via Claude Code (plugin mode, no key) or 🔑 BYOK multi-provider (OpenRouter/Ollama…) in autonomous mode; bets on *breadth* (vs Liza's *depth*)"
migrated_from: ruflo
---

# Ruflo

**In one sentence** — Ruflo (formerly *Claude Flow*, by ruvnet) is an open-source meta-harness that turns Claude Code into a multi-agent swarm: 60-100+ types of specialized agents, ~210-215 MCP tools and machine-learning-driven task routing.

## Type & integration
Multi-agent orchestration framework / meta-harness for Claude, distributed as an npm package (`ruflo`). Three integration modes:
- **CLI**: `npx ruflo@latest init wizard`
- **Claude Code plugin**: via the marketplace (`/plugin install ruflo-core@ruflo`)
- **MCP server**: `npx ruflo@latest mcp start`

It relies on Claude Code's hooks for pre/post-execution checks and orchestrates "swarms" of agents (coder, tester, architect, security-architect, DevOps, data analyst, etc.). Persistent indexed memory (HNSW), a "ReasoningBank" that searches past patterns by similarity (trigrams/Jaccard), and task routing to the agents with the best history (Q-learning / "SONA" neural routing announced at ~89% accuracy).

## Pricing model
Free software under **MIT license**, free, on GitHub (`ruvnet/ruflo`, ~59.6k stars at the time of verification). No subscription or proprietary API. There is no direct revenue/commercial model: it is a community open-source project.

## LLM cost
**🟢🔑 — two modes** (Ruflo does not resell an LLM; verified in the README on 2026-06-16):
- **Claude Code plugin mode** (`/plugin install`, "after init, just use Claude Code normally") → runs **via your Claude Code**, **no key** (🟢, your existing subscription/login).
- **Autonomous / multi-provider mode** → **BYOK** (🔑): you plug in your own keys (Anthropic, OpenAI, Gemini, Cohere, local Ollama) or an OpenAI-compatible endpoint via OpenRouter.

The "~75% savings" argument rests on **multi-provider routing** + adaptive model selection (cheaper models for simple tasks), not on included pricing. (Hosted demo flo.ruv.io: no key or account.)

## What it's for
Build and drive autonomous multi-agent systems on top of Claude Code (or Codex): coordinated software development (coding, testing, security, architecture), autonomous workflows, RAG integration, adaptive memory and swarm self-learning. Target: maximize **breadth** — many specialized agents and tools, with ML routing that dispatches each task to the best-performing agent.

## Notes
- Architectural bet opposite to [Liza](liza.md): Ruflo optimizes **breadth** (60+ agent types, ~215 MCP tools, ML routing, swarm topologies, byzantine consensus, HNSW indexing); Liza optimizes **depth** (behavioral simplicity, those infra concepts having been deliberately discarded by Liza).
- Figures to clarify: the docs oscillate between "60+" and "100+" agents, and "210+" vs "215+" MCP tools — consistent orders of magnitude, exact counts vary by version.
- Former name: **Claude Flow**. Renamed Ruflo. To watch for reference continuity.
- Marketing claims (75% savings, 89% routing accuracy) to be taken cautiously: not independently verified, depend on usage context.

## Source
- https://github.com/ruvnet/ruflo (official repo, MIT, tagline "leading agent meta-harness for Claude") *(verified on 2026-06-15)*
- https://github.com/ruvnet/ruflo/wiki — Wiki (agents, configuration) *(verified on 2026-06-15)*
- https://deepwiki.com/ruvnet/ruflo/6.1-agent-types-and-configuration *(verified on 2026-06-15)*
- "Liza" competitive comparison: https://raw.githubusercontent.com/liza-mas/liza/main/specs/architecture/competition-survey/mas-survey.md *(verified on 2026-06-15)*
