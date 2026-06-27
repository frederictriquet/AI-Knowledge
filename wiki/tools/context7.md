---
tool: "Context7"
title: "Context7"
themes: [rag-context]
type: "MCP server (library docs) — open-source + hosted"
url: https://context7.com/
pricing_model: "Open-source (MIT) + free hosted service (API key for more quota)"
llm_cost: "Built-in (docs source; runs no LLM)"
objectives: [code-generation]
family: "Documentation & external knowledge sources (MCP servers)"
eco_icons: "🔓🎁"
llm_cost_icons: "🟢"
summary: "**Open-source (MIT, Upstash)** MCP server injecting **up-to-date, versioned** library docs + code examples (`resolve-library-id`, `query-docs`). Hosted (`mcp.context7.com`) or local; free, free API key for more quota. 30+ agents. **Already connected in this session**"
migrated_from: context7
---

# Context7

**In one sentence** — MCP server (Upstash) that injects into the prompt the **up-to-date, version-specific** docs of libraries + code examples, so the agent doesn't get the API wrong.

## Type & integration
MCP server, hosted remote (`https://mcp.context7.com/mcp`) or local. Tools: `resolve-library-id` (resolves a lib name to an ID, e.g. `/supabase/supabase`) then `query-docs`. Also a `ctx7` CLI. Compatible with Claude Code, Cursor and 30+ agents. **Already connected in this Claude Code session.**

## Pricing model
**Open-source — MIT.** Hosted service **free** without authentication; a **free API key** (context7.com/dashboard) unlocks higher rate limits. No clearly documented paid tier so far.

## LLM cost
**🟢 Built-in**: a documentation source — generates no completion, runs inside your agent (LLM cost = the agent's). Aims to *reduce* API hallucinations and the context loaded.

## What it's for
Serve the agent the **right, up-to-date library docs** at the moment it codes — the same niche as Ref. Very widespread, trivial integration (MCP).

## Notes
- Direct neighbors: [Ref](ref.md) (docs + private repos/PDFs, freemium) and [GitMCP](gitmcp.md) (GitHub repo → MCP).
- Published by **Upstash** (serverless Redis/Kafka); good community traction.

## Source
https://context7.com/ · https://github.com/upstash/context7 (LICENSE = MIT). *(verified on 2026-06-17)*
