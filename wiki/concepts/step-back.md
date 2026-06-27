---
title: "Step-Back prompting"
type: "Concept"
theme: reasoning-planning
level: 🟡
source_url: https://arxiv.org/abs/2310.06117
migrated_from: step-back
---

# Step-Back prompting

**In one sentence** — before answering a specific question, ask the model to "step back" and formulate the underlying general concept or principle, then reason from that abstraction.

## The idea
Rather than attacking the detail directly, Step-Back derives an **abstraction question**: what physical principle, what rule, what higher-level concept governs this case? The model first answers that general question, then uses the principle as a guide to solve the concrete question. This abstraction reduces reasoning errors caused by premature focus on irrelevant details.

## Example
On the TimeQA question "Which school did Estella Leopold attend between August and November 1954?", Step-Back first generates the abstraction "What is Estella Leopold's education history?", removes the misleading temporal constraint, then filters. On PaLM-2L: MMLU Chemistry rises from 70.9 to 81.8%, and TimeQA jumps from 41.5 to 68.7% in RAG, i.e. +27 points.

## Tradeoff / when to use it
Gains on scientific, multi-step reasoning and factual questions requiring an intermediate principle. Modest cost: one extra call for the abstraction. Effective when a generalizable principle exists behind the particular case; useless, even counterproductive, on purely factual or lookup questions where no abstraction helps. Complementary to Least-to-Most: one abstracts upward, the other decomposes downward.

## Primary source
Zheng et al., 2023, *Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models*, arXiv:2310.06117. *(arXiv verified — HTTP 200 + title)*

## See also
- [least-to-most](least-to-most.md)
- [chain-of-thought](chain-of-thought.md)
