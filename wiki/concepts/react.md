---
title: ReAct
type: "Concept"
theme: reasoning-planning
tags: [agents, tools, reasoning]
level: 🟢
source_url: https://www.ibm.com/think/topics/react-agent
source_title: "What is a ReAct agent? — IBM Think"
primary_source: "Yao et al., ReAct: Synergizing Reasoning and Acting in Language Models (arXiv:2210.03629)"
---

# ReAct

**In one sentence** — a thought → action (tool call) → observation loop, repeated until an answer is reached.

## In detail
ReAct ("Reasoning and acting") combines chain-of-thought reasoning (CoT) with the use of external tools through an interleaved thought/action/observation loop. The agent generates a thought, runs an action (tool, API, search), observes the result, then feeds that observation back into the next thought. The loop ends after a maximum number of iterations or when a condition is met; note that ReAct can regenerate the same reasoning and actions, which may cause infinite loops. LangGraph's `ZERO_SHOT_REACT-DESCRIPTION` system prompt follows the Question/Thought/Action/Observation/Final Answer format. ReAct depends heavily on a central LLM that is strong at reasoning and instruction-following.

## Example
The `ZERO_SHOT_REACT-DESCRIPTION` system prompt exposes three tools (Wikipedia, duckduckgo_search, Calculator) then enforces the format: `Question / Thought / Action / Action Input / Observation`, where the `Thought/Action/Action Input/Observation` block can repeat N times before `Thought: I now know the final answer` then `Final Answer`. The source's analogy: packing for a trip — think "What will the weather be?", act (check the forecast), observe "It's going to be cold", then adjust to a surprise ("my warm clothes are in the attic"). The `{agent_scratchpad}` acts as a notepad where the reasoning accumulates.

## Tradeoff / insight (for a senior)
For simple/predictable tasks, function calling is faster, cheaper in tokens and simpler; ReAct is only justified for complex or unpredictable reasoning, where step-by-step traceability and dynamic adaptability are worth the extra tokens and the risk of looping.

## Primary source
Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models", arXiv:2210.03629 (10 March 2023).

## See also
- [ReWOO](rewoo.md)
- [Self-reflection / Reflexion](reflexion.md)
- [Chain-of-Thought (CoT)](chain-of-thought.md)
