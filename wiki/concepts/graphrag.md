---
title: "GraphRAG"
type: "Concept"
theme: rag-context
level: 🔴
source_url: https://arxiv.org/abs/2404.16130
migrated_from: graphrag
---

# GraphRAG

**In one sentence** — build a knowledge graph and community summaries from the corpus, to answer the *global* questions that vector RAG fails to handle.

## The idea
Vector RAG retrieves a few chunks close to the query: perfect for a local factual question, useless for "what are the main themes of this corpus?". GraphRAG first extracts entities and relations with an LLM to build a **knowledge graph**, detects **communities** (hierarchical Leiden-style clustering), then pre-generates a summary per community. At query time, these summaries are aggregated into a global answer (map-reduce). You move from retrieval by similarity to retrieval by corpus *structure*.

## Example
On a podcast corpus (1,669 chunks of 600 tokens, ~1M tokens), GraphRAG extracts a graph of 8,564 nodes / 20,691 edges, hierarchized into communities (34 root summaries C0, up to 1,310 leaves C3). Faced with a global question like "Which episodes mostly deal with tech policy and regulation?", it wins 72–83% of pairwise duels on comprehensiveness and 75–82% on diversity against vector RAG (p<.001). The root C0 summaries answer with 97% fewer tokens (26,657 vs 1,014,611) than a summary of the raw source text.

## Tradeoff / when to use it
Indispensable for global synthesis and exploration of large thematic corpora. High indexing cost: many LLM calls to extract the graph and summarize the communities, plus maintenance on each update. Overkill for plain factual Q&A.

## Primary source
Edge et al., 2024 (Microsoft Research), *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*, arXiv:2404.16130. *(arXiv verified — HTTP 200 + title)*

## See also
- [raptor](raptor.md)
- [rag-agentique](rag-agentique.md)
