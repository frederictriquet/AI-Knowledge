---
titre: "GraphRAG"
type: "Concept"
theme: rag-contexte
niveau: 🔴
source_url: https://arxiv.org/abs/2404.16130
---

# GraphRAG

**En une phrase** — construire un graphe de connaissances et des résumés de communautés à partir du corpus, pour répondre aux questions *globales* que le RAG vectoriel échoue à traiter.

## L'idée
Le RAG vectoriel récupère quelques chunks proches de la requête : parfait pour une question factuelle locale, inutile pour « quels sont les grands thèmes de ce corpus ? ». GraphRAG extrait d'abord entités et relations avec un LLM pour bâtir un **knowledge graph**, détecte des **communautés** (clustering hiérarchique type Leiden), puis pré-génère un résumé par communauté. À la requête, ces résumés sont agrégés en une réponse globale (map-reduce). On passe d'une récupération par similarité à une récupération par *structure* du corpus.

## Exemple
Sur un corpus de podcasts (1 669 chunks de 600 tokens, ~1 M tokens), GraphRAG extrait un graphe de 8 564 nœuds / 20 691 arêtes, hiérarchisé en communautés (34 résumés racine C0, jusqu'à 1 310 feuilles C3). Face à une question globale type « Quels épisodes traitent surtout de politique tech et de régulation ? », il gagne 72–83 % des duels en exhaustivité et 75–82 % en diversité contre le RAG vectoriel (p<.001). Les résumés racine C0 répondent avec 97 % de tokens en moins (26 657 vs 1 014 611) qu'un résumé du texte source brut.

## Tradeoff / quand l'utiliser
Indispensable pour la synthèse globale et l'exploration de gros corpus thématiques. Coût d'indexation élevé : nombreux appels LLM pour extraire le graphe et résumer les communautés, plus une maintenance à chaque mise à jour. Surdimensionné pour du simple Q&A factuel.

## Source primaire
Edge et al., 2024 (Microsoft Research), *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*, arXiv:2404.16130. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [raptor](raptor.md)
- [rag-agentique](rag-agentique.md)
