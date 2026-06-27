---
type: index
title: "Theme — Memory"
theme: memory
---

# 💾 Memory

> ⚙️ **Generated file** by `tools/build_index.py` — do not edit by hand.

_Short/long-term memory and persistence across sessions._

## Concepts (5)

### 🔴 Substance / core
- **[Generative Agents — memory stream](../concepts/generative-agents-memory-stream.md)** — a timestamped log of observations, re-read through a score combining **recency + importance + relevance**; the scoring function is the transferable idea for agent memory.
- **[MemGPT (Letta)](../concepts/memgpt.md)** — manage an LLM's memory like an operating system: paging between a limited "RAM" context and an external "disk" store, with the model deciding for itself what to load.

### 🟡 Tradeoff / intermediate
- **[Entity / graph-based memory](../concepts/entity-memory.md)** — structure long-term memory as a **graph of entities and relations** (who / what / link) rather than a plain vector store.
- **[Episodic / semantic / procedural memory](../concepts/episodic-semantic-procedural-memory.md)** — three subtypes of long-term memory modeled on psychology: traces of lived events (episodic), structured facts (semantic), automated know-how (procedural).

### 🟢 Overview / introductory
- **[Short-term vs long-term memory](../concepts/short-vs-long-term-memory.md)** — short-term memory is the context window/buffer of the current session; long-term memory is a persistent external store read back on demand.

## Tools (10)

- **[Cavemem](../tools/cavemem.md)** — _MCP server / CLI (+ IDE hooks)_
- **[Chroma (ChromaDB)](../tools/chroma.md)** — _Vector database (library + server + Cloud SaaS)_
- **[GraphMind](../tools/graphmind.md)** — _Desktop application / MCP server / CLI_
- **[LanceDB](../tools/lancedb.md)** — _Embedded open-source vector database (Apache 2.0) + cloud/Enterprise_
- **[Milvus](../tools/milvus.md)** — _Open-source distributed vector database (Apache 2.0) + managed cloud (Zilliz)_
- **[pgvector](../tools/pgvector.md)** — _Open-source PostgreSQL extension (vector search)_
- **[Pinecone](../tools/pinecone.md)** — _Web service (managed vector database, proprietary)_
- **[Qdrant](../tools/qdrant.md)** — _Open-source vector database (Apache 2.0, Rust) self-host + managed cloud_
- **[turbopuffer](../tools/turbopuffer.md)** — _Web service (serverless vector + full-text search, proprietary)_
- **[Weaviate](../tools/weaviate.md)** — _Open-source vector database (BSD-3, Go) self-host + managed cloud_
