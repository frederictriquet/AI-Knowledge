---
title: "Reasoning models & test-time compute"
type: "Concept"
theme: reasoning-planning
level: 🔴
source_url: https://arxiv.org/abs/2501.12948
objectives: [cost-control]
migrated_from: inference-time-scaling
---

# Reasoning models & test-time compute

**In one sentence** — gain quality by letting the model "think longer" at inference rather than by growing its weights.

## The idea
The classic scaling axis was the size of the model and of the training data. *Inference-time scaling* shifts the compute budget toward **inference**: the model produces long internal reasoning chains, explores several paths, corrects itself, before answering. Reasoning models (o1/o3 at OpenAI, DeepSeek-R1) are trained by reinforcement to exploit this budget. Snell et al. show that, for a given budget, spending at test-time can outperform a much larger model.

## Example
DeepSeek-R1-Zero, trained by pure RL without SFT, sees its pass@1 on AIME 2024 climb from 15.6% to 71.0% over training (86.7% with majority vote over 64 samples, on par with o1-0912). The length of the reasoning chains grows spontaneously from a few hundred to several thousand tokens, and an "aha moment" emerges: mid-solution the model interrupts itself with "Wait, wait. Wait. That's an aha moment" before re-evaluating its approach. The final DeepSeek-R1 reaches 97.3% on MATH-500 and a Codeforces rating of 2,029 (top 3.7% of humans).

## Tradeoff / when to use it
Valuable on deep-reasoning tasks (math, code, planning) where a correct answer is worth the overhead. Drawback: **far higher latency and cost per request**, verbose output, small gains on simple tasks. Reasoning models represent an evolution subsequent to classic prompting approaches.

## Primary source
OpenAI, 2024, *o1* (product announcement); DeepSeek-AI, 2025, *DeepSeek-R1*, arXiv:2501.12948 *(arXiv verified — HTTP 200 + title)*; Snell et al., 2024, *Scaling LLM Test-Time Compute Optimally*, arXiv:2408.03314 *(arXiv verified — HTTP 200 + title)*.

## See also
- [process-reward-models](process-reward-models.md)
- [react](react.md)
