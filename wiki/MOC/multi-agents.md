---
type: index
titre: "MOC — Multi-agents"
theme: multi-agents
---

# 👥 Multi-agents

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Orchestrer et structurer plusieurs agents._

## Concepts (9)

### 🔴 Substance / cœur
- **[DroidSpeak](../fiches/droidspeak.md)** — au lieu de faire dialoguer deux LLM en texte, on partage directement le cache KV entre eux pour accélérer la communication inter-agents, avec une perte de précision annoncée comme minimale.
- **[MacNet : passage à l'échelle multi-agents](../fiches/macnet.md)** — l'extension de ChatDev qui structure plus de mille agents en graphe acyclique (DAG) et les fait raisonner dans l'ordre topologique, avec une loi de croissance de la qualité en fonction du nombre d'agents.
- **[MetaGPT : communication structurée + feedback exécutable](../fiches/metagpt-pattern.md)** — un cadre multi-agents qui simule une société de logiciels et où les agents s'échangent des documents schématisés (PRD, diagrammes) plutôt que du dialogue libre, l'ingénieur bouclant sur ses propres tests.
- **[Mixture-of-Agents (MoA)](../fiches/mixture-of-agents.md)** — empiler **plusieurs LLM en couches** : chaque couche d'agents reçoit et agrège les réponses de la couche précédente, améliorant la qualité au-delà du meilleur modèle isolé.
- **[Multi-agent debate / Society of Mind](../fiches/society-of-mind-debate.md)** — faire **débattre plusieurs instances de LLM** : chacune propose une réponse, critique celles des autres sur plusieurs tours, jusqu'à converger vers une réponse plus factuelle.

### 🟡 Tradeoff / intermédiaire
- **[Réseaux centralisés vs décentralisés](../fiches/reseaux-centralises-decentralises.md)** — soit une unité centrale détient le savoir global et relie tous les agents, soit chacun ne parle qu'à ses voisins.
- **[Stratégies de collaboration : règles / rôles / modèles](../fiches/strategies-collaboration.md)** — trois manières de faire coopérer des agents : scripté, par répartition de rôles, ou par raisonnement probabiliste sous incertitude.
- **[Structures multi-agents : hiérarchique / holonique / coalition / équipe](../fiches/structures-multi-agents.md)** — quatre façons d'organiser les agents : arbre de commandement, tout-et-partie, alliance temporaire, ou équipe interdépendante.
- **[Types d'orchestration des agents IA](../fiches/orchestration-types.md)** — quatre façons de répartir la prise de décision entre agents : un chef unique, un collectif sans chef, des couches hiérarchiques, ou des organisations qui collaborent sans se partager les données.

## Outils (18)

- **[AutoGen / AG2](../fiches%20outils/autogen-ag2.md)** — _Framework Python multi-agents conversationnels (deux lignées + un successeur)_
- **[Conductor](../fiches%20outils/conductor.md)** — _Application desktop Mac (orchestrateur d'agents de codage)_
- **[CrewAI](../fiches%20outils/crewai.md)** — _Framework (bibliothèque Python) + plateforme cloud_
- **[Crystal](../fiches%20outils/crystal.md)** — _Application desktop (Electron) — orchestrateur d'agents_
- **[LangGraph](../fiches%20outils/langgraph.md)** — _Bibliothèque Python + JS/TS (graphes d'agents stateful) + plateforme de déploiement_
- **[Liza](../fiches%20outils/liza.md)** — _CLI (Go) — système multi-agents de codage_
- **[MindFlight Orchestrator (MFO)](../fiches%20outils/mindflight-orchestrator.md)** — _Plateforme (orchestration d'agents IA / automatisation d'entreprise)_
- **[Multica](../fiches%20outils/multica.md)** — _Plateforme « managed agents » (orchestration d'agents de codage)_
- **[OpenAI Agents SDK](../fiches%20outils/openai-agents-sdk.md)** — _SDK Python + TypeScript (agents légers)_
- **[Orca](../fiches%20outils/orca.md)** — _Application desktop (Mac/Win/Linux) + mobile — Agent Development Environment (ADE)_
- **[Paperclip](../fiches%20outils/paperclip.md)** — _Plateforme open-source d'orchestration et de gouvernance d'agents IA (« zero-human companies »)_
- **[Pheromind](../fiches%20outils/pheromind.md)** — _Framework d'orchestration multi-agents (swarm)_
- **[Ruflo](../fiches%20outils/ruflo.md)** — _Meta-harnais / framework d'orchestration multi-agents pour Claude (open source, npm)_
- **[Sculptor](../fiches%20outils/sculptor.md)** — _Application desktop Mac — orchestrateur d'agents_
- **[Sim (Sim Studio)](../fiches%20outils/sim.md)** — _Builder visuel de workflows d'agents — open-source + Cloud_
- **[Supacode](../fiches%20outils/supacode.md)** — _Application desktop macOS native (orchestrateur d'agents de codage)_
- **[Superset (superset-sh)](../fiches%20outils/superset.md)** — _Application desktop (orchestrateur d'agents de codage)_
- **[Vibe Kanban](../fiches%20outils/vibe-kanban.md)** — _Plateforme kanban / orchestration d'agents de codage (web)_
