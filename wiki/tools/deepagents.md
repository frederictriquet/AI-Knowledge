---
tool: "deepagents (Deep Agents)"
title: "deepagents (Deep Agents)"
themes: [frameworks-tooling, agent-fundamentals]
type: "Python library (+ JS/TS) — agent harness"
url: https://github.com/langchain-ai/deepagents
pricing_model: "Open-source (MIT), free — by LangChain"
llm_cost: "BYOK (🔑) — model-agnostic: any tool-calling LLM (frontier API, open-weight, local); you supply the model/key"
objectives: [production]
family: "General-purpose multi-agent frameworks (for developers)"
eco_icons: "🔓"
llm_cost_icons: "🔑"
summary: "**\"Batteries-included\" high-level harness** (LangChain, MIT, ~25k★) built on LangGraph/`create_agent`: turnkey **long-horizon** agents — **planning** tool, **sub-agents** with isolated context, **virtual file system**, automatic context management/summarization, cross-session memory, human-in-the-loop, skills. Model-agnostic (frontier/open-weight/local), BYOK"
---

# deepagents (Deep Agents)

**In one sentence** — "the batteries-included agent harness": a library that gives you, turnkey, the building blocks of a **long-horizon** agent (planning, sub-agents, file system, context management) on top of LangGraph.

## Type & integration
**Python library** (`pip`, ~25k★, Python 99%), with a **JS/TS** version (`deepagentsjs`). Published by **LangChain**. Model-agnostic via LangChain chat models. Building blocks provided:
- **Planning tool** (todo / decomposition),
- **Sub-agents** with **isolated context** (task delegation),
- **Virtual file system** (read/write/edit/search) + sandboxed shell execution,
- **Automatic context management/summarization**, **cross-session memory**,
- **Human-in-the-loop** (approval gates), custom skills/tools.

## Position in the LangChain stack (important)
> "**LangGraph** = the graph *runtime*. LangChain's **`create_agent`** = a minimal harness on top. **Deep Agents** = a **more opinionated** harness on top of `create_agent` — same blocks, but with filesystem, sub-agents, context management and skills *built in*."

So three layers, to choose based on need:
- **deepagents** → you want the **full harness** (planning + context + delegation) ready to use.
- **`create_agent`** (LangChain) → a **lightweight** harness without the bundled middleware.
- **[LangGraph](langgraph.md)** → when the **agent loop itself** must be custom (bespoke graph).

## Pricing model
**Open-source, MIT license**, free. No offering of its own: LangChain monetization is elsewhere (LangSmith / LangGraph Platform). Natural integration with **LangSmith** for tracing.

## LLM cost
**BYOK 🔑** — deepagents neither embeds nor resells an LLM. You plug in **any tool-calling model**: frontier API (OpenAI, Anthropic, Google), open-weight (Baseten, Fireworks…), or **local** (Ollama, vLLM, llama.cpp). The cost = your provider's, at your usage. ⚠️ Like any "deep agent" harness (planning + sub-agents + large system prompt + context re-reads), **token consumption can be high** on long tasks — that is the price of long-horizon autonomy.

## What it's for
Quickly building autonomous **multi-step / long-horizon** agents (deep research, refactors, business workflows) without rewriting the planning/context/delegation plumbing. It is the "product" implementation of the **deep-agents pattern** (planner + sub-agents + virtual FS + detailed system prompt) popularized by Claude Code / Deep Research.

## Notes
- **[General-purpose multi-agent frameworks](../guides/ai-in-production.md#fam-general-purpose-multi-agent-frameworks-for-developers) family**: a **high-level** layer complementary to [LangGraph](langgraph.md) (low-level) — same publisher. Also to be distinguished from [CrewAI](crewai.md) (roles/teams), OpenAI Agents SDK (minimalist). It is **not** a turnkey coding tool (do not confuse with the [coding orchestrators](../guides/generate-code-with-ai.md#fam-coding-orchestrators-multi-agent-systems)).
- The **"deep agents" pattern** itself (planning tool + sub-agents + virtual file system + detailed system prompt) has its own **concept page**: [`concepts/deep-agents.md`](../concepts/deep-agents.md) (architecture, independent of this product).
- JS/TS version: `langchain-ai/deepagentsjs`. Docs: docs.langchain.com/deepagents.

## Source
- Repo: https://github.com/langchain-ai/deepagents (MIT, ~25k★, GitHub API verified on 2026-06-17) · JS/TS: https://github.com/langchain-ai/deepagentsjs · docs: https://docs.langchain.com/deepagents

*(verified on 2026-06-17 — GitHub API [MIT license] + README)*
