---
tool: "AWS Documentation MCP"
title: "AWS Documentation MCP"
themes: [rag-context]
type: "Local MCP server (official AWS docs)"
url: https://github.com/awslabs/mcp
pricing_model: "Open-source (Apache 2.0) — free"
llm_cost: "Built-in (docs source; runs no LLM)"
objectives: [code-generation]
family: "Documentation & external knowledge sources (MCP servers)"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "**Official AWS Labs (Apache 2.0)** MCP server: search/read the official **AWS docs**, API refs, What's New (local stdio). Free, open-source; one of the servers in the `awslabs/mcp` repo. 1-click install (Cursor, VS Code, Kiro)"
migrated_from: aws-documentation-mcp
---

# AWS Documentation MCP

**In one sentence** — **official AWS Labs** MCP server giving the agent access to up-to-date **official AWS documentation** (docs, API references, What's New), to code correctly on AWS.

## Type & integration
**Local** MCP server (stdio transport), configured in the agent (1-click install in Kiro, Cursor, VS Code…). Lets you search and read AWS docs, API references and new releases. It is **one of the many MCP servers** in the `awslabs/mcp` repo (which also covers other AWS capabilities).

## Pricing model
**Open-source — Apache 2.0**, free. Maintained by **AWS Labs**.

## LLM cost
**🟢 Built-in**: a docs source — no LLM generation; runs inside your agent. (The doc server itself makes no billed AWS service calls.)

## What it's for
Code correctly on the **AWS ecosystem** by relying on up-to-date official docs. Microsoft-side counterpart: [Microsoft Learn MCP](microsoft-learn-mcp.md).

## Notes
- Self-hostable (local stdio) → no dependency on a third-party service, unlike MS Learn MCP (remote).
- The `awslabs/mcp` repo contains other servers (AWS API, IaC…) — here, only the **Documentation** server is recorded.
- ⚠️ Covers official AWS docs only — no guarantee of real-time freshness or coverage of recent services; does not replace checking the AWS console. Outside the AWS ecosystem, of no use.

## Source
https://github.com/awslabs/mcp (LICENSE = Apache 2.0, `aws-documentation` server). *(verified on 2026-06-17)*
