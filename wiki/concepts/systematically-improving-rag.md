---
title: "Systematically improving your RAG"
type: "Concept"
theme: rag-context
level: 🔴
source_url: https://jxnl.co/writing/2024/05/22/systematically-improving-your-rag/
source_title: "Systematically Improving Your RAG"
objectives: [production]
---

# Systematically improving your RAG

**In one sentence** — treat a RAG system as a measurable product that you improve through metric-driven iterations, not as a fixed recipe.

## What the source says
Liu offers an incremental *runbook* drawn from his consulting work. A common first mistake: focusing on *synthesis* (generation) without checking that *retrieval* works. So you must start by generating **synthetic questions** for each chunk, then measure retrieval **precision and recall** to establish a baseline. In his tests, full-text search and embeddings were sometimes on par (full-text 10× faster), but on repository issues recall went from 55% (full-text) to 65% (embeddings) — hence the value of combining the two. He insists on **metadata extraction** (dates, sources) and *query understanding*, because some questions ("what recent developments?") escape both text and vector. He recommends explicit **feedback mechanisms** ("Did we answer correctly? yes/no"), then **clustering** queries by topics and capabilities to prioritize underperforming areas, and continuous monitoring with a **latency vs recall** tradeoff depending on the stakes (medical diagnosis vs consumer docs).

## Example
Liu generates synthetic questions per chunk to establish a retrieval baseline. A concrete surprise: in some trials, full-text search and embeddings tie on recall (but full-text is 10× faster); on a repository's *issues*, full-text tops out at 55% recall against 65% for embeddings. The lesson: you don't *guess* which retriever to pick, you *measure* it per use case. On feedback, he replaces the ambiguous "thumbs up/down" with a targeted question — "Did we answer correctly? yes/no" — to build a real eval dataset, free of confounding variables (tone, latency).

## Why it matters
Liu brings the *production* view: how to **measure** retrieval, build a feedback loop, segment failures by topic and decide what to improve with numbers — RAG as a continuous-improvement system.

## Key points
- Measure retrieval before generation: recall/precision on synthetic questions (baseline).
- Hybrid full-text + vector; ideally a single store to avoid desynchronization.
- Metadata + query understanding for filtering questions (dates, sources).
- Targeted user feedback ("correct answer? yes/no") to build an eval dataset.
- Clustering by topics/capabilities to prioritize; trade off latency vs recall by stakes.

## See also
- [Agentic RAG](agentic-rag.md) · [Agentic RAG subtypes](agentic-rag-subtypes.md)
- [Reranking](reranking.md)
- [Error analysis](error-analysis.md) · [Eval-driven development](eval-driven-development.md)
- [full post](../../sources/jason-liu/md/ameliorer-rag-systematiquement.md)
