---
title: "Other protocols: ANP / AG-UI / Agora / LMOS"
type: "Concept"
theme: interop-protocols
level: 🟡
source_url: https://www.ibm.com/think/topics/ai-agent-protocols
source_title: "What are AI agent protocols?"
migrated_from: autres-protocoles
---

# Other protocols: ANP / AG-UI / Agora / LMOS

**In one sentence** — four emerging protocols beyond the MCP/A2A/ACP trio: ANP (P2P + W3C DID identity), AG-UI (real-time, event-oriented UI), Agora (natural-language protocol negotiation) and LMOS (Eclipse's Internet of Agents).

## In detail
Four additional protocols. **ANP (Agent Network Protocol)** aims to be "the HTTP of the agentic era": HTTP transport, JSON-LD formatting, a three-layer peer-to-peer architecture (identity with end-to-end encryption and decentralized W3C DID authentication, a meta-protocol for negotiation, an application protocol for capabilities and discovery). **AG-UI (Agent-User Interaction)** standardizes the connection between back-end agents and front-end applications: event-oriented architecture (messages, tool calls, task execution), real-time human-agent interaction, multi-transport middleware (SSE, webhooks, WebSockets). **Agora** is an LLM-powered inter-agent protocol: agents describe their own protocols in plain text (metadata + a communication mode in natural language and code) then negotiate autonomously; HTTPS + JSON, identifiers by hash. **LMOS (Language Model Operating System)**, from the Eclipse Foundation, aims for an Internet of Agents (IoA): three layers (identity/security with W3C DID and OAuth 2.0, adaptable transport, application in JSON-LD with a WebSocket sub-protocol), dynamic or decentralized discovery.

## Example
With Agora, two LLM agents have no fixed schema: each publishes a plain-text "protocol document." The first part is metadata (name, description, single- or multi-turn conversation); the second describes the communication mode through natural-language instructions and code. The agents read these documents and negotiate the protocol to adopt themselves, with no human intervention — hence identification by the document's hash rather than by a versioned URL. This is the most singular bet: the exchange specification itself becomes generated and negotiated on the fly by the models.

## Tradeoff / insight (for a senior)
Note: these protocols are young, little-deployed at scale, with moving specifications — plan for adaptation. Worth keeping as differentiation axes: decentralization/identity (ANP, LMOS via W3C DID), a real-time UI layer (AG-UI, which addresses a need orthogonal to A2A/ACP), and dynamic natural-language protocol negotiation (Agora, the most singular conceptual bet).

## Primary source
Sources: agent-network-protocol.com (ANP), docs.ag-ui.com (AG-UI), agoraprotocol.org (Agora), eclipse.dev/lmos (LMOS).

## See also
- [a2a](a2a.md)
- [acp](acp.md)
