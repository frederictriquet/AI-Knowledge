---
titre: "LangFlow"
theme: frameworks-outillage
niveau: 🟢
provenance: ✅
base: ibm-guide-agents-ia
source_url: https://www.ibm.com/fr-fr/think/topics/langflow
source_titre: "Qu’est-ce que LangFlow ?"
---

# LangFlow

> Fiche du glossaire des patterns · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [55-langflow](../sources/ibm-guide-agents-ia/md/55-langflow.md)

**En une phrase** — une GUI low/no-code en glisser-déposer pour assembler agents, LLM et systèmes RAG en connectant des composants modulaires, avec des flux exportables en JSON.

## Ce que dit le corpus
IBM décrit LangFlow comme un outil open source low-code permettant de créer des agents IA et autres applications d'IA via une interface visuelle. Les utilisateurs connectent des composants entre eux ; les connexions déterminent le flux de données. L'interface transforme un projet de codage complexe en organigramme intuitif par glisser-déposer. Caractéristiques principales : interface visuelle low/no-code, nombreuses intégrations (mêmes API, bases vectorielles et options que son cadre parent LangChain), bibliothèque de composants (composants centraux et offres groupées de fournisseurs), flux exportables au format JSON (réutilisables et partageables) et code source ouvert. LangFlow se distingue du *vibe coding* : il remplace le codage par des composants prédéfinis plutôt que de générer du code via prompts. Cas d'usage cités : prototypage rapide, développement d'agents IA no-code, applications RAG, automatisation du service client. Le corpus distingue LangFlow (outil visuel) de LangChain (cadre à base de code) et de LangGraph (systèmes agentiques représentés sous forme de graphes).

## Tradeoff / insight pour un senior
Le compromis classique du low-code : vélocité de prototypage et collaboration (flux JSON exportables) contre profondeur de contrôle. Le corpus le note implicitement — composants personnalisés en Python possibles, mais un composant à source fermée n'expose pas son fonctionnement interne. Outil de prototype et de démo, pas de moteur d'exécution de production par défaut.

## Source primaire
Non citée par IBM — voir le dépôt GitHub LangFlow (hors-corpus).

## Voir aussi
- [llamaindex](llamaindex.md)
- [orchestration-types](orchestration-types.md)
