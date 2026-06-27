---
type: index
title: "Theme — Multi-agent"
theme: multi-agent
---

# 👥 Multi-agent

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

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

## Tools (0)

- _(aucun)_
