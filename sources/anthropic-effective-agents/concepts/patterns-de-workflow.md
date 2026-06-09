# Les 5 patterns de workflow composables (Anthropic)

> Fiche **source : Anthropic — Building Effective Agents (déc. 2024)** · [post complet](../md/building-effective-agents.md) · Pertinence 🔴 substance

**En une phrase** — un catalogue de patterns composables, du plus simple au plus complexe, à assembler soi-même plutôt qu'à déléguer à un framework.

## Ce que dit la source
Brique de base : l'**augmented LLM** (LLM + retrieval + outils + mémoire). Puis cinq patterns, par complexité croissante :
- **Prompt chaining** — découper en étapes séquentielles, chaque appel traite la sortie du précédent ; on peut insérer des « gates » (vérifications programmatiques) entre étapes. Échange latence contre exactitude.
- **Routing** — classifier l'entrée et l'aiguiller vers un traitement spécialisé (sépare les préoccupations ; ex. router les questions faciles vers Haiku, les dures vers Sonnet).
- **Parallelization** — *sectioning* (sous-tâches indépendantes en parallèle) et *voting* (lancer la même tâche N fois pour gagner en confiance ; ex. plusieurs prompts revoient un code).
- **Orchestrator-workers** — un LLM central décompose **dynamiquement**, délègue à des workers, synthétise. Différence avec la parallélisation : les sous-tâches ne sont pas prédéfinies, elles dépendent de l'entrée.
- **Evaluator-optimizer** — un LLM génère, un autre évalue et donne du feedback en boucle ; pertinent quand des critères d'évaluation clairs existent.

## Ce que ça ajoute vs IBM
Un catalogue **net et nommé**. IBM a « l'orchestration » en bloc, mais pas *parallelization-voting* ni *evaluator-optimizer* comme patterns distincts et réutilisables.

## À retenir
- Ces patterns se **combinent** ; mesurer la performance et n'ajouter de la complexité que si elle améliore le résultat.

## Voir aussi
- (prompt-eng IBM) [Prompt chaining](../../../ibm-guide-prompt-engineering/concepts/prompt-chaining.md)
- (agents IBM) [Superviseur & équipes hiérarchiques](../../../ibm-guide-agents-ia/concepts/hors-corpus/supervisor-hierarchical-teams.md) · [Mixture-of-Agents](../../../ibm-guide-agents-ia/concepts/hors-corpus/mixture-of-agents.md)
- (Prompt Report) [Techniques d'ensembling](../../prompt-report/concepts/ensembling-techniques.md)
- [post complet](../md/building-effective-agents.md)
