---
outil: "OpenRouter"
type: "Service web (gateway LLM hébergé)"
url: https://openrouter.ai/
modele_economique: "Propriétaire / paiement à l'usage (crédits)"
cout_llm: "Revendu à l'usage (crédits, frais à l'achat) ou BYOK"
---

# OpenRouter

**En une phrase** — Passerelle LLM hébergée : une API unique (compatible SDK OpenAI) vers 400+ modèles de 60+ fournisseurs, avec routage prix/perf et failover automatique entre fournisseurs.

## Type & intégration
Service web SaaS. On change la base URL et on appelle des centaines de modèles via un seul endpoint au format OpenAI — pas de SDK à réécrire par fournisseur. Apporte : routing multi-modèles, **fallback/failover** entre fournisseurs (mutualisation de la disponibilité), facturation consolidée (un compte au lieu de N) et *data policies* (restreindre quels fournisseurs voient les prompts).

## Modèle économique
Propriétaire, **pay-as-you-go via crédits prépayés** (libellés en $). Le point clé : **aucune marge sur l'inférence** — le prix par million de tokens est répercuté au tarif fournisseur. OpenRouter se rémunère sur **l'achat de crédits** :
- carte/Stripe : **5,5 %** du montant, **min 0,80 $** ;
- crypto (USDC) : **5,0 %** flat, sans minimum.
- Crédits remboursables (fenêtre ~24 h), expiration après 1 an. (L'ancien frais fixe de 0,35 $ a été supprimé le 2025-06-09.)

## Coût LLM
Deux modes :
- **💸 Crédits (revendu à l'usage)** : OpenRouter achète l'inférence et te la facture au prix coûtant ; la « marge » se limite aux frais d'achat de crédits (5,5 %/5,0 %), pas aux tokens.
- **🔑 BYOK** : tu branches ta propre clé fournisseur et paies le fournisseur en direct ; OpenRouter ne facture que l'orchestration. Historiquement : 1er million de requêtes BYOK/mois gratuites, puis **5 %** du coût normalisé. ⚠️ Le BYOK migre vers un **abonnement mensuel fixe** (annoncé 2025-06-09) dont le montant n'était **pas chiffré à la source** au 2026-06-16 — à reconfirmer avant de s'engager.

## À quoi ça sert
Tester/exploiter beaucoup de modèles sans ouvrir N comptes fournisseurs, avec failover pour la disponibilité et une facturation unique. Le plus « marketplace clé-en-main » de la famille routeurs — au prix d'un intermédiaire sur le chemin critique.

## Notes / à creuser
- La « marge » est sur le **rechargement**, pas les tokens : le coût total dépend du volume et du mode (crédits vs BYOK).
- Dépendance à un intermédiaire unique (latence, point de défaillance, exposition des prompts sauf *data policies* strictes — pas de cœur self-host, contrairement à [LiteLLM](litellm.md)/[Portkey](portkey.md)).
- Alternatives : [LiteLLM](litellm.md) (open-source, self-host, pass-through), [Portkey](portkey.md) (open-core BYOK), [Requesty](requesty.md) (SaaS EU). Appel direct aux fournisseurs sinon.

## Source
https://openrouter.ai/ · https://openrouter.ai/docs/faq · annonce frais https://openrouter.ai/blog/announcements/simplifying-our-platform-fee/ · https://openrouter.ai/pricing. *(vérifié le 2026-06-16 ; montant du futur abonnement BYOK non publié à cette date)*
