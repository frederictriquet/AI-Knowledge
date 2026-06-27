---
tool: "Braintrust"
title: "Braintrust"
themes: [evaluation]
type: "Web service (SaaS) + SDK"
url: https://www.braintrust.dev/
pricing_model: "Proprietary — Freemium / Subscription + usage"
llm_cost: "Built-in (logs) + BYOK / resold by usage (eval & playground)"
objectives: [reliability, production]
family: "LLMOps — evaluation & observability"
eco_icons: "🎁🔁💳"
llm_cost_icons: "🟢🔑"
summary: "**Proprietary** LLMOps platform centered on **evaluation/experimentation** (datasets, scoring, playground) + logs. Free Starter ($10 credits, 10k scores, 14 days) → Pro $249/month, Enterprise (on-prem/hybrid). Bills data + scores + tokens (LLM proxy: $0.06/$0.40 per Mtok in/out). LLM-as-judge eval → tokens (BYOK/credits)"
migrated_from: braintrust
---

# Braintrust

**In one sentence** — proprietary LLMOps platform **centered on evaluation and experimentation** (datasets, scoring, playground, comparing prompt/model versions), with logs and observability as a complement.

## Type & integration
SaaS + SDK (Python, TS). Core of the product: build eval **datasets**, run scored **experiments** (including **LLM-as-judge** via the `autoevals` lib), compare results in a playground, then wire up production logs and observability. On-prem / hybrid available on Enterprise for sensitive data.

## Pricing model
Proprietary, freemium (observed on 2026-06-15):
- **Starter**: free — $10 credits, 1 GB data processed (+$4/GB), 10k scores (+$2.50/1k), 14-day retention, unlimited users/projects/datasets.
- **Pro**: $249/month.
- **Enterprise**: on quote, on-prem or hosted deployment.
- Three-dimension billing: **data processed** (GB), **scores**, and **tokens/credits**.

## LLM cost
- **Logs / observability**: records your calls → no LLM cost of its own (🟢).
- **Evaluation & playground**: Braintrust can **run LLM calls** (proxy) to score/compare → consumes tokens. Either via **your keys** (BYOK 🔑), or via their usage-billed credits (💸): observed proxy rates ~$0.06/Mtok input, ~$0.40/Mtok output.

## What it's for
When the #1 need is **rigorous evaluation**: measuring whether a prompt/model change improves or degrades quality, industrializing evals in CI, comparing approaches side by side.

## Notes
- "Eval-first" positioning vs LangSmith/Langfuse, which are more "tracing-first" (all overlap).
- The `autoevals` SDK (ready-to-use evaluators) is published on GitHub — check its license if reused outside the platform.

## Source
https://www.braintrust.dev/pricing · https://www.braintrust.dev/docs *(verified on 2026-06-15)*
