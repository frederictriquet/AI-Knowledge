---
titre: "AgentOps"
type: "Concept"
theme: gouvernance-alignement-ops
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/topics/agentops
source_titre: "Qu’est-ce que l’AgentOps ?"
---

# AgentOps

**En une phrase** — le DevOps/MLOps des agents : instrumenter l'exécution en session → trace → étendue (span) pour rendre observable une boîte noire non déterministe, avec coût et latence par étape et routage multi-LLM.

## En détail
L'AgentOps (« Agent Opérations ») désigne « un ensemble de pratiques émergentes axées sur la gestion du cycle de vie des agents IA autonomes », réunissant « les principes de disciplines opérationnelles telles que le DevOps et le MLOps ». Objectif : « apporter observabilité et fiabilité » et « examiner la boîte noire des interactions ». La surveillance se fait « au niveau de la session, de la trace ou de l'étendue » ; les développeurs peuvent « revoir étape par étape l'exécution des agents », examiner « les schémas d'utilisation des outils », « quelles API ont été utilisées », « la latence lors de chaque étape » et « le coût final du LLM ». L'idée (Adam Silverman, Agency AI) qu'« en utilisant différents LLM pour différentes tâches, ce coût pouvait être réduit » est également avancée. L'écosystème compte de nombreux outils (Agenta, LangSmith, Trulens). IBM Research a bâti sa solution « en s'appuyant sur les normes OpenTelemetry (OTEL), un SDK open source », avec une plateforme analytique ouverte et extensible, et des analyses elles-mêmes alimentées par l'IA (« visualiser les workflows multi-traces et explorer les trajectoires »).

## Exemple
Cas IBM : un agent de support client composé de plusieurs LLM qui surveille les e-mails entrants, fouille la base de connaissances d'entreprise et crée des tickets en autonomie. Le débogage devient « répondre à des questions » sur la trace : l'agent a-t-il consulté la bonne doc support ? Quelles API a-t-il appelées, dans quel ordre ? Quelle latence à chaque étape, quel coût LLM final ? L'analogie de la source : laisser un agent sans relire ses traces, « c'est donner une carte bancaire à un adolescent sans consulter le relevé ». L'étude citée recense 17 outils sur GitHub pour outiller cette pratique.

## Tradeoff / insight pour un senior
La pépite : c'est de l'observabilité distribuée classique (session/trace/span d'OTEL) appliquée à des systèmes non déterministes. Le fondement OTEL est le bon choix d'ingénierie — instrumentation automatique multi-framework, pas de vendor lock-in, métriques extensibles. Le coût et la latence *par étape* permettent l'arbitrage concret « routage multi-LLM » (modèle cher pour les tâches dures, modèle bon marché ailleurs).

## Source primaire
Billet IBM Research (research.ibm.com/blog/ibm-agentops-ai-agents-observability). Standard sous-jacent : OpenTelemetry (OTEL).

## Voir aussi
- [evaluation-trajectoire](evaluation-trajectoire.md)
