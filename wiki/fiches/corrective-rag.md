---
titre: "Corrective RAG (cRAG)"
type: "Concept"
theme: rag-contexte
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/tutorials/build-corrective-rag-agent-granite-tavily
source_titre: "Créer un agent RAG correctif avec IBM Granite et Tavily"
---

# Corrective RAG (cRAG)

**En une phrase** — un grader LLM note les passages récupérés ; si mauvais → fallback recherche web (Tavily) + réécriture de requête, sinon refus explicite plutôt qu'hallucination.

## En détail
La cRAG « ne se contente pas de s'appuyer sur la RAG traditionnelle, mais l'améliore » : elle évalue la qualité et la pertinence des résultats récupérés. Un workflow ordonné, illustré ici pour des questions sur une police d'assurance (PDF), enchaîne : récupération initiale dans une base FAISS, **notation du contexte** par un évaluateur LLM (score 0-5, seuil `SIMILARITY_THRESHOLD = 3`), puis **fallback Tavily** (recherche web) si le contexte est trop court (`MIN_CONTEXT_LENGTH = 100`), **vérification des sources** par LLM, **réécriture de la requête** + seconde recherche Tavily si nécessaire, enfin **génération sous contrainte** ou refus. Le LLM Granite est configuré `temperature: 0.2` pour des réponses factuelles. Point clé : « Si le contexte est faible, non pertinent ou provenant d'une source non fiable, la cRAG tente de trouver de meilleures informations […], ou refuse explicitement de répondre au lieu de fabriquer une réponse. »

## Exemple
Question « How does the policy cover for In-Patient Hospitalisation? » sur une brochure d'assurance santé. Le retriever FAISS sort le top-8, le grader note chaque chunk (Score: 0-5) ; les `< 3` sont jetés. Si le contexte reste sous 100 caractères, fallback Tavily — mais le `CONTEXT_SOURCE_VERIFICATION_PROMPT` rejette un résultat web parlant de Medi-Cal (programme public) avec un « NO », car hors police privée. Faute de contexte vérifié, le prompt final impose : citer mot pour mot ou répondre « I'm sorry, but this information is not available in the provided policy details » — jamais inventer.

## Tradeoff / insight pour un senior
La cRAG transforme la récupération en boucle correctrice à plusieurs garde-fous (score, longueur, vérification de source). Le compromis : chaque garde-fou est un appel LLM supplémentaire (latence, tokens) et chaque seuil (`SIMILARITY_THRESHOLD`, `MIN_CONTEXT_LENGTH`) est un point de calibration fragile. La vraie valeur est le refus assumé : préférer « je ne sais pas » à une fabrication, ce qui change la fonction d'utilité en domaine critique.

## Source primaire
Le paper fondateur de la cRAG : Yan et al., « Corrective Retrieval Augmented Generation », 2024.

## Voir aussi
- [Vérification de source](verification-de-source.md)
- [RAG agentique](rag-agentique.md)
