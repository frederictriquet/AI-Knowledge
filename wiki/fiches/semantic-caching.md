---
titre: "Mise en cache sémantique"
type: "Concept"
theme: efficacite-cout
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/agentic-rag
source_titre: "Qu’est-ce que la RAG agentique ?"
objectifs: [couts]
---

# Mise en cache sémantique

**En une phrase** — cacher requêtes, contexte et résultats par similarité sémantique, utilisé comme mécanisme de mémoire de l'agent.

## En détail
La mise en cache sémantique s'inscrit dans la **mémoire** de l'agent, l'une de ses trois caractéristiques essentielles. Un agent dispose d'une mémoire à court et à long terme qui lui permet de planifier et d'exécuter des tâches complexes, et de se référer aux tâches précédentes pour éclairer les workflows futurs. C'est précisément dans ce rôle que s'inscrit le cache sémantique : « Les systèmes de RAG agentique utilisent la mise en cache sémantique pour stocker les ensembles de requêtes, le contexte et les résultats précédents et s'y référer. » Ce mécanisme se positionne comme le support concret de la fonction mémoire de l'agent dans un pipeline RAG agentique.

## Exemple
Un agent support a déjà traité « Comment réinitialiser mon mot de passe ? » et stocké requête + contexte + résultat dans son cache sémantique. Un autre utilisateur tape plus tard « j'ai oublié mes identifiants, comment me reconnecter ? » : aucune égalité de chaîne, mais les deux embeddings sont voisins, donc le cache renvoie la réponse pré-calculée sans relancer récupération + génération. C'est la mémoire long terme à l'œuvre : l'agent « se réfère aux tâches précédentes » pour éclairer le workflow courant et éviter de refaire le travail.

## Tradeoff / insight pour un senior
Le terme « sémantique » est ce qui distingue ce cache d'un cache clé-valeur classique : la correspondance se fait par proximité de sens (embeddings) et non par égalité exacte de la requête. Avantage : deux formulations différentes d'une même intention frappent le même cache, économisant un cycle complet de récupération + génération. Risque : un faux positif sémantique sert une réponse pré-calculée à une requête subtilement différente. Le seuil de similarité devient un paramètre critique à calibrer, exactement comme le `SIMILARITY_THRESHOLD` d'un retrieval scoré.

## Source primaire
« Les systèmes de RAG agentique utilisent la mise en cache sémantique pour stocker les ensembles de requêtes, le contexte et les résultats précédents et s'y référer. » ([agentic-rag](../sources/ibm-guide-agents-ia/md/64-agentic-rag.md))

## Voir aussi
- [RAG agentique](rag-agentique.md)
- [Sous-types de RAG agentique](sous-types-rag-agentique.md)
