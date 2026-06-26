---
titre: "LLM-as-a-judge : le faire correctement"
type: "Concept"
theme: evaluation
tags: [evaluation, llm-judge, alignement]
niveau: 🔴
source_url: https://hamel.dev/blog/posts/llm-judge/
source_titre: "Using LLM-as-a-Judge For Evaluation: A Complete Guide — Hamel Husain"
objectifs: [fiabilite]
---

# LLM-as-a-judge : le faire correctement

**En une phrase** — Un LLM-as-a-judge n'a de valeur que s'il est aligné sur le jugement binaire pass/fail d'un expert métier via un protocole itératif (« Critique Shadowing »), pas via des scores 1-5 arbitraires.

## Ce que dit la source
Les équipes se noient sous des metrics ingérables : trop de mesures, des échelles non calibrées (1-5), l'absence de domain expert et des metrics non validées. La solution proposée est le **Critique Shadowing**, un processus en 7 étapes : (1) trouver *le* **Principal Domain Expert**, (2) créer un dataset diversifié (features, scenarios, personas), (3) faire émettre par l'expert des jugements **binaires pass/fail accompagnés d'une critique** écrite expliquant le raisonnement, (4) corriger les erreurs trouvées, (5) construire le **LLM judge** itérativement avec des **few-shot** issus des critiques de l'expert, (6) mener une **error analysis** par dimension et root cause, (7) créer des juges spécialisés si nécessaire. On itère le prompt jusqu'à **convergence** avec l'expert (chez Honeycomb : > 90 % d'agreement en seulement trois itérations). Point clé revendiqué : la vraie valeur ne vient pas du juge lui-même mais du fait de regarder ses données de près.

## Exemple
Scénario d'éval B2C : l'utilisateur demande « Où est ma commande ? » alors qu'il a trois commandes actives (#123, #124, #125) — l'assistant doit désambiguïser plutôt que supposer. L'expert métier juge la réponse **pass/fail** et écrit d'abord une critique (« n'a pas demandé quel numéro, a supposé la plus récente »), qui devient ensuite un few-shot du prompt du juge. On itère le prompt jusqu'à convergence avec l'expert : chez Honeycomb, > 90 % d'accord juge/humain est atteint en seulement trois itérations. Le verdict reste binaire — pas d'échelle 1-5, jugée non actionnable.

## Pourquoi c'est utile
Ce guide fournit le protocole rigoureux complet (7 étapes, rôle de l'expert, critique-puis-note, mesure d'accord juge/humain), ce qui transforme une idée en pratique d'ingénierie reproductible.

## À retenir
- **Aligner le juge sur des labels humains** : tout part des jugements du Principal Domain Expert, pas de metrics génériques.
- **Critique-puis-note** : écrire d'abord une critique détaillée, puis le verdict ; ces critiques servent de few-shot examples pour le prompt du juge.
- **Binaire plutôt que Likert** : pass/fail seulement au départ ; les échelles 1-5 sont non actionnables et corrèlent mal au jugement de l'expert.
- **Mesurer l'accord juge/humain** : utiliser precision/recall (et non l'agreement brut, trompeur en cas de classes déséquilibrées) ; viser la convergence (ex. > 90 % d'agreement en 3 itérations).
- **Itérer** : raffiner le prompt à la main jusqu'à convergence, ré-évaluer à chaque changement matériel (ex. changement de modèle).
- **« Benevolent dictator »** : un seul expert décisionnaire pour garantir la cohérence, jamais un proxy de complaisance.
- **~30 exemples** pour démarrer, jusqu'à ne plus voir de nouveaux failure modes.
- **Error analysis** : taux d'erreur par feature/scenario/persona, classification des root causes, sur données non vues uniquement.
- Le juge n'est qu'un « hack » : la valeur réelle vient de l'analyse attentive des données.

## Voir aussi
- [LLM-as-a-judge](llm-as-a-judge.md)
- [Techniques d'auto-critique](self-criticism-techniques.md)
- [error analysis](error-analysis.md)
- [post complet](../sources/hamel-husain/md/llm-judge.md)
- [Eugene Yan — LLM-evaluators](llm-evaluators.md) (complémentaire — *choisir/évaluer* un juge)
