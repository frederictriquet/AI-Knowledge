---
title: "BeeAI"
type: "Concept"
theme: frameworks-tooling
level: 🟢
source_url: https://www.ibm.com/think/topics/beeai
source_title: "What is BeeAI?"
migrated_from: beeai
---

# BeeAI

**In one sentence** — a framework-agnostic orchestration layer from IBM, built on the ACP protocol, that discovers, runs and shares agents regardless of their frameworks, isolating each agent in its own container.

## In detail
BeeAI is an open-source platform to discover, run and share AI agents in a centralized way, across all frameworks. Developed by IBM Research and hosted by the Linux Foundation, it is built on the ACP (Agent Communication Protocol). It addresses three challenges: siloed ecosystems, limited scalability, fragmented discovery — through a browsable agent catalog and a centralized discovery hub. BeeAI uses ACP to standardize agent usage regardless of framework; you can import local agents or agents from GitHub, LangChain, etc. Each agent runs in its own container with defined resource limits. The key components: containerized agents communicating via ACP, a BeeAI server (orchestration, lifecycles, routing, telemetry), a CLI and a UI, a Python integration through the ACP SDK. Observability is built in: telemetry collection with OpenTelemetry, sent to an Arize Phoenix instance. BeeAI favors a local-first experience giving the user full control of their data.

## Example
A typical setup via the interactive configuration assistant: entering API keys, model-selection recommendations, connection tests, and provider-specific options such as Ollama's context window. Pluggable LLMs include Anthropic's Claude, OpenAI's GPT, DeepSeek and IBM's watsonx, plus Meta's Llama3 through a local Ollama connection. At runtime, you import an agent from GitHub or LangChain, launch it in interactive mode (multi-line input to paste a Python snippet), and the container logs stream in real time — OTEL telemetry routed to Arize Phoenix in parallel.

## Tradeoff / insight (for a senior)
The real differentiator is container isolation (resource limits, packaging of heterogeneous agents working around incompatibilities) coupled with out-of-the-box OTEL/Phoenix telemetry. BeeAI is not yet another framework but a layer on top of frameworks: the value is interoperability, at the price of a dependency on the maturity of ACP/A2A.

## Primary source
beeai.dev and the ACP documentation. See also the i-am-bee GitHub repository.

## See also
- [acp](acp.md)
- [a2a](a2a.md)
