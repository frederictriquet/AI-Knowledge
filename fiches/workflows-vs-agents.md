---
titre: "Workflows vs agents : la distinction architecturale d'Anthropic"
type: "Concept"
theme: fondamentaux-agents
niveau: 🔴
source_url: https://www.anthropic.com/engineering/building-effective-agents
source_titre: "Building effective agents"
---

# Workflows vs agents : la distinction architecturale d'Anthropic

**En une phrase** — distinguer **workflows** (LLM et outils orchestrés par des chemins de code prédéfinis) et **agents** (le LLM dirige dynamiquement son propre processus), au lieu de tout appeler « agentique ».

## Ce que dit la source
On regroupe tout sous « systèmes agentiques », mais une distinction nette s'impose : un **workflow** suit des chemins de code prédéfinis ; un **agent** garde le contrôle de *comment* il accomplit la tâche (il planifie, choisit ses outils, boucle sur le feedback de l'environnement). Recommandation centrale : chercher la solution la plus simple et n'ajouter de la complexité que si elle améliore *mesurablement* le résultat — souvent, optimiser un seul appel LLM (retrieval + exemples en contexte) suffit. Les systèmes agentiques échangent **latence et coût** contre de la performance ; les agents sont à réserver aux problèmes ouverts où l'on ne peut pas coder un chemin fixe, dans des environnements de confiance.

## Pourquoi c'est utile
La distinction fournit un **critère de décision** explicite et un avertissement anti-hype : beaucoup d'applications n'ont pas besoin d'un agent, et opposer workflow et agent évite de sur-complexifier par défaut.

## À retenir
- Workflow = prévisibilité/cohérence (tâches bien définies) ; agent = flexibilité/décision pilotée par le modèle, à l'échelle.
- Autonomie = coûts plus élevés et **erreurs cumulées** → tester en sandbox, garde-fous, condition d'arrêt (max d'itérations).

## Voir aussi
- [Cadre canonique de l'agent](agent-architecture-canonique.md)
- [Types d'orchestration](orchestration-types.md) · [ReAct](react.md)
- [post complet](../sources/anthropic-effective-agents/md/building-effective-agents.md)
