---
titre: "LATS (Language Agent Tree Search)"
type: "Concept"
theme: raisonnement-planification
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/topics/agentic-reasoning
source_titre: "Qu’est-ce que le raisonnement agentique ?"
---

# LATS (Language Agent Tree Search)

**En une phrase** — appliquer la recherche arborescente Monte Carlo (MCTS) au raisonnement d'un agent LLM, en mémorisant les autoréflexions pour guider l'exploration.

## En détail
LATS est un exemple d'autoréflexion partageant des similitudes avec le raisonnement par arbre de pensées dans les LLM. Il s'inspire de l'apprentissage par renforcement Monte Carlo : la recherche arborescente Monte Carlo est adaptée aux agents basés sur LLM. LATS construit un arbre de décision où un état est un nœud et une action une branche, parcourt l'arbre pour les options d'action possibles et fait appel à un évaluateur d'état pour choisir une action. Il intègre une étape d'autoréflexion combinant ses propres observations et les commentaires d'un modèle de langage pour identifier les erreurs et proposer des alternatives ; erreurs et réflexions sont stockées en mémoire comme contexte ultérieur. LATS excelle sur des tâches complexes (codage, QA interactif, recherche/navigation web) mais est plus gourmand en ressources et plus lent que ReAct.

## Tradeoff / insight pour un senior
LATS achète de la qualité sur tâches difficiles au prix d'une explosion du coût : MCTS multiplie les rollouts, et l'étape d'autoréflexion ajoute encore des appels LLM. C'est l'option « lourde » du spectre de raisonnement — pertinente quand l'exactitude prime sur la latence et le budget tokens, à proscrire pour du temps réel.

## Quand l'utiliser (et comment)
LATS n'a de sens que si **les trois** conditions sont réunies : (1) le coût d'une erreur dépasse de loin celui d'un appel LLM — tu acceptes de « cramer » des dizaines d'appels pour fiabiliser un résultat ; (2) **tu sais évaluer un état intermédiaire** via un signal objectif (tests qui passent, compilateur, vérificateur, ou un LLM-juge crédible) — sans cette boussole, MCTS explore à l'aveugle et n'apporte rien ; (3) le problème **se décompose en étapes avec branchements** où une mauvaise décision précoce condamne la suite (résolution de bug, navigation web, preuve formelle).

Faute de ces conditions, on reste plus bas sur l'échelle de complexité — `1 appel → CoT → Self-Consistency → ReAct → Reflexion → … → LATS`. Dans l'immense majorité des cas, [Self-Consistency](self-consistency.md) (N essais + vote) ou [Reflexion](reflexion.md) (réessai après critique de l'échec) donnent 80 % du bénéfice pour une fraction de la complexité. LATS est le dernier recours, quand on a vraiment besoin du backtracking sur un arbre persistant.

Côté implémentation : **ne jamais réécrire MCTS soi-même.** Les 4 étapes (sélection UCT, expansion, simulation, rétropropagation) sont délicates et déjà résolues — **LangGraph** (tutoriel LATS quasi clé-en-main) et **LlamaIndex** (`LATSAgentWorker`) fournissent l'algorithme. Ce que tu apportes se limite à trois fonctions : la **génération des actions candidates**, l'**évaluation d'un nœud** (le juge/vérificateur), et l'**exécution d'une action** dans l'environnement. L'arbre, le compromis exploration/exploitation et le backtracking sont du ressort du framework — pas du tien, et surtout pas du LLM, qui n'est appelé que comme composant (acteur, juge, critique).

## Source primaire
« Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models », arXiv, 6 juin 2024.

## Voir aussi
- [Autoréflexion / Reflexion](reflexion.md)
- [Tree of Thoughts (ToT)](tree-of-thoughts.md)
- [ReAct](react.md)
