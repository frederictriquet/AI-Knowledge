---
titre: "Les 5 patterns de workflow composables (Anthropic)"
theme: fondamentaux-agents
niveau: 🔴
source_url: https://www.anthropic.com/engineering/building-effective-agents
source_titre: "Building effective agents"
---

# Les 5 patterns de workflow composables (Anthropic)

**En une phrase** — un catalogue de patterns composables, du plus simple au plus complexe, à assembler soi-même plutôt qu'à déléguer à un framework.

## Ce que dit la source
Brique de base : l'**augmented LLM** (LLM + retrieval + outils + mémoire). Puis cinq patterns, par complexité croissante :
- **Prompt chaining** — découper en étapes séquentielles, chaque appel traite la sortie du précédent ; on peut insérer des « gates » (vérifications programmatiques) entre étapes. Échange latence contre exactitude.
- **Routing** — classifier l'entrée et l'aiguiller vers un traitement spécialisé (sépare les préoccupations ; ex. router les questions faciles vers Haiku, les dures vers Sonnet).
- **Parallelization** — *sectioning* (sous-tâches indépendantes en parallèle) et *voting* (lancer la même tâche N fois pour gagner en confiance ; ex. plusieurs prompts revoient un code).
- **Orchestrator-workers** — un LLM central décompose **dynamiquement**, délègue à des workers, synthétise. Différence avec la parallélisation : les sous-tâches ne sont pas prédéfinies, elles dépendent de l'entrée.
- **Evaluator-optimizer** — un LLM génère, un autre évalue et donne du feedback en boucle ; pertinent quand des critères d'évaluation clairs existent.

## Pourquoi c'est utile
Un catalogue **net et nommé** de patterns composables : *parallelization-voting* et *evaluator-optimizer* y sont des patterns distincts et réutilisables, souvent absents des présentations généralistes de l'orchestration.

## À retenir
- Ces patterns se **combinent** ; mesurer la performance et n'ajouter de la complexité que si elle améliore le résultat.

## Voir aussi
- [Prompt chaining](prompt-chaining.md)
- [Structures multi-agents](structures-multi-agents.md) · [Mixture-of-Agents](mixture-of-agents.md)
- [Techniques d'ensembling](ensembling-techniques.md)
- [post complet](../sources/anthropic-effective-agents/md/building-effective-agents.md)
