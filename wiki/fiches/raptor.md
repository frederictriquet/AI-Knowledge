---
titre: "RAPTOR"
type: "Concept"
theme: rag-contexte
niveau: 🟡
source_url: https://arxiv.org/abs/2401.18059
---

# RAPTOR

**En une phrase** — clustering et résumés *hiérarchiques* récursifs des chunks (un arbre), permettant de récupérer à différents niveaux d'abstraction.

## L'idée
Les chunks plats ne capturent que des détails locaux : une question qui exige de relier plusieurs passages échoue. RAPTOR regroupe les chunks par similarité, résume chaque cluster avec un LLM, puis recommence sur ces résumés — construisant récursivement un **arbre** dont les feuilles sont le texte brut et les nœuds supérieurs des synthèses de plus en plus abstraites. La récupération interroge l'arbre entier : selon la question, on récupère soit un détail (feuille) soit une vue d'ensemble (nœud haut).

## Exemple
Le clustering n'est pas k-means mais un **soft clustering par Gaussian Mixture Models** : UMAP réduit la dimension des embeddings, fait varier `n_neighbors` pour dégager d'abord des clusters globaux puis locaux, et un nœud peut appartenir à plusieurs clusters. À la requête, la variante *collapsed tree* (arbre aplati en une couche, ~top-20 nœuds dans une enveloppe de 2000 tokens) bat la traversée couche par couche. Résultats : QuALITY passe de 62.3 % à **82.6 %** avec GPT-4, et QASPER atteint 55.7 % de F1, devançant CoLT5 XL (53.9 %).

## Tradeoff / quand l'utiliser
Utile pour les questions multi-passages ou thématiques sur des documents longs, là où le chunking plat perd le fil. Coût : construction de l'arbre (appels LLM de résumé à l'indexation) et stockage supplémentaire. Moins lourd que GraphRAG car pas d'extraction d'entités, mais moins structuré pour les requêtes relationnelles.

## Source primaire
Sarthi et al., 2024, *RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval*, arXiv:2401.18059. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [graphrag](graphrag.md)
- [strategies-de-chunking](strategies-de-chunking.md)
