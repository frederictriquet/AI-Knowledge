# MetaGPT : communication structurée + feedback exécutable

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🔴 substance · Provenance ✅ présent · Sources corpus : [56-metagpt](../md/56-metagpt.md)

**En une phrase** — un cadre multi-agents qui simule une société de logiciels et où les agents s'échangent des documents schématisés (PRD, diagrammes) plutôt que du dialogue libre, l'ingénieur bouclant sur ses propres tests.

## Ce que dit le corpus
MetaGPT (technologie de DeepWisdom) encode des procédures opérationnelles standard (SOP) dans des séquences de prompts pour orchestrer une équipe d'agents jouant les rôles d'une société de logiciels : chef de produit, architecte, chef de projet, ingénieur, ingénieur QA. Sa particularité : il n'utilise pas de langage naturel non contraint comme interface de communication, mais une **communication structurée**. Là où ChatDev fait dialoguer ses agents, ceux de MetaGPT communiquent via des sorties structurées (documents, schémas, diagrammes) publiées dans un **pool de messages global** (mécanisme publish/subscribe). Tous les transferts respectent un schéma établi, ce qui « réduit le risque d'hallucination causée par des discussions à vide entre différents LLM » et améliore le taux de réussite de la génération de code. L'agent ingénieur pratique une **programmation itérative avec feedback exécutable** : il écrit et exécute ses propres tests unitaires, débogue, et reprend jusqu'à réussite ou un **maximum de 3 tentatives**.

## Tradeoff / insight pour un senior
Insight réel : remplacer le chat inter-agents par des artefacts schématisés (sorties typées) coupe la dérive conversationnelle — c'est de la communication par contrat plutôt que par conversation. La boucle test-debug plafonnée à 3 essais est un garde-fou anti-boucle infinie concret.

## Source primaire
Cité par IBM : « MetaGPT : Metaprogramming for A Multi-Agent Collaborative Framework », arXiv:2308.00352.

## Voir aussi
- [chatdev-chatchain](chatdev-chatchain.md)
- [crewai](crewai.md)
