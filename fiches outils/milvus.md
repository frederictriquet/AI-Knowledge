---
outil: "Milvus"
titre: "Milvus"
type: "Base vectorielle open-source (Apache 2.0) distribuée + cloud managé (Zilliz)"
url: https://milvus.io/
modele_economique: "Open-source (Apache 2.0, LF AI & Data) + Zilliz Cloud (freemium + à l'usage)"
cout_llm: "🟢 BYO embeddings ; modules d'embedding relaient des providers tiers (BYOK)"
---

# Milvus

**En une phrase** — Base vectorielle **open-source (Apache 2.0)** cloud-native, pensée pour l'**échelle massive** (dizaines de milliards de vecteurs) via une architecture distribuée compute/stockage désagrégés ; managée sous **Zilliz Cloud**.

## Type & intégration
Projet **gradué de la LF AI & Data** (créé par Zilliz). Trois modes : **Milvus Lite** (lib Python embarquée, prototypage), **Standalone** (Docker mono-machine, ~100 M vecteurs), **Distributed** (Kubernetes, jusqu'à des dizaines de milliards). Le mode distribué dépend d'etcd + object storage + message queue (Pulsar/Kafka). Index CPU (HNSW, IVF, DiskANN…) **et GPU** (NVIDIA CAGRA).

## Modèle économique
**Open-source Apache 2.0** (self-host gratuit). **Zilliz Cloud** (managé) :
- **Free** : gratuit (5 Go, ~1 M vecteurs, 5 collections). Crédits 100 $ (+100 $ avec moyen de paiement).
- **Serverless** : à l'usage — **4 $/M vCU** + stockage **0,04 $/Go/mois** (tarif unifié depuis 2026-01-01).
- **Dedicated** : par CU/heure selon région (ex. 0,248 $/CU·h, Enterprise AWS). Plans Standard/Enterprise/Business Critical/**BYOC** sur devis.

## Coût LLM
**🟢** Milvus **stocke et indexe des vecteurs** — il ne génère pas d'embeddings. BYO embeddings par défaut. Deux couches d'intégration relaient des **modèles externes** (jamais hébergés par Milvus) : côté client `pymilvus.model` (OpenAI, Voyage, Cohere…) ; côté serveur les **Embedding Functions** (« Data in, Data out », Milvus 2.6 — tu insères du texte, Milvus appelle OpenAI/Bedrock/Vertex… en **BYOK**). ⚠️ Les anciens « Zilliz Cloud Pipelines » managés sont **dépréciés/offline depuis oct. 2025**.

## À quoi ça sert
Le choix quand on vise le **milliard+ de vecteurs** avec scaling horizontal Kubernetes et accélération GPU. RAG et recherche sémantique à très grande échelle.

## Notes / à creuser
- Mode distribué = dépendances etcd + object storage + message queue → **plus lourd à auto-héberger** que [Qdrant](qdrant.md) (binaire/Docker) ou [Weaviate](weaviate.md). Milvus Lite/Standalone allègent pour démarrer.
- ~44,8k étoiles GitHub ; ligne stable 2.6.x, Milvus 3.0 en beta (mai 2026, pas GA) — version GA exacte à reconfirmer.
- Claims d'échelle/perf auto-déclarés par l'éditeur. Vs [Pinecone](pinecone.md) (managé propriétaire).

## Source
https://milvus.io/docs/install-overview.md · https://milvus.io/docs/embedding-function-overview.md · LICENSE Apache 2.0 (github.com/milvus-io/milvus) · docs.zilliz.com (pricing) · lfaidata.foundation/projects/milvus. *(vérifié le 2026-06-16 ; prix Dedicated/BYOC sur devis)*
