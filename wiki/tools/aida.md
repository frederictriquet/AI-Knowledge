---
tool: "AIDA (AI-Driven Security Assessment)"
title: "AIDA (AI-Driven Security Assessment)"
themes: [security]
type: "Autonomous pentest agent (CLI + web dashboard)"
url: https://github.com/Vasco0x4/AIDA
pricing_model: "Open-source (AGPL v3), free — community project"
llm_cost: "Model-agnostic — defaults to running via Claude Code WITHOUT an LLM API key (🟢); a token is needed only for a custom Anthropic-compatible endpoint (--base-url/--api-key, \"Claude Code only\", optional, 🔑)"
objectives: [production]
family: "Domain-specialized autonomous agents"
eco_icons: "🔓"
llm_cost_icons: "🟢🔑"
summary: "Open-source autonomous pentest agent (AGPL v3) wiring an LLM to 400+ security tools (nmap, sqlmap, ffuf, nuclei + Python payloads) via MCP, in a Docker container; recon → exploitation → CVSS 4.0 scoring. Model-agnostic: runs via Claude Code **without an LLM API key** (default) or a custom Anthropic-compatible endpoint (`--api-key`, optional). ⚠️ Alpha, authorized testing only, local use"
---

# AIDA (AI-Driven Security Assessment)

**In one sentence** — autonomous penetration-testing agent that turns any LLM into a pentester: you set the scope, the agent does reconnaissance, exploitation and vulnerability mapping, and you review the findings.

> 🔐 **Usage frame**: a **dual-use offensive security** tool, intended for **authorized penetration testing** (pentest engagements, research, CTF, labs). Use only on systems for which you have explicit authorization.

## Type & integration
**CLI agent + web dashboard**. **Python** backend, **JavaScript/React** frontend, runs in an isolated **Docker container**. Wires the AI to **400+ pentest tools** (nmap, sqlmap, ffuf, nuclei…) and generates/runs **Python payloads on the fly** (encoding, protocol-specific logic). Tool-calling interface: HTTP manipulation, credential storage, command execution, automatic **CVSS 4.0** scoring of findings.

**Model-agnostic via MCP**: Claude (Claude Code CLI), Kimi CLI, Gemini, any OpenAI-compatible API, local models or APIs interchangeable.

## Pricing model
**Open-source, AGPL v3 license**, free. Community project (author: Vasco0x4); no commercial offering. ⚠️ **Alpha**: local use recommended without additional security hardening.

## LLM cost
**Model-agnostic, LLM API key *not* required** 🟢🔑 — AIDA embeds no LLM. Verified in the README + `aida.py`:
- **Claude Code** (`python3 aida.py`, default) → uses your **Claude Code client's auth**, with **no dedicated key** (🟢). The model is "optional, uses CLI default if not specified".
- **Custom Anthropic-compatible endpoint**: the `--base-url` / `--api-key` options — documented **"Claude Code only"**, mapped to `ANTHROPIC_BASE_URL` / `ANTHROPIC_AUTH_TOKEN` — point to a compatible gateway; *only there* do you supply that gateway's token (🔑). **Optional.**
- **Gemini CLI** via MCP config.

⚠️ **Caveat**: the **README mentions no LLM API key** (just `--base-url`). The "api-key" occurrences in the code are mostly **non-LLM**: `.aida/api-key` (= token for **AIDA's own backend**, interactive login, env `AIDA_TOKEN`) and `--mcp-api-key` / `AIDA_MCP_API_KEY` (HTTP MCP transport bearer).

So: no LLM API key needed via Claude Code. ⚠️ Whatever the mode, an autonomous pentest chains **many iterations** → potentially **large** token usage depending on the model.

## What it's for
Automate vulnerability assessments on web apps, APIs and infrastructure: reconnaissance, scanning, exploitation, post-exploitation, all orchestrated by the LLM with a human safeguard (findings review). Target: pentesters, red teams, security research — in authorized environments.

## Notes
- **Family 10 (domain-specialized autonomous agents)**: the first of its kind here — an agent dedicated to a discipline (offensive security), distinct from coding agents (family 1) and "capability" MCP servers (family 9, e.g. [Firefox DevTools MCP](firefox-devtools-mcp.md)). AIDA does *consume* tools via MCP, like family 9, but as an **end-to-end domain agent**.
- ⚠️ **Security/ethics**: containerized execution recommended; classic offensive-agent risks (destructive commands, false positives, exfiltration). Authorized testing only.
- Same author's ecosystem: **Neo-AI** (AI assistant for the Linux terminal) → candidate note.
- 🔎 **To dig into — backend component**: `aida.py` authenticates to a `BACKEND_API_URL` via a token obtained through **interactive login** (`.aida/api-key`, valid 1 year). AIDA is therefore not 100% autonomous/local: there is an **AIDA service** on the server side (exact role, free status, exchanged data to verify).
- Alpha status → features and stability evolving.

## Source
- Repo: https://github.com/Vasco0x4/AIDA · README: github.com/Vasco0x4/AIDA/blob/main/README.md
- MCP directory: lobehub.com/mcp/vasco0x4-aida

*(verified on 2026-06-15 — GitHub README + web search)*
