---
titre: "Techniques d'ensembling"
theme: prompting
niveau: 🔴
source_url: https://arxiv.org/abs/2406.06608
source_titre: "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques"
---

# Techniques d'ensembling

**En une phrase** — Résoudre le même problème via plusieurs prompts/chemins de raisonnement, puis agréger les sorties (souvent par vote majoritaire) pour réduire la variance, au prix de N appels.

## Ce que dit la source
L'ensembling (§2.2.4) consiste à utiliser plusieurs prompts pour résoudre un même problème, puis à agréger les réponses en une sortie finale, le plus souvent par majority vote. Le rapport indique que ces techniques réduisent la variance des sorties et améliorent souvent la précision, mais augmentent le nombre d'appels au modèle. Self-Consistency (Wang et al.) échantillonne plusieurs chemins CoT à température non nulle puis prend un vote majoritaire. Universal Self-Consistency (Chen et al.) délègue la sélection du majoritaire à un prompt plutôt qu'à un comptage programmatique, utile pour le texte libre. DiVeRSe (Li et al.) crée plusieurs prompts, applique Self-Consistency à chacun et score les chemins de raisonnement. Mixture of Reasoning Experts / MoRE (Si et al.) combine des experts spécialisés par type de raisonnement et sélectionne par score d'accord. Max Mutual Information Method (Sorensen et al.) choisit le template maximisant l'information mutuelle prompt-sorties. USP (Wan et al.) généralise COSP via des données non labellisées. Prompt Paraphrasing (Jiang et al.) reformule un prompt pour produire des variantes d'ensemble.

## Pourquoi c'est utile
Cette famille détaille tout un éventail d'agrégateurs (Universal Self-Consistency, DiVeRSe, MoRE, Max Mutual Information, USP, Prompt Paraphrasing) et pose explicitement l'arbitrage coût ×N contre robustesse.

## Techniques clés
- Self-Consistency (Wang et al.) — multiples chemins CoT puis vote majoritaire.
- Universal Self-Consistency (Chen et al.) — sélection du majoritaire par prompt.
- DiVeRSe (Li et al.) — Self-Consistency par prompt puis scoring des chemins.
- Mixture of Reasoning Experts / MoRE (Si et al.) — experts spécialisés, choix par accord.
- Max Mutual Information Method (Sorensen et al.) — template maximisant l'information mutuelle.
- USP (Wan et al.) — généralisation de COSP via données non labellisées.
- Prompt Paraphrasing (Jiang et al.) — reformulations pour ensemble.

## Voir aussi
- [Self-Consistency](self-consistency.md)
- [papier complet](../sources/prompt-report/md/prompt-report.md)
