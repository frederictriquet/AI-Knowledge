---
outil: "Pinecone"
titre: "Pinecone"
themes: [rag-contexte, memoire]
type: "Service web (base vectorielle managée, propriétaire)"
url: https://www.pinecone.io/
modele_economique: "Propriétaire / SaaS — freemium + paiement à l'usage (serverless)"
cout_llm: "🟢 stocke des vecteurs (BYO embeddings) ; embeddings/rerank hébergés en option, facturés au token"
objectifs: [mise-en-prod]
famille: "Infrastructure RAG / bases vectorielles"
eco_icones: "🔒🎁💳"
cout_icones: "🟢"
resume: "**Managée propriétaire, zéro-ops** (AWS/Azure/GCP), serverless, milliards de vecteurs. Starter gratuit → Standard 50 $/mois min, à l'usage (stockage 0,33 $/Go, reads/writes au M). Pinecone Inference (embeddings/rerank) en option. Lock-in mais simple"
---

# Pinecone

**En une phrase** — Base vectorielle **entièrement managée, propriétaire**, zéro-ops : recherche sémantique / RAG à grande échelle (milliards de vecteurs) sur AWS/Azure/GCP, sans infra à provisionner.

## Type & intégration
SaaS cloud-only (pas de self-host open-source ; option **BYOC** = data plane dans ton compte cloud mais opéré par Pinecone). Architecture **serverless** : séparation stockage/compute, vecteurs en fichiers immuables sur object storage, exécuteurs stateless qui montent/descendent. Écritures interrogeables en < 100 ms, scaling sans resharding. SDK et format de filtres propriétaires.

## Modèle économique
Propriétaire, **freemium + pay-as-you-go**. Plans (vérifié le 2026-06-16) :
- **Starter** : gratuit — jusqu'à 2 Go, 2 M write units/mois, 1 M read units/mois, 5 index.
- **Builder** : 20 $/mois forfait. **Standard** : 50 $/mois de conso min. **Enterprise** : 500 $/mois min.
- À l'usage (serverless) : stockage **0,33 $/Go/mois** ; reads **16–18 $/M** (Standard) ; writes **4–4,50 $/M**. (Index *pod-based* legacy : facturés à l'heure par pod.)

## Coût LLM
**🟢** Pinecone **stocke et recherche des vecteurs** que tu fournis (BYO embeddings, jusqu'à 20k dim) — il **n'appelle pas de LLM génératif**. En option, **Pinecone Inference** héberge des modèles d'**embedding** et de **reranking**, facturés à l'usage : embeddings **0,08–0,16 $/M tokens**, reranking **2 $/1k requêtes** (avec allocations gratuites). Ces modèles d'embedding ne sont pas des LLM de chat.

## À quoi ça sert
Le choix « zéro-ops » quand on veut une base vectorielle de production sans gérer d'infra. RAG, recherche hybride (dense + sparse), recommandation, déduplication, détection de fraude.

## Notes / à creuser
- **Propriétaire + cloud-only** → lock-in (syntaxe, filtres, SDK spécifiques ; migration = ré-export + ré-indexation). À l'inverse de [Qdrant](qdrant.md)/[Weaviate](weaviate.md)/[Milvus](milvus.md), open-source et auto-hébergeables.
- Coût linéaire à l'usage : à très grande échelle, des bases open-source auto-hébergées peuvent être nettement moins chères (au prix de l'expertise Kubernetes).
- Positionnement : simplicité managée. Alternative serverless low-cost : [turbopuffer](turbopuffer.md).

## Source
https://www.pinecone.io/pricing/ · https://docs.pinecone.io/guides/inference/understanding-inference · https://docs.pinecone.io/reference/architecture/serverless-architecture. *(vérifié le 2026-06-16 ; tarifs reads/writes publiés en fourchettes selon cloud/région)*
