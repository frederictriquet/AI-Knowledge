# Résumé des Concepts de l'IA Agentique

Ce document présente une synthèse des concepts clés identifiés dans la documentation, en privilégiant la concision et la clarté technique.

## Tableau des Concepts

| Concept | Description | Référence |
| :--- | :--- | :--- |
| **Agent IA** | Système autonome utilisant un LLM pour planifier et exécuter des tâches via des outils. | [01-ai-agents.md](./md/01-ai-agents.md) |
| **IA Agentique** | Cadre technologique où l'IA agit de manière autonome, s'adapte et prend des décisions. | [03-agentic-ai.md](./md/03-agentic-ai.md) |
| **Workflow Agentique** | Processus itératif où l'IA décompose une tâche, l'exécute et s'auto-corrige. | [11-agentic-workflows.md](./md/11-agentic-workflows.md) |
| **Raisonnement Agentique** | Capacité d'un agent à appliquer une logique (conditionnelle, heuristique) pour décider des actions. | [18-agentic-reasoning.md](./md/18-agentic-reasoning.md) |
| **ReAct** | Paradigme de raisonnement combinant "Pensée" (Chain-of-Thought) et "Action" (appel d'outil) en boucle. | [28-react-agent.md](./md/28-react-agent.md) |
| **ReWOO** | "Reasoning Without Observation" : planification complète en amont pour réduire la consommation de tokens. | [30-rewoo.md](./md/30-rewoo.md) |
| **LATS** | "Language Agent Tree Search" : utilisation d'arbres de recherche (type Monte Carlo) pour la décision. | [18-agentic-reasoning.md](./md/18-agentic-reasoning.md) |
| **RAG Agentique** | Utilisation d'agents pour router les requêtes, planifier la recherche et valider les sources externes. | [64-agentic-rag.md](./md/64-agentic-rag.md) |
| **cRAG (Corrective RAG)** | RAG qui évalue la pertinence des documents récupérés et effectue des actions correctives (ex: recherche web). | [68-build-corrective-rag-agent-granite-tavily.md](./md/68-build-corrective-rag-agent-granite-tavily.md) |
| **Chunking Agentique** | Découpage dynamique et sémantique de documents en "chunks" optimisés par un agent IA. | [66-agentic-chunking.md](./md/66-agentic-chunking.md) |
| **Tool Calling** | Capacité d'un LLM à générer des appels structurés (API, fonctions) pour interagir avec le monde. | [19-tool-calling.md](./md/19-tool-calling.md) |
| **Système Multi-Agents (MAS)** | Collaboration de plusieurs agents spécialisés (hiérarchique ou horizontal) pour résoudre un problème. | [25-multiagent-system.md](./md/25-multiagent-system.md) |
| **AgentOps** | Pratiques de surveillance, débogage et gestion du cycle de vie des agents (similaire au DevOps). | [07-agentops.md](./md/07-agentops.md) |
| **ACP** | "Agent Communication Protocol" : norme ouverte d'IBM pour l'interopérabilité entre agents. | [33-agent-communication-protocol.md](./md/33-agent-communication-protocol.md) |
| **A2A** | "Agent2Agent" : protocole de messagerie universel (Google/Linux Foundation) pour la collaboration inter-agents. | [35-agent2agent-protocol.md](./md/35-agent2agent-protocol.md) |
| **MCP** | "Model Context Protocol" : standard d'Anthropic pour connecter les LLM aux outils et données. | [37-model-context-protocol.md](./md/37-model-context-protocol.md) |
| **HITL** | "Human In The Loop" : intégration d'une validation ou d'un retour humain dans le cycle de l'agent. | [63-human-in-the-loop-ai-agent-langraph-watsonx-ai.md](./md/63-human-in-the-loop-ai-agent-langraph-watsonx-ai.md) |
| **Mémoire d'agent** | Stockage du contexte à court terme (session) et à long terme (connaissances apprises). | [15-ai-agent-memory.md](./md/15-ai-agent-memory.md) |
| **Planification (Planning)** | Décomposition d'objectifs complexes en sous-tâches exécutables. | [17-ai-agent-planning.md](./md/17-ai-agent-planning.md) |
| **Perception** | Collecte et interprétation des données de l'environnement (API, capteurs, documents). | [16-ai-agent-perception.md](./md/16-ai-agent-perception.md) |
| **Automatisation Agentique** | Évolution de la RPA vers une automatisation capable de s'adapter et de raisonner sur des données non structurées. | [70-agentic-automation.md](./md/70-agentic-automation.md) |

## Frameworks et Outils Notables

- **LangChain / LangGraph** : Frameworks de référence pour construire des chaînes et des graphes d'agents cycliques.
- **AutoGen (Microsoft)** : Framework spécialisé dans les conversations multi-agents et la délégation de tâches.
- **CrewAI** : Orchestrateur focalisé sur le rôle des agents et le travail d'équipe ("crews").
- **BeeAI (IBM)** : Écosystème open-source pour l'orchestration et le déploiement d'agents via ACP.
- **ChatDev / MetaGPT** : Frameworks simulant des structures organisationnelles (ex: entreprise de logiciel) avec des agents.

---
*Document généré par Gemini CLI.*
