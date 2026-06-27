---
title: "Mixture-of-Agents (MoA)"
type: "Concept"
theme: multi-agent
level: 🔴
source_url: https://arxiv.org/abs/2406.04692
primary_source: "arXiv:2406.04692"
migrated_from: mixture-of-agents
---

# Mixture-of-Agents (MoA)

**In one sentence** — stack **multiple LLMs in layers**: each layer of agents receives and aggregates the previous layer's responses, improving quality beyond the best single model.

## The idea
MoA organizes several models into successive layers. At each layer, "proposer" agents generate responses; the next layer takes all of them as input, aggregates and refines them, up to a final "aggregator" agent. Inter-model collaboration exploits the complementarity of heterogeneous LLMs: the collective outperforms the best single model, including on benchmarks like AlpacaEval. It is a depth-wise generalization of multi-agent debate.

## Example
The reference configuration (Together AI) stacks **3 layers** of six open-source proposers — Qwen1.5-110B/72B-Chat, LLaMA-3-70B-Instruct, WizardLM-8x22B, Mixtral-8x22B, dbrx-instruct — with Qwen1.5-110B-Chat as the final aggregator. Result on AlpacaEval 2.0: **65.1% LC win rate** vs **57.5%** for GPT-4 Omni (+7.6 pts), using only open models. The "Aggregate-and-Synthesize" prompt requires the aggregator to evaluate the responses critically ("some may be biased or incorrect") and not merely copy them.

## Tradeoff / when to use it
Relevant when **quality matters more than cost** and several complementary models are available. Cost: latency and number of calls multiplied by the number of layers and agents per layer. Pointless for throughput or simple tasks; a single call is preferable then.

## Primary source
Wang et al., 2024, *Mixture-of-Agents Enhances Large Language Model Capabilities*, arXiv:2406.04692 (Together AI). *(arXiv verified — HTTP 200 + title)*

## See also
- [Society of Mind / debate](society-of-mind-debate.md)
- [Collaboration strategies](collaboration-strategies.md)
