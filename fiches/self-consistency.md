---
titre: "Self-Consistency"
type: "Concept"
theme: raisonnement-planification
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/prompt-engineering-techniques
source_titre: "Techniques de prompt engineering"
---

# Self-Consistency

**En une phrase** — échantillonner plusieurs chaînes de raisonnement CoT indépendantes puis voter à la majorité pour la réponse finale, plutôt que de se fier à une seule génération.

## En détail
La self-consistency est parfois nommée « cohérence propre » en français. Elle désigne un principe qui « utilise le modèle pour générer plusieurs propositions indépendantes et identifier la réponse la plus cohérente et la plus précise », utile pour les tâches de raisonnement ou d'interprétation. Elle figure parmi les avancées de la CoT, garantissant « l'intégrité logique des chemins générés ». Dans le contexte du ToT, le mécanisme de cohérence propre « fournit des évaluations fiables en sollicitant le modèle plusieurs fois ».

## Exemple
Sur la tâche « expliquer le changement climatique », le prompt IBM matérialise la cohérence propre : `Provide three different explanations of climate change, its causes, and its effects. Then identify the most coherent and clear explanation`. Le modèle produit trois explications distinctes dans un même appel, puis sélectionne lui-même la plus logique. C'est une approximation « low-cost » du vrai self-consistency de Wang et al. (N échantillons indépendants + vote externe) : ici, génération et arbitrage tiennent dans un seul prompt, sans agrégation programmatique.

## Tradeoff / insight pour un senior
La self-consistency échange un coût d'inférence multiplié par N (N échantillons) contre une réduction de variance : le vote majoritaire absorbe les chaînes aberrantes. Elle ne s'applique proprement qu'aux tâches à réponse finale agrégeable (un nombre, un label) ; sur du texte libre, « voter » devient un problème ouvert. Diminishing returns rapides au-delà de quelques dizaines d'échantillons.

## Source primaire
Wang et al. 2022, « Self-Consistency Improves Chain of Thought Reasoning in Language Models ».

## Voir aussi
- [Chain-of-Thought (CoT)](chain-of-thought.md)
- [Tree of Thoughts (ToT)](tree-of-thoughts.md)
