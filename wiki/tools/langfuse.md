---
tool: "Langfuse"
title: "Langfuse"
themes: [evaluation, governance-alignment-ops]
type: "Web service (cloud) + open-source self-host"
url: https://langfuse.com/
pricing_model: "Open-source (MIT core) + Freemium / Subscription (cloud)"
llm_cost: "Built-in (observability) + BYOK (LLM-as-judge eval)"
objectives: [reliability, production]
family: "LLMOps — evaluation & observability"
eco_icons: "🔓🎁🔁"
llm_cost_icons: "🟢🔑"
summary: "Open-source LLMOps platform (**MIT** core, commercial `ee` folders): tracing, evaluation, prompt management, datasets. Free self-host or cloud (Hobby free 50k units/month → Core $29, Pro $199, Enterprise $2,499/month). Observability with no LLM cost (🟢); LLM-as-judge eval is BYOK. OSS alternative to LangSmith"
migrated_from: langfuse
---

# Langfuse

**In one sentence** — open-source LLMOps platform (tracing, evaluation, prompt management, datasets) to debug, measure and monitor an LLM application; the reference open-source alternative to LangSmith.

## Type & integration
Hosted web service (Langfuse Cloud) **or** free self-hosting (Docker, k8s). You instrument your app via SDK (Python, JS/TS), integrations (LangChain, LlamaIndex, OpenAI SDK…) or the API/OpenTelemetry. Covers the three pillars: **tracing** (detail of an execution), **evaluation** (datasets, scores, LLM-as-judge), **observability** (costs, latency, volumes) + prompt management.

## Pricing model
Open-source: the core of the repo is under the **MIT license**, **except the `ee` folders** (Enterprise Edition) which fall under a commercial license. Self-hosting **free**. Cloud (observed 2026-06-15):
- **Hobby**: free, 50k units/month, 2 users, 30-day retention.
- **Core**: $29/month, 100k units included then $8/100k, 90 days, unlimited users.
- **Pro**: $199/month, 3-year retention (Teams option +$300/month).
- **Enterprise**: $2,499/month, custom rate limits, dedicated support.
- Volume discount: $8 → $6/100k units by tier.

## LLM cost
- **Observability / tracing**: Langfuse **does not call an LLM** — it records your calls and their tokens/costs → no separate LLM cost (🟢).
- **LLM-as-judge evaluation**: evaluators can invoke an LLM; it's then **your** key/model (BYOK 🔑) → tokens billed by your LLM provider, not by Langfuse.

## What it's for
Mastering an LLM app in production: debug a response via its trace, track cost/latency, test quality on datasets, version prompts. Natural choice when you want **self-hostable open-source** (data on your premises, no vendor lock-in).

## Notes
- Distinguish the MIT core from the `ee` features (enterprise SSO, etc.) under a commercial license.
- Direct competitors: LangSmith (proprietary, LangChain-integrated), Braintrust (eval-focused), Arize Phoenix (OTel).

## Source
https://langfuse.com/pricing · repo https://github.com/langfuse/langfuse (README: "This repository is MIT licensed, except for the `ee` folders"). *(verified on 2026-06-15)*
