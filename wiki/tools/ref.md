---
tool: "Ref (ref.tools)"
title: "Ref (ref.tools)"
themes: [efficiency-cost, rag-context]
type: "MCP server (up-to-date technical documentation)"
url: https://ref.tools/
pricing_model: "Freemium / Subscription (open-source MCP client)"
llm_cost: "Built-in (doc source; generates no LLM output)"
objectives: [code-generation]
family: "Documentation & external knowledge sources (MCP servers)"
eco_icons: "🎁🔁"
llm_cost_icons: "🟢"
summary: "Serves agents **up-to-date technical docs** (public libs/APIs + private repos/PDFs), pre-chunked → *just the useful tokens* (reduces \"context rot\"). Open-source MCP client; freemium hosted service (Free 200 credits → Basic $19, Pro $50, Max $200/month). Neighbor of Context7"
migrated_from: ref
---

# Ref (ref.tools)

**In one sentence** — MCP server that gives coding agents **token-efficient** access to an index of **up-to-date technical documentation** (public libs/APIs + private repos/PDFs), to avoid API hallucinations without wasting context.

## Type & integration
MCP server (`ref-tools-mcp`) exposing two tools: `ref_search_documentation(query)` and `ref_read_url(url)`. Index intelligently **pre-chunked** → the agent receives *just the useful tokens* rather than whole pages (reduces "context rot"). Covers GitHub repos and doc sites of the main platforms/libs, plus your private sources.

## Pricing model
The **MCP server is open-source** (`ref-tools/ref-tools-mcp` repo); the hosted service (the index) is **freemium + subscription** (observed on 2026-06-17):
- **Free**: $0, 200 one-shot credits (no expiry), 3 small repos + 1 large.
- **Basic**: $19/month, 2,000 credits, 10 small repos.
- **Pro**: $50/month, 6,000 credits, 50 small repos.
- **Max**: $200/month, 30,000 credits.
- **Enterprise**: by quote (SSO, custom limits).

## LLM cost
**🟢 Built-in**: Ref is a **knowledge source** — it generates no completion. It runs inside your agent (LLM cost = that of your agent) and instead aims to **reduce** consumed tokens by returning only relevant context.

## What it's for
Prevent the agent from getting library APIs wrong (versions, signatures) by serving it the **right, up-to-date documentation in a token-efficient way**. Same niche as Context7.

## Notes
- ⚠️ **Classification**: filed here as a code-production aid (external docs for the agent). Neighbors: Context7, GitMCP (same "MCP knowledge sources" for coding).
- Credit-based pricing depends on the volume of searches/indexed repos.

## Source
https://ref.tools/ · https://docs.ref.tools/usage/pricing · https://github.com/ref-tools/ref-tools-mcp. *(verified on 2026-06-17)*
