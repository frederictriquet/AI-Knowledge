---
title: "Eval-driven development"
type: "Concept"
theme: evaluation
level: 🔴
source_url: https://hamel.dev/blog/posts/evals/
source_title: "Your AI Product Needs Evals"
objectives: [code-generation, reliability, production]
---

# Eval-driven development

**In one sentence** — Building an evaluation system specific to your domain is the foundation of an AI product: it creates the data → evals → improvement flywheel and unlocks everything else.

## What the source says
Hamel observes that failing LLM products share one root cause: "a failure to create robust evaluation systems". Success depends on iteration speed, which rests on three capabilities: evaluating quality (tests), debugging (logging & inspecting data), and changing the system (prompt eng, fine-tuning, code); many do only the third and stay at the demo stage. He describes three evaluation levels of increasing cost: Level 1, unit tests as assertions (pytest-style), fast and run on every code change; Level 2, human & model eval relying on trace logging and an LLM-as-judge aligned with a human; Level 3, A/B testing reserved for mature products. He rejects generic evaluation frameworks: "Don't rely on generic evaluation frameworks… create an evaluation system specific to your problem." The same eval system then serves for free in debugging and fine-tuning (data synthesis & curation).

## Example
At Rechat, the "Listing Finder" feature of the Lucy assistant breaks down into scenarios testable by assertions. On "Find properties with more than 3 bedrooms under $2M in San Jose", the LLM produces a CRM query and the assertion checks the number of results: `len(listing_array) == 1` (a single match), `> 1` (several), `== 0` (none). Added to that are generic cross-cutting tests, like a regex ensuring no internal UUID leaks into the response. Rechat maintains hundreds of these unit tests, updated with every new failure mode observed. Sign of a good test: the model struggles to pass it — those are the cases to fix next via fine-tuning.

## Why it matters
Hamel lays out a complete, tiered approach (assertions → human/model eval → A/B testing) and insists on the business specificity of evals: write evaluations suited to the domain, don't rely only on generic frameworks.

## Takeaways
- Invest in evals first, not only in prompting/fine-tuning.
- Level 1: write many assertions scoped per feature/scenario, run in CI.
- Level 2: log traces, look at them, align the LLM-as-judge with a human (measure precision/recall, not raw agreement if imbalanced).
- Level 3: A/B testing only when the product is mature.
- Reuse the eval infrastructure for debugging and data curation/fine-tuning.

## See also
- [Trajectory evaluation](trajectory-evaluation.md)
- [LLM-as-a-judge](llm-as-a-judge.md)
- [Evaluator-optimizer pattern](workflow-patterns.md)
- [full post](../../sources/hamel-husain/md/evals.md)
