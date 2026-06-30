---
title: "Agentic RAG"
type: "Concept"
theme: rag-context
tags: [rag, agents, retrieval]
level: 🟡
source_url: https://www.ibm.com/think/topics/agentic-rag
source_title: "What is agentic RAG? — IBM Think"
objectives: [production]
---

# Agentic RAG

**In one sentence** — an agent placed in front of retrieval that decides whether to search, where to search, reformulates, and iterates, instead of a fixed reactive RAG pipeline.

## In detail
Agentic RAG consists of inserting one or more AI agents into the RAG pipeline to improve its adaptability and accuracy. It contrasts point by point with traditional RAG: flexibility (multiple knowledge bases and external tools, where standard RAG connects an LLM to a single dataset), adaptability, accuracy (agents can iterate to optimize their results, validate, and correct, which reactive RAG does not do), scalability, and multimodality. Metaphor: traditional RAG is an employee who executes explicit tasks with no initiative; agentic RAG is a proactive team that takes initiative. Agentic RAG leverages the ability of agents to plan and execute sub-tasks.

## Classic vs agentic RAG, decision by decision
Classic RAG is a **fixed pipeline** (one pass: search → injection → answer); the agentic version places an **agent** in front of retrieval, which becomes a tool it drives:

| Decision | Classic RAG | Agentic RAG |
|---|---|---|
| Should we search? | always | **the agent decides** (may answer directly) |
| Where to search? | 1 fixed source | **routes** to the right source (several bases, web, API) |
| The query | the raw question | **reformulates / decomposes** into sub-queries |
| Weak results | generates anyway | **evaluates, rejects, retries** (cf. [corrective RAG](corrective-rag.md)) |
| Number of passes | 1 | **iterates** until satisfied |

Telling example — *"Compare the 2023 revenue of our France and Germany subsidiaries"*: classic RAG searches on the whole sentence → mixed passages, approximate answer; the agentic version **decomposes** into two targeted retrievals (`France revenue`, `Germany revenue`), checks both figures, then compares.

## Example
The source illustrates the multi-agent version with a specialized search system: "one agent queries external databases while another can browse emails and web results." Each search agent is dedicated to a domain or a source type, and a routing agent chooses which one to call based on the query. For an enterprise question mixing proprietary data and current events, one queries the internal data store, the other goes to search the Web; their returns are merged where classic RAG would have been limited to its single base.

## Tradeoff / insight
It is "not always the best option." More agents = more tokens, more latency (the LLM takes time to generate), more risk of failed collaboration, and hallucination is never entirely eliminated. Reserve it for cases requiring the querying of multiple sources; for a single source and simple queries, the agentic overhead is not justified.

## Primary source
"Although agentic RAG optimizes results through function calling, multi-step reasoning, and multi-agent systems, it is not always the best option." ([source](../../sources/ibm-guide-agents-ia/md/64-agentic-rag.md))

## See also
- [Sub-types of agentic RAG](agentic-rag-subtypes.md)
- [Semantic caching](semantic-caching.md)
- [Corrective RAG (cRAG)](corrective-rag.md)
