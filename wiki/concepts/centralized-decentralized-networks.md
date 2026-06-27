---
title: "Centralized vs decentralized networks"
type: "Concept"
theme: multi-agent
level: 🟡
source_url: https://www.ibm.com/think/topics/multiagent-system
source_title: "What is a multiagent system?"
migrated_from: reseaux-centralises-decentralises
---

# Centralized vs decentralized networks

**In one sentence** — either a central unit holds the global knowledge and links all the agents, or each one only talks to its neighbors.

## In detail
In **centralized networks** a central unit contains the global knowledge base, links the agents, and oversees their information. Strength: ease of communication and uniformity of knowledge. Weakness: dependence on the central unit — if it fails, the whole system fails. In **decentralized networks**, agents share information with their neighbors rather than with a global base; advantages: robustness and modularity, the failure of a single agent does not bring down the system. Challenge: coordinating behavior so that it benefits the other cooperating agents. This duality recurs at the orchestration level (centralized with a "brain" agent vs decentralized by consensus) and at the communication level (centralized control of an AI that distributes data vs decentralized peer-to-peer communication).

## Example
Maritime defense system: agents organized in a decentralized network each monitor a distinct zone of the network to spot incoming threats (DDoS attacks, intrusions), and cooperate as a team to identify the interactions between approaching hostile boats and defense vessels — the loss of one sensor does not collapse the overall surveillance. Conversely, a centralized network would suit a unified medical knowledge base shared among diagnostic agents, at the price of total dependence on the central unit.

## Tradeoff / insight
The classic distributed-systems trade-off: strong consistency and simple control (centralized) against fault tolerance and scaling (decentralized), at the price of coordination difficulty and potentially unpredictable behaviors. It is the single-orchestrator vs peer-to-peer opposition, played out across three planes (knowledge, orchestration, communication).

## Primary source
General notion of distributed AI. The KQML (DARPA, 1990s) and FIPA-ACL protocols for agent-to-agent communication are cited elsewhere.

## See also
- [Vertical / horizontal / hybrid architectures](vertical-horizontal-hybrid-architectures.md)
- [Multi-agent structures: hierarchical / holonic / coalition / team](multi-agent-structures.md)
