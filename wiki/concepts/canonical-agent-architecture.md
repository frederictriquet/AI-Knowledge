---
title: "The canonical framework: Agent = LLM + Planning + Memory + Tools"
type: "Concept"
theme: tools-function-calling
level: 🔴
source_url: https://lilianweng.github.io/posts/2023-06-23-agent/
source_title: "LLM Powered Autonomous Agents"
objectives: [code-generation]
---

# The canonical framework: Agent = LLM + Planning + Memory + Tools

**In one sentence** — the reference decomposition of an autonomous agent: an LLM plays the role of the brain (controller), supported by three components — planning, memory and tool use.

## What the source says
Weng posits that an LLM-powered autonomous agent uses the model as a brain, complemented by three key components. **Planning** covers subgoal decomposition and self-reflection on past actions to learn from mistakes. **Memory** splits into short-term memory (in-context learning) and long-term memory (retention and recall of near-infinite information through an external vector store and fast retrieval). **Tool use** lets the agent call external APIs to fill what is missing from the model's weights (current information, code execution, proprietary sources). Weng cites AutoGPT, GPT-Engineer and BabyAGI as inspiring demonstrators, and presents the LLM as a "general problem solver" that goes beyond mere text generation.

## Example
AutoGPT instantiates the schema: its system message defines the LLM as the brain (a `thoughts` block with `reasoning`, `plan`, `criticism`) and lists 20 tool-commands (`google`, `browse_website`, `write_to_file`, `execute_python_file`, `start_agent`…). Planning is explicit there ("Aim to complete tasks in the least number of steps"), as is memory: "~4000 word limit for short term memory […] immediately save important information to files" — long-term memory delegated to the file system for lack of context. The output is forced into JSON parsable by `json.loads`.

## Why it matters
Weng provides a unified, hierarchical mental map (brain + 3 components) that explicitly articulates the sub-mechanisms (decomposition, reflection, ST/LT, APIs) into a single reference schema.

## Primary sources (cited by Weng)
- AutoGPT (Significant-Gravitas) — autonomous agent with the LLM as the main controller.
- GPT-Engineer (Anton Osika) — generation of a complete code repository from a single instruction.
- BabyAGI (Yohei Nakajima) — task-loop agent demonstrator.

## See also
- [Short-/long-term memory](short-vs-long-term-memory.md)
- [Planning](goal-state-action-planning.md)
- [Tool calling](tool-calling.md)
- [Agent types](five-agent-types-taxonomy.md)
- [full post](https://lilianweng.github.io/posts/2023-06-23-agent/)
