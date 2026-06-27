---
title: "HyDE (Hypothetical Document Embeddings)"
type: "Concept"
theme: rag-context
level: 🟡
source_url: https://arxiv.org/abs/2212.10496
migrated_from: hyde
---

# HyDE (Hypothetical Document Embeddings)

**In one sentence** — generate a *hypothetical* answer to the question, then search for documents close to that answer (and not to the question) to improve zero-shot retrieval.

## The idea
A question and a relevant document often live in different regions of the embedding space: the question is short and interrogative, the document is long and assertive. HyDE first asks the LLM to *write* a plausible answer — even partially wrong — then encodes this **hypothetical document** and uses it as the vector query. Retrieval is therefore document-against-document, aligning the distributions and better capturing semantic relevance, with no labeled training data.

## Example
The generator prompt is minimal: "Please write a passage to answer the question. Question: [Q]. Passage:", varied by domain ("scientific paper passage to support/refute the claim" for SciFact, or in Swahili/Korean for Mr.TyDi). On TREC DL19, HyDE backed by unsupervised Contriever lifts nDCG@10 from 44.5 to 61.3 and recall@1k from 74.6 to 88.0. The gain explodes cross-lingually: Japanese MRR@100 from 19.5 to 30.7, Korean from 22.3 to 30.6 — without any labeled data.

## Tradeoff / when to use it
Excellent in zero-shot or on domains/languages where no reranker is trained. Cost: one extra LLM call before each search (latency, price) and a risk if the hypothesis hallucinates off-topic. Favor it when the raw query retrieves poorly and fine-tuning the retriever is out of reach.

## Primary source
Gao et al., 2022, *Precise Zero-Shot Dense Retrieval without Relevance Labels* (HyDE), arXiv:2212.10496. *(arXiv verified — HTTP 200 + title)*

## See also
- [reranking](reranking.md)
- [rag-agentique](rag-agentique.md)
