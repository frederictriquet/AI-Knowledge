---
tool: "LangGraph"
title: "LangGraph"
themes: [multi-agent, frameworks-tooling]
type: "Python + JS/TS library (stateful agent graphs) + deployment platform"
url: https://www.langchain.com/langgraph
pricing_model: "Open-source (MIT) + paid managed platform (LangSmith Deployment)"
llm_cost: "🔑 BYOK — orchestrates, does not bill tokens"
objectives: [production]
family: "General-purpose multi-agent frameworks (for developers)"
eco_icons: "🔓🎁💳"
llm_cost_icons: "🔑"
summary: "**Low-level orchestration** (LangChain Inc.), MIT: graphs with cycles, persistence/checkpoints, human-in-the-loop, durable execution. Fine-grained flow control. Managed platform (LangSmith Deployment): Developer $0 → Plus $39/seat → Enterprise. Concept: [📄 notion](../concepts/langgraph.md)"
migrated_from: langgraph
---

# LangGraph

**In one sentence** — **low-level** orchestration framework (LangChain Inc.) for *stateful* agents: graphs with cycles, persistence/checkpoints, human-in-the-loop and durable execution — fine-grained flow control where high-level frameworks abstract it away.

> 📄 Detailed concept: [LangGraph concept note](../concepts/langgraph.md). This note covers the product angle (license, pricing, LLM cost).

## Type & integration
Open-source **Python** (`langgraph`) **and JS/TS** (`@langchain/langgraph`) library. Usable **without LangChain** (but LangChain v1 agents are built on it). `StateGraph` (nodes = logic, edges = routing, conditional edges, cycles), checkpointers (short-term memory, recovery after failure, time-travel), stores (long-term memory), streaming. + managed **LangGraph Platform**, renamed **LangSmith Deployment** (Oct. 2025), to deploy/run agents.

## Pricing model
- **Library: open-source MIT**, free, usable on its own.
- **Managed platform** (billed via the LangSmith plans): **Developer** $0/seat (1 seat, 5k traces/month) → **Plus** $39/seat/month (10k traces) → **Enterprise** on quote (only one for full hybrid/self-hosted VPC). Usage-based: runs $0.005/run, prod uptime $0.0036/min, traces $2.50/1k. Self-hostable Agent Server (Docker/K8s + Postgres + Redis), basic self-host option free (Developer plan).

## LLM cost
**🔑 BYOK**, provider-agnostic (~25 providers via `init_chat_model`: OpenAI, Anthropic, Google, Bedrock, Mistral, Groq, Ollama…). Calls go directly to the provider's API, which bills your key — LangGraph **does not resell tokens** (implied by the architecture, not stated verbatim).

## What it's for
The choice when you need **fine-grained control**: cycles (essential to agentic architectures, vs DAGs), explicit state, persistence and recovery, mid-run human validation. First released Jan. 2024; advertised adoption Klarna, Replit, Elastic.

## Notes
- Vs **LangChain** (same publisher): LangGraph = low-level orchestration runtime; LangChain = high-level abstractions built on top. Complementary.
- Vs [CrewAI](crewai.md) (roles/"employees"), [AutoGen/AG2](autogen-ag2.md) (conversational): "graph/low-level controllable" positioning (a contrast mostly documented by third parties).
- Enterprise price not published.

## Source
https://www.langchain.com/langgraph · https://www.langchain.com/pricing · LICENSE MIT (github.com/langchain-ai/langgraph) · docs.langchain.com (models/persistence/streaming). *(verified on 2026-06-16)*
