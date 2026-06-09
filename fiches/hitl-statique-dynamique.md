---
titre: "Human-in-the-loop : interruptions statiques vs dynamiques"
theme: gouvernance-alignement-ops
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/tutorials/human-in-the-loop-ai-agent-langraph-watsonx-ai
source_titre: "Supervision « l’humain dans la boucle » d’un agent IA de recherche d’antériorités avec LangGraph et watsonx.ai"
---

# Human-in-the-loop : interruptions statiques vs dynamiques

**En une phrase** — deux mécanismes LangGraph pour insérer un humain dans la boucle : des breakpoints prédéterminés autour d'un nœud (statiques) ou un appel `interrupt()` déclenché depuis l'intérieur d'un nœud selon l'état (dynamiques).

## En détail
**Interruptions statiques** : « modification de l'état du graphe directement à des points prédéterminés *avant ou après* l'exécution d'un nœud donné. Cette approche exige que les paramètres `interrupt_before` ou `interrupt_after` soient définis sur une liste de noms de nœuds lors de la compilation du graphe d'état » — ex. `builder.compile(interrupt_before=["assistant"], checkpointer=memory)`. La reprise se fait via `graph.update_state(...)`, qui utilise le réducteur `add_messages` (ajout ou remplacement de message selon présence d'un `id`), puis en relançant le stream (au besoin avec `None` pour simplement continuer). **Interruptions dynamiques** : « interrompre un graphe et attendre l'entrée de l'utilisateur *à partir* d'un nœud en fonction de l'état actuel du graphe. Cette approche exige l'utilisation de la fonction `interrupt` de LangGraph ». On construit un nœud `human_in_the_loop` appelant `value = interrupt('Would you like to revise the input or continue?')` ; la reprise passe par `Command(resume=...)`, qui « met à jour l'état comme s'il provenait du nœud ».

## Tradeoff / insight pour un senior
Statique = simple à câbler (liste de nœuds à la compilation) mais le point d'arrêt est figé, indépendant de l'état ; reprise par `update_state`. Dynamique = l'arrêt est conditionnel à l'état courant (on n'interrompt que si nécessaire) mais exige un nœud dédié ; reprise par `Command(resume=)`. Pattern LangGraph, pas concept IBM générique.

## Source primaire
Mécanismes du framework LangGraph (`interrupt_before`/`interrupt_after`, `interrupt()`, `Command(resume=)`), documentés par LangGraph.

## Voir aussi
- [guardrail-noeud-entree](guardrail-noeud-entree.md)
