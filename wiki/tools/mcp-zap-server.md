---
tool: "MCP ZAP Server"
title: "MCP ZAP Server"
themes: [security]
type: "MCP server — OWASP ZAP operator"
url: https://github.com/dtkmn/mcp-zap-server
pricing_model: "Open-source (Apache 2.0), free — by dtkmn (not affiliated with OWASP)"
llm_cost: "No LLM of its own — bridge/operator; BYO MCP client (Claude Desktop, Cursor, Open WebUI…)"
objectives: [production, reliability]
family: "Security — tools exposed via MCP"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "MCP server (Spring Boot, Apache 2.0, by dtkmn) exposing **OWASP ZAP** to agents: spider, active/passive scan, OpenAPI import, findings, reports. \"Production\" guardrails (API-key/JWT auth, scopes, rate limits, audit, Postgres state), Docker/Helm. Not OWASP-affiliated. ⚠️ Authorized tests"
---

# MCP ZAP Server

**In one sentence** — MCP server that gives AI agents a safe, self-hosted **OWASP ZAP** operator to run guided web security scans (spider, active/passive scan), analyze results and generate reports.

> 🔐 **Usage frame**: offensive security — **authorized** tests only, in a controlled environment.

## Type & integration
**Spring Boot application (Java ~95%)** that exposes **OWASP ZAP** as a **streamable HTTP MCP server**. Compatible with any MCP client (Claude Desktop, Cursor, Open WebUI — the latter bundled for local testing). "Guided" MCP tools (spider, active/passive scan, OpenAPI import, findings, reports) + low-level ZAP controls for advanced workflows. Deployment via **Docker Compose** (local) and **Helm/Kubernetes** (prod).

Careful security posture: **API-key or JWT auth**, tool scopes, **runtime policy bundles**, **rate limits**, **audit events**, scan queue, **durable Postgres state**. Conservative defaults (default API key, localhost binding).

## Pricing model
**Open-source, Apache 2.0 license**, free. Maintained by **dtkmn (Daniel Tse)**; contributions via GitHub. ⚠️ **Not affiliated** with the OWASP/ZAP project (an independent project that *drives* ZAP).

## LLM cost
**No LLM of its own** 🟢 — operator/bridge: the LLM comes from your MCP client (BYO subscription/key). No cost on the server side. Like [MCP Kali Server](mcp-kali-server.md) and [Burp Suite MCP Server (PortSwigger)](burp-mcp-server.md), the LLM cost is that of the orchestrating agent.

## What it's for
Letting an agent drive ZAP scans conversationally but **within guardrails** (scopes, quotas, audit), analyze the structured results and produce readable reports — without fragile glue scripts or raw/unsafe access to the scanner. Designed for adoption up to production (guardrails, persistent state).

## Notes
- **Family 9b (offensive security — tools via MCP)**: the open-source/OWASP equivalent of [Burp Suite MCP Server (PortSwigger)](burp-mcp-server.md) (Burp, commercial); sibling of [MCP Kali Server](mcp-kali-server.md) (Kali arsenal). To be distinguished from the **autonomous agents** [AIDA (AI-Driven Security Assessment)](aida.md)/[Shannon (Keygraph)](shannon.md) (family 10).
- Stands out for its **"production" guardrails** (auth, scopes, rate limits, audit, Postgres) — more ops-mature than many community security MCPs.
- ⚠️ Remains an active scan tool (can disrupt a target) → authorized scope, network isolation.

## Source
- Repository: https://github.com/dtkmn/mcp-zap-server · directories: glama.ai, mcpservers.org

*(verified on 2026-06-15 — GitHub README + web search)*
