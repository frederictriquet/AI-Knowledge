---
tool: "Greptile"
title: "Greptile"
themes: [evaluation]
type: "Web service (GitHub app)"
url: https://www.greptile.com/
pricing_model: "Proprietary (SaaS) — Freemium / Subscription per seat + usage"
llm_cost: "Included (the vendor provides the LLM in the price)"
objectives: [code-generation, reliability]
family: "AI code review"
eco_icons: "🎁🔁💳"
llm_cost_icons: "📦"
summary: "AI PR reviewer with **whole-codebase understanding** (strong on architecture/context); ~82% of bugs caught (recall > precision). Pro $30/seat/month (50 reviews included, +$1/review), Enterprise (self-host). Free for qualifying OSS, -50% for startups"
---

# Greptile

**In one sentence** — AI code reviewer for GitHub PRs that relies on a **whole-codebase understanding**: strong on architecture and context issues, favours recall.

## Type & integration
Application connected to GitHub (GitHub Enterprise on Enterprise); automatic PR review with a codebase graph to catch cross-file impacts that a local review misses. In the benchmark cited by Addy Osmani: ~82% of bugs caught, trading precision for recall.

## Pricing model
Proprietary, freemium (observed 2026-06-17):
- **Pro**: $30/seat/month — 50 reviews included, then $1/extra review.
- **Enterprise**: on quote — dedicated support, **self-hosting** (exclusive to this plan).
- 14-day trial; **free** for qualifying open-source projects; **-50%** for pre-Series A startups (<$2M revenue).

## LLM cost
**Included (📦)**: the LLM is provided by Greptile in the price (per seat + per review) — no BYOK, no tokens billed separately.

## What it's for
Detecting bugs that depend on the project's **global context** (architecture, conventions, cross-module side effects), where "local" reviewers are blind. A good complement to a precision-oriented tool.

## Notes
- Recall > precision = more false positives to filter; the human keeps the merge.
- Self-host reserved to Enterprise; worth knowing if data cannot leave.

## Source
https://www.greptile.com/pricing *(verified on 2026-06-17)*
