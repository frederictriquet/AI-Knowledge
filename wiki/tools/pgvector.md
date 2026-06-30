---
tool: "pgvector"
title: "pgvector"
themes: [rag-context, memory]
type: "Open-source PostgreSQL extension (vector search)"
url: https://github.com/pgvector/pgvector
pricing_model: "Open-source (PostgreSQL License) — free, no separate bill"
llm_cost: "🟢 BYO embeddings — only stores/indexes, generates nothing"
objectives: [production]
family: "RAG infrastructure / vector databases"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "**Postgres extension** (not a separate database): `vector` type + HNSW/IVFFlat index. PostgreSQL License, **free**, available on Supabase/Neon/RDS/Cloud SQL/Azure → cost = that of your database. Vectors + SQL/JOIN/ACID in the same place. Enough up to ~tens of millions of vectors; beyond that, a dedicated database"
---

# pgvector

**In one sentence** — PostgreSQL extension that adds a `vector` type and ANN indexes (**HNSW**, IVFFlat): do vector similarity search **inside Postgres**, next to your relational data — no separate database to operate.

## Type & integration
Not a separate database: `CREATE EXTENSION vector;` in an existing Postgres database. Types `vector` (up to 16,000 dim), `halfvec`, `bit`, `sparsevec`; distances L2, cosine, inner product, L1, Hamming, Jaccard. Pre-installed/enableable on most managed Postgres offerings: **Supabase, Neon, AWS RDS/Aurora, GCP Cloud SQL, Azure**. Usable from any Postgres client (40+ languages).

## Pricing model
**Open-source, PostgreSQL License** (permissive, BSD-style). **Free**, commercial use allowed. **No separate bill**: the cost = that of your Postgres instance (which you already operate or take managed), not a distinct vector-database subscription.

## LLM cost
**🟢** pgvector **generates no embeddings** and calls no LLM: BYO embeddings (you supply vectors computed upstream by OpenAI/Cohere/a local model…), it **stores, indexes and queries** them. No inference cost attributable to pgvector; the embedding cost depends on the external model plugged in upstream.

## What it's for
The "don't add another system" answer: combine vector search, `JOIN`, `WHERE` filters, ACID transactions and metadata **in a single SQL query**, on the same data. Ideal for RAG/semantic search when the team is already on Postgres and wants to minimize the number of technologies to operate.

## Notes
- **When pgvector is enough**: low-to-medium volumes (a few million to ~tens of millions of vectors), combined relational filtering, already-Postgres stack.
- **When to move to a dedicated database** ([Pinecone](pinecone.md)/[Qdrant](qdrant.md)/[Milvus](milvus.md)/[Weaviate](weaviate.md)): hundreds of millions/billions of vectors, native horizontal sharding, advanced quantization, very high QPS. Main limit: Postgres scales mostly vertically, and HNSW index build is RAM/time-costly on very large volumes. *(Thresholds = orders of magnitude, to be benchmarked.)*
- Stable version 0.8.0 series (to reconfirm in CHANGELOG).

## Source
https://github.com/pgvector/pgvector (README + LICENSE PostgreSQL License). Managed availability: AWS RDS/Aurora, Supabase, Neon, Cloud SQL, Azure docs. *(verified on 2026-06-16; exact version number to reconfirm)*
