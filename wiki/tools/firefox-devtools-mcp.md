---
tool: "Firefox DevTools MCP"
title: "Firefox DevTools MCP"
themes: [tools-function-calling]
type: "MCP server (browser automation / inspection)"
url: https://github.com/freema/firefox-devtools-mcp
pricing_model: "Open-source, dual-licensed MIT / Apache 2.0 — free"
llm_cost: "No LLM of its own — a tool for agents; BYO client (Claude, Cursor…)"
objectives: [code-generation]
family: "Browser automation (MCP servers)"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Open-source MCP server (TypeScript) to drive/inspect Firefox via WebDriver BiDi: navigation, DOM, network, console, screenshots, JS eval, preferences/extensions. Testing, scraping, browser control. Local only (Firefox + Node). Dual-licensed MIT/Apache 2.0"
migrated_from: firefox-devtools-mcp
---

# Firefox DevTools MCP

**In one sentence** — MCP server that lets an AI agent **drive and inspect Firefox** (DevTools) via WebDriver BiDi: navigate, read the DOM, capture network and console, take screenshots, run JS in the page.

## Type & integration
**MCP server**, written in **TypeScript** (~84%), relying on **WebDriver BiDi** (via Selenium WebDriver / Firefox's remote debugging protocol). Plugs into Claude Code, Claude Desktop, Cursor, Cline, and any MCP client. Launch: `npx firefox-devtools-mcp@latest` (or the `@mozilla/...` variant, see lineage below), or via Docker.

Capabilities exposed as MCP tools:
- Navigation and page management
- **DOM** inspection (snapshots + UID)
- Capture and inspection of **network requests**
- Access to **console messages**
- **Screenshots**
- **JavaScript evaluation** in the page context
- Management of **Firefox preferences** and **extensions**

⚠️ **Local only**: requires an installed Firefox (100+) and Node.js (≥20.19); does not run on hosted cloud. Dedicated Firefox profile recommended (security).

## Pricing model
**Open-source**, **dual-licensed MIT / Apache 2.0** (flexible use), free. No commercial offering.

## LLM cost
**No LLM of its own** 🟢 — it is a *tool the agent uses*, not a model. No server-side cost; you bring your own AI client (BYO subscription/key, e.g. Claude). The LLM cost is that of your agent.

## What it's for
Giving an agent a **drivable Firefox browser**: E2E/QA testing, scraping, reproducing web bugs, visual verification, journey automation. Complements coding agents when you need to *act in a real browser* (e.g. checking that a front-end change works).

## Notes
- **Family 9 (automation/control via MCP)**: the first of its kind here — an **action** capability on an external environment, distinct from data sources ([Ansvar Compliance MCP (suite)](ansvar-compliance-mcp.md)) or codebase knowledge ([Serena](serena.md)). Category neighbours: Playwright MCP, Puppeteer MCP, Chrome DevTools MCP, computer-use.
- ✅ **Lineage clarified** (verified via GitHub API): `freema/firefox-devtools-mcp` **redirects to `mozilla/firefox-devtools-mcp`** — the project was **transferred to Mozilla** (official maintained repo). Dual license **MIT OR Apache-2.0** confirmed (LICENSE-MIT / LICENSE-APACHE files; GitHub shows NOASSERTION because of the dual license). For long-term use, point to the Mozilla repo.
- WebDriver BiDi = modern standard (vs CDP on the Chrome side) → good inspection fidelity.

## Source
- Repo (requested): https://github.com/freema/firefox-devtools-mcp · npm: `firefox-devtools-mcp`
- Official Mozilla: https://github.com/mozilla/firefox-devtools-mcp · docs: firefox-source-docs.mozilla.org/ai-agent-tools/firefox-devtools-mcp.html

*(verified on 2026-06-15 — GitHub README + web search)*
