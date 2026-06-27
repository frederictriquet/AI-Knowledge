---
title: "AgentOps"
type: "Concept"
theme: governance-alignment-ops
level: 🔴
source_url: https://www.ibm.com/think/topics/agentops
source_title: "What is AgentOps?"
migrated_from: agentops
---

# AgentOps

**In one sentence** — the DevOps/MLOps of agents: instrumenting execution at the session → trace → span level to make a non-deterministic black box observable, with cost and latency per step and multi-LLM routing.

## In detail
AgentOps ("Agent Operations") refers to "a set of emerging practices focused on managing the lifecycle of autonomous AI agents," combining "the principles of operational disciplines such as DevOps and MLOps." The goal: to "bring observability and reliability" and to "examine the black box of interactions." Monitoring happens "at the session, trace or span level"; developers can "review agent execution step by step," examine "tool usage patterns," "which APIs were used," "the latency at each step" and "the final LLM cost." The idea (Adam Silverman, Agency AI) that "by using different LLMs for different tasks, this cost could be reduced" is also put forward. The ecosystem has many tools (Agenta, LangSmith, Trulens). IBM Research built its solution "on the OpenTelemetry (OTEL) standards, an open-source SDK," with an open, extensible analytics platform, and analyses themselves powered by AI ("visualize multi-trace workflows and explore trajectories").

## Example
An IBM case: a customer-support agent made of several LLMs that monitors incoming emails, searches the enterprise knowledge base and creates tickets autonomously. Debugging becomes "answering questions" about the trace: did the agent consult the right support doc? Which APIs did it call, in what order? What latency at each step, what final LLM cost? The source's analogy: leaving an agent to run without reviewing its traces is "like giving a teenager a credit card without looking at the statement." The cited study counts 17 GitHub tools for supporting this practice.

## Tradeoff / insight (for a senior)
The nugget: this is classic distributed observability (OTEL's session/trace/span) applied to non-deterministic systems. The OTEL foundation is the right engineering choice — automatic multi-framework instrumentation, no vendor lock-in, extensible metrics. Cost and latency *per step* enable the concrete tradeoff of "multi-LLM routing" (an expensive model for hard tasks, a cheap model elsewhere).

## Primary source
IBM Research post (research.ibm.com/blog/ibm-agentops-ai-agents-observability). Underlying standard: OpenTelemetry (OTEL).

## See also
- [Trajectory evaluation](evaluation-trajectoire.md)
