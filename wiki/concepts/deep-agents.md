---
title: "Deep Agents (pattern)"
type: "Concept"
theme: agent-fundamentals
level: 🟡
source_url: https://blog.langchain.com/deep-agents/
objectives: [code-generation]
---

# Deep Agents (pattern)

**In one sentence** — an agent architecture pattern for **long-horizon** tasks: instead of a simple "think → call a tool → observe" loop, it combines **explicit planning + sub-agents with isolated context + a file system as external memory + a detailed system prompt** to go the distance without saturating the context.

## The idea
A "flat" ReAct loop degrades on long tasks: the context fills up ("context rot"), the plan gets lost, details fade. The *deep agents* pattern — articulated by LangChain, **inspired by Claude Code and Deep Research (Anthropic)** — fixes this with **four pillars**:

1. **Detailed system prompt** — rich instructions (when to plan, when to delegate, how to use files), often with examples. It is the "brain" of the harness.
2. **Planning tool** — a to-do tool (often nearly a no-op, e.g. `write_todos`) that **forces the agent to make its plan explicit and re-anchor it** in the recent context, against drift.
3. **Sub-agents with isolated context** — delegating a sub-task to an agent **with a clean context** ("context quarantine"): the detail stays with the sub-agent, only the result bubbles up → the main agent's context stays **thin**.
4. **File system (external memory)** — reading/writing/editing files to **offload** context and **persist** state across steps/sessions, instead of keeping everything in the window.

The net effect: the orchestrator's context stays **lean**, memory lives **outside** (files), heavy work is **delegated** to disposable sub-agents, and the plan is **re-asserted** regularly.

## Tradeoff / when to use it
- **For**: **multi-step / long** tasks (deep research, large refactors, business workflows) where a simple loop collapses.
- **Against**: **token and latency overhead** (planning, sub-agent spawns, file I/O) → **disproportionate** for a short task, where a direct ReAct/function-calling suffices. Requires a **capable model** (good tool-calling + instruction following) and adds **orchestration complexity**.
- Situate it relative to [react](react.md) (the base loop), the [canonical agent architecture](canonical-agent-architecture.md) and the [multi-agent structures](multi-agent-structures.md): *deep agents* is a **harness recipe** that assembles planning, delegation and external memory — not a new algorithm.

## Primary source
LangChain, *Deep Agents* — articulation of the pattern (planning tool, sub-agents, virtual file system, detailed system prompt). Blog: https://blog.langchain.com/deep-agents/ ; docs: https://docs.langchain.com/oss/python/deepagents/overview *(verified — HTTP 200, 2026-06-17)*. Cited inspirations: Claude Code and Deep Research (Anthropic).

## See also
- [react](react.md) · [react-vs-function-calling](react-vs-function-calling.md) — the base loop this pattern goes beyond
- [agent-architecture-canonique](canonical-agent-architecture.md) · [structures-multi-agents](multi-agent-structures.md) · [orchestration-types](orchestration-types.md) — delegation / sub-agents
- [planification-goal-state-action](goal-state-action-planning.md) · [self-reflection-agents](self-reflection-agents.md) — the planning pillar
- [memoire-court-long-terme](short-vs-long-term-memory.md) · [voyager-skill-library](voyager-skill-library.md) — external memory & skills
- Product implementation: `deepagents` (LangChain) → [tool note](../tools/deepagents.md)
