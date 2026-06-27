---
title: "Vertical / horizontal / hybrid architectures"
type: "Concept"
theme: agent-fundamentals
level: 🟡
source_url: https://www.ibm.com/think/topics/agentic-architecture
source_title: "What is an agentic architecture?"
primary_source: "arXiv:2404.11584"
migrated_from: archi-vertical-horizontal-hybride
---

# Vertical / horizontal / hybrid architectures

**In one sentence** — the three topologies of a multi-agent system: a centralized leader, equal peers, or a mix of both depending on the phase.

## In detail
Three types of multi-agent architectures stand out. **Vertical**: a leader agent supervises the subtasks and decisions, and the agents report to it (centralized control, hierarchy, centralized communication). Strengths: efficiency on sequential workflows, clear accountability. Weaknesses: bottlenecks and a **single point of failure** tied to the leader. Use cases: workflow automation with multiple approvals, document generation. **Horizontal**: a peer-collaboration model, equal agents in a decentralized system, group-driven decisions. Strengths: dynamic resolution, parallel processing. Weaknesses: coordination problems, **slower decisions (too much deliberation)**. Use cases: brainstorming, interdisciplinary problems. **Hybrid**: combines structured leadership and collaborative flexibility, with dynamic leadership that adapts to the task phase. Strength: versatility; weakness: the complexity of managing roles.

## Example
A concrete sports case cited by the source: a team of specialized agents — one in *performance analysis*, another in *injury prevention*, a third in *market research* — collaborating on a single case. In a **vertical** topology, a leader agent distributes these subtasks and centralizes the final decision (ideal for sequential approvals); in a **horizontal** one, the three peers share resources and ideas and decide collectively (brainstorming). On the tooling side, the source names **crewAI** (a Python framework built on LangChain) and DeepWisdom's **MetaGPT**, which orchestrates agents via standardized operating procedures (SOPs).

## Tradeoff / insight (for a senior)
The real tradeoff is centralization vs robustness: vertical gives control and debuggability at the price of a SPOF; horizontal eliminates the SPOF but pays in consensus latency. Hybrid is the pragmatic answer (a leader that hands off), at the price of heavier orchestration. Same tradeoffs as orchestrated vs choreographed microservices.

## Primary source
T. Masterman, S. Besen, M. Sawtell, A. Chao, "The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey", arXiv:2404.11584, April 2024.

## See also
- [Centralized vs decentralized networks](centralized-decentralized-networks.md)
- [Multi-agent structures: hierarchical / holonic / coalition / team](multi-agent-structures.md)
