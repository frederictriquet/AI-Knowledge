---
titre: "Limites structurelles des agents LLM (selon Weng)"
type: "Concept"
theme: fondamentaux-agents
niveau: 🟡
source_url: https://lilianweng.github.io/posts/2023-06-23-agent/
source_titre: "LLM Powered Autonomous Agents"
---

# Limites structurelles des agents LLM (selon Weng)

**En une phrase** — les trois limites communes que Weng identifie après avoir parcouru les démonstrateurs d'agents : contexte fini, planification long-horizon fragile, et interface en langage naturel peu fiable.

## Ce que dit la source
En conclusion, Weng relève trois limitations récurrentes. **Longueur de contexte finie** : la capacité restreinte limite l'inclusion de l'historique, des instructions détaillées et du contexte des appels d'API ; les magasins vectoriels et la récupération élargissent l'accès au savoir mais leur pouvoir de représentation reste inférieur à l'attention pleine. **Difficultés de planification long terme et de décomposition** : planifier sur un long historique et explorer efficacement l'espace des solutions reste ardu ; les LLM peinent à ajuster leurs plans face à des erreurs imprévues, donc sont moins robustes que les humains qui apprennent par essai-erreur. **Fiabilité de l'interface en langage naturel** : l'agent s'appuie sur le langage naturel comme interface entre le LLM et les composants externes, mais les sorties peuvent comporter des erreurs de formatage ou un comportement « rebelle » (refus d'instruction) — d'où le fait qu'une grande part du code des démos serve au parsing des sorties.

## Exemple
ChemCrow (Bran et al. 2023) illustre la fragilité de l'évaluation par LLM, corollaire de l'interface peu fiable : une évaluation menée par GPT-4 lui-même juge GPT-4 et ChemCrow quasi équivalents, alors que des chimistes experts jugeant la justesse chimique réelle voient ChemCrow surclasser nettement GPT-4. Sans l'expertise du domaine, le LLM ne perçoit pas ses propres failles et ne peut juger la correction. Côté planification long-horizon, l'agent de Boiko et al. enchaîne bien quatre étapes pour « concevoir un anticancéreux » mais sans robustesse face aux erreurs imprévues.

## Pourquoi c'est utile
Weng livre une critique honnête et structurelle (trois défis nommés) qui équilibre l'enthousiasme : elle ancre les limites dans des causes techniques précises (attention finie, robustesse de planification, parsing), avec une orientation diagnostic plutôt que solutions.

## Sources primaires (citées par Weng)
- Weng, Lilian (Jun 2023). « LLM-powered Autonomous Agents », Lil'Log — synthèse personnelle des limites.
- AutoGPT (Significant-Gravitas) — illustration des problèmes de fiabilité de l'interface en langage naturel et du parsing.

## Voir aussi
- [Mémoire CT/LT](memoire-court-long-terme.md)
- [ReAct](react.md)
- [post complet](../sources/lilian-weng/md/2023-06-23-agent.md)
