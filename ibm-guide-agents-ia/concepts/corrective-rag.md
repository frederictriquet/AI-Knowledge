# Corrective RAG (cRAG)

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [68-build-corrective-rag-agent-granite-tavily](../md/68-build-corrective-rag-agent-granite-tavily.md)

**En une phrase** — un grader LLM note les passages récupérés ; si mauvais → fallback recherche web (Tavily) + réécriture de requête, sinon refus explicite plutôt qu'hallucination.

## Ce que dit le corpus
La cRAG « ne se contente pas de s'appuyer sur la RAG traditionnelle, mais l'améliore » : elle évalue la qualité et la pertinence des résultats récupérés. Le tutoriel implémente, pour des questions sur une police d'assurance (PDF), un workflow ordonné : récupération initiale dans une base FAISS, **notation du contexte** par un évaluateur LLM (score 0-5, seuil `SIMILARITY_THRESHOLD = 3`), puis **fallback Tavily** (recherche web) si le contexte est trop court (`MIN_CONTEXT_LENGTH = 100`), **vérification des sources** par LLM, **réécriture de la requête** + seconde recherche Tavily si nécessaire, enfin **génération sous contrainte** ou refus. Le LLM Granite est configuré `temperature: 0.2` pour des réponses factuelles. Point clé : « Si le contexte est faible, non pertinent ou provenant d'une source non fiable, la cRAG tente de trouver de meilleures informations […], ou refuse explicitement de répondre au lieu de fabriquer une réponse. »

## Tradeoff / insight pour un senior
La cRAG transforme la récupération en boucle correctrice à plusieurs garde-fous (score, longueur, vérification de source). Le compromis : chaque garde-fou est un appel LLM supplémentaire (latence, tokens) et chaque seuil (`SIMILARITY_THRESHOLD`, `MIN_CONTEXT_LENGTH`) est un point de calibration fragile. La vraie valeur est le refus assumé : préférer « je ne sais pas » à une fabrication, ce qui change la fonction d'utilité en domaine critique.

## Source primaire
Le tutoriel IBM ne cite pas le paper fondateur CRAG — voir Yan et al., « Corrective Retrieval Augmented Generation », 2024 (hors-corpus, ➕).

## Voir aussi
- [Vérification de source](verification-de-source.md)
- [RAG agentique](rag-agentique.md)
