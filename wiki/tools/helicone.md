---
tool: "Helicone"
title: "Helicone"
themes: [governance-alignment-ops]
type: "Web service (proxy/gateway) + open-source self-host"
url: https://www.helicone.ai/
pricing_model: "Open-source (Apache 2.0) + Freemium / Subscription (cloud)"
llm_cost: "Built-in — observes (and can reduce via cache) your own calls"
objectives: [reliability, production]
family: "LLMOps — evaluation & observability"
eco_icons: "🔓🎁🔁"
llm_cost_icons: "🟢"
summary: "Open-source (**Apache 2.0**) LLM observability, mostly via **proxy**: logs, costs, latency, caching, rate-limit, fallbacks. Free self-host or cloud (free Hobby 10k requests/month → Pro $79, Team $799, Enterprise on-prem). Intercepts your calls, generates none (🟢); caching can *reduce* your LLM bill"
---

# Helicone

**In one sentence** — Open-source (Apache 2.0) LLM observability platform, mostly used **via proxy**: logs, costs, latency, caching, rate-limiting and fallbacks, in a few lines of config.

## Type & integration
Two modes: **proxy/gateway** (route your LLM calls through Helicone — the fastest integration, a one-line base URL) or **asynchronous logging** (SDK, without adding latency on the critical path). Self-hostable for free (Docker) or cloud. Beyond observability, the proxy provides "gateway" functions: **cache** (reduces costs and latency), **rate limits**, automatic **fallbacks**.

## Pricing model
Open-source **Apache 2.0**; free self-host. Cloud (observed 2026-06-15):
- **Hobby**: free — 10k requests/month, 1 GB storage, 1 seat, 7-day retention.
- **Pro**: $79/month, unlimited seats, alerts (7-day trial).
- **Team**: $799/month, 5 organizations, compliance functions.
- **Enterprise**: on quote, on-prem deployment.

## LLM cost
**Built-in (🟢)**: Helicone **intercepts your** LLM calls and does not generate completions itself → no separate LLM cost for observability. Better: its **cache** can *reduce* your LLM bill by avoiding redundant calls. (It also offers evaluators; an LLM-as-judge would then consume your tokens as BYOK.)

## What it's for
When you want to **log and monitor quickly** the cost/usage/latency of your LLM calls without re-instrumenting the code, and add cache/rate-limit/fallback along the way. The most "ops/cost" of the family.

## Notes
- Proxy mode = a point on the critical path (latency, dependency); async mode avoids it at the cost of a bit of integration.
- Less oriented toward "rigorous evaluation" than Braintrust; complementary.

## Source
https://www.helicone.ai/pricing · repo https://github.com/Helicone/helicone (README: "licensed under the Apache v2.0 License"). *(verified on 2026-06-15)*
