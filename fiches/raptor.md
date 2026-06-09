---
titre: "RAPTOR"
theme: rag-contexte
niveau: 🟡
provenance: ➕
base: ibm-guide-agents-ia/hors-corpus
source_url: https://arxiv.org/abs/2401.18059
---

# RAPTOR

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. Glossaire · Pertinence 🟡 tradeoff

**En une phrase** — clustering et résumés *hiérarchiques* récursifs des chunks (un arbre), permettant de récupérer à différents niveaux d'abstraction.

## L'idée
Les chunks plats ne capturent que des détails locaux : une question qui exige de relier plusieurs passages échoue. RAPTOR regroupe les chunks par similarité, résume chaque cluster avec un LLM, puis recommence sur ces résumés — construisant récursivement un **arbre** dont les feuilles sont le texte brut et les nœuds supérieurs des synthèses de plus en plus abstraites. La récupération interroge l'arbre entier : selon la question, on récupère soit un détail (feuille) soit une vue d'ensemble (nœud haut).

## Tradeoff / quand l'utiliser
Utile pour les questions multi-passages ou thématiques sur des documents longs, là où le chunking plat perd le fil. Coût : construction de l'arbre (appels LLM de résumé à l'indexation) et stockage supplémentaire. Moins lourd que GraphRAG car pas d'extraction d'entités, mais moins structuré pour les requêtes relationnelles.

## Source primaire
Sarthi et al., 2024, *RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval*, arXiv:2401.18059. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [graphrag](graphrag.md) (hors-corpus sœur)
- [strategies-de-chunking](strategies-de-chunking.md) (corpus)
