---
title: "LLM-as-a-judge: doing it right"
type: "Concept"
theme: evaluation
tags: [evaluation, llm-judge, alignment]
level: 🔴
source_url: https://hamel.dev/blog/posts/llm-judge/
source_title: "Using LLM-as-a-Judge For Evaluation: A Complete Guide — Hamel Husain"
objectives: [reliability]
migrated_from: llm-as-judge-correct
---

# LLM-as-a-judge: doing it right

**In one sentence** — an LLM-as-a-judge is only valuable if it is aligned with the binary pass/fail judgment of a domain expert through an iterative protocol ("Critique Shadowing"), not through arbitrary 1-5 scores.

## What the source says
Teams drown under unmanageable metrics: too many measures, uncalibrated scales (1-5), no domain expert, and unvalidated metrics. The proposed solution is **Critique Shadowing**, a 7-step process: (1) find *the* **Principal Domain Expert**, (2) create a diverse dataset (features, scenarios, personas), (3) have the expert issue **binary pass/fail judgments accompanied by a written critique** explaining the reasoning, (4) fix the errors found, (5) build the **LLM judge** iteratively with **few-shot** examples drawn from the expert's critiques, (6) run an **error analysis** by dimension and root cause, (7) create specialized judges if needed. You iterate the prompt until **convergence** with the expert (at Honeycomb: > 90% agreement in only three iterations). Key claimed point: the real value comes not from the judge itself but from looking closely at your data.

## Example
A B2C eval scenario: the user asks "Where is my order?" while having three active orders (#123, #124, #125) — the assistant should disambiguate rather than assume. The domain expert judges the answer **pass/fail** and first writes a critique ("did not ask which number, assumed the most recent"), which then becomes a few-shot example in the judge's prompt. You iterate the prompt until convergence with the expert: at Honeycomb, > 90% judge/human agreement is reached in only three iterations. The verdict stays binary — no 1-5 scale, judged non-actionable.

## Why it matters
This guide provides the complete rigorous protocol (7 steps, the expert's role, critique-then-score, judge/human agreement measurement), which turns an idea into reproducible engineering practice.

## Takeaways
- **Align the judge with human labels**: everything starts from the Principal Domain Expert's judgments, not generic metrics.
- **Critique-then-score**: write a detailed critique first, then the verdict; these critiques serve as few-shot examples for the judge's prompt.
- **Binary rather than Likert**: pass/fail only at the start; 1-5 scales are non-actionable and correlate poorly with the expert's judgment.
- **Measure judge/human agreement**: use precision/recall (not raw agreement, misleading with imbalanced classes); aim for convergence (e.g. > 90% agreement in 3 iterations).
- **Iterate**: refine the prompt by hand until convergence, re-evaluate on any material change (e.g. a model change).
- **"Benevolent dictator"**: a single decision-making expert to guarantee consistency, never a complacency proxy.
- **~30 examples** to start, until you no longer see new failure modes.
- **Error analysis**: error rate per feature/scenario/persona, classification of root causes, on unseen data only.
- The judge is only a "hack": the real value comes from careful analysis of the data.

## See also
- [LLM-as-a-judge](llm-as-a-judge.md)
- [Self-criticism techniques](self-criticism-techniques.md)
- [error analysis](error-analysis.md)
- [full post](../../sources/hamel-husain/md/llm-judge.md)
- [Eugene Yan — LLM-evaluators](llm-evaluators.md) (complementary — *choosing/evaluating* a judge)
