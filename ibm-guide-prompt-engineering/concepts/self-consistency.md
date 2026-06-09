# Self-Consistency

> Fiche du [glossaire prompting](../GLOSSAIRE-PROMPTING.md) · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [../md/02-prompt-engineering-techniques.md](../md/02-prompt-engineering-techniques.md), [../md/06-tree-of-thoughts.md](../md/06-tree-of-thoughts.md), [../md/20-chain-of-thoughts.md](../md/20-chain-of-thoughts.md)

**En une phrase** — échantillonner plusieurs chaînes de raisonnement CoT indépendantes puis voter à la majorité pour la réponse finale, plutôt que de se fier à une seule génération.

## Ce que dit le corpus
IBM emploie le terme français « cohérence propre » (self-consistency). Le fichier 02 la définit comme un principe qui « utilise le modèle pour générer plusieurs propositions indépendantes et identifier la réponse la plus cohérente et la plus précise », utile pour les tâches de raisonnement ou d'interprétation. Le fichier 20 la classe parmi les avancées de la CoT (section « Modèles plus petits et cohérence propre »), garantissant « l'intégrité logique des chemins générés ». Le fichier 06 la mobilise dans le ToT : le « mécanisme de cohérence propre est utilisé pour fournir des évaluations fiables en sollicitant le modèle plusieurs fois ». Le corpus reste descriptif : ni le mécanisme de vote majoritaire, ni de chiffres, ni de référence ne sont fournis.

## Tradeoff / insight pour un senior
La self-consistency échange un coût d'inférence multiplié par N (N échantillons) contre une réduction de variance : le vote majoritaire absorbe les chaînes aberrantes. Elle ne s'applique proprement qu'aux tâches à réponse finale agrégeable (un nombre, un label) ; sur du texte libre, « voter » devient un problème ouvert. Diminishing returns rapides au-delà de quelques dizaines d'échantillons.

## Source primaire
Non citée par IBM — voir Wang et al. 2022, « Self-Consistency Improves Chain of Thought Reasoning in Language Models » (hors-corpus).

## Voir aussi
- [Chain-of-Thought (CoT)](chain-of-thought.md)
- [Tree of Thoughts (ToT)](tree-of-thoughts.md)
- (base agents, hors-corpus) [Self-Consistency](../../ibm-guide-agents-ia/concepts/hors-corpus/self-consistency.md)
