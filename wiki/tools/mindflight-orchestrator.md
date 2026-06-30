---
tool: "MindFlight Orchestrator (MFO)"
title: "MindFlight Orchestrator (MFO)"
themes: [multi-agent, governance-alignment-ops]
type: "Platform (AI agent orchestration / enterprise automation)"
url: https://www.mindflight.be/
pricing_model: "Proprietary, B2B — no public pricing (sales-led / CEO diagnostic)"
llm_cost: "❓ Unverified — the publisher mentions integrating your own providers (OpenAI/Anthropic/… or local), suggesting BYOK, but the LLM billing mechanism is not publicly documented"
objectives: [production]
family: "Multi-agent orchestration & enterprise automation"
eco_icons: "🔒"
llm_cost_icons: "❓"
summary: "Belgian B2B AI-agent orchestration platform (\"AI Operating System\"): connects CRM/ERP/email…, agents as dynamic workflows, multi-provider (OpenAI, Anthropic, Mistral… or local). Proprietary, pricing on quote"
---

# MindFlight Orchestrator (MFO)

**In one sentence** — AI agent orchestration platform for the enterprise, presented as an "AI Operating System": a transparent layer that connects silos (CRM, ERP, email, Slack…), structures data flows and coordinates AI agents across departments.

> Context: product from the Belgian publisher MindFlight (mindflight.be). B2B/enterprise positioning, not a coding tool — hence its dedicated family (orchestration & automation).

## Type & integration
**Platform** (not a simple app), three-part architecture:
- **MFO Client** — local intelligence: captures events where they happen (emails, CRM updates, customer interactions) and triggers workflows.
- **MFO Server** — the engine: APIs, memory, AI tools; secure, stateless, extensible.
- **MFO Providers** — specialized modules: each enterprise system (CRM, ERP, documents, AI models) becomes an augmented module.

Agents are **dynamic workflows** (in teams) or **task flows** (solo): instead of following a fixed sequence, the agent adapts within a frame. They understand natural language, decide under uncertainty, remember context and collaborate with each other.

## Pricing model
**Proprietary, B2B sales.** No public pricing: the journey pushes toward a "Book My 25-Minute CEO Diagnostic" and a free ebook → typical **sales-contact / quote** model of enterprise platforms. Highlights: governance (security, compliance, auditability), modular scalability, measurable ROI (per-agent dashboard: hours saved, revenue generated).

## LLM cost
**❓ Unverified.** MindFlight's marketing says AI integrates via **any provider** (OpenAI, Anthropic, Grok, Groq, Mistral, DeepSeek…) or **local** models, combinable within one workflow — which **suggests** a **BYOK** model (you plug in your own providers). **But**: no pricing page (/pricing 404s), and the exact LLM billing mechanism (your keys vs included in the enterprise subscription) **is documented nowhere**. So I'm not asserting it. The platform itself is on quote (B2B). → to confirm with the publisher.

## What it's for
Industrializing AI in an enterprise beyond isolated pilots: customer/employee chatbots, behind-the-scenes assistant teams, business agents (CEO assistant producing briefs before meetings, data agent that cleans/enriches/routes customer data, support agent linking emails and a knowledge base). Target: company leadership looking to connect their systems and automate processes.

## Notes
- The only **non-coding** tool in the census at this stage: "enterprise orchestration / automation" family, distinct from the dev tools.
- Conceptual competitors/neighbors: n8n (+ AI), Make, Zapier AI, watsonx Orchestrate (IBM), Microsoft Copilot Studio.
- To dig into: real pricing, deployment (cloud/on-prem), scope of self-hosting.

## Source
- Official site: https://www.mindflight.be/ (and /how-it-works/, /core-components/, docs) — automated fetch blocked (403), content retrieved via curl on 2026-06-15

*(verified on 2026-06-15 — official pages via curl + web search; pricing not public)*
