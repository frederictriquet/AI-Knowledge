---
titre: "Process Reward Models (Let's Verify Step by Step)"
type: "Concept"
theme: raisonnement-planification
niveau: 🔴
source_url: https://arxiv.org/abs/2305.20050
source_titre: "Let’s Verify Step by Step"
---

# Process Reward Models (Let's Verify Step by Step)

> ⚠️ Fiche établie à partir de l'**abstract** (le HTML LaTeXML de ce papier est indisponible sur arXiv ; voir [md](../sources/frontier-reasoning/md/verify-step-by-step.md)).

**En une phrase** — Récompenser chaque étape intermédiaire du raisonnement (supervision de processus) entraîne des modèles nettement plus fiables que récompenser seulement la réponse finale (supervision de résultat).

## Ce que dit la source
Les grands modèles de langage se sont fortement améliorés sur le raisonnement multi-étapes, mais même les meilleurs commettent encore régulièrement des erreurs logiques. Pour entraîner des modèles plus fiables, on peut recourir soit à la supervision de résultat (outcome supervision), qui ne fournit un signal que sur le résultat final, soit à la supervision de processus (process supervision), qui fournit un signal sur chaque étape intermédiaire de raisonnement. Les auteurs comparent les deux et constatent que la supervision de processus surpasse significativement la supervision de résultat pour entraîner des modèles à résoudre les problèmes du jeu de données MATH, difficile. Leur modèle supervisé par processus résout 78 % d'un sous-ensemble représentatif du jeu de test MATH. Ils montrent en outre que l'apprentissage actif (active learning) améliore nettement l'efficacité de la supervision de processus. Pour soutenir la recherche, ils publient PRM800K, le jeu complet de 800 000 labels de feedback humain au niveau de l'étape.

## Pourquoi c'est utile
Ce papier introduit un Process Reward Model (PRM) qui note chaque étape de raisonnement, posant les bases de l'alignement et de l'évaluation des modèles de raisonnement. Pour des agents amenés à raisonner sur plusieurs étapes, cela offre un levier de fiabilité (détecter où le raisonnement dérape) que la simple vérification du résultat ne permet pas.

## Points clés
- **Process vs outcome supervision** : noter chaque étape de raisonnement, et non la seule réponse finale.
- La supervision de processus **surpasse significativement** la supervision de résultat sur le jeu MATH.
- Modèle PRM : **78 %** de réussite sur un sous-ensemble représentatif du test MATH.
- L'**active learning** améliore l'efficacité de la supervision de processus.
- **PRM800K** : 800 000 labels humains au niveau de l'étape, publiés pour la communauté.
- **Usage** : un PRM guide ensuite la recherche (best-of-N *vérifié*, arbre de raisonnement) ou sert à entraîner le modèle. Distinction clé : l'*Outcome Reward Model* (ORM) ne juge que le résultat et récompense parfois un raisonnement faux qui tombe juste ; le PRM donne un signal dense et localisé.
- **Coût/risque** : annotation par étape onéreuse, et risque de *reward hacking* sur le scoring intermédiaire.

## Voir aussi
- [Test-time compute](test-time-compute-thinking.md)
- [DeepSeek-R1 : le RL fait émerger le raisonnement](deepseek-r1-rl-raisonnement.md)
- [papier](../sources/frontier-reasoning/md/verify-step-by-step.md)
