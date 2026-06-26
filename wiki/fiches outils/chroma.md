---
outil: "Chroma (ChromaDB)"
titre: "Chroma (ChromaDB)"
themes: [rag-contexte, memoire]
type: "Base de données vectorielle (bibliothèque + serveur + Cloud SaaS)"
url: https://www.trychroma.com/products/chromadb
modele_economique: "Open-source (Apache 2.0) self-hosted gratuit + Chroma Cloud (freemium / à l'usage / Team / Enterprise)"
cout_llm: "Aucune inférence LLM — stocke/indexe des embeddings fournis (BYOK pour la génération d'embeddings)"
objectifs: [mise-en-prod]
famille: "Infrastructure RAG / bases vectorielles"
eco_icones: "🔓🎁💳"
cout_icones: "🟢"
resume: "Base vectorielle open-source (Apache 2.0) pour RAG / recherche sémantique ; self-hosted gratuit ou Chroma Cloud serverless (Starter gratuit + à l'usage, Team 250 $/mois+). Stocke les embeddings, ne les génère pas (BYOK)"
---

# Chroma (ChromaDB)

**En une phrase** — base de données vectorielle open-source (« search infrastructure for AI ») pour stocker et interroger des embeddings à grande échelle, socle des applications RAG et de recherche sémantique.

## Type & intégration
**Brique d'infrastructure**, pas un outil d'agent. Déclinaisons :
- **Self-hosted** : installation mono-nœud via `pip`, `npm` ou Docker, en mémoire ou persistante.
- **Chroma Cloud** : service managé serverless (GA depuis la v1.4.1).
- **Enterprise / BYOC** : déploiement auto-géré dans le VPC du client.

Même base de code Apache 2.0 pour l'open-source et le cloud → pas de vendor lock-in. Recherche unifiée : **vectorielle + full-text + regex + métadonnées** (hybride). S'intègre comme store de RAG dans les apps LLM (LangChain, LlamaIndex, SDK Python/JS).

## Modèle économique
- **Open-source self-hosted** : gratuit (Apache 2.0).
- **Chroma Cloud** : **Starter 0 $/mois + à l'usage** (serverless, ~5 $ de crédits offerts) ; **Team 250 $/mois** (+ usage, ~100 $ de crédits inclus) ; **Enterprise** sur devis avec BYOC. Tarifs à l'usage (vérifiés) : Write ~2,50 $/Gio, Storage ~0,33 $/Gio-mois, Query ~0,0075 $/Tio, Network ~0,09 $/Gio.

Modèle « open-core / managed cloud » classique : la valeur payante est l'hébergement managé, pas une version fermée du moteur.

## Coût LLM
**Aucune inférence LLM** 🟢 de la part de Chroma : il **stocke et indexe des embeddings**, il ne les **génère pas**. Tu fournis des vecteurs pré-calculés (sémantiques, BM25, SPLADE…). La génération d'embeddings se fait à part : via une **API d'embeddings externe** (OpenAI, Voyage, Cohere… → coût **BYOK** à l'usage) ou un modèle local (gratuit).

→ Dans ta grille : le coût de Chroma lui-même est de l'**infra** (stockage/compute cloud), distinct du coût LLM. Le seul coût « modèle » potentiel est celui des embeddings, hors Chroma.

## À quoi ça sert
Le moteur de récupération d'un système RAG : indexer des documents (sous forme d'embeddings + métadonnées) et retrouver les passages pertinents pour nourrir le contexte d'un LLM. Utilisé par des équipes IA en production (Capital One, Cisco, Intel cités).

## Notes / à creuser
- Différence avec les outils du « cluster réduction de tokens » ([CodeGraph](codegraph.md), [Polaris (polarismcp.com)](polaris.md), [GraphMind](graphmind.md)) : ceux-ci **embarquent** leur propre index vectoriel spécialisé pour le code ; Chroma est la **base vectorielle générique** sur laquelle on bâtirait soi-même une telle solution.
- Concurrents : Pinecone (propriétaire/cloud), Weaviate, Qdrant, Milvus, pgvector.
- Choix self-hosted = coût nul mais ops à gérer ; Cloud = simplicité contre coût à l'usage.

## Source
- Page produit : https://www.trychroma.com/products/chromadb · site : https://www.trychroma.com/
- Comparatifs pricing 2026 : pecollective, modern-datatools

*(vérifié le 2026-06-15 — page produit officielle + recherche web)*
