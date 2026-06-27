---
title: "LangGraph"
type: "Concept"
theme: frameworks-tooling
level: 🟢
source_url: https://www.ibm.com/think/topics/langgraph
source_title: "What is LangGraph?"
migrated_from: langgraph
---

# LangGraph

**In one sentence** — LangChain's orchestration framework that models an agent workflow as a state graph (nodes, edges, cycles) with explicit state management and human-in-the-loop.

## In detail
LangGraph, created by LangChain, is an open-source framework for building, deploying, and managing complex agent workflows. It "harnesses the power of graph-based architectures" to model the relationships between components. Its key concepts: a **state** acting as a memory store that records and tracks all processed information (useful for debugging, since it centralizes the application's state); **stateful graphs** where each node is a computation step that preserves context; **cyclic graphs** (at least one cycle, essential to agent runs); **nodes** representing agents or components ("actors"); and **edges**, Python functions that determine the next node based on the current state, in conditional branches or fixed transitions. LangGraph builds on LangChain, integrates **human-in-the-loop (HITL)**, RAG, MCP servers, and offers LangGraph Studio (a visual no-code interface) as well as debugging capabilities.

## Example
A concrete example of state: an agent that monitors the weather keeps the cumulative snowfall in its "state" and emits suggestions according to how the snow evolves — debugging consists of inspecting this centralized notepad. On the production side: Norwegian Cruise Line relies on LangGraph to compile and refine AI solutions for its hosts, and services like Google Duplex use it to mimic human conversations. An emblematic multi-agent case from Joao Moura: CrewAI orchestrating, via LangGraph, the verification of emails and the drafting of replies, where dedicated agents collaborate in parallel.

## Tradeoff / insight (for a senior)
Pure vocabulary, but it is the most serious tool for **flow control**: state graph + cycles = a real state machine, where LangChain stops at linear chains. If you need loops, conditional branching, and resumption from a checkpoint, this is the right building block.

## Primary source
See the LangGraph documentation.

## See also
- [langchain](langchain.md)
- [crewai](crewai.md)
