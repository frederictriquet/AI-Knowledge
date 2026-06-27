---
title: "Episodic / semantic / procedural memory"
type: "Concept"
theme: memory
level: 🟡
source_url: https://www.ibm.com/think/topics/ai-agent-memory
source_title: "What is AI agent memory?"
migrated_from: memoire-episodique-semantique-procedurale
---

# Episodic / semantic / procedural memory

**In one sentence** — three subtypes of long-term memory modeled on psychology: traces of lived events (episodic), structured facts (semantic), automated know-how (procedural).

## In detail
Researchers classify agentic memory the way psychologists classify human memory; Princeton's CoALA paper describes these types. **Episodic memory** lets the agent recall specific past experiences, useful for case-based reasoning; it is implemented by recording events, actions and outcomes in a structured format accessible at decision time (e.g. a financial advisor recalling past investment choices). **Semantic memory** stores structured factual knowledge — facts, definitions, rules — via knowledge bases, symbolic AI or vector embeddings; it serves expert domains (legal assistant, medical diagnosis). **Procedural memory** stores skills, rules and learned behaviors that allow acting without reasoning explicitly each time; inspired by human procedural memory (riding a bike), it is acquired through training, often via reinforcement learning.

## Example
The source grounds each type in a case. Episodic: an AI-powered financial advisor remembers a user's past investment choices and draws on that history for better recommendations. Semantic: a legal assistant queries its knowledge base to retrieve precedents and provide accurate advice. Procedural: the analogy of a human riding a bike or typing on a keyboard without thinking through each step — the agent automates learned action sequences, often via reinforcement learning.

## Tradeoff / insight
Decoupling these three memories avoids pushing everything into a single vector store: episodic calls for a timestamped append-only log, semantic for a deduplicated fact base, procedural for frozen policies/skills. Conflating episodic and semantic pollutes retrieval (one-off events treated as general facts).

## Primary source
"Cognitive Architectures for Language Agents" (CoALA), Princeton University, February 2024 — the reference source on agentic memory.

## See also
- [Short-term vs long-term memory](short-vs-long-term-memory.md)
- [Case-based reasoning](case-based-reasoning.md)
