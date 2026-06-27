---
tool: "CrewAI"
title: "CrewAI"
themes: [multi-agent, frameworks-tooling]
type: "Framework (Python library) + cloud platform"
url: https://www.crewai.com
pricing_model: "Open-source (MIT, free framework) + proprietary enterprise offering (CrewAI AMP / Enterprise — cloud or on-premise, quote-based pricing; free control plane trial)"
llm_cost: "BYOK — you plug in your own LLM API keys (OpenAI by default, Anthropic, etc.) or local models (Ollama). Token cost is usually the largest expense."
objectives: [production]
family: "General-purpose multi-agent frameworks (for developers)"
eco_icons: "🔓🔒"
llm_cost_icons: "🔑"
summary: "Open-source (MIT) Python framework to orchestrate teams of autonomous AI agents (Crews) and workflows (Flows), general-purpose; paid enterprise platform (AMP). BYOK"
migrated_from: crewai
---

# CrewAI

**In one sentence** — Open-source Python framework to **orchestrate teams of role-playing autonomous AI agents** ("Crews") and **event-driven workflows** ("Flows"), general-purpose (not coding-specific), paired with an enterprise platform (AMP) for deployment, observability and governance in production.

## Type & integration
**Python library** (`pip install crewai`) — a framework you import into your own code to build multi-agent systems. It is neither a turnkey CLI, nor an MCP server, nor a ready-to-use agent: it is a **building block to assemble**, whose logic the developer writes.

Two main abstractions:
- **Crews** — teams of autonomous agents that collaborate, each with a role, a goal, tools; they distribute and delegate tasks.
- **Flows** — deterministic event-driven orchestration (fine control over the flow, branching, state) for production-grade automations.

Claimed technical characteristic: **fully rewritten from scratch, independent of LangChain** ("lean, lightning-fast"), unlike the early versions.

On the production side, **CrewAI AMP** (Agent Management Platform, formerly CrewAI Enterprise) provides a cloud or on-premise control plane: real-time tracing, execution history, step-by-step inspection, connectors (Gmail, Slack, Salesforce, HubSpot…).

## Pricing model
**Mixed: open-source + enterprise cloud.**
- **Framework**: open-source under the **MIT license**, free, personal and commercial use. ~53k+ ★ on GitHub (repo `crewAIInc/crewAI`), active community.
- **CrewAI AMP / Enterprise**: **proprietary** offering with a **Free tier at $0** (visual editor, copilot, GitHub integration, **50 workflow executions/month**) then **Enterprise on quote** (price not public). Adds managed deployment, observability, advanced security (PII masking, RBAC, secret manager, audit logs, SSO), compliance (SOC2, HIPAA), isolated VPCs and 24/7 support.

## LLM cost
**BYOK 🔑** — CrewAI does not provide an LLM. You supply your own **API keys** (OpenAI by default, but Anthropic, Gemini, etc. supported via the LLM abstraction layer) or point to **local models** (Ollama). You therefore pay the model provider directly by usage.

**Order of magnitude**: like any multi-agent system, cost ramps up fast — several agents exchanging messages, reasoning and calling tools multiply LLM calls. A non-trivial "Crew" run can consume **tens to hundreds of thousands of tokens**, i.e. from a few cents to several dollars per run depending on the model (a high-end model like Opus/GPT-4 costs orders of magnitude more than a small model or a free local model). Cost control (per-agent model choice, iteration limits) is a topic in its own right.

## What it's for
Building **general-purpose multi-agent applications**: research/analysis pipelines, content generation, business-process automation, agents connected to enterprise tools, support assistants, etc. The developer composes specialized agents that collaborate on a complex task broken down into steps. Targets both rapid prototyping (free framework) and governed production deployment (AMP).

## Notes
- **Different family from turnkey coding tools**: CrewAI is a **general-purpose multi-agent framework to build with**, not a ready-to-use coding agent. To be clearly distinguished from [Liza](liza.md) (turnkey coding orchestrator), [Kilo Code](kilo-code.md), [Trae](trae.md), [Supacode](supacode.md). Direct competitors in the same category: **LangGraph** (LangChain), **AutoGen** (Microsoft), **OpenAI Agents SDK**, **LlamaIndex Agents**, Google ADK, Pydantic AI.
- **Link with [Liza](liza.md)**: CrewAI appears in [Liza](liza.md)'s competitive survey (`specs/architecture/competition-survey`). Liza classifies it as a **general framework with *post-hoc* guardrails**: the safeguards (validation, faithfulness scoring, task guardrails) are added around the agents rather than mechanically enforced by construction — the opposite of the deterministic "by the code" approach claimed by Liza. The advanced guardrails are mostly in the **paid AMP offering**, not in the base framework.
- **Cost watch point**: multi-agent = potentially high and unpredictable LLM consumption; monitor the number of iterations and the model choice.
- **To dig into**: real maturity of Flows vs Crews; depth of open-source guardrails vs AMP; exact Enterprise pricing (quote-based, not public).

## Source
- Official site: https://www.crewai.com — *(verified on 2026-06-15)*
- Repo: https://github.com/crewAIInc/crewAI (MIT, ~53k+ ★) — *(verified on 2026-06-15)*
- CrewAI AMP: https://blog.crewai.com/crewai-amp-the-agent-management-platform/ — *(verified on 2026-06-15)*
- Liza competitive survey: `liza-mas/liza/specs/architecture/competition-survey` — *(verified on 2026-06-15)*
