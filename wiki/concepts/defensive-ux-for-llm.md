---
title: "Defensive UX for LLM products"
type: "Concept"
theme: governance-alignment-ops
level: 🔴
source_url: https://eugeneyan.com/writing/llm-patterns/
source_title: "Patterns for Building LLM-based Systems & Products (Defensive UX)"
objectives: [production]
---

# Defensive UX for LLM products

**In one sentence** — an LLM makes mistakes, hallucinates and answers slowly *by construction*; defensive UX designs the interface starting from that fallibility rather than denying it — guide the input, handle the error gracefully, and keep the human in control of the output.

## What the source says
This is one of Eugene Yan's 7 production patterns: "anticipate and handle errors on the interface side". The central idea: the perceived quality of an LLM product depends as much on the **UX wrapping** as on the model. Three families of levers:

- **Input side — reduce the failure surface**: prompt suggestions/examples, autocompletion, input constraints, templates. The user is guided toward the queries the system handles well.
- **Latency side — manage perceived time**: token-by-token *streaming* (reduces the perceived *time-to-first-token*), progress indicators, optimistic responses. An LLM that "types" feels faster than a frozen spinner at equal duration.
- **Output side — keep the human as judge**: present several candidates, allow editing before sending, cite sources ([source verification](source-verification.md)), display a confidence level, make *undo* and reporting easy. Never pass off an unverified output as truth.

## Tradeoff / insight (for a senior)
- **UX is a guardrail as powerful as the prompt.** Many "model failures" are actually interface failures: the user asked an out-of-scope question for lack of guidance, or took a hallucination for a fact for lack of friction. Fixing the UX is often cheaper and more reliable than re-prompting or fine-tuning.
- **Calibrated friction.** Too many confirmations kill usage; zero friction turns every hallucination into an action. The right level depends on the **cost of error** (suggesting a text ≠ executing a transaction). This is the junction with [human-in-the-loop](human-in-the-loop-static-dynamic.md).
- **Streaming is a double-edged sword**: it improves perceived latency but exposes the response *before* any post-filtering (output guardrails, moderation). Streaming AND filtering requires engineering (buffering, on-the-fly redaction).
- **Honesty > magic.** Announcing limits ("I may be wrong, verify") builds more durable trust than a UX that overplays omniscience and betrays it at the first misstep.

## Primary source
Eugene Yan, *Patterns for Building LLM-based Systems & Products*, "Defensive UX" section (eugeneyan.com/writing/llm-patterns/). Lineage: Human-AI interaction guidelines (Microsoft/Apple) cited in the post.

## See also
- [llm-system-patterns](llm-system-patterns.md) — the 7 patterns this one is part of.
- [llm-resilience-fallback](resilience-fallback-llm.md) — the infra side of graceful degradation.
- [hitl-static-dynamic](human-in-the-loop-static-dynamic.md) — calibrating friction by risk.
- [data-flywheel-feedback](data-flywheel-feedback.md) — user reporting feeds the loop.
