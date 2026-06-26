---
titre: "Réseaux centralisés vs décentralisés"
type: "Concept"
theme: multi-agents
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/multiagent-system
source_titre: "Qu’est-ce qu’un système multi-agent ?"
---

# Réseaux centralisés vs décentralisés

**En une phrase** — soit une unité centrale détient le savoir global et relie tous les agents, soit chacun ne parle qu'à ses voisins.

## En détail
Dans les **réseaux centralisés** une unité centrale contient la base de connaissances globale, relie les agents et supervise leurs informations. Force : facilité de communication et uniformité des connaissances. Faiblesse : dépendance à l'unité centrale — si elle est défaillante, c'est tout le système qui l'est. Dans les **réseaux décentralisés**, les agents partagent l'information avec leurs voisins plutôt qu'avec une base globale ; avantages : robustesse et modularité, la défaillance d'un seul agent n'entraîne pas celle du système. Défi : coordonner le comportement pour qu'il bénéficie aux autres agents coopérants. Cette dualité se retrouve au niveau de l'orchestration (centralisée avec agent « cerveau » vs décentralisée par consensus) et au niveau communication (contrôle centralisé d'une IA qui distribue les données vs communication décentralisée entre pairs).

## Exemple
Système de défense maritime : des agents organisés en réseau décentralisé surveillent chacun une zone distincte du réseau pour repérer des menaces entrantes (attaques DDoS, intrusions), et coopèrent en équipe pour identifier les interactions entre bateaux hostiles en approche et navires de défense — la perte d'un capteur n'effondre pas la surveillance globale. À l'inverse, un réseau centralisé conviendrait à une base de connaissances médicale unifiée partagée entre agents de diagnostic, au prix d'une dépendance totale à l'unité centrale.

## Tradeoff / insight pour un senior
Le compromis classique des systèmes distribués : cohérence forte et contrôle simple (centralisé) contre tolérance aux pannes et passage à l'échelle (décentralisé), au prix de la difficulté de coordination et de comportements potentiellement imprévisibles. C'est l'opposition orchestrateur unique vs pair-à-pair, déclinée sur trois plans (connaissance, orchestration, communication).

## Source primaire
Notion générale de l'IA distribuée. Les protocoles KQML (DARPA, années 1990) et FIPA-ACL pour la communication d'agent à agent sont cités par ailleurs.

## Voir aussi
- [Architectures verticale / horizontale / hybride](archi-vertical-horizontal-hybride.md)
- [Structures multi-agents : hiérarchique / holonique / coalition / équipe](structures-multi-agents.md)
