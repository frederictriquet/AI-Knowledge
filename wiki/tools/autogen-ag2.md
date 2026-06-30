---
tool: "AutoGen / AG2"
title: "AutoGen / AG2"
themes: [multi-agent, frameworks-tooling]
type: "Python conversational multi-agent framework (two lineages + a successor)"
url: https://microsoft.github.io/autogen/
pricing_model: "Open-source (AutoGen MIT, AG2 Apache 2.0)"
llm_cost: "🔑 BYOK — orchestrates, does not bill tokens"
objectives: [production]
family: "General-purpose multi-agent frameworks (for developers)"
eco_icons: "🔓"
llm_cost_icons: "🔑"
summary: "**Conversational** agents (GroupChat). ⚠️ **3 lineages**: AutoGen (Microsoft, MIT, **maintenance mode**) → successor **Microsoft Agent Framework** (GA Apr 2026); **AG2** (community fork, Apache 2.0, active). Choose based on your ecosystem. Concept: [📄 notion](../concepts/autogen-ag2.md)"
---

# AutoGen / AG2

**In one sentence** — Python framework for **conversational** agents (LLM agents that talk to each other and to the human via GroupChat) — but the project has **split into three lineages** that must be untangled before choosing.

> 📄 Detailed concept: [AutoGen/AG2 concept fiche](../concepts/autogen-ag2.md). Here: the state of the project, licenses and cost (product angle).

## ⚠️ Three lineages not to confuse (verified on 2026-06-16)
- **AutoGen (Microsoft)** — now in **maintenance mode** (no new features; last release python-v0.7.5, Sept 2025). PyPI: `autogen-agentchat`/`-core`/`-ext` + `pyautogen`.
- **Microsoft Agent Framework (MAF)** — Microsoft's **official successor** (merging Semantic Kernel + AutoGen), **GA on April 3, 2026** (.NET + Python, MIT, long-term support). This is Microsoft's "production" path.
- **AG2** — the **community fork** by the original creators (Chi Wang, Qingyun Wu), **still active** (v0.13.4, June 2026, "toward v1.0"). PyPI: `ag2` (and the `autogen` alias).

## Pricing model
Everything is open-source: **AutoGen (Microsoft) = MIT** (code); **AG2 = Apache 2.0** (keeps AutoGen's MIT history). No self-service commercial offering; AG2 announces a hosted **AgentOS** platform on a **waitlist** (price/GA not published).

## LLM cost
**🔑 BYOK** for both: neither bundles nor bills LLM usage. Config via env variables / `OAI_CONFIG_LIST` (OpenAI, Azure, Anthropic, Gemini, Mistral, Groq… + local models Ollama/LM Studio/LiteLLM).

## What it's for
Inherited patterns: conversational agents (`ConversableAgent`/`AssistantAgent`), `UserProxyAgent` (human-in-the-loop), and especially **GroupChat** (multiple agents, a manager picks who speaks). The **AutoGen v0.4** rewrite (Jan 2025) introduced an **event-driven/async** architecture in 3 layers (`autogen-core` actor runtime + OTel tracing, `autogen-agentchat` high-level, `autogen-ext`), RoundRobin/Selector/Magentic-One teams, and **AutoGen Studio** (low-code, prototyping only).

## Notes
- **The real risk = fragmentation**: for a new Microsoft project, aim for **MAF** (not legacy AutoGen); to stay close to the original community spirit, **AG2**. The PyPI name confusion (`autogen` = AG2, `pyautogen` = Microsoft) is a trap.
- GitHub stars: microsoft/autogen ~59k (the historical base stayed there), ag2ai/ag2 ~4–5k (few stars followed the fork).
- Vs [LangGraph](langgraph.md) (graph/state) and [CrewAI](crewai.md) (roles): the distinctive axis = **conversational orchestration**.

## Source
github.com/microsoft/autogen (LICENSE-CODE MIT; maintenance-mode discussion) · github.com/ag2ai/ag2 (LICENSE Apache 2.0) · devblogs.microsoft.com (Microsoft Agent Framework 1.0 GA, 2026-04-03). *(verified on 2026-06-16; AG2 AgentOS price not published)*
