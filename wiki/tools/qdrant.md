---
tool: "Qdrant"
title: "Qdrant"
themes: [rag-context, memory]
type: "Open-source vector database (Apache 2.0, Rust) self-host + managed cloud"
url: https://qdrant.tech/
pricing_model: "Open-source (Apache 2.0) + Qdrant Cloud (free tier + pay-as-you-go)"
llm_cost: "🟢 BYO embeddings; FastEmbed (local) or Cloud Inference (per token, Cloud only)"
objectives: [production]
family: "RAG infrastructure / vector databases"
eco_icons: "🔓🎁💳"
llm_cost_icons: "🟢"
summary: "**Open-source Apache 2.0 engine in Rust**, performance + **advanced filtering** (filterable HNSW), binary quantization (×32). Self-host `docker run` or Cloud (free tier 1 GB for life, then hourly). Local FastEmbed / Cloud Inference per token. Simple under ~100M vectors"
migrated_from: qdrant
---

# Qdrant

**In one sentence** — **Open-source vector database written in Rust** (Apache 2.0), performance- and **advanced-filtering**-focused: a similarity search engine easy to self-host (Docker), with a managed cloud.

## Type & integration
Open-source engine (Rust, in-house "Gridstore" storage engine), self-host via `docker run` (REST 6333, gRPC 6334, dashboard) **or** Qdrant Cloud / Hybrid Cloud / Private Cloud. Open-core model (OSS engine + proprietary managed control-plane).

## Pricing model
**Open-source Apache 2.0** (self-host free, unlimited). **Qdrant Cloud**:
- **Free tier for life**, no credit card: 1 GB RAM / 0.5 vCPU / 4 GB disk (~1M vectors at 768 dim). Suspended after 1 week of inactivity.
- **Standard**: pay-as-you-go, **billed hourly** (vCPU + memory + storage), 99.5% SLA. **Premium**: minimum spend (not published), SSO, VPC, 24/7 support.
- ⚠️ **Unit prices ($/vCPU/h) not published** at the source — only via the calculator. Hybrid/Private Cloud by quote.

## LLM cost
**🟢** The engine **stores and indexes supplied vectors** (BYO embeddings) — calls no LLM. Two optional helpers: **FastEmbed** (official lib, **local** embedding generation via ONNX, no GPU or external cost); **Qdrant Cloud Inference** (Cloud only, generates embeddings in the cluster, **billed per token**, free quota, also acts as a proxy to OpenAI/Cohere/Jina billed by them).

## What it's for
The "Rust perf + easy on-prem" choice when you want full control and **rich filtering**. Real differentiator: **filterable HNSW** (payload filtering is integrated into the HNSW graph, not applied as a post-filter), Range/Geo/Full-text/Nested filters, ACORN fallback. Scalar (×4) and **binary** (×32 memory) quantization. Hybrid search (dense + sparse/ColBERT, RRF/DBSF).

## Notes
- Documented limits: max 65,535 dimensions, payload index to be created before ingestion, **irreversible migrations** (no downgrade).
- Performance benchmarks = self-benchmarks (bias acknowledged by Qdrant). Series B $50M (March 2026), ~250M downloads.
- Positioning: simple under ~100M vectors (single binary/Docker). Vs [Milvus](milvus.md) (distributed, higher scale but heavy ops), [Weaviate](weaviate.md) (built-in vectorization), [Pinecone](pinecone.md) (managed proprietary).

## Source
https://qdrant.tech/pricing/ · https://qdrant.tech/documentation/cloud/inference/ · LICENSE Apache 2.0 (github.com/qdrant/qdrant) · filtering/quantization docs. *(verified on 2026-06-16; Cloud unit prices not published)*
