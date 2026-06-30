---
tool: "Headroom"
title: "Headroom"
themes: [efficiency-cost]
type: "CLI / Proxy / MCP server / Library"
url: https://github.com/headroomlabs-ai/headroom
pricing_model: "Open-source"
llm_cost: "Built-in"
objectives: [cost-control]
family: "Token & agent-behavior optimization"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Open-source (Apache 2.0) context-compression layer: cuts 60–95% of tokens (JSON, code AST, logs, RAG, history) **before** the call, via **deterministic, LLM-free** compression. Multi-format (Py/TS lib, proxy, agent wrapper, MCP, middleware); local, sits in front of the existing key/subscription (no key of its own)"
---

# Headroom

**In one sentence** — open-source (Apache 2.0) **context-compression** layer that cuts 60–95% of tokens sent to LLMs (tool outputs, logs, RAG chunks, files, conversation history) **before** the call, via deterministic compression — with no LLM or key of its own.

## Type & integration
Multi-format, to plug in as close to your usage as possible:
- **Python/TypeScript library**: `compress(messages)`.
- **Language-agnostic proxy**: `headroom proxy --port 8787` (zero code change, for any OpenAI-compatible client).
- **CLI wrapper** for coding agents: `headroom wrap claude|codex|cursor|aider|copilot`.
- **MCP server**: `headroom_compress`, `headroom_retrieve`, `headroom_stats` tools.
- **Middleware** for frameworks (agno, langchain…).

Install: `pip install "headroom-ai[all]"` (Python 3.10+, granular options `[proxy]`/`[mcp]`/`[ml]`/`[code]`/`[memory]`…), `npm install headroom-ai`, or `docker pull ghcr.io/chopratejas/headroom:latest`.

## Pricing model
**Open-source, free**, under the **Apache 2.0** license. Runs locally ("your data stays here") — no paid offering or hosted service identified at the source.

## LLM cost
**🟢 Built-in.** The compression is **deterministic / heuristic, with no LLM call**: `SmartCrusher` (JSON), `CodeCompressor` (AST-aware: Python, JS, Go, Rust, Java, C++) engines, and a `Kompress-base` model (a **local** HuggingFace model, not an API service). In wrapper/proxy mode, Headroom **sits in front of the agent's existing key/subscription** (Claude Code, Cursor, Aider…) and requires **no key of its own** — it does not resell tokens, it *reduces their volume*. The benefit is on **your** provider's bill, downstream.

## What it's for
Fitting more useful info into the context window and **lowering the LLM bill** of agents: compressing large payloads (bulky tool outputs, logs, RAG, files, history) before sending to the model. Neighbour of [RTK](rtk.md) and [Tokenade](tokenade.md), but covering more surfaces (lib + proxy + MCP + wrapper + middleware) and modalities (JSON, code AST, conversation, image).

## Notes
- "60–95%" claim: vendor order of magnitude, to be measured on your own payloads (answer quality vs compression ratio).
- Deterministic compression ≠ LLM summarization: no "semantic" loss through hallucination, but the gain depends on the data structure (JSON/code highly compressible, prose less so).
- GitHub org `headroomlabs-ai`, images published under `ghcr.io/chopratejas/*` (author Tejas Chopra).

## Source
- Repo: https://github.com/headroomlabs-ai/headroom — README (compression mechanics, integration modes, install), Apache 2.0 license. *(verified on 2026-06-23)*
