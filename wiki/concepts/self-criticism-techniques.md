---
title: "Self-criticism techniques"
type: "Concept"
theme: prompting
level: 🔴
source_url: https://arxiv.org/abs/2406.06608
source_title: "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques"
objectives: [reliability]
---

# Self-criticism techniques

**In one sentence** — have the model evaluate, verify and correct its own output, looping if needed, to make the answer more reliable without human intervention.

## What the source says
The Self-Criticism family (§2.2.5) rests on the idea that it is useful for LLMs to critique their own outputs: a simple judgment (is the answer correct?) or feedback used to improve the answer. Self-Calibration (Kadavath et al.) replays the question with the model's answer and asks whether it is correct, to gauge confidence. Self-Refine (Madaan et al.) is an iterative framework: the model produces an answer, generates feedback on it, then improves it, until a stopping condition. Reversing Chain-of-Thought / RCoT (Xue et al.) reconstructs the problem from the generated answer and compares to detect inconsistencies turned into feedback. Self-Verification (Weng et al.) generates several CoT solutions then scores them by masking parts of the question. Chain-of-Verification / COVE (Dhuliawala et al.) generates verification questions, answers them, then produces a revised answer. Cumulative Reasoning (Zhang et al.) generates steps, has the LLM accept or reject them, and iterates until the final answer.

## Example
COVE (Dhuliawala et al.) unfolds in four steps: the model answers, generates a list of verification questions targeting the facts in its own answer, answers them one by one independently, then produces a revised answer in light of those checks — which reduces factual hallucinations in QA. Self-Verification (Weng et al.) proceeds differently: it samples several CoT solutions, then masks part of the original statement and asks the model to reconstruct it from the candidate solution; a solution that lets the masked information be recovered is scored higher. Gains reported across eight reasoning datasets.

## Why it matters
This family covers the whole span of self-verification and self-revision (Self-Refine, COVE, Self-Verification, Cumulative Reasoning), where the model loops on its own output to correct it.

## Key techniques
- Self-Refine (Madaan et al.) — feedback then improvement loop until stop.
- Self-Verification (Weng et al.) — scoring CoT solutions by masking the question.
- Chain-of-Verification / COVE (Dhuliawala et al.) — verification questions then revised answer.
- Self-Calibration (Kadavath et al.) — re-question to gauge confidence.
- Reversing Chain-of-Thought / RCoT (Xue et al.) — problem reconstruction to detect inconsistencies.
- Cumulative Reasoning (Zhang et al.) — accepted/rejected steps in a loop.

## See also
- [Chain-of-Thought](chain-of-thought.md)
- [Agent self-reflection](self-reflection-agents.md)
- [full paper](https://arxiv.org/abs/2406.06608)
