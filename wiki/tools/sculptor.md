---
tool: "Sculptor"
title: "Sculptor"
themes: [multi-agent, frameworks-tooling]
type: "Mac desktop app — agent orchestrator"
url: https://imbue.com/sculptor/
pricing_model: "Proprietary — free in beta"
llm_cost: "Built-in (BYO Anthropic: API key or Claude Pro/Max subscription)"
objectives: [code-generation]
family: "Coding orchestrators & multi-agent systems"
eco_icons: "🔒"
llm_cost_icons: "🟢🔑"
summary: "Mac app (Imbue) orchestrating **Claude Code agents in isolated Docker containers** + Pairing Mode (instant local testing) + dev containers (startup in seconds). **Free in beta**, proprietary. BYO Anthropic (API key or Claude Pro/Max subscription)"
---

# Sculptor

**In one sentence** — the "missing UI for coding agents" (Imbue): a Mac app that launches **several Claude Code agents in parallel in isolated Docker containers**, with instant preview of changes.

## Type & integration
macOS desktop app. Each agent runs in an **isolated container** (it can install packages and execute code without risk to your machine). **Pairing Mode**: instantly switch to an agent's environment to test its changes locally. Supports **dev containers** (dependencies pre-installed in the image → agent startup in seconds instead of minutes). Runs entirely locally; you control what is sent back to Imbue.

## Pricing model
Proprietary, **free during the beta**. No public pricing at this stage.

## LLM cost
**🟢🔑 BYO Anthropic**: requires Anthropic access — either your **API key** (🔑) or your **Claude Pro/Max** subscription (🟢). Sculptor adds no LLM cost of its own.

## What it's for
Running and comparing several coding agents **safely** (container isolation), with a fast round-trip to test their results. It stands out for Docker isolation and accelerated startup.

## Notes
- Built by **Imbue** (an AI research lab); beta → maturity and business model to watch.
- macOS only; same family as Conductor / Crystal (desktop orchestrators).
- ⚠️ macOS only, beta with no pricing; running N agents in parallel **multiplies the real usage** of your Anthropic subscription/key; weigh it against Conductor (free, more mature) before any commitment.

## Source
https://imbue.com/sculptor/ · https://imbue.com/blog/sculptor-announce · https://imbue.com/blog/containers. *(verified on 2026-06-17; free in beta, future pricing not published)*
