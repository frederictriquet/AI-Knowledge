---
titre: "DSPy : compilation & bootstrapping"
type: "Concept"
theme: gouvernance-alignement-ops
niveau: 🔴
source_url: https://arxiv.org/abs/2310.03714
source_titre: "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines"
---

# DSPy : compilation & bootstrapping

**En une phrase** — compiler un programme DSPy, c'est laisser un teleprompter *bootstrapper* automatiquement de bonnes démonstrations en simulant le pipeline, en filtrant les traces qui passent le metric, puis en sélectionnant les meilleurs candidats — et le papier montre que ce processus fait passer des LM modestes de 4–20 % à 49–88 % d'accuracy sur GSM8K en quelques minutes.

## Ce que dit la source
**Le compilateur DSPy** optimise automatiquement n'importe quel programme via un teleprompter (unifiant prompting et finetuning). Un teleprompter typique passe par trois étapes :

- **Étape 1 — Génération de candidats.** Le compilateur trouve récursivement tous les modules `Predict` (predictors) uniques, y compris imbriqués. Pour chaque predictor, le teleprompter génère des valeurs candidates pour ses paramètres : instructions, descriptions de champs, ou — surtout — *démonstrations* (paires entrée-sortie). Cette itération de DSPy se concentre sur les démonstrations via une approche type rejection-sampling. Le teleprompter le plus simple, **BootstrapFewShot**, simule un *teacher program* (ou la version zero-shot du programme à compiler) sur des entrées d'entraînement, parfois plusieurs fois à haute température ; en mode compile, les *traces multi-étapes* sont suivies de façon thread-safe ; le metric filtre les traces qui aident le pipeline à passer, et on garde les bons exemples comme démonstrations potentielles pour toutes les signatures du programme. Constat clé : « LMs can be highly unreliable » mais sont efficaces pour chercher dans l'espace des solutions ; un programme bien décomposé trouve généralement quelques exemples passant les contraintes des signatures et metrics, ce qui permet de bootstrapper itérativement.
- **Étape 2 — Optimisation des paramètres.** Chaque paramètre a un ensemble discret de candidats. Des algorithmes d'hyperparamétrage s'appliquent pour la sélection : random search ou Tree-structured Parzen Estimators (HyperOpt, Optuna) — d'où **BootstrapFewShotWithRandomSearch** et **BootstrapFewShotWithOptuna**. Autre voie : **BootstrapFinetune**, où les démonstrations servent à mettre à jour les *poids du LM* de chaque predictor (optimisation de la qualité moyenne par cross-validation, possible même sans aucun label selon le metric).
- **Étape 3 — Optimisation d'ordre supérieur.** Modification du flux de contrôle, notamment les **ensembles** : bootstrapper plusieurs copies du programme, les exécuter en parallèle et réduire leurs prédictions (ex. vote majoritaire). Travaux futurs : bootstrapping dynamique au test-time, logique de backtracking automatique.

Compilateurs additionnels évoqués : **LabeledFewShot** (échantillonne k=8 démonstrations aléatoires du trainset) ; composition de teleprompters via un `teacher` (un programme cher avec un grand LM peut superviser un programme bon marché avec un petit LM, ou finetuner un T5).

**Résultats — GSM8K (problèmes de maths, test 1.3k).** Programmes : `vanilla` (Predict), `CoT` (ChainOfThought), `reflection` (ThoughtReflection = 5 chaînes échantillonnées comparées par MultiChainComparison). Trainset/dev = 200/300 exemples. En zero-shot (`none`), `vanilla` atteint 24.0 % (dev) / 25.2 % (test) pour GPT-3.5 et 7.0 % / 9.4 % pour Llama2-13b-chat. Compiler `vanilla` avec `bootstrap` puis `bootstrap×2` le porte à 64.7 % / 61.7 % (GPT-3.5) et 37.3 % / 36.5 % (Llama2). Le bilan du papier : **« composing the right generic modules, rather than manipulating string prompts, improves different LMs from 4–20 % accuracy to 49–88 % accuracy »**, avec des programmes composant 2 à 4 modules et teleprompters. Pour le programme CoT, le `bootstrap` égale ou dépasse les chaînes de raisonnement humaines expertes (`+human_CoT`) ; `reflection` est le meilleur. La compilation tourne en minutes à dizaines de minutes (ex. 10–20 essais sur 150–300 exemples de validation, parallélisables).

**Résultats — HotPotQA (multi-hop QA, fullwiki, retriever ColBERTv2 sur le dump Wikipedia 2017).** Métriques : answer exact match (Ans) et pair-retrieval accuracy (Psg). Le `multihop` (génère des requêtes en plusieurs « hops ») est globalement le meilleur ; `bootstrap` dépasse le fewshot (pour multihop) et le raisonnement humain expert (pour react). Compiler rend **llama2-13b-chat compétitif avec GPT-3.5**. Le compilateur `multihop_t5` (BootstrapFinetune) produit un **T5-Large (770M paramètres)** scorant **39.3 % answer EM et 46.0 % passage accuracy** sur le dev, avec seulement **200 entrées labellisées et 800 questions non labellisées**, supervisé par un teacher = ensemble de deux `multihop` Llama2-13b-chat — pour un coût d'inférence ordres de grandeur plus bas qu'un LM propriétaire.

**Synthèse chiffrée (abstract / conclusion).** Les programmes DSPy compilés dépassent le few-shot standard « generally by over 25 % » (GPT-3.5) et « 65 % » (Llama2-13b-chat), et les pipelines avec démonstrations expertes « by up to 5–46 % » (GPT-3.5) et « 16–40 % » (Llama2). Les programmes simples passent de 33 % à 82 % (GSM8K) et de 32 % à 46 % (HotPotQA) pour GPT-3.5, et de 9 % à 47 % puis 22 % à 41 % pour Llama2-13b-chat.

## Pourquoi c'est utile
Le papier fournit la mécanique en trois étapes (génération de candidats par rejection-sampling sur traces filtrées → optimisation d'hyperparamètres → optimisation d'ordre supérieur/ensembles) **et les chiffres primaires** : les sauts 4–20 % → 49–88 % sur GSM8K, le T5-770M à 39.3 % EM avec 200 labels, et la mise à niveau de Llama2-13b sur GPT-3.5.

## Points clés
- Bootstrapping = simuler le pipeline (teacher ou zero-shot), suivre les traces multi-étapes, filtrer par metric, garder les bons exemples comme démonstrations.
- Trois étapes : candidats → optimisation paramètres (random search / Optuna / finetune) → ordre supérieur (ensembles, vote majoritaire).
- GSM8K : `vanilla` zero-shot 24.0 %/7.0 % (dev GPT-3.5/Llama2) → `bootstrap×2` 64.7 %/37.3 % ; bilan global 4–20 % → 49–88 %.
- HotPotQA : `multihop` meilleur ; T5-Large 770M atteint 39.3 % EM / 46.0 % Psg avec 200 labels + 800 non labellisés.
- Compiler rend Llama2-13b-chat compétitif avec GPT-3.5 ; compilation en minutes à dizaines de minutes, parallélisable.
- Label-efficience : labels typiquement requis seulement pour la sortie finale, le reste est bootstrappé.

## Voir aussi
- [DSPy](dspy.md)
- [Le prompt engineering est empirique](prompt-engineering-est-empirique.md)
- [Eval-driven development](eval-driven-development.md)
- [DSPy : signatures, modules, optimiseurs](dspy-signatures-modules-optimiseurs.md)
- [papier complet](../sources/dspy/md/dspy-paper.md)
