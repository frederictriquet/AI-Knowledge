---
tool: "Pydantic AI"
title: "Pydantic AI"
themes: [frameworks-tooling]
type: "Type-safe Python agent framework"
url: https://ai.pydantic.dev/
pricing_model: "Open-source (MIT) + Pydantic Logfire (observability, freemium)"
llm_cost: "🔑 BYOK, model-agnostic — does not bill tokens"
objectives: [production]
family: "General-purpose multi-agent frameworks (for developers)"
eco_icons: "🔓🎁"
llm_cost_icons: "🔑"
summary: "**Type-safe** (MIT) by the Pydantic team: validated structured outputs, \"FastAPI feeling\", DI, MCP/A2A. Model-agnostic. Observability via **Logfire** (freemium: Team $49 → Growth $249). Mature (>v1.0)"
migrated_from: pydantic-ai
---

# Pydantic AI

**In one sentence** — **Type-safe** Python agent framework by the Pydantic team: validated structured outputs, "that FastAPI feeling" ergonomics (errors moved from runtime to authoring time), dependency injection, native observability via Logfire.

## Type & integration
Open-source Python framework, built by the creators of **Pydantic** (the validation brick used by the OpenAI/Anthropic/Google ADK SDKs, LangChain, LlamaIndex, CrewAI, Instructor…). Confirmed maturity: **> v1.0** (v1.107, June 2026, ~17.8k★). **MCP** support, **A2A** interoperability, durable execution.

## Pricing model
- **Framework: open-source MIT**, free.
- **Pydantic Logfire** (OTel observability, optional but natively integrated) = the **freemium** commercial offering: **Personal** free (10M spans, 30 days) → **Team** $49/month (+$2/M) → **Growth** $249/month → **Enterprise** by quote (self-host, SSO, SLA).

## LLM cost
**🔑 BYOK and model-agnostic**: "supports virtually every model and provider" (OpenAI, Anthropic, Gemini, DeepSeek, Mistral, Cohere, Groq, Ollama, Bedrock, OpenRouter, LiteLLM…). The MIT framework **bills no tokens**; you pay the model provider.

## What it's for
The choice when **output reliability** is paramount: Pydantic validation at runtime (typed, streamed structured outputs), type-safe DI to customize agents, and cost/perf tracking via Logfire/OpenTelemetry. Strong credibility (Pydantic is already under the hood of most AI SDKs).

## Notes
- **Recent but already mature** project (>1.0).
- Positioning (third-party sources): vs [LangGraph](langgraph.md) (complex routing/state, more boilerplate), vs [CrewAI](crewai.md) (multi-agent/roles), vs [OpenAI Agents SDK](openai-agents-sdk.md) (lightweight) — Pydantic AI bets on **typing and validation**.
- Often combined with other frameworks rather than opposed to them.

## Source
https://ai.pydantic.dev/ · github.com/pydantic/pydantic-ai (LICENSE MIT, providers, v1.107) · https://pydantic.dev/pricing (Logfire). *(verified on 2026-06-16)*
