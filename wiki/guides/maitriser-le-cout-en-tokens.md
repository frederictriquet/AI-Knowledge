---
type: guide
titre: "Maîtriser le coût en tokens"
objectif: couts
description: "Parcours transverse : leviers pour réduire le coût et la latence d'un système LLM sans sacrifier la qualité."
---

# ⚡ Maîtriser le coût en tokens

> **Guide par objectif (L3)** — comment réduire le coût (et la latence) d'un système LLM sans perdre en qualité ?
> Concepts/pratiques ci-dessous ; **outils** (optimisation tokens, passerelles/routeurs) en **section Outils** en bas de page.

## En bref

Le coût se travaille à plusieurs niveaux : **choisir le bon modèle** (routing/cascade), **ne pas recalculer** (caching), **émettre moins de tokens inutiles** (sorties contraintes), **aller plus vite** (décodage spéculatif) et **réduire le contexte** injecté. La plupart sont silencieux pour la qualité — c'est ce qui en fait des leviers à fort effet.

## Parcours de lecture conseillé

1. **Router & cascader** — [Routage & cascades de modèles](../fiches/model-routing-cascades.md) : envoyer chaque requête au modèle le moins cher *capable*.
2. **Ne pas recalculer** — [Prompt caching](../fiches/prompt-caching.md) et [mise en cache sémantique](../fiches/semantic-caching.md).
3. **Émettre moins** — [décodage contraint / sortie structurée](../fiches/constrained-decoding.md) et [sorties structurées (instructor / Pydantic)](../fiches/sorties-structurees-instructor.md).
4. **Aller plus vite** — [Speculative decoding](../fiches/speculative-decoding.md).
5. **Réduire le contexte** — [Contextual Retrieval](../fiches/contextual-retrieval.md) pour des chunks plus pertinents et moins nombreux.
6. **Arbitrer le raisonnement** — [modèles de raisonnement & test-time compute](../fiches/inference-time-scaling.md) : payer du calcul à l'inférence quand (et seulement quand) ça vaut le coup.

## Toutes les fiches de cet objectif

<!-- AUTO:objectif=couts -->
> ⚙️ **Index généré** — 8 fiche(s) taguée(s) `objectifs: [couts]`, régénéré par `tools/build_index.py`. La prose ci-dessus est curée à la main.

### 🧠 Raisonnement & planification
- 🔴 **[Modèles de raisonnement & test-time compute](../fiches/inference-time-scaling.md)** — gagner en qualité en laissant le modèle « penser plus longtemps » à l'inférence plutôt qu'en grossissant ses poids.

### ✍️ Prompting
- 🟡 **[Prompt caching](../fiches/prompt-caching.md)** — réutiliser une réponse déjà calculée pour un prompt identique, mais attention : le tutoriel implémente un cache de réponses exact-match côté client (LangChain `SQLiteCache`), pas le prompt caching de préfixe (KV-cache) côté fournisseur.

### 📊 Évaluation
- 🟡 **[Contextual Retrieval](../fiches/contextual-retrieval.md)** — préfixer chaque chunk d'un court contexte (situant le chunk dans son document) *avant* l'embedding, pour réduire les échecs de récupération dus à des chunks ambigus.

### ⚡ Efficacité & coût
- 🟡 **[Décodage contraint / sortie structurée](../fiches/constrained-decoding.md)** — forcer la sortie à respecter une grammaire/schéma (JSON, regex) en masquant les tokens invalides au décodage ; garantit un format parsable (≠ « demander gentiment » du JSON).
- 🟡 **[Mise en cache sémantique](../fiches/semantic-caching.md)** — cacher requêtes, contexte et résultats par similarité sémantique, utilisé comme mécanisme de mémoire de l'agent.
- 🟡 **[Routage & cascades de modèles](../fiches/model-routing-cascades.md)** — router chaque requête vers le modèle le moins cher CAPABLE, ou enchaîner du petit au gros (cascade) avec un juge de confiance ; réduit fortement le coût à qualité quasi constante.
- 🟡 **[Sorties structurées (instructor / Pydantic)](../fiches/sorties-structurees-instructor.md)** — Obtenir d'un LLM des données typées et validées (via des modèles Pydantic) plutôt que de parser du texte libre, avec validation et retries automatiques.
- 🟡 **[Speculative decoding](../fiches/speculative-decoding.md)** — un petit modèle « brouillon » propose plusieurs tokens, le gros modèle les VÉRIFIE en un pass ; accélère l'inférence sans changer la distribution de sortie.
<!-- /AUTO -->

