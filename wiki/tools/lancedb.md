---
tool: "LanceDB"
title: "LanceDB"
themes: [rag-context, memory]
type: "Embedded open-source vector database (Apache 2.0) + cloud/Enterprise"
url: https://lancedb.com/
pricing_model: "Open-source (Apache 2.0) + LanceDB Cloud/Enterprise (prices not published)"
llm_cost: "🟢 BYO embeddings; optional embedding functions via BYOK / local"
objectives: [production]
family: "RAG infrastructure / vector databases"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "**Embedded** (\"the SQLite of vector search\"), open-source Apache 2.0, **Lance** columnar format, native **object storage** (S3), **multimodal**, no server to operate. Cloud/Enterprise (BYOC) **prices not public**. Local-first / ML pipelines. Limited concurrent writes"
migrated_from: lancedb
---

# LanceDB

**In one sentence** — **embedded multimodal** vector database (in-process, "the SQLite of vector search"), open-source, built on the **Lance** columnar format: data + metadata + embeddings in the same table, directly on object storage (S3/GCS/Azure), **with no server to operate**.

## Type & integration
Embedded library (**Rust** core; Python, TypeScript, Rust SDKs), running inside your process. Native persistence on **object storage** (`s3://`, `gs://`, `az://` URIs) or local FS → storage/compute separation, automatic versioning of every write. Managed offerings on top: **LanceDB Cloud** (serverless) and **Enterprise** (BYOC/VPC).

## Pricing model
**Open-source Apache 2.0** (`lancedb` lib + `lance` format), free. **LanceDB Cloud** (usage-based, storage-driven) and **Enterprise** (BYOC or managed, RBAC/SSO/SLA, via cloud marketplaces). ⚠️ **No public numeric price**: the pricing page is a contact form ("contact sales"). *(A third party mentions a free Cloud in beta + scale-to-zero, not confirmed in a primary source.)*

## LLM cost
**🟢** BYO embeddings (vectors supplied, stored/queried directly). **Optional** embedding layer via a model registry: remote providers (`openai`, `cohere`, `bedrock`, `gemini`, `voyageai`, `jina`…) called with **your key (BYOK)**, or **local** models (`sentence-transformers`, `ollama`, `open-clip`…) at compute cost only. LanceDB does not resell embedding tokens.

## What it's for
The **local-first / edge / batch ML pipelines** choice: no server infra to manage, data on S3, multimodal (text, images, video, point clouds). IVF / IVF_HNSW(_PQ) indexing, full-text BM25, hybrid search, GPU index build.

## Notes
- **Confirmed limits**: limited concurrent writes ("too many concurrent writers" → failures); **reads** scale, heavy writes do not. Python `fork` dangerous (Lance is multi-threaded). Compaction needed with many small inserts.
- Positioning drifted from "embedded vector DB" toward "**AI-native multimodal lakehouse**". Series A $30M (June 2025); in production at Runway, Midjourney, Character.ai.
- Vs [Chroma](chroma.md) (also embedded, often in memory, ≤ ~1M vectors, good metadata filtering); vs server databases ([Qdrant](qdrant.md)/[Weaviate](weaviate.md)/[Milvus](milvus.md)) that require a cluster/managed setup.

## Source
https://lancedb.com · https://docs.lancedb.com (indexing/storage/enterprise) · LICENSE Apache 2.0 (github.com/lancedb/lancedb + /lance) · embeddings registry (source code). *(verified on 2026-06-16; Cloud/Enterprise prices not public; scale figures = marketing)*
