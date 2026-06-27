---
type: index
title: "Theme — Efficiency & cost"
theme: efficiency-cost
---

# ⚡ Efficiency & cost

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Reducing cost and latency (routing, caching, decoding)._

## Concepts (5)

### 🟡 Tradeoff / intermediate
- **[Constrained decoding / structured output](../concepts/constrained-decoding.md)** — force the output to respect a grammar/schema (JSON, regex) by masking invalid tokens at decoding time; guarantees a parsable format (≠ "politely asking" for JSON).
- **[Model routing & cascades](../concepts/model-routing-cascades.md)** — route each request to the cheapest model CAPABLE of handling it, or chain from small to large (cascade) with a confidence judge; sharply reduces cost at near-constant quality.
- **[Semantic caching](../concepts/semantic-caching.md)** — cache queries, context and results by semantic similarity, used as an agent memory mechanism.
- **[Speculative decoding](../concepts/speculative-decoding.md)** — a small "draft" model proposes several tokens, the large model VERIFIES them in one pass; speeds up inference without changing the output distribution.
- **[Structured outputs (instructor / Pydantic)](../concepts/structured-outputs-instructor.md)** — get typed and validated data from an LLM (via Pydantic models) rather than parsing free text, with automatic validation and retries.

## Tools (0)

- _(aucun)_
