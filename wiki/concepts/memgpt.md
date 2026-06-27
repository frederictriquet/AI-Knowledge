---
title: "MemGPT (Letta)"
type: "Concept"
theme: memory
level: 🔴
source_url: https://arxiv.org/abs/2310.08560
primary_source: "arXiv:2310.08560"
migrated_from: memgpt
---

# MemGPT (Letta)

**In one sentence** — manage an LLM's memory like an operating system: paging between a limited "RAM" context and an external "disk" store, with the model deciding for itself what to load.

## The idea
The context window is treated as a bounded main memory. MemGPT gives the LLM **functions** to move information between this context and an external store (history, facts, documents), to handle eviction and to re-read on demand — like an OS's memory paging. The result: conversations and documents of effectively unlimited size, with memory that persists across sessions.

## Example
The paper validates MemGPT on two concrete domains. In **document analysis**, it processes documents that exceed the underlying model's native window by paging through the passages. In **multi-session chat**, the agent remembers past interactions, "reflects" on its experience and evolves over the course of prolonged engagement with the user. The core mechanism is borrowed from the OS: **interrupts** manage the transfer of control between the model and the user, exactly as an OS regains control on a system call.

## Tradeoff / when to use it
The right reference if you are building **serious long-term memory** (persistent assistants, long-running agents) rather than plain RAG. Cost: latency and extra calls for memory operations, plus the complexity of state management. The project became **Letta**.

## Primary source
Packer et al., 2023, *MemGPT: Towards LLMs as Operating Systems*, arXiv:2310.08560 (UC Berkeley). *(arXiv verified — HTTP 200 + title)*

## See also
- [Short-term vs long-term memory](short-vs-long-term-memory.md)
- [Episodic / semantic / procedural memory](episodic-semantic-procedural-memory.md)
