---
title: "Entity / graph-based memory"
type: "Concept"
theme: memory
level: 🟡
source_url: https://arxiv.org/abs/2501.13956
source_title: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"
---

# Entity / graph-based memory

**In one sentence** — structure long-term memory as a **graph of entities and relations** (who / what / link) rather than a plain vector store.

## The idea
Instead of storing text chunks indexed by embedding, you extract **entities** (people, places, objects) and the **relations** that link them, forming a knowledge graph updated as interactions unfold. Retrieving a memory means traversing this graph, which preserves coherence over the long term: contradictory facts are reconciled at the entity level rather than duplicated across floating passages.

## Tradeoff / when to use it
Relevant for persistent assistants that must track **stable, connected facts** across many sessions. Cost: extracting and maintaining the graph adds calls and complexity; for purely semantic retrieval over documents, a vector store stays simpler.

## Primary source
No single canonical paper. Concept implemented in LangChain (entity memory), Zep/Graphiti and A-MEM (2024). Cited as such, without an invented arXiv identifier.

## See also
- [memgpt](memgpt.md)
- [memoire-court-long-terme](short-vs-long-term-memory.md)
