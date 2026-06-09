---
titre: "Logique conditionnelle & heuristique"
theme: fondamentaux-agents
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/agentic-reasoning
source_titre: "Qu’est-ce que le raisonnement agentique ?"---

# Logique conditionnelle & heuristique

> Fiche du glossaire des patterns · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [../md/18-agentic-reasoning.md](../sources/ibm-guide-agents-ia/md/18-agentic-reasoning.md)

**En une phrase** — du raisonnement câblé : des règles si-alors et des scores/fonctions d'utilité codés en dur dans la boucle de décision, sans apprentissage.

## Ce que dit le corpus
Le corpus classe la logique conditionnelle et l'heuristique parmi les stratégies de raisonnement agentique (18). La logique conditionnelle repose sur des règles condition-action préprogrammées (« si-alors ») : quand une condition est remplie, l'agent exécute l'action correspondante ; exemple donné : un agent bancaire de détection de fraude signalant une transaction selon des critères définis (18). Sa limite explicite : l'agent ne peut pas agir face à un scénario non reconnu ; les agents basés sur modèle atténuent cela via mémoire et perception mais restent soumis aux règles (18). L'heuristique concerne les agents basés sur objectifs (algorithme de recherche pour atteindre un but) et basés sur l'utilité (fonction d'utilité pour choisir le résultat optimal) ; exemple : un agent de navigation cherchant l'itinéraire le plus rapide, puis aussi le moins consommateur de carburant (18).

## Tradeoff / insight pour un senior
Programmation classique, rien de non trivial : déterminisme, traçabilité et faible coût contre rigidité totale hors du domaine prévu. C'est le socle des agents réflexes et basés sur objectifs/utilité ; le « raisonnement » LLM (CoT, ReAct, etc.) n'intervient que lorsque l'espace d'états devient trop ouvert pour être câblé à la main.

## Source primaire
Non citée par IBM — concept de programmation classique / IA symbolique décrit sans référence dans le corpus (hors-corpus : algorithmes de recherche heuristique type A*, fonctions d'utilité).

## Voir aussi
- [ReAct](react.md)
- [Chain-of-Thought (CoT)](chain-of-thought.md)
