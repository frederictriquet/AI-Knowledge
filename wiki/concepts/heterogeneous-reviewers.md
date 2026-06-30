---
title: "Heterogeneous reviewers: low overlap between tools"
type: "Concept"
theme: evaluation
level: 🟡
source_url: https://addyosmani.com/blog/agentic-code-review/
source_title: "Agentic Code Review — Addy Osmani"
objectives: [code-generation]
---

# Heterogeneous reviewers: low overlap between tools

**In one sentence** — AI code reviewers overlap very little: rather than hunting for "the best" tool, run several with complementary strengths, like an ensemble.

## What the source says
Osmani cites a parallel comparative study of four AI reviewers: across 617 flagged locations, **93.4% were detected by only one of the four tools**, and *none* by all four; only ~6.6% of findings were caught by two or more tools. In other words, each tool has a distinct detection "signature" (one strong on architecture, another on the severity of production failures, etc.), and choosing a single "best" tool means accepting a wide blind spot. The recommendation: **run two or more reviewers** of different natures to capture complementary bugs — at the cost of more noise to triage (precision vs recall) and a token cost. This is the transposition, to code review, of the idea of **ensembling**: diverse evaluators cover more failure modes than the redundancy of a single evaluator.

## Why it matters
The figure (93.4% "solo" findings) contradicts the intuition of a "shoot-out to elect the best tool" and quantitatively justifies a multi-reviewer strategy; it aligns with ensembling patterns and verification through diverse perspectives.

## Takeaways
- Don't benchmark to *elect* a tool; benchmark to *combine* complementary tools.
- Favor **diversity** of reviewers (architecture, security, production severity) over redundancy.
- Accept the tradeoff: more recall = more noise → a human triages, the AI does not decide.
- Watch the cost: N reviewers on each PR = N× the tokens.

## See also
- [Agentic code review: from writing to verification](agentic-code-review.md)
- [Ensembling techniques](ensembling-techniques.md)
- [LLM evaluators (LLM judges)](llm-evaluators.md)
