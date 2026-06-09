---
titre: "Architectures verticale / horizontale / hybride"
theme: fondamentaux-agents
niveau: 🟡
provenance: ✅
base: ibm-guide-agents-ia
source_url: https://www.ibm.com/fr-fr/think/topics/agentic-architecture
source_titre: "Qu’est-ce qu’une architecture agentique ?"
source_primaire: "arXiv:2404.11584"
---

# Architectures verticale / horizontale / hybride

> Fiche du glossaire des patterns · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [22-agentic-architecture](../sources/ibm-guide-agents-ia/md/22-agentic-architecture.md), [03-agentic-ai](../sources/ibm-guide-agents-ia/md/03-agentic-ai.md)

**En une phrase** — les trois topologies d'un système multi-agents : chef centralisé, pairs égaux, ou mélange des deux selon la phase.

## Ce que dit le corpus
IBM compare trois types d'architectures multi-agents. **Verticale** : un agent leader supervise les sous-tâches et décisions, les agents lui rendent compte (contrôle centralisé, hiérarchie, communication centralisée). Forces : efficacité sur les workflows séquentiels, responsabilité claire. Faiblesses : goulets d'étranglement et **point de défaillance unique** lié au leader. Cas d'usage : automatisation de workflow à approbations multiples, génération de documents. **Horizontale** : modèle de collaboration entre pairs, agents égaux dans un système décentralisé, décisions pilotées par le groupe. Forces : résolution dynamique, traitement parallèle. Faiblesses : problèmes de coordination, **décisions plus lentes (trop de délibération)**. Cas d'usage : brainstorming, problèmes interdisciplinaires. **Hybride** : combine leadership structuré et flexibilité collaborative, leadership dynamique qui s'adapte à la phase de la tâche. Force : polyvalence ; faiblesse : complexité de gestion des rôles.

## Tradeoff / insight pour un senior
Le vrai arbitrage est centralisation vs robustesse : la verticale donne contrôle et débogabilité au prix d'un SPOF ; l'horizontale élimine le SPOF mais paie en latence de consensus. L'hybride est la réponse pragmatique (leader qui passe la main), au prix d'une orchestration plus lourde. Mêmes tradeoffs que microservices orchestrés vs chorégraphiés.

## Source primaire
Citée par IBM (note 3/5/6 du fichier 22) : T. Masterman, S. Besen, M. Sawtell, A. Chao, « The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey », arXiv:2404.11584, avril 2024.

## Voir aussi
- [Réseaux centralisés vs décentralisés](reseaux-centralises-decentralises.md)
- [Structures multi-agents : hiérarchique / holonique / coalition / équipe](structures-multi-agents.md)
