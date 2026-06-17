---
outil: "Weaviate"
type: "Base vectorielle open-source (BSD-3, Go) self-host + cloud managé"
url: https://weaviate.io/
modele_economique: "Open-source (BSD-3-Clause) + Weaviate Cloud (freemium + à l'usage)"
cout_llm: "🟢 BYO embeddings ; vectorizers BYOK ou Weaviate Embeddings hébergé (au token)"
---

# Weaviate

**En une phrase** — Base vectorielle **open-source (BSD-3, écrite en Go)**, « batteries-included » : recherche hybride dense+BM25, modules vectorizer et generative search intégrés, en self-host ou cloud managé.

## Type & intégration
Cœur open-source auto-hébergeable **ET** service managé **Weaviate Cloud**. Interfaces REST (CRUD), GraphQL et **gRPC** (recherche/batch performants). Modules : vectorizers, generative (`generative-openai`…), rerankers. Multi-tenancy (shard par tenant). Index **HNSW en mémoire** → la RAM est le facteur dimensionnant.

## Modèle économique
**Open-source BSD-3-Clause** (self-host gratuit). **Weaviate Cloud** — tarification refondue le 2025-10-27 (les anciens paliers Standard/Professional sont périmés). Paliers actuels (à partir de, varient selon cloud/région) :
- **Free** (sandbox), puis **Flex** 45 $/mois, **Plus** 280 $, **Premium** 400 $, **Dedicated** (~400 $+, sur devis).
- Facturation sur 3 axes : **dimensions vectorielles stockées** (ex. 0,0039–0,0047 $/M dim/mois selon palier), stockage disque, backups.

## Coût LLM
**🟢** Quatre options : (1) **BYO-vectors** (vecteurs fournis, aucun coût côté Weaviate) ; (2) **vectorizers en BYOK** (`text2vec-openai/cohere/huggingface` — ta clé provider, facturé par le provider) ; (3) **Weaviate Embeddings**, modèles hébergés **facturés par Weaviate au token** (0,025–0,065 $/M tokens, Cloud uniquement) ; (4) **modèles locaux** (`text2vec-transformers`, `-ollama`, self-host, compute seul). La base elle-même ne facture pas d'inférence en mode BYO.

## À quoi ça sert
Quand on veut une base vectorielle open-source avec **recherche hybride mature** et RAG/génératif intégrés sans assembler soi-même. Bonne DX.

## Notes / à creuser
- Contrainte mémoire **HNSW en RAM** (goulot principal) ; resharding coûteux/déconseillé → dimensionner la RAM en amont. Mitigation : quantization (PQ, binary).
- Positionnement : recherche hybride + modules intégrés. Vs [Qdrant](qdrant.md) (Rust, perf/filtrage, plus léger), [Milvus](milvus.md) (échelle distribuée), [Pinecone](pinecone.md) (managé propriétaire).

## Source
https://weaviate.io/pricing · https://weaviate.io/blog/weaviate-cloud-pricing-update · LICENSE BSD-3 (github.com/weaviate/weaviate) · docs Weaviate Embeddings/hybrid. *(vérifié le 2026-06-16 ; multiplicateurs de prix par région non publiés)*
