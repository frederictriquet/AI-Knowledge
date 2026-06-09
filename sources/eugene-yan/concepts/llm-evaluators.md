# LLM-evaluators (juges LLM) — vue d'Eugene

> Fiche **source : Eugene Yan** · [post](../md/llm-evaluators.md) · Pertinence 🟡 tradeoff

**En une phrase** — Synthèse de deux douzaines d'articles sur les LLM-as-a-Judge : quand et comment les utiliser, leurs biais connus, et comment les aligner sur des critères humains.

## Ce que dit la source
Un **LLM-evaluator** est un LLM qui juge la qualité de la réponse d'un autre LLM. Leur adoption croît par nécessité : les évals classiques (n-grammes, similarité sémantique, référence gold) distinguent mal les sorties sur des tâches ouvertes (résumé long, traduction, dialogue multi-tours). Eugene structure la décision autour de trois axes : (i) **direct scoring vs comparaison pairwise**, (ii) **métriques de corrélation vs de classification**, (iii) **API LLM vs modèle évaluateur fine-tuné**. La question préalable est le **baseline** : la cible usuelle est que la corrélation LLM-humain égale la corrélation humain-humain ; vs des annotateurs humains, un LLM-evaluator est bien plus rapide et moins cher. Il détaille des techniques de prompting (zero-shot, CoT, cross-examination « LM vs LM » pour détecter les erreurs factuelles), l'alignement sur des critères idiosyncratiques (EvalLM), et le fine-tuning d'évaluateurs (Shepherd sur llama-2-7b). Surtout, il documente les **biais** mesurés (MT-Bench / Chatbot Arena) : **position bias** (préférence pour la première position), **verbosity bias** (réponses longues préférées >90 % du temps), et **self-enhancement bias** (préférence pour ses propres sorties).

## Ce que ça ajoute vs IBM
Là où IBM présente le LLM-as-a-judge comme une technique, Eugene fournit une **revue de littérature critique** : les arbres de décision (scoring vs pairwise), les baselines à comparer, et surtout la cartographie des biais à neutraliser — la rigueur qui sépare un juge fiable d'un juge trompeur.

## Arbre de décision
Le livrable central du post est un arbre de décision (« mental model ») qui guide le choix du type d'évaluateur et de métrique. Eugene avertit que c'est une simplification utile comme point de départ.

1. **La tâche est-elle objective ou subjective ?**
   - **Objective** (factualité, toxicité, suivi d'instructions) → **direct scoring** : la meilleure réponse d'une paire peut rester défectueuse, et on n'a pas besoin d'une alternative pour comparer.
   - **Subjective** (ton, persuasion, style d'écriture) → **comparaison pairwise**, plus fiable.
2. **Si direct scoring, peut-on ramener la tâche à du binaire (vrai/faux) ?**
   - **Oui (binaire)** → métriques de classification (recall, precision) ou Cohen's κ.
   - **Non (échelle de Likert)** → corrélations : Spearman's ρ, Kendall's τ.
3. **Si comparaison pairwise** → Cohen's κ ; et si on est très confiant dans la vérité-terrain, envisager des métriques de classification (recall sur le bon choix de la paire).
4. **Évaluateur en développement, ou guardrail en production ?**
   - **Développement** (quelques centaines d'échantillons, latence/coût d'une API LLM tolérables) → prompter une API LLM avec **CoT + n-shot** pour la fiabilité.
   - **Guardrail en production** (faible latence, fort débit) → envisager de **fine-tuner un classifieur ou un reward model**, bootstrappé sur données open-source et labels collectés en interne.

## Points clés
- 3 choix : direct scoring vs pairwise ; corrélation vs classification ; API vs fine-tuné.
- Viser : corrélation LLM-humain ≈ corrélation humain-humain.
- Biais à corriger : position, verbosity, self-enhancement.
- Techniques : CoT, cross-examination, alignement sur critères (EvalLM).
- Mise en garde sur les évaluateurs **fine-tunés** : coûteux, et surtout ils se comportent comme des **classifieurs spécifiques à une tâche** (« On the Limitations of Fine-tuned Judge Models »). Ils battent gpt-4 en in-domain mais généralisent mal : changer de schéma d'évaluation (ex. d'une paire vers du direct scoring) provoque une chute catastrophique, et ils échouent sur la fairness (sous le hasard sur LLMBar), la factualité, la toxicité, la sécurité. Le fine-tuning ne vaut le coup que comme guardrail en production (faible latence/fort débit) ou quand recall/precision restent insuffisants en prompting (Shepherd, Prometheus).

## Voir aussi
- (agents IBM) [LLM-as-a-judge](../../../ibm-guide-agents-ia/concepts/llm-as-a-judge.md)
- (Hamel) [LLM-as-a-judge fait correctement](../../hamel-husain/concepts/llm-as-judge-correct.md)
- [post complet](../md/llm-evaluators.md)
