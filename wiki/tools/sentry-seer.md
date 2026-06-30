---
tool: "Sentry Seer"
title: "Sentry Seer"
themes: [evaluation, governance-alignment-ops]
type: "Web service (Sentry add-on)"
url: https://docs.sentry.io/product/ai-in-sentry/seer/
pricing_model: "Proprietary (SaaS) — Sentry add-on, billed per active contributor"
llm_cost: "Included (the vendor provides the LLM in the price)"
objectives: [code-generation, reliability]
family: "AI code review"
eco_icons: "🔒🔁💳"
llm_cost_icons: "📦"
summary: "Sentry's AI debugging agent (Autofix, conversational agent, **Code Review**): predicts failures before merge, strong on **production severity** (backed by your Sentry telemetry). Add-on billed per active contributor (2+ PRs/month). LLM included"
---

# Sentry Seer

**In one sentence** — Sentry's AI debugging agent that leverages errors, traces, logs and profiles; its *Code Review* feature analyzes PRs to predict failures **before merge**, with production-issue severity as its strength.

## Type & integration
Add-on to the Sentry platform (so it is backed by your existing error telemetry). Three capabilities: **Autofix** (root-cause analysis + PR generation, triggered when an issue arrives), **Seer Agent** (conversational debugging across all telemetry), and **Code Review** (PR analysis, error prediction and suggestions). It can hand off to external agents (e.g. Claude Code). In the comparison cited by Addy Osmani: the best at judging the **severity** of a production failure.

## Pricing model
Proprietary, an add-on to a Sentry subscription. Billed **per active contributor**: "anyone creating 2 or more PRs in a month in a Seer-enabled project is billed" (observed 2026-06-17). Unit prices not detailed publicly in the docs → to be confirmed on the Sentry pricing page.

## LLM cost
**Included (📦)**: the model is provided by Sentry within the add-on price (underlying LLM not disclosed) — no BYOK.

## What it's for
Linking **PR review** and **production observability**: prioritize what actually breaks in production, do root-cause analysis and propose fixes, drawing on Sentry incident data. Relevant if you already use Sentry.

## Notes
- Broader than a plain PR reviewer (Autofix + debug agent); *Code Review* is just one of its facets.
- Value conditioned on using Sentry as the telemetry backbone.
- ⚠️ Underlying LLM model not disclosed (opaque quality and cost) and value locked into the Sentry ecosystem; for pure PR review, compare with CodeRabbit / Cursor Bugbot / Greptile.

## Source
https://docs.sentry.io/product/ai-in-sentry/seer/ *(verified on 2026-06-17)*
