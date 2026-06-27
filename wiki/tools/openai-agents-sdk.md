---
tool: "OpenAI Agents SDK"
title: "OpenAI Agents SDK"
themes: [multi-agent, frameworks-tooling]
type: "Python + TypeScript SDK (lightweight agents)"
url: https://openai.github.io/openai-agents-python/
pricing_model: "Open-source (MIT) — free"
llm_cost: "🔑 BYOK — free; you pay the API of the model used"
objectives: [production]
family: "General-purpose multi-agent frameworks (for developers)"
eco_icons: "🔓"
llm_cost_icons: "🔑"
summary: "**Minimalist** (MIT): Agents, Handoffs, Guardrails, Sessions + free tracing. Production successor to **Swarm**. Provider-agnostic (100+ LLMs via LiteLLM). Pre-1.0. Good lightweight entry point"
migrated_from: openai-agents-sdk
---

# OpenAI Agents SDK

**In one sentence** — **minimalist** agent framework from OpenAI (few abstractions: Agents, Handoffs, Guardrails, Sessions + built-in tracing), the **production successor** to the Swarm experiment — and, despite its name, **provider-agnostic** (100+ models).

> 📄 Related concept: [Swarm](../concepts/openai-swarm.md), the deprecated experimental predecessor.

## Type & integration
**Python SDK** (≥ 3.10, `openai-agents`) **and TypeScript/JS** (`@openai/agents`). Still **pre-1.0** (Python v0.17.x, API subject to change). Primitives: **Agents** (LLM + instructions + tools), **Handoffs** (delegation between agents / agents-as-tools), **Guardrails** (I/O validation), **Sessions** (memory/context), + human-in-the-loop and realtime.

## Pricing model
**Open-source MIT**, free. **Provider-agnostic** confirmed verbatim: supports the OpenAI Responses & Chat Completions APIs **+ 100+ other LLMs** via the **LiteLLM** extension (`openai-agents[litellm]`, marked "beta/best-effort").

## LLM cost
**🔑 BYOK**: the SDK is free; you pay the API of the model used (OpenAI or other). **Free OpenAI tracing** enabled by default — documented trick: an OpenAI key enables free tracing in the OpenAI dashboard **even with non-OpenAI models**. Disableable (`OPENAI_AGENTS_DISABLE_TRACING=1`).

## What it's for
The "**lightweight and readable**" choice when you want to compose a few agents without the machinery of a large framework. Built-in tracing for debug/eval. Good entry point, especially if you're already in the OpenAI ecosystem.

## Notes
- **Light lock-in**: the default tracing pushes toward the OpenAI dashboard (disableable; third-party integrations — Langfuse, AgentOps…).
- Pre-1.0: moving API; multi-model via LiteLLM in beta.
- Vs [LangGraph](langgraph.md) (graph/state, more control) and [AutoGen/AG2](autogen-ag2.md)/[CrewAI](crewai.md): "minimalist" positioning (third-party appraisal, no official OpenAI comparison).

## Source
https://openai.github.io/openai-agents-python/ (+ /tracing, /models) · github.com/openai/openai-agents-python (LICENSE MIT) · github.com/openai/swarm (deprecated → Agents SDK). *(verified on 2026-06-16)*
