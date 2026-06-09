---
titre: "Évaluer les LLM (évals spécifiques à la tâche)"
theme: evaluation
niveau: 🔴
source_url: https://eugeneyan.com/writing/evals/
source_titre: "Task-Specific LLM Evals that Do & Don't Work"
---

# Évaluer les LLM (évals spécifiques à la tâche)

**En une phrase** — Les évals « sur étagère » corrèlent mal avec la performance applicative ; Eugene propose des évals concrètes, calibrées par tâche (classification, résumé, traduction, toxicité), sans jamais abandonner l'évaluation humaine.

## Ce que dit la source
Le post réel est « Task-Specific LLM Evals that Do & Don't Work » : la plupart des évals génériques ne sont ni discriminantes ni corrélées à la performance en production. Eugene détaille des évals qui marchent par tâche — **classification/extraction** (recall, precision, ROC-AUC, PR-AUC, séparation des distributions), **résumé** (les quatre dimensions de Kryscinski : consistance factuelle via NLI, pertinence, fluidité, cohérence ; les évals reference-based comme ROUGE marchent mal), **traduction** (évals statistiques et apprises, reference-based et reference-free, en s'appuyant sur le WMT), et **toxicité** (RealToxicityPrompts, BOLD, Perspective API au seuil p ≥ 0,5). Il insiste : l'**évaluation humaine reste le gold standard** pour les tâches complexes et la plupart des évals automatiques reposent in fine sur des annotations humaines. Enfin, il faut **calibrer la barre d'évaluation sur le niveau de risque** : viser le quasi-parfait partout est irréaliste — le taux d'incohérence factuelle typique reste de 5-10 % même après RAG et bon prompting.

## Pourquoi c'est utile
Eugene apporte la **rigueur métier par tâche** : quelles métriques utiliser, lesquelles échouent (ROUGE pour le résumé abstrait), l'usage du NLI pour la consistance, l'active learning pour enrichir les labels, et le pragmatisme de calibrer le seuil au risque réel.

## Points clés
- Les évals off-the-shelf échouent souvent : peu discriminantes.
- Classification : ROC-AUC, PR-AUC, séparation des distributions.
- Résumé : consistance (NLI), pertinence, longueur — pas ROUGE seul.
- L'évaluation humaine reste indispensable et sous-tend les évals auto.
- Calibrer la barre au risque ; ~5-10 % d'incohérence factuelle résiduelle.

## Voir aussi
- [Évaluation de trajectoire](evaluation-trajectoire.md)
- [Pourquoi les benchmarks comptent](pourquoi-les-benchmarks-comptent.md)
- [Error analysis](error-analysis.md)
- [post complet](../sources/eugene-yan/md/evals.md)
