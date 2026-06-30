---
title: "ReWOO"
type: "Concept"
theme: reasoning-planning
level: 🟡
source_url: https://www.ibm.com/think/topics/rewoo
source_title: "What is ReWOO?"
---

# ReWOO

**In one sentence** — "Reasoning Without Observation": plan the whole reasoning chain internally first, then execute the tools, then synthesize, without re-injecting each observation.

## In detail
ReWOO removes ReAct's observation step and decouples reasoning from external observations. It is built from three modules: Planner (decomposes the task into sub-questions, sets the blueprint), Worker (calls external tools to collect evidence without calling the LLM back to "think") and Solver (synthesizes plans and evidence into the final answer). Because each ReAct tool call re-includes the whole history, ReWOO saves roughly 80% of tokens at equivalent or slightly higher performance. A measured example on HotpotQA: ReWOO reaches 42.4% accuracy with 2,000 tokens versus 40.8% with 10,000 tokens for ReAct. ReWOO is also more robust when a tool fails (a partial answer instead of an infinite loop). It does fail, however, on exploratory/poorly structured tasks (e.g. Python debugging), facing "unknown unknowns."

## Example
Question: pack for a flight New York → Chicago tomorrow, then a car trip to Milwaukee the next day. ReAct chains three separate thought-action-observation cycles (NY weather, then Chicago, then Milwaukee) before concluding "plan for several layers." ReWOO plans all three weather queries upfront, then the Worker calls the APIs in tight sequence or in parallel without "thinking," and the Solver aggregates. If the Chicago API fails, ReWOO returns at least a partial answer (NY + Milwaukee) instead of looping forever on the failing endpoint.

## Tradeoff / insight
The token saving comes at the cost of reactivity: the plan is frozen before any observation, so ReWOO excels on predictable evidence ("known unknowns") and fails as soon as intermediate results should redirect the plan. Reserve it for deterministic pipelines; for the exploratory, ReAct remains preferable despite its cost.

## Primary source
Binfeng Xu et al., 2023, "official" implementation available on GitHub (no arXiv number in the source).

## See also
- [ReAct](react.md)
- [Chain-of-Thought (CoT)](chain-of-thought.md)
