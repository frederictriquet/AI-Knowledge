---
tool: "LiteLLM"
title: "LiteLLM"
themes: [efficiency-cost, governance-alignment-ops]
type: "Python library (SDK) + self-host Proxy/Gateway (open-source) + Enterprise"
url: https://www.litellm.ai/
pricing_model: "Open-source (MIT) + paid Enterprise (self-managed)"
llm_cost: "BYOK — pass-through, does not bill tokens"
objectives: [cost-control, production]
family: "LLM gateways / routers"
eco_icons: "🔓🎁"
llm_cost_icons: "🔑"
summary: "**Open-source MIT** core (BerriAI): SDK (in code) **or** self-host proxy/gateway (virtual keys, budgets, multi-tenant). Unified API to 100+ LLMs, routing/fallback. **Pure pass-through**: does not bill tokens (BYOK). Paid Enterprise (SSO/RBAC/audit, self-managed, prices not published)"
migrated_from: litellm
---

# LiteLLM

**In one sentence** — call 100+ LLM providers via a **unified OpenAI-format API**, as a Python SDK (embedded in code) or as a self-host proxy (centralized gateway), with routing, fallbacks and spend tracking. Publisher: BerriAI.

## Type & integration
Two distinct objects, usable separately:
- **Python SDK (library)**: to import into an app — retry/fallback, application-level load balancing, observability callbacks.
- **Proxy Server / "AI Gateway" (self-host)**: centralized gateway shared across teams (auth, **virtual keys**, budgets, RPM/TPM rate limits, dashboard, multi-tenant tracking), deployable in Docker.

No general-purpose hosted cloud offering: you host it yourself.

## Pricing model
- **Open-source core — MIT license** (SDK *and* base proxy): free, modifiable, free commercial use.
- **LiteLLM Enterprise** (paid, **self-managed**): SSO/SAML/SCIM, granular RBAC, guardrails, secret-manager, key rotation, Prometheus metrics, audit logs, 24/7 SLA support. Trial via a 30-day key.
- **Enterprise prices not published** at the source ("contact sales"). Third-party estimates circulate (~$250/month to ~$2,500/month) but come from a competitor's blog — **unverified**, not to be cited as official.

## LLM cost
**🔑 Pure BYOK**: you plug in your own provider keys; LiteLLM **does not bill tokens** — it proxies your calls and consumption is billed directly by each provider on your keys. LiteLLM **measures and attributes** costs (per key/user/team/org) without inserting itself into billing. (Clear difference from [OpenRouter](openrouter.md), which resells credits.)

## What it's for
Standardize all your LLM calls behind a single OpenAI interface, with routing/fallback and — via the proxy — access governance (virtual keys, budgets) for multiple teams. An infra building block that other observability tools (Langfuse, Arize Phoenix, OpenTelemetry) instrument.

## Notes
- **SDK vs Proxy**: the SDK handles one app; the proxy is a shared gateway. Choose by scale.
- Enterprise features (SSO, fine RBAC, guardrails, audit) are under a **commercial license**, not MIT.
- Self-host mandatory → hosting costs/operations are on you.
- Alternatives: [OpenRouter](openrouter.md) (hosted gateway, resells tokens), [Portkey](portkey.md) (open-core + cloud), Cloudflare AI Gateway.

## Source
https://www.litellm.ai/ · https://www.litellm.ai/enterprise · https://github.com/BerriAI/litellm · LICENSE = **MIT** (Copyright (c) 2023 Berri AI). *(verified on 2026-06-16; Enterprise prices not published at the source)*
