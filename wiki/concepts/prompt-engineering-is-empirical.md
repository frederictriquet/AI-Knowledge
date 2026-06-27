---
title: "Prompt engineering is empirical (case study)"
type: "Concept"
theme: prompting
level: 🔴
source_url: https://arxiv.org/abs/2406.06608
source_title: "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques"
migrated_from: prompt-engineering-est-empirique
---

# Prompt engineering is empirical (case study)

**In one sentence** — a real case study (detecting "entrapment" in suicide-risk texts) shows that prompt engineering is an iterative, sensitive, and poorly transferable process, where even reputed techniques do not always win.

## What the source says
The report (§6.2) documents an annotated case study: an expert prompt engineer attempts to detect entrapment in Reddit posts with gpt-4-turbo-preview. The process is entirely manual and trial-and-error: the model first ignores the concept, over-generates positive labels, sometimes refuses to answer. Some decisions that improve F1 turn out to be substantively wrong (restricting to explicit mentions when entrapment can be implicit). The discussion (§6.2.4) draws three lessons: prompt engineering differs from classical programming (you "cajole" the model, which is extremely sensitive to details for no apparent reason); you must dive into the data; and above all collaborate between the prompt engineer and domain experts. Case study §6.1 adds that technique selection resembles a hyperparameter search and that Zero-Shot-CoT can fall below Zero-Shot. Finally, DSPy (Khattab et al.) automatically optimizes the prompt and beats the human expert on the test, illustrating the promise of automation.

## Example
The "black art" shows up in a detail: the prompt engineer accidentally pastes the same context email twice — and this unintended duplicate markedly improves F1; removing the duplication makes it drop, and anonymizing the proper names in the email degrades it further (an effect reminiscent of the Re-reading technique). Conversely, DSPy (BootstrapFewShotWithRandomSearch, gpt-4-0125-preview, 16 iterations) bootstraps a prompt of 15 exemplars + one reasoning demonstration on its own and reaches 0.548 F1 / 0.385 precision / 0.952 recall on the test, without resorting to either the email or the erroneous instruction about explicitness — beating the human.

## Why it matters
Provides a substantiated methodological lesson: prompt engineering is empirical, finicky, and fragile, justifying rigorous evaluation and automation (DSPy-style) rather than trust in ready-made recipes.

## Key points
- Iterative, trial-and-error process; the model is "cajoled," not programmed.
- Extreme sensitivity to details for no apparent reason; low transferability across models/tasks.
- F1 gains can mask substantively bad decisions (explicit vs implicit).
- CoT does not always help: Zero-Shot-CoT sometimes falls below Zero-Shot.
- Technique selection = hyperparameter search; DSPy automates it and beats the expert on the test.
- Key recommendation: collaboration between prompt engineer and domain experts.

## See also
- [Prompt optimization](prompt-optimization.md)
- [DSPy](dspy.md)
- [What is prompt engineering](prompt-engineering.md)
- [full paper](../../sources/prompt-report/md/prompt-report.md)
