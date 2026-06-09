---
titre: "Tool retrieval (RAG sur les outils)"
theme: evaluation
niveau: 🟡
source_url: https://arxiv.org/abs/2305.15334
---

# Tool retrieval (RAG sur les outils)

**En une phrase** — quand on a des centaines d'outils, en **récupérer dynamiquement** un sous-ensemble pertinent par requête au lieu de tous les exposer dans le prompt.

## L'idée
Mettre des centaines de définitions d'outils dans le contexte sature la fenêtre, fait grimper le coût et **dégrade la sélection** (le modèle se trompe d'outil). Le tool retrieval traite le catalogue d'outils comme une base à indexer : à chaque requête, un retriever (embeddings sur la description des API) **récupère** les quelques outils les plus pertinents, qui seuls sont présentés au modèle. Gorilla applique cette idée à un appel d'API massif, en couplant le LLM à un retriever de documentation pour réduire les hallucinations d'API et suivre les changements de signature.

## Tradeoff / quand l'utiliser
Indispensable au-delà de quelques dizaines d'outils. Avantage : prompt court, sélection plus fiable, catalogue extensible. Contrepartie : un **étage de retrieval** à maintenir, et le risque qu'un outil pertinent soit écarté par un mauvais score de récupération.

## Source primaire
Patil et al., 2023, *Gorilla: Large Language Model Connected with Massive APIs*, arXiv:2305.15334 *(arXiv vérifié — HTTP 200 + titre)*.

## Voir aussi
- [tool-calling](tool-calling.md)
- [sous-types-rag-agentique](sous-types-rag-agentique.md)
