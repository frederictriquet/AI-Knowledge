---
titre: "Planification : objectif / état / séquençage"
type: "Concept"
theme: raisonnement-planification
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-planning
source_titre: "Qu’est-ce que la planification par agent d’IA ?"
---

# Planification : objectif / état / séquençage

**En une phrase** — planifier, c'est définir un objectif (état final visé), modéliser l'état courant, puis dériver la séquence d'actions qui mène de l'un à l'autre.

## En détail
La planification par agent d'IA détermine une séquence d'actions pour atteindre un objectif donné ; elle implique prise de décision, hiérarchisation des objectifs et séquençage. Trois éléments clés sont décrits. La **définition des objectifs** fixe l'état final visé ; les objectifs peuvent être statiques ou dynamiques, et un objectif complexe est éclaté en sous-objectifs (décomposition des tâches), les LLM divisant un but général en sous-tâches exécutées en plusieurs étapes. La **représentation de l'état** modélise conditions actuelles, contraintes et facteurs contextuels via les connaissances intégrées et la perception (ex. positions des pièces aux échecs, coordonnées et obstacles en robotique). Le **séquençage des actions** structure un ensemble logique d'étapes : identifier les actions potentielles, les réduire aux optimales, les prioriser, repérer dépendances et étapes conditionnelles.

## Exemple
Un utilisateur demande à un chatbot de planifier un voyage via un prompt en langage naturel. L'objectif complexe est d'abord décomposé en sous-tâches — réserver les vols, chercher des hôtels, bâtir un itinéraire — puis l'agent appelle des API pour récupérer prix et disponibilités en temps réel et suggérer des destinations. Pour le séquençage, la source prend un robot aspirateur : il doit calculer le parcours couvrant toute la pièce sans repasser inutilement, faute de quoi il gaspille ressources et temps d'exécution.

## Tradeoff / insight pour un senior
C'est le vocabulaire classique de la planification (goal / state / action), réhabillé pour les agents LLM. L'enjeu d'ingénierie est la fidélité de la représentation d'état : un état mal modélisé fait diverger le séquençage quelle que soit la qualité du LLM.

## Source primaire
Reformulation du vocabulaire de planification classique en IA ; aucune source primaire unique identifiée.

## Voir aussi
- [Planification probabiliste](planification-probabiliste.md)
- [Décomposition anticipée vs au fil de l'eau](decomposition-first-vs-interleaved.md)
