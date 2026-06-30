---
title: "Entry-node guardrail (Granite Guardian)"
type: "Concept"
theme: security
level: 🟡
source_url: https://www.ibm.com/think/tutorials/build-sql-agent-langgraph-mistral-medium-3-watsonx-ai
source_title: "Build a SQL agent with LangGraph and Mistral Medium 3 in watsonx.ai"
objectives: [reliability]
---

# Entry-node guardrail (Granite Guardian)

**In one sentence** — place a moderation detector (HAP/PII via Granite Guardian) as the very first node of the graph, and route through a conditional edge to block undesirable content BEFORE it reaches the LLM and the tools.

## In detail
The LangGraph pattern rests on a moderation node at the entry. The graph "starts at the `guardian` node", which calls `guardian_moderation` "to detect any offensive content before it reaches the LLM and the database" / "before they reach the LLM and the API". The edge is set by `graph.add_edge(START, "guardian")` then an `add_conditional_edges("guardian", ...)` that "routes the graph state either to the `llm`/`assistant` node or to the end", depending on the output of `guardian_moderation`. The function defines a `detectors` dictionary with thresholds — `"granite_guardian": {"threshold": 0.4}`, `"hap": {"threshold": 0.4}`, `"pii": {}` — instantiates `Guardian(...)` (imported from `ibm_watsonx_ai.foundation_models.moderations`) and calls `guardian.detect(...)`, which returns a `moderation_verdict` ("safe"/"appropriate" or "inappropriate"). It is demonstrated that "a sensitive request" is blocked: "the graph did not reach the LLM node before ending the conversation".

## Example
watsonx demo on a SQL agent: the prompt "What is the address of the customer who bought the most expensive car last month?" is judged `inappropriate` (the PII detector sniffs out the extraction of a customer address), routed to `block_message` which returns "This message has been blocked due to inappropriate content." — the graph never reached the LLM node nor the database. Conversely, "What is the total sales revenue of the 5 best-performing dealerships in 2022?" passes as `safe`, and the agent chains `sql_db_list_tables` → `sql_db_schema` → `sql_db_query_checker` → `sql_db_query`. Same `guardian` node at the head of the graph, opposite verdict.

## Tradeoff / insight
Placing the detector upstream (fail-closed before any LLM/tool call) saves tokens and latency on malicious inputs and reduces the injection attack surface. Limit: a fixed detector with a single threshold (0.4) catches HAP/PII but not sophisticated semantic injection; complement it with prompt validation/hardening (see agent security).

## Primary source
watsonx implementation with the Granite Guardian model (`ibm_watsonx_ai.foundation_models.moderations.Guardian`), HAP and PII detectors.

## See also
- [hitl-statique-dynamique](human-in-the-loop-static-dynamic.md)
- [securite-agentique](agentic-security.md)
- [ethique-gouvernance](ethics-governance.md)
