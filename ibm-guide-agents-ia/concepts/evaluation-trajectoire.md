# Évaluation de trajectoire

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🔴 substance · Provenance ✅ présent · Sources corpus : [60-ai-agent-evaluation](../md/60-ai-agent-evaluation.md)

**En une phrase** — évaluer la suite des décisions, appels d'outils et étapes intermédiaires qu'a empruntées l'agent, pas seulement la qualité de sa réponse finale.

## Ce que dit le corpus
Le fichier 60 insiste sur le fait que les agents génératifs « effectuent généralement des opérations plus larges et plus complexes, comme le raisonnement en plusieurs étapes, l'appel d'outils et l'interaction avec des systèmes externes ». Conséquence : « même lorsque la production finale est du texte, elle peut être le résultat d'actions intermédiaires telles que l'interrogation d'une base de données ou l'appel d'une API, chacune devant être évaluée séparément ». Dans certains cas, « l'agent ne produit pas de sortie textuelle du tout » — la réussite se mesure à la bonne exécution de la tâche. L'évaluation doit « aller au-delà de la qualité du texte en surface ». Le corpus demande de « planifier chaque étape potentielle du workflow » et de tenir compte de « l'approche globale de l'agent tout au long du workflow, c'est-à-dire le cheminement qu'il suit pour résoudre un problème en plusieurs étapes ». Les questions clés posées : a-t-il choisi le bon outil, appelé la bonne fonction, transmis la bonne information dans le bon contexte, produit une réponse factuellement correcte ?

## Tradeoff / insight pour un senior
IBM ne nomme pas « évaluation de trajectoire » mais en décrit le principe : décomposer le workflow en étapes individuelles et noter le cheminement, pas seulement le résultat. Compromis : c'est plus coûteux à instrumenter qu'une éval de sortie finale, mais c'est le seul moyen de diagnostiquer *pourquoi* un agent échoue (mauvais outil, mauvais contexte) et de localiser le point de défaillance dans une chaîne non déterministe.

## Source primaire
Non citée par IBM — la page expose le principe sans référence académique (concept proche des « trajectory evaluations » de l'état de l'art, hors-corpus).

## Voir aussi
- [taxonomie-erreurs-appel-fonction](taxonomie-erreurs-appel-fonction.md)
- [llm-as-a-judge](llm-as-a-judge.md)
- [agentops](agentops.md)
