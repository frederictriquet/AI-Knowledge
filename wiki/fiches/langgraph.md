---
titre: "LangGraph"
type: "Concept"
theme: frameworks-outillage
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/langgraph
source_titre: "Qu’est-ce que LangGraph ?"
---

# LangGraph

**En une phrase** — le cadre d'orchestration de LangChain qui modélise un workflow d'agents comme un graphe d'états (nœuds, arêtes, cycles) avec gestion explicite de l'état et human-in-the-loop.

## En détail
LangGraph, créé par LangChain, est un cadre open source pour construire, déployer et gérer des workflows d'agents complexes. Il « exploite la puissance des architectures basées sur des graphes » pour modéliser les relations entre composants. Ses concepts clés : un **état** servant de banque de mémoire qui enregistre et suit toutes les informations traitées (utile au débogage, car il centralise l'état de l'application) ; des **graphes avec état** où chaque nœud est une étape de calcul conservant le contexte ; des **graphes cycliques** (au moins un cycle, essentiels aux exécutions d'agents) ; des **nœuds** représentant agents ou composants (« acteurs ») ; et des **arêtes** (edges), fonctions Python déterminant le nœud suivant selon l'état courant, en branches conditionnelles ou transitions fixes. LangGraph s'appuie sur LangChain, intègre le **human-in-the-loop (HITL)**, le RAG, les serveurs MCP, et propose LangGraph Studio (interface visuelle no-code) ainsi que des capacités de débogage.

## Exemple
Concret de l'état : un agent qui surveille la météo conserve dans l'« état » le cumul d'enneigement et émet des suggestions selon l'évolution des chutes de neige — le débogage consiste à inspecter ce bloc-notes centralisé. Côté production : Norwegian Cruise Line s'appuie sur LangGraph pour compiler et affiner des solutions d'IA destinées à ses hôtes, et des services comme Google Duplex l'emploient pour imiter des conversations humaines. Cas multi-agents emblématique de Joao Moura : CrewAI orchestrant via LangGraph la vérification d'e-mails et la rédaction de brouillons, où des agents dédiés collaborent en parallèle.

## Tradeoff / insight pour un senior
Pur vocabulaire, mais c'est l'outil le plus sérieux pour le **contrôle de flux** : graphe d'états + cycles = vraie machine à états, là où LangChain s'arrête aux chaînes linéaires. Si tu as besoin de boucles, branchements conditionnels et reprise sur point de contrôle, c'est la brique adaptée.

## Source primaire
Voir la documentation LangGraph.

## Voir aussi
- [langchain](langchain.md)
- [crewai](crewai.md)
