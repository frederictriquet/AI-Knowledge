---
tool: "LlamaIndex"
title: "LlamaIndex"
themes: [rag-context, frameworks-tooling]
type: "Python + TS framework (data/RAG + agents) + managed LlamaCloud/LlamaParse platform"
url: https://www.llamaindex.ai/
pricing_model: "Open-source (MIT) + LlamaCloud/LlamaParse (freemium, usage-based credits)"
llm_cost: "🔑 BYOK (framework); LlamaParse bills in credits/page (LLM included)"
objectives: [production]
family: "General-purpose multi-agent frameworks (for developers)"
eco_icons: "🔓🎁💳"
llm_cost_icons: "🔑"
summary: "**RAG-first** (MIT): connectors, indexing, query, agentic Workflows. Strength = **LlamaParse** (OCR parsing of complex docs). Usage-based LlamaCloud (credits: Free 10k → Starter $50 → Pro $500). Concept: [📄 notion](../concepts/llamaindex.md)"
migrated_from: llamaindex
---

# LlamaIndex

**In one sentence** — data framework for LLMs, **RAG-oriented**: data connectors, indexing, advanced retrieval/query and agents (event-driven Workflows), complemented by a managed platform for **document parsing** (LlamaParse) and indexing (LlamaCloud).

> 📄 Detailed concept: [LlamaIndex concept note](../concepts/llamaindex.md). Here: the product angle (license, pricing, LLM cost).

## Type & integration
Open-source **Python** (`llama_index`) **and TypeScript** (`LlamaIndexTS`) framework. Covers ingestion (LlamaHub), indexing, query/retrieval, and **Workflows** (event-driven agentic orchestration, ≈ equivalent of LangGraph on the agent side). + managed **LlamaCloud** (managed indexing/RAG) and **LlamaParse** (OCR + "layout-aware" agentic parsing of complex documents).

## Pricing model
- **Framework: open-source MIT**, free.
- **LlamaCloud / LlamaParse**: paid **usage-based in credits** (1,000 credits = $1.25). Plans: **Free** $0 (10k credits) → **Starter** $50/month (40k) → **Pro** $500/month (400k) → **Enterprise** on quote. LlamaParse bills **per page** by mode: Fast 1 credit, Cost-effective 3, Agentic 10, Agentic Plus 45 (≈ 800 to 18 pages/$).

## LLM cost
**🔑 BYOK on the framework side**: you supply your model **+ embedding** keys (OpenAI by default, but pluggable to any model, or `llm=None`). ⚠️ Nuance: on the **managed LlamaParse** side, the internal LLM/VLM parsing costs are **included in the credit** (not BYOK) — you pay in credits, not via your key.

## What it's for
The **RAG-first** choice: large catalog of connectors, and especially **LlamaParse** to ingest complex documents (tables, multi-column PDFs, scans) where naive parsing fails. Workflows for the agentic part.

## Notes
- Vs LangChain ([📄 notion](../concepts/langchain.md)) / [LangGraph](langgraph.md): LlamaIndex leans **data/RAG/parsing**; LangChain/LangGraph lean general orchestration. Partial overlap (Workflows ≈ LangGraph).
- Commercial value = the managed layer (LlamaParse/LlamaCloud); the framework stays 100% MIT.
- Some managed services shown as "free (beta)" — status to reconfirm.

## Source
https://www.llamaindex.ai/pricing · https://developers.llamaindex.ai/python/cloud/general/pricing/ · LICENSE MIT (github.com/run-llama/llama_index). *(verified on 2026-06-16)*
