---
title: "Semantic Kernel"
type: "Concept"
theme: frameworks-tooling
level: 🟢
source_url: https://www.ibm.com/think/insights/top-ai-agent-frameworks
source_title: "AI agent frameworks: choosing the right foundation for your business"
---

# Semantic Kernel

**In one sentence** — Microsoft's agent SDK, with two built-in agent types (chat-completion and assistant) and a Process Framework to orchestrate step-based workflows.

## In detail
Semantic Kernel is an open-source development kit from Microsoft for building enterprise generative AI applications. Its agent framework, announced as experimental, provides core abstractions for building agents. It offers two built-in implementations: a chat-completion agent and a more advanced assistant agent. Several agents can be orchestrated through group chats, or using the *Process Framework* (also marked experimental) for more complex workflows. A process consists of steps that represent the tasks assigned to AI agents and describe how data flows between them. Semantic Kernel is available on GitHub.

## Example
Support-ticket handling process: a `Classify` step (chat-completion agent) reads the message and emits the category; the data flows to a `Resolve` step (assistant agent, more advanced, with access to plugins) that queries the knowledge base; a third `Draft` step composes the answer. If the category is "complex case," the Process Framework instead routes to a group chat where several agents deliberate. Each step explicitly declares the tasks assigned and the data flow between them — it's the step, not a free-form graph.

## Tradeoff / insight
Pure vocabulary for anyone already in the Microsoft ecosystem: "plugins/kernel" on the tooling side, "Process Framework" on the step-based orchestration side (conceptually close to other frameworks' steps). The dual "experimental" status of the agent framework and the Process Framework is the one real engineering signal: not to be set as the foundation of production without watching for API breakage.

## Primary source
See the Microsoft Semantic Kernel documentation and the GitHub repository.

## See also
- [llamaindex](llamaindex.md)
- [orchestration-types](orchestration-types.md)
