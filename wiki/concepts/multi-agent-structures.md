---
title: "Multi-agent structures: hierarchical / holonic / coalition / team"
type: "Concept"
theme: multi-agent
level: 🟡
source_url: https://www.ibm.com/think/topics/multiagent-system
source_title: "What is a multiagent system?"
objectives: [code-generation]
---

# Multi-agent structures: hierarchical / holonic / coalition / team

**In one sentence** — four ways to organize agents: a chain of command, a whole-and-part arrangement, a temporary alliance, or an interdependent team.

## In detail
Four agent organization structures stand out. **Hierarchical**: a tree structure with different levels of autonomy; in a simple hierarchy a single agent decides, in a uniform hierarchy responsibility is distributed. **Holonic**: agents are grouped into holarchies; a holon is an entity that cannot function without its components (like the human body and its organs); the main agent can have several sub-agents while appearing as a single entity, and those sub-agents can play roles in other holons — these structures are self-organized. **Coalition**: useful when individual agents do not perform well alone; they unite temporarily to improve utility, then the coalition is dissolved once performance is achieved (hard to maintain in a dynamic environment). **Team**: a structure close to a coalition, but the agents do not work independently, they depend much more on one another, and the structure is more hierarchical.

## Example
Supply chain management: conversational agents with sometimes conflicting goals (buyer, supplier, logistics) must negotiate with each other — typically an opportunistic coalition, formed for the time needed to smooth out a flow then dissolved. By contrast, maritime defense is a team structure: strongly interdependent and hierarchical agents collaborate continuously to identify the interactions between hostile ships and defense ships, never acting in isolation. The holon, in turn, is experienced like the human body: an organ-agent inseparable from the whole it serves.

## Tradeoff / insight (for a senior)
Hierarchical and team are intuitive. The two worth knowing are: **holonic** (an agent is simultaneously a whole and a part, and a sub-agent can be shared across several holons — useful for pooling capabilities without duplicating them), and **coalition** (an opportunistic, autonomous and short-lived grouping, dissolved as soon as the goal is reached — dynamic elasticity at the price of a (re)formation cost). The distinctive axis of coalition vs team: the independence and lifespan of the alliance.

## Primary source
The notion of a holon comes from Arthur Koestler (*The Ghost in the Machine*, 1967) and its multi-agent application from the MAS literature.

## See also
- [Flocking / swarming behaviors](flocking-swarming.md)
- [Vertical / horizontal / hybrid architectures](vertical-horizontal-hybrid-architectures.md)
