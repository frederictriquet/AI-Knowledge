---
title: "Evaluating LLMs (task-specific evals)"
type: "Concept"
theme: evaluation
level: 🔴
source_url: https://eugeneyan.com/writing/evals/
source_title: "Task-Specific LLM Evals that Do & Don't Work"
objectives: [reliability]
---

# Evaluating LLMs (task-specific evals)

**In one sentence** — Off-the-shelf evals correlate poorly with application performance; Eugene proposes concrete evals, calibrated per task (classification, summarization, translation, toxicity), without ever giving up human evaluation.

## What the source says
The actual post is "Task-Specific LLM Evals that Do & Don't Work": most generic evals are neither discriminating nor correlated with production performance. Eugene details evals that work per task — **classification/extraction** (recall, precision, ROC-AUC, PR-AUC, distribution separation), **summarization** (Kryscinski's four dimensions: factual consistency via NLI, relevance, fluency, coherence; reference-based evals like ROUGE work poorly), **translation** (statistical and learned evals, reference-based and reference-free, leaning on WMT), and **toxicity** (RealToxicityPrompts, BOLD, Perspective API at threshold p ≥ 0.5). He insists: **human evaluation remains the gold standard** for complex tasks and most automatic evals ultimately rest on human annotations. Finally, you must **calibrate the evaluation bar to the risk level**: aiming for near-perfection everywhere is unrealistic — the typical factual-inconsistency rate stays at 5-10% even after RAG and good prompting.

## Example
Voiceflow monitors its intent classification with an eval harness: migrating from `gpt-3.5-turbo-0301` (deprecated) to `gpt-3.5-turbo-1106`, the harness detects a 10% performance drop that would have gone unnoticed without measurement. On the summarization side, an NLI model (document = premise, summary = hypothesis, drop the neutral then softmax over entailment/contradiction) fine-tuned on a few thousand FIB/USB samples raises the ROC-AUC of factual-inconsistency detection from 0.56 (near-random) to 0.85.

## Why it matters
Eugene brings **per-task business rigor**: which metrics to use, which fail (ROUGE for abstractive summarization), the use of NLI for consistency, active learning to enrich labels, and the pragmatism of calibrating the threshold to the real risk.

## Key points
- Off-the-shelf evals often fail: poorly discriminating.
- Classification: ROC-AUC, PR-AUC, distribution separation.
- Summarization: consistency (NLI), relevance, length — not ROUGE alone.
- Human evaluation stays indispensable and underpins automatic evals.
- Calibrate the bar to the risk; ~5-10% residual factual inconsistency.

## See also
- [Trajectory evaluation](trajectory-evaluation.md)
- [Why benchmarks matter](why-benchmarks-matter.md)
- [Error analysis](error-analysis.md)
- [full post](../../sources/eugene-yan/md/evals.md)
