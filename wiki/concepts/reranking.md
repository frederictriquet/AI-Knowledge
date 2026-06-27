---
title: "Reranking (cross-encoders)"
type: "Concept"
theme: rag-context
level: 🟡
source_url: https://arxiv.org/abs/1901.04085
migrated_from: reranking
---

# Reranking (cross-encoders)

**In one sentence** — re-ranking the retrieved top-k passages with a cross-encoder (query and passage go *together* through the model); the most cost-effective quality lever in practice, at the price of latency.

## The idea
Vector retrieval encodes query and passages *separately* (bi-encoder), which is fast but coarse. A **cross-encoder** concatenates query and passage and runs them together through the model: cross-attention judges relevance finely, but prevents any pre-computation. It is therefore applied as a second stage: the retriever brings back a large top-k (≈100), the reranker re-sorts it to keep only the best. ColBERT offers a compromise (late interaction) between the two regimes.

## Example
The paper's pipeline on MS MARCO: BM25 brings back the **top 1000** passages, a BERT Large cross-encoder re-scores them by pairs (query + passage concatenated). MRR@10 on the dev set rises from **16.7** (BM25 alone) to **36.5** — i.e. +27% relative over the former best (IRNet, 27.8). On TREC-CAR, MAP climbs from 15.3 to 33.5. The retriever and index are unchanged: all the gain comes from the second stage.

## Tradeoff / when to use it
Often the most cost-effective quality gain of a RAG pipeline, without touching the retriever or the index. Cost: latency and compute proportional to the re-scored top-k; one call per pair. Add it as soon as the precision of the final top-5 matters.

## Primary source
Nogueira & Cho, 2019, *Passage Re-ranking with BERT*, arXiv:1901.04085 *(arXiv verified — HTTP 200 + title)*; ColBERT (Khattab & Zaharia, 2020); Cohere Rerank (product).

## See also
- [hyde](hyde.md)
- [rag-agentique](rag-agentique.md)
