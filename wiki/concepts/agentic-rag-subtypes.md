---
title: "Agentic RAG subtypes"
type: "Concept"
theme: rag-context
level: 🟡
source_url: https://www.ibm.com/think/topics/agentic-rag
source_title: "What is agentic RAG?"
migrated_from: sous-types-rag-agentique
---

# Agentic RAG subtypes

**In one sentence** — four families of agents for RAG: routing, query planning, ReAct, and plan-and-execute.

## In detail
Four types of AI agents can make up an agentic RAG system. **Routing agents** determine which knowledge sources and external tools to use for a query; in a single-agent system, the routing agent picks the source to query. **Query-planning agents** are the "task managers": they decompose complex queries into step-by-step sub-queries, send them to other agents, then combine their answers into a coherent overall response (a form of orchestration). **ReAct agents** create step-by-step solutions, identify useful tools and dynamically adjust the next steps based on results. **Plan-and-execute agents** are an evolution of ReAct: they "can run multi-step workflows without calling back the main agent, for lower costs and better efficiency."

## Example
The source describes the query-planning agent as a "task manager" performing orchestration: on a composite query, it decomposes it into step-by-step sub-queries, distributes them to the system's other agents, waits for their answers, then recombines them into a coherent overall response. This is the manager/workers pattern: an agent retrieves nothing itself but drives other AI models, whereas a routing agent merely picks the right source for a single query.

## Tradeoff / insight
The decision axis is the cost of re-invoking the planner. ReAct calls the central reasoning back at each observation (adaptive, costly); plan-and-execute builds the full plan once then executes it (economical, but blind to surprises mid-plan). Note: because the plan-and-execute agent must reason over all steps upfront, "completion rates and quality tend to be higher."

## Primary source
"Plan-and-execute agent frameworks are an evolution of ReAct agents. They can run multi-step workflows without calling back the main agent." ([source](../../sources/ibm-guide-agents-ia/md/64-agentic-rag.md))

## See also
- [Agentic RAG](rag-agentique.md)
- [ReAct vs function calling](react-vs-function-calling.md)
