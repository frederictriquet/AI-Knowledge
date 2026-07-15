---
tool: "oh-my-pi (omp)"
title: "oh-my-pi (omp)"
themes: [frameworks-tooling, efficiency-cost, multi-agent]
type: "CLI / TUI (terminal coding agent)"
url: https://omp.sh/
pricing_model: "Open-source (MIT)"
llm_cost: "🔑 BYOK (per-token API keys) OR 🟢 routed through an existing OAuth / coding-plan subscription; local models supported"
family: "Coding agents & IDEs"
objectives: [code-generation]
eco_icons: "🔓"
llm_cost_icons: "🔑🟢"
summary: "Open-source (MIT) terminal coding agent (TS + Rust core). Brings **your own model access across 40+ providers** — 🔑 API keys (pay-per-token) or 🟢 OAuth / coding-plan subscription (rides an existing plan). Token-optimized harness (hash-anchored edits, LSP, subagents, an *advisor* reviewer model). Alternative to Claude Code / Codex / aider"
---

# oh-my-pi (omp)

**In one sentence** — An open-source (MIT) terminal coding agent that plugs into 40+ LLM providers via your own keys/accounts (BYOK), built around a token-optimized tool harness (anchored edits, LSP, subagents, and a second "advisor" model watching each turn).

## Type & integration
Standalone **CLI/TUI** coding agent (TypeScript host + ~55k-line Rust core), by Mario Zechner. You run `omp` in a terminal; it drives edits, search, LSP (14 ops), DAP debug (28 ops), a browser tool, Python, image gen/inspect, and web search across ranked providers. Model roles route work by intent (`default`, `smol` for cheap subagent fan-out, `slow` for reasoning, `plan`, `commit`), swappable mid-session. Also embeddable as a library (Node/TS hosts import `ModelRegistry`, `SessionManager`, `createAgentSession`). Not an MCP server or a wrapper around Claude Code — it **is** the agent.

## Pricing model
**Open-source, MIT** (© 2025 Mario Zechner). Free; no paid tier or hosted/pro offering found on omp.sh (verified 2026-07-15).

## LLM cost
**🔑🟢 — you bring your own model access; omp bundles and resells nothing.** Two distinct cost mechanisms, depending on how you connect (40+ providers + custom OpenAI/Anthropic/Google-compatible endpoints, per-role fallback chains, round-robin credentials):
- **🔑 BYOK** — direct **API keys** (Anthropic, OpenAI, xAI, Gemini…) → you pay the provider **per token**.
- **🟢 existing subscription** — `oauth` (sign in with your provider account) or `plan` (route through a **coding-plan subscription you already pay for**, e.g. Anthropic OAuth, Codex, Copilot, GLM) → no separate/metered LLM cost beyond that flat plan. `local` (Ollama/vLLM/llama.cpp) runs self-hosted, key optional.

So a literal API **key is not required** if you attach an OAuth account or coding-plan subscription (BYOK ≠ bring-your-own-subscription). Either way the cost lands on your own provider account — omp is not a metered reseller.

## What it's for
A fast, provider-agnostic alternative to Claude Code / Codex / aider for people who want to **pick any model** and keep costs on their own accounts. Its differentiator is the **harness**: hash-anchored edits (the model points at anchors instead of retyping lines) that the author reports cut wasted "string-not-found" retry loops — self-declared figures such as *Grok 4 Fast −61% output tokens* and a *Grok Code Fast 1 6.7%→68.3%* edit-success lift (vendor benchmarks on omp's own harness, to treat as such). Cross-session memory (`retain`/`recall`), inline rule-injection on regex match, and an **advisor** reviewer model that reads every turn add lightweight verification.

## Notes
- **Popular & active**: ~17.8k GitHub stars, pushed the day of verification — but a single-maintainer project moving fast; expect churn.
- **Self-declared benchmarks**: the token/edit-success numbers come from the project itself; no independent eval. Weight accordingly.
- **BYOK trade-off**: full model freedom, but you manage credentials, quotas and spend yourself (no bundled/predictable pricing).
- **Alternatives**: [Continue](continue.md), Claude Code, OpenAI Codex, aider, [Kilo Code](kilo-code.md), opencode. omp's angle vs these = provider breadth + an aggressively token-optimized harness.

## Source
https://omp.sh/ · https://github.com/can1357/oh-my-pi (LICENSE = MIT; README: providers/auth, harness) · https://omp.sh/docs/providers. *(verified on 2026-07-15)*