## Outils pour cet objectif

<!-- AUTO-OUTILS:objectif=couts -->
> ⚙️ **Outils générés** — 10 outil(s) `objectifs: [couts]`, groupés par famille. Régénéré par `tools/build_index.py` depuis le frontmatter des fiches outils.

<a id="fam-optimisation-des-tokens-du-comportement-de-l-agent"></a>
### Optimisation des tokens & du comportement de l'agent

*Réduisent ce que l'agent consomme (entrée) ou produit (sortie / périmètre du code).*

| Outil | Type | Éco | Coût LLM | En bref |
|---|---|:--:|:--:|---|
| **[Caveman](https://github.com/juliusbrussee/caveman)** · [📄](../fiches%20outils/caveman.md) | Skill (Claude Code + ~30 agents) | 🔓 | 🟢 | Skill open-source (Claude Code + ~30 agents) qui coupe ~65 % des tokens de sortie en faisant « parler comme un homme des cavernes » ; code/chemins préservés, niveaux lite/full/ultra/wenyan |
| **[dupehound](https://github.com/Rafaelpta/dupehound)** · [📄](../fiches%20outils/dupehound.md) | CLI / Serveur MCP | 🔓 | 🟢 | Détecteur de **code dupliqué** (Rust, MIT) pour bases écrites par l'IA : empreinte structurelle (tree-sitter + winnowing) → repère les fonctions dupliquées même renommées, même sans LLM ni clé. `scan`/`history`/`check` (gate CI + « slop score ») + mode **MCP** pour que l'agent réutilise au lieu de réécrire. ⚠️ Jeune (v0.1.2, juin 2026) |
| **[Headroom](https://github.com/headroomlabs-ai/headroom)** · [📄](../fiches%20outils/headroom.md) | CLI / Proxy / Serveur MCP / Bibliothèque | 🔓 | 🟢 | Couche de compression de contexte open-source (Apache 2.0) : réduit 60–95 % des tokens (JSON, code AST, logs, RAG, historique) **avant** l'appel, par compression **déterministe sans LLM**. Multi-format (lib Py/TS, proxy, wrapper d'agents, MCP, middleware) ; local, se place devant la clé/abonnement existant (pas de clé propre) |
| **[Ponytail](https://github.com/DietrichGebert/ponytail)** · [📄](../fiches%20outils/ponytail.md) | Skill / Plugin (multi-agents) | 🔓 | 🟢 | Skill open-source (Claude Code, Codex, Gemini, Cursor…) qui pousse l'agent à coder « comme le dev senior le plus paresseux » : anti-over-engineering (YAGNI, stdlib d'abord). 80–94 % de code en moins annoncé, niveaux lite/full/ultra |
| **[RTK (Rust Token Killer)](https://www.rtk-ai.app/)** · [📄](../fiches%20outils/rtk.md) | CLI (proxy) | 🔓 | 🟢 | Proxy CLI open-source (binaire Rust unique) qui compresse la sortie des commandes terminal avant le contexte LLM (60–90 % de tokens en moins) ; hook PreToolUse dans Claude Code, sans clé ni télémétrie. RTK Cloud (équipes) à venir, 15 $/dev/mois |
| **[Tokenade](https://tokenade.net/)** · [📄](../fiches%20outils/tokenade.md) | CLI | 🎁🔁 | 🟢 | CLI propriétaire qui réduit jusqu'à 88 % des tokens envoyés aux LLM par les agents (recherche sémantique, trim des sorties, chargement sélectif d'outils MCP) ; gratuit jusqu'à 20 M tokens, Pro 9,90 $/mois |

<a id="fam-passerelles-routeurs-llm"></a>
### Passerelles / routeurs LLM

*Une **API unique** (compatible OpenAI) devant des dizaines de fournisseurs : router selon prix/perf, basculer en **fallback** si un fournisseur tombe, mutualiser clés, budgets et observabilité. Brique directement liée à la **maîtrise du coût** et à la résilience multi-provider d'un produit. Notion de fond : [observabilité LLM — best practices](../fiches/observabilite-llm-best-practices.md).*
> **Clé de lecture du coût LLM** : deux modèles s'opposent. Les gateways **self-host / pass-through** ([LiteLLM](../fiches%20outils/litellm.md), [Portkey](../fiches%20outils/portkey.md)) ne facturent **pas** les tokens — tu gardes ta relation directe au fournisseur (🔑 BYOK). Les gateways **hébergés** ([OpenRouter](../fiches%20outils/openrouter.md), [Requesty](../fiches%20outils/requesty.md)) peuvent **revendre l'inférence** avec frais/marge (💸), tout en offrant souvent un mode BYOK (🔑).

| Outil | Type | Éco | Coût LLM | En bref |
|---|---|:--:|:--:|---|
| **[LiteLLM](https://www.litellm.ai/)** · [📄](../fiches%20outils/litellm.md) | Bibliothèque Python (SDK) + Proxy/Gateway self-host (open-source) + Enterprise | 🔓🎁 | 🔑 | Cœur **open-source MIT** (BerriAI) : SDK (dans le code) **ou** proxy/gateway self-host (clés virtuelles, budgets, multi-tenant). API unifiée vers 100+ LLM, routing/fallback. **Pass-through pur** : ne facture pas les tokens (BYOK). Enterprise payant (SSO/RBAC/audit, self-managed, prix non publiés) |
| **[OpenRouter](https://openrouter.ai/)** · [📄](../fiches%20outils/openrouter.md) | Service web (gateway LLM hébergé) | 🔒💳 | 💸🔑 | Gateway hébergé : 1 API (format OpenAI) vers **400+ modèles / 60+ fournisseurs**, routing prix/perf + failover. **Aucune marge sur l'inférence** ; se rémunère sur l'**achat de crédits** (5,5 % carte, min 0,80 $ ; 5,0 % crypto). Mode BYOK aussi (migre vers un abonnement fixe, montant non publié). Le plus « marketplace clé-en-main » |
| **[Portkey](https://portkey.ai/)** · [📄](../fiches%20outils/portkey.md) | AI Gateway open-source (MIT) self-host + Service web (SaaS managé) | 🔓🎁🔁 | 🔑 | **Open-core MIT** : gateway < 1 ms par-dessus 1 600+ modèles + guardrails (50+), observabilité (OTel), caching sémantique, prompt management. **BYOK pass-through** (ne marque pas les tokens). SaaS facturé au volume de logs (Developer gratuit 10k → Production 49 $/mois → Enterprise). Control plane « enterprise » |
| **[Requesty](https://www.requesty.ai/)** · [📄](../fiches%20outils/requesty.md) | Service web (gateway LLM hébergé) | 🔒🎁💳 | 💸🔑 | Gateway hébergé **EU-first / RGPD** (« alternative européenne à OpenRouter ») : 400+ modèles, smart routing, caching, observabilité. Free 200 req/j → pay-as-you-go **+5 % de marge** sur le tarif fournisseur → Enterprise (SSO/RBAC/PII/résidence EU). BYOK supporté (% de frais non documenté). **Early-stage** (seed 3 M$ sept. 2025) |
<!-- /AUTO-OUTILS -->
