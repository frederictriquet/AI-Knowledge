---
title: "Semantic caching"
type: "Concept"
theme: efficiency-cost
level: 🟡
source_url: https://www.ibm.com/think/topics/agentic-rag
source_title: "What is agentic RAG?"
objectives: [cost-control]
---

# Semantic caching

**In one sentence** — cache queries, context and results by semantic similarity, used as an agent memory mechanism.

## In detail
Semantic caching belongs to the agent's **memory**, one of its three essential traits. An agent has short- and long-term memory that lets it plan and execute complex tasks, and refer to previous tasks to inform future workflows. It is precisely in this role that semantic caching fits: "Agentic RAG systems use semantic caching to store sets of previous queries, context and results and refer back to them." This mechanism is the concrete support of the agent's memory function in an agentic RAG pipeline.

## Example
A support agent has already handled "How do I reset my password?" and stored query + context + result in its semantic cache. Another user later types "I forgot my credentials, how do I log back in?": no string equality, but the two embeddings are neighbors, so the cache returns the pre-computed answer without re-running retrieval + generation. This is long-term memory at work: the agent "refers back to previous tasks" to inform the current workflow and avoid redoing the work.

## Tradeoff / insight
The term "semantic" is what distinguishes this cache from a classic key-value cache: matching is done by closeness of meaning (embeddings) and not by exact query equality. Advantage: two different phrasings of the same intent hit the same cache, saving a full retrieval + generation cycle. Risk: a semantic false positive serves a pre-computed answer to a subtly different query. The similarity threshold becomes a critical parameter to calibrate, exactly like the `SIMILARITY_THRESHOLD` of a scored retrieval.

## Primary source
"Agentic RAG systems use semantic caching to store sets of previous queries, context and results and refer back to them." ([source](https://www.ibm.com/think/topics/agentic-rag))

## See also
- [Agentic RAG](agentic-rag.md)
- [Agentic RAG subtypes](agentic-rag-subtypes.md)
