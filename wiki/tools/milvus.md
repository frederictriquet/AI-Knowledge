---
tool: "Milvus"
title: "Milvus"
themes: [rag-context, memory]
type: "Open-source distributed vector database (Apache 2.0) + managed cloud (Zilliz)"
url: https://milvus.io/
pricing_model: "Open-source (Apache 2.0, LF AI & Data) + Zilliz Cloud (freemium + usage-based)"
llm_cost: "🟢 BYO embeddings; embedding modules relay third-party providers (BYOK)"
objectives: [production]
family: "RAG infrastructure / vector databases"
eco_icons: "🔓🎁💳"
llm_cost_icons: "🟢"
summary: "**Open-source Apache 2.0** (LF AI & Data), built for **massive scale** (tens of billions of vectors), distributed K8s + GPU architecture (CAGRA). Lite (embedded) / Standalone / Distributed. Managed = **Zilliz Cloud** (Free → Serverless $4/M vCU). Heavier distributed ops"
migrated_from: milvus
---

# Milvus

**In one sentence** — **open-source (Apache 2.0)** cloud-native vector database, built for **massive scale** (tens of billions of vectors) via a distributed architecture with disaggregated compute/storage; managed under **Zilliz Cloud**.

## Type & integration
**Graduated project of the LF AI & Data** (created by Zilliz). Three modes: **Milvus Lite** (embedded Python lib, prototyping), **Standalone** (single-machine Docker, ~100M vectors), **Distributed** (Kubernetes, up to tens of billions). The distributed mode depends on etcd + object storage + message queue (Pulsar/Kafka). CPU indexes (HNSW, IVF, DiskANN…) **and GPU** (NVIDIA CAGRA).

## Pricing model
**Open-source Apache 2.0** (free self-host). **Zilliz Cloud** (managed):
- **Free**: free (5 GB, ~1M vectors, 5 collections). $100 credits (+$100 with a payment method).
- **Serverless**: usage-based — **$4/M vCU** + storage **$0.04/GB/month** (unified rate since 2026-01-01).
- **Dedicated**: per CU/hour by region (e.g. $0.248/CU·h, Enterprise AWS). Standard/Enterprise/Business Critical/**BYOC** plans on quote.

## LLM cost
**🟢** Milvus **stores and indexes vectors** — it does not generate embeddings. BYO embeddings by default. Two integration layers relay **external models** (never hosted by Milvus): client-side `pymilvus.model` (OpenAI, Voyage, Cohere…); server-side **Embedding Functions** ("Data in, Data out", Milvus 2.6 — you insert text, Milvus calls OpenAI/Bedrock/Vertex… in **BYOK**). ⚠️ The old managed "Zilliz Cloud Pipelines" are **deprecated/offline since Oct. 2025**.

## What it's for
The choice when targeting **a billion+ vectors** with horizontal Kubernetes scaling and GPU acceleration. RAG and semantic search at very large scale.

## Notes
- Distributed mode = etcd + object storage + message queue dependencies → **heavier to self-host** than [Qdrant](qdrant.md) (binary/Docker) or [Weaviate](weaviate.md). Milvus Lite/Standalone lighten the start.
- ~44.8k GitHub stars; stable line 2.6.x, Milvus 3.0 in beta (May 2026, not GA) — exact GA version to reconfirm.
- Scale/perf claims self-declared by the publisher. Vs [Pinecone](pinecone.md) (proprietary managed).

## Source
https://milvus.io/docs/install-overview.md · https://milvus.io/docs/embedding-function-overview.md · LICENSE Apache 2.0 (github.com/milvus-io/milvus) · docs.zilliz.com (pricing) · lfaidata.foundation/projects/milvus. *(verified on 2026-06-16; Dedicated/BYOC prices on quote)*
