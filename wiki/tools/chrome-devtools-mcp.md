---
tool: "Chrome DevTools MCP"
title: "Chrome DevTools MCP"
themes: [tools-function-calling]
type: "MCP server (browser automation)"
url: https://github.com/ChromeDevTools/chrome-devtools-mcp
pricing_model: "Open-source (Apache 2.0) — official project of the Chrome team (Google), free, distributed via npm"
llm_cost: "No LLM of its own — no LLM embedded; the server is used from an agent (Claude, Cursor, Copilot…) that brings its own model"
objectives: [code-generation]
family: "Browser automation (MCP servers)"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Official MCP server from the Chrome team (Google, Apache 2.0) driving Chrome via CDP + Puppeteer; stands out for **performance traces** and network/DOM/console debugging"
migrated_from: chrome-devtools-mcp
---

# Chrome DevTools MCP

**In one sentence** — official MCP server from the Chrome team (Google) that gives a coding agent control of a real Chrome via the Chrome DevTools Protocol and Puppeteer, with a strong emphasis on performance traces and deep debugging.

## Type & integration
MCP server (Model Context Protocol) written in TypeScript, run under Node.js (LTS version) and typically launched via `npx chrome-devtools-mcp@latest`. It plugs into any MCP client (Claude Code/Desktop, Cursor, GitHub Copilot, etc.) through a standard JSON config. Under the hood, it combines the **Chrome DevTools Protocol (CDP)** for low-level inspection and **Puppeteer** to drive the browser and automatically wait for actions to complete.

## Pricing model
Open-source under **Apache 2.0** license, free. It's an official repo of the `ChromeDevTools` org (Google), actively maintained (heavily starred, frequent releases, e.g. v1.2.0). No license cost; the only dependency is a local Chrome/Chromium.

## LLM cost
No language model is embedded: it's a pure tool provider for an external agent. The LLM cost is therefore the calling agent's (BYOK). Note that rich inspection (performance traces, DOM snapshots, network/console logs) can return large outputs: watch out for the agent's context consumption.

## What it's for
- **Performance traces**: recording and extracting actionable "insights" (distinctive angle via CDP).
- **Browser debugging**: inspecting network requests, console messages (with source-mapped stack traces), memory/heap snapshots.
- **Automation**: navigation, clicks, form filling, screenshots/snapshots, evaluating scripts in the DOM, all with automatic waiting for results.

Use cases: let an agent reproduce a bug, measure a page's performance, or inspect a live network/DOM state.

## Notes
- "Browser automation & control via MCP" family, alongside [Playwright MCP](playwright-mcp.md) (Microsoft), [Puppeteer MCP](puppeteer-mcp.md) (the old, deprecated Puppeteer server) and [Firefox DevTools MCP](firefox-devtools-mcp.md).
- **Positioning vs the deprecated Puppeteer MCP**: the official `@modelcontextprotocol/server-puppeteer` server is deprecated. The generally recommended successor for cross-browser automation is rather **[Playwright MCP](playwright-mcp.md)** (accessibility snapshots, multi-browser). Chrome DevTools MCP is therefore not a simple 1:1 replacement for Puppeteer MCP: it stands out via the **CDP + performance traces + deep Chrome debugging** angle, where Playwright MCP aims at deterministic DOM interaction at scale.
- Specific to Chrome/Chromium (no native cross-browser), unlike Playwright MCP.
- Several namesake community forks/implementations exist (benjaminr, ctrlShiftBryan, diegorafs…); this fiche targets the official `ChromeDevTools/chrome-devtools-mcp` repo.

## Source
- https://github.com/ChromeDevTools/chrome-devtools-mcp
- https://www.npmjs.com/package/chrome-devtools-mcp
- https://mcpservers.org/servers/github-com-chromedevtools-chrome-devtools-mcp *(verified on 2026-06-15)*
