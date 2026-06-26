---
type: index
titre: "Thème — Frameworks & outillage"
theme: frameworks-outillage
---

# 🛠️ Frameworks & outillage

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Frameworks et bibliothèques pour construire des agents._

## Concepts (11)

### 🟡 Tradeoff / intermédiaire
- **[Comportements d'essaim (flocking / swarming)](../fiches/flocking-swarming.md)** — coordonner une foule d'agents par quelques règles locales bio-inspirées, sans contrôleur central.
- **[RAISE](../fiches/raise.md)** — une variante de ReAct enrichie d'un composant de mémoire pour conserver le contexte entre les étapes.

### 🟢 Survol / introductif
- **[AutoGen & AG2](../fiches/autogen-ag2.md)** — le cadre multi-agents de Microsoft pour des conversations asynchrones entre agents (AssistantAgent qui « pense », UserProxyAgent qui exécute), prolongé par un fork communautaire, AG2.
- **[BeeAI](../fiches/beeai.md)** — une couche d'orchestration framework-agnostique d'IBM, fondée sur le protocole ACP, qui découvre, exécute et partage des agents quels que soient leurs cadres, en isolant chaque agent dans son conteneur.
- **[CrewAI](../fiches/crewai.md)** — un cadre multi-agents bâti sur LangChain qui organise des agents en « équipe » via rôles, tâches et processus (séquentiel ou hiérarchique à manager auto-généré).
- **[LangChain](../fiches/langchain.md)** — un cadre d'orchestration open source qui fournit des abstractions modulaires (chaînes, index, mémoire, outils, agents) pour bâtir des applications pilotées par LLM, branchables sur quasi n'importe quel modèle.
- **[LangFlow](../fiches/langflow.md)** — une GUI low/no-code en glisser-déposer pour assembler agents, LLM et systèmes RAG en connectant des composants modulaires, avec des flux exportables en JSON.
- **[LangGraph](../fiches/langgraph.md)** — le cadre d'orchestration de LangChain qui modélise un workflow d'agents comme un graphe d'états (nœuds, arêtes, cycles) avec gestion explicite de l'état et human-in-the-loop.
- **[LlamaIndex](../fiches/llamaindex.md)** — un cadre d'orchestration d'agents dont l'unité de base est le *workflow* événementiel : des étapes déclenchées par des événements et reliées par un contexte partagé, sans chemins prédéfinis entre elles.
- **[OpenAI Swarm](../fiches/openai-swarm.md)** — un cadre OpenAI où chaque agent est une unité spécialisée et où l'on passe la main d'un agent à l'autre (handoff) au fil de la conversation.
- **[Semantic Kernel](../fiches/semantic-kernel.md)** — le SDK d'agents de Microsoft, avec deux types d'agents intégrés (chat-completion et assistant) et un Process Framework pour orchestrer des workflows par étapes.

## Outils (32)

- **[AutoGen / AG2](../fiches%20outils/autogen-ag2.md)** — _Framework Python multi-agents conversationnels (deux lignées + un successeur)_
- **[BMAD-METHOD](../fiches%20outils/bmad-method.md)** — _Framework / méthodologie (agents IA pour IDE)_
- **[Cavekit](../fiches%20outils/cavekit.md)** — _Plugin (Claude Code) + skills_
- **[Conductor](../fiches%20outils/conductor.md)** — _Application desktop Mac (orchestrateur d'agents de codage)_
- **[Continue](../fiches%20outils/continue.md)** — _Extension IDE (VS Code / JetBrains) + CLI_
- **[CrewAI](../fiches%20outils/crewai.md)** — _Framework (bibliothèque Python) + plateforme cloud_
- **[Crystal](../fiches%20outils/crystal.md)** — _Application desktop (Electron) — orchestrateur d'agents_
- **[deepagents (Deep Agents)](../fiches%20outils/deepagents.md)** — _Bibliothèque Python (+ JS/TS) — harness d'agents_
- **[ECC](../fiches%20outils/ecc.md)** — _Système de harness d'agent (skills/agents/hooks/rules) — multi-plateforme, OSS + GitHub App_
- **[Flowise](../fiches%20outils/flowise.md)** — _Builder visuel d'apps/agents LLM (low-code) — open-source + Cloud_
- **[GitHub Spec Kit](../fiches%20outils/spec-kit.md)** — _Toolkit CLI (spec-driven development)_
- **[gstack](../fiches%20outils/gstack.md)** — _Suite de skills / workflow open-source pour agents de codage IA (Claude Code et compatibles)_
- **[Gumloop](../fiches%20outils/gumloop.md)** — _Builder no-code d'automatisations IA (SaaS)_
- **[Kilo Code](../fiches%20outils/kilo-code.md)** — _Extension IDE / CLI_
- **[LangGraph](../fiches%20outils/langgraph.md)** — _Bibliothèque Python + JS/TS (graphes d'agents stateful) + plateforme de déploiement_
- **[LlamaIndex](../fiches%20outils/llamaindex.md)** — _Framework Python + TS (data/RAG + agents) + plateforme managée LlamaCloud/LlamaParse_
- **[Mastra](../fiches%20outils/mastra.md)** — _Framework d'agents TypeScript/JS + Mastra Cloud (déploiement)_
- **[Multica](../fiches%20outils/multica.md)** — _Plateforme « managed agents » (orchestration d'agents de codage)_
- **[Neo-AI](../fiches%20outils/neo-ai.md)** — _CLI — assistant IA pour terminal Linux_
- **[OpenAI Agents SDK](../fiches%20outils/openai-agents-sdk.md)** — _SDK Python + TypeScript (agents légers)_
- **[Orca](../fiches%20outils/orca.md)** — _Application desktop (Mac/Win/Linux) + mobile — Agent Development Environment (ADE)_
- **[Pydantic AI](../fiches%20outils/pydantic-ai.md)** — _Framework d'agents Python type-safe_
- **[Relay.app](../fiches%20outils/relay-app.md)** — _Automatisation de workflows avec IA + human-in-the-loop (SaaS)_
- **[Sculptor](../fiches%20outils/sculptor.md)** — _Application desktop Mac — orchestrateur d'agents_
- **[Serena](../fiches%20outils/serena.md)** — _Serveur MCP / toolkit d'agent de codage_
- **[Sim (Sim Studio)](../fiches%20outils/sim.md)** — _Builder visuel de workflows d'agents — open-source + Cloud_
- **[Supacode](../fiches%20outils/supacode.md)** — _Application desktop macOS native (orchestrateur d'agents de codage)_
- **[Superpowers](../fiches%20outils/superpowers.md)** — _Plugin / framework de skills agentiques (multi-plateforme)_
- **[Superset (superset-sh)](../fiches%20outils/superset.md)** — _Application desktop (orchestrateur d'agents de codage)_
- **[Task Master (Taskmaster)](../fiches%20outils/task-master.md)** — _CLI + Serveur MCP (gestion de tâches pour agents)_
- **[Trae](../fiches%20outils/trae.md)** — _Application (IDE)_
- **[Vibe Kanban](../fiches%20outils/vibe-kanban.md)** — _Plateforme kanban / orchestration d'agents de codage (web)_
