---
tool: "Computer use (Anthropic / Claude)"
title: "Computer use (Anthropic / Claude)"
themes: [tools-function-calling]
type: "Model capability/tool (Anthropic API) + open-source reference implementation"
url: https://docs.claude.com/en/docs/agents-and-tools/tool-use/computer-use-tool
pricing_model: "Proprietary (Anthropic API), usage-based; demo code open-source"
llm_cost: "Resold by usage / pay-as-you-go via the Anthropic API — it's the Claude model itself that acts, so billed in tokens (text AND images: each screenshot consumes ~1000–1800 input tokens)"
objectives: [production]
family: "Computer / desktop control"
eco_icons: "🔒💳"
llm_cost_icons: "💸"
summary: "Anthropic API tool where **Claude itself** sees screenshots and drives mouse/keyboard; ≠ MCP: it's the model that acts → **billed in API tokens** (images included, potentially high cost). Run in an isolated environment"
migrated_from: computer-use
---

# Computer use (Anthropic / Claude)

**In one sentence** — "Computer use" is not a standalone product but an **Anthropic API tool** (`tool type` `computer_...`) that gives Claude the ability to view screenshots and emit mouse/keyboard actions; since it's Claude doing the acting, everything goes through **API tokens billed by usage**, screenshots included (potentially high cost).

## Type & integration

It's a **capability/tool of the Claude model**, exposed as a Messages API tool (on the `tools` side), not a local piece of software or an MCP server. You enable it by declaring a tool whose `type` is:

- `computer_20251124` — for Claude Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6 and Opus 4.5;
- `computer_20250124` — for Claude Sonnet 4.5, Haiku 4.5 and older models (Opus 4.1 / Sonnet 4 / Opus 4, deprecated).

The feature is **in beta** and requires a beta header (`computer-use-2025-11-24` or `computer-use-2025-01-24` depending on the model). The cycle is a client-side **agent loop**: Claude returns actions (`screenshot`, click, keypress, etc.), your code runs them in an environment (often a virtual desktop), returns the new screenshot, and so on. It's a **client-side tool**: screenshots, actions and files stay with you; Anthropic processes the images in real time during the API call but does not retain them after the response (Zero Data Retention eligible).

Anthropic provides an **open-source reference implementation**: the Docker `computer-use-demo` in the `anthropics/anthropic-quickstarts` repo (container, tool implementation, agent loop, web interface). Also available via Amazon Bedrock and Google Vertex AI.

## Pricing model

**Proprietary**: the capability is built into the commercial Claude models and accessible only via the Anthropic API (or Bedrock / Vertex AI), by usage. Only the **demo code** (computer-use-demo) is open-source; the "brain" that acts remains the paid proprietary model.

## LLM cost

A key point, **contrasting with MCP servers**: here, **it's not your external LLM client that consumes — it's Claude itself that acts**, so the cost is in **Anthropic API tokens, paid by usage**. Pricing follows the standard tool-use grid, and adds up:

- **System prompt overhead**: the computer-use beta adds ~466–499 tokens to the system prompt.
- **Tool definition**: ~735 tokens (Claude 4.x models).
- **Screenshots**: billed as **image tokens** (vision) — count **~1000 to 1800 input tokens per screenshot**. Since an agent loop generates many screenshots, the total can climb fast; prompt caching and limiting the number of screenshots are recommended.

The per-token rate depends on the chosen model; don't invent figures — refer to the Anthropic API pricing grid (https://www.anthropic.com/pricing). Consequence: unlike a "free" local tool, **the more the agent looks at the screen, the more it costs**.

## What it's for

Let Claude use a computer like a human: look at the screen (screenshots), move/click the mouse, type on the keyboard, automate any desktop application or interface, browse the web, fill in forms, etc. Often combined with the `bash` and text-editor tools for more complex automation workflows. Anthropic reports state-of-the-art results (among single-agent systems) on the WebArena benchmark for autonomous web navigation.

## Security / precautions

Anthropic explicitly recommends **running computer use only in an isolated environment**: a dedicated VM or container, with minimal privileges, isolated from sensitive data and actions (the reference implementation does run in a Docker container).

Major risk: **prompt injection**. Claude may follow instructions found in on-screen content (web pages, text in images) that contradict the user's. Mitigations:

- The model is trained to resist these injections, and a **classifier layer** runs automatically over prompts/screenshots; if a potential injection is detected in a screenshot, the model **asks the user for confirmation** before the next action (a behavior that can be disabled via support, e.g. for no-human-in-the-loop uses).
- Anthropic advises starting with low-risk tasks, and reading the jailbreak/injection guide before providing login credentials (to pass in XML tags like `<robot_credentials>`).
- The capability is still imperfect and in beta.

## Notes

- **Central contrast of the census**: the MCP servers in the "Automation & control" family — [Firefox DevTools MCP](firefox-devtools-mcp.md), [Playwright MCP](playwright-mcp.md), [Chrome DevTools MCP](chrome-devtools-mcp.md) — are **free tools that the agent drives** (the LLM cost is your *own* LLM client's, which decides the actions). With computer use, conversely, **the Anthropic model IS the agent**: the cost is in **Anthropic API tokens**, screenshots (images) included, so potentially far higher than a local MCP driven by a cheap LLM.
- Screenshots are resized by the API (≤1568 px / ~1.15 Mpx for older models; up to 2576 px on Opus 4.7/4.8 with 1:1 coordinates) — watch out for click-coordinate mapping.
- Exact supported models and beta headers may change (beta feature): re-check the official docs.

## Source

- Official docs "Computer use tool": https://docs.claude.com/en/docs/agents-and-tools/tool-use/computer-use-tool *(verified on 2026-06-15)*
- Announcement "Introducing computer use": https://www.anthropic.com/news/3-5-models-and-computer-use *(verified on 2026-06-15)*
- Reference implementation: https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo *(verified on 2026-06-15)*
