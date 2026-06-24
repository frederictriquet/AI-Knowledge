---
outil: "LanceDB"
titre: "LanceDB"
themes: [rag-contexte, memoire]
type: "Base vectorielle embarquée open-source (Apache 2.0) + cloud/Enterprise"
url: https://lancedb.com/
modele_economique: "Open-source (Apache 2.0) + LanceDB Cloud/Enterprise (prix non publiés)"
cout_llm: "🟢 BYO embeddings ; fonctions d'embedding optionnelles en BYOK / local"
---

# LanceDB

**En une phrase** — Base vectorielle/**multimodale embarquée** (in-process, « le SQLite du vectoriel ») open-source, bâtie sur le format columnar **Lance** : données + métadonnées + embeddings dans la même table, directement sur du stockage objet (S3/GCS/Azure), **sans serveur à opérer**.

## Type & intégration
Bibliothèque embarquée (cœur en **Rust** ; SDK Python, TypeScript, Rust), exécutée dans ton process. Persistance native sur **object storage** (URI `s3://`, `gs://`, `az://`) ou FS local → séparation stockage/compute, versioning automatique de chaque écriture. Offres managées en plus : **LanceDB Cloud** (serverless) et **Enterprise** (BYOC/VPC).

## Modèle économique
**Open-source Apache 2.0** (lib `lancedb` + format `lance`), gratuit. **LanceDB Cloud** (à l'usage, basé stockage) et **Enterprise** (BYOC ou managé, RBAC/SSO/SLA, via marketplaces cloud). ⚠️ **Aucun prix chiffré public** : la page pricing est un formulaire de contact (« contact sales »). *(Un tiers évoque un Cloud gratuit en beta + scale-to-zero, non confirmé en source primaire.)*

## Coût LLM
**🟢** BYO embeddings (vecteurs fournis, stockés/interrogés directement). Couche d'embedding **optionnelle** via un registry de modèles : providers distants (`openai`, `cohere`, `bedrock`, `gemini`, `voyageai`, `jina`…) appelés avec **ta clé (BYOK)**, ou modèles **locaux** (`sentence-transformers`, `ollama`, `open-clip`…) à coût compute seul. LanceDB ne revend pas de tokens d'embedding.

## À quoi ça sert
Le choix **local-first / edge / pipelines ML batch** : pas d'infra serveur à gérer, données sur S3, multimodal (texte, images, vidéo, point clouds). Indexation IVF / IVF_HNSW(_PQ), full-text BM25, recherche hybride, build d'index sur GPU.

## Notes / à creuser
- **Limites confirmées** : écritures concurrentes limitées (« too many concurrent writers » → échecs) ; les **lectures** scalent, pas les écritures lourdes. `fork` Python dangereux (Lance est multi-thread). Compaction nécessaire si beaucoup de petites insertions.
- Positionnement glissé de « vector DB embarqué » vers « **AI-native multimodal lakehouse** ». Série A 30 M$ (juin 2025) ; en prod chez Runway, Midjourney, Character.ai.
- Vs [Chroma](chroma.md) (embarqué aussi, souvent en mémoire, ≤ ~1 M vecteurs, bon filtrage métadonnées) ; vs bases serveur ([Qdrant](qdrant.md)/[Weaviate](weaviate.md)/[Milvus](milvus.md)) qui demandent un cluster/managé.

## Source
https://lancedb.com · https://docs.lancedb.com (indexing/storage/enterprise) · LICENSE Apache 2.0 (github.com/lancedb/lancedb + /lance) · registry embeddings (code source). *(vérifié le 2026-06-16 ; prix Cloud/Enterprise non publics ; chiffres de scale = marketing)*
