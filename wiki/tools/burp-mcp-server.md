---
tool: "Burp Suite MCP Server (PortSwigger)"
title: "Burp Suite MCP Server (PortSwigger)"
themes: [security]
type: "MCP server / Burp Suite extension (Kotlin)"
url: https://github.com/PortSwigger/mcp-server
pricing_model: "Open-source (GPL-3.0) — free extension; requires Burp Suite (Community free / Pro paid)"
llm_cost: "No LLM of its own — a bridge/extension; BYO MCP client (Claude Desktop…)"
objectives: [production, reliability]
family: "Security — tools exposed via MCP"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "**Official** Burp Suite MCP extension (PortSwigger, GPL-3.0, Kotlin) connecting an AI client to Burp: request/response analysis, contextual payload generation, obfuscated-JS analysis, business-logic flaws, endpoint prediction. BApp Store, BYO client. ⚠️ Burp Community (free) is enough; Pro required only for Burp Collaborator (out-of-band). Authorized testing"
---

# Burp Suite MCP Server (PortSwigger)

**In one sentence** — **official** Burp Suite extension that exposes its capabilities via the Model Context Protocol, letting an AI client (Claude Desktop…) interact programmatically with Burp to assist web security testing.

> 🔐 **Usage frame**: offensive security — reserve for **authorized** penetration testing. (Lower risk than raw command execution: the assistance happens *inside* Burp, but it remains an offensive tool.)

## Type & integration
**Burp Suite extension** (Java/**Kotlin** ~99%) that runs an **SSE MCP server** on `localhost:9876`, with a packaged **stdio proxy** for clients like Claude Desktop (auto-install for Claude Desktop). The exposed MCP tools are defined in the code (`Tools.kt`). Available in PortSwigger's **BApp Store**. Install: build the JAR via Gradle, then load it as a Burp extension. A security option "allow tools that edit config" can be disabled.

Part of PortSwigger's broader **"Burp AI"** strategy.

## Pricing model
- **Extension: open-source GPL-3.0**, free (on GitHub, ~900★).
- **Burp Suite itself**: required to use it — but **Burp Community (free) is enough** for the MCP extension (verified). **Only** the **Burp Collaborator** feature (out-of-band testing) requires **Burp Pro** (paid). So no Pro needed for the majority of uses.

## LLM cost
**No LLM of its own** 🟢 — the extension is a bridge: the LLM comes from **your MCP client** (BYO subscription/key, e.g. Claude). No cost on the extension side. Like [MCP Kali Server](mcp-kali-server.md) and the browser MCPs ([Firefox DevTools MCP](firefox-devtools-mcp.md)), the LLM cost is that of the driving agent.

## What it's for
Boost manual web pentesting with AI, without leaving Burp:
- Send requests/responses to the AI to analyze an endpoint's behavior and weaknesses.
- **Generate contextual payloads** for injection points.
- Analyze **obfuscated JavaScript** (sensitive sections).
- Spot **business-logic flaws** in multi-step processes.
- **Predict endpoints** and spot sensitive API calls.

## Notes
- **Family 9 (automation & control — security scope)**: a vendor's official capability server (PortSwigger), distinct from the **autonomous agents** [AIDA (AI-Driven Security Assessment)](aida.md)/[Shannon (Keygraph)](shannon.md) (family 10). A security sibling of [MCP Kali Server](mcp-kali-server.md) (Kali) — one exposes Burp, the other the Kali arsenal.
- "Official" advantage: maintained by Burp's vendor, clean integration (BApp Store), vs community implementations of security MCP.
- ⚠️ Exposing Burp to an LLM = sensitive test data sent to the model; caution with a cloud LLM on real targets/clients.

## Source
- Repo: https://github.com/PortSwigger/mcp-server · BApp Store: portswigger.net/bappstore/9952290f04ed4f628e624d0aa9dccebc
- Context: PortSwigger "Burp AI" blog

*(verified on 2026-06-15 — GitHub README + BApp Store + web search)*
