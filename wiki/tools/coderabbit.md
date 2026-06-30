---
tool: "CodeRabbit"
title: "CodeRabbit"
themes: [evaluation]
type: "Web service (GitHub/GitLab app) + IDE / CLI"
url: https://www.coderabbit.ai/
pricing_model: "Proprietary (SaaS) — Freemium / per-seat subscription"
llm_cost: "Included (the vendor provides the LLM in the price)"
objectives: [code-generation, reliability]
family: "AI code review"
eco_icons: "🎁🔁💳"
llm_cost_icons: "📦"
summary: "AI PR reviewer (GitHub/GitLab): summaries, line-by-line review, linters + SAST, 1-click fix. **Free forever for public repos**; Pro $24, Pro Plus $48/user/month, Enterprise (SSO, self-host). Best **recall** in the Martian benchmark (~49% precision). LLM included"
---

# CodeRabbit

**In one sentence** — AI code reviewer that installs on your GitHub/GitLab PRs: summaries, line-by-line review, linter and SAST integration, 1-click fixes; also available in the IDE and CLI.

## Type & integration
An app to connect to the repo (GitHub/GitLab) that automatically comments on each PR; it also acts in the IDE and CLI, plus a Slack agent. It leans on linters and SAST tools in addition to LLM analysis. In the benchmark cited by Addy Osmani: ~49% precision, the **best recall**, with 1-click fixes.

## Pricing model
Proprietary, freemium (observed on 2026-06-17):
- **Free**: $0 — **free forever for public repos**, 14-day Pro Plus trial, IDE/CLI reviews.
- **Pro**: $24/user/month (annual) — full PR reviews, linters, SAST, analytics.
- **Pro Plus**: $48/user/month — custom pre-merge checks, advanced finishing.
- **Enterprise**: on quote — SSO, RBAC, API, **self-hosting**, SLA.
- Usage-based add-on (unlimited PR/CLI reviews); Slack agent at $0.50/agent-minute.

## LLM cost
**Included (📦)**: the LLM is provided by CodeRabbit within the subscription price — no key to bring and no tokens billed separately. Predictable cost (per seat / per usage), not BYOK.

## What it's for
Automate the first review pass on every PR: surface bugs, smells and security points before the human, and smooth out small fixes. Free for open-source.

## Notes
- High recall = more findings to triage (noise); treat as a sensor, not a verdict (cf. [agentic code review](../concepts/agentic-code-review.md)).
- Combine with a reviewer of a different nature (low overlap between tools).

## Source
https://www.coderabbit.ai/pricing *(verified on 2026-06-17)*
