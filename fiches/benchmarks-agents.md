---
titre: "Benchmarks d'agents & de LLM (référence)"
theme: benchmarks
niveau: 🟡
source_url: https://arxiv.org/abs/2310.06770---

# Benchmarks d'agents & de LLM (référence)

> Compilé depuis les papiers sources (liens ci-dessous).
> Pour chaque benchmark : ce qu'il mesure, comment, le constat marquant (scores rapportés fidèlement).
>
> NOTE de sourcing : seul WebArena disposait d'un rendu HTML arXiv complet (extrait intégral). Pour SWE-bench, τ-bench et GAIA, le rendu HTML arXiv était indisponible (404) ou tronqué ; les constats ci-dessous proviennent donc de l'abstract officiel (et, pour eux, seuls les chiffres présents dans l'abstract sont rapportés).

## SWE-bench

- **Mesure** : la capacité d'un modèle à résoudre de vrais bugs/issues de logiciel — l'ingénierie logicielle réelle comme banc d'essai, bien au-delà de la simple génération de code.
- **Méthode** : cadre d'évaluation de **2 294 problèmes** d'ingénierie logicielle tirés de vraies issues GitHub et de leurs pull requests, sur **12 dépôts Python** populaires. On fournit au modèle une base de code + la description d'une issue à résoudre ; le modèle doit éditer la base de code pour corriger le problème. Résoudre une issue exige souvent de coordonner des changements à travers plusieurs fonctions, classes et fichiers, d'interagir avec des environnements d'exécution et de traiter des contextes extrêmement longs.
- **Constat** : les modèles propriétaires de pointe comme le modèle affiné des auteurs (SWE-Llama) ne résolvent que les issues les plus simples. **Le meilleur modèle, Claude 2, ne résout que 1,96 % des issues.** (Chiffres de l'abstract original ; les classements ont fortement évolué depuis.)
- Source : https://arxiv.org/abs/2310.06770

## τ-bench

- **Mesure** : l'interaction **agent–outil–utilisateur** — capacité d'un agent à dialoguer avec un utilisateur humain et à respecter des règles métier (policy) propres à un domaine. Deux dimensions ignorées par les benchmarks classiques mais vitales en production.
- **Méthode** : conversations dynamiques entre un utilisateur (simulé par un LLM) et un agent doté d'**outils API** et de **directives de politique** propres au domaine. L'évaluation compare l'**état final de la base de données** à l'état-cible annoté (évaluation fidèle et efficace). Nouvelle métrique **pass^k** pour mesurer la **fiabilité** du comportement sur plusieurs essais.
- **Constat** : même des agents de pointe à appel de fonctions (comme gpt-4o) réussissent **moins de 50 % des tâches**, et sont très **incohérents** : **pass^8 < 25 % dans le domaine retail**. Le besoin pointé est celui d'agents capables d'agir de façon cohérente et de suivre les règles de manière fiable.
- Source : https://arxiv.org/abs/2406.12045

## GAIA

- **Mesure** : les capacités d'un **assistant IA généraliste** — raisonnement, multi-modalité, navigation web, et maîtrise de l'usage d'outils. Questions « conceptuellement simples pour un humain mais difficiles pour les IA ».
- **Méthode** : **466 questions** réelles avec leur réponse. Les réponses de **300 d'entre elles** sont gardées secrètes pour alimenter un leaderboard. La philosophie inverse la tendance des benchmarks : viser des tâches faciles pour l'humain plutôt que toujours plus dures.
- **Constat** : **les humains répondent correctement à 92 % des questions, contre 15 % pour GPT-4 équipé de plugins.** Cet écart contraste avec la tendance des LLM à dépasser les humains sur des tâches expertes (droit, chimie). Les auteurs posent que l'AGI dépend de la capacité à atteindre une robustesse comparable à celle de l'humain moyen sur ces questions.
- Source : https://arxiv.org/abs/2311.12983

## WebArena

- **Mesure** : la capacité d'agents guidés par le langage à accomplir des **tâches web réalistes et long-horizon**, évaluées sur la **correction fonctionnelle** du résultat (pas sur la similarité de surface).
- **Méthode** : un environnement web **hautement réaliste et reproductible** composé de sites pleinement fonctionnels sur **quatre domaines** (e-commerce, forum social, développement logiciel collaboratif, gestion de contenu), enrichi d'outils (ex. une carte) et de bases de connaissances externes (ex. manuels, Wikipédia). Le benchmark compte **812 tâches** (intents) instanciées à partir de **241 templates** (en moyenne 3,3 exemples par template). Les agents de base testés intègrent des techniques récentes comme « raisonner avant d'agir ».
- **Constat** : résoudre des tâches complexes reste difficile. **Le meilleur agent à base de GPT-4 n'atteint qu'un taux de réussite end-to-end de 14,41 %**, très loin de la **performance humaine de 78,24 %** (GPT-3.5 : 6,41 %). Résultat qui souligne le besoin d'agents robustes.
- Source : https://arxiv.org/abs/2307.13854

## Synthèse transversale

| Benchmark   | Domaine                          | Tâches  | Meilleur agent rapporté | Humain |
|-------------|----------------------------------|---------|-------------------------|--------|
| SWE-bench   | Bugs GitHub réels (code)         | 2 294   | Claude 2 : 1,96 %       | —      |
| τ-bench     | Agent–outil–utilisateur (règles) | —       | gpt-4o : < 50 %         | —      |
| GAIA        | Assistant généraliste            | 466     | GPT-4+plugins : 15 %    | 92 %   |
| WebArena    | Tâches web long-horizon          | 812     | GPT-4 : 14,41 %         | 78,24 %|

Constante : sur des tâches **réalistes, longues et outillées**, les agents de pointe restent **très en deçà de l'humain** — l'écart est le message central de chacun de ces papiers.

## Voir aussi

- (agents IBM) [Évaluation de trajectoire](evaluation-trajectoire.md) · (Hamel) [Eval-driven development](eval-driven-development.md)
