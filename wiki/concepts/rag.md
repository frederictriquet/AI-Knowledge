---
title: "RAG (Retrieval-Augmented Generation)"
type: "Concept"
theme: evaluation
level: 🟢
source_url: https://www.ibm.com/think/topics/agentic-rag
source_title: "What is agentic RAG?"
objectives: [production]
---

# RAG (Retrieval-Augmented Generation)

**In one sentence** — instead of answering from its training memory alone, the LLM **retrieves relevant passages from an external store** and injects them into the context to ground its answer on sources.

## The idea
RAG fixes three limitations of the LLM alone: knowledge **frozen** at the training date (→ fresh/private info), **hallucinations** (→ answer grounded on verifiable sources), and **no access to business data** (→ queryable without retraining). The canonical flow:

```
Question → [Retrieval] relevant passages → [Augmentation] injected into the prompt
→ [Generation] the LLM answers based on them (+ citations)
```

Retrieval most often relies on **semantic search**: documents are split into *chunks*, encoded as **embeddings** stored in a vector database; the question is vectorized in turn and the closest chunks (top-K) are retrieved.

## The building blocks
| Block | Role |
|---|---|
| **Chunking** | Split the docs ([strategies](chunking-strategies.md): fixed, recursive, semantic, [agentic](agentic-chunking.md)) |
| **Embeddings + vector store** | Index for similarity search |
| **Retriever** | Bring back the top-K passages (often + a [reranking](reranking.md)) |
| **Generation** | The LLM composes the answer from the retrieved context |

## Example
Typical enterprise case: an HR chatbot wired to the internal document base. An employee asks "how many days of paternity leave?"; the embedding model vectorizes the question, FAISS surfaces the chunks of the collective agreement, the LLM composes the grounded answer — without retraining, on private data never seen at training time. The IBM source spins the image: static RAG is the employee who perfectly executes a framed task but takes no initiative; agentic RAG is the proactive team that decides to look elsewhere, reformulates, and cross-references several sources.

## Tradeoff / insight
"Classic" RAG is **static**: a single retrieval → generation pass, with no initiative. Quality depends entirely on retrieval — bad chunking or an off-topic top-K sinks the answer, with no way for the model to recover. This is precisely what the variants address: [agentic RAG](agentic-rag.md) places an agent *in front of* retrieval (deciding to search, reformulating, iterating, routing), and [corrective RAG](corrective-rag.md) adds a *grader* that rejects weak passages and falls back to web search. The overhead (tokens, latency) is justified only against multiple sources or complex queries; for a single source and simple questions, static RAG suffices.

## RAG: product feature ≠ to build yourself
RAG is an **orchestration architecture, never a model capability** — hence a frequent confusion depending on the point of view:

| Layer | RAG? |
|---|---|
| The **model** (Claude, GPT) via the raw API | ❌ no RAG by default — **you** build the pipeline (chunking, embeddings, vector store, retriever) |
| The **product** (Claude.ai, ChatGPT, Projects, web search) | ✅ RAG is **already wired by the app**; the end user has nothing to build or prompt |

In other words: on Claude.ai you *benefit* from RAG without knowing it (the app retrieves and injects the passages before calling the model); on the API you start from a blank page. The model itself never tells the difference — it receives ordinary context.

**Nuance**: not everything a consumer app does is RAG. A **small file** is often pasted whole into the context (*context stuffing*, no semantic search); **real RAG** only kicks in when the corpus exceeds the context window. The switch happens on **size** — RAG exists precisely because you cannot put everything in the context.

## See also
- [Agentic RAG](agentic-rag.md) — an agent in front of retrieval
- [Corrective RAG (cRAG)](corrective-rag.md) — grader + web fallback
- [Chunking strategies](chunking-strategies.md) · [Source verification](source-verification.md)
- [HyDE](hyde.md) · [GraphRAG](graphrag.md) · [Reranking](reranking.md) · [Contextual Retrieval](contextual-retrieval.md)
