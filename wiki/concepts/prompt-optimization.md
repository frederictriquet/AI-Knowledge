---
title: "Prompt optimization"
type: "Concept"
theme: prompting
level: 🟡
source_url: https://www.ibm.com/think/topics/prompt-optimization
source_title: "What is prompt optimization?"
---

# Prompt optimization

**In one sentence** — automatically (or semi-automatically) refining existing prompts through iteration, metric-based evaluation, and feedback loops, to be distinguished from manual prompt engineering, which designs them from scratch.

## In detail
The contrast is between prompt engineering (designing a structure from scratch: few-shot, CoT, metaprompts) and prompt optimization (refining and tuning an original prompt over several runs with metrics). The typical process: evaluate the reference prompt, measure the outputs (human judgment or metrics), adjust clarity/structure/length, test on a representative set, and create a reusable template or metaprompt. Strategies mentioned: template design, CFPO (joint content + format optimization), few-shot + CoT, LLM-driven metaprompts, and PROMST (PRompt Optimization in Multi-Step Tasks) for multi-step workflows. Choi (2025) introduces a confusion-matrix-based tuning framework that improves relevance while limiting token usage. Named tools: PromptLayer ("Git for prompts," versioning, A/B testing) and Humanloop (structured human feedback). Pitfalls: lack of precision, overloading a single prompt, inconsistent formatting, skipping iterations, ignoring the audience.

## Example
Customer support at scale: rather than a single prompt, you derive variants indexed on the problem type AND the detected sentiment (furious customer vs simple billing question), each optimized separately. Targeted result: faster resolution, compliance with internal policies, and lower token cost because outputs are shorter and more targeted. Explicit anti-pattern from the source: overloading a single prompt with multiple tasks, tones, and instructions — the model "gets lost" and returns fragmented answers; and mixing few-shot formats (how the examples are presented) breaks quality.

## Tradeoff / insight
Prompt optimization is warranted when latency, accuracy, or token cost become critical at scale. It shifts the work from manual craft to a measurable pipeline (logs, metrics, A/B). Limitation: optimizing against a proxy metric can overfit the evaluation set and break at deployment — the metric is not the task.

## Primary source
Only Choi (2025, confusion matrix) is named; CFPO and PROMST are mentioned without a resolved reference.

## See also
- [DSPy](dspy.md)
- [Meta-prompting](meta-prompting.md)
