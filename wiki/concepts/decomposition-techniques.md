---
title: "Decomposition techniques"
type: "Concept"
theme: prompting
level: 🔴
source_url: https://arxiv.org/abs/2406.06608
source_title: "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques"
objectives: [code-generation]
migrated_from: decomposition-techniques
---

# Decomposition techniques

**In one sentence** — explicitly break a complex problem into simpler sub-problems, then solve them one by one, to make the final answer more reliable.

## What the source says
The Decomposition family (§2.2.3) groups the techniques that break a complex problem into simpler sub-questions. The report notes that, while CoT often decomposes naturally, doing so explicitly further improves problem-solving ability. Least-to-Most Prompting (Zhou et al.) first asks to split the problem into sub-problems without solving them, then solves them sequentially, accumulating the answers. Decomposed Prompting / DECOMP (Khot et al.) shows the LLM, in few-shot, how to call functions (string split, web search...) to handle the sub-problems. Plan-and-Solve (Wang et al.) is an improved Zero-Shot CoT that asks for a plan before executing it step by step. Tree-of-Thought / ToT (Yao et al., Long) builds a tree search by generating and evaluating multiple thoughts. Recursion-of-Thought (Lee and Kim) delegates each sub-problem to a new call. Program-of-Thoughts (Chen et al.) generates code executed by an interpreter; Faithful Chain-of-Thought (Lyu et al.) mixes natural and symbolic language; Skeleton-of-Thought (Ning et al.) parallelises via an answer skeleton.

## Example
DECOMP (Khot et al.) illustrates the routing concretely: in few-shot, the model is shown atomic functions (`split`, `str_pos`, internet search), each often implemented as a separate LLM call. Faced with a symbolic-manipulation task, the model does not solve everything in one block: it decomposes into function calls and delegates, outperforming Least-to-Most on some tasks. Recursion-of-Thought goes further by emitting a special token that sends each sub-problem into a new call whose answer is reinserted, which allows handling a problem exceeding the context window (gains reported on arithmetic and algorithmic tasks).

## Why it matters
This family formalises a whole range of explicit-splitting strategies (Least-to-Most, DECOMP, Plan-and-Solve, Program-of-Thoughts), including the use of code and external function calls, beyond Tree of Thoughts and prompt chaining.

## Key techniques
- Least-to-Most Prompting (Zhou et al.) — split then solve sequentially.
- Decomposed Prompting / DECOMP (Khot et al.) — sub-problems routed to functions.
- Plan-and-Solve Prompting (Wang et al.) — plan before executing step by step.
- Tree-of-Thought / ToT (Yao et al., Long) — tree search over thoughts.
- Recursion-of-Thought (Lee and Kim) — sub-problem delegated to a new call.
- Program-of-Thoughts (Chen et al.) — code generated and executed as reasoning.
- Faithful Chain-of-Thought (Lyu et al.) — natural + symbolic reasoning.
- Skeleton-of-Thought (Ning et al.) — skeleton then parallelised resolution.

## See also
- [Tree of Thoughts](tree-of-thoughts.md)
- [Prompt chaining](prompt-chaining.md)
- [CodeAct (including PAL)](codeact.md)
- [full paper](../../sources/prompt-report/md/prompt-report.md)
