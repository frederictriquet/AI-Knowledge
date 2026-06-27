---
title: "Zero-shot prompting"
type: "Concept"
theme: prompting
level: 🟢
source_url: https://www.ibm.com/think/topics/zero-shot-prompting
source_title: "What is zero-shot learning?"
migrated_from: zero-shot-prompting
---

# Zero-shot prompting

**In one sentence** — asking an LLM to perform a task without providing any example, relying solely on its pre-trained knowledge.

## In detail
Zero-shot is a prompt engineering method where the model receives no example output. Illustrative example: granite-3-8b-instruct on a classification task (the urgency of an IT problem as "High / Medium / Low"), run in watsonx.ai Prompt Lab in Freeform mode. The components of a prompt: instruction, context, input data and output indicator (the latter optional). Advantages: simplicity, ease of use (no data required), flexibility. Limits: performance variability depending on task complexity, and a strong dependence on the quality of the pre-trained model. Two improvement levers: instruction tuning and RLHF. Applications: text classification, information extraction, question answering, summarization, generation, conversation.

## Example
Without any solved example, granite-3-8b-instruct is given the instruction "Define the class name for the described problem: High, Medium or Low", followed by only the definitions of the three classes, then the case "Problem: users report that they are unable to download files". The output indicator "Class:" primes the answer. The model infers **High** and justifies it: inability to download → many users blocked, high business cost. No demonstration was provided, only the definitions and the proper instruction/context/input split.

## Tradeoff / insight (for a senior)
Reynolds & McDonell (2021) showed that with a better prompt structure, zero-shot can outperform few-shot. In other words, adding examples is not always worthwhile; refining the wording of the instruction can be worth more than consuming context with demonstrations. Schulhoff et al. (2024) find different results — the debate remains open.

## Primary source
Reynolds and McDonell (2021), noting that zero-shot can outperform few-shot with better prompt structures; Schulhoff et al. (2024) as a counterpoint.

## See also
- [one-shot-prompting](one-shot-prompting.md)
- [few-shot-prompting](few-shot-prompting.md)
- [in-context-learning](in-context-learning.md)
