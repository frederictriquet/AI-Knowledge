# Mise en cache sémantique

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [64-agentic-rag](../md/64-agentic-rag.md)

**En une phrase** — cacher requêtes, contexte et résultats par similarité sémantique, utilisé comme mécanisme de mémoire de l'agent.

## Ce que dit le corpus
Le corpus mentionne la mise en cache sémantique dans le cadre des trois caractéristiques essentielles d'un agent IA, au sein de la **mémoire**. Un agent dispose d'une mémoire à court et à long terme qui lui permet de planifier et d'exécuter des tâches complexes, et de se référer aux tâches précédentes pour éclairer les workflows futurs. C'est précisément dans ce rôle que s'inscrit le cache sémantique : « Les systèmes de RAG agentique utilisent la mise en cache sémantique pour stocker les ensembles de requêtes, le contexte et les résultats précédents et s'y référer. » Le corpus ne détaille pas davantage le mécanisme ; il le positionne comme le support concret de la fonction mémoire de l'agent dans un pipeline RAG agentique.

## Tradeoff / insight pour un senior
Le terme « sémantique » est ce qui distingue ce cache d'un cache clé-valeur classique : la correspondance se fait par proximité de sens (embeddings) et non par égalité exacte de la requête. Avantage : deux formulations différentes d'une même intention frappent le même cache, économisant un cycle complet de récupération + génération. Risque : un faux positif sémantique sert une réponse pré-calculée à une requête subtilement différente. Le seuil de similarité devient un paramètre critique à calibrer, exactement comme le `SIMILARITY_THRESHOLD` d'un retrieval scoré.

## Source primaire
« Les systèmes de RAG agentique utilisent la mise en cache sémantique pour stocker les ensembles de requêtes, le contexte et les résultats précédents et s'y référer. » (IBM, [agentic-rag](../md/64-agentic-rag.md))

## Voir aussi
- [RAG agentique](rag-agentique.md)
- [Sous-types de RAG agentique](sous-types-rag-agentique.md)
