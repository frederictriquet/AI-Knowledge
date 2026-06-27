---
title: "Contextual Retrieval"
type: "Concept"
theme: evaluation
level: 🟡
source_url: https://www.anthropic.com/news/contextual-retrieval
source_title: "Introducing Contextual Retrieval — Anthropic"
objectives: [cost-control]
migrated_from: contextual-retrieval
---

# Contextual Retrieval

**In one sentence** — prefix each chunk with a short context (situating the chunk in its document) *before* embedding, to reduce retrieval failures caused by ambiguous chunks.

## The idea
Splitting a document destroys context: a chunk "revenue grew by 3%" says neither which company nor which quarter it concerns, and embeds poorly. Contextual Retrieval asks an LLM to generate, for each chunk, one or two sentences resituating it within the full document, then prefixes the chunk with this context before computing the embedding and the BM25 index. Retrieval thus operates on *self-contained* chunks. Prompt caching makes passing the entire document affordable.

## Example
Raw chunk: "The company's revenue grew by 3% over the previous quarter." — unusable in isolation. The contextualising prompt ("give a short succinct context to situate this chunk within the overall document") produces the prefix: "This chunk is from an SEC filing on ACME corp's performance in Q2 2023; the previous quarter's revenue was $314 million." Cumulative results on top-20 retrieval failures (baseline 5.7%): contextual embeddings alone −35% (→ 3.7%), +contextual BM25 −49% (→ 2.9%), +reranking −67% (→ 1.9%). Indexing cost: $1.02 per million tokens of documents thanks to prompt caching.

## Tradeoff / when to use it
Markedly reduces retrieval failures on fragmented corpora (reports, contracts). Cost: one contextualising LLM call per chunk at indexing time. Combinable with a reranker to stack the gains. Favour it when isolated chunks lose their meaning.

## Primary source
Anthropic, 2024, *Introducing Contextual Retrieval* (engineering blog post; no arXiv).

## See also
- [reranking](reranking.md)
- [agentic-chunking](agentic-chunking.md)
