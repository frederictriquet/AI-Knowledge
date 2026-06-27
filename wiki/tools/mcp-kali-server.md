---
tool: "MCP Kali Server"
title: "MCP Kali Server"
themes: [security]
type: "MCP server (command-execution bridge to Kali Linux)"
url: https://www.kali.org/tools/mcp-kali-server/
pricing_model: "Open-source (MIT license, verified via GitHub API), free — packaged in Kali Linux; Wh0am123/MCP-Kali-Server repo"
llm_cost: "No LLM of its own — bridge/tool; BYO MCP client (Claude, Copilot…)"
objectives: [production, reliability]
family: "Security — tools exposed via MCP"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "MCP bridge (Flask API) packaged in Kali (`apt install`) giving an AI agent access to Kali pentest tools: command execution (nmap, nxc, curl, gobuster…). Assisted pentest, CTF, HTB/THM. ⚠️ Command execution — isolated container, access control, authorized tests only"
migrated_from: mcp-kali-server
---

# MCP Kali Server

**In one sentence** — MCP bridge that gives an AI agent access to Kali Linux's pentest toolbox: the agent calls MCP tools, which execute the commands (nmap, nxc, curl, gobuster…) on a Kali machine/container.

> 🔐 **Usage frame**: dual-use **offensive security** tool. Reserve for **authorized penetration testing** (engagements, CTF, HTB/THM labs) and run in an **isolated environment** with strict access control.

## Type & integration
**MCP server** = **API bridge** (Flask, Python) between MCP clients (Claude Desktop, GitHub Copilot, Cursor…) and a Linux/Kali machine. The agent calls MCP tools → forwarding to the Flask API which executes commands in the Kali environment (ideally a **pre-configured container**). Now **officially packaged in Kali**: `sudo apt install mcp-kali-server`. Upstream repo: `github.com/Wh0am123/MCP-Kali-Server` (dependencies `python3-flask`, `python3-mcp`).

## Pricing model
**Open-source, MIT license** (verified via the GitHub API of the upstream repo `Wh0am123/MCP-Kali-Server`), free; packaged in the Kali Linux tools repo. Community project.

## LLM cost
**No LLM of its own** 🟢 — it's a bridge/tool: the LLM (via your MCP client) issues the requests, the server executes the commands. No cost on the server side; you bring your own client (BYO subscription/key). As with the browser MCPs ([Firefox DevTools MCP](firefox-devtools-mcp.md), [Playwright MCP](playwright-mcp.md)), the LLM cost is that of the driving agent.

## What it's for
Real-time AI-assisted pentest: reconnaissance, scanning, web interaction, CTF challenge solving, HTB/THM machines — letting the agent chain Kali tools under supervision. Makes the Kali arsenal "callable" by an LLM.

## Notes
- **Family 9 (automation & control — system/security side)**: it's a **capability server** (the agent drives the tool), to be distinguished from [AIDA (AI-Driven Security Assessment)](aida.md), which is an **end-to-end autonomous pentest agent** (family 10). MCP Kali Server is "the Kali arsenal exposed over MCP", not the orchestrator.
- ⚠️ **High risk**: a **command-execution** server exposed to an LLM = serious attack surface (prompt injection → arbitrary commands). Container isolation, segmented network, no secrets in the environment, authorized scope.
- **Several "Kali MCP" implementations** coexist: `Wh0am123/MCP-Kali-Server` (the one packaged by Kali); `zebbern/zebbern-kali-mcp` (~130 tools); various Docker variants. Verify which one you deploy.
- Neighbors/context: critical analyses (penligent.ai) on the limits of "Kali + Claude via MCP" for real pentest teams.
- ⚠️ Beyond the security risk already noted, the real usefulness for a professional pentest remains debated: an LLM driving Kali often produces unreliable / non-reproducible chains — validate on a real engagement before depending on it.

## Source
- Kali page: https://www.kali.org/tools/mcp-kali-server/ · upstream repo: https://github.com/Wh0am123/MCP-Kali-Server

*(verified on 2026-06-15 — official Kali page + web search)*
