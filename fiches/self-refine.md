---
titre: "Self-Refine"
theme: raisonnement-planification
niveau: 🟡
provenance: ➕
base: ibm-guide-agents-ia/hors-corpus
source_url: https://arxiv.org/abs/2303.17651
---

# Self-Refine

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. Glossaire · Pertinence 🟡 tradeoff

**En une phrase** — un même modèle produit une sortie, génère sa propre critique, puis se révise, en boucle, sans aucun signal externe.

## L'idée
Self-Refine est une boucle générer → critiquer → raffiner pilotée par un seul LLM via trois prompts. Le modèle produit une réponse initiale, se donne un **feedback** détaillé et actionnable sur sa propre sortie, puis réécrit en intégrant ce feedback. On itère jusqu'à convergence ou budget épuisé. Tout le signal d'amélioration vient du modèle lui-même : pas d'exécution de code, pas d'environnement, pas d'humain.

## Tradeoff / quand l'utiliser
Gains réels sur la qualité rédactionnelle, la lisibilité ou le respect de contraintes, sans infrastructure. Mais l'auto-critique sans ancrage externe plafonne vite et peut renforcer les erreurs du modèle (il ne sait pas ce qu'il ne sait pas). À distinguer de Reflexion, qui exploite un **retour de l'environnement** (échec de test, récompense) : Self-Refine raffine « à l'aveugle », Reflexion apprend d'un signal objectif. Utiliser Self-Refine quand aucun vérificateur externe n'existe.

## Source primaire
Madaan et al., 2023, *Self-Refine: Iterative Refinement with Self-Feedback*, arXiv:2303.17651. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [reflexion](reflexion.md) (corpus)
- [chain-of-verification](chain-of-verification.md) (hors-corpus)
