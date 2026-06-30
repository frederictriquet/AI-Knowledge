---
title: "Speculative decoding"
type: "Concept"
theme: efficiency-cost
level: 🟡
source_url: https://arxiv.org/abs/2211.17192
objectives: [cost-control]
---

# Speculative decoding

**In one sentence** — a small "draft" model proposes several tokens, the large model VERIFIES them in one pass; speeds up inference without changing the output distribution.

## The idea
Autoregressive generation is sequential: one token per pass of the large model, hence slow. Speculative decoding has a small **draft** model propose a burst of k candidate tokens, which the large **target** model validates in a single parallel pass. A probabilistic acceptance test accepts the longest coherent prefix and rejects the rest. Key guarantee: the output distribution remains **exactly** that of the large model alone — this is acceleration, not approximation.

## Example
Paper measurements (Table 2) with **T5-small (77M)** as draft and **T5-XXL (11B)** as target. WMT EnDe translation in argmax (T=0): **3.4×** speedup, γ=7 tokens proposed per pass, acceptance rate α=0.75; in sampling (T=1) the gain drops to 2.6× because α=0.62. CNN/DM summarization: 3.1× (γ=5, α=0.65) in argmax, 2.3× in sampling. The speedup tracks α directly: a poorly aligned draft collapses the gain despite the parallelism.

## Tradeoff / when to use it
Speeds up latency (often 2-3×) without touching quality. The gain depends on the **acceptance rate**: you need a draft sufficiently aligned with the target, otherwise rejections cancel the benefit. Costs memory (two models) and implementation complexity; transparent to the user, it is an inference-infrastructure lever.

## Primary source
Leviathan et al., 2023, *Fast Inference from Transformers via Speculative Decoding*, arXiv:2211.17192 *(arXiv verified — HTTP 200 + title)*; Chen et al., 2023, *Accelerating Large Language Model Decoding with Speculative Sampling* (DeepMind).

## See also
- [model-routing-cascades](model-routing-cascades.md)
- [inference-time-scaling](inference-time-scaling.md)
