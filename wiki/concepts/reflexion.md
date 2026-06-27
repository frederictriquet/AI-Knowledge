---
title: "Self-reflection / Reflexion"
type: "Concept"
theme: reasoning-planning
level: 🟡
source_url: https://www.ibm.com/think/topics/agentic-reasoning
source_title: "What is agentic reasoning?"
objectives: [code-generation]
migrated_from: reflexion
---

# Self-reflection / Reflexion

**In one sentence** — after a failure, the agent writes a critique of what went wrong and replays the task with that critique kept in memory.

## In detail
Self-reflection is a mechanism by which agentic AI evaluates and perfects its reasoning abilities. LATS illustrates it concretely: it integrates a self-reflection step combining the agent's observations and a language model's comments to identify reasoning errors and recommend alternatives; these errors and reflections are stored in memory as context for subsequent tasks. Reflexion is among the emerging frameworks alongside ReWOO and RAISE, "each with its own advantages and disadvantages." ReAct contributed to later advances "such as Reflexion, which led to modern reasoning models."

## Example
A ReAct loop tasked with answering an interactive question spins in circles: it regenerates the same reasoning and the same actions, up to the infinite loop described as ReAct's main flaw. Self-reflection breaks this cycle: after the failure, the agent confronts its own observations with the comment of an LLM-critic, which diagnoses "you keep querying the same source without success, change angle." This reflection is filed in memory and re-injected as context at the next replay, preventing the error from repeating — the exact mechanism that LATS embodies in the agentic literature.

## Tradeoff / insight
The reflective loop adds LLM cycles (hence latency and cost) to gain success rate on tasks where the agent can detect its own errors. It assumes an exploitable failure signal (test, feedback); without a reliable verdict, the "critique" risks reinforcing a wrong path. Reflexion is mainly described through LATS in the agentic literature.

## Primary source
Shinn et al. 2023, "Reflexion: Language Agents with Verbal Reinforcement Learning." In the agentic literature, self-reflection is mainly addressed through LATS.

## See also
- [LATS (Language Agent Tree Search)](lats.md)
- [ReAct](react.md)
- [RAISE](raise.md)
