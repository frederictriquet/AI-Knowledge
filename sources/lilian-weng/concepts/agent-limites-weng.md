# Limites structurelles des agents LLM (selon Weng)

> Fiche **source : Lilian Weng** · [post complet](../md/2023-06-23-agent.md) · Pertinence 🟡 tradeoff

**En une phrase** — les trois limites communes que Weng identifie après avoir parcouru les démonstrateurs d'agents : contexte fini, planification long-horizon fragile, et interface en langage naturel peu fiable.

## Ce que dit la source
En conclusion, Weng relève trois limitations récurrentes. **Longueur de contexte finie** : la capacité restreinte limite l'inclusion de l'historique, des instructions détaillées et du contexte des appels d'API ; les magasins vectoriels et la récupération élargissent l'accès au savoir mais leur pouvoir de représentation reste inférieur à l'attention pleine. **Difficultés de planification long terme et de décomposition** : planifier sur un long historique et explorer efficacement l'espace des solutions reste ardu ; les LLM peinent à ajuster leurs plans face à des erreurs imprévues, donc sont moins robustes que les humains qui apprennent par essai-erreur. **Fiabilité de l'interface en langage naturel** : l'agent s'appuie sur le langage naturel comme interface entre le LLM et les composants externes, mais les sorties peuvent comporter des erreurs de formatage ou un comportement « rebelle » (refus d'instruction) — d'où le fait qu'une grande part du code des démos serve au parsing des sorties.

## Ce que ça ajoute vs IBM
Weng livre une critique honnête et structurelle (trois défis nommés) qui équilibre l'enthousiasme : elle ancre les limites dans des causes techniques précises (attention finie, robustesse de planification, parsing), là où le guide IBM est plus orienté solutions.

## Sources primaires (citées par Weng)
- Weng, Lilian (Jun 2023). « LLM-powered Autonomous Agents », Lil'Log — synthèse personnelle des limites.
- AutoGPT (Significant-Gravitas) — illustration des problèmes de fiabilité de l'interface en langage naturel et du parsing.

## Voir aussi
- [Mémoire CT/LT](../../../ibm-guide-agents-ia/concepts/memoire-court-long-terme.md)
- [ReAct](../../../ibm-guide-agents-ia/concepts/react.md)
- [post complet](../md/2023-06-23-agent.md)
