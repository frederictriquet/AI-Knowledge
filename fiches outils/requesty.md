---
outil: "Requesty"
titre: "Requesty"
type: "Service web (gateway LLM hébergé)"
url: https://www.requesty.ai/
modele_economique: "Propriétaire / freemium + paiement à l'usage (+5 % de marge)"
cout_llm: "Revendu à l'usage (+5 %) ou BYOK"
---

# Requesty

**En une phrase** — Passerelle LLM hébergée se positionnant en **alternative européenne à OpenRouter** : API unifiée vers 400+ modèles (30+ fournisseurs), optimisation de coût, failover et observabilité, avec un angle EU/RGPD et résidence des données.

## Type & intégration
Service web SaaS (proxy entre l'app et les fournisseurs), API **compatible OpenAI** ; intégrable via SDK (provider communautaire AI SDK). Apporte routing multi-modèles, **failover chains** automatiques, **prompt caching** (jusqu'à 90 % d'économie de tokens revendiquée), dashboards temps réel (coût, latence, TTFT, P50/P90/P95/P99, taux d'erreur) et, en Enterprise, guardrails / détection PII / RBAC / résidence EU.

## Modèle économique
Propriétaire, **freemium + pay-as-you-go** :
- **Free** : 0 $, 200 requêtes/jour, modèles gratuits uniquement, sans CB.
- **Pay-as-you-go** : **+5 % de marge** sur le coût de base du modèle (ex. un modèle à 10 $/Mtok revient à **10,50 $**), 400+ modèles, BYOK supporté, plafonds de budget. Pas d'abonnement, pas de frais par siège, pas de minimum.
- **Enterprise** : sur devis — SSO (Okta/Azure AD/Google/OIDC), RBAC + audit logs, guardrails, détection PII, SLA, résidence EU.

## Coût LLM
Deux modes coexistent :
- **💸 Crédits (revendu à l'usage)** : consommation facturée avec **+5 %** sur le tarif fournisseur.
- **🔑 BYOK** : brancher ses propres clés, en conservant la relation de facturation directe.
- ⚠️ **Le % de frais exact en mode BYOK n'est pas documenté** à la source (page pricing/docs BYOK muettes) ; des tiers avancent « 5 % de la valeur de la requête » par analogie avec OpenRouter, **sans confirmation officielle** — à valider auprès du support avant de s'appuyer dessus.

## À quoi ça sert
Router/optimiser ses appels multi-modèles avec un **angle souveraineté EU** (serveurs UE, RGPD by design) que les concurrents US ne mettent pas en avant. Smart routing (tâches simples → modèles moins chers) et caching pour réduire la facture.

## Notes / à creuser
- **Produit jeune / early-stage** : seed de **3 M$ levés en septembre 2025** (lead 20VC). Peu de chiffres d'usage publics → traction difficile à évaluer.
- Économies revendiquées (30–50 %, « 400 k$/an » chez un client) = **marketing fournisseur, non audité**.
- Nombre de modèles incohérent selon les pages (300+ / 400+) ; le site principal annonce 400+.
- Positionnement : proche de [Portkey](portkey.md) (gateway + observabilité + gouvernance) mais plus récent et EU-first ; vs [OpenRouter](openrouter.md) (US, marketplace) et [LiteLLM](litellm.md) (open-source self-host).

## Source
https://www.requesty.ai/ · https://www.requesty.ai/pricing · https://docs.requesty.ai/features/bring-your-own-keys · https://www.requesty.ai/blog/requesty-raises-3m. *(vérifié le 2026-06-16 ; % de frais BYOK non documenté à la source)*
