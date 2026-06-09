# LangGraph

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [53-langgraph](../md/53-langgraph.md)

**En une phrase** — le cadre d'orchestration de LangChain qui modélise un workflow d'agents comme un graphe d'états (nœuds, arêtes, cycles) avec gestion explicite de l'état et human-in-the-loop.

## Ce que dit le corpus
LangGraph, créé par LangChain, est un cadre open source pour construire, déployer et gérer des workflows d'agents complexes. Il « exploite la puissance des architectures basées sur des graphes » pour modéliser les relations entre composants. Ses concepts clés : un **état** servant de banque de mémoire qui enregistre et suit toutes les informations traitées (utile au débogage, car il centralise l'état de l'application) ; des **graphes avec état** où chaque nœud est une étape de calcul conservant le contexte ; des **graphes cycliques** (au moins un cycle, essentiels aux exécutions d'agents) ; des **nœuds** représentant agents ou composants (« acteurs ») ; et des **arêtes** (edges), fonctions Python déterminant le nœud suivant selon l'état courant, en branches conditionnelles ou transitions fixes. LangGraph s'appuie sur LangChain, intègre le **human-in-the-loop (HITL)**, le RAG, les serveurs MCP, et propose LangGraph Studio (interface visuelle no-code) ainsi que des capacités de débogage.

## Tradeoff / insight pour un senior
Pur vocabulaire, mais c'est l'outil du corpus le plus sérieux pour le **contrôle de flux** : graphe d'états + cycles = vraie machine à états, là où LangChain s'arrête aux chaînes linéaires. Si tu as besoin de boucles, branchements conditionnels et reprise sur point de contrôle, c'est la brique adaptée.

## Source primaire
Non citée académiquement par IBM — voir la documentation LangGraph (hors-corpus).

## Voir aussi
- [langchain](langchain.md)
- [crewai](crewai.md)
