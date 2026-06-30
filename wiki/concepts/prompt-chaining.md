---
title: "Prompt chaining"
type: "Concept"
theme: prompting
level: 🟡
source_url: https://www.ibm.com/think/topics/prompt-chaining
source_title: "What is prompt chaining?"
objectives: [code-generation]
---

# Prompt chaining

**In one sentence** — breaking a complex task into a sequence of simple prompts where the output of each step feeds the next.

## In detail
Prompt chaining links several prompts together to produce a coherent, controllable output. The method starts from the simple-prompts / complex-prompts contrast and proposes a decomposition (identify the goal, split it into sub-tasks, one prompt per sub-task, test, iterate), illustrated by a Spanish→English→extraction→Spanish translation case. Benefits: consistency (tone, style, format), tighter control, reduced error rate. A LangChain tutorial enumerates nine sub-types: sequential, branched (branches), iterative, hierarchical, conditional, multimodal, dynamic, recursive, inverse — with a decision grid (complexity, dependency, adaptability, modality). It implements a customer-feedback processing pipeline (keyword extraction → sentiment summary → refinement) with watsonx.ai and granite-3-8b-instruct, via PromptTemplate, LLMChain, and SequentialChain.

## Example
The source walks through the decomposition of a complex prompt ("Consider the Spanish text, translate it to English, extract all statistics and facts as bullets, translate them back to Spanish") into five chained simple prompts: 1) "Read the given Spanish text," 2) "Translate the text to English," 3) "Retrieve the statistics and facts from the text," 4) "Create a bulleted list of all these facts," 5) "Translate them to Spanish." Each output feeds the next prompt: isolating each step reduces the risk of errors that a monolithic prompt would compound.

## Tradeoff / insight
Chaining trades LLM calls for reliability: each isolated step hallucinates less, but latency and cost multiply, and errors propagate in cascade. Technical caveat: this tutorial uses `LLMChain` / `SequentialChain`, the deprecated legacy LangChain API — for a 2026 guide, prefer LCEL (LangChain Expression Language) and `Runnable`. For agentic workflows, decoupling planning from execution connects to patterns like ReWOO.

## See also
- [ReWOO](rewoo.md)
- [chain-of-thought](chain-of-thought.md)
