---
title: "Agent self-reflection (ReAct, Reflexion, CoH, AD)"
type: "Concept"
theme: reasoning-planning
level: 🔴
source_url: https://lilianweng.github.io/posts/2023-06-23-agent/
source_title: "LLM Powered Autonomous Agents"
---

# Agent self-reflection (ReAct, Reflexion, CoH, AD)

**In one sentence** — the family of mechanisms by which an agent improves in a loop by revisiting its past decisions and errors, essential in real-world tasks where trial and error is unavoidable.

## What the source says
Self-reflection is essential for an agent to improve iteratively. **ReAct** (Yao et al. 2023) interleaves reasoning and action by extending the action space to discrete actions plus the language space, following the `Thought / Action / Observation` template repeated; it beats the `Act`-only baseline. **Reflexion** (Shinn & Labash 2023) adds dynamic memory and self-reflection on an RL framework with binary reward: a heuristic function detects inefficient trajectories or hallucinations (repeated identical actions) and can reset the environment; the reflections (up to three) are injected into working memory. **Chain of Hindsight** (CoH; Liu et al. 2023) presents the model with a sequence of its past outputs annotated with human feedback, via supervised fine-tuning, so it learns to produce better. **Algorithm Distillation** (AD; Laskin et al. 2023) applies the same idea to multi-episode RL trajectories, distilling the learning process itself.

## Example
Concretely, Reflexion's self-reflection is built from two few-shot examples, each a pair (failed trajectory, ideal reflection to fix the plan), then injected as context. On AlfWorld and HotpotQA, the diagnosis distinguishes two failure modes: on AlfWorld, hallucination — defined as a series of identical actions leading to the same observation — is more frequent than inefficient planning (a too-long trajectory without success). For AD, the telling detail: 2 to 4 episodes of multi-episode context suffice to learn a near-optimal in-context RL algorithm, and AD approaches RL^2 while using only offline RL.

## Why it matters
These four techniques (ReAct, Reflexion, CoH, AD) belong to the same "learn from your mistakes" lineage, whose internal mechanisms differ (heuristic, binary reward, fine-tuning on history).

## Primary sources
- Yao et al. 2023 — "ReAct: Synergizing Reasoning and Acting in Language Models" (ICLR 2023).
- Shinn & Labash 2023 — "Reflexion: an autonomous agent with dynamic memory and self-reflection."
- Liu et al. 2023 — "Chain of Hindsight Aligns Language Models with Feedback."
- Laskin et al. 2023 — "In-context Reinforcement Learning with Algorithm Distillation" (ICLR 2023).

## See also
- [Reflexion](reflexion.md)
- [ReAct](react.md)
- [full post](../../sources/lilian-weng/md/2023-06-23-agent.md)
