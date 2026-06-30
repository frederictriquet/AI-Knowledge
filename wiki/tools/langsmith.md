---
tool: "LangSmith"
title: "LangSmith"
themes: [evaluation, governance-alignment-ops]
type: "Web service (SaaS) + SDK"
url: https://www.langchain.com/langsmith
pricing_model: "Proprietary — Freemium / Subscription per seat + usage"
llm_cost: "Built-in (observability) + BYOK (LLM-as-judge eval)"
objectives: [reliability, production]
family: "LLMOps — evaluation & observability"
eco_icons: "🎁🔁💳"
llm_cost_icons: "🟢🔑"
summary: "**Proprietary** LLMOps platform from LangChain: tracing, eval, monitoring; tightly integrated with LangChain/LangGraph but usable without. Developer free (1 seat, 5k traces/month) → Plus $39/seat/month (10k traces then $2.50/1k), Enterprise on quote (**only** one to allow self-host/VPC). Observability 🟢, LLM-as-judge eval via BYOK"
---

# LangSmith

**In one sentence** — proprietary LLMOps platform from LangChain (tracing, evaluation, monitoring of LLM apps/agents), tightly integrated with LangChain/LangGraph but usable without any framework.

## Type & integration
Hosted SaaS + client SDKs (Python, TS) to instrument the app. **Self-hosting** (Cloud / Hybrid / VPC) is available **only on the Enterprise plan**; Developer and Plus are cloud-only (data hosted at LangChain, a GDPR concern). Not to be confused with the **`langchain` framework** (which is open-source MIT): LangSmith, the platform, is proprietary.

## Pricing model
Proprietary, freemium (observed 2026-06-15):
- **Developer**: free, 1 seat, up to 5k base traces/month then usage-based.
- **Plus**: $39/seat/month, 10k traces/month then usage-based; unlimited seats at $39 each.
- **Enterprise**: on quote — only one to offer self-host/hybrid/VPC, SSO, SLA.
- Usage beyond quota: ~$2.50/1k base traces, deployment runs ~$0.005 each.

## LLM cost
- **Tracing / observability**: LangSmith records calls, **does not call an LLM** → no separate LLM cost (🟢). It bills the ingestion/storage of traces, not tokens.
- **LLM-as-judge evaluation**: the evaluator uses **your** key/model (BYOK 🔑) → tokens billed by your provider.

## What it's for
The "default", minimal-friction choice when you already work with **LangChain / LangGraph**: debug chains/agents, monitor cost and latency in production, replay evals before merging.

## Notes
- Billing **per trace**: can climb fast at high production volume (watch base vs extended retention).
- Self-host reserved for Enterprise: blocking if data can't leave premises.
- Self-hostable open-source alternatives: **Langfuse**, **Arize Phoenix**.

## Source
https://www.langchain.com/pricing-langsmith · https://docs.smith.langchain.com *(verified on 2026-06-15)*
