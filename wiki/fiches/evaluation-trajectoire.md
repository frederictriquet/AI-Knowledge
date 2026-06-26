---
titre: "Évaluation de trajectoire"
type: "Concept"
theme: evaluation
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-evaluation
source_titre: "Qu’est-ce que l’évaluation des agents IA ?"
objectifs: [fiabilite]
---

# Évaluation de trajectoire

**En une phrase** — évaluer la suite des décisions, appels d'outils et étapes intermédiaires qu'a empruntées l'agent, pas seulement la qualité de sa réponse finale.

## En détail
Les agents génératifs « effectuent généralement des opérations plus larges et plus complexes, comme le raisonnement en plusieurs étapes, l'appel d'outils et l'interaction avec des systèmes externes ». Conséquence : « même lorsque la production finale est du texte, elle peut être le résultat d'actions intermédiaires telles que l'interrogation d'une base de données ou l'appel d'une API, chacune devant être évaluée séparément ». Dans certains cas, « l'agent ne produit pas de sortie textuelle du tout » — la réussite se mesure à la bonne exécution de la tâche. L'évaluation doit « aller au-delà de la qualité du texte en surface ». Il convient de « planifier chaque étape potentielle du workflow » et de tenir compte de « l'approche globale de l'agent tout au long du workflow, c'est-à-dire le cheminement qu'il suit pour résoudre un problème en plusieurs étapes ». Les questions clés : a-t-il choisi le bon outil, appelé la bonne fonction, transmis la bonne information dans le bon contexte, produit une réponse factuellement correcte ?

## Exemple
Le process d'éval en cinq étapes rend la trajectoire concrète. Étape 2 : on planifie *chaque* étape potentielle du workflow — appel d'API, transmission d'info à un second agent, prise de décision — pour noter chacune isolément. Étape 3 : on exécute l'agent dans plusieurs environnements, idéalement avec des LLM différents, et on surveille par exemple son usage du RAG pour récupérer une donnée externe, ou sa réponse à un appel d'API. On capture ainsi non seulement le « quoi » mais le « pourquoi » des décisions, point de départ du débogage à l'étape 5 (réécriture de prompts, ajustement d'architecture).

## Tradeoff / insight pour un senior
Le principe : décomposer le workflow en étapes individuelles et noter le cheminement, pas seulement le résultat. Compromis : c'est plus coûteux à instrumenter qu'une éval de sortie finale, mais c'est le seul moyen de diagnostiquer *pourquoi* un agent échoue (mauvais outil, mauvais contexte) et de localiser le point de défaillance dans une chaîne non déterministe.

## Source primaire
Pas de référence académique formelle — concept proche des « trajectory evaluations » de l'état de l'art.

## Voir aussi
- [taxonomie-erreurs-appel-fonction](taxonomie-erreurs-appel-fonction.md)
- [llm-as-a-judge](llm-as-a-judge.md)
- [agentops](agentops.md)
