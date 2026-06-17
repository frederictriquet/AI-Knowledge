---
outil: "LangGraph"
type: "Bibliothèque Python + JS/TS (graphes d'agents stateful) + plateforme de déploiement"
url: https://www.langchain.com/langgraph
modele_economique: "Open-source (MIT) + plateforme managée payante (LangSmith Deployment)"
cout_llm: "🔑 BYOK — orchestre, ne facture pas les tokens"
---

# LangGraph

**En une phrase** — Framework d'orchestration **bas niveau** (LangChain Inc.) pour agents *stateful* : graphes avec cycles, persistance/checkpoints, human-in-the-loop et exécution durable — le contrôle fin du flux là où les frameworks haut niveau abstraient.

> 📄 Concept détaillé : [fiche notion LangGraph](../fiches/langgraph.md). Cette fiche-ci couvre l'angle produit (licence, prix, coût LLM).

## Type & intégration
Bibliothèque open-source **Python** (`langgraph`) **et JS/TS** (`@langchain/langgraph`). S'utilise **sans LangChain** (mais les agents LangChain v1 reposent dessus). `StateGraph` (nœuds = logique, arêtes = routage, arêtes conditionnelles, cycles), checkpointers (mémoire court terme, reprise après panne, time-travel), stores (mémoire long terme), streaming. + plateforme managée **LangGraph Platform**, renommée **LangSmith Deployment** (oct. 2025), pour déployer/exécuter les agents.

## Modèle économique
- **Lib : open-source MIT**, gratuite, utilisable seule.
- **Plateforme managée** (facturée via les plans LangSmith) : **Developer** 0 $/siège (1 siège, 5k traces/mois) → **Plus** 39 $/siège/mois (10k traces) → **Enterprise** sur devis (seul pour hybride/self-hosted complet VPC). À l'usage : runs 0,005 $/run, uptime prod 0,0036 $/min, traces 2,50 $/1k. Agent Server auto-hébergeable (Docker/K8s + Postgres + Redis), option self-host basique gratuite (plan Developer).

## Coût LLM
**🔑 BYOK**, provider-agnostic (~25 providers via `init_chat_model` : OpenAI, Anthropic, Google, Bedrock, Mistral, Groq, Ollama…). Les appels vont directement à l'API du provider qui facture ta clé — LangGraph **ne revend pas de tokens** (impliqué par l'architecture, non formulé verbatim).

## À quoi ça sert
Le choix quand on a besoin de **contrôle fin** : cycles (essentiels aux architectures agentiques, vs DAG), état explicite, persistance et reprise, validation humaine à mi-parcours. Première sortie janv. 2024 ; adoption affichée Klarna, Replit, Elastic.

## Notes / à creuser
- Vs **LangChain** (même éditeur) : LangGraph = runtime d'orchestration bas niveau ; LangChain = abstractions haut niveau qui s'appuient dessus. Complémentaires.
- Vs [CrewAI](crewai.md) (rôles/« employés »), [AutoGen/AG2](autogen-ag2.md) (conversationnel) : positionnement « graphe/bas niveau contrôlable » (contraste surtout documenté par des tiers).
- Prix Enterprise non publié.

## Source
https://www.langchain.com/langgraph · https://www.langchain.com/pricing · LICENSE MIT (github.com/langchain-ai/langgraph) · docs.langchain.com (models/persistence/streaming). *(vérifié le 2026-06-16)*
