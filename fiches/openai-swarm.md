---
titre: "OpenAI Swarm"
theme: frameworks-outillage
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/multi-agent-collaboration
source_titre: "Qu’est-ce que la collaboration multi-agent ?"---

# OpenAI Swarm

> Fiche du glossaire des patterns · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [27-multi-agent-collaboration](../sources/ibm-guide-agents-ia/md/27-multi-agent-collaboration.md)

**En une phrase** — un cadre OpenAI où chaque agent est une unité spécialisée et où l'on passe la main d'un agent à l'autre (handoff) au fil de la conversation.

## Ce que dit le corpus
IBM présente le cadre Swarm d'OpenAI comme « une nouvelle manière de coordonner plusieurs agents autour de routines et de transmissions de tâches ». Au lieu d'agir indépendamment, chaque agent est vu comme une unité spécialisée dotée d'outils personnalisés et de consignes spécifiques. Le transfert d'une tâche ou d'une conversation d'un agent à un autre permet une expérience utilisateur fluide, chaque agent étant spécialisé dans un rôle précis. Cette approche améliore l'efficacité, la modularité et la réactivité du système dans son ensemble. Le corpus souligne que le terme « Swarm » met l'accent sur une coordination légère et une exécution efficace des tâches, ce qui permet de déployer le système à plus grande échelle dans des situations concrètes.

## Tradeoff / insight pour un senior
Pur vocabulaire : « routines » = consignes + outils par agent, « handoff » = passation explicite du contrôle conversationnel. Le pattern est un routeur d'agents à coordination minimale — utile à connaître comme nom, mais l'idée (router vers le bon spécialiste) est déjà familière.

## Source primaire
Non citée par IBM — voir le dépôt expérimental OpenAI Swarm (hors-corpus).

## Voir aussi
- [orchestration-types](orchestration-types.md)
- [langchain](langchain.md)
