---
titre: "AgentOps"
theme: gouvernance-alignement-ops
niveau: 🔴
provenance: ✅
base: ibm-guide-agents-ia
source_url: https://www.ibm.com/fr-fr/think/topics/agentops
source_titre: "Qu’est-ce que l’AgentOps ?"
---

# AgentOps

> Fiche du glossaire des patterns · Pertinence 🔴 substance · Provenance ✅ présent · Sources corpus : [07-agentops](../sources/ibm-guide-agents-ia/md/07-agentops.md)

**En une phrase** — le DevOps/MLOps des agents : instrumenter l'exécution en session → trace → étendue (span) pour rendre observable une boîte noire non déterministe, avec coût et latence par étape et routage multi-LLM.

## Ce que dit le corpus
Le fichier 07 définit l'AgentOps (« Agent Opérations ») comme « un ensemble de pratiques émergentes axées sur la gestion du cycle de vie des agents IA autonomes », réunissant « les principes de disciplines opérationnelles telles que le DevOps et le MLOps ». Objectif : « apporter observabilité et fiabilité » et « examiner la boîte noire des interactions ». La surveillance se fait « au niveau de la session, de la trace ou de l'étendue » ; les développeurs peuvent « revoir étape par étape l'exécution des agents », examiner « les schémas d'utilisation des outils », « quelles API ont été utilisées », « la latence lors de chaque étape » et « le coût final du LLM ». Le corpus cite l'idée (Adam Silverman, Agency AI) qu'« en utilisant différents LLM pour différentes tâches, ce coût pouvait être réduit ». L'écosystème est cité (Agenta, LangSmith, Trulens — « 17 outils sur Github »). IBM Research a bâti sa solution « en s'appuyant sur les normes OpenTelemetry (OTEL), un SDK open source », avec une plateforme analytique ouverte et extensible, et des analyses elles-mêmes alimentées par l'IA (« visualiser les workflows multi-traces et explorer les trajectoires »).

## Tradeoff / insight pour un senior
La pépite : c'est de l'observabilité distribuée classique (session/trace/span d'OTEL) appliquée à des systèmes non déterministes. Le fondement OTEL est le bon choix d'ingénierie — instrumentation automatique multi-framework, pas de vendor lock-in, métriques extensibles. Le coût et la latence *par étape* permettent l'arbitrage concret « routage multi-LLM » (modèle cher pour les tâches dures, modèle bon marché ailleurs).

## Source primaire
Non citée formellement pour le concept ; le corpus renvoie au billet IBM Research (research.ibm.com/blog/ibm-agentops-ai-agents-observability) annoncé à IBM Think. Standard sous-jacent : OpenTelemetry (OTEL).

## Voir aussi
- [evaluation-trajectoire](evaluation-trajectoire.md)
