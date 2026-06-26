---
titre: "Self-Refine"
type: "Concept"
theme: raisonnement-planification
niveau: 🟡
source_url: https://arxiv.org/abs/2303.17651
---

# Self-Refine

**En une phrase** — un même modèle produit une sortie, génère sa propre critique, puis se révise, en boucle, sans aucun signal externe.

## L'idée
Self-Refine est une boucle générer → critiquer → raffiner pilotée par un seul LLM via trois prompts. Le modèle produit une réponse initiale, se donne un **feedback** détaillé et actionnable sur sa propre sortie, puis réécrit en intégrant ce feedback. On itère jusqu'à convergence ou budget épuisé. Tout le signal d'amélioration vient du modèle lui-même : pas d'exécution de code, pas d'environnement, pas d'humain.

## Exemple
Tâche « somme de 1 à N » : la sortie initiale est une boucle `for i in range(n+1): res += i`. Le modèle génère son propre feedback — « code lent, force brute ; utiliser la formule n(n+1)/2 » — puis réécrit en `return (n*(n+1))//2`. Avec GPT-4, les gains absolus par tâche sont spectaculaires hors maths : Dialogue Response **+49,2** (25,4 → 74,6 %), Sentiment Reversal **+32,4**, Constrained Generation **+30,0**, mais Math Reasoning seulement **+0,2** (92,9 → 93,1 %) — l'auto-critique aveugle ne corrige pas ce que le modèle ne sait pas vérifier.

## Tradeoff / quand l'utiliser
Gains réels sur la qualité rédactionnelle, la lisibilité ou le respect de contraintes, sans infrastructure. Mais l'auto-critique sans ancrage externe plafonne vite et peut renforcer les erreurs du modèle (il ne sait pas ce qu'il ne sait pas). À distinguer de Reflexion, qui exploite un **retour de l'environnement** (échec de test, récompense) : Self-Refine raffine « à l'aveugle », Reflexion apprend d'un signal objectif. Utiliser Self-Refine quand aucun vérificateur externe n'existe.

## Source primaire
Madaan et al., 2023, *Self-Refine: Iterative Refinement with Self-Feedback*, arXiv:2303.17651. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [reflexion](reflexion.md)
- [chain-of-verification](chain-of-verification.md)
