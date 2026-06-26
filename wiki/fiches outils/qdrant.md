---
outil: "Qdrant"
titre: "Qdrant"
themes: [rag-contexte, memoire]
type: "Base vectorielle open-source (Apache 2.0, Rust) self-host + cloud managé"
url: https://qdrant.tech/
modele_economique: "Open-source (Apache 2.0) + Qdrant Cloud (free tier + à l'usage)"
cout_llm: "🟢 BYO embeddings ; FastEmbed (local) ou Cloud Inference (au token, Cloud only)"
objectifs: [mise-en-prod]
famille: "Infrastructure RAG / bases vectorielles"
eco_icones: "🔓🎁💳"
cout_icones: "🟢"
resume: "Moteur **open-source Apache 2.0 en Rust**, perf + **filtrage avancé** (filterable HNSW), quantization binaire (×32). Self-host `docker run` ou Cloud (free tier 1 Go à vie, puis à l'heure). FastEmbed local / Cloud Inference au token. Simple sous ~100 M vecteurs"
---

# Qdrant

**En une phrase** — Base vectorielle **open-source écrite en Rust** (Apache 2.0), axée performance et **filtrage avancé** : moteur de recherche par similarité simple à auto-héberger (Docker), avec cloud managé.

## Type & intégration
Moteur open-source (Rust, storage engine maison « Gridstore »), self-host via `docker run` (REST 6333, gRPC 6334, dashboard) **ou** Qdrant Cloud / Hybrid Cloud / Private Cloud. Modèle open-core (moteur OSS + control-plane managé propriétaire).

## Modèle économique
**Open-source Apache 2.0** (self-host gratuit, illimité). **Qdrant Cloud** :
- **Free tier à vie**, sans CB : 1 Go RAM / 0,5 vCPU / 4 Go disque (~1 M vecteurs en 768 dim). Suspendu après 1 semaine d'inactivité.
- **Standard** : à l'usage, **facturé à l'heure** (vCPU + mémoire + stockage), SLA 99,5 %. **Premium** : minimum spend (non publié), SSO, VPC, support 24/7.
- ⚠️ **Prix unitaires ($/vCPU/h) non publiés** à la source — uniquement via le calculateur. Hybrid/Private Cloud sur devis.

## Coût LLM
**🟢** Le moteur **stocke et indexe des vecteurs fournis** (BYO embeddings) — n'appelle aucun LLM. Deux aides optionnelles : **FastEmbed** (lib officielle, génération d'embeddings **locale** via ONNX, sans GPU ni coût externe) ; **Qdrant Cloud Inference** (Cloud uniquement, génère les embeddings dans le cluster, **facturé au token**, quota gratuit, sert aussi de proxy vers OpenAI/Cohere/Jina facturés par eux).

## À quoi ça sert
Le choix « perf Rust + on-prem facile » quand on veut un contrôle total et un **filtrage riche**. Différenciateur réel : **filterable HNSW** (le filtrage par payload est intégré au graphe HNSW, pas appliqué en post-filtre), filtres Range/Geo/Full-text/Nested, fallback ACORN. Quantization scalaire (×4) et **binaire** (×32 mémoire). Recherche hybride (dense + sparse/ColBERT, RRF/DBSF).

## Notes / à creuser
- Limites doc : max 65 535 dimensions, index payload à créer avant ingestion, **migrations irréversibles** (pas de downgrade).
- Benchmarks de perf = auto-benchmarks (biais reconnu par Qdrant). Série B 50 M$ (mars 2026), ~250 M téléchargements.
- Positionnement : simple sous ~100 M vecteurs (binaire/Docker unique). Vs [Milvus](milvus.md) (distribué, échelle supérieure mais ops lourdes), [Weaviate](weaviate.md) (vectorisation intégrée), [Pinecone](pinecone.md) (managé propriétaire).

## Source
https://qdrant.tech/pricing/ · https://qdrant.tech/documentation/cloud/inference/ · LICENSE Apache 2.0 (github.com/qdrant/qdrant) · docs filtering/quantization. *(vérifié le 2026-06-16 ; prix unitaires Cloud non publiés)*
