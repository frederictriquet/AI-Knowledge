---
title: "LATS (Language Agent Tree Search)"
type: "Concept"
theme: reasoning-planning
level: 🔴
source_url: https://www.ibm.com/think/topics/agentic-reasoning
source_title: "What is agentic reasoning?"
migrated_from: lats
---

# LATS (Language Agent Tree Search)

**In one sentence** — applying Monte Carlo Tree Search (MCTS) to an LLM agent's reasoning, memorizing self-reflections to guide exploration.

## In detail
LATS is an example of self-reflection sharing similarities with tree-of-thoughts reasoning in LLMs. It is inspired by Monte Carlo reinforcement learning: Monte Carlo Tree Search is adapted to LLM-based agents. LATS builds a decision tree where a state is a node and an action is a branch, traverses the tree for possible action options, and calls on a state evaluator to choose an action. It includes a self-reflection step combining its own observations and feedback from a language model to identify errors and propose alternatives; errors and reflections are stored in memory as later context. LATS excels at complex tasks (coding, interactive QA, web search/navigation) but is more resource-intensive and slower than ReAct.

## Example
Coding task: fix a function that fails its tests. The agent opens a state node (initial code), branches into several candidate actions (edit line X, add an edge case, refactor). The state evaluator runs the test suite: 3/5 pass on branch A, 5/5 on branch B. MCTS backpropagates this score, the self-reflection notes "branch A forgets the n=0 case" and stores this lesson in memory. On the next rollout, the tree favors B and avoids the already-identified error — backtracking that is impossible with a linear ReAct.

## Tradeoff / insight (for a senior)
LATS buys quality on hard tasks at the price of an explosion in cost: MCTS multiplies rollouts, and the self-reflection step adds even more LLM calls. It is the "heavy" option on the reasoning spectrum — relevant when accuracy matters more than latency and token budget, to be avoided for real-time.

## When to use it (and how)
LATS only makes sense if **all three** conditions are met: (1) the cost of an error far exceeds that of an LLM call — you accept "burning" dozens of calls to make a result reliable; (2) **you can evaluate an intermediate state** via an objective signal (passing tests, a compiler, a verifier, or a credible LLM judge) — without this compass, MCTS explores blindly and adds nothing; (3) the problem **decomposes into branching steps** where a bad early decision dooms the rest (bug fixing, web navigation, formal proof).

Without these conditions, you stay lower on the complexity scale — `1 call → CoT → Self-Consistency → ReAct → Reflexion → … → LATS`. In the vast majority of cases, [Self-Consistency](self-consistency.md) (N attempts + vote) or [Reflexion](reflexion.md) (retry after critiquing the failure) give 80% of the benefit for a fraction of the complexity. LATS is the last resort, when you really need backtracking over a persistent tree.

On the implementation side: **never rewrite MCTS yourself.** The 4 steps (UCT selection, expansion, simulation, backpropagation) are delicate and already solved — **LangGraph** (a near-turnkey LATS tutorial) and **LlamaIndex** (`LATSAgentWorker`) provide the algorithm. What you contribute is limited to three functions: the **generation of candidate actions**, the **evaluation of a node** (the judge/verifier), and the **execution of an action** in the environment. The tree, the exploration/exploitation tradeoff, and the backtracking are the framework's responsibility — not yours, and especially not the LLM's, which is only called as a component (actor, judge, critic).

## Primary source
"Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models," arXiv, 6 June 2024.

## See also
- [Self-reflection / Reflexion](reflexion.md)
- [Tree of Thoughts (ToT)](tree-of-thoughts.md)
- [ReAct](react.md)
