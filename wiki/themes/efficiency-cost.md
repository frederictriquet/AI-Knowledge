---
type: index
title: "Theme — Efficiency & cost"
theme: efficiency-cost
---

# ⚡ Efficiency & cost

> ⚙️ **Generated file** by `tools/build_index.py` — do not edit by hand.

_Reducing cost and latency (routing, caching, decoding)._

## Concepts (5)

### 🟡 Tradeoff / intermediate
- **[Constrained decoding / structured output](../concepts/constrained-decoding.md)** — force the output to respect a grammar/schema (JSON, regex) by masking invalid tokens at decoding time; guarantees a parsable format (≠ "politely asking" for JSON).
- **[Model routing & cascades](../concepts/model-routing-cascades.md)** — route each request to the cheapest model CAPABLE of handling it, or chain from small to large (cascade) with a confidence judge; sharply reduces cost at near-constant quality.
- **[Semantic caching](../concepts/semantic-caching.md)** — cache queries, context and results by semantic similarity, used as an agent memory mechanism.
- **[Speculative decoding](../concepts/speculative-decoding.md)** — a small "draft" model proposes several tokens, the large model VERIFIES them in one pass; speeds up inference without changing the output distribution.
- **[Structured outputs (instructor / Pydantic)](../concepts/structured-outputs-instructor.md)** — get typed and validated data from an LLM (via Pydantic models) rather than parsing free text, with automatic validation and retries.

## Tools (12)

- **[Agent Booster](../tools/agent-booster.md)** — _MCP server / CLI_
- **[Cavekit](../tools/cavekit.md)** — _Plugin (Claude Code) + skills_
- **[Caveman](../tools/caveman.md)** — _Skill (Claude Code + ~30 agents)_
- **[ECC](../tools/ecc.md)** — _Agent harness system (skills/agents/hooks/rules) — multi-platform, OSS + GitHub App_
- **[Headroom](../tools/headroom.md)** — _CLI / Proxy / MCP server / Library_
- **[LiteLLM](../tools/litellm.md)** — _Python library (SDK) + self-host Proxy/Gateway (open-source) + Enterprise_
- **[OpenRouter](../tools/openrouter.md)** — _Web service (hosted LLM gateway)_
- **[Portkey](../tools/portkey.md)** — _Open-source AI Gateway (MIT) self-host + Web service (managed SaaS)_
- **[Ref (ref.tools)](../tools/ref.md)** — _MCP server (up-to-date technical documentation)_
- **[Requesty](../tools/requesty.md)** — _Web service (hosted LLM gateway)_
- **[RTK (Rust Token Killer)](../tools/rtk.md)** — _CLI (proxy)_
- **[Tokenade](../tools/tokenade.md)** — _CLI_
