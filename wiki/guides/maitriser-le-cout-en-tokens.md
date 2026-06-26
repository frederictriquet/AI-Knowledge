---
type: guide
titre: "Maîtriser le coût en tokens"
objectif: couts
description: "Parcours transverse : leviers pour réduire le coût et la latence d'un système LLM sans sacrifier la qualité."
---

# ⚡ Maîtriser le coût en tokens

> **Guide par objectif (L3)** — comment réduire le coût (et la latence) d'un système LLM sans perdre en qualité ?
> Côté **outils**, voir les passerelles/routeurs et l'optimisation tokens dans [produire du code](../produire-du-code.md) & [IA dans un produit](../ia-dans-un-produit.md).

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
