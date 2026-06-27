---
title: "LLM resilience & fallback"
type: "Concept"
theme: governance-alignment-ops
level: 🔴
source_url: https://github.com/Portkey-AI/gateway
source_title: "Portkey AI Gateway — fallbacks, retries, load balancing (reference implementation)"
objectives: [production]
migrated_from: resilience-fallback-llm
---

# LLM resilience & fallback

**In one sentence** — an LLM call is a network call to a fallible third-party service (429, 5xx, timeout, quality drift): a serious product applies the reflexes of distributed reliability — retry with backoff, timeout, fallback to another model/provider, circuit breaker and graceful degradation.

## The idea
To be distinguished from [routing & cascades](model-routing-cascades.md), which optimizes for cost (the cheapest capable model). Here the goal is availability: making the request succeed despite a downstream failure.

- **Retry + exponential backoff** on transient errors (429 rate limit, 5xx, network timeout). With jitter to avoid synchronized retry storms. Cap the number of attempts (gateways like Portkey go up to ~5, exponential backoff).
- **Explicit per-call timeout**: an LLM can "hang"; without a timeout, the latency propagates to the whole system.
- **Model/provider fallback**: if OpenAI returns 429, switch to Anthropic (or an equivalent model) rather than failing. This is precisely what gateways ([OpenRouter](../../tools/openrouter.md), [LiteLLM](../../tools/litellm.md), [Portkey](../../tools/portkey.md)) sell under the name failover chains.
- **Circuit breaker**: temporarily cut off a provider that is failing in bursts, instead of hammering it.
- **Graceful degradation**: provide a fallback response (cache, partial answer, honest "try again" message) rather than a raw 500 error to the user — the infra side of [defensive UX](defensive-ux-for-llm.md).

## Tradeoff / insight
Each mechanism has a hidden cost to weigh, not to enable blindly:
- **Retries = amplification.** Under an incident, naive retries make the provider's overload *worse* (retry storm) and multiply the token bill. Backoff + jitter + cap are not optional.
- **Idempotency & double billing.** A retry after a timeout can re-trigger a generation that was already billed (the provider produced the response, only the network was cut). Watch this on the cost side.
- **Fallback ≠ equivalence.** Switching GPT→Claude changes the behavior, format and tone: a silent fallback can degrade quality with no alert. It must be traced (see [LLM observability](llm-observability-best-practices.md)) and both paths must be tested.
- **The SLA is that of the weakest link**: a product depending on a single provider inherits *its* uptime. Multi-provider via a gateway is the most direct resilience lever — at the cost of one more intermediary on the critical path.

## Primary source
Distributed reliability practices (retry/backoff/jitter, circuit breaker — *Release It!*, Hystrix) applied to LLM APIs. Verified reference implementations: Portkey AI Gateway (retries up to 5, exponential backoff, fallback/load-balancing — github.com/Portkey-AI/gateway), LiteLLM (fallbacks), provider *rate limit* guides (429/5xx handling).

## See also
- [model-routing-cascades](model-routing-cascades.md) — the cost axis (not to be confused).
- [ux-defensive-llm](defensive-ux-for-llm.md) — the interface side of graceful degradation.
- [observabilite-llm-best-practices](llm-observability-best-practices.md) — tracing fallbacks and alerting on errors.
- [patterns-systemes-llm](llm-system-patterns.md) — the overall product view.
