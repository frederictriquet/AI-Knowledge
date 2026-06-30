---
title: "Least-to-Most prompting"
type: "Concept"
theme: reasoning-planning
level: 🟡
source_url: https://arxiv.org/abs/2205.10625
---

# Least-to-Most prompting

**In one sentence** — you explicitly decompose a problem into subproblems ordered from simplest to most complex, then solve them in sequence, each answer serving as context for the next.

## The idea
Least-to-Most proceeds in two phases. First a **decomposition** phase: the model lists the subquestions needed, from the most elementary to the most dependent. Then a **sequential solving** phase: each subproblem is solved by reinjecting the previous answers into the prompt. Unlike CoT, which reasons "in one block," the dependency is made explicit and chained, which helps on problems harder than the examples seen in few-shot.

## Example
On SCAN (compositional generalization, length split where test sequences exceed those seen), code-davinci-002 goes from 16.2% with chain-of-thought to 99.7% with least-to-most, using only 14 demonstrations. The gap widens with complexity: on last-letter concatenation, at 4 words 94.0% vs 84.2%, but at 12 words 74.0% vs 31.8% — CoT collapses as soon as the instance exceeds the length of the examples, where sequential decomposition holds.

## Tradeoff / when to use it
Improves **compositional generalization**: you solve instances longer/more complex than the demonstrations. Cost: several calls and a correct decomposition (a bad decomposition propagates the error). To favor when the problem naturally breaks into dependent steps (parsing, symbolic reasoning, multi-stage math). Less useful for atomic or non-decomposable tasks, where the orchestration overhead does not pay off.

## Primary source
Zhou et al., 2022, *Least-to-Most Prompting Enables Complex Reasoning in Large Language Models*, arXiv:2205.10625. *(arXiv verified — HTTP 200 + title)*

## See also
- [chain-of-thought](chain-of-thought.md)
- [step-back](step-back.md)
