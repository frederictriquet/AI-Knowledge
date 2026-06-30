---
title: "LLM Compiler (parallel function calling)"
type: "Concept"
theme: tools-function-calling
level: 🟡
source_url: https://arxiv.org/abs/2312.04511
---

# LLM Compiler (parallel function calling)

**In one sentence** — plan a **DAG of tool calls** and execute in parallel those that are independent, instead of chaining them sequentially like ReAct.

## The idea
Inspired by compilers: a *planner* decomposes the task into calls with their dependencies (a graph), a *task-fetching unit* launches in **parallel** everything that depends on nothing, a *joiner* aggregates the results. You remove the sequential round trips of the think-act-observe scheme when the subtasks are independent.

## How the plan and execution are expressed
Unlike MRKL (where the decision is entirely neural), LLM Compiler is an **explicit split into two layers** — this is the core of the compiler analogy. The **semantic decision** is entrusted to the LLM through **prompting**: the *planner* (few-shot) emits the DAG, the *joiner* (LLM) decides whether it is done or whether to re-plan. But the **execution mechanics** — scheduling, parallelism, dependency resolution — are taken out of the LLM and entrusted to **deterministic code** (the *task-fetching unit*), exactly as a CPU executes in dependency order.

Concretely, the planner emits via prompting a **plan syntax** where each task is numbered and references previous outputs via placeholders (`$1`, `$2`…):

```
1. search("weather Paris")
2. search("weather Lyon")
3. compare($1, $2)        # depends on 1 and 2
```

The runtime sees that `1` and `2` depend on nothing → launches them **in parallel**, then substitutes `$1`/`$2` with the real results and unblocks `3`. This variable substitution and *out-of-order* scheduling are **mechanical** (code, zero LLM calls) — it is this decoupling that buys the latency and the cost.

## Example
On the paper's benchmarks (UC Berkeley), LLMCompiler measures, against ReAct, up to **3.7× less latency**, **6.7× less cost**, and **~9% more accuracy**. The accuracy gain also comes from a side effect: by taking scheduling out of the LLM, you remove ReAct's pathologies (call repetition, premature interruption of reasoning by observations). The reference code is published under `SqueezeAILab/LLMCompiler` (accepted at ICML 2024).

## Tradeoff / when to use it
A gain in **latency and cost** when several tools can run in parallel (e.g. querying three weather APIs). Same intuition as the native *parallel tool calling* of recent APIs and as ReWOO's decoupling. Useless, even counterproductive, if the steps are intrinsically sequential (each call depends on the previous one).

## Primary source
Kim et al., 2023, *An LLM Compiler for Parallel Function Calling*, arXiv:2312.04511 (UC Berkeley). *(arXiv verified — HTTP 200 + title)*

## See also
- [rewoo](rewoo.md)
- [decomposition-first-vs-interleaved](decomposition-first-vs-interleaved.md)
