---
title: "Multi-agent debate / Society of Mind"
type: "Concept"
theme: multi-agent
level: 🔴
source_url: https://arxiv.org/abs/2305.14325
migrated_from: society-of-mind-debate
---

# Multi-agent debate / Society of Mind

**In one sentence** — have **several LLM instances debate**: each proposes an answer, critiques the others over several rounds, until converging on a more factual answer.

## The idea
Rather than a single (fallible) model, N agents generate independent answers then iterate by reading and critiquing the peers' proposals. The confrontation surfaces errors and improves factuality and reasoning. The name evokes Minsky's *Society of Mind* (intelligence emerging from simple agents); the modern instantiation on LLMs is "multiagent debate."

## Example
Paper setup: **3 agents**, **2 rounds** of debate (each agent rereads the others' answers and revises). Measured gains: arithmetic 67.0 → **81.8%**, GSM8K 77.0 → **85.0%**, biography generation 66.0 → **73.8%**, MMLU 63.9 → **71.1%**, chess move validity 29.3 → **45.2%**. Notable fact: the debate sometimes corrects cases where *all* agents started on a wrong answer — it is not a mere amplification of the initial consensus, the population converges on a shared, more correct answer.

## Tradeoff / when to use it
Improves factuality and reasoning on some tasks, but **costly** (N agents × several rounds). It is the conceptual ancestor of "judge panels" and adversarial verification. To be reserved for high-stakes-accuracy questions, not for throughput.

## Primary source
Du et al., 2023, *Improving Factuality and Reasoning in Language Models through Multiagent Debate*, arXiv:2305.14325. Founding concept: Minsky, *The Society of Mind*, 1986. *(arXiv verified — HTTP 200 + title)*

## See also
- [strategies-collaboration](collaboration-strategies.md)
- [llm-as-a-judge](llm-as-a-judge.md)
