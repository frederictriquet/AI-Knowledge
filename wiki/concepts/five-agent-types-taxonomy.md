---
title: "Taxonomy of the 5 agent types"
type: "Concept"
theme: agent-fundamentals
level: 🟢
source_url: https://www.ibm.com/think/topics/ai-agent-types
source_title: "AI agent types"
migrated_from: taxonomie-5-types-agents
---

# Taxonomy of the 5 agent types

**In one sentence** — the classic scale of agent sophistication, from hard-wired `if/then` to an agent that improves through feedback.

## In detail
Five main types of AI agents are distinguished, ranked by level of intelligence and decision-making process: simple reflex agents, model-based reflex agents, goal-based agents, utility-based agents, and learning agents. The simple reflex applies condition-action rules without memory or anticipation (thermostat, traffic lights). The model-based reflex adds an internal model of the world to handle a partially observable environment. The goal-based agent plans and reasons to reach an objective. The utility-based agent evaluates several outcomes via a utility function and arbitrates between competing goals. The learning agent updates its behavior from experience feedback. These five types can be deployed together in a multi-agent system, each specializing in the subtask it is best suited for.

## Example
The same autonomous vehicle illustrates the goal → utility jump: a goal-based agent merely plans a route that reaches the destination while avoiding known obstacles; a utility-based agent, on the other hand, scores each route via a utility function arbitrating between speed, fuel economy and passenger safety, then takes the option with the best overall score. On the e-commerce side, the utility agent does dynamic pricing by weighing sales history, customer preferences and stock levels — a simple reflex `if price < threshold` cannot make that trade-off.

## Tradeoff / insight (for a senior)
Pure pedagogical vocabulary. The hierarchy reflex → model → goal → utility → learning corresponds to increasing cost/complexity: you only "move up" a rung when the environment requires it (memory, planning, arbitration, adaptation). The factory example shows that combining all five produces layers: reflex for instant safety, utility for arbitration, learning for continuous optimization.

## Primary source
Taxonomy from Russell & Norvig, *Artificial Intelligence: A Modern Approach* (AIMA, ch. 2).

## See also
- [Learning agent (AIMA model)](learning-agent.md)
- [Reactive / deliberative / cognitive architectures](reactive-deliberative-cognitive-architectures.md)
