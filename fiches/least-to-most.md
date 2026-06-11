---
titre: "Least-to-Most prompting"
type: "Concept"
theme: raisonnement-planification
niveau: 🟡
source_url: https://arxiv.org/abs/2205.10625
---

# Least-to-Most prompting

**En une phrase** — on décompose explicitement un problème en sous-problèmes ordonnés du plus simple au plus complexe, puis on les résout en séquence, chaque réponse servant de contexte à la suivante.

## L'idée
Least-to-Most procède en deux phases. D'abord une phase de **décomposition** : le modèle liste les sous-questions nécessaires, du plus élémentaire au plus dépendant. Ensuite une phase de **résolution séquentielle** : chaque sous-problème est résolu en réinjectant les réponses précédentes dans le prompt. Contrairement au CoT qui raisonne « en un bloc », la dépendance est rendue explicite et chaînée, ce qui aide sur les problèmes plus durs que les exemples vus en few-shot.

## Exemple
Sur SCAN (généralisation compositionnelle, split par longueur où les séquences de test dépassent celles vues), code-davinci-002 passe de 16,2 % en chain-of-thought à 99,7 % en least-to-most, avec seulement 14 démonstrations. L'écart se creuse avec la complexité : sur la concaténation de dernières lettres, à 4 mots 94,0 % vs 84,2 %, mais à 12 mots 74,0 % vs 31,8 % — le CoT s'effondre dès que l'instance dépasse la longueur des exemples, là où la décomposition séquentielle tient.

## Tradeoff / quand l'utiliser
Améliore la **généralisation compositionnelle** : on résout des instances plus longues/complexes que les démonstrations. Coût : plusieurs appels et une décomposition correcte (une mauvaise décomposition propage l'erreur). À privilégier quand le problème se découpe naturellement en étapes dépendantes (parsing, raisonnement symbolique, math à plusieurs étages). Moins utile pour les tâches atomiques ou non décomposables, où le surcoût d'orchestration ne paie pas.

## Source primaire
Zhou et al., 2022, *Least-to-Most Prompting Enables Complex Reasoning in Large Language Models*, arXiv:2205.10625. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [chain-of-thought](chain-of-thought.md)
- [step-back](step-back.md)
