---
outil: "turbopuffer"
titre: "turbopuffer"
type: "Service web (recherche vectorielle + full-text serverless, propriétaire)"
url: https://turbopuffer.com/
modele_economique: "Propriétaire / SaaS — paiement à l'usage (min 64 $/mois)"
cout_llm: "🟢 BYO embeddings — indexe/recherche seulement, ne génère pas d'embeddings"
---

# turbopuffer

**En une phrase** — Moteur de recherche **serverless** (vectoriel + full-text BM25) bâti **sur le stockage objet** (S3/GCS/Azure) : ~10× moins cher à grande échelle, conçu pour les charges multi-namespace majoritairement « froides ».

## Type & intégration
Service managé **propriétaire** (pas de self-host). Architecture en tiers : données froides sur object storage (~0,02 $/Go), chaudes sur SSD/NVMe, brûlantes en RAM. BYO embeddings (vecteurs denses & sparses), filtres (index inversé), regex (index trigramme).

## Modèle économique
Propriétaire, **pay-as-you-go** sur 3 dimensions (stockage, écritures, requêtes), avec minimums mensuels (vérifié le 2026-06-16) :
- **Launch** : min **64 $/mois** (toutes fonctions, support communautaire).
- **Scale** : min **256 $/mois** (HIPAA-ready, SSO, audit logs).
- **Enterprise** : **≥ 4 096 $/mois** (+35 % d'usage) — single-tenancy, BYOC, CMEK, SLA 99,95 %.
- ⚠️ **Prix unitaires exacts non vérifiables à la source** (calculateur interactif). Estimations tierces : ~1 $/M vecteurs/mois, ~4 $/M requêtes, stockage ~0,02 $/Go — à confirmer.

## Coût LLM
**🟢** turbopuffer **ne génère pas d'embeddings** : moteur **BYO embeddings**, tu fournis les vecteurs, il indexe et interroge (+ full-text BM25, filtres, regex). Aucun coût LLM/embedding intégré.

## À quoi ça sert
Le pari **coût** : stocker les vecteurs froids sur object storage plutôt que SSD/RAM réduit drastiquement la facture pour les charges multi-tenant / nombreux namespaces peu sollicités (index de code, recherche par espace de travail). Échelle annoncée : 4T+ documents, 10M+ writes/s, 25k+ queries/s.

## Notes / à creuser
- **Compromis latence** : sub-10 ms p50 sur données en cache, mais **premier accès « froid » ~300–500 ms**. Pas de reranking intégré.
- Produit récent (lancé oct. 2023, fondateurs ex-Shopify) mais **forte traction** : clients cités sur le site — Cursor, Anthropic, Notion, Atlassian, Linear, Grammarly… Cas publiés : Cursor ~95 %, Notion ~80 % de réduction de coût de recherche (sources secondaires).
- Vs [Pinecone](pinecone.md) serverless : turbopuffer mise sur le coût et le multi-namespace ; Pinecone sur la latence garantie sub-10 ms sur **chaque** requête.

## Source
https://turbopuffer.com/ · https://turbopuffer.com/pricing · https://turbopuffer.com/docs · https://turbopuffer.com/about. *(vérifié le 2026-06-16 ; prix unitaires par-unité et licence formelle non publiés en clair sur le site)*
