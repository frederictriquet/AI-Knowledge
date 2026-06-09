# Méta-prompting

> Fiche du [glossaire prompting](../GLOSSAIRE-PROMPTING.md) · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [../md/07-meta-prompting.md](../md/07-meta-prompting.md)

**En une phrase** — fournir au LLM un template de raisonnement réutilisable par classe de tâches (structure et étapes), plutôt qu'un prompt jetable pour un cas unique.

## Ce que dit le corpus
IBM définit le méta-prompting comme une technique avancée qui donne au LLM un template étape par étape réutilisable pour résoudre toute une catégorie de tâches, en se concentrant sur la structure, la syntaxe et le schéma de raisonnement plutôt que sur l'instance. Le corpus l'ancre dans la théorie des catégories et des types : une catégorie de tâches T, une catégorie de prompts structurés P, et un foncteur de méta-prompting M qui traduit chaque tâche en son prompt en préservant la structure logique. Trois types sont distingués : fourni par l'utilisateur (template rédigé à la main), récursif (RMP, le LLM génère son propre méta-prompt en deux passes) et conducteur (un modèle orchestre des spécialistes multi-agents). IBM oppose le méta-prompting au zero-shot, au few-shot (lié aux exemples) et à la CoT (qui suscite le raisonnement sans le structurer par type). Des benchmarks sont cités (MATH 46,3 % avec Qwen-72B contre 42,5 % pour GPT-4 ; puzzles Python 32,7 → 45,8 % ; sonnets 62 → 79,6 %) mais sans référence vérifiable dans le fichier.

## Tradeoff / insight pour un senior
Le formalisme catégorie/foncteur est de l'habillage : l'idée opératoire est de capitaliser un squelette de raisonnement par type de problème. Gain : cohérence et réutilisabilité à l'échelle ; coût : il faut investir du savoir-faire pour écrire le template (variante fournie) ou accepter que la qualité dépende du prompt auto-généré (RMP). Le mode conducteur multiplie les appels et la puissance de calcul.

## Source primaire
Non citée par IBM (notes [1]–[2] non résolues) — voir Suzgun & Kalai 2024, « Meta-Prompting » (hors-corpus). N'invente aucune référence.

## Voir aussi
- [Catalogue des techniques](techniques-catalogue.md)
- [Optimisation des prompts](prompt-optimization.md)
