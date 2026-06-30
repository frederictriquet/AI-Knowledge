---
title: "Prompt tuning (soft prompts)"
type: "Concept"
theme: prompting
level: 🔴
source_url: https://www.ibm.com/think/topics/prompt-tuning
source_title: "What is prompt tuning?"
---

# Prompt tuning (soft prompts)

**In one sentence** — a PEFT method that trains, by gradient descent, a small set of continuous vectors ("soft prompts" / virtual tokens) injected at the input, with the backbone kept frozen — not to be confused with textual prompt engineering.

## In detail
Prompt tuning adapts a frozen pre-trained model by learning a few trainable vectors (soft prompts), non-interpretable, that steer behavior without touching the weights. Only these parameters (often < 1% of the model) are updated by backpropagation, hence drastically reduced compute and storage costs and a "plug-and-play" modularity (one prompt file per task). The PEFT comparison ranks P-tuning v2 (~0.1-3% of parameters) as less expressive than LoRA (~0.1-1%) or adapters (~1-4%). Central expressive limitation: a formal analysis shows that prompt/prefix-tuning only adds a bias to the output of the attention blocks and does not modify the learned attention patterns — it combines existing skills but does not learn genuinely new tasks. Effectiveness depends on scale: competitive with full fine-tuning beyond 10 billion parameters. On Granite 3-8B for review classification, prompt tuning achieves ~98% accuracy versus ~93% for the base model, i.e. ~+5%.

## Example
Sentiment analysis on a frozen 175B model: you initialize 20 virtual tokens, vectors living in the same 12,288-dimensional space as the vocabulary. The input "The movie was absolutely fantastic!" becomes internally `[<v1>, <v2>, ... <v20>, The, movie, was, absolutely, fantastic, !]`. Backpropagation updates only these 20 vectors (a few thousand parameters), never the 175B weights. To switch to spam detection, you train a new soft-prompt file and swap it in at inference — without duplicating the model.

## Tradeoff / insight
The trap is believing that "tuning the prompt" learns new capabilities: no, the soft prompt only re-elicits and combines what the backbone already knows. For genuinely novel reasoning patterns, you need LoRA or full fine-tuning. On the ops side, the soft prompt weighs a few KB against 350 GB for a full copy of a 175B model — modularity is the decisive argument, not raw performance.

## Caveats
The formal analysis of the expressive limitation and the PEFT figures (P-tuning v2, LoRA, adapters) lack a reproducible arXiv reference.

## See also
- [in-context-learning](in-context-learning.md)
- [rag-vs-fine-tuning-vs-prompt-engineering](rag-vs-fine-tuning-vs-prompt-engineering.md)
