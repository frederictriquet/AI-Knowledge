---
tool: "GitMCP"
title: "GitMCP"
themes: [rag-context]
type: "Remote MCP server (GitHub repo → MCP)"
url: https://gitmcp.io/
pricing_model: "Free (open-source, idosal/git-mcp)"
llm_cost: "Built-in (context source; generates no LLM)"
objectives: [code-generation]
family: "Documentation & external knowledge sources (MCP servers)"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Turns **any GitHub repo** into a remote MCP server: replace `github.com` with `gitmcp.io` → the agent reads `llms.txt`/`readme` for context. Free (idosal/git-mcp). ⚠️ License not confirmed at the source"
migrated_from: gitmcp
---

# GitMCP

**In one sentence** — Turns **any GitHub repo** into a remote MCP server: just replace `github.com` with `gitmcp.io` in the URL to give the agent a project's context (docs, code).

## Type & integration
**Remote** MCP server, no local install: you convert the repo URL (`github.com/x/y` → `gitmcp.io/x/y`) and point the agent at it. Reads the repo's context files first (`llms.txt`, `llms-full.txt`, `readme.md`). Compatible with Claude, Cursor, Windsurf, VS Code, Cline…

## Pricing model
**Free**, open-source (repo `idosal/git-mcp`, **Apache-2.0 license**, ~8.2k★).

## LLM cost
**🟢 Built-in**: context source — no LLM generation of its own; runs in your agent.

## What it's for
Giving the agent the **docs/code of a specific GitHub project** without cloning or loading the whole repo into context. Complementary to Context7/Ref (which index a large catalogue of libraries) when targeting **one** given repo.

## Notes
- ⚠️ **Third-party hosted service** (gitmcp.io) → external dependency + sending the repo's context to a service you do not control; for private/sensitive code, prefer a local MCP.
- Reads mostly `llms.txt`/`readme.md`: on a repo **without** well-curated context files, usefulness drops (it does not "understand" the code, it serves what is exposed).

## Source
https://gitmcp.io/ · https://github.com/idosal/git-mcp (Apache-2.0). *(verified on 2026-06-24 — GitHub API: Apache-2.0 license, ~8.2k★)*
