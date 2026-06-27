---
title: "OpenAI Swarm"
type: "Concept"
theme: frameworks-tooling
level: 🟢
source_url: https://www.ibm.com/think/topics/multi-agent-collaboration
source_title: "What is multi-agent collaboration?"
migrated_from: openai-swarm
---

# OpenAI Swarm

**In one sentence** — an OpenAI framework where each agent is a specialized unit and control is passed from one agent to another (handoff) over the course of the conversation.

## In detail
OpenAI's Swarm framework offers "a new way to coordinate multiple agents around routines and handoffs." Instead of acting independently, each agent is a specialized unit equipped with custom tools and specific instructions. Handing off a task or conversation from one agent to another enables a smooth user experience, with each agent specialized in a precise role. This approach improves the efficiency, modularity and responsiveness of the system as a whole. The term "Swarm" emphasizes lightweight coordination and efficient task execution, which lets the system scale to larger real-world situations.

## Example
Customer-service triage: a front-desk agent holds the conversation, classifies the request, then performs a handoff to the billing agent or the technical-support agent as needed — each with its own tools (account lookup, fault database) and instructions. The user perceives only a continuous thread, while conversational control has shifted to a different specialist. The source places this pattern alongside financial analysis and compliance monitoring, where Swarm's "lightweight" coordination allows scaling without a heavy orchestrator.

## Tradeoff / insight
Pure vocabulary: "routines" = per-agent instructions + tools, "handoff" = explicit transfer of conversational control. The pattern is an agent router with minimal coordination — useful to know as a name, but the idea (route to the right specialist) is already familiar.

## Primary source
See the experimental OpenAI Swarm repository.

## See also
- [Orchestration types](orchestration-types.md)
- [LangChain](langchain.md)
