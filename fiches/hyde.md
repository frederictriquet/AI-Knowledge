---
titre: "HyDE (Hypothetical Document Embeddings)"
theme: rag-contexte
niveau: 🟡
provenance: ➕
base: ibm-guide-agents-ia/hors-corpus
source_url: https://arxiv.org/abs/2212.10496
---

# HyDE (Hypothetical Document Embeddings)

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. Glossaire · Pertinence 🟡 tradeoff

**En une phrase** — générer une réponse *hypothétique* à la question, puis chercher les documents proches de cette réponse (et non de la question) pour améliorer la récupération zero-shot.

## L'idée
Une question et un document pertinent vivent souvent dans des zones différentes de l'espace d'embedding : la question est courte et interrogative, le document est long et affirmatif. HyDE demande d'abord au LLM de *rédiger* une réponse plausible — même partiellement fausse — puis encode ce **document hypothétique** et l'utilise comme requête vectorielle. La récupération se fait donc document-contre-document, alignant les distributions et capturant mieux la pertinence sémantique, sans aucune donnée d'entraînement étiquetée.

## Tradeoff / quand l'utiliser
Excellent en zero-shot ou sur des domaines/langues où aucun reranker n'est entraîné. Coût : un appel LLM supplémentaire avant chaque recherche (latence, prix) et un risque si l'hypothèse hallucine hors-sujet. À privilégier quand la requête brute récupère mal et qu'un fine-tuning du retriever est hors de portée.

## Source primaire
Gao et al., 2022, *Precise Zero-Shot Dense Retrieval without Relevance Labels* (HyDE), arXiv:2212.10496. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [reranking](reranking.md) (hors-corpus sœur)
- [rag-agentique](rag-agentique.md) (corpus)
