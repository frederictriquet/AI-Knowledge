---
title: "In-context learning (ICL)"
type: "Concept"
theme: prompting
level: 🔴
source_url: https://www.ibm.com/think/topics/in-context-learning
source_title: "What is in-context learning?"
migrated_from: in-context-learning
---

# In-context learning (ICL)

**In one sentence** — an LLM's ability to learn a task from the demonstrations placed in its prompt, with no update to its weights.

## In detail
ICL conditions an LLM on a prompt containing k input-output pairs; the model infers the task and applies the same mapping to a new input, computing argmax P(yⱼ | x, C) — the parameters stay unchanged. Zero/one/few-shot and CoT are techniques internal to ICL, not distinct from it. Two theoretical framings coexist: ICL as Bayesian inference (the model deduces a latent concept and grows more confident as examples are added) and ICL as implicit gradient descent (transformers internally simulate learning, demonstrated on linear regression). Note: even random labels improve performance — the format and distribution of the prompt matter as much as the labels. Limits: prompt sensitivity, dependence on model scale and pretraining quality, bias, privacy. "Context engineering" extends ICL to agentic systems.

## Example
Wireless network intrusion detection without retraining: GPT-4 is fed a few labeled traces (normal traffic vs attack) directly in the prompt, via three strategies — illustrative, heuristic, interactive — enriched with domain-specific questions. Tested on a real dataset covering 9 DDoS attack types, precision and F1 climb to around 90%, and beyond 95% with just 10 in-context examples. Specialized TAL variant: on aviation safety reports, an example selection by BM25 reaches ~80.24% precision and 84.15% F1 with just 8 examples.

## Tradeoff / insight
The fact that random labels work (the model mainly learns the format and the class space, not the exact mapping) reframes few-shot debugging: a failure often comes from a bad format or example order, not from wrong labels. ICL is an adaptation at inference — powerful, but unstable and not persistent from one query to the next.

## Primary source
"Language Models are Few-Shot Learners" (the founding GPT-3 paper, Brown et al. 2020) — the paper that introduces ICL.

## See also
- [few-shot-prompting](few-shot-prompting.md)
- [zero-shot-prompting](zero-shot-prompting.md)
- [prompt-tuning](prompt-tuning.md)
