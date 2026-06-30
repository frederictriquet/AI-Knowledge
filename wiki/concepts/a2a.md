---
title: "A2A (Agent2Agent)"
type: "Concept"
theme: interop-protocols
level: 🟡
source_url: https://www.ibm.com/think/topics/agent2agent-protocol
source_title: "What is the A2A (Agent2Agent) protocol?"
---

# A2A (Agent2Agent)

**In one sentence** — the agent↔agent protocol (Google, April 2025, now under the Linux Foundation) where each agent publishes a discoverable Agent Card, then communicates over JSON-RPC 2.0 on HTTPS with SSE for streaming.

## In detail
A2A is an open communication protocol for multi-agent systems, launched by Google in April 2025 and hosted by the Linux Foundation. It acts as a messaging layer that lets agents of distinct architectures "talk" to each other; it is complementary to MCP (A2A for agent-to-agent, MCP for model-to-tools). Components: an A2A client (the client agent that delegates), an A2A server (a remote agent exposing an HTTP endpoint), the **Agent Card** (JSON metadata: name, description, version, URL, modalities, authentication), Task (lifecycle: submitted, working, input-required, completed, failed), Message, Artifact and Part (TextPart, FilePart, DataPart). A three-step workflow: **discovery** (fetching the cards of remote agents), **authentication** (OpenAPI schemes: API keys, OAuth 2.0, OpenID Connect), **communication** (HTTPS + JSON-RPC 2.0). Long-running tasks: push notifications to a webhook; large outputs: SSE streaming. In practice, the card is exposed at `/.well-known/agent-card.json`, and BeeAI provides A2AServer/A2AAgent adapters.

## Example
A retail store illustrates the MCP/A2A complementarity: the inventory agent uses MCP to query product databases and stock levels. As soon as it detects a stockout, it alerts an internal ordering agent, which switches to A2A to talk to the agents of external suppliers and trigger the order. The source compares the Agent Card to a résumé or LinkedIn profile: it is the discoverable "business card" that lets the ordering agent pick the right supplier. Beyond immediate replies, A2A handles long-running tasks (hours/days) via push notifications to a webhook if the client disconnects.

## Tradeoff / insight (for a senior)
A2A treats agents as **opaque** (no exposure of their memory or proprietary logic): good for cross-organization confidentiality, but discovery rests entirely on the quality of the Agent Card. Tradeoff vs ACP: A2A is JSON-RPC/HTTPS and "optimized for the Google ecosystem"; ACP aims for lightweight REST and neutrality. Both merged under the Linux Foundation.

## Primary source
Launched by Google (April 2025), Linux Foundation, official site a2aproject.github.io/A2A/ and examples github.com/a2aproject/a2a-samples.

## See also
- [acp](acp.md)
- [mcp](mcp.md)
