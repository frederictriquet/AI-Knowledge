---
tool: "Arize Phoenix / Arize AX"
title: "Arize Phoenix / Arize AX"
themes: [evaluation, governance-alignment-ops]
type: "Open-source library/app (Phoenix) + SaaS web service (Arize AX)"
url: https://phoenix.arize.com/
pricing_model: "Open-source (Phoenix, Elastic License 2.0) + Freemium / Subscription + usage (Arize AX)"
llm_cost: "Built-in (tracing) + BYOK (LLM-as-judge eval)"
objectives: [reliability, production]
family: "LLMOps — evaluation & observability"
eco_icons: "🔓🎁🔁💳"
llm_cost_icons: "🟢🔑"
summary: "**Phoenix**: open-source LLM observability/eval (**Elastic License 2.0**), built on **OpenTelemetry/OpenInference** (framework-agnostic), free self-host. **Arize AX**: SaaS for ML/LLM monitoring in production (Free 25k spans/month → Pro $50/month, Enterprise self-host/SLA/SOC2). Tracing 🟢, eval (`phoenix-evals`) BYOK"
migrated_from: phoenix-arize
---

# Arize Phoenix / Arize AX

**In one sentence** — Two related products from Arize AI: **Phoenix**, an open-source LLM observability/evaluation platform built on **OpenTelemetry/OpenInference** (framework-agnostic, free self-host); and **Arize AX**, the SaaS for ML/LLM monitoring in production at scale.

## Type & integration
- **Phoenix**: library + app (Python-first), runnable locally/in a notebook or self-hosted. Built on **OpenTelemetry** and the **OpenInference** conventions → standard, framework-independent instrumentation (vs LangSmith, which is LangChain-centric). Tracing, evals, experimentation, prompt iteration.
- **Arize AX**: cloud platform to monitor in production (drift, quality, volumes), with governance, compliance and scaling.

## Pricing model
- **Phoenix**: open-source under **Elastic License 2.0 (ELv2)** — free, self-hostable. (ELv2 = source-available, restricts reselling as a competing SaaS; it is not a classic OSI license.)
- **Arize AX** (observed on 2026-06-15): **Free** (25k trace spans/month, 1 GB ingestion, 15-day retention) → **Pro** $50/month (50k spans, 10 GB, 30 days; +$0.0008/span, +$3/GB) → **Enterprise** by quote (self-host, SLA, SOC2/HIPAA, multi-region). Reduced-rate startup program.

## LLM cost
- **Tracing / observability**: calls no LLM → no separate cost (🟢).
- **Evaluation**: the `arize-phoenix-evals` lib does **LLM-as-judge** with **your** key/model (BYOK 🔑) → tokens billed by your provider.

## What it's for
When you want **open standards (OpenTelemetry)** and **local, free** eval/tracing (Phoenix), with a possible move up to **production monitoring at scale** (Arize AX). Phoenix is also a good framework-agnostic entry point.

## Notes
- Watch Phoenix's **ELv2** license (source-available ≠ OSI open-source): fine for internal/self-host use, restrictions on managed reselling.
- The OpenInference instrumentation packages (Python/TS/Java) are reusable with other OTel backends.

## Source
https://phoenix.arize.com/ · https://arize.com/pricing/ · repo https://github.com/Arize-ai/phoenix (README: "licensed under the terms of the Elastic License 2.0 (ELv2)"). *(verified on 2026-06-15)*
