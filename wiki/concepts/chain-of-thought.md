---
title: "Chain-of-Thought (CoT)"
type: "Concept"
theme: reasoning-planning
level: 🟢
source_url: https://www.ibm.com/think/topics/chain-of-thoughts
source_title: "What is chain-of-thought (CoT) prompting?"
---

# Chain-of-Thought (CoT)

**In one sentence** — asking the model to write its intermediate reasoning steps before the final answer, instead of answering directly.

## In detail
CoT is a prompt-engineering technique that breaks a complex problem into sequential logical steps, improving arithmetic, symbolic and common-sense reasoning. The user typically appends an instruction at the end of the prompt ("describe your reasoning steps"). CoT is an emergent capability that appears with model size; instruction tuning, however, lets smaller models (Granite Instruct) practise it. Several variants exist: zero-shot CoT (no examples), auto-CoT (automatic generation of the steps), multimodal CoT (text + image) and "self-consistency". Limitations: increased compute cost, need for high-quality prompts, risk of plausible-but-incorrect paths, and difficulty of evaluation.

## Example
Zero-shot, on the riddle "What is the capital of a country bordering France whose flag is red and white?": without CoT the model jumps to a plausible answer and often gets it wrong; with CoT it chains bordering countries → filter for a red-and-white flag → Switzerland → Bern. On the equation `x² − 5x + 6 = 0`, the explicit trace (factoring, roots) leads to `x = 3` and `x = 2` rather than an asserted result. The downside highlighted: a verbose but wrong path ("flawed concept") remains possible — the trace impresses without guaranteeing correctness.

## In agents
On the agent side, CoT is not a standalone technique but the **reasoning building block of ReAct**: the thought→action→observation loop relies on a chain of thought. Note: CoT alone increases the risk of **hallucination**, mitigated by external grounding (tool observations); ReAct "greatly benefits from highly capable models".

## Tradeoff / insight
CoT trades compute cost (generated tokens) for reliability and observability on multi-step tasks. The trap: verbose, plausible reasoning is not correct reasoning — the trace is not a proof. On recent models already trained to reason, the explicit instruction adds less, and can even degrade simple tasks. The state-of-the-art insight: CoT only truly emerges on large models; on small models it often degrades the answer (except with instruction tuning, cf. Granite Instruct).

## Primary source
Wei et al. 2022, "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models".

## See also
- [Tree of Thoughts (ToT)](tree-of-thoughts.md)
- [Self-Consistency](self-consistency.md)
- [ReAct](react.md)
