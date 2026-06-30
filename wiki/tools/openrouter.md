---
tool: "OpenRouter"
title: "OpenRouter"
themes: [efficiency-cost, governance-alignment-ops]
type: "Web service (hosted LLM gateway)"
url: https://openrouter.ai/
pricing_model: "Proprietary / pay-as-you-go (credits)"
llm_cost: "Usage-resold (credits, fee on purchase) or BYOK"
objectives: [cost-control, production]
family: "LLM gateways / routers"
eco_icons: "🔒💳"
llm_cost_icons: "💸🔑"
summary: "Hosted gateway: 1 API (OpenAI format) to **400+ models / 60+ providers**, price/perf routing + failover. **No margin on inference**; monetizes on **credit purchases** (5.5% card, min $0.80; 5.0% crypto). BYOK mode too (migrating to a fixed subscription, amount not published). The most \"turnkey marketplace\""
---

# OpenRouter

**In one sentence** — hosted LLM gateway: a single API (OpenAI SDK-compatible) to 400+ models from 60+ providers, with price/perf routing and automatic failover between providers.

## Type & integration
SaaS web service. You change the base URL and call hundreds of models through a single OpenAI-format endpoint — no per-provider SDK to rewrite. It brings: multi-model routing, **fallback/failover** between providers (availability pooling), consolidated billing (one account instead of N) and *data policies* (restrict which providers see the prompts).

## Pricing model
Proprietary, **pay-as-you-go via prepaid credits** (denominated in $). The key point: **no margin on inference** — the per-million-token price is passed through at the provider's rate. OpenRouter monetizes on **credit purchases**:
- card/Stripe: **5.5%** of the amount, **min $0.80**;
- crypto (USDC): **5.0%** flat, no minimum.
- Refundable credits (~24h window), expire after 1 year. (The former fixed $0.35 fee was removed on 2025-06-09.)

## LLM cost
Two modes:
- **💸 Credits (usage-resold)**: OpenRouter buys the inference and bills it to you at cost; the "margin" is limited to the credit-purchase fees (5.5%/5.0%), not the tokens.
- **🔑 BYOK**: you plug in your own provider key and pay the provider directly; OpenRouter bills only the orchestration. Historically: first 1M BYOK requests/month free, then **5%** of the normalized cost. ⚠️ BYOK is migrating to a **fixed monthly subscription** (announced 2025-06-09) whose amount was **not stated at the source** as of 2026-06-16 — to reconfirm before committing.

## What it's for
Testing/operating many models without opening N provider accounts, with failover for availability and a single bill. The most "turnkey marketplace" of the router family — at the cost of an intermediary on the critical path.

## Notes
- The "margin" is on **top-ups**, not tokens: total cost depends on volume and mode (credits vs BYOK).
- Dependence on a single intermediary (latency, point of failure, prompt exposure unless strict *data policies* — no self-host core, unlike [LiteLLM](litellm.md)/[Portkey](portkey.md)).
- Alternatives: [LiteLLM](litellm.md) (open-source, self-host, pass-through), [Portkey](portkey.md) (open-core BYOK), [Requesty](requesty.md) (EU SaaS). Direct provider calls otherwise.

## Source
https://openrouter.ai/ · https://openrouter.ai/docs/faq · fee announcement https://openrouter.ai/blog/announcements/simplifying-our-platform-fee/ · https://openrouter.ai/pricing. *(verified on 2026-06-16; amount of the future BYOK subscription not published at that date)*
