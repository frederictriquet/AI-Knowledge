---
title: "Short-term vs long-term memory"
type: "Concept"
theme: memory
level: 🟢
source_url: https://www.ibm.com/think/topics/ai-agent-memory
source_title: "What is AI agent memory?"
migrated_from: memoire-court-long-terme
---

# Short-term vs long-term memory

**In one sentence** — short-term memory is the context window/buffer of the current session; long-term memory is a persistent external store read back on demand.

## In detail
An LLM on its own remembers nothing: it needs a memory component. **Short-term memory (STM)** retains recent inputs for immediate decisions; useful in conversational AI, it is implemented as a circular buffer or a context window holding a limited volume of recent data before being overwritten. It provides continuity within a session (e.g. ChatGPT keeps the history of a session) but does not survive beyond it, which makes it unsuitable for durable personalization. **Long-term memory (LTM)** stores and retrieves information across sessions, for permanent storage; it is implemented via databases, knowledge graphs or vector embeddings. RAG is considered "one of the most effective techniques" for LTM, with the agent pulling the relevant information from a stored knowledge base. The central challenge is retrieval efficiency: too much data slows responses down.

## Example
The source contrasts two thermostats. The basic one "does not need to remember yesterday's temperature": pure reaction, zero memory. The "smart" thermostat stores and analyzes history to identify trends, adapt to the user's behavior and optimize energy efficiency — typically LTM. On the STM side, a customer-support agent remembers earlier exchanges within a session and adapts its replies, whereas the memoryless version would treat each message in isolation.

## Tradeoff / insight
The tradeoff is latency vs richness: STM is free in infrastructure terms but volatile and bounded by the window; LTM brings persistence and personalization at the price of a storage/retrieval layer and a latency risk if the store is not filtered.

## Primary source
The classification draws on the CoALA paper (Cognitive Architectures for Language Agents, Princeton University, February 2024).

## See also
- [Episodic / semantic / procedural memory](episodic-semantic-procedural-memory.md)
