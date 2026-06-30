---
title: "Patterns for LLM systems in production"
type: "Concept"
theme: evaluation
level: 🔴
source_url: https://eugeneyan.com/writing/llm-patterns/
source_title: "Patterns for Building LLM-based Systems & Products"
objectives: [reliability, production]
---

# Patterns for LLM systems in production

**In one sentence** — seven practical patterns to turn an LLM demo into a reliable product, organized along two axes: improve performance vs reduce cost/risk, and close to the data vs close to the user.

## What the source says
Eugene distills academic research, industry resources and practitioner know-how into seven key patterns: **Evals** (measure performance and detect regressions, otherwise "you're flying blind"), **RAG** (add fresh external knowledge, reduce hallucinations by grounding the model), **Fine-tuning** (specialize on a task), **Caching** (reduce latency and cost by caching responses, but "caching safely" rather than semantic similarity alone), **Guardrails** (validate the output: JSON schema, factuality, harmful content, adversarial inputs), **Defensive UX** (anticipate and handle errors at the interface), and **Collecting feedback** (build the data flywheel — explicit or implicit). He quotes a HackerNews comment: the emphasis on evals distinguishes those who "rush hot garbage" from those building seriously.

## Example
The naive semantic cache illustrated by Eugene: a query "summary of *Mission Impossible 2*" is judged close enough, by embedding similarity, to "*Mission Impossible 3*" — and the wrong summary is served. The "caching safely" fix: key on the item ID (or the pair of IDs for a comparison), pre-compute anticipated queries offline in batch, and choose the pattern based on the power law of traffic (a cache only makes sense if a minority of requests concentrate the majority of hits; on uniformly random traffic, the cost of maintaining it cancels the gain).

## Why it matters
Eugene provides the **end-to-end system/product view** with engineering detail: concrete metrics (BLEU, ROUGE, BERTScore and their limits), caching as an often-ignored cost/latency lever, and above all the insistence that without representative evals you cannot measure a change at scale.

## Key points
- 7 patterns on a 2×2 plane: data ↔ user, defensive ↔ offensive.
- Evals = the foundation: measure each component (LLM, prompt, context, temperature).
- RAG: cheaper to keep an index up to date than to re-pre-train.
- Semantic caching = a "disaster waiting to happen" if naive.
- User feedback feeds evals, fine-tuning AND guardrails.

## See also
- [Workflow patterns](workflow-patterns.md)
- [Agentic RAG](agentic-rag.md)
- [Eval-driven development](eval-driven-development.md)
- [full post](https://eugeneyan.com/writing/llm-patterns/)
