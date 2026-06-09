---
titre: "Réseaux centralisés vs décentralisés"
theme: multi-agents
niveau: 🟡
provenance: ✅
base: ibm-guide-agents-ia
source_url: https://www.ibm.com/fr-fr/think/topics/multiagent-system
source_titre: "Qu’est-ce qu’un système multi-agent ?"
---

# Réseaux centralisés vs décentralisés

> Fiche du glossaire des patterns · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [25-multiagent-system](../sources/ibm-guide-agents-ia/md/25-multiagent-system.md), [23-ai-agent-orchestration](../sources/ibm-guide-agents-ia/md/23-ai-agent-orchestration.md), [13-ai-agent-communication](../sources/ibm-guide-agents-ia/md/13-ai-agent-communication.md)

**En une phrase** — soit une unité centrale détient le savoir global et relie tous les agents, soit chacun ne parle qu'à ses voisins.

## Ce que dit le corpus
Pour IBM, dans les **réseaux centralisés** une unité centrale contient la base de connaissances globale, relie les agents et supervise leurs informations. Force : facilité de communication et uniformité des connaissances. Faiblesse : dépendance à l'unité centrale — si elle est défaillante, c'est tout le système qui l'est. Dans les **réseaux décentralisés**, les agents partagent l'information avec leurs voisins plutôt qu'avec une base globale ; avantages : robustesse et modularité, la défaillance d'un seul agent n'entraîne pas celle du système. Défi : coordonner le comportement pour qu'il bénéficie aux autres agents coopérants. Le fichier 23 reprend cette dualité au niveau de l'orchestration (centralisée avec agent « cerveau » vs décentralisée par consensus), et le fichier 13 au niveau communication (contrôle centralisé d'une IA qui distribue les données vs communication décentralisée entre pairs).

## Tradeoff / insight pour un senior
Le compromis classique des systèmes distribués : cohérence forte et contrôle simple (centralisé) contre tolérance aux pannes et passage à l'échelle (décentralisé), au prix de la difficulté de coordination et de comportements potentiellement imprévisibles. C'est l'opposition orchestrateur unique vs pair-à-pair, déclinée sur trois plans (connaissance, orchestration, communication).

## Source primaire
Non citée par IBM — notion générale de l'IA distribuée. Le fichier 13 cite par ailleurs les protocoles KQML (DARPA, années 1990) et FIPA-ACL pour la communication d'agent à agent.

## Voir aussi
- [Architectures verticale / horizontale / hybride](archi-vertical-horizontal-hybride.md)
- [Structures multi-agents : hiérarchique / holonique / coalition / équipe](structures-multi-agents.md)
