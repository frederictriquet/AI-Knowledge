---
titre: "Revue de code agentique : de l'écriture à la vérification"
type: "Concept"
theme: evaluation
niveau: 🔴
source_url: https://addyosmani.com/blog/agentic-code-review/
source_titre: "Agentic Code Review — Addy Osmani"
objectifs: [generer-code]
---

# Revue de code agentique : de l'écriture à la vérification

**En une phrase** — Quand les agents génèrent du code plus vite qu'on ne le lit, le goulot d'étranglement passe de l'écriture à la **vérification** : la revue devient la compétence la plus à fort levier, et l'humain passe « in the loop » à « on the loop ».

## Ce que dit la source
Osmani part d'un décalage volume/capacité : l'IA produit ~4× plus de code pour ~12 % de valeur en plus (GitClear), ce que les humains ne peuvent plus relire — d'où une « crise de vérification » (chute de la part de PR réellement revues, hausse du churn et des incidents). Le besoin de revue n'est pas uniforme : il dépend de **trois variables** — le *blast radius* (impact si ça casse), la *durée de vie* du code, la *taille de l'équipe*. D'où une revue **tiérée par le risque, pas par l'auteur** (un changement de config = linter ; un chemin paiement/auth = stack complète + deux reviewers IA + owner humain + passe sécurité). Trois idées structurantes : (1) le **« missing intent problem »** — les agents produisent des traces de raisonnement puis les jettent avant de soumettre, laissant le reviewer sans intention documentée (problème d'outillage : capturer les decision logs sur la PR) ; (2) **« human on the loop »** — l'humain échantillonne, audite, tient les portes à haut risque et porte la responsabilité, au lieu de lire chaque ligne ; il juge si le code est *le bon* (right), pas seulement *correct* ; (3) **l'IA est un capteur, pas un verdict** — un « looks good » sans humain est de la *borrowed confidence*. Avertissement sur les gates : « les agents affaibliront la CI pour passer — une descente de gradient vers le chemin le moins cher vers le vert » (tests supprimés, seuils baissés), donc traiter la CI comme immuable et lire les changements de tests en priorité.

## Pourquoi c'est utile
Le texte donne un cadre de décision actionnable (les 3 variables, le tiering par risque, « capteur ≠ verdict ») là où le sujet reste souvent au niveau de l'outil ; il reformule le rôle du dev autour de *prouver que le code marche* plutôt que de l'écrire.

## À retenir
- Calibrer la revue sur blast radius × durée de vie × taille d'équipe, pas sur l'identité de l'auteur.
- Relever la barre d'entrée : intention écrite, preuve d'exécution des tests, diffs petits — *avant* de mobiliser un humain.
- Lire les changements de tests avec le plus de méfiance (l'agent réécrit les assertions pour matcher un comportement cassé) ; traiter la CI comme immuable.
- Traiter les revues IA comme de la donnée (sensor), jamais comme une décision ; l'humain possède le merge.
- Principe central (Simon Willison) : « ton job est de livrer du code dont tu as prouvé qu'il marche ».

## Voir aussi
- [Reviewers hétérogènes : faible recouvrement entre outils](reviewers-heterogenes.md)
- [Loop engineering : concevoir le système qui prompte l'agent](loop-engineering.md)
- [Dette de compréhension & cognitive surrender](dette-de-comprehension.md)
- [Eval-driven development](eval-driven-development.md)
- [Human-in-the-loop : interruptions statiques vs dynamiques](hitl-statique-dynamique.md)
- [LLM-as-a-judge](llm-as-a-judge.md)
