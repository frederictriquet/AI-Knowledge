---
title: "Directional Stimulus Prompting (DSP)"
type: "Concept"
theme: prompting
level: 🔴
source_url: https://www.ibm.com/think/topics/directional-stimulus-prompting
source_title: "What is directional stimulus prompting (DSP)?"
migrated_from: directional-stimulus-prompting
---

# Directional Stimulus Prompting (DSP)

**In one sentence** — train a small policy model that generates, per instance, stimuli (keywords, hints) steering a large frozen black-box LLM — you optimise the policy model, never the LLM.

## In detail
DSP addresses the problem of "black-box" LLMs (GPT-3/4, PaLM) accessible only through a text prompt. Rather than fine-tuning the large model, you train a small auxiliary policy model (T5, GPT-2) that produces directional stimuli tailored to each input. Training proceeds in two stages: supervised fine-tuning (SFT) on a small dataset associating each input with a pseudo-stimulus (keywords drawn from a reference summary, dialogue acts), then reinforcement-learning (RL) fine-tuning with a reward function (ROUGE/BLEU in summarisation). The target LLM stays frozen. Reported figures: +4% to +13% on a 4,000-sample subset of CNN/Daily Mail (summarisation), surpassing fully supervised models; +41.4% on MultiWOZ with only 80 dialogues (dialogue generation, ahead of ChatGPT, Codex, InstructGPT). Cited advantages: optimised resource usage, targeted attention. Drawbacks: dependence on precise stimuli, configuration complexity, limited generalisation.

## Example
CNN/Daily Mail summarisation task: rather than prompting the frozen LLM directly, the policy model emits, per article, a stimulus of the form `[Keywords: hurricane, evacuation, governor, casualties]`. These keywords are concatenated to the article before the call to the large model, which then produces a summary including those key points. The RL reward maximises the summary's ROUGE vs reference; the LLM is never touched. In MultiWOZ dialogue generation, the stimulus takes the form of dialogue acts (`request`, `inform`) that frame ChatGPT's response.

## Tradeoff / insight
The architectural trick: shifting the optimisation away from the costly LLM (impossible in black-box form) toward a cheap policy model. You get per-instance control without a gradient on the large model. Cost: an SFT+RL pipeline to train and maintain, plus fragility to domain shifts — the policy model does not generalise beyond its training distribution.

## Primary source
See Li et al. 2023, "Guiding Large Language Models via Directional Stimulus Prompting".

## See also
- [Prompt optimization](prompt-optimization.md)
- [tool grounding](tool-grounding.md)
