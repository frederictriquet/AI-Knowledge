---
tool: "Requesty"
title: "Requesty"
themes: [efficiency-cost, governance-alignment-ops]
type: "Web service (hosted LLM gateway)"
url: https://www.requesty.ai/
pricing_model: "Proprietary / freemium + pay-as-you-go (+5% margin)"
llm_cost: "Resold per usage (+5%) or BYOK"
objectives: [cost-control, production]
family: "LLM gateways / routers"
eco_icons: "🔒🎁💳"
llm_cost_icons: "💸🔑"
summary: "Hosted **EU-first / GDPR** gateway (\"European alternative to OpenRouter\"): 400+ models, smart routing, caching, observability. Free 200 req/day → pay-as-you-go **+5% margin** on the provider rate → Enterprise (SSO/RBAC/PII/EU residency). BYOK supported (fee % undocumented). **Early-stage** (seed $3M Sept 2025)"
---

# Requesty

**In one sentence** — Hosted LLM gateway positioning itself as a **European alternative to OpenRouter**: a unified API to 400+ models (30+ providers), cost optimization, failover and observability, with an EU/GDPR and data-residency angle.

## Type & integration
SaaS web service (proxy between the app and the providers), **OpenAI-compatible** API; integrable via SDK (community AI SDK provider). Brings multi-model routing, automatic **failover chains**, **prompt caching** (up to 90% token savings claimed), real-time dashboards (cost, latency, TTFT, P50/P90/P95/P99, error rate) and, on Enterprise, guardrails / PII detection / RBAC / EU residency.

## Pricing model
Proprietary, **freemium + pay-as-you-go**:
- **Free**: $0, 200 requests/day, free models only, no credit card.
- **Pay-as-you-go**: **+5% margin** on the model's base cost (e.g. a model at $10/Mtok comes to **$10.50**), 400+ models, BYOK supported, budget caps. No subscription, no per-seat fee, no minimum.
- **Enterprise**: by quote — SSO (Okta/Azure AD/Google/OIDC), RBAC + audit logs, guardrails, PII detection, SLA, EU residency.

## LLM cost
Two modes coexist:
- **💸 Credits (resold per usage)**: consumption billed with **+5%** on the provider rate.
- **🔑 BYOK**: plug in your own keys, keeping the direct billing relationship.
- ⚠️ **The exact fee % in BYOK mode is not documented** at the source (pricing page/BYOK docs silent); third parties suggest "5% of the request value" by analogy with OpenRouter, **without official confirmation** — validate with support before relying on it.

## What it's for
Route/optimize multi-model calls with an **EU sovereignty angle** (EU servers, GDPR by design) that US competitors don't emphasize. Smart routing (simple tasks → cheaper models) and caching to reduce the bill.

## Notes
- **Young / early-stage product**: seed of **$3M raised in September 2025** (lead 20VC). Few public usage figures → traction hard to assess.
- Claimed savings (30–50%, "$400k/year" at a customer) = **vendor marketing, unaudited**.
- Inconsistent model count across pages (300+ / 400+); the main site announces 400+.
- Positioning: close to [Portkey](portkey.md) (gateway + observability + governance) but more recent and EU-first; vs [OpenRouter](openrouter.md) (US, marketplace) and [LiteLLM](litellm.md) (open-source self-host).

## Source
https://www.requesty.ai/ · https://www.requesty.ai/pricing · https://docs.requesty.ai/features/bring-your-own-keys · https://www.requesty.ai/blog/requesty-raises-3m. *(verified on 2026-06-16; BYOK fee % not documented at the source)*
