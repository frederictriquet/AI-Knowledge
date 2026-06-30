---
tool: "Microsoft Learn MCP"
title: "Microsoft Learn MCP"
themes: [rag-context]
type: "Remote MCP server (official Microsoft docs)"
url: https://learn.microsoft.com/training/support/mcp
pricing_model: "Proprietary (Microsoft-hosted service) — free, no auth"
llm_cost: "Built-in (doc source; does not generate an LLM)"
objectives: [code-generation]
family: "Documentation & external knowledge sources (MCP servers)"
eco_icons: "🔒"
llm_cost_icons: "🟢"
summary: "**Official Microsoft** MCP server (streamable HTTP) serving official Microsoft/Azure docs (\"Ask Learn\" service, daily refresh): doc search, full article, examples. **Free, no authentication**; proprietary (hosted service)"
---

# Microsoft Learn MCP

**In one sentence** — **official Microsoft** MCP server serving up-to-date official Microsoft/Azure documentation directly to the agent (the "Ask Learn" service that powers Copilot for Azure).

## Type & integration
**Remote** MCP server (streamable HTTP), connectable from GitHub Copilot, VS Code, Visual Studio, Copilot Studio and other agents. Three uses: search the docs, fetch a full article, look up code examples. The knowledge service refreshes continuously (daily full refresh).

## Pricing model
**Proprietary** (service hosted by Microsoft), but **free** and **without authentication** — publicly accessible, no usage cost for the MCP server.

## LLM cost
**🟢 Built-in**: a doc source — no LLM generation; runs inside your agent.

## What it's for
Coding precisely on the **Microsoft/Azure/.NET ecosystem** by relying on up-to-date official docs rather than on the model's (potentially stale) memory. The "vendor" equivalent of Context7, on the Microsoft side.

## Notes
- Microsoft-hosted service → not self-hostable, but free and keyless.
- AWS counterpart: [AWS Documentation MCP](aws-documentation-mcp.md).
- ⚠️ Limited to the Microsoft/Azure/.NET ecosystem and not self-hostable (MS-hosted service); outside this scope, a general-purpose doc MCP (e.g. Context7) is more relevant.

## Source
https://learn.microsoft.com/training/support/mcp · https://learn.microsoft.com/en-us/training/support/mcp-developer-reference. *(verified on 2026-06-17)*
