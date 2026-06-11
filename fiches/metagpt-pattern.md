---
titre: "MetaGPT : communication structurée + feedback exécutable"
type: "Concept"
theme: multi-agents
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/topics/metagpt
source_titre: "Qu'est-ce que MetaGPT ?"
source_primaire: "arXiv:2308.00352"
---

# MetaGPT : communication structurée + feedback exécutable

**En une phrase** — un cadre multi-agents qui simule une société de logiciels et où les agents s'échangent des documents schématisés (PRD, diagrammes) plutôt que du dialogue libre, l'ingénieur bouclant sur ses propres tests.

## En détail
MetaGPT (technologie de DeepWisdom) encode des procédures opérationnelles standard (SOP) dans des séquences de prompts pour orchestrer une équipe d'agents jouant les rôles d'une société de logiciels : chef de produit, architecte, chef de projet, ingénieur, ingénieur QA. Sa particularité : il n'utilise pas de langage naturel non contraint comme interface de communication, mais une **communication structurée**. Là où ChatDev fait dialoguer ses agents, ceux de MetaGPT communiquent via des sorties structurées (documents, schémas, diagrammes) publiées dans un **pool de messages global** (mécanisme publish/subscribe). Tous les transferts respectent un schéma établi, ce qui « réduit le risque d'hallucination causée par des discussions à vide entre différents LLM » et améliore le taux de réussite de la génération de code. L'agent ingénieur pratique une **programmation itérative avec feedback exécutable** : il écrit et exécute ses propres tests unitaires, débogue, et reprend jusqu'à réussite ou un **maximum de 3 tentatives**.

## Exemple
Prompt utilisateur unique : « Créez-moi une application React pour gestionnaires de patrimoine, permettant d'examiner les portefeuilles clients et de recommander des fonds, fonctionnant en Amérique, au Royaume-Uni et en Espagne. » Le chef de produit en dérive un PRD typé via des instructions SOP figées : « Fournir jusqu'à trois objectifs orthogonaux », « 3 à 5 scénarios utilisateurs », « 5 à 7 produits concurrents » (Wealthfront, Personal Capital…), un pool d'exigences priorisé P0/P1/P2. Ce PRD-artefact transite vers l'architecte avec le prompt : « Examinez si la conception de cette API répond aux exigences du PRD. » Aucun chat libre : chaque transfert est un document schématisé.

## Tradeoff / insight pour un senior
Insight réel : remplacer le chat inter-agents par des artefacts schématisés (sorties typées) coupe la dérive conversationnelle — c'est de la communication par contrat plutôt que par conversation. La boucle test-debug plafonnée à 3 essais est un garde-fou anti-boucle infinie concret.

## Source primaire
« MetaGPT : Metaprogramming for A Multi-Agent Collaborative Framework », arXiv:2308.00352.

## Voir aussi
- [chatdev-chatchain](chatdev-chatchain.md)
- [crewai](crewai.md)
