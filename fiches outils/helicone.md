---
outil: "Helicone"
type: "Service web (proxy/gateway) + self-host open-source"
url: https://www.helicone.ai/
modele_economique: "Open-source (Apache 2.0) + Freemium / Abonnement (cloud)"
cout_llm: "Intégré — observe (et peut réduire via cache) tes propres appels"
---

# Helicone

**En une phrase** — Plateforme d'observabilité LLM open-source (Apache 2.0), surtout utilisée **via proxy** : logs, coûts, latence, caching, rate-limiting et fallbacks, en quelques lignes de config.

## Type & intégration
Deux modes : **proxy/gateway** (on route ses appels LLM via Helicone — intégration la plus rapide, une ligne de base URL) ou **logging asynchrone** (SDK, sans ajouter de latence sur le chemin critique). Self-hostable gratuitement (Docker) ou cloud. Au-delà de l'observabilité, le proxy apporte des fonctions « gateway » : **cache** (réduit coûts et latence), **rate limits**, **fallbacks** automatiques.

## Modèle économique
Open-source **Apache 2.0** ; self-host gratuit. Cloud (constaté le 2026-06-15) :
- **Hobby** : gratuit — 10k requêtes/mois, 1 Go de stockage, 1 seat, rétention 7 j.
- **Pro** : 79 $/mois, seats illimités, alertes (essai 7 j).
- **Team** : 799 $/mois, 5 organisations, fonctions de conformité.
- **Enterprise** : sur devis, déploiement on-prem.

## Coût LLM
**Intégré (🟢)** : Helicone **intercepte tes appels** LLM et ne génère pas de complétion lui-même → pas de coût LLM séparé pour l'observabilité. Mieux : son **cache** peut *réduire* ta facture LLM en évitant des appels redondants. (Il propose aussi des évaluateurs ; un LLM-as-judge consommerait alors tes tokens en BYOK.)

## À quoi ça sert
Quand on veut **logger et monitorer vite** coûts/usage/latence de ses appels LLM sans réinstrumenter le code, et ajouter cache/rate-limit/fallback au passage. Le plus « ops/coût » de la famille.

## Notes / à creuser
- Mode proxy = un point sur le chemin critique (latence, dépendance) ; le mode async l'évite au prix d'un peu d'intégration.
- Moins orienté « évaluation rigoureuse » que Braintrust ; complémentaire.

## Source
https://www.helicone.ai/pricing · dépôt https://github.com/Helicone/helicone (README : « licensed under the Apache v2.0 License »). *(vérifié le 2026-06-15)*
