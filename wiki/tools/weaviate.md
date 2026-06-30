---
tool: "Weaviate"
title: "Weaviate"
themes: [rag-context, memory]
type: "Open-source vector database (BSD-3, Go) self-host + managed cloud"
url: https://weaviate.io/
pricing_model: "Open-source (BSD-3-Clause) + Weaviate Cloud (freemium + usage-based)"
llm_cost: "🟢 BYO embeddings; BYOK vectorizers or hosted Weaviate Embeddings (per token)"
objectives: [production]
family: "RAG infrastructure / vector databases"
eco_icons: "🔓🎁💳"
llm_cost_icons: "🟢"
summary: "**Open-source BSD-3 (Go)**, 'batteries-included': hybrid dense+BM25 search, built-in vectorizers and generative search. Free self-host or Weaviate Cloud (Free → Flex $45 → Plus $280…, billed by stored dimensions). HNSW **in RAM** = the sizing factor"
---

# Weaviate

**In one sentence** — an **open-source vector database (BSD-3, written in Go)**, "batteries-included": hybrid dense+BM25 search, built-in vectorizer and generative-search modules, self-hosted or in the managed cloud.

## Type & integration
A self-hostable open-source core **AND** a managed **Weaviate Cloud** service. Interfaces: REST (CRUD), GraphQL and **gRPC** (high-performance search/batch). Modules: vectorizers, generative (`generative-openai`…), rerankers. Multi-tenancy (one shard per tenant). **In-memory HNSW** index → RAM is the sizing factor.

## Pricing model
**Open-source BSD-3-Clause** (free self-host). **Weaviate Cloud** — pricing reworked on 2025-10-27 (the old Standard/Professional tiers are obsolete). Current tiers (starting from, vary by cloud/region):
- **Free** (sandbox), then **Flex** $45/month, **Plus** $280, **Premium** $400, **Dedicated** (~$400+, on quote).
- Billing on 3 axes: **stored vector dimensions** (e.g. $0.0039–0.0047/M dim/month by tier), disk storage, backups.

## LLM cost
**🟢** Four options: (1) **BYO-vectors** (you supply the vectors, no cost on Weaviate's side); (2) **BYOK vectorizers** (`text2vec-openai/cohere/huggingface` — your provider key, billed by the provider); (3) **Weaviate Embeddings**, hosted models **billed by Weaviate per token** ($0.025–0.065/M tokens, Cloud only); (4) **local models** (`text2vec-transformers`, `-ollama`, self-host, compute only). The database itself bills no inference in BYO mode.

## What it's for
When you want an open-source vector database with **mature hybrid search** and built-in RAG/generative without assembling it yourself. Good DX.

## Notes
- **HNSW in RAM** memory constraint (the main bottleneck); resharding is costly/discouraged → size the RAM upfront. Mitigation: quantization (PQ, binary).
- Positioning: hybrid search + built-in modules. Vs [Qdrant](qdrant.md) (Rust, performance/filtering, lighter), [Milvus](milvus.md) (distributed scale), [Pinecone](pinecone.md) (managed proprietary).

## Source
https://weaviate.io/pricing · https://weaviate.io/blog/weaviate-cloud-pricing-update · BSD-3 LICENSE (github.com/weaviate/weaviate) · Weaviate Embeddings/hybrid docs. *(verified on 2026-06-16; per-region price multipliers not published)*
