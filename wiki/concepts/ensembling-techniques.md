---
title: "Ensembling techniques"
type: "Concept"
theme: prompting
level: 🔴
source_url: https://arxiv.org/abs/2406.06608
source_title: "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques"
---

# Ensembling techniques

**In one sentence** — Solve the same problem through several prompts/reasoning paths, then aggregate the outputs (often by majority vote) to reduce variance, at the cost of N calls.

## What the source says
Ensembling (§2.2.4) consists of using several prompts to solve the same problem, then aggregating the answers into a final output, most often by majority vote. The report states that these techniques reduce output variance and often improve accuracy, but increase the number of model calls. Self-Consistency (Wang et al.) samples several CoT paths at non-zero temperature then takes a majority vote. Universal Self-Consistency (Chen et al.) delegates the selection of the majority answer to a prompt rather than a programmatic count, useful for free text. DiVeRSe (Li et al.) creates several prompts, applies Self-Consistency to each and scores the reasoning paths. Mixture of Reasoning Experts / MoRE (Si et al.) combines experts specialized by reasoning type and selects via an agreement score. Max Mutual Information Method (Sorensen et al.) picks the template that maximizes prompt-output mutual information. USP (Wan et al.) generalizes COSP via unlabeled data. Prompt Paraphrasing (Jiang et al.) rephrases a prompt to produce ensemble variants.

## Example
MoRE (Si et al.) makes the "experts per reasoning type" idea very concrete: the same model is instantiated with specialized prompts — retrieval-augmented for factual questions, Chain-of-Thought for multi-hop and math, generated-knowledge for commonsense — then the best answer is kept via an agreement score. Universal Self-Consistency shows the other side: instead of counting votes programmatically (impossible on free text where "Paris" and "the city of Paris" are the same answer), all outputs are fed back into a prompt that itself designates the majority answer.

## Why it matters
This family details a whole range of aggregators (Universal Self-Consistency, DiVeRSe, MoRE, Max Mutual Information, USP, Prompt Paraphrasing) and explicitly frames the cost ×N versus robustness tradeoff.

## Key techniques
- Self-Consistency (Wang et al.) — multiple CoT paths then majority vote.
- Universal Self-Consistency (Chen et al.) — majority selection by prompt.
- DiVeRSe (Li et al.) — Self-Consistency per prompt then path scoring.
- Mixture of Reasoning Experts / MoRE (Si et al.) — specialized experts, choice by agreement.
- Max Mutual Information Method (Sorensen et al.) — template maximizing mutual information.
- USP (Wan et al.) — generalization of COSP via unlabeled data.
- Prompt Paraphrasing (Jiang et al.) — rephrasings for ensembling.

## See also
- [Self-Consistency](self-consistency.md)
- [full paper](https://arxiv.org/abs/2406.06608)
