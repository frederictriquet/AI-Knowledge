---
title: "MetaGPT: structured communication + executable feedback"
type: "Concept"
theme: multi-agent
level: 🔴
source_url: https://www.ibm.com/think/topics/metagpt
source_title: "What is MetaGPT?"
primary_source: "arXiv:2308.00352"
migrated_from: metagpt-pattern
---

# MetaGPT: structured communication + executable feedback

**In one sentence** — a multi-agent framework that simulates a software company, where agents exchange schematized documents (PRDs, diagrams) rather than free-form dialogue, with the engineer looping on its own tests.

## In detail
MetaGPT (technology from DeepWisdom) encodes standard operating procedures (SOPs) into prompt sequences to orchestrate a team of agents playing the roles of a software company: product manager, architect, project manager, engineer, QA engineer. Its distinctive feature: it does not use unconstrained natural language as the communication interface, but **structured communication**. Where ChatDev has its agents talk to each other, MetaGPT's communicate via structured outputs (documents, schemas, diagrams) published to a **global message pool** (a publish/subscribe mechanism). All transfers follow an established schema, which "reduces the risk of hallucination caused by idle chatter between different LLMs" and improves the success rate of code generation. The engineer agent practices **iterative programming with executable feedback**: it writes and runs its own unit tests, debugs, and retries until success or a **maximum of 3 attempts**.

## Example
A single user prompt: "Build me a React app for wealth managers, letting them review client portfolios and recommend funds, operating in the Americas, the UK and Spain." The product manager derives a typed PRD from frozen SOP instructions: "Provide up to three orthogonal goals", "3 to 5 user scenarios", "5 to 7 competing products" (Wealthfront, Personal Capital…), a prioritized P0/P1/P2 requirement pool. This PRD artifact moves on to the architect with the prompt: "Review whether this API design meets the PRD requirements." No free chat: every handoff is a schematized document.

## Tradeoff / insight
The real insight: replacing inter-agent chat with schematized artifacts (typed outputs) cuts conversational drift — it is communication by contract rather than by conversation. The test-debug loop capped at 3 attempts is a concrete anti-infinite-loop guardrail.

## Primary source
"MetaGPT: Metaprogramming for A Multi-Agent Collaborative Framework", arXiv:2308.00352.

## See also
- [ChatDev / ChatChain](chatdev-chatchain.md)
- [CrewAI](crewai.md)
