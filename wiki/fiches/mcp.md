---
titre: "MCP (Model Context Protocol)"
type: "Concept"
theme: protocoles-interop
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/topics/model-context-protocol
source_titre: "Qu’est-ce que le MCP ?"
---

# MCP (Model Context Protocol)

**En une phrase** — le standard ouvert (Anthropic, 2024) qui branche un modèle sur des outils/données externes via un trio hôte/client/serveur en JSON-RPC 2.0 ; l'« USB-C » de l'intégration d'outils, pas un framework d'orchestration.

## En détail
Le MCP est une couche de standardisation permettant aux applications d'IA de communiquer avec des services externes (outils, bases de données, modèles prédéfinis), introduite par Anthropic en 2024. Ce n'est pas un framework pour agents mais une couche d'intégration : il complète LangChain, LangGraph, BeeAI, LlamaIndex, crewAI sans les remplacer — c'est le LLM qui décide quel outil appeler. L'architecture client/serveur comporte trois composants : l'**hôte MCP** (logique d'orchestration, peut héberger plusieurs clients), le **client MCP** (relation 1:1 avec un serveur, gestion de session, parsing/erreurs) et le **serveur MCP**. Les serveurs exposent trois primitives : **Ressources** (renvoient des données sans calcul), **Outils** (effet de bord : calcul ou requête API) et **Prompts** (modèles réutilisables). La couche de transport encode les messages en JSON-RPC 2.0 (requêtes, réponses, notifications), via deux transports : **stdio** (ressources locales, synchrone et léger) et HTTP en flux (*HTTP streamable* ; les itérations antérieures utilisaient SSE).

## Exemple
Cas concret tiré de la source : une IA qui scanne votre boîte mail pour planifier des rendez-vous clients, pousse des mises à jour boursières et vous résume par SMS la dernière heure d'activité Slack. Le problème sans MCP : chaque fournisseur expose une API différente, et la moindre modification d'un outil fait s'effondrer tout le workflow. Côté serveur, les intégrations exposées sont par exemple Slack, GitHub, Git, Docker ou la recherche web ; côté client, Claude.ai, Cursor, Microsoft Copilot Studio ou Postman. Analogie filée : MCP est le tableau de commande d'un circuit électrique qui décide quel courant (contexte, sortie d'outil) alimente le moteur (modèle) et à quel moment.

## Tradeoff / insight pour un senior
Le point non trivial : MCP standardise l'**accès aux outils** (un modèle ↔ plusieurs outils), pas la communication inter-agents — d'où sa complémentarité avec A2A/ACP. L'équipe ACP l'a jugé inadapté au multi-agents : pas de streaming delta granulaire, pas de mémoire partagée multi-agents, corps de message non structuré (tout schéma JSON accepté), complexité JSON-RPC + SDK requis. Relation client↔serveur strictement 1:1.

## Source primaire
MCP introduit par Anthropic en 2024 (standard ouvert), primitives Ressources/Outils/Prompts selon la documentation Anthropic.

## Voir aussi
- [a2a](a2a.md)
- [acp](acp.md)
