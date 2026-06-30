# AI tools — candidates to arbitrate

List of candidates **complementary** to the census ([`tools-hub.md`](wiki/tools-hub.md)), classified by existing family.

**How to arbitrate**: tick `- [x]` the ones to add (or tell me "the whole family X"). For each tool retained, I'll verify at the source (license, business model, **LLM cost** — key required? backend? local?) before recording it, then I'll create its note.

> ⚠️ These names come from my knowledge + the "neighbors" cited in the notes. **Nothing is verified yet** — status/license/price to be confirmed at the time of addition.

> ✅ **Integrated as of 2026-06-17** (the `[x]` below): **Generate code** — Continue (1a); Crystal, Sculptor (1b); GitHub Spec Kit, Task Master, Pheromind (4); Ref, Context7, GitMCP, Exa MCP, Microsoft Learn MCP, AWS Documentation MCP (→ family *Documentation & external MCP sources*, new). **AI in a product** — pgvector, Qdrant, Weaviate, Milvus, LanceDB, Pinecone, Turbopuffer (fam. 1); LangGraph, AutoGen/AG2, OpenAI Agents SDK, LlamaIndex, Pydantic AI, Mastra (fam. 2); Flowise, Sim, Gumloop, Relay.app (fam. 4). Families 12 (LLMOps) & 13 (routers) already done. *Anything left unticked = to arbitrate.*

---

## 1a — Agents & IDEs that code
- [ ] **Cursor** — AI IDE (VS Code fork), subscription + included/usage models
- [ ] **Windsurf** — AI IDE (VS Code fork), direct competitor to Cursor
- [ ] **GitHub Copilot** — the legacy one, in VS Code / JetBrains
- [ ] **Cline** — open-source VS Code extension (lineage from which Kilo descends)
- [ ] **Roo Code** — fork/evolution of Cline, open-source
- [x] **Continue** — open-source VS Code/JetBrains extension
- [ ] **Aider** — open-source CLI agent (git pair-programming)
- [ ] **Zed** — fast native editor with built-in agent
- [X] **Amp** (Sourcegraph) — coding agent
- [ ] **Codex CLI** (OpenAI) — agent CLI
- [ ] **Gemini CLI** (Google) — agent CLI

## 1b — Coding orchestrators / multi-agents
- [ ] **Intent** — macOS orchestrator (competitor to Conductor, already cited)
- [x] **Crystal** — multi-agent runner (worktrees)
- [x] **Sculptor** (Imbue) — agent orchestrator
- [ ] **Terragon** — coding agent orchestration
- [ ] **Async** — agent orchestrator
- [ ] **Devin** (Cognition) — autonomous cloud agent
- [ ] **Factory (Droids)** — autonomous agent platform
- [ ] **claude-squad** — terminal multi-agent manager (open-source)
- [ ] **uzi** — multi-agent manager (open-source)

## 2 — Code knowledge
- [ ] **Sourcegraph / Cody** — code search & context at scale
- [ ] **Greptile** — codebase understanding
- [ ] **Glean** — enterprise search (beyond code)
- [ ] **Repomix** — "codebase → prompt" (overlaps fam. 3)
- [ ] **code2prompt** — context packer (overlaps fam. 3)
- [ ] **files-to-prompt** — file concat for prompts
- [ ] **ast-grep** — structural / AST search
- [ ] **Probe** — code search for agents

## 3 — Token & behavior optimization
- [ ] **LLMLingua** (Microsoft) — prompt compression
- [ ] **ccusage / cc-usage** — Claude Code consumption analytics
- [ ] (Repomix / code2prompt — see fam. 2, straddling)

## 4 — Workflow, methodology & spec-driven
- [ ] **Kiro** (AWS) — spec-driven IDE
- [x] **GitHub Spec Kit** — open-source spec-driven dev
- [ ] **OpenSpec** — open-source spec-driven
- [x] **Task Master** (claude-task-master) — task management for agents
- [ ] **Agent OS** — methodology/standards framework
- [x] **Pheromind** — "pheromone-based" multi-agent framework

## 5 — RAG infrastructure / vector databases
> ✅ *Family handled on 2026-06-16 — 7 notes created and added to [AI in a product](wiki/guides/ai-in-production.md), family 1 (alongside Chroma).*
- [x] **Pinecone** — managed vector database (proprietary/cloud)
- [x] **Weaviate** — open-source vector database + cloud
- [x] **Qdrant** — open-source vector database (Rust) + cloud
- [x] **Milvus** — large-scale open-source vector database
- [x] **pgvector** — Postgres extension
- [x] **LanceDB** — embedded vector database
- [x] **Turbopuffer** — serverless vector database

## 6 — Enterprise orchestration & automation
- [ ] **n8n** — open-source automation (+ AI)
- [ ] **Make** — no-code automation
- [ ] **Zapier (AI)** — consumer automation + agents
- [ ] **Activepieces** — open-source automation
- [ ] **Dify** — open-source LLM app platform
- [x] **Flowise** — open-source agent/flow builder
- [x] **Sim** — agent builder
- [x] **Gumloop** — AI automation
- [ ] **Lindy** — business assistants/agents
- [x] **Relay.app** — automation with human-in-the-loop
- [ ] **Microsoft Copilot Studio** — enterprise agents (cited, neighbor of MindFlight)
- [ ] **watsonx Orchestrate** (IBM) — multi-agent orchestration (cited)

