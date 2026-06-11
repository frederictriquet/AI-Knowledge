---
titre: "Méta-prompting"
type: "Concept"
theme: prompting
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/meta-prompting
source_titre: "Qu’est-ce que le méta-prompting ?"
---

# Méta-prompting

**En une phrase** — fournir au LLM un template de raisonnement réutilisable par classe de tâches (structure et étapes), plutôt qu'un prompt jetable pour un cas unique.

## En détail
Le méta-prompting est une technique avancée qui donne au LLM un template étape par étape réutilisable pour résoudre toute une catégorie de tâches, en se concentrant sur la structure, la syntaxe et le schéma de raisonnement plutôt que sur l'instance. La technique s'ancre dans la théorie des catégories et des types : une catégorie de tâches T, une catégorie de prompts structurés P, et un foncteur de méta-prompting M qui traduit chaque tâche en son prompt en préservant la structure logique. Trois types sont distingués : fourni par l'utilisateur (template rédigé à la main), récursif (RMP, le LLM génère son propre méta-prompt en deux passes) et conducteur (un modèle orchestre des spécialistes multi-agents). Le méta-prompting s'oppose au zero-shot, au few-shot (lié aux exemples) et à la CoT (qui suscite le raisonnement sans le structurer par type). Des benchmarks sont rapportés (MATH 46,3 % avec Qwen-72B contre 42,5 % pour GPT-4 ; puzzles Python 32,7 → 45,8 % ; sonnets 62 → 79,6 %), sans référence vérifiable rattachée.

## Exemple
Pour « résoudre tout système de deux équations linéaires », le foncteur génère un prompt-template appliqué à `2x + 3y = 12` et `x - y = 4` : « En tant que prof de maths, explique étape par étape… 1 : identifier les coefficients a1,b1,c1 et a2,b2,c2 ; 2 : choisir substitution ou élimination ; 3-4 : aligner et soustraire pour supprimer une variable ; 5-6 : calculer puis réinjecter ; 7 : vérifier dans les deux équations ; 8 : synthétiser (x, y). » Changer les chiffres ne change pas la structure : le squelette de raisonnement se réutilise tel quel.

## Tradeoff / insight pour un senior
Le formalisme catégorie/foncteur est de l'habillage : l'idée opératoire est de capitaliser un squelette de raisonnement par type de problème. Gain : cohérence et réutilisabilité à l'échelle ; coût : il faut investir du savoir-faire pour écrire le template (variante fournie) ou accepter que la qualité dépende du prompt auto-généré (RMP). Le mode conducteur multiplie les appels et la puissance de calcul.

## Source primaire
Suzgun & Kalai 2024, « Meta-Prompting ».

## Voir aussi
- [Catalogue des techniques](techniques-catalogue.md)
- [Optimisation des prompts](prompt-optimization.md)
