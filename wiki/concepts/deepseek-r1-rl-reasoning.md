---
title: "DeepSeek-R1: RL makes reasoning emerge"
type: "Concept"
theme: reasoning-planning
level: 🔴
source_url: https://arxiv.org/abs/2501.12948
source_title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
---

# DeepSeek-R1: RL makes reasoning emerge

**In one sentence** — Applied directly to a base model, reinforcement learning (RL) without supervised fine-tuning is enough to make long reasoning chains and self-verification emerge spontaneously.

## What the source says
The authors introduce DeepSeek-R1-Zero, trained by large-scale RL directly on DeepSeek-V3-Base, without any prior supervised fine-tuning (SFT) step. Through RL, the model naturally "emerges" with strong reasoning behaviours — self-verification, reflection (revisiting and re-evaluating its own steps), and long chains of thought (CoT). It is the first open research to show that an LLM's reasoning abilities can be incentivized purely by RL. R1-Zero does suffer from poor readability and language mixing, though; the authors then introduce DeepSeek-R1, which adds a little "cold start" data and a multi-stage pipeline to reach performance comparable to OpenAI-o1-1217. On AIME 2024, R1-Zero's pass@1 rises from 15.6% to 71.0% over training (86.7% with majority voting).

## Example
The "aha moment" (Table 3 in the paper) illustrates the emergence: at an intermediate version of R1-Zero, mid-way through a problem, the model interrupts itself spontaneously — "Wait, wait. Wait. That's an aha moment I can flag here. Let me reevaluate this step by step" — reallocates thinking time and resumes its initial reasoning. Nobody taught it this self-correction behaviour: it emerges from reward incentives alone. The effect is measurable: on AIME 2024, pass@1 climbs from 15.6% to 71.0% over training (86.7% with majority voting).

## Why it matters
DeepSeek-R1 shows that reasoning is not only a matter of prompting (elicited chain-of-thought) but can be a learned, measurable and transferable behaviour. For a team building agents, this changes the foundation: you can now rely on reasoning models (and their open-source distilled versions) instead of rebuilding everything at the orchestration level.

## Key points
- **R1-Zero recipe**: pure RL applied to the base model, no SFT — evidence that reasoning is elicited by incentive, not by imitation.
- **GRPO** (Group Relative Policy Optimization): an RL algorithm that drops the critic (a model the same size as the policy) and estimates the baseline from the scores of a group of samples, which cuts cost.
- **Rule-based reward**: a correctness reward (deterministic verification: boxed answer for maths, compiler/tests for code) + a format reward (`<think>`/`</think>` tags). No neural reward model, to avoid reward hacking.
- **Self-evolution**: thinking time (response length) increases naturally during training; reflection and exploration of alternative approaches emerge without being programmed.
- **"Aha moment"**: at an intermediate version, the model learns to reallocate thinking time by re-evaluating its initial approach — a direct illustration of sophisticated behaviours emerging from RL.
- **Distillation**: distilling R1's reasoning into smaller dense models (1.5B → 70B, Qwen2.5/Llama3) outperforms applying RL directly to those small models. R1-Distill-Qwen-32B reaches 72.6% on AIME 2024.

## See also
- [Test-time compute](test-time-compute-thinking.md)
- [Reasoning models](inference-time-scaling.md)
- [Process Reward Models](process-reward-models.md)
- [paper](../../sources/frontier-reasoning/md/deepseek-r1.md)
