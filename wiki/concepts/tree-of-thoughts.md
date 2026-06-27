---
title: "Tree of Thoughts (ToT)"
type: "Concept"
theme: reasoning-planning
level: 🔴
source_url: https://www.ibm.com/think/topics/tree-of-thoughts
source_title: "What is tree of thoughts?"
primary_source: "arXiv:2305.10601"
migrated_from: tree-of-thoughts
---

# Tree of Thoughts (ToT)

**In one sentence** — generalizing CoT into a tree: generate several "thoughts" per step, evaluate them, and explore the solution space by search (BFS/DFS) with backtracking.

## In detail
The ToT framework rests on four components: thought decomposition, thought generation (sampling or proposing), state evaluation (a scalar value or a vote), and a search algorithm (BFS which explores all nodes of a level, DFS which digs into a branch before backtracking). A self-evaluation by the LLM validates each step and allows returning to an earlier node in case of a dead end. The TouT extension (Tree of Uncertain Thoughts, Monte Carlo Dropout to quantify uncertainty) is also documented. Limits: compute overhead, implementation complexity (a prompter agent, a checker, memory, a controller), and above all an efficiency critique: ToT explores low-value paths, failing to prioritize promising branches. The "Thought of Search" alternative integrates planning heuristics and information gain. Case studies: sudoku, the 24 puzzle, creative writing, 5×5 crosswords.

## Example
The source illustrates ToT with sudoku solving: the model explores different digit placements by trial and error, backtracks as soon as a number leads to a contradiction, and tries another number until the grid is solved — mimicking human trial and error. Thought decomposition is shown via trip planning: one thought = choosing the destination, the next = the mode of transport, the last = the lodging, each step being evaluable in isolation. On the 24 puzzle (arithmetic), exploring several calculation paths markedly raised the success rate.

## Tradeoff / insight (for a senior)
ToT increases the success rate on highly combinatorial problems (puzzles, planning) at the price of an explosion of LLM calls that grows with breadth × depth. "Vanilla" ToT wastes budget on dead branches: the efficiency critique (Thought of Search) suggests that well-chosen search heuristics often beat naive tree exploration.

## Primary source
Yao et al. 2023, "Tree of Thoughts: Deliberate Problem Solving with Large Language Models", arXiv:2305.10601; repository [princeton-nlp/tree-of-thought-llm](https://github.com/princeton-nlp/tree-of-thought-llm); Mo & Xin 2023 (TouT, arXiv:2309.07694); Katz et al. 2024 (Thought of Search, NeurIPS vol. 37).

## See also
- [Chain-of-Thought (CoT)](chain-of-thought.md)
- [Self-Consistency](self-consistency.md)
- [LATS (Language Agent Tree Search)](lats.md) — on the agent side, ToT is the conceptual backdrop of LATS
