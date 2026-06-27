---
type: index
title: "Theme — Interop protocols"
theme: interop-protocols
---

# 🔌 Interop protocols

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Interoperability standards (MCP, A2A…)._

## Concepts (5)

### 🔴 Substance / core
- **[MCP (Model Context Protocol)](../concepts/mcp.md)** — the open standard (Anthropic, 2024) that connects a model to external tools/data via a host/client/server trio over JSON-RPC 2.0; the "USB-C" of tool integration, not an orchestration framework.

### 🟡 Tradeoff / intermediate
- **[A2A (Agent2Agent)](../concepts/a2a.md)** — the agent↔agent protocol (Google, April 2025, now under the Linux Foundation) where each agent publishes a discoverable Agent Card, then communicates over JSON-RPC 2.0 on HTTPS with SSE for streaming.
- **[ACP (Agent Communication Protocol)](../concepts/acp.md)** — the agent↔agent protocol from IBM's BeeAI, built on lightweight REST/HTTP (vs JSON-RPC), asynchronous by default, with offline discovery; it merged with A2A under the Linux Foundation.
- **[KQML & FIPA-ACL](../concepts/kqml-fipa-acl.md)** — the two historical agent communication languages (ACLs) that standardized "communicative acts" (inform, request, query) long before LLMs, and that most current frameworks ignore in favor of natural language.
- **[Other protocols: ANP / AG-UI / Agora / LMOS](../concepts/other-protocols.md)** — four emerging protocols beyond the MCP/A2A/ACP trio: ANP (P2P + W3C DID identity), AG-UI (real-time, event-oriented UI), Agora (natural-language protocol negotiation) and LMOS (Eclipse's Internet of Agents).

## Tools (0)

- _(aucun)_
