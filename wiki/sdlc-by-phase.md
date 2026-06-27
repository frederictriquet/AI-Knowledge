# SDLC × AI tools — which tool for which phase

> Synthesis view: the phases of the software development life cycle (SDLC) and the census's AI tools usable at each step. Derived from [generating code](guides/generate-code-with-ai.md) (+ security from [Embedding AI in a product](guides/ai-in-production.md)). The **cost/license icons** and the full list are in the per-family tables — here we only show the **mapping**.

```mermaid
flowchart TB
  classDef phase fill:#0d3b66,stroke:#0a2d4d,color:#fff;
  classDef trans fill:#3a2d5c,stroke:#241a3d,color:#fff;
  classDef gap fill:#5c3a3a,stroke:#3d2424,color:#fff;

  P["<b>1 · PLAN &amp; SPEC</b><br/><i>Workflow / methodology / spec-driven</i><br/>BMAD-METHOD · GitHub Spec Kit · GSD<br/>Task Master · Superpowers · gstack · Cavekit · Pheromind⚠️"]
  C["<b>2 · UNDERSTAND / CONTEXT</b><br/><i>Code knowledge</i><br/>Serena · CodeGraph · GraphMind · Polaris · Graphify · Cavemem<br/><br/><i>Docs &amp; external sources — MCP</i><br/>Context7 · Ref · GitMCP · Exa · MS Learn · AWS Docs"]
  D["<b>3 · CODE</b><br/><i>Agents &amp; IDEs</i><br/>Kilo Code · Trae · Continue⚠️<br/><br/><i>Multi-agent orchestrators</i><br/>Conductor · Orca · Vibe Kanban · Superset · Supacode<br/>Liza · Ruflo · Multica · Sculptor<br/><br/><i>Terminal / shell</i> : Neo-AI"]
  TE["<b>4 · TEST (web / UI)</b><br/><i>Browser automation — MCP</i><br/>Playwright MCP · Chrome DevTools MCP · Firefox DevTools MCP"]
  R["<b>5 · REVIEW (PR)</b><br/><i>AI code review</i><br/>CodeRabbit · Greptile · Sentry Seer · Cursor BugBot"]
  S["<b>6 · SECURE</b><br/><i>Defensive</i> : Snyk MCP (SAST/SCA)<br/><i>Offensive / pentest</i><br/>Kali MCP · Burp MCP · ZAP MCP · AIDA · Shannon"]
  O["<b>7 · DELIVER / DEPLOY / OPERATE</b><br/><i>CI/CD, delivery &amp; ops AI</i><br/>Mergify (CI / merge / flaky)<br/>Cleric · Resolve.ai · Traversal (AI SRE / incident)"]

  T["<b>⚙️ CROSS-CUTTING — cost &amp; behavior</b><br/>RTK · Tokenade · Caveman · Ponytail<br/><i>reduce input/output tokens & code scope, at every step</i>"]

  P --> C --> D --> TE --> R --> S --> O
  O -.->|next iteration| P
  T -.->|applies everywhere| D

  class P,C,D,TE,R,S,O phase;
  class T trans;
```

## Detailed mapping (to families, for costs & the full list)

| SDLC phase | Tool families (click → full table + costs) |
|---|---|
| **1. Plan & spec** | [Workflow / methodology / spec-driven](guides/generate-code-with-ai.md#fam-workflow-methodology-spec-driven-development) |
| **2. Understand / context** | [Code knowledge](guides/generate-code-with-ai.md#fam-codebase-knowledge-graphs-search-memory) · [Docs & MCP sources](guides/generate-code-with-ai.md#fam-documentation-external-knowledge-sources-mcp-servers) |
| **3. Code** | [Agents & IDEs](guides/generate-code-with-ai.md#fam-coding-agents-ides) · [Multi-agent orchestrators](guides/generate-code-with-ai.md#fam-coding-orchestrators-multi-agent-systems) · [Terminal / shell](guides/generate-code-with-ai.md#fam-ai-assistants-for-terminal-shell) |
| **4. Test (web/UI)** | [Browser automation (MCP)](guides/generate-code-with-ai.md#fam-browser-automation-mcp-servers) |
| **5. Review (PR)** | [AI code review](guides/generate-code-with-ai.md#fam-ai-code-review) |
| **6. Secure** | [Security via MCP](guides/ai-in-production.md#fam-security-tools-exposed-via-mcp) · [Pentest agents](guides/ai-in-production.md#fam-domain-specialized-autonomous-agents) |
| **7. Deliver / deploy / operate** | [CI/CD, delivery & ops AI](guides/generate-code-with-ai.md#fam-ci-cd-delivery-ai-assisted-operations) · [LLMOps](guides/build-reliable-llm-systems.md#fam-llmops-evaluation-observability) *(if LLM product)* |
| **Cross-cutting** | [Token & behavior optimization](guides/control-token-cost.md#fam-token-agent-behavior-optimization) |

## Honest notes
- **Phase 7 (deliver / deploy / operate)**: now covered by the [CI/CD, delivery & ops AI](guides/generate-code-with-ai.md#fam-ci-cd-delivery-ai-assisted-operations) family — CI/merge/flaky (**Mergify**) and **AI SRE / incident** (**Cleric · Resolve.ai · Traversal**). Acknowledged caveats: AI SREs are **proprietary enterprise SaaS / quote-based** (LLM included 📦) and the ops aspect **spills over into "operating a product"** (boundary with *embedding AI in a product*); [LLM observability](guides/build-reliable-llm-systems.md#fam-llmops-evaluation-observability) (Langfuse, Helicone…) remains distinct (a product that embeds an LLM, not code deployment). The most "agent" CI-AI (Datadog Bits AI Dev Agent, Aviator, Trunk) remains in **unverified candidates**.
- **Tools excluded from the diagram because deprecated** (still in the tables, with ⚠️): **Puppeteer MCP** (archived), **Crystal** (→ Nimbalyst). **Continue** (⚠️ acquired by Cursor) and **Pheromind** (⚠️ unclear status) kept but flagged.
- The SDLC is **iterative** (the 7→1 arrow): most of these tools serve on each pass of the loop, not just once.
- Many tools are **multi-phase** (an agent like Kilo also helps with understanding/testing); they are placed here at their **primary use**.

*(synthesis generated on 2026-06-18 from the per-domain tables; regenerate if the families change.)*
