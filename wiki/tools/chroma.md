---
tool: "Chroma (ChromaDB)"
title: "Chroma (ChromaDB)"
themes: [rag-context, memory]
type: "Vector database (library + server + Cloud SaaS)"
url: https://www.trychroma.com/products/chromadb
pricing_model: "Open-source (Apache 2.0) self-hosted free + Chroma Cloud (freemium / usage-based / Team / Enterprise)"
llm_cost: "No LLM inference — stores/indexes supplied embeddings (BYOK for embedding generation)"
objectives: [production]
family: "RAG infrastructure / vector databases"
eco_icons: "🔓🎁💳"
llm_cost_icons: "🟢"
summary: "Open-source vector database (Apache 2.0) for RAG / semantic search; self-hosted free or Chroma Cloud serverless (free Starter + usage, Team $250/month+). Stores embeddings, does not generate them (BYOK)"
---

# Chroma (ChromaDB)

**In one sentence** — open-source vector database ("search infrastructure for AI") to store and query embeddings at scale, the foundation of RAG and semantic-search applications.

## Type & integration
**An infrastructure building block**, not an agent tool. Variants:
- **Self-hosted**: single-node install via `pip`, `npm` or Docker, in-memory or persistent.
- **Chroma Cloud**: managed serverless service (GA since v1.4.1).
- **Enterprise / BYOC**: self-managed deployment in the client's VPC.

Same Apache 2.0 codebase for open-source and cloud → no vendor lock-in. Unified search: **vector + full-text + regex + metadata** (hybrid). Integrates as a RAG store in LLM apps (LangChain, LlamaIndex, Python/JS SDK).

## Pricing model
- **Open-source self-hosted**: free (Apache 2.0).
- **Chroma Cloud**: **Starter $0/month + usage** (serverless, ~$5 free credits); **Team $250/month** (+ usage, ~$100 credits included); **Enterprise** on quote with BYOC. Usage rates (verified): Write ~$2.50/GiB, Storage ~$0.33/GiB-month, Query ~$0.0075/TiB, Network ~$0.09/GiB.

A classic "open-core / managed cloud" model: the paid value is managed hosting, not a closed version of the engine.

## LLM cost
**No LLM inference** 🟢 from Chroma: it **stores and indexes embeddings**, it does not **generate** them. You supply pre-computed vectors (semantic, BM25, SPLADE…). Embedding generation happens separately: via an **external embeddings API** (OpenAI, Voyage, Cohere… → **BYOK** usage cost) or a local model (free).

→ In your grid: Chroma's own cost is **infrastructure** (cloud storage/compute), distinct from the LLM cost. The only potential "model" cost is embeddings, outside Chroma.

## What it's for
The retrieval engine of a RAG system: index documents (as embeddings + metadata) and retrieve relevant passages to feed an LLM's context. Used by AI teams in production (Capital One, Cisco, Intel cited).

## Notes
- Difference from the "token-reduction cluster" tools ([CodeGraph](codegraph.md), [Polaris (polarismcp.com)](polaris.md), [GraphMind](graphmind.md)): those **embed** their own specialized vector index for code; Chroma is the **generic vector database** on which you would build such a solution yourself.
- Competitors: Pinecone (proprietary/cloud), Weaviate, Qdrant, Milvus, pgvector.
- Self-hosted = zero cost but ops to manage; Cloud = simplicity vs usage cost.

## Source
- Product page: https://www.trychroma.com/products/chromadb · site: https://www.trychroma.com/
- 2026 pricing comparisons: pecollective, modern-datatools

*(verified on 2026-06-15 — official product page + web search)*
