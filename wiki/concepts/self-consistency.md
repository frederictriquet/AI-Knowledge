---
title: "Self-Consistency"
type: "Concept"
theme: reasoning-planning
level: 🟡
source_url: https://www.ibm.com/think/topics/prompt-engineering-techniques
source_title: "Prompt engineering techniques"
migrated_from: self-consistency
---

# Self-Consistency

**In one sentence** — sample several independent CoT reasoning chains then take a majority vote for the final answer, rather than relying on a single generation.

## In detail
Self-consistency designates a principle that "uses the model to generate multiple independent proposals and identify the most coherent and accurate answer," useful for reasoning or interpretation tasks. It is one of the advances over CoT, ensuring "the logical integrity of the generated paths." In the context of ToT, the self-consistency mechanism "provides reliable evaluations by prompting the model several times."

## Example
On the "explain climate change" task, the IBM prompt instantiates self-consistency: `Provide three different explanations of climate change, its causes, and its effects. Then identify the most coherent and clear explanation`. The model produces three distinct explanations in a single call, then selects the most logical itself. This is a "low-cost" approximation of true self-consistency from Wang et al. (N independent samples + external vote): here, generation and arbitration fit in a single prompt, with no programmatic aggregation.

## Tradeoff / insight
Self-consistency trades an inference cost multiplied by N (N samples) for a reduction in variance: the majority vote absorbs the aberrant chains. It applies cleanly only to tasks with an aggregatable final answer (a number, a label); on free text, "voting" becomes an open problem. Diminishing returns kick in quickly beyond a few dozen samples.

## Primary source
Wang et al. 2022, "Self-Consistency Improves Chain of Thought Reasoning in Language Models."

## See also
- [Chain-of-Thought (CoT)](chain-of-thought.md)
- [Tree of Thoughts (ToT)](tree-of-thoughts.md)
