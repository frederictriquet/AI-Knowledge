---
title: "MCP (Model Context Protocol)"
type: "Concept"
theme: interop-protocols
level: 🔴
source_url: https://www.ibm.com/think/topics/model-context-protocol
source_title: "What is MCP?"
---

# MCP (Model Context Protocol)

**In one sentence** — the open standard (Anthropic, 2024) that connects a model to external tools/data via a host/client/server trio over JSON-RPC 2.0; the "USB-C" of tool integration, not an orchestration framework.

## In detail
MCP is a standardization layer that lets AI applications communicate with external services (tools, databases, predefined models), introduced by Anthropic in 2024. It is not a framework for agents but an integration layer: it complements LangChain, LangGraph, BeeAI, LlamaIndex, crewAI without replacing them — it is the LLM that decides which tool to call. The client/server architecture has three components: the **MCP host** (orchestration logic, can host several clients), the **MCP client** (a 1:1 relationship with a server, session management, parsing/errors), and the **MCP server**. Servers expose three primitives: **Resources** (return data without computation), **Tools** (side effect: computation or API request), and **Prompts** (reusable templates). The transport layer encodes messages in JSON-RPC 2.0 (requests, responses, notifications), via two transports: **stdio** (local resources, synchronous and lightweight) and streamed HTTP (*streamable HTTP*; earlier iterations used SSE).

## Example
A concrete case from the source: an AI that scans your mailbox to schedule client appointments, pushes stock-market updates, and summarizes the last hour of Slack activity to you by SMS. The problem without MCP: each provider exposes a different API, and the slightest change to a tool makes the whole workflow collapse. On the server side, the integrations exposed are, for example, Slack, GitHub, Git, Docker, or web search; on the client side, Claude.ai, Cursor, Microsoft Copilot Studio, or Postman. Extended analogy: MCP is the control board of an electrical circuit that decides which current (context, tool output) feeds the motor (the model) and when.

## Tradeoff / insight (for a senior)
The non-trivial point: MCP standardizes **tool access** (one model ↔ several tools), not inter-agent communication — hence its complementarity with A2A/ACP. The ACP team judged it unsuitable for multi-agent: no granular delta streaming, no shared multi-agent memory, an unstructured message body (any JSON schema accepted), JSON-RPC complexity + required SDK. The client↔server relationship is strictly 1:1.

## Primary source
MCP introduced by Anthropic in 2024 (open standard), Resources/Tools/Prompts primitives per the Anthropic documentation.

## See also
- [a2a](a2a.md)
- [acp](acp.md)
