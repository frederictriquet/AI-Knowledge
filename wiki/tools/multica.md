---
tool: "Multica"
title: "Multica"
themes: [multi-agent, frameworks-tooling]
type: "\"Managed agents\" platform (coding-agent orchestration)"
url: https://multica.ai/
pricing_model: "Source-available (MODIFIED Apache 2.0 — anti-third-party-service clause, commercial license required to host/embed) + Multica Cloud (no public pricing)"
llm_cost: "No LLM cost of its own (🟢) — drives your existing CLI agents (which carry their own auth); vendor-neutral, code does not pass through Multica's servers"
objectives: [code-generation]
family: "Coding orchestrators & multi-agent systems"
eco_icons: "🔓🔒"
llm_cost_icons: "🟢"
summary: "\"Managed agents\" platform in Go (~37k★) managing coding agents like teammates: task board, queue, reusable skills, multi-runtime dashboard (local + cloud), 12 agents (Claude Code, Codex, Cursor…). Self-host or Multica Cloud (no public pricing). ⚠️ **Modified** Apache 2.0 license (anti-third-party-service clause → not OSI). Code does not pass through their servers. BYO agent"
migrated_from: multica
---

# Multica

**In one sentence** — platform that manages coding agents **like real teammates**: you assign them tasks on a board, they execute, report progress, comment, and accumulate reusable "skills".

## Type & integration
**Open-core platform in Go** (`multica-ai/multica`, ~37k★). Orchestration / project-management layer for agents: task board (enqueue → claim → execute → complete/fail), real-time tracking (WebSocket), library of reusable **skills**, **multi-runtime dashboard** (local daemons + cloud runtimes, auto-detection of available CLIs), unified humans + agents timeline. Vendor-neutral: compatible with **12 agents** — Claude Code, Codex, GitHub Copilot CLI, OpenClaw, OpenCode, Hermes, Gemini, Pi, Cursor Agent, Kimi, Kiro CLI (+ Antigravity). Setup: `multica setup` (connects to Multica Cloud) or `multica setup self-host` (full server via Docker/GHCR).

## Pricing model
⚠️ **Not open-source in the OSI sense**, despite the site's "fully open source". The LICENSE file is a **modified Apache License 2.0** with additional conditions (verified):
- **Anti-third-party-service clause**: prohibition on using the code to provide a **hosted service** to third parties or to **embed** Multica as a component, without a **commercial license** from the publisher.
- (GitHub classifies the license as "Other / NOASSERTION".)

→ **Open-core / source-available** model: self-host allowed, but reselling as a service is reserved. **Multica Cloud** (hosted version) exists — **no public pricing page** (/pricing 404s); a "Start free trial" is highlighted.

## LLM cost
**No LLM cost of its own** 🟢 — Multica **embeds no LLM** and adds no key: it **routes tasks to your existing CLI agents** (Claude Code, Codex, Cursor…), which carry **their own authentication/subscription**. "Code does not pass through Multica's servers". The LLM cost is therefore that of your underlying agents (as with the other 1b orchestrators). No BYOK of Multica's own on the model side.

## What it's for
Industrializing the work of several coding agents as a team: assign issues as you would to colleagues, track progress, have humans + agents collaborate in one place, and reuse acquired skills. Targets dev teams that want to treat agents as managed team members, not as one-off tools.

## Notes
- **Family 1b (coding orchestrators & multi-agent systems)**: close to [Orca](orca.md), [Conductor](conductor.md), [Superset (superset-sh)](superset.md) (driving several agents), but with a **"project management / teammates"** angle (board, assignment, skills) rather than pure parallel worktrees. Distinct from [MindFlight Orchestrator (MFO)](mindflight-orchestrator.md) (business processes, not coding).
- Open-core license comparable to **Superset**'s (ELv2) / **Supacode**'s (FSL): "open but not resellable as a service".
- To dig into: real Multica Cloud price (not public), scope of the free trial, what the commercial license covers.

## Source
- Site: https://multica.ai/ · docs: https://multica.ai/docs · repo: https://github.com/multica-ai/multica (Go, ~37k★)
- Verified LICENSE: "modified version of the Apache License 2.0" + anti-third-party-service clause (raw GitHub)

*(verified on 2026-06-15 — official site + GitHub API + LICENSE file + README)*

<!-- direct neighbor: [Vibe Kanban](vibe-kanban.md) (agent-orchestration kanban, Apache-2.0) -->
