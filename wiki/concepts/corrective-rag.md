---
title: "Corrective RAG (cRAG)"
type: "Concept"
theme: rag-context
level: 🟡
source_url: https://www.ibm.com/think/tutorials/build-corrective-rag-agent-granite-tavily
source_title: "Build a corrective RAG agent with IBM Granite and Tavily"
---

# Corrective RAG (cRAG)

**In one sentence** — an LLM grader scores the retrieved passages; if poor → fallback to web search (Tavily) + query rewriting, otherwise an explicit refusal rather than a hallucination.

## In detail
cRAG "does not just rely on traditional RAG but improves on it": it assesses the quality and relevance of the retrieved results. An ordered workflow, illustrated here for questions about an insurance policy (PDF), chains: initial retrieval from a FAISS store, **context scoring** by an LLM grader (score 0–5, threshold `SIMILARITY_THRESHOLD = 3`), then a **Tavily fallback** (web search) if the context is too short (`MIN_CONTEXT_LENGTH = 100`), **source verification** by the LLM, **query rewriting** + a second Tavily search if needed, and finally **constrained generation** or refusal. The Granite LLM is configured at `temperature: 0.2` for factual answers. Key point: "If the context is weak, irrelevant or from an unreliable source, cRAG attempts to find better information [...], or explicitly refuses to answer instead of fabricating an answer."

## Example
Question "How does the policy cover for In-Patient Hospitalisation?" over a health-insurance brochure. The FAISS retriever returns the top-8, the grader scores each chunk (Score: 0–5); those `< 3` are discarded. If the context stays below 100 characters, the Tavily fallback fires — but the `CONTEXT_SOURCE_VERIFICATION_PROMPT` rejects a web result about Medi-Cal (a public program) with a "NO", since it is outside the private policy. Absent verified context, the final prompt mandates: quote verbatim or answer "I'm sorry, but this information is not available in the provided policy details" — never invent.

## Tradeoff / insight
cRAG turns retrieval into a corrective loop with several guardrails (score, length, source verification). The trade-off: each guardrail is an extra LLM call (latency, tokens) and each threshold (`SIMILARITY_THRESHOLD`, `MIN_CONTEXT_LENGTH`) is a fragile calibration point. The real value is the deliberate refusal: preferring "I don't know" to a fabrication, which changes the utility function in critical domains.

## Primary source
The founding cRAG paper: Yan et al., "Corrective Retrieval Augmented Generation", 2024.

## See also
- [Source verification](source-verification.md)
- [Agentic RAG](agentic-rag.md)
