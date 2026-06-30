---
tool: "Puppeteer MCP"
title: "Puppeteer MCP"
themes: [tools-function-calling]
type: "MCP server (browser automation)"
url: "https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer"
pricing_model: "Open source (MIT) — free. ⚠️ Official reference server archived/deprecated since May 2025."
llm_cost: "No own LLM — no embedded LLM, the server exposes tools consumed by the MCP client (Claude, etc.)"
objectives: [code-generation]
family: "Browser automation (MCP servers)"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "⚠️ **Deprecated/archived (May 2025)**: reference MCP server driving Chromium via Puppeteer (7 tools), known vulnerabilities. Recommended successors: Chrome DevTools MCP / Playwright MCP"
---

# Puppeteer MCP

**In one sentence** — (Historical) reference MCP server that drives Chrome/Chromium via Puppeteer to let an LLM navigate, click, fill forms, capture screenshots and run JavaScript in a real browser — now **archived and deprecated**.

## Type & integration
Local MCP server (Node.js), distributed via `npx -y @modelcontextprotocol/server-puppeteer` or as a Docker image (headless Chromium). It integrates with any MCP client (Claude Desktop, Claude Code, VS Code, etc.) and exposes a small fixed tool set:
- `puppeteer_navigate` (go to a URL)
- `puppeteer_screenshot` (page/element capture, base64)
- `puppeteer_click`, `puppeteer_hover`, `puppeteer_fill`, `puppeteer_select` (interactions via CSS selectors)
- `puppeteer_evaluate` (run JS in the console)

It also exposes resources: console logs and named screenshots. It is a Chromium-only server, screenshot-oriented, with a deliberately small tool surface.

"Browser/system automation & control via MCP" family, alongside [Playwright MCP](playwright-mcp.md) (multi-browser, accessibility snapshot, actively maintained) and [Firefox DevTools MCP](firefox-devtools-mcp.md) (Firefox). Compared to Playwright MCP, Puppeteer MCP is more limited (Chromium only, screenshot-driven rather than accessibility-tree-driven).

## Pricing model
Free software under **MIT** license, hence free and redistributable. No paid service or reselling: you run it yourself locally. The source code now lives in the `modelcontextprotocol/servers-archived` repo.

## LLM cost
**BYOK**: the server embeds no model. It only exposes browser-automation tools; reasoning and tool calls are performed by the MCP client's LLM (e.g. Claude). The token cost thus comes from the client, and can be high: screenshot-driven control returns images to the model, and each interaction consumes tool round-trips.

## What it's for
- Give an LLM agent the ability to navigate real web pages, fill/submit forms, click, and capture visual state.
- AI-driven scraping, exploratory testing, automation of simple web tasks.
- Run arbitrary JavaScript in a page context.

## Notes
⚠️ **Status: deprecated and archived.** The reference repo was archived on 29 May 2025 (moved to `modelcontextprotocol/servers-archived`, read-only, with no security guarantees or maintenance). The npm package `@modelcontextprotocol/server-puppeteer` is still downloaded (~90k/month) but is officially deprecated.

⚠️ **Security**: known warnings — the server launches a browser on your machine and can access local files and internal/local IPs. Vulnerabilities have been reported (SSRF, indirect prompt injection, sandbox bypass — repo issue #3662). Not to be used as-is in a sensitive environment.

**Recommended successor**: **Chrome DevTools MCP** (`ChromeDevTools/chrome-devtools-mcp`), official server from Google's Chrome team, built on the Chrome DevTools Protocol (and which itself relies on Puppeteer internally). It offers a much richer surface (DOM inspection, network traffic, performance/Core Web Vitals traces, console messages) and is actively maintained. [Playwright MCP](playwright-mcp.md) (Microsoft) is the other frequently cited alternative, multi-browser.

**Homonyms / forks**: several "puppeteer-mcp" coexist and cause confusion — the deprecated official reference server described here; community forks like `@hisma/server-puppeteer` (MCP SDK update); and independent implementations like `puppeteer-mcp-server` (e.g. by Meraj Mehrabi), inspired by the original but distinct. Verify the exact package/repo before use.

## Source
- Archived repo: https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer *(verified on 2026-06-15)*
- Reference servers repo (issues #3662 security, #4118 SDK): https://github.com/modelcontextprotocol/servers *(verified on 2026-06-15)*
- npm package: https://www.npmjs.com/package/@modelcontextprotocol/server-puppeteer *(verified on 2026-06-15)*
- Successor — Chrome DevTools MCP: https://github.com/ChromeDevTools/chrome-devtools-mcp *(verified on 2026-06-15)*
