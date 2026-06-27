---
title: "Planning: goal / state / sequencing"
type: "Concept"
theme: reasoning-planning
level: 🟢
source_url: https://www.ibm.com/think/topics/ai-agent-planning
source_title: "What is AI agent planning?"
migrated_from: planification-goal-state-action
---

# Planning: goal / state / sequencing

**In one sentence** — to plan is to define a goal (the target end state), model the current state, then derive the sequence of actions that leads from one to the other.

## In detail
AI agent planning determines a sequence of actions to reach a given goal; it involves decision-making, goal prioritization and sequencing. Three key elements are described. **Goal definition** sets the target end state; goals can be static or dynamic, and a complex goal is broken into sub-goals (task decomposition), with LLMs splitting a general aim into subtasks executed over several steps. **State representation** models current conditions, constraints and contextual factors via built-in knowledge and perception (e.g. piece positions in chess, coordinates and obstacles in robotics). **Action sequencing** structures a logical set of steps: identify potential actions, narrow them to the optimal ones, prioritize them, spot dependencies and conditional steps.

## Example
A user asks a chatbot to plan a trip via a natural-language prompt. The complex goal is first decomposed into subtasks — book flights, search for hotels, build an itinerary — then the agent calls APIs to fetch real-time prices and availability and suggest destinations. For sequencing, the source takes a robot vacuum: it must compute the route covering the whole room without needlessly going over the same spot, otherwise it wastes resources and runtime.

## Tradeoff / insight
This is the classic vocabulary of planning (goal / state / action), re-dressed for LLM agents. The engineering challenge is the fidelity of the state representation: a poorly modeled state makes the sequencing diverge regardless of the LLM's quality.

## Primary source
A restatement of classic AI planning vocabulary; no single primary source identified.

## See also
- [Probabilistic planning](probabilistic-planning.md)
- [First vs interleaved decomposition](decomposition-first-vs-interleaved.md)
