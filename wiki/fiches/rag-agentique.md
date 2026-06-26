---
titre: RAG agentique
type: "Concept"
theme: rag-contexte
tags: [rag, agents, recuperation]
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/agentic-rag
source_titre: "Qu'est-ce que la RAG agentique ? — IBM Think"
---

# RAG agentique

**En une phrase** — un agent placé devant la récupération qui décide s'il faut chercher, où chercher, reformule et itère, au lieu d'un pipeline RAG réactif fixe.

## En détail
La RAG agentique consiste à insérer un ou plusieurs agents IA dans le pipeline RAG pour en améliorer l'adaptabilité et la précision. Elle s'oppose point par point à la RAG traditionnelle : flexibilité (plusieurs bases de connaissances et outils externes, là où le RAG standard connecte un LLM à un seul jeu de données), adaptabilité, exactitude (les agents peuvent itérer pour optimiser leurs résultats, valider et corriger, ce que le RAG réactif ne fait pas), évolutivité et multimodalité. Métaphore : le RAG traditionnel est un employé qui exécute des tâches explicites sans initiative ; la RAG agentique est une équipe proactive qui prend des initiatives. La RAG agentique fait appel à la capacité des agents à planifier et exécuter des sous-tâches.

## RAG classique vs agentique, décision par décision
Le RAG classique est un **pipeline figé** (une passe : recherche → injection → réponse) ; l'agentique place un **agent** devant la récupération, qui devient un outil qu'il pilote :

| Décision | RAG classique | RAG agentique |
|---|---|---|
| Faut-il chercher ? | toujours | **l'agent décide** (peut répondre directement) |
| Où chercher ? | 1 source fixe | **route** vers la bonne source (plusieurs bases, web, API) |
| La requête | la question brute | **reformule / décompose** en sous-requêtes |
| Résultats faibles | génère quand même | **évalue, rejette, ré-essaie** (cf. [corrective RAG](corrective-rag.md)) |
| Nombre de passes | 1 | **itère** jusqu'à satisfaction |

Exemple parlant — *« Compare le CA 2023 de nos filiales France et Allemagne »* : le RAG classique fait une recherche sur la phrase entière → passages mêlés, réponse approximative ; l'agentique **décompose** en deux récupérations ciblées (`CA France`, `CA Allemagne`), vérifie les deux chiffres, puis compare.

## Exemple
La source illustre la version multi-agent par un système de recherche spécialisée : « un agent consulte des bases de données externes tandis qu'un autre peut parcourir les e-mails et les résultats du Web ». Chaque agent de recherche est dédié à un domaine ou un type de source, et un agent de routage choisit lequel solliciter selon la requête. Pour une question d'entreprise mêlant données propriétaires et actualité, l'un interroge le data store interne, l'autre va chercher sur le Web ; leurs retours sont fusionnés là où le RAG classique se serait limité à son unique base.

## Tradeoff / insight pour un senior
Ce n'est « pas toujours la meilleure option ». Plus d'agents = plus de tokens, plus de latence (le LLM met du temps à générer), plus de risques de collaboration défaillante, et l'hallucination n'est jamais entièrement éliminée. Réserve-la aux cas nécessitant l'interrogation de plusieurs sources ; pour une source unique et des requêtes simples, le surcoût agentique n'est pas justifié.

## Source primaire
« Bien que la RAG agentique optimise les résultats grâce à l'appel de fonctions, au raisonnement à plusieurs étapes et aux systèmes multi-agents, il ne s'agit pas toujours de la meilleure option. » ([source](../sources/ibm-guide-agents-ia/md/64-agentic-rag.md))

## Voir aussi
- [Sous-types de RAG agentique](sous-types-rag-agentique.md)
- [Mise en cache sémantique](semantic-caching.md)
- [Corrective RAG (cRAG)](corrective-rag.md)