## 7 — Generalist multi-agent frameworks (for developers)
> ✅ *6 notes created on 2026-06-16 and added to [AI in a product](wiki/guides/ai-in-production.md), family 2 (alongside CrewAI). Still to arbitrate: Google ADK, Agno, smolagents, Strands.*
- [x] **LangGraph** (LangChain) — agent graphs (cited, peer of CrewAI)
- [x] **AutoGen / AG2** (Microsoft) — multi-agent framework (cited)
- [x] **OpenAI Agents SDK** — agent framework (cited)
- [x] **LlamaIndex** (+ Agents) — RAG + agents
- [x] **Pydantic AI** — typed agent framework (Python)
- [ ] **Google ADK** — Agent Development Kit
- [x] **Mastra** — TypeScript agent framework
- [ ] **Agno** (ex-phidata) — agent framework
- [ ] **smolagents** (Hugging Face) — lightweight agents
- [ ] **Strands** (AWS) — agent SDK

## 8 — Knowledge sources (MCP servers)
- [x] **Context7** — up-to-date library docs via MCP (already connected in the session) ✅ Docs & MCP sources
- [x] **GitMCP** — expose a GitHub repo as MCP ✅ Docs & MCP sources
- [x] **Ref** — technical docs as MCP
- [x] **Exa MCP** — web/neural search as MCP ✅ Docs & MCP sources
- [x] **Microsoft Learn MCP** — Microsoft docs ✅ Docs & MCP sources
- [x] **AWS Documentation MCP** — AWS docs ✅ Docs & MCP sources
- [ ] **US-law-mcp / US_Compliance_MCP** (Ansvar) — if they reappear (currently 404)
- [ ] **Reference MCP servers** (filesystem, fetch, GitHub, Slack…)

## 9a — Browser automation (MCP)
- [ ] **browser-use** — browser automation for agents (open-source)
- [ ] **Stagehand** (Browserbase) — AI browser automation
- [ ] **Browserbase** — cloud browsers for agents
- [ ] **Hyperbrowser** — browser infra for agents
- [ ] **Browser MCP** (browsermcp.io) — drive your local browser via MCP
- [ ] **WebMCP** — standard for exposing web pages to agents

## 9b — Security (tools via MCP)
- [ ] **Semgrep MCP** — SAST (defensive)
- [ ] **Nuclei MCP** — vulnerability scanning (offensive/def.)
- [ ] **Metasploit MCP** — exploitation (offensive)
- [ ] **CodeQL** — code analysis (defensive)
- [ ] **Trivy** — container/dependency scanning (defensive)

## 9c — Computer / desktop control
- [ ] **OpenAI Operator / computer use** — agent that drives a browser/computer
- [ ] **UI-TARS** (ByteDance) — GUI control model/agent
- [ ] **Claude for Chrome** — browser control extension by Claude
- [ ] **Open Interpreter** — local machine code execution/control

## 10 — Specialized autonomous agents
- [ ] **XBOW** — autonomous pentest (and benchmark cited by Shannon)
- [ ] **Strix** — autonomous security agent
- [ ] **CAI** (Cybersecurity AI) — security agent framework
- [ ] **PentAGI** — autonomous pentest
- [ ] **Nebula** — pentest assistant/agent
- [ ] **GPT Researcher** — autonomous research agent (outside security)

## 11 — Terminal / shell assistants
- [ ] **Warp** (Agent Mode) — modern terminal with agent
- [ ] **Amazon Q Developer CLI** — AWS shell/dev assistant
- [ ] **Gemini CLI** (Google) — also a terminal assistant
- [ ] **ShellGPT** — open-source shell assistant
- [ ] **Aichat** — open-source shell assistant (Rust)
- [ ] **Butterfish** — shell assistant
- [ ] **tgpt** — lightweight terminal LLM client

---

## CI/CD, delivery & ops (AI) — generate code, CI/CD & ops family (created on 2026-06-18)
*Family created to fill phase 7 of the SDLC. Already added & verified: Mergify, Cleric, Resolve.ai, Traversal. Remaining candidates to arbitrate:*
- [ ] **Datadog Bits AI Dev Agent** — autonomous flaky-test fix → draft PR (Datadog add-on); the most "agent" on the CI side
- [ ] **Aviator** — AI merge queue + flaky management
- [ ] **Trunk** — flaky-test detection/quarantine (Trunk Flaky Tests)
- [ ] **Rootly** — incident management + AI SRE (long-standing SOC2)
- [ ] **PagerDuty AIOps** / **Datadog Bits AI** — AIOps incumbents (correlation/incident)
- [ ] **Pulumi AI** — AI-assisted IaC (infra deployment)

---

## Leads for NEW families (broadening beyond pure dev)
- [x] **12. LLM evaluation / observability** — Langfuse, LangSmith, Braintrust, Helicone, Arize Phoenix ✅ *added to [AI in a product](wiki/guides/ai-in-production.md), family 8 (LLMOps)*
- [x] **13. LLM gateways / routers** — **OpenRouter**, **LiteLLM**, **Portkey**, **Requesty** ✅ *added to [AI in a product](wiki/guides/ai-in-production.md), family 9 (verified on 2026-06-16)*
- [ ] **14. Voice agents** — (to define if relevant)
- [ ] **15. Image / video generation** — (probably out of scope)

---

### Recommendations (my opinion)
1. **LLM routers** (OpenRouter, LiteLLM) — squarely in your cost theme.
2. **Big missing agents/IDEs** (Cursor, Windsurf, Cline, Aider) — building blocks that most other tools orchestrate.
3. **Context7** — already present in your session, natural fit for family 8.
