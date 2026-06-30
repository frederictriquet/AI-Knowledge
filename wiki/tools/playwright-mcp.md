---
tool: "Playwright MCP"
title: "Playwright MCP"
themes: [tools-function-calling]
type: "MCP server (browser automation)"
url: https://github.com/microsoft/playwright-mcp
pricing_model: "Open-source (Apache 2.0, Microsoft) — free, no proprietary backend"
llm_cost: "No own LLM — the tool consumes no tokens; the LLM cost depends on the MCP client orchestrating it"
objectives: [code-generation]
family: "Browser automation (MCP servers)"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Official Microsoft MCP server (Apache 2.0) driving Chromium/Firefox/WebKit via the **accessibility tree** (not screenshots) → fast and token-efficient. Tests, scraping, browser control"
---

# Playwright MCP

**In one sentence** — Official Microsoft MCP server that lets an LLM agent drive a real browser (clicks, typing, navigation, extraction) by leveraging the page's accessibility tree rather than screenshots.

## Type & integration
Open-source MCP (Model Context Protocol) server, distributed as the npm package `@playwright/mcp` and runnable via `npx @playwright/mcp@latest` (Node.js 18+). An official Docker image exists (`mcr.microsoft.com/playwright/mcp`).

It integrates like any MCP server into many clients: Claude Code, Claude Desktop, Cursor, VS Code, Windsurf, Goose, Cline, GitHub Copilot, LM Studio, Warp, etc.

Major technical specificity: it drives the browser via Playwright's **accessibility tree**, serialized into a YAML-like text format optimized for LLMs, rather than via screenshots / pixel vision. Consequences: deterministic, fast, token-efficient, and requiring no multimodal model. Browsers supported via the Playwright engine: **Chromium, Firefox and WebKit** (plus the Chrome and Microsoft Edge channels).

## Pricing model
Entirely free and open-source. **Apache 2.0** license, copyright Microsoft Corporation. No hosted service or paid license; the code runs locally (or in a container you host yourself).

## LLM cost
The tool itself calls no LLM and consumes no tokens: it is a browser-action executor. The cost comes from the **MCP client** orchestrating the calls (e.g. Claude Code), so **BYOK** — you pay for your client's model. Strength: since page state is exposed as a compact text accessibility tree (not images), token consumption is markedly lower than with a screenshot-based approach.

## What it's for
- Give an AI agent the ability to actually act on the web: fill forms, click, navigate, extract structured data.
- Persistent agentic loops: exploratory automation, self-healing tests, assisted scraping, long autonomous workflows.
- A "structured" alternative to vision-based "computer use" approaches: faster and more reliable when the page exposes good accessibility semantics.

## Notes
- "Browser/system automation & control via MCP" family, alongside [Firefox DevTools MCP](firefox-devtools-mcp.md). Difference in approach: Playwright MCP relies on the **accessibility tree** (semantic, multi-engine), whereas firefox-devtools-mcp goes through Firefox's low-level **WebDriver BiDi** / DevTools protocol (finer browser introspection, but Firefox-targeted).
- Direct neighbors / competitors: **Puppeteer MCP** (Puppeteer equivalent, Chromium) and **Chrome DevTools MCP** (official Google, debugging/perf via Chrome DevTools).
- Limit of the accessibility-tree approach: on poorly tagged pages (poor accessibility semantics, canvas, purely visual content), an agent may be less effective than with a vision-based approach.
- Very active project (33k+ GitHub stars, frequent releases aligned with Playwright versions).

## Source
- https://github.com/microsoft/playwright-mcp *(verified on 2026-06-15)*
- https://raw.githubusercontent.com/microsoft/playwright-mcp/main/LICENSE — Apache 2.0 license *(verified on 2026-06-15)*
- https://www.npmjs.com/package/@playwright/mcp — npm package `@playwright/mcp` *(reference)*
