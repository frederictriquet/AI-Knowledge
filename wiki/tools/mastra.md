---
tool: "Mastra"
title: "Mastra"
themes: [frameworks-tooling]
type: "TypeScript/JS agent framework + Mastra Cloud (deployment)"
url: https://mastra.ai/
pricing_model: "Open-source (Apache 2.0 core; ee/ under Enterprise license) + Mastra Cloud (freemium)"
llm_cost: "🔑 BYOK, model-agnostic (via Vercel AI SDK) — does not bill tokens"
objectives: [production]
family: "General-purpose multi-agent frameworks (for developers)"
eco_icons: "🔓🎁💳"
llm_cost_icons: "🔑"
summary: "**TypeScript-native** (Apache 2.0 core; Gatsby team): agents, workflows, RAG, memory, evals, on Vercel AI SDK. Fills the gap vs the Python ecosystem. Mastra Cloud (beta): Starter $0 → Teams $250. YC W25, $13M seed"
migrated_from: mastra
---

# Mastra

**In one sentence** — **TypeScript-native** agent framework (by the team behind Gatsby): agents, workflows, RAG, memory, evals and observability — built to fill the gap in an agentic ecosystem long dominated by Python.

## Type & integration
Open-source **TypeScript/JS** framework (not a Python port), built for the JS ecosystem and relying on the **Vercel AI SDK**. Primitives: agents, **workflows**, RAG, persistent memory, tools (**Zod** schemas), evals/scorers, guardrails, tracing (tokens/latency/costs). Deployable on any Node.js runtime (Vercel/Netlify/Cloudflare deployers) or via **Mastra Cloud** (public beta). Stable 1.0 on Jan. 21, 2026, ~25k★.

## Pricing model
- **Core: open-source Apache 2.0.** The `ee/` directory (Enterprise Edition) is **source-available under the "Mastra Enterprise License"** (dual-license).
- **Mastra Cloud** (deployment/monitoring, public beta): **Starter** $0/month (100k obs. events, 24 CPU-h, 15 days) → **Teams** $250/month (1M events, SSO, SOC 2) → **Enterprise** on quote (RBAC, audit, SLA).

## LLM cost
**🔑 BYOK, model-agnostic** via **model routing** (40+ providers: OpenAI, Anthropic, Gemini…). The open-source framework **does not bill tokens**. The only **optional** exception: Mastra Cloud's "Memory Gateway", billed at **Market Rate + 5.5%** if you route through it.

## What it's for
The choice when building an AI product **in TypeScript** (JS front and back) and you don't want to switch to Python. Full stack (agents → workflows → RAG → memory → evals → obs) idiomatic to JS.

## Notes
- **Young but strong traction**: launched Oct. 2024, 1.0 in Jan. 2026, 300k+ npm downloads/week, YC W25, $13M seed (Oct. 2025, YC + Gradient Ventures, with G. Rauch / A. Masad / S. Banon among the angels). Counters and "beta" status evolve fast.
- Positioning: TS-first alternative to **LangGraph.js** and to the Python ecosystem ([CrewAI](crewai.md), [LangGraph](langgraph.md), [Pydantic AI](pydantic-ai.md)).
- Customer logos (Replit, PayPal, SoftBank…) = Mastra communication, not audited.

## Source
https://mastra.ai/ · https://mastra.ai/pricing · https://mastra.ai/blog/apache-license · github.com/mastra-ai/mastra (LICENSE.md Apache 2.0 + ee/LICENSE) · https://mastra.ai/blog/seed-round. *(verified on 2026-06-16; beta status/counters volatile)*
