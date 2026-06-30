---
title: "Decomposition-first vs interleaved"
type: "Concept"
theme: prompting
level: 🟡
source_url: https://www.ibm.com/think/topics/ai-agent-planning
source_title: "What is AI agent planning?"
---

# Decomposition-first vs interleaved

**In one sentence** — plan everything up front then execute without re-reasoning (ReWOO) versus planning and revising at every observation (ReAct).

## In detail
ReAct is a thought-action-observation methodology where reasoning generates a sequence of steps; ReWOO, RAISE and Reflexion are emerging frameworks "each with its own advantages and disadvantages". ReAct follows a think-act-observe cycle: the system observes what it generates before reasoning about it again, but each tool call must re-include the entire history, hence heavy token consumption. ReWOO ("reasoning without observation") decouples reasoning from observations: the **Planner** module lays out the whole plan in advance, the **Worker** executes the tool calls without costly re-reasoning, and the **Solver** synthesises. Reported result: accuracy on par with ReAct (42.4% vs 40.8% on HotpotQA) with ~80% fewer tokens (2,000 vs 10,000). ReWOO is also more robust to a tool failure, but fails on unpredictable problems ("unknown unknowns", e.g. iterative Python debugging).

## Example
A favourable ReWOO case: a multi-hop HotpotQA question ("in which city was the director of film X born?"). The Planner lays out the plan in advance — find the director, then their birth city; the Worker runs the two searches; the Solver synthesises. No history is re-injected between steps. An unfavourable case cited: iterative Python debugging, an "unknown unknown" where the error message at step N redefines step N+1 — there, the plan frozen in advance collapses and only ReAct, which re-reasons after each observation, holds up.

## Tradeoff / insight
The structuring trade-off of agentic planning. Decomposing everything up front is unbeatable on cost and robustness when the required evidence is regular and predictable; planning on the fly costs more tokens but remains the only viable option for exploratory work, where each observation invalidates the previous plan.

## Primary source
ReWOO described by Binfeng Xu et al., 2023 (reference implementation on GitHub); quoted seed prompt: "For the following task, devise plans that can solve the problem step by step."

## See also
- [Planning: goal / state / sequencing](goal-state-action-planning.md)
- [Probabilistic planning](probabilistic-planning.md)
