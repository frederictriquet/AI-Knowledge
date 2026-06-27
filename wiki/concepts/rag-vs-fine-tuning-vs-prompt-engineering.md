---
title: "RAG vs fine-tuning vs prompt engineering"
type: "Concept"
theme: rag-context
level: 🟡
source_url: https://www.ibm.com/think/topics/rag-vs-fine-tuning-vs-prompt-engineering
source_title: "RAG, fine-tuning, and prompt engineering"
objectives: [production]
migrated_from: rag-vs-fine-tuning-vs-prompt-engineering
---

# RAG vs fine-tuning vs prompt engineering

**In one sentence** — a comparison of the three levers for optimizing an LLM across four axes (approach, goals, resources, applications), presented as complementary and often combined.

## In detail
Three methods are compared. Prompt engineering optimizes the input prompts without significantly modifying the parameters; it is the least costly, doable manually with no extra compute, ideal for open-ended situations (content generation). RAG connects the LLM to a database and enriches the prompts via semantic search on vector stores; it requires data expertise to build the pipelines, and shines when precise, current information matters most (customer-service chatbots). Fine-tuning retrains the model on a labeled, domain-specific dataset, updating its weights; it is the most demanding in time and compute (GPU). A distinction is made between full fine-tuning and PEFT (parameter-efficient fine-tuning), as well as fine-tuning (labeled data, targeted expertise) vs continued pre-training (transfer learning on unlabeled data).

## Example
The source details the RAG flow in four steps on a user query. 1) Query: the user submits their question, which kicks off the system. 2) Retrieval: algorithms or APIs comb through internal and external knowledge bases (semantic search on a vector store, not keyword-based). 3) Integration: the retrieved data is concatenated to the query and passed to the LLM — which has not processed anything yet. 4) Response: the LLM combines retrieved context + trained knowledge to generate a suitable answer. Fine-tuning, by contrast, is supervised learning on labeled data that updates the weights.

## Tradeoff / insight
The real trade-off is not "which to choose" but "in what order to stack them": start with prompt engineering (zero cost), move to RAG when the problem is a deficit of fresh knowledge, reserve fine-tuning for deficits of behavior or format that context does not fix. The cook metaphor (adviser / recipe book / cooking class) sums it up well: knowledge vs access vs skill.

## Primary source
Conceptual page with no academic reference.

## See also
- [Agentic RAG](rag-agentique.md)
- [prompt-tuning](prompt-tuning.md)
- [prompt-engineering](prompt-engineering.md)
