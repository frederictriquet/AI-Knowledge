---
titre: "Logique conditionnelle & heuristique"
type: "Concept"
theme: fondamentaux-agents
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/agentic-reasoning
source_titre: "Qu’est-ce que le raisonnement agentique ?"
---

# Logique conditionnelle & heuristique

**En une phrase** — du raisonnement câblé : des règles si-alors et des scores/fonctions d'utilité codés en dur dans la boucle de décision, sans apprentissage.

## En détail
La logique conditionnelle et l'heuristique figurent parmi les stratégies de raisonnement agentique. La logique conditionnelle repose sur des règles condition-action préprogrammées (« si-alors ») : quand une condition est remplie, l'agent exécute l'action correspondante ; exemple : un agent bancaire de détection de fraude signalant une transaction selon des critères définis. Sa limite : l'agent ne peut pas agir face à un scénario non reconnu ; les agents basés sur modèle atténuent cela via mémoire et perception mais restent soumis aux règles. L'heuristique concerne les agents basés sur objectifs (algorithme de recherche pour atteindre un but) et basés sur l'utilité (fonction d'utilité pour choisir le résultat optimal) ; exemple : un agent de navigation cherchant l'itinéraire le plus rapide, puis aussi le moins consommateur de carburant.

## Tradeoff / insight pour un senior
Programmation classique, rien de non trivial : déterminisme, traçabilité et faible coût contre rigidité totale hors du domaine prévu. C'est le socle des agents réflexes et basés sur objectifs/utilité ; le « raisonnement » LLM (CoT, ReAct, etc.) n'intervient que lorsque l'espace d'états devient trop ouvert pour être câblé à la main.

## Source primaire
Concept de programmation classique / IA symbolique. Voir aussi : algorithmes de recherche heuristique type A*, fonctions d'utilité.

## Voir aussi
- [ReAct](react.md)
- [Chain-of-Thought (CoT)](chain-of-thought.md)
