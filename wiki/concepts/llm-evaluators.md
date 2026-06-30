---
title: "LLM-evaluators (LLM judges) — Eugene's view"
type: "Concept"
theme: evaluation
level: 🟡
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_title: "Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)"
objectives: [reliability]
---

# LLM-evaluators (LLM judges) — Eugene's view

**In one sentence** — a synthesis of two dozen papers on LLM-as-a-Judge: when and how to use them, their known biases, and how to align them with human criteria.

## What the source says
An **LLM-evaluator** is an LLM that judges the quality of another LLM's response. Their adoption is growing out of necessity: classic evals (n-grams, semantic similarity, gold reference) poorly distinguish outputs on open-ended tasks (long summary, translation, multi-turn dialogue). Eugene structures the decision around three axes: (i) **direct scoring vs pairwise comparison**, (ii) **correlation vs classification metrics**, (iii) **LLM API vs fine-tuned evaluator model**. The prerequisite question is the **baseline**: the usual target is for the LLM-human correlation to equal the human-human correlation; vs human annotators, an LLM-evaluator is much faster and cheaper. He details prompting techniques (zero-shot, CoT, cross-examination "LM vs LM" to detect factual errors), alignment with idiosyncratic criteria (EvalLM), and the fine-tuning of evaluators (Shepherd on llama-2-7b). Above all, he documents the measured **biases** (MT-Bench / Chatbot Arena): **position bias** (preference for the first position), **verbosity bias** (long answers preferred >90% of the time), and **self-enhancement bias** (preference for its own outputs).

## Example
On MT-Bench, the biases are quantified. Position bias: in pairwise, `claude-v1` prefers the answer in first position 70% of the time, `gpt-3.5` 50%. Verbosity bias: you ask gpt-4 to rephrase an answer without adding information then concatenate it to the original — `claude-v1` and `gpt-3.5` then prefer the longer version in >90% of cases. Self-enhancement bias: `gpt-4` favors itself with a win-rate of +10%, `claude-v1` +25%. Hence the countermeasure: swap the order of the answers and average the two passes.

## Why it matters
Eugene provides a **critical literature review** on LLM-as-a-judge: the decision trees (scoring vs pairwise), the baselines to compare against, and above all the mapping of biases to neutralize — the rigor that separates a reliable judge from a misleading one.

## Decision tree
The central deliverable of the post is a decision tree ("mental model") that guides the choice of evaluator type and metric. Eugene warns that it is a useful simplification as a starting point.

1. **Is the task objective or subjective?**
   - **Objective** (factuality, toxicity, instruction following) → **direct scoring**: the better answer of a pair may still be flawed, and you do not need an alternative to compare against.
   - **Subjective** (tone, persuasion, writing style) → **pairwise comparison**, more reliable.
2. **If direct scoring, can the task be reduced to binary (true/false)?**
   - **Yes (binary)** → classification metrics (recall, precision) or Cohen's κ.
   - **No (Likert scale)** → correlations: Spearman's ρ, Kendall's τ.
3. **If pairwise comparison** → Cohen's κ; and if you are very confident in the ground truth, consider classification metrics (recall on the correct choice of the pair).
4. **Evaluator in development, or guardrail in production?**
   - **Development** (a few hundred samples, latency/cost of an LLM API tolerable) → prompt an LLM API with **CoT + n-shot** for reliability.
   - **Guardrail in production** (low latency, high throughput) → consider **fine-tuning a classifier or a reward model**, bootstrapped on open-source data and labels collected internally.

## Key points
- 3 choices: direct scoring vs pairwise; correlation vs classification; API vs fine-tuned.
- Aim for: LLM-human correlation ≈ human-human correlation.
- Biases to correct: position, verbosity, self-enhancement.
- Techniques: CoT, cross-examination, alignment with criteria (EvalLM).
- Warning about **fine-tuned** evaluators: expensive, and above all they behave like **task-specific classifiers** ("On the Limitations of Fine-tuned Judge Models"). They beat gpt-4 in-domain but generalize poorly: changing the evaluation scheme (e.g. from pairwise to direct scoring) causes a catastrophic drop, and they fail on fairness (below chance on LLMBar), factuality, toxicity, safety. Fine-tuning is only worth it as a production guardrail (low latency/high throughput) or when recall/precision remain insufficient in prompting (Shepherd, Prometheus).

## See also
- [LLM-as-a-judge](llm-as-a-judge.md)
- [LLM-as-a-judge done right](llm-as-judge-correct.md)
- [full post](../../sources/eugene-yan/md/llm-evaluators.md)
