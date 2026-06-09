# Planification : objectif / état / séquençage

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [17-ai-agent-planning](../md/17-ai-agent-planning.md), [03-agentic-ai](../md/03-agentic-ai.md)

**En une phrase** — planifier, c'est définir un objectif (état final visé), modéliser l'état courant, puis dériver la séquence d'actions qui mène de l'un à l'autre.

## Ce que dit le corpus
La planification par agent d'IA détermine une séquence d'actions pour atteindre un objectif donné ; elle implique prise de décision, hiérarchisation des objectifs et séquençage. Trois éléments clés sont décrits. La **définition des objectifs** fixe l'état final visé ; les objectifs peuvent être statiques ou dynamiques, et un objectif complexe est éclaté en sous-objectifs (décomposition des tâches), les LLM divisant un but général en sous-tâches exécutées en plusieurs étapes. La **représentation de l'état** modélise conditions actuelles, contraintes et facteurs contextuels via les connaissances intégrées et la perception (ex. positions des pièces aux échecs, coordonnées et obstacles en robotique). Le **séquençage des actions** structure un ensemble logique d'étapes : identifier les actions potentielles, les réduire aux optimales, les prioriser, repérer dépendances et étapes conditionnelles. Le corpus 03 rejoint ce vocabulaire (« définition des objectifs », arbres de décision, planification).

## Tradeoff / insight pour un senior
C'est le vocabulaire classique de la planification (goal / state / action), réhabillé pour les agents LLM. L'enjeu d'ingénierie est la fidélité de la représentation d'état : un état mal modélisé fait diverger le séquençage quelle que soit la qualité du LLM.

## Source primaire
Non rattaché par IBM à une source nommée ; reformulation du vocabulaire de planification classique en IA (hors-corpus).

## Voir aussi
- [Planification probabiliste](planification-probabiliste.md)
- [Décomposition anticipée vs au fil de l'eau](decomposition-first-vs-interleaved.md)
