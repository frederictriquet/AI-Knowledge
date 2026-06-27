---
tool: "Exa MCP"
title: "Exa MCP"
themes: [rag-context]
type: "MCP server (web / neural search)"
url: https://github.com/exa-labs/exa-mcp-server
pricing_model: "Open-source MCP server (MIT) + paid usage-based Exa API"
llm_cost: "Built-in on the LLM side (but a paid usage-based Exa key is required for search)"
objectives: [code-generation]
family: "Documentation & external knowledge sources (MCP servers)"
eco_icons: "🔓💳"
llm_cost_icons: "🟢"
summary: "Gives the agent **web/code/company search** via the **Exa** neural API (`web_search_exa`, `web_fetch_exa`). MCP server **MIT** free, but **Exa key required** (usage-based paid API, free tier). Broader than library docs. 🟢 on the LLM side, but Exa search has a usage-based cost"
migrated_from: exa-mcp
---

# Exa MCP

**In one sentence** — MCP server giving the agent **web search** (and code, and company search) via the **Exa neural search** API — broader than library docs: the open web.

## Type & integration
MCP server exposing `web_search_exa` (web search) and `web_fetch_exa` (full-page retrieval). Local, or via the hosted endpoint `https://mcp.exa.ai/mcp` (API key passed as a parameter/env var). Compatible with Claude, Cursor, etc.

## Pricing model
**Open-source MCP server — MIT** and free. **But** it requires an **Exa API key**: Exa is a **usage-based paid search API** (per request; free tier/starter credits available). The real cost is therefore not in the MCP server but in the **Exa API** consumed.

## LLM cost
**🟢 on the LLM side**: Exa MCP generates no LLM tokens. ⚠️ However it consumes **Exa search credits** (BYO Exa key, billed per request) — a *usage-based* cost distinct from the LLM, not to be forgotten.

## What it's for
Giving the agent **quality web access** (semantic/neural search) for real-time research, not just library docs. Useful when the need goes beyond technical documentation.

## Notes
- The only one in the family with a usage-based cost of its own (the Exa API), vs Context7/GitMCP/MS Learn/AWS docs which are free.
- Check current Exa pricing before intensive use.

## Source
https://github.com/exa-labs/exa-mcp-server (MIT) · https://exa.ai/. *(verified on 2026-06-17; Exa pricing to be reconfirmed at the source)*
