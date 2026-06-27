---
title: "Reactive / deliberative / cognitive architectures"
type: "Concept"
theme: reasoning-planning
level: 🟢
source_url: https://www.ibm.com/think/topics/agentic-architecture
source_title: "What is an agentic architecture?"
primary_source: "arXiv:2404.11584"
migrated_from: archi-reactif-deliberatif-cognitif
---

# Reactive / deliberative / cognitive architectures

**In one sentence** — three levels of agent sophistication: a stateless reflex, a planner with a world model, or a cognitive system with memory and learning.

## In detail
Three families of agentic frameworks are distinguished. **Reactive architectures** directly couple situations to actions; they are reflexive, with decisions resting on immediate stimuli rather than memory or prediction — these agents can neither learn from the past nor plan for the future. **Deliberative architectures** make decisions based on reasoning, planning and internal world models: unlike reactive agents, deliberative agents analyze their environment, predict future outcomes and make informed choices before acting. **Cognitive architectures** are advanced systems that mimic human thinking, reasoning, learning and decision-making; they integrate perception, memory, reasoning and adaptation, each represented by individual modules, and constitute the most advanced type. The BDI model is placed in this last category.

## Example
The same mission, "reach a target in a maze," with three agents. The **reactive** one applies a pure reflex — *wall on the right → turn left* — on the immediate stimulus alone: no memory of corridors already visited, no anticipation, it may loop indefinitely. The **deliberative** one maintains an internal model of the maze, simulates several paths, predicts which one leads to the exit and acts only after that informed choice. The **cognitive** one adds separate modules for perception, memory, reasoning and adaptation: it retains its past failures and improves its strategy from one run to the next — the most advanced, but the most expensive.

## Tradeoff / insight (for a senior)
Pure vocabulary, which overlaps the AIMA taxonomy: reactive = simple reflex, deliberative = goal/utility-based, cognitive = learning + memory. The axis is the state retained: stateless (fast, predictable) → world model (plans) → memory + learning (adapts, but expensive). The choice depends on the observability and dynamism of the environment.

## Primary source
This tripartite split belongs to the classic vocabulary of agent AI (Wooldridge, Brooks for the reactive part). Bandura (doi:10.1146/annurev.psych.52.1.1) and Masterman et al. (arXiv:2404.11584) come in on other points.

## See also
- [Taxonomy of the 5 agent types](five-agent-types-taxonomy.md)
- [BDI architecture (Belief-Desire-Intention)](bdi.md)
