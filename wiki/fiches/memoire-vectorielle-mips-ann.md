---
titre: "Mémoire vectorielle : MIPS & ANN"
type: "Concept"
theme: rag-contexte
niveau: 🔴
source_url: https://lilianweng.github.io/posts/2023-06-23-agent/
source_titre: "LLM Powered Autonomous Agents"
---

# Mémoire vectorielle : MIPS & ANN

**En une phrase** — la mémoire long terme d'un agent s'implémente comme une recherche par produit interne maximal (MIPS) dans un magasin vectoriel, accélérée par des algorithmes de plus proches voisins approchés (ANN).

## Ce que dit la source
Weng mappe la mémoire long terme sur un magasin vectoriel externe que l'agent consulte à la requête, contournant la portée d'attention finie du Transformer. La pratique standard consiste à stocker les représentations par embedding dans une base vectorielle supportant un **Maximum Inner Product Search (MIPS)** rapide. Pour la vitesse, on recourt aux algorithmes de **plus proches voisins approchés (ANN)**, qui sacrifient un peu de précision contre une accélération massive. Weng détaille cinq algorithmes : **LSH** (Locality-Sensitive Hashing, fonction de hachage envoyant les items proches dans les mêmes seaux) ; **ANNOY** (arbres de projection aléatoire) ; **HNSW** (Hierarchical Navigable Small World, graphes hiérarchiques inspirés des réseaux « petit monde ») ; **FAISS** (quantification vectorielle par clustering, Facebook) ; et **ScaNN** (quantification vectorielle anisotrope). Elle renvoie à ann-benchmarks.com pour les comparaisons.

## Exemple
HNSW rend concret le compromis vitesse/précision. Inspiré des « six degrés de séparation » des réseaux sociaux, il empile des graphes « small world » : la recherche démarre à un nœud aléatoire de la couche supérieure et se rapproche de la cible ; bloquée, elle descend d'une couche, jusqu'à la couche du bas qui contient les vrais points. Chaque saut en haut couvre une grande distance dans l'espace des données, chaque saut en bas affine. ScaNN, lui, ne choisit pas le centroïde le plus proche : sa quantification anisotrope préserve le produit interne `⟨q, x_i⟩` plutôt que la distance brute — exactement ce que MIPS optimise.

## Pourquoi c'est utile
Weng descend au niveau algorithmique concret de la mémoire vectorielle : MIPS, le compromis précision/vitesse de l'ANN, et cinq implémentations nommées — une profondeur d'ingénierie rarement traitée dans les présentations générales du RAG.

## Sources primaires (citées par Weng)
- Maximum Inner Product Search (MIPS) — formulation de la récupération mémoire.
- LSH (Locality-Sensitive Hashing) et ANNOY (Spotify) — hachage et arbres de projection aléatoire.
- HNSW (Malkov & Yashunin) — graphes hiérarchiques « small world ».
- FAISS (Facebook AI) et ScaNN (Google, quantification anisotrope).

## Voir aussi
- [Mémoire CT/LT](memoire-court-long-terme.md)
- [Mémoire épisodique/sémantique/procédurale](memoire-episodique-semantique-procedurale.md)
- [post complet](../sources/lilian-weng/md/2023-06-23-agent.md)
