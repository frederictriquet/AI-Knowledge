---
titre: "Agent apprenant (modèle AIMA)"
type: "Concept"
theme: fondamentaux-agents
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-learning
source_titre: "Qu’est-ce qu’un agent d’IA apprenant ?"
---

# Agent apprenant (modèle AIMA)

**En une phrase** — un agent qui se décompose en quatre rôles internes pour boucler sur ses propres erreurs et s'améliorer dans le temps.

## En détail
Un agent apprenant améliore ses performances au fil du temps en s'adaptant aux nouvelles expériences et données, là où les autres agents s'appuient sur des règles ou des modèles prédéfinis. Il se décompose en quatre éléments principaux : l'**élément de performance** (prend les décisions à partir d'une base de connaissances), l'**élément d'apprentissage** (ajuste et améliore les connaissances en fonction des retours et de l'expérience), le **critique** (évalue les actions et fournit un retour sous forme de récompenses ou de sanctions), et le **générateur de problèmes** (suggère des actions exploratoires pour découvrir de nouvelles stratégies). L'apprentissage par renforcement en est l'illustration canonique : l'agent explore, reçoit récompenses et pénalités, et affine sa politique. Il s'appuie sur le machine learning (supervisé, non supervisé, par renforcement, continu).

## Exemple
La source déroule un cas multi-agents en réseau hospitalier : un agent apprenant avancé équipé d'IA générative supervise des agents plus simples (réflexes ou basés sur des objectifs), chacun portant un rôle ou une tâche du système de santé, pour améliorer les résultats patients et l'efficacité opérationnelle. La nuance utile : la rétroaction (le rôle du critique) n'est pas tout l'apprentissage. La source distingue son régime selon la technique — récompenses/pénalités en RL, comparaison à la vérité terrain via fonction de perte en supervisé, pseudo-étiquettes auto-générées en auto-supervisé.

## Tradeoff / insight pour un senior
Pur vocabulaire, mais utile : le quatuor performance / apprentissage / critique / générateur de problèmes est exactement le découpage d'une boucle RL (politique, mise à jour, fonction de récompense, exploration). Le « générateur de problèmes » formalise le compromis exploration/exploitation que les autres types d'agents ignorent — c'est ce qui distingue un agent qui s'améliore d'un agent figé.

## Source primaire
Le modèle des quatre composants vient de Russell & Norvig, *AIMA* (chap. 2, learning agent).

## Voir aussi
- [Taxonomie des 5 types d'agents](taxonomie-5-types-agents.md)
- [Architectures réactive / délibérative / cognitive](archi-reactif-deliberatif-cognitif.md)
