---
title: "Few-shot prompting"
type: "Concept"
theme: prompting
level: 🟢
source_url: https://www.ibm.com/think/topics/few-shot-prompting
source_title: "What is few-shot learning?"
---

# Few-shot prompting

**In one sentence** — provide a few labeled examples in the prompt to guide the model, leveraging its pretrained knowledge without retraining.

## In detail
Few-shot presents several examples of the task in the prompt (e.g. sentiment classification "positive / negative"). One notable pipeline: examples are stored in a vector database, and at query time the system does semantic matching to retrieve the most relevant examples — this is RAG applied to example selection, not systematically required but beneficial. Several research frameworks are relevant: SetFit (Tunstall et al., efficient fine-tuning of sentence-transformers), UPT / Unified Prompt Tuning (Feihu Jin et al.), TransPrompt (transferable cross-task prompting), and QaNER for NER. Note: an "empty prompt" (no example, no template) can reach competitive accuracy. Limits: dependence on prompt quality, computational complexity, hard generalization, limited zero-shot abilities.

## Example
Sentiment classification: you provide in the prompt a few texts labeled "positive" / "negative", then ask to classify "This product is very profitable". The full pipeline stores all examples in a vector database; at query time, semantic matching retrieves the closest demonstrations (RAG over the example bank) and assembles them into the prompt before passing it to the LLM. Conversely, the cited study shows that an "empty prompt" — just "What is the sentiment of the following text?", with no example or template — already reaches competitive accuracy.

## Tradeoff / insight
The practical insight: example selection matters as much as their number. Coupling few-shot with a vector search (RAG over the example bank) dynamically adapts the demonstrations to each query, which outperforms a fixed set of examples. The flip side: you spend context budget and add a retrieval infrastructure — to weigh against plain instruction tuning.

## Primary source
Cited frameworks: SetFit (Lewis Tunstall et al.), Unified Prompt Tuning / UPT (Feihu Jin et al.), TransPrompt, QaNER; without DOI/arXiv resolved in the source.

## See also
- [in-context-learning](in-context-learning.md)
- [zero-shot-prompting](zero-shot-prompting.md)
