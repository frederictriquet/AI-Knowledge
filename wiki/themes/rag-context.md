---
type: index
title: "Theme — RAG & context"
theme: rag-context
---

# 📚 RAG & context

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Augmenting the model through retrieval and managing context._

## Concepts (15)

### 🔴 Substance / core
- **[GraphRAG](../concepts/graphrag.md)** — build a knowledge graph and community summaries from the corpus, to answer the *global* questions that vector RAG fails to handle.
- **[Self-RAG](../concepts/self-rag.md)** — an LLM trained to decide *when* to retrieve and to *self-critique* the relevance and factual support of what it retrieves and generates, via "reflection tokens."
- **[Systematically improving your RAG](../concepts/systematically-improving-rag.md)** — treat a RAG system as a measurable product that you improve through metric-driven iterations, not as a fixed recipe.
- **[Vector memory: MIPS & ANN](../concepts/vector-memory-mips-ann.md)** — an agent's long-term memory is implemented as a maximum inner product search (MIPS) over a vector store, accelerated by approximate nearest neighbor (ANN) algorithms.

### 🟡 Tradeoff / intermediate
- **[Agentic RAG](../concepts/rag-agentique.md)** — an agent placed in front of retrieval that decides whether to search, where to search, reformulates, and iterates, instead of a fixed reactive RAG pipeline.
- **[Agentic RAG subtypes](../concepts/agentic-rag-subtypes.md)** — four families of agents for RAG: routing, query planning, ReAct, and plan-and-execute.
- **[Agentic chunking](../concepts/agentic-chunking.md)** — an LLM splits the text by unit of meaning and tags each piece with metadata, instead of applying mechanical fixed-size cuts.
- **[Corrective RAG (cRAG)](../concepts/corrective-rag.md)** — an LLM grader scores the retrieved passages; if poor → fallback to web search (Tavily) + query rewriting, otherwise an explicit refusal rather than a hallucination.
- **[HyDE (Hypothetical Document Embeddings)](../concepts/hyde.md)** — generate a *hypothetical* answer to the question, then search for documents close to that answer (and not to the question) to improve zero-shot retrieval.
- **[LLM Wiki: an LLM-maintained wiki instead of RAG](../concepts/llm-wiki-karpathy.md)** — rather than re-synthesizing from raw sources on every question (classic RAG), you have the LLM maintain a **persistent wiki** (interconnected markdown): a *compiled* knowledge layer whose value accumulates with each ingested source.
- **[RAG vs fine-tuning vs prompt engineering](../concepts/rag-vs-fine-tuning-vs-prompt-engineering.md)** — a comparison of the three levers for optimizing an LLM across four axes (approach, goals, resources, applications), presented as complementary and often combined.
- **[RAPTOR](../concepts/raptor.md)** — recursive *hierarchical* clustering and summarization of chunks (a tree), allowing retrieval at different levels of abstraction.
- **[Reranking (cross-encoders)](../concepts/reranking.md)** — re-ranking the retrieved top-k passages with a cross-encoder (query and passage go *together* through the model); the most cost-effective quality lever in practice, at the price of latency.

### 🟢 Overview / introductory
- **[Chunking strategies](../concepts/chunking-strategies.md)** — four families of chunking, from the most mechanical (fixed size) to the most costly (semantic, agentic), to be chosen according to the document's structure.
- **[Reports over RAG (RAG as a feature, not a benefit)](../concepts/reports-over-rag.md)** — Liu predicts a shift from "question-answer" RAG toward **report generation**, because the value of a report (decision support) far exceeds the time saved finding an answer.

## Tools (0)

- _(aucun)_
