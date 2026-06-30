---
tool: "turbopuffer"
title: "turbopuffer"
themes: [rag-context, memory]
type: "Web service (serverless vector + full-text search, proprietary)"
url: https://turbopuffer.com/
pricing_model: "Proprietary / SaaS — pay-as-you-go (min $64/month)"
llm_cost: "🟢 BYO embeddings — only indexes/searches, does not generate embeddings"
objectives: [production]
family: "RAG infrastructure / vector databases"
eco_icons: "🔒💳"
llm_cost_icons: "🟢"
summary: "**Serverless on object storage** (~10× cheaper at scale), vector + BM25. Pay-as-you-go, min **$64/month** (Launch) → $256 → $4,096+. Cold latency 300–500 ms acknowledged. Strong traction (Cursor, Anthropic, Notion). Unit prices not publicly stated in the clear"
---

# turbopuffer

**In one sentence** — a **serverless** search engine (vector + full-text BM25) built **on object storage** (S3/GCS/Azure): ~10× cheaper at scale, designed for mostly-"cold" multi-namespace workloads.

## Type & integration
A **proprietary** managed service (no self-host). Tiered architecture: cold data on object storage (~$0.02/GB), warm on SSD/NVMe, hot in RAM. BYO embeddings (dense & sparse vectors), filters (inverted index), regex (trigram index).

## Pricing model
Proprietary, **pay-as-you-go** across 3 dimensions (storage, writes, queries), with monthly minimums (verified on 2026-06-16):
- **Launch**: min **$64/month** (all features, community support).
- **Scale**: min **$256/month** (HIPAA-ready, SSO, audit logs).
- **Enterprise**: **≥ $4,096/month** (+35% usage) — single-tenancy, BYOC, CMEK, 99.95% SLA.
- ⚠️ **Exact unit prices not verifiable at the source** (interactive calculator). Third-party estimates: ~$1/M vectors/month, ~$4/M queries, storage ~$0.02/GB — to be confirmed.

## LLM cost
**🟢** turbopuffer **does not generate embeddings**: it is a **BYO embeddings** engine, you supply the vectors, it indexes and queries (+ full-text BM25, filters, regex). No built-in LLM/embedding cost.

## What it's for
The **cost** bet: storing cold vectors on object storage rather than SSD/RAM drastically reduces the bill for multi-tenant / many lightly-used namespace workloads (code indexes, per-workspace search). Claimed scale: 4T+ documents, 10M+ writes/s, 25k+ queries/s.

## Notes
- **Latency trade-off**: sub-10 ms p50 on cached data, but **first "cold" access ~300–500 ms**. No built-in reranking.
- Recent product (launched Oct. 2023, ex-Shopify founders) but **strong traction**: customers cited on the site — Cursor, Anthropic, Notion, Atlassian, Linear, Grammarly… Published cases: Cursor ~95%, Notion ~80% search-cost reduction (secondary sources).
- Vs [Pinecone](pinecone.md) serverless: turbopuffer bets on cost and multi-namespace; Pinecone on guaranteed sub-10 ms latency on **every** query.

## Source
https://turbopuffer.com/ · https://turbopuffer.com/pricing · https://turbopuffer.com/docs · https://turbopuffer.com/about. *(verified on 2026-06-16; per-unit prices and formal license not published in the clear on the site)*
