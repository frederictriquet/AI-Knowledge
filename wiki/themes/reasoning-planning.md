---
type: index
title: "Theme — Reasoning & planning"
theme: reasoning-planning
---

# 🧠 Reasoning & planning

> ⚙️ **Generated file** by `tools/build_index.py` — do not edit by hand.

_Making a model reason, plan and self-correct._

## Concepts (22)

### 🔴 Substance / core
- **[Agent self-reflection (ReAct, Reflexion, CoH, AD)](../concepts/self-reflection-agents.md)** — the family of mechanisms by which an agent improves in a loop by revisiting its past decisions and errors, essential in real-world tasks where trial and error is unavoidable.
- **[DeepSeek-R1: RL makes reasoning emerge](../concepts/deepseek-r1-rl-reasoning.md)** — Applied directly to a base model, reinforcement learning (RL) without supervised fine-tuning is enough to make long reasoning chains and self-verification emerge spontaneously.
- **[Graph of Thoughts (GoT)](../concepts/graph-of-thoughts.md)** — reasoning is modeled as an arbitrary graph of thoughts where you can not only branch but also **merge** several thoughts, loop and refine, where Tree-of-Thoughts is limited to a tree.
- **[LATS (Language Agent Tree Search)](../concepts/lats.md)** — applying Monte Carlo Tree Search (MCTS) to an LLM agent's reasoning, memorizing self-reflections to guide exploration.
- **[Process Reward Models (Let's Verify Step by Step)](../concepts/process-reward-models.md)** — rewarding each intermediate reasoning step (process supervision) trains markedly more reliable models than rewarding only the final answer (outcome supervision).
- **[Reasoning models & test-time compute](../concepts/inference-time-scaling.md)** — gain quality by letting the model "think longer" at inference rather than by growing its weights.
- **[Source verification (anti-context-contamination)](../concepts/source-verification.md)** — an LLM step that rejects a retrieved passage as soon as it comes from an out-of-scope source, before it pollutes the context.
- **[Test-time compute: \"thinking\" as inference-time computation](../concepts/test-time-compute-thinking.md)** — "thinking" is not a metaphor: it is allocating more FLOPs at inference, with chain-of-thought letting the model use a variable amount of computation depending on the difficulty of the problem.
- **[Tree of Thoughts (ToT)](../concepts/tree-of-thoughts.md)** — generalizing CoT into a tree: generate several "thoughts" per step, evaluate them, and explore the solution space by search (BFS/DFS) with backtracking.

### 🟡 Tradeoff / intermediate
- **[Case-based reasoning](../concepts/case-based-reasoning.md)** — deciding by reusing similar past cases rather than reasoning from scratch.
- **[Chain-of-Verification (CoVe)](../concepts/chain-of-verification.md)** — the model writes an answer, derives factual verification questions from it, answers them in isolation, then corrects its answer in light of those checks.
- **[Least-to-Most prompting](../concepts/least-to-most.md)** — you explicitly decompose a problem into subproblems ordered from simplest to most complex, then solve them in sequence, each answer serving as context for the next.
- **[Probabilistic planning](../concepts/probabilistic-planning.md)** — decide under uncertainty by evaluating several possible outcomes and choosing the action with the highest expected utility.
- **[ReWOO](../concepts/rewoo.md)** — "Reasoning Without Observation": plan the whole reasoning chain internally first, then execute the tools, then synthesize, without re-injecting each observation.
- **[Self-Consistency](../concepts/self-consistency.md)** — sample several independent CoT reasoning chains then take a majority vote for the final answer, rather than relying on a single generation.
- **[Self-Refine](../concepts/self-refine.md)** — a single model produces an output, generates its own critique, then revises, in a loop, with no external signal.
- **[Self-reflection / Reflexion](../concepts/reflexion.md)** — after a failure, the agent writes a critique of what went wrong and replays the task with that critique kept in memory.
- **[Step-Back prompting](../concepts/step-back.md)** — before answering a specific question, ask the model to "step back" and formulate the underlying general concept or principle, then reason from that abstraction.

### 🟢 Overview / introductory
- **[Chain-of-Thought (CoT)](../concepts/chain-of-thought.md)** — asking the model to write its intermediate reasoning steps before the final answer, instead of answering directly.
- **[Planning: goal / state / sequencing](../concepts/goal-state-action-planning.md)** — to plan is to define a goal (the target end state), model the current state, then derive the sequence of actions that leads from one to the other.
- **[ReAct](../concepts/react.md)** — a thought → action (tool call) → observation loop, repeated until an answer is reached.
- **[Reactive / deliberative / cognitive architectures](../concepts/reactive-deliberative-cognitive-architectures.md)** — three levels of agent sophistication: a stateless reflex, a planner with a world model, or a cognitive system with memory and learning.

## Tools (1)

- **[Task Master (Taskmaster)](../tools/task-master.md)** — _CLI + MCP server (task management for agents)_
