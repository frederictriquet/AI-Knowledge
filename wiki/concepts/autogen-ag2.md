---
title: "AutoGen & AG2"
type: "Concept"
theme: frameworks-tooling
level: 🟢
source_url: https://www.ibm.com/think/topics/autogen
source_title: "What is AutoGen?"
---

# AutoGen & AG2

**In one sentence** — Microsoft's multi-agent framework for asynchronous conversations between agents (an AssistantAgent that "thinks," a UserProxyAgent that executes), extended by a community fork, AG2.

## In detail
Microsoft AutoGen is an open-source framework out of Microsoft Research for building AI agents and applications, simplifying the construction of LLM-based multi-agent systems. Its architecture has **three layers**: **Core** (message passing, event-driven agents, local or distributed execution — the "plumbing" that lets agents talk to each other and react to triggers); **AgentChat**, which assumes conversational agents and provides "template" teams pairing an **AssistantAgent** (which uses LLMs to reason) and a **UserProxyAgent** (code execution and tool use); and **Extensions** (LocalSearchTool, MultimodalWebSurfer, AutoGenBench, the no-code AutoGen Studio). An **award-winning paper published in 2024 by Chi Wang (Microsoft) and other researchers** demonstrated the applicability to real-world problems (supply chain, online decision-making). On **AG2**: presented as an "open-source AgentOS," it is essentially version 0.2.34 of AutoGen continued under a different name — a **community-driven** fork (Chi Wang having left Microsoft for Google DeepMind), with contributors from Meta, IBM and universities.

## Example
A concrete workplace-safety case demonstrated on GitHub: AutoGen examines, in real time, the images from a factory camera to detect workers without a helmet, and an automation overlays a red bounding box on the image to alert the safety staff. On the enterprise side, IBM engineers Abuelsaad and Gutowska built a multi-agent RAG app where six specialized agents (planning, research assistant, report generator…) "divide and conquer" a local corpus — each agent being scalable separately as soon as it becomes a bottleneck.

## Tradeoff / insight (for a senior)
Pure vocabulary: the AssistantAgent / UserProxyAgent pair = separation of reasoning / execution, an already-known pattern. Note: the AutoGen (Microsoft) vs AG2 (community) split is a governance risk to weigh before adopting either.

## Primary source
Award-winning paper by Chi Wang et al., 2024 (named reference but no DOI available).

## See also
- [crewai](crewai.md)
- [langgraph](langgraph.md)
