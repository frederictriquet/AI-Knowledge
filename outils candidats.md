# Outils IA — candidats à arbitrer

Liste de candidats **complémentaires** au recensement ([`outils IA.md`](outils%20IA.md)), classés par famille existante.

**Comment arbitrer** : coche `- [x]` ceux à ajouter (ou dis-moi « toute la famille X »). Pour chaque outil retenu, je vérifierai à la source (licence, modèle éco, **coût LLM** — clé requise ? backend ? local ?) avant de l'inscrire, puis je créerai sa fiche.

> ⚠️ Ces noms viennent de mes connaissances + des « voisins » cités dans les fiches. **Rien n'est encore vérifié** — statut/licence/prix à confirmer au moment de l'ajout.

> ✅ **Intégrés au 2026-06-17** (les `[x]` ci-dessous) : **Produire du code** — Continue (1a) ; Crystal, Sculptor (1b) ; GitHub Spec Kit, Task Master, Pheromind (4) ; Ref, Context7, GitMCP, Exa MCP, Microsoft Learn MCP, AWS Documentation MCP (→ famille *Documentation & sources MCP externes*, nouvelle). **IA dans un produit** — pgvector, Qdrant, Weaviate, Milvus, LanceDB, Pinecone, Turbopuffer (fam. 1) ; LangGraph, AutoGen/AG2, OpenAI Agents SDK, LlamaIndex, Pydantic AI, Mastra (fam. 2) ; Flowise, Sim, Gumloop, Relay.app (fam. 4). Familles 12 (LLMOps) & 13 (routeurs) déjà faites. *Reste non coché = à arbitrer.*

---

## 1a — Agents & IDE qui codent
- [ ] **Cursor** — IDE IA (fork VS Code), abonnement + modèles inclus/usage
- [ ] **Windsurf** — IDE IA (fork VS Code), concurrent direct de Cursor
- [ ] **GitHub Copilot** — l'historique, dans VS Code / JetBrains
- [ ] **Cline** — extension VS Code open-source (lignée dont descend Kilo)
- [ ] **Roo Code** — fork/évolution de Cline, open-source
- [x] **Continue** — extension open-source VS Code/JetBrains
- [ ] **Aider** — agent CLI open-source (pair-programming git)
- [ ] **Zed** — éditeur natif rapide avec agent intégré
- [X] **Amp** (Sourcegraph) — agent de codage
- [ ] **Codex CLI** (OpenAI) — CLI d'agent
- [ ] **Gemini CLI** (Google) — CLI d'agent

## 1b — Orchestrateurs / multi-agents de codage
- [ ] **Intent** — orchestrateur macOS (concurrent de Conductor, déjà cité)
- [x] **Crystal** — runner multi-agents (worktrees)
- [x] **Sculptor** (Imbue) — orchestrateur d'agents
- [ ] **Terragon** — orchestration d'agents de codage
- [ ] **Async** — orchestrateur d'agents
- [ ] **Devin** (Cognition) — agent cloud autonome
- [ ] **Factory (Droids)** — plateforme d'agents autonomes
- [ ] **claude-squad** — gestionnaire multi-agents terminal (open-source)
- [ ] **uzi** — gestionnaire multi-agents (open-source)

## 2 — Connaissance du code
- [ ] **Sourcegraph / Cody** — recherche & contexte code à l'échelle
- [ ] **Greptile** — compréhension de codebase
- [ ] **Glean** — recherche entreprise (au-delà du code)
- [ ] **Repomix** — « codebase → prompt » (chevauche fam. 3)
- [ ] **code2prompt** — packer de contexte (chevauche fam. 3)
- [ ] **files-to-prompt** — concat de fichiers pour prompt
- [ ] **ast-grep** — recherche structurelle / AST
- [ ] **Probe** — recherche code pour agents

## 3 — Optimisation tokens & comportement
- [ ] **LLMLingua** (Microsoft) — compression de prompt
- [ ] **ccusage / cc-usage** — analytics de consommation Claude Code
- [ ] (Repomix / code2prompt — voir fam. 2, à cheval)

