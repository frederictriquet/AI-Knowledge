---
titre: "Optimisation des prompts"
theme: prompting
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/prompt-optimization
source_titre: "Qu’est-ce que l’optimisation des prompts ?"---

# Optimisation des prompts

> Fiche du glossaire prompting · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [../md/16-prompt-optimization.md](../sources/ibm-guide-prompt-engineering/md/16-prompt-optimization.md)

**En une phrase** — affiner automatiquement (ou semi-automatiquement) des prompts existants par itération, évaluation par indicateurs et boucles de feedback, à distinguer du prompt engineering manuel qui les conçoit de zéro.

## Ce que dit le corpus
IBM oppose explicitement prompt engineering (concevoir une structure depuis zéro : few-shot, CoT, métaprompts) et optimisation des prompts (affiner et régler un prompt d'origine sur plusieurs runs avec des indicateurs). Le processus type : évaluer le prompt de référence, mesurer les sorties (jugement humain ou métriques), ajuster clarté/structure/longueur, tester sur un jeu représentatif, et créer un template ou métaprompt réutilisable. Stratégies citées avec références non résolues : conception de templates, CFPO (optimisation conjointe contenu + format), few-shot + CoT, métaprompts pilotés par LLM, et PROMST (PRompt Optimization in Multi-Step Tasks) pour les workflows multi-étapes. IBM cite Choi (2025) introduisant un cadre de réglage par matrice de confusion qui améliore la pertinence en limitant l'usage de tokens. Outils nommés : PromptLayer (« Git pour les prompts », versioning, A/B testing) et Humanloop (feedback humain structuré). Pièges : manque de précision, surcharge d'un prompt unique, formatage incohérent, sauter les itérations, ignorer l'audience.

## Tradeoff / insight pour un senior
L'optimisation des prompts est justifiée quand latence, précision ou coût-token deviennent critiques à l'échelle. Elle déplace le travail d'un artisanat manuel vers un pipeline mesurable (logs, métriques, A/B). Limite : optimiser contre un metric proxy peut sur-ajuster au jeu d'évaluation et casser au déploiement — le metric n'est pas la tâche.

## Source primaire
Non citée de façon vérifiable : seul Choi (2025, matrice de confusion) est nommé ; CFPO et PROMST sont évoqués sans référence résolue dans le fichier. N'invente aucun arXiv.

## Voir aussi
- [DSPy](dspy.md)
- [Méta-prompting](meta-prompting.md)
