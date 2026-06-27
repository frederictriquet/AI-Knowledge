# AI tools — census

Exploration base for AI tools, organized around **three major usage domains**:

| Domain | File | Coverage |
|---------|---------|------------|
| **Generating code** | [generating code](guides/generer-du-code-avec-l-ia.md) | ✅ well stocked |
| **Embedding AI in a product** (integrated LLM, security, business agents) | [AI in a product](guides/mettre-de-l-ia-en-production.md) | 🟦 in progress |
| **AI for people who don't code** (marketing, sales…) | [for people who don't code](guides/ia-pour-ceux-qui-ne-codent-pas.md) | 🚧 to be built |

Each tool appears in the **topic page** of its objective(s), grouped by function **family** (tables generated from the frontmatter), and has a **detailed card** in [`tools/`](tools/). Candidates still to be triaged are in [`outils candidats.md`](outils%20candidats.md).

🗺️ Cross-cutting view: [**SDLC × AI tools — which tool for which phase**](sdlc-by-phase.md) (Mermaid diagram).

## Families by domain

**Generating code**
[1. Coding agents & IDEs](guides/generer-du-code-avec-l-ia.md#fam-coding-agents-ides) · [2. Code knowledge](guides/generer-du-code-avec-l-ia.md#fam-codebase-knowledge-graphs-search-memory) · [3. Token & behavior optimization](guides/maitriser-le-cout-en-tokens.md#fam-token-agent-behavior-optimization) · [4. Workflow / methodology / spec-driven](guides/generer-du-code-avec-l-ia.md#fam-workflow-methodology-spec-driven-development) · [5. Browser automation (MCP)](guides/generer-du-code-avec-l-ia.md#fam-browser-automation-mcp-servers) · [6. Terminal / shell assistants](guides/generer-du-code-avec-l-ia.md#fam-ai-assistants-for-terminal-shell) · [**7. AI code review**](guides/generer-du-code-avec-l-ia.md#fam-ai-code-review) · [**8. Documentation & external MCP sources**](guides/generer-du-code-avec-l-ia.md#fam-documentation-external-knowledge-sources-mcp-servers) · [**9. CI/CD, delivery & ops (AI)**](guides/generer-du-code-avec-l-ia.md#fam-ci-cd-delivery-ai-assisted-operations)

**Embedding AI in a product**
[1. RAG infrastructure / vector databases](guides/mettre-de-l-ia-en-production.md#fam-rag-infrastructure-vector-databases) · [2. Generalist multi-agent frameworks](guides/mettre-de-l-ia-en-production.md#fam-general-purpose-multi-agent-frameworks-for-developers) · [3. MCP knowledge sources (business data)](guides/mettre-de-l-ia-en-production.md#fam-specialized-knowledge-data-sources-mcp-servers) · [4. Multi-agent orchestration & enterprise automation](guides/mettre-de-l-ia-en-production.md#fam-multi-agent-orchestration-enterprise-automation) · [5. Autonomous agents specialized by domain](guides/mettre-de-l-ia-en-production.md#fam-domain-specialized-autonomous-agents) · [6. Security — tools via MCP](guides/mettre-de-l-ia-en-production.md#fam-security-tools-exposed-via-mcp) · [7. Computer / desktop control](guides/mettre-de-l-ia-en-production.md#fam-computer-desktop-control) · [**8. LLMOps — evaluation & observability**](guides/fiabiliser-evaluer-un-systeme-llm.md#fam-llmops-evaluation-observability) · [**9. LLM gateways / routers**](guides/maitriser-le-cout-en-tokens.md#fam-llm-gateways-routers)

**AI for people who don't code** — 🚧 to be defined.

## Reading grid: components of a loop → tool families

*[Loop engineering](concepts/loop-engineering.md)* (Addy Osmani) describes an autonomous agent loop in **6 components**. Each maps to a family of the census — handy for navigating between **theory** (`fiches/`) and **tools** (`tools/`):

| Loop component | Census family/families | Example tools |
|---------------------|---------------------------|-------------------|
| **Automations** (planning: `/loop`, `/goal`, GitHub Actions) | native Claude Code/Codex + [Agents & IDEs → orchestrators](guides/generer-du-code-avec-l-ia.md#fam-coding-orchestrators-multi-agent-systems) | orchestrators that plan/restart agents |
| **Worktrees** (isolate parallel work) | [Agents & IDEs → orchestrators](guides/generer-du-code-avec-l-ia.md#fam-coding-orchestrators-multi-agent-systems) | Conductor, Crystal, Orca, Supacode, Vibe Kanban |
| **Skills** (codify project knowledge, `SKILL.md`) | [Workflow / spec-driven](guides/generer-du-code-avec-l-ia.md#fam-workflow-methodology-spec-driven-development) | Superpowers, gstack, BMAD-METHOD, Cavekit, Spec Kit |
| **Plugins / Connectors** (external tools via MCP) | [Browser automation](guides/generer-du-code-avec-l-ia.md#fam-browser-automation-mcp-servers) & [MCP docs](guides/generer-du-code-avec-l-ia.md#fam-documentation-external-knowledge-sources-mcp-servers) · product side: [business sources](guides/mettre-de-l-ia-en-production.md#fam-specialized-knowledge-data-sources-mcp-servers), [security](guides/mettre-de-l-ia-en-production.md#fam-security-tools-exposed-via-mcp), [desktop](guides/mettre-de-l-ia-en-production.md#fam-computer-desktop-control) | browser (Playwright…), docs (Context7, Ref…), data (Ansvar), security (Burp…) |
| **Sub-agents** (separate ideation / verification) | [Agents & IDEs → orchestrators](guides/generer-du-code-avec-l-ia.md#fam-coding-orchestrators-multi-agent-systems) & [Code review](guides/generer-du-code-avec-l-ia.md#fam-ai-code-review) | Liza, Ruflo (disciplined); CodeRabbit, Greptile (verification) |
| **State / Memory** (persistent memory on disk) | [Code knowledge](guides/generer-du-code-avec-l-ia.md#fam-codebase-knowledge-graphs-search-memory) | Cavemem, GraphMind, Serena |

## Legend

**Type**: Application · MCP server · Plugin · Skill · CLI · IDE extension · Library · Web service

**Economic model** (icon):

| Icon | Meaning |
|-------|------|
| 🔓 | Open-source |
| 🎁 | Freemium (free + paid offer) |
| 🔁 | Subscription |
| 💳 | Pay-as-you-go |
| 🔒 | Proprietary / paid |

**LLM cost** — *who provides the LLM and how it is billed* (icon):

| Icon | Meaning |
|-------|------|
| 🟢 | *Built-in* — runs in/with Claude Code (or an existing subscription), or observes your own calls → no separate LLM cost |
| 📦 | *Included* — the vendor provides the LLM within the tool's price → predictable/capped cost |
| 💸 | *Resold per usage* — the vendor provides the LLM but bills by consumption (often with markup) |
| 🔑 | *BYOK* (Bring Your Own Key) — you provide your API key and pay the LLM provider directly per usage |
| ❓ | *Unverified* — LLM cost mechanism not publicly documented / not confirmed |

> One product can touch several families; it is classified by its primary use. Table row format: `**[Name](url)** · [📄](card) | Type | eco icon | LLM icon | one-line summary`.
