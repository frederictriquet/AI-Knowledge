---
title: "Collaboration strategies: rules / roles / models"
type: "Concept"
theme: multi-agent
level: 🟡
source_url: https://www.ibm.com/think/topics/multi-agent-collaboration
source_title: "What is multi-agent collaboration?"
---

# Collaboration strategies: rules / roles / models

**In one sentence** — three ways to make agents cooperate: scripted, by role assignment, or by probabilistic reasoning under uncertainty.

## In detail
Three agent collaboration strategies are distinguished. **Rule-based**: interactions are strictly governed by a precise set of rules (conditional instructions, state machines, logical frameworks); limited learning capacity, fixed policy; efficient and fair for highly structured tasks, but not very adaptable or scalable. **Role-based**: each agent is assigned a role, permissions and goals tied to part of the overall objective; agents work semi-independently while sharing information (inspired by human dynamics: leader, observer, executor); allows modular, expert collaboration, but depends on the agents' smooth integration. **Model-based**: agents build internal models (often probabilistic or learned) of their state, the environment and the other agents; they plan under uncertainty via belief updating and inference. Methods cited: Bayesian reasoning, Markov decision processes (MDP), machine-learning models. Great flexibility, but high complexity and computational cost.

## Example
Smart healthcare system in role-based collaboration: one agent monitors physiological signals, another identifies anomalies, a third recommends treatments, a last one manages patient data in regulatory compliance — each has its own permissions and goals, but shares information to ensure continuity and fault tolerance. The source also illustrates the emergent mode with a fleet of drones exploring a disaster zone: each drone follows its route, avoids the others, reports its findings and changes course on an unforeseen event, with no single leader.

## Tradeoff / insight
A cost/adaptability gradient: rules (deterministic, debuggable, rigid) → roles (modular, depends on the split) → models (handles uncertainty via Bayesian/MDP, but expensive). Choose "models" only if the environment is genuinely partially observable or uncertain; otherwise scripting or roles suffice and stay predictable.

## Primary source
Methods named without academic reference: Bayesian reasoning, MDP.

## See also
- [Centralized vs decentralized networks](centralized-decentralized-networks.md)
- [Multi-agent structures: hierarchical / holonic / coalition / team](multi-agent-structures.md)
