---
title: "Data flywheel: collecting feedback"
type: "Concept"
theme: evaluation
level: 🔴
source_url: https://eugeneyan.com/writing/llm-patterns/
source_title: "Patterns for Building LLM-based Systems & Products (Collect user feedback)"
objectives: [reliability, production]
---

# Data flywheel: collecting feedback

**In one sentence** — production data is the only durable asset of an LLM product: capturing user feedback (explicit and implicit) creates a *flywheel* that feeds evals, fine-tuning and guardrails alike — the competitive advantage that cannot be copied.

## What the source says
Eugene Yan's seventh production pattern. Two kinds of signal:

- **Explicit feedback**: thumbs up/down, ratings, corrections, flags. Precise but **rare** (few users bother) and biased (the dissatisfied vote more).
- **Implicit feedback**: did the user copy the answer? regenerate? rephrase? abandon? accept the code suggestion? Abundant but **noisy** (an ambiguous signal — a regeneration can mean "bad" or "explore a variant").

These signals close the loop: they become **eval cases** (real failures → golden set, cf. [eval-driven-development](eval-driven-development.md)), **fine-tuning data** (preferred/rejected pairs), and **guardrail rules** (recurring error patterns). The more the product is used, the more it improves — the *flywheel*.

## Tradeoff / insight
- **This is the real moat, not the model.** The base model is a commodity available to all; the **proprietary data loop** built from your users is not. A product without feedback capture throws away its only cumulative advantage.
- **Instrumenting feedback is an architecture decision, not an afterthought.** Each signal must be tied to the **trace** that produced it (prompt, context, model/prompt version) — otherwise the signal is unusable. Hence the tight coupling with [observability](llm-observability-best-practices.md): no `trace_id`, no flywheel.
- **Implicit feedback often lies.** Define the semantics of each signal *before* optimising it (what is a "good" answer: copied? not regenerated? converted?). Optimising a poorly defined proxy degrades the product.
- **Privacy.** Capturing prompts/responses + feedback means storing potentially sensitive data: consent, anonymisation/PII scrubbing, retention — the same requirements as for observability ingestion.

## Primary source
Eugene Yan, *Patterns for Building LLM-based Systems & Products*, section "Collect user feedback" (eugeneyan.com/writing/llm-patterns/). The *data flywheel* concept popularised on the product ML side (Andrew Ng, Tesla).

## See also
- [patterns-systemes-llm](llm-system-patterns.md) — the 7 patterns, this one among them.
- [eval-driven-development](eval-driven-development.md) — captured failures become evals.
- [error-analysis](error-analysis.md) — exploit the collected signals qualitatively.
- [ux-defensive-llm](defensive-ux-for-llm.md) — the UX that makes feedback capturable.
- [observabilite-llm-best-practices](llm-observability-best-practices.md) — linking feedback ↔ trace.
