---
tool: "RTK (Rust Token Killer)"
title: "RTK (Rust Token Killer)"
themes: [efficiency-cost]
type: "CLI (proxy)"
url: https://www.rtk-ai.app/
pricing_model: "Open-source (Apache 2.0), free; RTK Cloud (teams) upcoming, $15/dev/month"
llm_cost: "No LLM inference — compresses command output before the context (saves on the bill)"
objectives: [cost-control]
family: "Token & agent-behavior optimization"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Open-source CLI proxy (single Rust binary) that compresses terminal command output before the LLM context (60–90% fewer tokens); PreToolUse hook in Claude Code, no key or telemetry. RTK Cloud (teams) upcoming, $15/dev/month"
migrated_from: rtk
---

# RTK (Rust Token Killer)

**In one sentence** — Rust CLI proxy that intercepts and compresses terminal command output *before* it enters the LLM context, to remove noise and save 60–90% of tokens. *"Your AI agent is drowning in CLI noise. Fix it."*

## Type & integration
**Single Rust binary, zero dependency, zero config** — a transparent proxy that sits between the shell and the AI assistant. Covers 100+ common commands (git, cargo, npm, ls, cat, find…). **Claude Code** integration via `rtk init --global`: installs a **PreToolUse hook** that automatically rewrites Bash commands into `rtk` equivalents (transparent, 0 token overhead). Also compatible with Cursor, Aider, Copilot…

Four strategies: **filtering, grouping, truncation, deduplication** — prunes the repetitive (warnings, formatting, padding) while preserving the essential (errors, failures, diffs). Overhead < 10 ms/command.

## Pricing model
- **RTK (core)**: **open-source Apache 2.0**, fully free, no usage limit, no API key, no telemetry, no account.
- **RTK Cloud** (waitlist): team analytics (centralized token tracking) starting at **$15/dev/month**.

## LLM cost
**No own LLM inference** 🟢. RTK runs no model: it **compresses existing command output**. Effect = direct savings on the agent's LLM bill (you keep your own keys on your AI tools, BYOK). Measured results: ~89% noise removed across 2,900+ real commands (cargo test 91.8%, git status 80.8%, find 78.3%); a 30-min Claude Code session goes from ~118,000 to ~23,900 tokens (~80%).

## What it's for
Extend agent sessions and reduce costs by removing the CLI-output noise that needlessly fills the context window. Particularly relevant for those paying for LLMs by usage.

## Notes
- **"Token optimization" family**: the most direct analog of [Tokenade](tokenade.md) (which also trims command output), but RTK is **open-source/free** vs Tokenade proprietary/freemium, and purely focused on **shell command output**. See also [Caveman](caveman.md) (model output) and [Ponytail](ponytail.md) (code scope).
- 🛠️ **Used in the user's environment**: configured globally via a Claude Code hook (cf. global `RTK.md`) — all shell commands are transparently rewritten to `rtk <cmd>`.
- Meta-commands: `rtk gain` (savings analytics), `rtk discover`, `rtk proxy <cmd>` (raw execution without filtering).

## Source
- Official site: https://www.rtk-ai.app/
- Repo: https://github.com/rtk-ai/rtk · Docs: https://mintlify.com/explore/rtk-ai/rtk

*(verified on 2026-06-15 — official landing page + GitHub + web search)*
