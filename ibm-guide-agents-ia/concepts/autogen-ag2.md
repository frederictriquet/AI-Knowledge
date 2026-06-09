# AutoGen & AG2

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [40-autogen](../md/40-autogen.md)

**En une phrase** — le cadre multi-agents de Microsoft pour des conversations asynchrones entre agents (AssistantAgent qui « pense », UserProxyAgent qui exécute), prolongé par un fork communautaire, AG2.

## Ce que dit le corpus
Microsoft AutoGen est un framework open source issu de Microsoft Research pour créer des agents et applications d'IA, simplifiant la construction de systèmes multi-agents à base de LLM. Son architecture comporte **trois couches** : **Core** (transfert de messages, agents pilotés par les événements, exécution locale ou distribuée — la « plomberie » qui permet aux agents de se parler et de réagir à des déclencheurs) ; **AgentChat**, qui suppose des agents conversationnels et fournit des équipes « modèles » réunissant un **AssistantAgent** (qui utilise les LLM pour raisonner) et un **UserProxyAgent** (exécution du code et usage d'outils) ; et **Extensions** (LocalSearchTool, MultimodalWebSurfer, AutoGenBench, AutoGen Studio no-code). Le corpus cite un **article primé publié en 2024 par Chi Wang (Microsoft) et d'autres chercheurs**, démontrant l'applicabilité à des problèmes réels (chaîne d'approvisionnement, décision en ligne). Côté **AG2** : présenté comme un « AgentOS open source », c'est essentiellement la version 0.2.34 d'AutoGen poursuivie sous un autre nom — un fork **piloté par la communauté** (Chi Wang ayant quitté Microsoft pour Google DeepMind), avec des contributeurs de Meta, IBM et d'universités.

## Tradeoff / insight pour un senior
Pur vocabulaire : le couple AssistantAgent / UserProxyAgent = séparation raisonnement / exécution, pattern déjà connu. À noter : la fracture AutoGen (Microsoft) vs AG2 (communauté) est un risque de gouvernance à arbitrer avant d'adopter l'un ou l'autre.

## Source primaire
Cité par IBM : article primé de Chi Wang et al., 2024 (référence nommée mais sans DOI dans le texte du corpus).

## Voir aussi
- [crewai](crewai.md)
- [langgraph](langgraph.md)