## 4 — Workflow, méthodologie & spec-driven
- [ ] **Kiro** (AWS) — IDE spec-driven
- [x] **GitHub Spec Kit** — spec-driven dev open-source
- [ ] **OpenSpec** — spec-driven open-source
- [x] **Task Master** (claude-task-master) — gestion de tâches pour agents
- [ ] **Agent OS** — framework de méthodo/standards
- [x] **Pheromind** — framework multi-agents « pheromone-based »

## 5 — Infrastructure RAG / bases vectorielles
> ✅ *Famille traitée le 2026-06-16 — 7 fiches créées et ajoutées à [IA dans un produit](ia-dans-un-produit.md), famille 1 (aux côtés de Chroma).*
- [x] **Pinecone** — base vectorielle managée (propriétaire/cloud)
- [x] **Weaviate** — base vectorielle open-source + cloud
- [x] **Qdrant** — base vectorielle open-source (Rust) + cloud
- [x] **Milvus** — base vectorielle open-source à grande échelle
- [x] **pgvector** — extension Postgres
- [x] **LanceDB** — base vectorielle embarquée
- [x] **Turbopuffer** — base vectorielle serverless

## 6 — Orchestration & automatisation d'entreprise
- [ ] **n8n** — automatisation open-source (+ IA)
- [ ] **Make** — automatisation no-code
- [ ] **Zapier (AI)** — automatisation grand public + agents
- [ ] **Activepieces** — automatisation open-source
- [ ] **Dify** — plateforme d'apps LLM open-source
- [x] **Flowise** — builder d'agents/flux open-source
- [x] **Sim** — builder d'agents
- [x] **Gumloop** — automatisation IA
- [ ] **Lindy** — assistants/agents business
- [x] **Relay.app** — automatisation avec humain-dans-la-boucle
- [ ] **Microsoft Copilot Studio** — agents entreprise (cité, voisin MindFlight)
- [ ] **watsonx Orchestrate** (IBM) — orchestration multi-agents (cité)

## 7 — Frameworks multi-agents généralistes (pour développeurs)
> ✅ *6 fiches créées le 2026-06-16 et ajoutées à [IA dans un produit](ia-dans-un-produit.md), famille 2 (aux côtés de CrewAI). Restent à arbitrer : Google ADK, Agno, smolagents, Strands.*
- [x] **LangGraph** (LangChain) — graphes d'agents (cité, pair de CrewAI)
- [x] **AutoGen / AG2** (Microsoft) — framework multi-agents (cité)
- [x] **OpenAI Agents SDK** — framework d'agents (cité)
- [x] **LlamaIndex** (+ Agents) — RAG + agents
- [x] **Pydantic AI** — framework d'agents typé (Python)
- [ ] **Google ADK** — Agent Development Kit
- [x] **Mastra** — framework d'agents TypeScript
- [ ] **Agno** (ex-phidata) — framework d'agents
- [ ] **smolagents** (Hugging Face) — agents légers
- [ ] **Strands** (AWS) — SDK d'agents

## 8 — Sources de connaissances (serveurs MCP)
- [x] **Context7** — doc de libs à jour via MCP (déjà connecté dans la session) ✅ Doc & sources MCP
- [x] **GitMCP** — exposer un repo GitHub en MCP ✅ Doc & sources MCP
- [x] **Ref** — doc technique en MCP
- [x] **Exa MCP** — recherche web/néon en MCP ✅ Doc & sources MCP
- [x] **Microsoft Learn MCP** — doc Microsoft ✅ Doc & sources MCP
- [x] **AWS Documentation MCP** — doc AWS ✅ Doc & sources MCP
- [ ] **US-law-mcp / US_Compliance_MCP** (Ansvar) — si réapparaissent (actuellement 404)
- [ ] **Serveurs MCP de référence** (filesystem, fetch, GitHub, Slack…)

