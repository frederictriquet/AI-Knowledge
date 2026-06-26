---
outil: "LlamaIndex"
titre: "LlamaIndex"
themes: [rag-contexte, frameworks-outillage]
type: "Framework Python + TS (data/RAG + agents) + plateforme managée LlamaCloud/LlamaParse"
url: https://www.llamaindex.ai/
modele_economique: "Open-source (MIT) + LlamaCloud/LlamaParse (freemium, crédits à l'usage)"
cout_llm: "🔑 BYOK (framework) ; LlamaParse facture en crédits/page (LLM inclus)"
---

# LlamaIndex

**En une phrase** — Framework de données pour LLM, **orienté RAG** : connecteurs de données, indexation, retrieval/query avancé et agents (Workflows événementiels), complété par une plateforme managée de **parsing de documents** (LlamaParse) et d'indexation (LlamaCloud).

> 📄 Concept détaillé : [fiche notion LlamaIndex](../fiches/llamaindex.md). Ici : l'angle produit (licence, prix, coût LLM).

## Type & intégration
Framework open-source **Python** (`llama_index`) **et TypeScript** (`LlamaIndexTS`). Couvre ingestion (LlamaHub), indexation, query/retrieval, et **Workflows** (orchestration agentique événementielle, ≈ équivalent LangGraph côté agents). + plateforme managée **LlamaCloud** (indexation/RAG géré) et **LlamaParse** (OCR + parsing « layout-aware » agentique de documents complexes).

## Modèle économique
- **Framework : open-source MIT**, gratuit.
- **LlamaCloud / LlamaParse** : payant **à l'usage en crédits** (1 000 crédits = 1,25 $). Plans : **Free** 0 $ (10k crédits) → **Starter** 50 $/mois (40k) → **Pro** 500 $/mois (400k) → **Enterprise** sur devis. LlamaParse facture **par page** selon le mode : Fast 1 crédit, Cost-effective 3, Agentic 10, Agentic Plus 45 (≈ 800 à 18 pages/$).

## Coût LLM
**🔑 BYOK côté framework** : tu fournis tes clés modèle **+ embeddings** (par défaut OpenAI, mais brancheable sur n'importe quel modèle, ou `llm=None`). ⚠️ Nuance : côté **LlamaParse managé**, les coûts LLM/VLM internes au parsing sont **inclus dans le crédit** (pas du BYOK) — tu paies en crédits, pas via ta clé.

## À quoi ça sert
Le choix **RAG-first** : large catalogue de connecteurs, et surtout **LlamaParse** pour ingérer des documents complexes (tableaux, PDF en colonnes, scans) là où un parsing naïf échoue. Workflows pour la partie agentique.

## Notes / à creuser
- Vs LangChain ([📄 notion](../fiches/langchain.md)) / [LangGraph](langgraph.md) : LlamaIndex penche **data/RAG/parsing** ; LangChain/LangGraph penchent orchestration générale. Recouvrement partiel (Workflows ≈ LangGraph).
- Valeur commerciale = couche managée (LlamaParse/LlamaCloud) ; le framework reste 100 % MIT.
- Certains services managés affichés « free (beta) » — statut à reconfirmer.

## Source
https://www.llamaindex.ai/pricing · https://developers.llamaindex.ai/python/cloud/general/pricing/ · LICENSE MIT (github.com/run-llama/llama_index). *(vérifié le 2026-06-16)*
