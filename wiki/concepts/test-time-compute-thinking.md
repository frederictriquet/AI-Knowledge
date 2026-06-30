---
title: "Test-time compute: \"thinking\" as inference-time computation"
type: "Concept"
theme: reasoning-planning
level: 🔴
source_url: https://lilianweng.github.io/posts/2025-05-01-thinking/
source_title: "Why We Think"
---

# Test-time compute: "thinking" as inference-time computation

**In one sentence** — "thinking" is not a metaphor: it is allocating more FLOPs at inference, with chain-of-thought letting the model use a variable amount of computation depending on the difficulty of the problem.

## What the source says
Weng frames reasoning around three motivations: the psychological analogy (Kahneman's System 1 / System 2), **computation as a resource** (in a Transformer, ~2× the number of parameters per token; CoT multiplies this computation by each response token) and latent-variable modeling (the thought trace z as a hidden variable). At decoding time she distinguishes **parallel sampling** (best-of-N, beam search, self-consistency, guided by a Process Reward Model) and **sequential revision** (iterative self-correction, which does not work natively without external feedback — Huang et al. 2024). On the training side, **RL for reasoning** culminates with o1/o3 and the DeepSeek-R1 report (2025), where a simple policy gradient with rule-based rewards (format + correctness) makes reflection and backtracking emerge ("aha moment") even in pure RL without SFT; the DeepSeek team also reports the failure of PRMs and MCTS. Weng finally covers **latent reasoning** (recurrent architectures à la Geiping et al. 2025, thinking/pause tokens, Quiet-STaR) and the scaling laws (Snell et al. 2024: test-time compute does not replace a good base model on hard problems).

## Example
R1's "aha moment" is documented: under pure RL, the model spontaneously starts spending more and more thinking tokens over training, and learns to re-read itself ("reflecting on previous mistakes") then to try another approach. On the failure side, PRM stumbles on the impossibility of defining per-step rubrics and becomes vulnerable to reward hacking; MCTS fails because the search space over language tokens is gigantic compared to chess, and the fine-grained value model is unmanageable to train. Open-R1, SimpleRL-reason and TinyZero (all on Qwen) reproduced the emergence in pure RL on math.

## Why it matters
It frames test-time compute as a new scaling dimension and makes explicit the o1/R1 recipe and its failures, an angle little covered by sources centered on agent frameworks.

## Primary sources (cited by Weng)
- DeepSeek-AI, *DeepSeek-R1* (2025)
- Wei et al., *Chain-of-thought prompting* (2022)
- Snell et al., *Scaling LLM Test-Time Compute Optimally* (2024)
- Lightman et al., *Let's Verify Step by Step* (PRM, 2023)
- Zelikman et al., *STaR: Bootstrapping Reasoning With Reasoning* (2022)

## See also
- [Reasoning models & test-time compute](inference-time-scaling.md) · [Process Reward Models](process-reward-models.md)
- [Chain-of-Thought](chain-of-thought.md)
- [full post](../../sources/lilian-weng/md/2025-05-01-thinking.md)
