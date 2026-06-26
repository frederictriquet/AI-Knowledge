---
titre: "Self-RAG"
type: "Concept"
theme: rag-contexte
niveau: 🔴
source_url: https://arxiv.org/abs/2310.11511
---

# Self-RAG

**En une phrase** — un LLM entraîné à décider *quand* récupérer et à *auto-critiquer* la pertinence et le support factuel de ce qu'il récupère et génère, via des « tokens de réflexion ».

## L'idée
Le RAG classique récupère systématiquement et fait confiance aux passages. Self-RAG entraîne le modèle à émettre des **reflection tokens** spéciaux qui : (1) décident si une récupération est nécessaire pour le segment courant, (2) notent la pertinence de chaque passage, (3) vérifient si la génération est réellement *soutenue* par le passage, (4) évaluent l'utilité globale. La récupération devient **conditionnelle et auto-évaluée**.

## Exemple
Quatre tokens de réflexion concrets (Table 1) : `Retrieve` ∈ {yes, no, continue}, `IsRel` ∈ {relevant, irrelevant}, `IsSup` ∈ {fully, partially, no support}, `IsUse` ∈ {1..5}. Le modèle émet d'abord `Retrieve=yes`, note chaque passage avec `IsRel`, vérifie que sa phrase est `fully supported`, puis se donne un `IsUse=5`. Résultats (Table 2) : sur PopQA, Self-RAG 7B atteint **54,9 %** contre **29,3 %** pour ChatGPT ; sur PubHealth, 74,5 % (13B) vs 70,1 %. Il reste sous ChatGPT sur ARC-Challenge (73,1 vs 75,3).

## Tradeoff / quand l'utiliser
Réduit hallucinations et sur-récupération. Exige un modèle entraîné/fine-tuné à émettre ces tokens (≠ simple prompt). Même objectif que le Corrective RAG (cRAG), mais obtenu par **apprentissage** plutôt que par un grader externe : Self-RAG = la qualité dans les poids, cRAG = la qualité dans le pipeline.

## Source primaire
Asai et al., 2023, *Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection*, arXiv:2310.11511. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [corrective-rag](corrective-rag.md)
- [rag-agentique](rag-agentique.md)
