---
title: "Vector memory: MIPS & ANN"
type: "Concept"
theme: rag-context
level: 🔴
source_url: https://lilianweng.github.io/posts/2023-06-23-agent/
source_title: "LLM Powered Autonomous Agents"
migrated_from: memoire-vectorielle-mips-ann
---

# Vector memory: MIPS & ANN

**In one sentence** — an agent's long-term memory is implemented as a maximum inner product search (MIPS) over a vector store, accelerated by approximate nearest neighbor (ANN) algorithms.

## What the source says
Weng maps long-term memory onto an external vector store the agent queries at request time, working around the Transformer's finite attention span. The standard practice is to store embedding representations in a vector database supporting fast **Maximum Inner Product Search (MIPS)**. For speed, one relies on **approximate nearest neighbor (ANN)** algorithms, which trade a little accuracy for a massive speedup. Weng details five algorithms: **LSH** (Locality-Sensitive Hashing, a hash function mapping nearby items into the same buckets); **ANNOY** (random projection trees); **HNSW** (Hierarchical Navigable Small World, hierarchical graphs inspired by "small world" networks); **FAISS** (vector quantization by clustering, Facebook); and **ScaNN** (anisotropic vector quantization). She points to ann-benchmarks.com for comparisons.

## Example
HNSW makes the speed/accuracy tradeoff concrete. Inspired by social networks' "six degrees of separation", it stacks "small world" graphs: search starts at a random node in the top layer and moves toward the target; when stuck, it drops down a layer, until the bottom layer that holds the actual points. Each hop at the top covers a large distance in data space, each hop at the bottom refines. ScaNN, for its part, does not pick the nearest centroid: its anisotropic quantization preserves the inner product `⟨q, x_i⟩` rather than raw distance — exactly what MIPS optimizes.

## Why it matters
Weng goes down to the concrete algorithmic level of vector memory: MIPS, the ANN accuracy/speed tradeoff, and five named implementations — a depth of engineering rarely covered in general RAG overviews.

## Primary sources (cited by Weng)
- Maximum Inner Product Search (MIPS) — formulation of memory retrieval.
- LSH (Locality-Sensitive Hashing) and ANNOY (Spotify) — hashing and random projection trees.
- HNSW (Malkov & Yashunin) — hierarchical "small world" graphs.
- FAISS (Facebook AI) and ScaNN (Google, anisotropic quantization).

## See also
- [Short-term vs long-term memory](short-vs-long-term-memory.md)
- [Episodic / semantic / procedural memory](episodic-semantic-procedural-memory.md)
- [full post](../../sources/lilian-weng/md/2023-06-23-agent.md)
