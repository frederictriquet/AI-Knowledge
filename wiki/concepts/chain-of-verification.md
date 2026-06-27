---
title: "Chain-of-Verification (CoVe)"
type: "Concept"
theme: reasoning-planning
level: 🟡
source_url: https://arxiv.org/abs/2309.11495
objectives: [code-generation, reliability]
---

# Chain-of-Verification (CoVe)

**In one sentence** — the model writes an answer, derives factual verification questions from it, answers them in isolation, then corrects its answer in light of those checks.

## The idea
CoVe structures self-verification in four steps: (1) generate a baseline answer, (2) plan **verification questions** targeting the asserted facts, (3) answer those questions independently — ideally without looking at the initial answer, to avoid repeating the error, (4) produce a revised final answer. Isolating the checks is key: it stops the model from simply re-justifying its hallucinations.

## Example
Query "Name some politicians born in New York" (Figure 1): the baseline answer lists Hillary Clinton, Donald Trump, Michael Bloomberg. CoVe plans one verification question per entity — "Where was Hillary Clinton born?" — answered in isolation: Chicago (Illinois), Boston (Massachusetts)... The model then drops Clinton and Bloomberg, keeps Trump and adds Ocasio-Cortez. On Wikidata list questions with Llama 65B, precision rises from **0.17 (few-shot) to 0.32 (CoVe factored)**; the factored variant, which does not re-condition on the initial answer, beats the joint one (0.29) because it does not copy the hallucination.

## Tradeoff / when to use it
Markedly reduces factual hallucinations, especially on entity lists and multi-fact questions. Cost: several extra calls and sub-prompt orchestration. Use it when factual accuracy is paramount and no external source of truth (search, database) is wired in; otherwise a RAG setup or an external grader will be more reliable. Like Self-Refine, the signal stays internal to the model, so it is bounded by the model's knowledge.

## Primary source
Dhuliawala et al., 2023, *Chain-of-Verification Reduces Hallucination in Large Language Models*, arXiv:2309.11495. *(arXiv verified — HTTP 200 + title)*

## See also
- [self-refine](self-refine.md)
- [reflexion](reflexion.md)
