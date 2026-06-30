---
type: index
title: "Theme — Governance, alignment & ops"
theme: governance-alignment-ops
---

# ⚖️ Governance, alignment & ops

> ⚙️ **Generated file** by `tools/build_index.py` — do not edit by hand.

_Steering, observing and governing systems in production._

## Concepts (13)

### 🔴 Substance / core
- **[Agent ethics & governance](../concepts/ethics-governance.md)** — align agents on natural-language policy documents and organize oversight where the human decides while the AI questions, all framed by governance agents, ethical sandboxes and a kill switch.
- **[AgentOps](../concepts/agentops.md)** — the DevOps/MLOps of agents: instrumenting execution at the session → trace → span level to make a non-deterministic black box observable, with cost and latency per step and multi-LLM routing.
- **[Constitutional AI & RLAIF](../concepts/constitutional-ai-rlaif.md)** — aligning a model via a set of **written principles**: the model critiques and revises its own outputs against the "constitution", and training runs on this AI feedback (RLAIF) instead of human annotations (RLHF).
- **[DSPy](../concepts/dspy.md)** — "programming, not prompting": you declare signatures and modules in Python, and optimisers automatically compile the prompts against a metric, instead of writing and tinkering with them by hand.
- **[DSPy: compilation & bootstrapping](../concepts/dspy-compilation-bootstrap.md)** — compiling a DSPy program means letting a teleprompter automatically *bootstrap* good demonstrations by simulating the pipeline, filtering the traces that pass the metric, then selecting the best candidates — and the paper shows this process takes modest LMs from 4–20% to 49–88% accuracy on GSM8K in a few minutes.
- **[DSPy: signatures, modules, optimisers](../concepts/dspy-signatures-modules-optimizers.md)** — DSPy replaces hard-coded "prompt templates" with three composable abstractions — declarative *signatures*, parameterised *modules* (Predict, ChainOfThought, ReAct…) and *teleprompters* (optimisers) — so that you program an LM pipeline instead of writing prompts.
- **[Defensive UX for LLM products](../concepts/defensive-ux-for-llm.md)** — an LLM makes mistakes, hallucinates and answers slowly *by construction*; defensive UX designs the interface starting from that fallibility rather than denying it — guide the input, handle the error gracefully, and keep the human in control of the output.
- **[LLM observability: best practices (tool-agnostic)](../concepts/llm-observability-best-practices.md)** — instrumenting an LLM app is not wiring up a dashboard: it is deciding *what* to trace (a span per chain step), *how* to evaluate quality without going broke or fooling yourself (a calibrated, sampled judge), and *what not to ingest* (PII) — the tool is merely the receptacle.
- **[LLM resilience & fallback](../concepts/resilience-fallback-llm.md)** — an LLM call is a network call to a fallible third-party service (429, 5xx, timeout, quality drift): a serious product applies the reflexes of distributed reliability — retry with backoff, timeout, fallback to another model/provider, circuit breaker and graceful degradation.
- **[Loop engineering: designing the system that prompts the agent](../concepts/loop-engineering.md)** — The leverage shifts from prompt engineering to *loop engineering*: instead of prompting the agent by hand, you design an autonomous system that discovers the work, distributes it to agents, verifies, documents and decides what comes next — with no human between cycles.

### 🟡 Tradeoff / intermediate
- **[Comprehension debt & cognitive surrender](../concepts/comprehension-debt.md)** — the faster an agent loop ships code you did not write, the wider the gap grows between what exists and what you understand — a "debt" that, ignored, slides toward "cognitive surrender".
- **[Deterministic hooks vs probabilistic memory (Skills / Memory / Hooks)](../concepts/deterministic-hooks-vs-probabilistic-memory.md)** — For a coding agent to honor a rule, the mechanism matters more than the wording: an instruction in memory (CLAUDE.md) is **probabilistic context** the model *may* follow, whereas a **hook** is a shell command run deterministically at a lifecycle point, which *guarantees* the action whatever the model decides — hence the triad "Skills = advice, Memory = reminder, Hooks = law".
- **[Human-in-the-loop: static vs dynamic interrupts](../concepts/human-in-the-loop-static-dynamic.md)** — two LangGraph mechanisms to insert a human in the loop: predetermined breakpoints around a node (static), or an `interrupt()` call triggered from inside a node based on state (dynamic).

## Tools (18)

- **[Ansvar Compliance MCP (suite)](../tools/ansvar-compliance-mcp.md)** — _Suite of MCP servers (regulatory / legal data sources)_
- **[Arize Phoenix / Arize AX](../tools/phoenix-arize.md)** — _Open-source library/app (Phoenix) + SaaS web service (Arize AX)_
- **[Cleric](../tools/cleric.md)** — _SaaS platform — AI SRE (incident investigation)_
- **[ECC](../tools/ecc.md)** — _Agent harness system (skills/agents/hooks/rules) — multi-platform, OSS + GitHub App_
- **[Helicone](../tools/helicone.md)** — _Web service (proxy/gateway) + open-source self-host_
- **[Langfuse](../tools/langfuse.md)** — _Web service (cloud) + open-source self-host_
- **[LangSmith](../tools/langsmith.md)** — _Web service (SaaS) + SDK_
- **[LiteLLM](../tools/litellm.md)** — _Python library (SDK) + self-host Proxy/Gateway (open-source) + Enterprise_
- **[Mergify](../tools/mergify.md)** — _SaaS platform — merge queue & CI (flaky-test detection)_
- **[MindFlight Orchestrator (MFO)](../tools/mindflight-orchestrator.md)** — _Platform (AI agent orchestration / enterprise automation)_
- **[OpenRouter](../tools/openrouter.md)** — _Web service (hosted LLM gateway)_
- **[Paperclip](../tools/paperclip.md)** — _Open-source AI-agent orchestration and governance platform (\"zero-human companies\")_
- **[Portkey](../tools/portkey.md)** — _Open-source AI Gateway (MIT) self-host + Web service (managed SaaS)_
- **[Relay.app](../tools/relay-app.md)** — _AI workflow automation + human-in-the-loop (SaaS)_
- **[Requesty](../tools/requesty.md)** — _Web service (hosted LLM gateway)_
- **[Resolve.ai](../tools/resolve-ai.md)** — _SaaS platform — AI SRE / production engineering_
- **[Sentry Seer](../tools/sentry-seer.md)** — _Web service (Sentry add-on)_
- **[Traversal](../tools/traversal.md)** — _SaaS platform — AI SRE (RCA at scale)_
