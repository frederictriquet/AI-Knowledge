---
tool: "Vibe Kanban"
title: "Vibe Kanban"
themes: [multi-agent, frameworks-tooling]
type: "Kanban platform / coding-agent orchestration (web)"
url: https://www.vibekanban.com/
pricing_model: "Open-source (Apache-2.0, verified), free — commercial product being sunset, becoming community-run. Vendor: Bloop AI Limited"
llm_cost: "No LLM cost of its own (🟢) — BYO agent; you only pay the underlying AI services (Claude Code, Codex…)"
objectives: [code-generation]
family: "Coding orchestrators & multi-agent systems"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Orchestration kanban (Bloop AI, **Apache-2.0**, ~27k★): planning→progress→review→done board, parallel execution in git worktrees, integrated browser; 10+ agents (Claude Code, Codex, Gemini, OpenCode, Cursor, Aider…). Free, BYO agent. ⚠️ Commercial product being *sunset* → now community open-source"
migrated_from: vibe-kanban
---

# Vibe Kanban

**In one sentence** — a Kanban board that orchestrates AI coding agents: you plan tasks, hand them to agents that work in parallel (each in its own git worktree), then review and merge — the human moves to a planning/review role.

## Type & integration
**Web orchestration platform** by **Bloop AI Limited** (repo `BloopAI/vibe-kanban`, ~27k★). Column workflow: **planning → in progress → in review → done**. Features: **isolated parallel execution** (each task in its own **git worktree**, no interference with the main branch), code review with comments, testing changes via an **integrated browser**. Orchestrates many executors: **Claude Code, Codex/ChatGPT, Gemini, OpenCode, Cursor, Amp, Aider, Copilot, Windsurf**… Traction: ~30,000 active users, ~100,000 PRs created.

## Pricing model
**Open-source, Apache-2.0 license** (verified via the GitHub API — a true OSI license, unlike [Multica](multica.md) under a *modified* Apache). **Free**. ⚠️ **Status**: Bloop AI is **sunsetting the commercial product**; the project **continues as open-source, community-maintained**. Watch for longevity (post-sunset maintenance pace).

## LLM cost
**No LLM cost of its own** 🟢 — Vibe Kanban is an orchestrator: you **plug in your own agent** (Claude Code, Codex…) and **pay only the underlying AI services** you use. Vibe Kanban itself is free and adds no model cost. Like the other 1b orchestrators, the LLM cost = that of your agents/subscriptions.

## What it's for
Reorganizing the dev cycle around parallel agents: planning tasks, launching several agents simultaneously in isolation, tracking/reviewing/merging from a single board. For developers who want to supervise a "team" of agents rather than drive a single agent at a time.

## Notes
- **Family 1b (coding orchestrators & multi-agent systems)**: very close to [Multica](multica.md) (board + teammate-agents), [Orca](orca.md), [Conductor](conductor.md), [Superset (superset-sh)](superset.md) — parallel execution in git worktrees. Vibe Kanban stands out for its **true Apache-2.0 license** (vs the open-core/source-available of Multica/Superset/Supacode) and its **integrated browser** for testing.
- ⚠️ **Commercial sunsetting**: the future rests on the community → check repo activity before committing to it in production.
- The "coding-agent orchestrators" sub-cluster is very crowded (Superset, Conductor, Supacode, Orca, Multica, Vibe Kanban) — a market in strong ferment and consolidation.

## Source
- Site: https://www.vibekanban.com/ · repo: https://github.com/BloopAI/vibe-kanban (Apache-2.0, ~27k★, verified via GitHub API)

*(verified on 2026-06-15 — official site + GitHub API [Apache-2.0 license] + web search)*
