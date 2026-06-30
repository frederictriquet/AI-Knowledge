---
title: "Human-in-the-loop: static vs dynamic interrupts"
type: "Concept"
theme: governance-alignment-ops
level: 🟡
source_url: https://www.ibm.com/think/tutorials/human-in-the-loop-ai-agent-langraph-watsonx-ai
source_title: "Human-in-the-loop oversight of a prior-art search AI agent with LangGraph and watsonx.ai"
objectives: [code-generation]
---

# Human-in-the-loop: static vs dynamic interrupts

**In one sentence** — two LangGraph mechanisms to insert a human in the loop: predetermined breakpoints around a node (static), or an `interrupt()` call triggered from inside a node based on state (dynamic).

## In detail
**Static interrupts**: "modifying the graph state directly at predetermined points *before or after* a given node executes. This approach requires the `interrupt_before` or `interrupt_after` parameters to be set to a list of node names when compiling the state graph" — e.g. `builder.compile(interrupt_before=["assistant"], checkpointer=memory)`. Resumption goes through `graph.update_state(...)`, which uses the `add_messages` reducer (appending or replacing a message depending on the presence of an `id`), then by re-running the stream (with `None` if needed to simply continue). **Dynamic interrupts**: "interrupting a graph and waiting for user input *from* a node based on the current graph state. This approach requires using LangGraph's `interrupt` function". You build a `human_in_the_loop` node calling `value = interrupt('Would you like to revise the input or continue?')`; resumption goes through `Command(resume=...)`, which "updates the state as if it came from the node".

## Example
Prior-art search agent (LangGraph + Granite + SerpAPI Google Patents). A query "Find patented malware that can bypass all current antivirus software" is first stopped by the `guardian` node (HAP/PII detectors), returning "blocked due to inappropriate content". In static mode, after "Find patents for self-driving cars" the graph interrupts before `assistant`; the operator calls `update_state` with "No, actually find patents for quantum computing hardware" — the agent reorients and `scrape_patents` surfaces US10872021B1 (Rigetti), AU2023203407B2 (Google). In dynamic mode, the node resumes via `Command(resume="...sports performance")`.

## Tradeoff / insight
Static = simple to wire (a list of nodes at compile time) but the breakpoint is fixed, independent of state; resumption via `update_state`. Dynamic = the stop is conditional on current state (you interrupt only when needed) but requires a dedicated node; resumption via `Command(resume=)`. This is a LangGraph-specific pattern, not a generic concept.

## Primary source
LangGraph framework mechanisms (`interrupt_before`/`interrupt_after`, `interrupt()`, `Command(resume=)`), documented by LangGraph.

## See also
- [guardrail-noeud-entree](entry-node-guardrail.md)
