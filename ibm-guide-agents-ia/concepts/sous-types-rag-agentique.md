# Sous-types de RAG agentique

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [64-agentic-rag](../md/64-agentic-rag.md)

**En une phrase** — quatre familles d'agents pour la RAG : routage, planification de requêtes, ReAct, et plan-and-execute.

## Ce que dit le corpus
Le corpus liste quatre types d'agents IA pouvant composer un système de RAG agentique. Les **agents de routage** déterminent quelles sources de connaissances et outils externes utiliser pour une requête ; dans un système mono-agent, l'agent de routage choisit la source à interroger. Les **agents de planification de requêtes** sont les « gestionnaires de tâches » : ils décomposent les requêtes complexes en sous-requêtes étape par étape, les envoient à d'autres agents, puis combinent leurs réponses en une réponse globale cohérente (forme d'orchestration). Les **agents ReAct** créent des solutions étape par étape, identifient les outils utiles et ajustent dynamiquement les étapes suivantes selon les résultats. Les **agents de planification et d'exécution** (plan-and-execute) sont une évolution de ReAct : ils « peuvent exécuter des workflows en plusieurs étapes sans rappeler l'agent principal, pour des coûts réduits et une meilleure efficacité ».

## Tradeoff / insight pour un senior
L'axe de décision est le coût de la réinvocation du planificateur. ReAct rappelle le raisonnement central à chaque observation (adaptatif, coûteux) ; plan-and-execute construit le plan complet une fois puis l'exécute (économe, mais aveugle aux imprévus en cours de plan). Le corpus note que comme l'agent plan-and-execute doit raisonner sur toutes les étapes d'emblée, « les taux d'achèvement et la qualité ont tendance à être plus élevés ».

## Source primaire
« Les cadres d'agents de planification et d'exécution sont une évolution des agents ReAct. Ils peuvent exécuter des workflows en plusieurs étapes sans rappeler l'agent principal. » (IBM, [agentic-rag](../md/64-agentic-rag.md))

## Voir aussi
- [RAG agentique](rag-agentique.md)
- [ReAct vs function calling](react-vs-function-calling.md)
