---
titre: "OpenAI Swarm"
type: "Concept"
theme: frameworks-outillage
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/multi-agent-collaboration
source_titre: "Qu’est-ce que la collaboration multi-agent ?"
---

# OpenAI Swarm

**En une phrase** — un cadre OpenAI où chaque agent est une unité spécialisée et où l'on passe la main d'un agent à l'autre (handoff) au fil de la conversation.

## En détail
Le cadre Swarm d'OpenAI propose « une nouvelle manière de coordonner plusieurs agents autour de routines et de transmissions de tâches ». Au lieu d'agir indépendamment, chaque agent est une unité spécialisée dotée d'outils personnalisés et de consignes spécifiques. Le transfert d'une tâche ou d'une conversation d'un agent à un autre permet une expérience utilisateur fluide, chaque agent étant spécialisé dans un rôle précis. Cette approche améliore l'efficacité, la modularité et la réactivité du système dans son ensemble. Le terme « Swarm » met l'accent sur une coordination légère et une exécution efficace des tâches, ce qui permet de déployer le système à plus grande échelle dans des situations concrètes.

## Exemple
Triage de service client : un agent d'accueil tient la conversation, classe la demande, puis exécute un handoff vers l'agent de facturation ou l'agent de dépannage technique selon le besoin — chacun ayant ses propres outils (consultation de compte, base de pannes) et ses consignes. L'utilisateur ne perçoit qu'un fil continu, alors que le contrôle conversationnel a changé de spécialiste. La source range ce pattern aux côtés de l'analyse financière et de la surveillance de conformité, où la coordination « légère » de Swarm permet de monter en échelle sans orchestrateur lourd.

## Tradeoff / insight pour un senior
Pur vocabulaire : « routines » = consignes + outils par agent, « handoff » = passation explicite du contrôle conversationnel. Le pattern est un routeur d'agents à coordination minimale — utile à connaître comme nom, mais l'idée (router vers le bon spécialiste) est déjà familière.

## Source primaire
Voir le dépôt expérimental OpenAI Swarm.

## Voir aussi
- [orchestration-types](orchestration-types.md)
- [langchain](langchain.md)
