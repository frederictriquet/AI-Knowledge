---
tool: "Caveman"
title: "Caveman"
themes: [efficiency-cost]
type: "Skill (Claude Code + ~30 agents)"
url: https://github.com/juliusbrussee/caveman
pricing_model: "Open-source (MIT), free (sponsorships accepted)"
llm_cost: "Built-in — no LLM of its own; reduces the agent's token consumption"
objectives: [cost-control]
family: "Token & agent-behavior optimization"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Open-source skill (Claude Code + ~30 agents) that cuts ~65% of output tokens by making the model 'talk like a caveman'; code/paths preserved, lite/full/ultra/wenyan levels"
---

# Caveman

**In one sentence** — open-source skill that forces the agent to answer "like a caveman" (fragments, zero frills) to cut ~65% of output tokens, without losing technical accuracy. *"Why use many token when few token do trick."* 🪨

## Type & integration
**Skill** for Claude Code (auto-activated each session via a flag file), compatible with ~30 other agents (Codex, Gemini, Cursor, Windsurf, Cline, Copilot…). Triggered by `/caveman` or "talk like caveman", stopped by "normal mode". Written mostly in JavaScript (+ Python, PowerShell, Shell).

## Pricing model
**Open-source, MIT license**, "free forever". The author (Julius Brussee) accepts **sponsorships**, but the tool stays free.

## LLM cost
**Built-in** 🟢 — Caveman has **no LLM of its own** and adds no cost: it's a style instruction applied to the agent's LLM (Claude Code, etc.). Its effect is the opposite of a cost: it **reduces** output tokens (~65%), and also compresses memory files (~46% on average) → direct savings on the agent's bill.

A counterintuitive bonus cited: a March 2026 article — **vague source, not cross-checked** — *claims* that constraining large models to brief answers *improved* accuracy by 26 points on some benchmarks → conciseness might help reasoning. To take with caution.

## What it's for
Lower an agent's cost and latency by stripping the verbiage from its answers, while keeping **code and paths preserved byte-for-byte**. Several compression levels: **lite, full, ultra, wenyan**. Side functions: commit-message generation, PR-review compression, token-usage statistics.

## Notes
- Same "token reduction" family as [CodeGraph](codegraph.md) / [Polaris (polarismcp.com)](polaris.md) / [Graphify](graphify.md), but from a different angle: here you compress the model's **output** (style), not the **input**/context.
- Same author's ecosystem: [Cavekit](cavekit.md) (Claude Code plugin, spec-driven development), [Cavemem](cavemem.md) (persistent cross-agent memory, compressed, local). "Caveman" encoding is the common thread across all three.
- The "wenyan" level = classical-Chinese-style compression, very aggressive.
- ⚠️ The "caveman" output degrades readability for human review and team communication; the "~65%" gain is self-declared, unverified.

## Source
- Repo: https://github.com/juliusbrussee/caveman
- Releases: https://github.com/JuliusBrussee/caveman/releases

*(verified on 2026-06-15 — GitHub README + web search)*
