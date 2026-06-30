---
title: "RAPTOR"
type: "Concept"
theme: rag-context
level: 🟡
source_url: https://arxiv.org/abs/2401.18059
---

# RAPTOR

**In one sentence** — recursive *hierarchical* clustering and summarization of chunks (a tree), allowing retrieval at different levels of abstraction.

## The idea
Flat chunks capture only local details: a question that requires connecting several passages fails. RAPTOR groups chunks by similarity, summarizes each cluster with an LLM, then starts again on these summaries — recursively building a **tree** whose leaves are the raw text and whose upper nodes are increasingly abstract syntheses. Retrieval queries the whole tree: depending on the question, you retrieve either a detail (leaf) or an overview (high node).

## Example
The clustering is not k-means but a **soft clustering via Gaussian Mixture Models**: UMAP reduces the dimensionality of the embeddings, varies `n_neighbors` to surface first global then local clusters, and a node can belong to several clusters. At query time, the *collapsed tree* variant (tree flattened into a single layer, ~top-20 nodes within a 2000-token budget) beats layer-by-layer traversal. Results: QuALITY rises from 62.3% to **82.6%** with GPT-4, and QASPER reaches 55.7% F1, ahead of CoLT5 XL (53.9%).

## Tradeoff / when to use it
Useful for multi-passage or thematic questions over long documents, where flat chunking loses the thread. Cost: building the tree (LLM summarization calls at indexing) and extra storage. Lighter than GraphRAG since there is no entity extraction, but less structured for relational queries.

## Primary source
Sarthi et al., 2024, *RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval*, arXiv:2401.18059. *(arXiv verified — HTTP 200 + title)*

## See also
- [graphrag](graphrag.md)
- [strategies-de-chunking](chunking-strategies.md)
