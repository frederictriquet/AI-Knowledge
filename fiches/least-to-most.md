---
titre: "Least-to-Most prompting"
theme: raisonnement-planification
niveau: 🟡
source_url: https://arxiv.org/abs/2205.10625---

# Least-to-Most prompting

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. Glossaire · Pertinence 🟡 tradeoff

**En une phrase** — on décompose explicitement un problème en sous-problèmes ordonnés du plus simple au plus complexe, puis on les résout en séquence, chaque réponse servant de contexte à la suivante.

## L'idée
Least-to-Most procède en deux phases. D'abord une phase de **décomposition** : le modèle liste les sous-questions nécessaires, du plus élémentaire au plus dépendant. Ensuite une phase de **résolution séquentielle** : chaque sous-problème est résolu en réinjectant les réponses précédentes dans le prompt. Contrairement au CoT qui raisonne « en un bloc », la dépendance est rendue explicite et chaînée, ce qui aide sur les problèmes plus durs que les exemples vus en few-shot.

## Tradeoff / quand l'utiliser
Améliore la **généralisation compositionnelle** : on résout des instances plus longues/complexes que les démonstrations. Coût : plusieurs appels et une décomposition correcte (une mauvaise décomposition propage l'erreur). À privilégier quand le problème se découpe naturellement en étapes dépendantes (parsing, raisonnement symbolique, math à plusieurs étages). Moins utile pour les tâches atomiques ou non décomposables, où le surcoût d'orchestration ne paie pas.

## Source primaire
Zhou et al., 2022, *Least-to-Most Prompting Enables Complex Reasoning in Large Language Models*, arXiv:2205.10625. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [chain-of-thought](chain-of-thought.md) (corpus)
- [step-back](step-back.md) (hors-corpus)