## 9a — Automatisation navigateur (MCP)
- [ ] **browser-use** — automatisation navigateur pour agents (open-source)
- [ ] **Stagehand** (Browserbase) — automatisation navigateur par IA
- [ ] **Browserbase** — navigateurs cloud pour agents
- [ ] **Hyperbrowser** — infra navigateur pour agents
- [ ] **Browser MCP** (browsermcp.io) — pilote ton navigateur local via MCP
- [ ] **WebMCP** — standard d'exposition de pages web aux agents

## 9b — Sécurité (outils via MCP)
- [ ] **Semgrep MCP** — SAST (défensif)
- [ ] **Nuclei MCP** — scan de vulnérabilités (offensif/déf.)
- [ ] **Metasploit MCP** — exploitation (offensif)
- [ ] **CodeQL** — analyse de code (défensif)
- [ ] **Trivy** — scan conteneurs/dépendances (défensif)

## 9c — Contrôle d'ordinateur / desktop
- [ ] **OpenAI Operator / computer use** — agent qui pilote un navigateur/ordinateur
- [ ] **UI-TARS** (ByteDance) — modèle/agent de contrôle GUI
- [ ] **Claude for Chrome** — extension de contrôle navigateur par Claude
- [ ] **Open Interpreter** — exécution de code/contrôle machine local

## 10 — Agents autonomes spécialisés
- [ ] **XBOW** — pentest autonome (et benchmark cité par Shannon)
- [ ] **Strix** — agent de sécurité autonome
- [ ] **CAI** (Cybersecurity AI) — framework d'agents sécurité
- [ ] **PentAGI** — pentest autonome
- [ ] **Nebula** — assistant/agent pentest
- [ ] **GPT Researcher** — agent de recherche autonome (hors sécurité)

## 11 — Assistants terminal / shell
- [ ] **Warp** (Agent Mode) — terminal moderne avec agent
- [ ] **Amazon Q Developer CLI** — assistant shell/dev AWS
- [ ] **Gemini CLI** (Google) — aussi assistant terminal
- [ ] **ShellGPT** — assistant shell open-source
- [ ] **Aichat** — assistant shell open-source (Rust)
- [ ] **Butterfish** — assistant shell
- [ ] **tgpt** — client LLM terminal léger

---

## CI/CD, livraison & ops (IA) — produire du code, famille CI/CD & ops (créée le 2026-06-18)
*Famille créée pour combler la phase 7 du SDLC. Déjà ajoutés & vérifiés : Mergify, Cleric, Resolve.ai, Traversal. Candidats restants à arbitrer :*
- [ ] **Datadog Bits AI Dev Agent** — fix autonome de tests flaky → draft PR (add-on Datadog) ; le plus « agent » côté CI
- [ ] **Aviator** — merge queue IA + gestion des flaky
- [ ] **Trunk** — détection/quarantaine de tests flaky (Trunk Flaky Tests)
- [ ] **Rootly** — gestion d'incidents + AI SRE (SOC2 de longue date)
- [ ] **PagerDuty AIOps** / **Datadog Bits AI** — AIOps incumbents (corrélation/incident)
- [ ] **Pulumi AI** — IaC assisté par IA (déploiement infra)

---

## Pistes de NOUVELLES familles (élargissement hors dev pur)
- [x] **12. Évaluation / observabilité LLM** — Langfuse, LangSmith, Braintrust, Helicone, Arize Phoenix ✅ *ajoutée dans [IA dans un produit](ia-dans-un-produit.md), famille 8 (LLMOps)*
- [x] **13. Passerelles / routeurs LLM** — **OpenRouter**, **LiteLLM**, **Portkey**, **Requesty** ✅ *ajoutée dans [IA dans un produit](ia-dans-un-produit.md), famille 9 (vérifié le 2026-06-16)*
- [ ] **14. Agents vocaux** — (à définir si pertinent)
- [ ] **15. Génération images / vidéo** — (probablement hors périmètre)

---

### Recommandations (mon avis)
1. **Routeurs LLM** (OpenRouter, LiteLLM) — pile dans ta thématique coût.
2. **Gros agents/IDE manquants** (Cursor, Windsurf, Cline, Aider) — briques que la plupart des autres outils orchestrent.
3. **Context7** — déjà présent dans ta session, naturel pour la famille 8.
