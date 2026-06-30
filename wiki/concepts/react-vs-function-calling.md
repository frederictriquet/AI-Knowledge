---
title: "ReAct vs function calling"
type: "Concept"
theme: tools-function-calling
level: 🟡
source_url: https://www.ibm.com/think/topics/react-agent
source_title: "What is a ReAct agent?"
---

# ReAct vs function calling

**In one sentence** — function calling is faster and more economical on predictable tasks; ReAct handles the unpredictable better at the cost of reasoning-loop tokens.

## In detail
Two agentic paradigms coexist. ReAct combines chain-of-thought (CoT) reasoning with tool use, in a loop alternating thoughts, actions, and observations. Function calling, introduced by OpenAI in June 2023, tunes models to recognize when to produce a structured JSON object of call arguments. The "best" one depends on the use case: for relatively simple or predictable tasks, function calling "can run faster, save tokens, and be simpler to implement than a ReAct agent," because the tokens spent in the CoT loop would then be wasted. The trade-off: function calling offers a relative inability to customize how and when the model selects a tool, and its rigidity limits adaptation to dynamic or unpredictable scenarios, where visualizing the reasoning step by step becomes useful.

## Example
The system prompt of LangChain's prebuilt `ZERO_SHOT_REACT-DESCRIPTION` agent materializes the ReAct loop with no few-shot at all: it lists the tools (`Wikipedia`, `duckduckgo_search`, `Calculator`) then imposes the text template `Question → Thought → Action → Action Input → Observation` with the note "... (this Thought/Action/Action Input/Observation can repeat N times)," closed by `Thought: I now know the final answer` / `Final Answer:`. The reasoning transits through the `{agent_scratchpad}` — where pure function calling would directly emit the JSON of arguments without this intermediate verbalization.

## Tradeoff / insight
It is not an exclusive choice: a ReAct agent uses function calling for its actions. The real opposition is "explicit reasoning loop" vs "direct call." Pay for the ReAct loop's tokens when you need explainability, self-correction, and adaptation; save them when the path is known in advance.

## Primary source
"In scenarios involving relatively simple (or at least predictable) tasks, function calling can run faster, save tokens, and be simpler to implement than a ReAct agent." ([source](https://www.ibm.com/think/topics/react-agent))

## See also
- [Tool calling / function calling](tool-calling.md)
