---
tool: "Neo-AI"
title: "Neo-AI"
themes: [frameworks-tooling]
type: "CLI — AI assistant for the Linux terminal"
url: https://github.com/Vasco0x4/Neo-AI
pricing_model: "Open-source (BSD 3-Clause), free — community project"
llm_cost: "🟢🔑 — local LM Studio mode = NO key, free (🟢); DigitalOcean cloud mode = credentials required (🔑). OpenAI/Anthropic accessible ONLY via the DigitalOcean gateway"
objectives: [code-generation]
family: "AI assistants for terminal / shell"
eco_icons: "🔓"
llm_cost_icons: "🟢🔑"
summary: "Open-source AI assistant for the Linux terminal (BSD-3, Python, by Vasco0x4): runs commands with context + approval, system analysis (logs, files, health), cybersecurity angle (network scan, CTF). Local LLM (LM Studio) or cloud (OpenAI/Claude). ⚠️ Beta, Linux"
---

# Neo-AI

**In one sentence** — AI assistant that lives in the Linux terminal: it understands context, runs system commands (with your approval), analyzes the system and helps with CLI and cybersecurity tasks. You invoke it with `neo`.

## Type & integration
**CLI tool** for Linux, written in **Python** (~96%), with a terminal UI (syntax highlighting, history). Requires Python 3.6+ and a compatible emulator (GNOME Terminal, Konsole…). Capabilities: **intelligent command execution** (interpretation + user approval), **system analysis** (logs, file inspection, health), multi-protocol (terminal, files, network, security), **cybersecurity**-oriented tools (network scan, CTF).

## Pricing model
**Open-source, BSD 3-Clause license**, free. Community project (author: Vasco0x4). **Beta** status, under development.

## LLM cost
**🟢🔑** — no embedded LLM; two modes (verified in `config.yaml` / `src/ai_core.py`):
- **Local** via **LM Studio** (OpenAI-compatible server `127.0.0.1:1234`, empty `api_key`) → **keyless, free** (🟢), runs on your machine.
- **Cloud** via **DigitalOcean** (`agent_id` + `agent_key` required) → credentials needed (🔑). ⚠️ OpenAI/Anthropic are accessible **only via the DigitalOcean gateway**, not via a direct OpenAI/Anthropic key.

Real cost = that of the chosen backend; the local mode is free (hardware aside).

## What it's for
Making the terminal more intuitive: translate intent into commands, execute under control, diagnose the system, assist with administration and security tasks. A general-purpose daily shell companion, with a **command-approval system** for safety.

## Notes
- **Family 11 (terminal/shell assistants)**: the first of its kind here. To be distinguished from [AIDA (AI-Driven Security Assessment)](aida.md) (same author, but an **autonomous pentest** specialist agent, family 10): Neo-AI is an interactive **general-purpose terminal companion**, AIDA an end-to-end offensive agent. Also distinct from the coding agents ([Kilo Code](kilo-code.md)) — Neo-AI targets **system administration/usage**, not development within a project.
- Category neighbors: Warp AI, term_agent, arch-ai, termax, Gemini CLI (shell use).
- ⚠️ System command execution → keep the approval guardrail active; caution with a cloud LLM on sensitive commands.
- Beta → features evolving.

## Source
- Repository: https://github.com/Vasco0x4/Neo-AI · docs: github.com/Vasco0x4/Neo-AI/blob/master/docs/INSTALLATION.md
- Write-up: dev.to/vasco0x4_85 ("Neo-AI, your intelligent Linux terminal companion")

*(verified on 2026-06-15 — GitHub README + web search)*
