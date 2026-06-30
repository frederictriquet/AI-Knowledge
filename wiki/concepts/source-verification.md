---
title: "Source verification (anti-context-contamination)"
type: "Concept"
theme: reasoning-planning
level: 🔴
source_url: https://www.ibm.com/think/tutorials/build-corrective-rag-agent-granite-tavily
source_title: "Build a corrective RAG agent with IBM Granite and Tavily"
---

# Source verification (anti-context-contamination)

**In one sentence** — an LLM step that rejects a retrieved passage as soon as it comes from an out-of-scope source, before it pollutes the context.

## In detail
Within the cRAG framework, source verification is an essential new prompt. The `CONTEXT_SOURCE_VERIFICATION_PROMPT` asks the LLM to distinguish text coming from a general/public source from text specific to a private policy. If the context mentions or strongly implies public health programs (Medi-Cal, Medicaid, Medicare, NHS, state-funded programs) or is too general, the model answers "NO"; otherwise "YES". Concretely, after each Tavily search, `is_relevant_source = llm(verification_prompt).strip().upper()`: only a "YES" adds the passage to `retrieved_context_pieces`; a "NO" triggers the log "context source rejected" and the passage is not integrated, which leaves the context short and triggers the next fallback or the final refusal. Stated goal: "prevents the generation of misleading answers and enables self-correction".

## Example
The tutorial's case: the agent answers questions about a private insurance policy ("Super Star Health" from Care Health Insurance). The internal PDF does not cover the question, the agent falls back on Tavily; the web search surfaces a factual passage about Medi-Cal (a state-funded public health program). This passage would pass the 0-5 relevance scoring, but the `CONTEXT_SOURCE_VERIFICATION_PROMPT` returns "NO", logs "context source rejected": it never enters `retrieved_context_pieces`. The context stays below `MIN_CONTEXT_LENGTH`, which triggers query rewriting then, failing that, a polite refusal.

## Tradeoff / insight (for a senior)
This is a domain relevance filter, distinct from the query relevance grader. The 0-5 scoring says "does this passage answer the question?"; source verification says "is this passage allowed to enter this context?". Without it, a factual but out-of-scope web result (a public program) would pass scoring and contaminate an answer meant to be about a private policy. The cost is one LLM call per external passage, and the binary yes/no decision remains subject to the judge's errors.

## Primary source
"This function prevents the generation of misleading answers and enables self-correction, contributing to knowledge refinement." ([source](../../sources/ibm-guide-agents-ia/md/68-build-corrective-rag-agent-granite-tavily.md))

## See also
- [Corrective RAG (cRAG)](corrective-rag.md)
- [Tool grounding](tool-grounding.md)
