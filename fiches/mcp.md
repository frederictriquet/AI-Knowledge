---
titre: "MCP (Model Context Protocol)"
theme: protocoles-interop
niveau: 🔴
provenance: ✅
base: ibm-guide-agents-ia
source_url: https://www.ibm.com/fr-fr/think/topics/model-context-protocol
source_titre: "Qu’est-ce que le MCP ?"
---

# MCP (Model Context Protocol)

> Fiche du glossaire des patterns · Pertinence 🔴 substance · Provenance ✅ présent · Sources corpus : [37-model-context-protocol](../sources/ibm-guide-agents-ia/md/37-model-context-protocol.md), [38-how-to-build-an-mcp-server](../sources/ibm-guide-agents-ia/md/38-how-to-build-an-mcp-server.md), [32-ai-agent-protocols](../sources/ibm-guide-agents-ia/md/32-ai-agent-protocols.md), [33-agent-communication-protocol](../sources/ibm-guide-agents-ia/md/33-agent-communication-protocol.md)

**En une phrase** — le standard ouvert (Anthropic, 2024) qui branche un modèle sur des outils/données externes via un trio hôte/client/serveur en JSON-RPC 2.0 ; l'« USB-C » de l'intégration d'outils, pas un framework d'orchestration.

## Ce que dit le corpus
IBM décrit le MCP comme une couche de standardisation permettant aux applications d'IA de communiquer avec des services externes (outils, bases de données, modèles prédéfinis), introduite par Anthropic en 2024. Ce n'est pas un framework pour agents mais une couche d'intégration : il complète LangChain, LangGraph, BeeAI, LlamaIndex, crewAI sans les remplacer — c'est le LLM qui décide quel outil appeler. L'architecture client/serveur comporte trois composants : l'**hôte MCP** (logique d'orchestration, peut héberger plusieurs clients), le **client MCP** (relation 1:1 avec un serveur, gestion de session, parsing/erreurs) et le **serveur MCP**. Les serveurs exposent trois primitives : **Ressources** (renvoient des données sans calcul), **Outils** (effet de bord : calcul ou requête API) et **Prompts** (modèles réutilisables). La couche de transport encode les messages en JSON-RPC 2.0 (requêtes, réponses, notifications), via deux transports : **stdio** (ressources locales, synchrone et léger) et HTTP en flux (*HTTP streamable* ; les itérations antérieures utilisaient SSE).

## Tradeoff / insight pour un senior
Le point non trivial : MCP standardise l'**accès aux outils** (un modèle ↔ plusieurs outils), pas la communication inter-agents — d'où sa complémentarité avec A2A/ACP. Le corpus 33 documente pourquoi l'équipe ACP l'a jugé inadapté au multi-agents : pas de streaming delta granulaire, pas de mémoire partagée multi-agents, corps de message non structuré (tout schéma JSON accepté), complexité JSON-RPC + SDK requis. Relation client↔serveur strictement 1:1.

## Source primaire
Citée par IBM : MCP introduit par Anthropic en 2024 (standard ouvert), primitives Ressources/Outils/Prompts selon la documentation Anthropic. Analogie USB-C reprise par le corpus.

## Voir aussi
- [a2a](a2a.md)
- [acp](acp.md)
