---
title: "LlamaIndex"
type: "Concept"
theme: frameworks-tooling
level: 🟢
source_url: https://www.ibm.com/think/insights/top-ai-agent-frameworks
source_title: "AI agent frameworks: choosing the right foundation for your business"
migrated_from: llamaindex
---

# LlamaIndex

**In one sentence** — an agent orchestration framework whose basic unit is the event-driven *workflow*: steps triggered by events and connected by a shared context, with no predefined paths between them.

## In detail
LlamaIndex is an open-source data-orchestration framework for building generative and agentic AI solutions, offering preconfigured agents and tools. The central mechanism is *workflows*, designed to develop multi-agent systems. Three elements make up a workflow: *steps* (actions specific to each agent, the basic building blocks), *events* (which trigger steps and serve as a means of communication between them), and *context* (shared throughout the workflow, allowing steps to store, retrieve, and pass data and to maintain state). This event-driven architecture enables asynchronous execution. Unlike a graph-based architecture, the paths between steps do not need to be defined, allowing more flexible transitions. LlamaIndex workflows are therefore well suited to dynamic agents that must often return to earlier steps or branch toward multiple steps.

## Example
A document-review workflow: a `parse` step emits a `ChunkReady` per section; each event triggers in parallel an `evaluate` step that drops its verdict into the shared context. If a chunk is judged incomplete, the step re-emits a `ChunkReady` to `parse` — a backward loop with no declared edge. A final step, subscribed to the fact that all verdicts are present in the context, emits a `StopEvent`. No wired graph: the branching and backtracking emerge solely from the published events.

## Tradeoff / insight (for a senior)
The explicit contrast with LangGraph is the insight: graph (nodes/edges wired in advance, granular control) vs events (coupling via publish/subscribe, emergent paths). LlamaIndex pays for flexibility with reduced traceability of the control flow; LangGraph pays for control with the rigidity of the graph. Choose depending on whether the transitions are known in advance or not.

## Primary source
See the LlamaIndex Workflows documentation and GitHub repository.

## See also
- [semantic-kernel](semantic-kernel.md)
- [orchestration-types](orchestration-types.md)
