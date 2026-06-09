# Agent apprenant (modèle AIMA)

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [14-ai-agent-learning](../md/14-ai-agent-learning.md), [01-ai-agents](../md/01-ai-agents.md)

**En une phrase** — un agent qui se décompose en quatre rôles internes pour boucler sur ses propres erreurs et s'améliorer dans le temps.

## Ce que dit le corpus
Un agent apprenant améliore ses performances au fil du temps en s'adaptant aux nouvelles expériences et données, là où les autres agents s'appuient sur des règles ou des modèles prédéfinis. IBM le décompose en quatre éléments principaux : l'**élément de performance** (prend les décisions à partir d'une base de connaissances), l'**élément d'apprentissage** (ajuste et améliore les connaissances en fonction des retours et de l'expérience), le **critique** (évalue les actions et fournit un retour sous forme de récompenses ou de sanctions), et le **générateur de problèmes** (suggère des actions exploratoires pour découvrir de nouvelles stratégies). Le corpus cite l'apprentissage par renforcement comme illustration : l'agent explore, reçoit récompenses et pénalités, et affine sa politique. Il s'appuie sur le machine learning (supervisé, non supervisé, par renforcement, continu).

## Tradeoff / insight pour un senior
Pur vocabulaire, mais utile : le quatuor performance / apprentissage / critique / générateur de problèmes est exactement le découpage d'une boucle RL (politique, mise à jour, fonction de récompense, exploration). Le « générateur de problèmes » formalise le compromis exploration/exploitation que les autres types d'agents ignorent — c'est ce qui distingue un agent qui s'améliore d'un agent figé.

## Source primaire
Non citée par IBM — le modèle des quatre composants vient de Russell & Norvig, *AIMA* (chap. 2, learning agent). Le corpus ne référence pas AIMA (hors-corpus).

## Voir aussi
- [Taxonomie des 5 types d'agents](taxonomie-5-types-agents.md)
- [Architectures réactive / délibérative / cognitive](archi-reactif-deliberatif-cognitif.md)
