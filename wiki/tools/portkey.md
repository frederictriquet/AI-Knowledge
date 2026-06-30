---
tool: "Portkey"
title: "Portkey"
themes: [efficiency-cost, governance-alignment-ops]
type: "Open-source AI Gateway (MIT) self-host + Web service (managed SaaS)"
url: https://portkey.ai/
pricing_model: "Open-core: free MIT gateway + metered SaaS (Free / $49 / Enterprise)"
llm_cost: "BYOK — pass-through, no token markup"
objectives: [cost-control, production]
family: "LLM gateways / routers"
eco_icons: "🔓🎁🔁"
llm_cost_icons: "🔑"
summary: "**Open-core MIT**: < 1 ms gateway over 1,600+ models + guardrails (50+), observability (OTel), semantic caching, prompt management. **BYOK pass-through** (no token markup). SaaS billed by log volume (Developer free 10k → Production $49/month → Enterprise). \"Enterprise\" control plane"
---

# Portkey

**In one sentence** — "Production stack" for GenAI apps: a unified AI Gateway (routing to 1,600+ models) combining gateway, observability, guardrails, governance and prompt management, with an open-source core and a managed cloud.

## Type & integration
**Open-core** model, three facets:
- **Open-source AI Gateway** (`Portkey-AI/gateway` repo, TypeScript): deployable via `npx`, Docker, Node or Cloudflare Workers (edge). Claimed latency overhead **< 1 ms** (~122 KB footprint).
- **Managed SaaS**: dashboard, hosted observability, governance.
- **Unified API/SDK** OpenAI-compatible on the client side.

## Pricing model
**Open-core: free OSS gateway + SaaS billed by log/request volume** (not per seat):
- **Open-source gateway — MIT license** (verified in the repo's LICENSE + GitHub API). ⚠️ March 2026 press releases say "Apache 2.0": **inaccurate**, the source is authoritative → MIT.
- **Developer**: free ("Free Forever"), 10,000 logs/month, 3-day log / 30-day metrics retention. Exceeding 10k does not interrupt requests (only logs beyond are not kept).
- **Production**: **$49/month**, 100,000 logs/month, 30-day / 90-day retention; overage **+$9 / 100K requests** up to 3M.
- **Enterprise**: by quote (VPC/private cloud, SSO/RBAC, compliance). Price not published.

## LLM cost
**🔑 BYOK by default**: you connect your own provider keys (encrypted vault). A **"Virtual Key"** (Model Catalog) acts as a secure alias giving access to several providers without exposing the raw key. **Portkey does not bill tokens** and does not mark them up — the billing relationship stays between you and the provider; Portkey only charges for its service (gateway/observability). (Contrast with [OpenRouter](openrouter.md), which resells credits.)

## What it's for
When you want an **"enterprise-grade" control plane** over your LLM calls: routing/fallback/load-balancing/retries, **50+ guardrails** (PII/redaction, anti-prompt-injection, moderation, JSON/RegEx checks), observability (40+ metrics, OpenTelemetry-compatible), simple **and** semantic caching, versioned prompt management. More oriented toward governance/observability than simple routing.

## Notes
- **Positioning**: BYOK governance/observability control plane. Vs [LiteLLM](litellm.md) (OSS self-host router, full ownership, larger GitHub base) and [OpenRouter](openrouter.md) (hosted gateway that resells tokens).
- **March 2026 — "Gateway 2.0"**: open-sourcing of functions previously SaaS-only (governance, real-time observability, auth, MCP Gateway OAuth 2.1) → **blurred OSS / paid-cloud boundary**, to be verified case by case.
- The SaaS cost **grows with log volume** ($9/100K).
- **Marketing inconsistencies**: model count (1,600+/3,000+/250+) and guardrails (50+/60+) vary across pages; keep the canonical README values (**1,600+ models, 50+ guardrails**).

## Source
https://portkey.ai/ · https://portkey.ai/pricing · https://github.com/Portkey-AI/gateway (LICENSE = **MIT**, via api.github.com/repos/Portkey-AI/gateway/license) · observability/keys docs. *(verified on 2026-06-16; Enterprise price by quote, post-Gateway 2.0 OSS/cloud boundary to reconfirm)*
