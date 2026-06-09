# Trois principes : simplicité, transparence, ACI

> Fiche **source : Anthropic — Building Effective Agents (déc. 2024)** · [post complet](../md/building-effective-agents.md) · Pertinence 🟡 tradeoff

**En une phrase** — le succès n'est pas le système le plus sophistiqué mais le *bon* système : commencer simple, mesurer, et n'ajouter de l'agentique que si le simple échoue.

## Ce que dit la source
Trois principes pour construire des agents : (1) **simplicité** de conception ; (2) **transparence** — montrer explicitement les étapes de planification de l'agent ; (3) soigner l'**ACI** (documentation et tests des outils). Sur les **frameworks** : ils accélèrent le démarrage mais ajoutent des couches d'abstraction qui masquent prompts et réponses et compliquent le debug — commencer par appeler les API LLM directement, et si l'on utilise un framework, **comprendre le code sous-jacent** (les hypothèses fausses sur « ce qu'il y a sous le capot » sont une source d'erreur fréquente). Mantra répété : ajouter de la complexité **uniquement** quand elle améliore *mesurablement* les résultats. Résumé : « commencer par des prompts simples, les optimiser par une évaluation complète, n'ajouter des systèmes agentiques multi-étapes que si les solutions simples sont insuffisantes ».

## Ce que ça ajoute vs IBM
Le contrepoids exact au biais commercial d'IBM (qui vend plateforme et complexité) : une **discipline de sobriété et de mesure**.

## À retenir
- Start simple → optimiser par l'éval → multi-étapes agentique seulement si nécessaire.
- Méfiance envers les abstractions de frameworks ; privilégier la transparence du raisonnement.

## Voir aussi
- (Prompt Report) [Le prompt engineering est empirique](../../prompt-report/concepts/prompt-engineering-est-empirique.md)
- (agents IBM) [Types d'orchestration](../../../ibm-guide-agents-ia/concepts/orchestration-types.md)
- [post complet](../md/building-effective-agents.md)
