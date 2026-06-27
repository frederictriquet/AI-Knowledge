---
type: index
title: "Theme — Tools & function calling"
theme: tools-function-calling
---

# 🔧 Tools & function calling

> ⚙️ **Generated file** by `tools/build_index.py` — do not edit by hand.

_Giving an agent tools and refining the agent-computer interface._

## Concepts (11)

### 🔴 Substance / core
- **[CodeAct (code as action space)](../concepts/codeact.md)** — the agent emits **executable Python code** as its action, instead of rigid JSON tool calls.
- **[Computer-use & GUI agents](../concepts/computer-use-gui-agents.md)** — driving a browser or an OS like a human, via **screenshots** as input and **actions** (click, type, scroll) as output.
- **[The canonical framework: Agent = LLM + Planning + Memory + Tools](../concepts/canonical-agent-architecture.md)** — the reference decomposition of an autonomous agent: an LLM plays the role of the brain (controller), supported by three components — planning, memory and tool use.
- **[Toolformer](../concepts/toolformer.md)** — an LLM *fine-tuned* to decide on its own when and how to call a tool, without few-shot examples or an orchestration prompt.
- **[Voyager & skill library](../concepts/voyager-skill-library.md)** — a continually-learning agent that **acquires, stores and reuses** skills as code, building itself a self-constructed procedural memory.

### 🟡 Tradeoff / intermediate
- **[LLM Compiler (parallel function calling)](../concepts/llm-compiler.md)** — plan a **DAG of tool calls** and execute in parallel those that are independent, instead of chaining them sequentially like ReAct.
- **[LLM nested inside a tool](../concepts/llm-in-a-tool.md)** — a tool called by the agent itself uses an LLM call internally (e.g. a yes/no relevance classifier).
- **[MRKL Systems](../concepts/mrkl.md)** — a **routing** architecture where an LLM directs each request to a set of expert modules (symbolic: calculator, database, API; or neural).
- **[ReAct vs function calling](../concepts/react-vs-function-calling.md)** — function calling is faster and more economical on predictable tasks; ReAct handles the unpredictable better at the cost of reasoning-loop tokens.
- **[Tool grounding](../concepts/tool-grounding.md)** — giving the agent tools that expose the verifiable legal state (e.g. legal chess moves) to prevent it from hallucinating its decisions.

### 🟢 Overview / introductory
- **[Tool calling / function calling](../concepts/tool-calling.md)** — the model emits a structured call (JSON + tool_call_id) that your code executes, then whose result it feeds back in.

## Tools (6)

- **[Chrome DevTools MCP](../tools/chrome-devtools-mcp.md)** — _MCP server (browser automation)_
- **[Computer use (Anthropic / Claude)](../tools/computer-use.md)** — _Model capability/tool (Anthropic API) + open-source reference implementation_
- **[Firefox DevTools MCP](../tools/firefox-devtools-mcp.md)** — _MCP server (browser automation / inspection)_
- **[Playwright MCP](../tools/playwright-mcp.md)** — _MCP server (browser automation)_
- **[Puppeteer MCP](../tools/puppeteer-mcp.md)** — _MCP server (browser automation)_
- **[Serena](../tools/serena.md)** — _MCP server / coding-agent toolkit_
