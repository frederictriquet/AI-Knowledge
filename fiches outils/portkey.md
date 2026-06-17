---
outil: "Portkey"
type: "AI Gateway open-source (MIT) self-host + Service web (SaaS managé)"
url: https://portkey.ai/
modele_economique: "Open-core : gateway MIT gratuit + SaaS métré (Free / 49 $ / Enterprise)"
cout_llm: "BYOK — pass-through, ne marque pas le prix des tokens"
---

# Portkey

**En une phrase** — « Production stack » pour apps GenAI : un AI Gateway unifié (routing vers 1 600+ modèles) combinant gateway, observabilité, guardrails, gouvernance et gestion de prompts, avec un cœur open-source et un cloud managé.

## Type & intégration
Modèle **open-core**, trois façettes :
- **AI Gateway open-source** (repo `Portkey-AI/gateway`, TypeScript) : déployable via `npx`, Docker, Node ou Cloudflare Workers (edge). Surcoût de latence revendiqué **< 1 ms** (footprint ~122 ko).
- **SaaS managé** : dashboard, observabilité hébergée, gouvernance.
- **API/SDK unifiée** compatible OpenAI côté client.

## Modèle économique
**Open-core : gateway OSS gratuit + SaaS facturé au volume de logs/requêtes** (pas au siège) :
- **Gateway open-source — licence MIT** (vérifié dans le LICENSE du repo + API GitHub). ⚠️ Des communiqués de mars 2026 disent « Apache 2.0 » : **inexact**, la source fait foi → MIT.
- **Developer** : gratuit (« Free Forever »), 10 000 logs/mois, rétention 3 j logs / 30 j métriques. Dépasser 10k n'interrompt pas les requêtes (seuls les logs au-delà ne sont pas conservés).
- **Production** : **49 $/mois**, 100 000 logs/mois, rétention 30 j / 90 j ; dépassement **+9 $ / 100 K requêtes** jusqu'à 3 M.
- **Enterprise** : sur devis (VPC/private cloud, SSO/RBAC, conformité). Prix non publié.

## Coût LLM
**🔑 BYOK par défaut** : tu connectes tes propres clés fournisseur (coffre chiffré). Une **« Virtual Key »** (Model Catalog) sert d'alias sécurisé donnant accès à plusieurs fournisseurs sans exposer la clé brute. **Portkey ne facture pas les tokens** et ne les marque pas — la relation de facturation reste entre toi et le fournisseur ; Portkey ne facture que son service (gateway/observabilité). (Contraste avec [OpenRouter](openrouter.md), qui revend des crédits.)

## À quoi ça sert
Quand on veut un **control plane « enterprise-grade »** par-dessus ses appels LLM : routing/fallback/load-balancing/retries, **guardrails 50+** (PII/redaction, anti-prompt-injection, modération, checks JSON/RegEx), observabilité (40+ métriques, compatible OpenTelemetry), caching simple **et sémantique**, prompt management versionné. Plus orienté gouvernance/observabilité que le simple routing.

## Notes / à creuser
- **Positionnement** : control plane BYOK gouvernance/observabilité. Vs [LiteLLM](litellm.md) (routeur OSS self-host, propriété totale, base GitHub plus large) et [OpenRouter](openrouter.md) (gateway hébergé qui revend les tokens).
- **Mars 2026 — « Gateway 2.0 »** : bascule en OSS de fonctions auparavant SaaS-only (gouvernance, observabilité temps réel, auth, MCP Gateway OAuth 2.1) → **frontière OSS / cloud payant désormais floue**, à vérifier au cas par cas.
- Le coût SaaS **croît avec le volume de logs** (9 $/100 K).
- **Incohérences marketing** : nombre de modèles (1 600+/3 000+/250+) et guardrails (50+/60+) variables selon les pages ; retenir les valeurs du README canonique (**1 600+ modèles, 50+ guardrails**).

## Source
https://portkey.ai/ · https://portkey.ai/pricing · https://github.com/Portkey-AI/gateway (LICENSE = **MIT**, via api.github.com/repos/Portkey-AI/gateway/license) · docs observabilité/clés. *(vérifié le 2026-06-16 ; prix Enterprise sur devis, frontière OSS/cloud post-Gateway 2.0 à reconfirmer)*
