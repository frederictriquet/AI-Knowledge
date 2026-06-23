---
outil: "pgvector"
titre: "pgvector"
type: "Extension PostgreSQL open-source (recherche vectorielle)"
url: https://github.com/pgvector/pgvector
modele_economique: "Open-source (PostgreSQL License) — gratuit, pas de facture séparée"
cout_llm: "🟢 BYO embeddings — stocke/indexe seulement, ne génère rien"
---

# pgvector

**En une phrase** — Extension PostgreSQL qui ajoute un type `vector` et des index ANN (**HNSW**, IVFFlat) : faire de la recherche de similarité vectorielle **à l'intérieur de Postgres**, à côté de ses données relationnelles — pas de base séparée à opérer.

## Type & intégration
Pas une base à part : `CREATE EXTENSION vector;` dans une base Postgres existante. Types `vector` (jusqu'à 16 000 dim), `halfvec`, `bit`, `sparsevec` ; distances L2, cosinus, inner product, L1, Hamming, Jaccard. Préinstallée/activable chez la plupart des Postgres managés : **Supabase, Neon, AWS RDS/Aurora, GCP Cloud SQL, Azure**. Utilisable depuis tout client Postgres (40+ langages).

## Modèle économique
**Open-source, licence PostgreSQL** (permissive, type BSD). **Gratuit**, usage commercial libre. **Pas de facture séparée** : le coût = celui de ton instance Postgres (que tu opères déjà ou prends en managé), pas un abonnement de base vectorielle distinct.

## Coût LLM
**🟢** pgvector **ne génère aucun embedding** et n'appelle aucun LLM : BYO embeddings (tu fournis des vecteurs calculés en amont par OpenAI/Cohere/un modèle local…), il les **stocke, indexe et interroge**. Aucun coût d'inférence imputable à pgvector ; le coût d'embedding dépend du modèle externe branché en amont.

## À quoi ça sert
La réponse « ne rajoute pas un système » : combiner recherche vectorielle, `JOIN`, filtres `WHERE`, transactions ACID et métadonnées **dans une seule requête SQL**, sur la même donnée. Idéal RAG/recherche sémantique quand l'équipe est déjà sur Postgres et veut minimiser le nombre de technos à exploiter.

## Notes / à creuser
- **Quand pgvector suffit** : volumes faibles à moyens (quelques millions à ~dizaines de millions de vecteurs), filtrage relationnel combiné, stack déjà Postgres.
- **Quand passer à une base dédiée** ([Pinecone](pinecone.md)/[Qdrant](qdrant.md)/[Milvus](milvus.md)/[Weaviate](weaviate.md)) : centaines de millions/milliards de vecteurs, sharding horizontal natif, quantization avancée, très fort QPS. Limite principale : Postgres scale surtout verticalement, et le build d'index HNSW est coûteux en RAM/temps sur de très gros volumes. *(Seuils = ordres de grandeur, à benchmarker.)*
- Version stable série 0.8.0 (à reconfirmer au CHANGELOG).

## Source
https://github.com/pgvector/pgvector (README + LICENSE PostgreSQL License). Disponibilité managée : docs AWS RDS/Aurora, Supabase, Neon, Cloud SQL, Azure. *(vérifié le 2026-06-16 ; n° de version exact à reconfirmer)*
