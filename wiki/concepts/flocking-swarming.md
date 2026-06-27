---
title: "Swarm behaviors (flocking / swarming)"
type: "Concept"
theme: frameworks-tooling
level: 🟡
source_url: https://www.ibm.com/think/topics/multiagent-system
source_title: "What is a multiagent system?"
migrated_from: flocking-swarming
---

# Swarm behaviors (flocking / swarming)

**In one sentence** — coordinate a crowd of agents through a few bio-inspired local rules, with no central controller.

## In detail
Agent behaviors in a multi-agent system often mirror those observed in nature (birds, fish, humans) and apply to software as well as robotic agents. **Flocking** concerns directional synchronization and is described by three heuristics: **separation** (avoid collisions with nearby agents), **alignment** (match the speed of nearby agents), **cohesion** (stay close to other agents). Managing transport networks (rail systems) is a representative software context. **Swarming** denotes emergent self-organization and aggregation among software agents with **decentralized control**; its advantage is that a single operator can be trained to manage a whole swarm, which is less computationally costly and more reliable than training one operator per agent.

## Example
Managing a rail network: each train is an agent that applies separation (don't hit the convoy ahead), alignment (match its speed to local traffic) and cohesion (stay in the flow) — directional synchronization emerges without a central plan. On the swarm side, the economic argument is concrete: instead of training one human operator per robot, a single operator drives the whole swarm, less computationally costly and more reliable. A model directly transposed from birds adjusting their flight to their immediate neighbors.

## Tradeoff / insight
The three rules separation/alignment/cohesion are Reynolds' boids: coherent global behavior emerges from purely local rules, with no global state or coordinator. Tradeoff: robustness and massive scale (thousands of agents) versus no guarantee on the global outcome and difficulty constraining the emergence. Key point: it is an answer to the cost of coordination when the number of agents explodes.

## Primary source
The separation/alignment/cohesion heuristics come from Craig Reynolds, "Flocks, Herds, and Schools: A Distributed Behavioral Model" (boids, SIGGRAPH 1987).

## See also
- [Multi-agent structures: hierarchical / holonic / coalition / team](multi-agent-structures.md)
- [Centralized vs decentralized networks](centralized-decentralized-networks.md)
