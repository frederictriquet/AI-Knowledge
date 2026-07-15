---
type: index
title: "Theme — Multi-agent"
theme: multi-agent
---

# 👥 Multi-agent

> ⚙️ **Generated file** by `tools/build_index.py` — do not edit by hand.

_Orchestrating and structuring multiple agents._

## Concepts (9)

### 🔴 Substance / core
- **[DroidSpeak](../concepts/droidspeak.md)** — instead of having two LLMs converse in text, the KV cache is shared directly between them to speed up inter-agent communication, with an accuracy loss reported as minimal.
- **[MacNet: scaling multi-agent collaboration](../concepts/macnet.md)** — the extension of ChatDev that structures more than a thousand agents into an acyclic graph (DAG) and has them reason in topological order, with a law governing how quality grows with the number of agents.
- **[MetaGPT: structured communication + executable feedback](../concepts/metagpt-pattern.md)** — a multi-agent framework that simulates a software company, where agents exchange schematized documents (PRDs, diagrams) rather than free-form dialogue, with the engineer looping on its own tests.
- **[Mixture-of-Agents (MoA)](../concepts/mixture-of-agents.md)** — stack **multiple LLMs in layers**: each layer of agents receives and aggregates the previous layer's responses, improving quality beyond the best single model.
- **[Multi-agent debate / Society of Mind](../concepts/society-of-mind-debate.md)** — have **several LLM instances debate**: each proposes an answer, critiques the others over several rounds, until converging on a more factual answer.

### 🟡 Tradeoff / intermediate
- **[Centralized vs decentralized networks](../concepts/centralized-decentralized-networks.md)** — either a central unit holds the global knowledge and links all the agents, or each one only talks to its neighbors.
- **[Collaboration strategies: rules / roles / models](../concepts/collaboration-strategies.md)** — three ways to make agents cooperate: scripted, by role assignment, or by probabilistic reasoning under uncertainty.
- **[Multi-agent structures: hierarchical / holonic / coalition / team](../concepts/multi-agent-structures.md)** — four ways to organize agents: a chain of command, a whole-and-part arrangement, a temporary alliance, or an interdependent team.
- **[Types of AI agent orchestration](../concepts/orchestration-types.md)** — four ways to distribute decision-making across agents: a single leader, a leaderless collective, hierarchical layers, or organizations that collaborate without sharing data.

## Tools (20)

- **[AutoGen / AG2](../tools/autogen-ag2.md)** — _Python conversational multi-agent framework (two lineages + a successor)_
- **[Conductor](../tools/conductor.md)** — _Mac desktop app (coding-agent orchestrator)_
- **[CrewAI](../tools/crewai.md)** — _Framework (Python library) + cloud platform_
- **[Crystal](../tools/crystal.md)** — _Desktop application (Electron) — agent orchestrator_
- **[LangGraph](../tools/langgraph.md)** — _Python + JS/TS library (stateful agent graphs) + deployment platform_
- **[Liza](../tools/liza.md)** — _CLI (Go) — multi-agent coding system_
- **[MindFlight Orchestrator (MFO)](../tools/mindflight-orchestrator.md)** — _Platform (AI agent orchestration / enterprise automation)_
- **[Multica](../tools/multica.md)** — _\"Managed agents\" platform (coding-agent orchestration)_
- **[oh-my-pi (omp)](../tools/oh-my-pi.md)** — _CLI / TUI (terminal coding agent)_
- **[OpenAI Agents SDK](../tools/openai-agents-sdk.md)** — _Python + TypeScript SDK (lightweight agents)_
- **[Orca](../tools/orca.md)** — _Desktop app (Mac/Win/Linux) + mobile — Agent Development Environment (ADE)_
- **[Paperclip](../tools/paperclip.md)** — _Open-source AI-agent orchestration and governance platform (\"zero-human companies\")_
- **[Pheromind](../tools/pheromind.md)** — _Multi-agent orchestration framework (swarm)_
- **[Ruflo](../tools/ruflo.md)** — _Multi-agent orchestration meta-harness / framework for Claude (open source, npm)_
- **[Sculptor](../tools/sculptor.md)** — _Mac desktop app — agent orchestrator_
- **[Sim (Sim Studio)](../tools/sim.md)** — _Visual agent-workflow builder — open-source + Cloud_
- **[Supacode](../tools/supacode.md)** — _Native macOS desktop application (coding-agent orchestrator)_
- **[Superset (superset-sh)](../tools/superset.md)** — _Desktop application (coding-agent orchestrator)_
- **[TRIP-workflow](../tools/trip-workflow.md)** — _Skills pack / dev workflow (SKILL.md) for AI coding agents_
- **[Vibe Kanban](../tools/vibe-kanban.md)** — _Kanban platform / coding-agent orchestration (web)_
