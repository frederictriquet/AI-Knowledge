---
title: "Self-Refine"
type: "Concept"
theme: reasoning-planning
level: 🟡
source_url: https://arxiv.org/abs/2303.17651
objectives: [reliability]
migrated_from: self-refine
---

# Self-Refine

**In one sentence** — a single model produces an output, generates its own critique, then revises, in a loop, with no external signal.

## The idea
Self-Refine is a generate → critique → refine loop driven by a single LLM through three prompts. The model produces an initial answer, gives itself detailed and actionable **feedback** on its own output, then rewrites incorporating that feedback. It iterates until convergence or budget exhaustion. All the improvement signal comes from the model itself: no code execution, no environment, no human.

## Example
Task "sum from 1 to N": the initial output is a loop `for i in range(n+1): res += i`. The model generates its own feedback — "slow, brute-force code; use the formula n(n+1)/2" — then rewrites it as `return (n*(n+1))//2`. With GPT-4, the absolute per-task gains are spectacular outside math: Dialogue Response **+49.2** (25.4 → 74.6%), Sentiment Reversal **+32.4**, Constrained Generation **+30.0**, but Math Reasoning only **+0.2** (92.9 → 93.1%) — blind self-critique does not fix what the model cannot verify.

## Tradeoff / when to use it
Real gains on writing quality, readability or constraint compliance, with no infrastructure. But self-critique without external grounding plateaus fast and can reinforce the model's errors (it doesn't know what it doesn't know). To be distinguished from Reflexion, which leverages an **environment signal** (test failure, reward): Self-Refine refines "blindly," Reflexion learns from an objective signal. Use Self-Refine when no external verifier exists.

## Primary source
Madaan et al., 2023, *Self-Refine: Iterative Refinement with Self-Feedback*, arXiv:2303.17651. *(arXiv verified — HTTP 200 + title)*

## See also
- [reflexion](reflexion.md)
- [chain-of-verification](chain-of-verification.md)
