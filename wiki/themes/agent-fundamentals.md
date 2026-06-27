---
type: index
title: "Theme — Agent fundamentals"
theme: agent-fundamentals
---

# 🧱 Agent fundamentals

> ⚙️ **Generated file** by `tools/build_index.py` — do not edit by hand.

_What an agent is, its components and its structural limits._

## Concepts (14)

### 🔴 Substance / core
- **[ACI: designing the agent-computer interface](../concepts/aci-agent-computer-interface.md)** — give as much care to tool definitions (names, descriptions, formats) as to prompts: the agent-computer interface (ACI) is, for an agent, what the human-computer interface is for a person.
- **[Augmented language models (Weng's taxonomy)](../concepts/augmented-language-models.md)** — the sourced genealogy of tool-using agents: before packaged "function calling," three families of techniques (retrieval, code execution, API calls) were already augmenting a frozen LLM through the prompt alone.
- **[Function-calling error taxonomy](../concepts/function-calling-error-taxonomy.md)** — a concrete grid for evaluating tool-calling: five errors detectable by deterministic rules, plus two semantic checks delegated to an LLM judge.
- **[The 5 composable workflow patterns (Anthropic)](../concepts/workflow-patterns.md)** — a catalog of composable patterns, from simplest to most complex, to assemble yourself rather than delegate to a framework.
- **[Workflows vs agents: Anthropic's architectural distinction](../concepts/workflows-vs-agents.md)** — distinguish **workflows** (LLMs and tools orchestrated by predefined code paths) from **agents** (the LLM dynamically directs its own process), instead of calling everything "agentic".

### 🟡 Tradeoff / intermediate
- **[BDI architecture (Belief-Desire-Intention)](../concepts/bdi.md)** — a breakdown of an agent's reasoning into three registers (what it knows, what it wants, what it decides to do), predating LLMs.
- **[Deep Agents (pattern)](../concepts/deep-agents.md)** — an agent architecture pattern for **long-horizon** tasks: instead of a simple "think → call a tool → observe" loop, it combines **explicit planning + sub-agents with isolated context + a file system as external memory + a detailed system prompt** to go the distance without saturating the context.
- **[Structural limitations of LLM agents (per Weng)](../concepts/agent-limitations-weng.md)** — the three common limitations Weng identifies after surveying agent demonstrators: finite context, brittle long-horizon planning, and an unreliable natural-language interface.
- **[Vertical / horizontal / hybrid architectures](../concepts/vertical-horizontal-hybrid-architectures.md)** — the three topologies of a multi-agent system: a centralized leader, equal peers, or a mix of both depending on the phase.

### 🟢 Overview / introductory
- **[AutoGPT](../concepts/autogpt.md)** — the 2023 demonstrator that decomposes a high-level goal into subtasks and runs a create/prioritize/execute loop with vector memory; mostly of historical value.
- **[BabyAGI](../concepts/babyagi.md)** — the minimal 2023 loop (Yohei Nakajima) of three agents — execution, creation, prioritization — backed by a vector memory; an "educational sandbox" more than a production tool.
- **[Conditional & heuristic logic](../concepts/conditional-heuristic-logic.md)** — hard-wired reasoning: if-then rules and utility scores/functions coded into the decision loop, with no learning.
- **[Learning agent (AIMA model)](../concepts/learning-agent.md)** — an agent that decomposes into four internal roles so it can loop over its own mistakes and improve over time.
- **[Taxonomy of the 5 agent types](../concepts/five-agent-types-taxonomy.md)** — the classic scale of agent sophistication, from hard-wired `if/then` to an agent that improves through feedback.

## Tools (1)

- **[deepagents (Deep Agents)](../tools/deepagents.md)** — _Python library (+ JS/TS) — agent harness_
