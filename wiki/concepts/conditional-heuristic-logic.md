---
title: "Conditional & heuristic logic"
type: "Concept"
theme: agent-fundamentals
level: 🟢
source_url: https://www.ibm.com/think/topics/agentic-reasoning
source_title: "What is agentic reasoning?"
migrated_from: logique-conditionnelle-heuristique
---

# Conditional & heuristic logic

**In one sentence** — hard-wired reasoning: if-then rules and utility scores/functions coded into the decision loop, with no learning.

## In detail
Conditional logic and heuristics are among the agentic reasoning strategies. Conditional logic relies on preprogrammed condition-action rules ("if-then"): when a condition is met, the agent executes the corresponding action; example: a banking fraud-detection agent flagging a transaction according to defined criteria. Its limit: the agent cannot act in the face of an unrecognized scenario; model-based agents mitigate this through memory and perception but remain bound by rules. Heuristics concern goal-based agents (a search algorithm to reach a goal) and utility-based agents (a utility function to choose the optimal outcome); example: a navigation agent looking for the fastest route, then also the most fuel-efficient one.

## Example
A warehouse robot must shelve a product. It consults an internal model of the warehouse to compute its route, then applies its condition-action rules: *if* an obstacle appears on the path, *then* deviate and continue. The model (the state of the environment) is updated with each new perception, but the agent stays a prisoner of its hard-wired rules: faced with an unforeseen scenario — a fully blocked aisle, a product absent from the model — it has no fallback action and gets stuck. It is precisely this out-of-domain rigidity that justifies moving to LLM reasoning.

## Tradeoff / insight (for a senior)
Classic programming, nothing non-trivial: determinism, traceability, and low cost versus total rigidity outside the intended domain. It is the foundation of reflex agents and goal/utility-based agents; LLM "reasoning" (CoT, ReAct, etc.) only steps in when the state space becomes too open to be hand-wired.

## Primary source
A classic programming / symbolic AI concept. See also: heuristic search algorithms such as A*, utility functions.

## See also
- [ReAct](react.md)
- [Chain-of-Thought (CoT)](chain-of-thought.md)
