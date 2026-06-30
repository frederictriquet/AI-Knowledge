---
title: "ACP (Agent Communication Protocol)"
type: "Concept"
theme: interop-protocols
level: 🟡
source_url: https://www.ibm.com/think/topics/agent-communication-protocol
source_title: "What is ACP (Agent Communication Protocol)?"
---

# ACP (Agent Communication Protocol)

**In one sentence** — the agent↔agent protocol from IBM's BeeAI, built on lightweight REST/HTTP (vs JSON-RPC), asynchronous by default, with offline discovery; it merged with A2A under the Linux Foundation.

## In detail
ACP is an open standard for agent-to-agent communication, introduced by IBM's BeeAI and now under the Linux Foundation. Components: an ACP client and an ACP server; the client sends requests through a RESTful API over HTTP, and the server hosts one or more agents behind a single HTTP endpoint, routing the tasks. Key features: **REST communication** (standard HTTP conventions, usable with cURL, Postman or a browser; an SDK is available but not required), **offline discovery** (metadata embedded in distribution packages, suited to scale-to-zero environments; online discovery is also possible through manifests at well-known URLs), **async by default** (synchronous is supported) and acceptance of varied message types (audio, images, text, video, binary). Notably, ACP positions itself against MCP on this point — the more complex JSON-RPC vs the lighter REST design. A tutorial illustrates a multi-agent workflow with BeeAI + crewAI where ACP serves as a shared messaging layer (JSON + metadata) via the `acp-sdk`.

## Example
A cross-organization case: a manufacturer (production-planning agent) must quote the lead time for a custom piece of equipment to produce a bid; it has to query a logistics provider's agent (transit estimate, carrier availability). Without ACP, this requires a custom integration between the two APIs, with manual handling of authentication and formats — fragile and not reproducible. With ACP, each organization wraps its agent in an ACP interface: the manufacturer sends order + destination, the logistics provider returns shipping options and lead times, without exposing its internal workings. On the code side, a compatible agent is defined by decorating a function with `@server.agent()` then calling `server.run()`.

## Tradeoff / insight (for a senior)
Deliberately designed to be lightweight and vendor-neutral: REST + async by default fits long-running tasks and decentralized cross-organization contexts. Offline discovery (metadata in the package) is the rare and useful detail: an agent stays discoverable even when off. Watch point: ACP joined A2A under the Linux Foundation — track the convergence of the SDKs.

## Primary source
Introduced by IBM's BeeAI, official site agentcommunicationprotocol.dev, repository github.com/i-am-bee/acp.

## See also
- [beeai](beeai.md)
- [a2a](a2a.md)
