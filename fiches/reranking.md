---
titre: "Reranking (cross-encoders)"
type: "Concept"
theme: rag-contexte
niveau: 🟡
source_url: https://arxiv.org/abs/1901.04085
---

# Reranking (cross-encoders)

**En une phrase** — re-classer les top-k passages récupérés avec un cross-encoder (requête et passage passent *ensemble* dans le modèle) ; le levier qualité le plus rentable en pratique, au prix de la latence.

## L'idée
La récupération vectorielle encode requête et passages *séparément* (bi-encoder), ce qui est rapide mais grossier. Un **cross-encoder** concatène requête et passage et les fait traverser ensemble le modèle : l'attention croisée juge finement la pertinence, mais empêche tout pré-calcul. On l'applique donc en second étage : le retriever ramène un large top-k (≈100), le reranker le re-trie pour ne garder que les meilleurs. ColBERT propose un compromis (late interaction) entre les deux régimes.

## Tradeoff / quand l'utiliser
Souvent le gain qualité le plus rentable d'un pipeline RAG, sans toucher au retriever ni à l'index. Coût : latence et calcul proportionnels au top-k re-scoré ; un appel par paire. À ajouter dès que la précision du top-5 final compte.

## Source primaire
Nogueira & Cho, 2019, *Passage Re-ranking with BERT*, arXiv:1901.04085 *(arXiv vérifié — HTTP 200 + titre)* ; ColBERT (Khattab & Zaharia, 2020) ; Cohere Rerank (produit).

## Voir aussi
- [hyde](hyde.md)
- [rag-agentique](rag-agentique.md)
