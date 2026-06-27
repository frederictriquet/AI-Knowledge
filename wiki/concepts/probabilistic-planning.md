---
title: "Probabilistic planning"
type: "Concept"
theme: reasoning-planning
level: 🟡
source_url: https://www.ibm.com/think/topics/ai-agent-planning
source_title: "What is AI agent planning?"
migrated_from: planification-probabiliste
---

# Probabilistic planning

**In one sentence** — decide under uncertainty by evaluating several possible outcomes and choosing the action with the highest expected utility.

## In detail
Presented as a method for optimizing and evaluating planning, alongside heuristic search and reinforcement learning. In real-world scenarios, AI agents often operate in uncertain environments where outcomes are not deterministic; probabilistic planning methods account for uncertainty by evaluating several possible outcomes and selecting the actions with the highest expected utility. In the context of model-based collaboration, this approach relies on Markov decision processes (MDPs) and Bayesian reasoning: agents build probabilistic or learned internal models, update their beliefs and predict outcomes, which lets them collaborate without full visibility. Pros/cons: high flexibility and strong decision-making capabilities, but significant complexity and high computational cost.

## Example
Take again the navigation robot described in the same source, whose state includes coordinates, obstacles and terrain conditions. In the deterministic case, heuristic search suffices. But if the terrain is slippery or an obstacle is moving, the outcome of a move is no longer certain: probabilistic planning evaluates several possible outcomes of each action and keeps the one with the highest expected utility. In multi-agent settings, the MDP/Bayesian framework lets each agent update its beliefs and predict outcomes without full visibility into the others.

## Tradeoff / insight
Probabilistic planning is the preferred route for handling partial visibility and non-determinism. The tradeoff is clear: the MDP/Bayesian framework brings robust decisions under uncertainty but explodes in modeling and compute cost; you only bring it out when the environment is genuinely stochastic, not for deterministic workflows where a heuristic suffices.

## Primary source
Not tied to a named source; MDPs and Bayesian reasoning are cited as the underlying methods.

## See also
- [Planning: goal / state / sequencing](goal-state-action-planning.md)
- [First vs interleaved decomposition](decomposition-first-vs-interleaved.md)
