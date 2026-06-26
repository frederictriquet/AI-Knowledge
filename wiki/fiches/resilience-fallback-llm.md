---
titre: "Résilience & fallback LLM"
type: "Concept"
theme: gouvernance-alignement-ops
niveau: 🔴
source_url: https://github.com/Portkey-AI/gateway
source_titre: "Portkey AI Gateway — fallbacks, retries, load balancing (référence d'implémentation)"
---

# Résilience & fallback LLM

**En une phrase** — un appel LLM est un appel réseau vers un service tiers faillible (429, 5xx, timeout, dérive de qualité) : un produit sérieux applique les réflexes de fiabilité distribuée — *retry* avec backoff, *timeout*, *fallback* vers un autre modèle/fournisseur, *circuit breaker* et **dégradation gracieuse**.

## L'idée
À distinguer du [routage & cascade](model-routing-cascades.md), qui optimise le **coût** (modèle le moins cher capable). Ici l'objectif est la **disponibilité** : que la requête aboutisse malgré une panne en aval.

- **Retry + backoff exponentiel** sur les erreurs transitoires (429 rate limit, 5xx, timeout réseau). Avec *jitter* pour éviter les tempêtes de retries synchronisées. Plafonner le nombre de tentatives (les gateways type Portkey vont jusqu'à ~5, backoff exponentiel).
- **Timeout** explicite par appel : un LLM peut « pendre » ; sans timeout, la latence se propage à tout le système.
- **Fallback de modèle/fournisseur** : si OpenAI renvoie 429, basculer vers Anthropic (ou un modèle équivalent) plutôt qu'échouer. C'est précisément ce que vendent les passerelles ([OpenRouter](../fiches%20outils/openrouter.md), [LiteLLM](../fiches%20outils/litellm.md), [Portkey](../fiches%20outils/portkey.md)) sous le nom *failover chains*.
- **Circuit breaker** : couper temporairement un fournisseur qui échoue en rafale, au lieu de le marteler.
- **Dégradation gracieuse** : prévoir une réponse de repli (cache, réponse partielle, message honnête « réessayez ») plutôt qu'une erreur 500 brute à l'utilisateur — versant infra de la [UX défensive](ux-defensive-llm.md).

## Tradeoff / insight pour un senior
Chaque mécanisme a un coût caché qu'il faut arbitrer, pas activer aveuglément :
- **Retries = amplification.** Sous incident, des retries naïfs *aggravent* la surcharge du fournisseur (retry storm) et **multiplient la facture tokens**. Backoff + jitter + plafond ne sont pas optionnels.
- **Idempotence & double-facturation.** Un retry après timeout peut relancer une génération déjà facturée (le fournisseur a produit la réponse, seul le réseau a coupé). À surveiller côté coût.
- **Fallback ≠ équivalence.** Basculer GPT→Claude change le comportement, le format, le ton : un fallback silencieux peut dégrader la qualité sans alerte. Il faut le **tracer** (cf. [observabilité LLM](observabilite-llm-best-practices.md)) et tester les deux chemins.
- **Le SLA est celui du maillon faible** : un produit qui dépend d'un seul fournisseur hérite de *son* uptime. Le multi-fournisseur via gateway est le levier de résilience le plus direct — au prix d'un intermédiaire de plus sur le chemin critique.

## Source primaire
Pratiques de fiabilité distribuée (retry/backoff/jitter, circuit breaker — *Release It!*, Hystrix) appliquées aux API LLM. Implémentations de référence vérifiées : Portkey AI Gateway (retries jusqu'à 5, backoff exponentiel, fallback/load-balancing — github.com/Portkey-AI/gateway), LiteLLM (fallbacks), guides *rate limits* des fournisseurs (gestion 429/5xx).

## Voir aussi
- [model-routing-cascades](model-routing-cascades.md) — l'axe coût (à ne pas confondre).
- [ux-defensive-llm](ux-defensive-llm.md) — le versant interface de la dégradation gracieuse.
- [observabilite-llm-best-practices](observabilite-llm-best-practices.md) — tracer les fallbacks et alerter sur les erreurs.
- [patterns-systemes-llm](patterns-systemes-llm.md) — la vue produit d'ensemble.
