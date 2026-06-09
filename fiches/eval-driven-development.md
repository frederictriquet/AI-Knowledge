---
titre: "Eval-driven development"
theme: evaluation
niveau: 🔴
provenance: 🔗
base: sources/hamel-husain
source_url: https://hamel.dev/blog/posts/evals/
source_titre: "Your AI Product Needs Evals"
---

# Eval-driven development

> Fiche **source : Hamel Husain** · [post complet](../sources/hamel-husain/md/evals.md) · Pertinence 🔴 substance

**En une phrase** — Construire un système d'évaluation spécifique à ton domaine est la fondation d'un produit IA : c'est lui qui crée la flywheel données → évals → amélioration et débloque le reste.

## Ce que dit la source
Hamel observe que les produits LLM qui échouent partagent une cause racine : « a failure to create robust evaluation systems ». Le succès dépend de la vitesse d'itération, qui repose sur trois capacités : évaluer la qualité (tests), débugger (logging & inspecting data), et changer le système (prompt eng, fine-tuning, code) ; beaucoup ne font que la troisième et restent au stade de démo. Il décrit trois niveaux d'évaluation de coûts croissants : Level 1, des unit tests sous forme d'assertions (façon pytest), rapides et lancés à chaque changement de code ; Level 2, human & model eval reposant sur le logging des traces et le LLM-as-judge aligné sur un humain ; Level 3, l'A/B testing réservé aux produits matures. Il rejette les generic evaluation frameworks : « Don't rely on generic evaluation frameworks… create an evaluation system specific to your problem. » Le même eval system sert ensuite gratuitement au debugging et au fine-tuning (data synthesis & curation).

## Ce que ça ajoute vs IBM
Là où le guide IBM mentionne le LLM-as-a-judge et l'évaluation de trajectoire, Hamel structure une démarche complète et hiérarchisée (assertions → human/model eval → A/B testing) et insiste sur la spécificité métier des évals, dimension quasi absente du guide IBM.

## À retenir
- Investir d'abord dans les évals, pas seulement dans le prompt/fine-tuning.
- Level 1 : écrire beaucoup d'assertions scopées par feature/scenario, lancées en CI.
- Level 2 : logger les traces, les regarder, aligner le LLM-as-judge sur un humain (mesurer precision/recall, pas l'agreement brut si déséquilibré).
- Level 3 : A/B testing seulement quand le produit est mûr.
- Réutiliser l'infra d'éval pour debugging et data curation/fine-tuning.

## Voir aussi
- (agents IBM) [Évaluation de trajectoire](evaluation-trajectoire.md)
- (agents IBM) [LLM-as-a-judge](llm-as-a-judge.md)
- (Anthropic) [Pattern evaluator-optimizer](patterns-de-workflow.md)
- [post complet](../sources/hamel-husain/md/evals.md)
