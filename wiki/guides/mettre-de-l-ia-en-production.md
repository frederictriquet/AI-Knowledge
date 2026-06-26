---
type: guide
titre: "Mettre de l'IA en production"
objectif: mise-en-prod
description: "Parcours transverse : passer d'un prototype LLM à un système en production — architecture, RAG, robustesse, amélioration continue."
---

# 🚀 Mettre de l'IA en production

> **Guide par objectif (L3)** — comment passer d'un prototype LLM à un produit fiable en production ?
> Côté **outils**, voir [IA dans un produit](../ia-dans-un-produit.md).

## En bref

Mettre un LLM en production, c'est moins une affaire de modèle que de **système** : choisir l'architecture (RAG vs fine-tuning vs prompt), garantir des **sorties exploitables**, encaisser les pannes (**résilience**), protéger l'utilisateur (**UX défensive**), et installer la **boucle d'amélioration** (évals + feedback + observabilité) qui fait progresser le produit.

## Parcours de lecture conseillé

1. **Cadrer l'architecture** — [Patterns pour systèmes LLM en production](../fiches/patterns-systemes-llm.md), [RAG vs fine-tuning vs prompt engineering](../fiches/rag-vs-fine-tuning-vs-prompt-engineering.md).
2. **RAG, si pertinent** — [RAG](../fiches/rag.md), [RAG agentique](../fiches/rag-agentique.md), [améliorer son RAG systématiquement](../fiches/ameliorer-rag-systematiquement.md). Alternative à considérer : [LLM Wiki (Karpathy)](../fiches/llm-wiki-karpathy.md).
3. **Sorties exploitables** — [sorties structurées (instructor / Pydantic)](../fiches/sorties-structurees-instructor.md).
4. **Encaisser les pannes** — [résilience & fallback LLM](../fiches/resilience-fallback-llm.md).
5. **Protéger l'utilisateur** — [UX défensive pour produits LLM](../fiches/ux-defensive-llm.md).
6. **Installer la boucle d'amélioration** — [eval-driven development](../fiches/eval-driven-development.md), [data flywheel](../fiches/data-flywheel-feedback.md), [observabilité LLM](../fiches/observabilite-llm-best-practices.md).

## Toutes les fiches de cet objectif

<!-- AUTO:objectif=mise-en-prod -->
> ⚙️ **Index généré** — 12 fiche(s) taguée(s) `objectifs: [mise-en-prod]`, régénéré par `tools/build_index.py`. La prose ci-dessus est curée à la main.

### 📚 RAG & contexte
- 🔴 **[Améliorer son RAG systématiquement](../fiches/ameliorer-rag-systematiquement.md)** — Traiter un système RAG comme un produit mesurable qu'on améliore par itérations guidées par des métriques, et non comme une recette figée.
- 🟡 **[LLM Wiki : un wiki maintenu par le LLM plutôt que du RAG](../fiches/llm-wiki-karpathy.md)** — Plutôt que de re-synthétiser depuis les sources brutes à chaque question (RAG classique), on fait maintenir au LLM un **wiki persistant** (markdown interconnecté) : une couche de connaissance *compilée* dont la valeur se cumule à chaque source ingérée.
- 🟡 **[RAG agentique](../fiches/rag-agentique.md)** — un agent placé devant la récupération qui décide s'il faut chercher, où chercher, reformule et itère, au lieu d'un pipeline RAG réactif fixe.
- 🟡 **[RAG vs fine-tuning vs prompt engineering](../fiches/rag-vs-fine-tuning-vs-prompt-engineering.md)** — comparatif des trois leviers d'optimisation d'un LLM sur quatre axes (approche, objectifs, ressources, applications), présentés comme complémentaires et souvent combinés.

### 📊 Évaluation
- 🔴 **[Data flywheel : collecte de feedback](../fiches/data-flywheel-feedback.md)** — la donnée de production est le seul actif durable d'un produit LLM : capter le feedback utilisateur (explicite et implicite) crée un *flywheel* qui alimente à la fois les évals, le fine-tuning et les guardrails — l'avantage compétitif qui ne se copie pas.
- 🔴 **[Eval-driven development](../fiches/eval-driven-development.md)** — Construire un système d'évaluation spécifique à ton domaine est la fondation d'un produit IA : c'est lui qui crée la flywheel données → évals → amélioration et débloque le reste.
- 🔴 **[Patterns pour systèmes LLM en production](../fiches/patterns-systemes-llm.md)** — Sept patterns pratiques pour transformer une démo LLM en produit fiable, organisés selon deux axes : améliorer la performance vs réduire coût/risque, et proche de la donnée vs proche de l'utilisateur.
- 🟢 **[RAG (Retrieval-Augmented Generation)](../fiches/rag.md)** — au lieu de répondre depuis sa seule mémoire d'entraînement, le LLM **récupère des passages pertinents dans une base externe** et les injecte dans le contexte pour ancrer sa réponse sur des sources.

### ⚡ Efficacité & coût
- 🟡 **[Sorties structurées (instructor / Pydantic)](../fiches/sorties-structurees-instructor.md)** — Obtenir d'un LLM des données typées et validées (via des modèles Pydantic) plutôt que de parser du texte libre, avec validation et retries automatiques.

### ⚖️ Gouvernance, alignement & ops
- 🔴 **[Observabilité LLM : best practices (indépendantes de l'outil)](../fiches/observabilite-llm-best-practices.md)** — instrumenter une app LLM, ce n'est pas brancher un dashboard : c'est décider *quoi* tracer (span par étape de chaîne), *comment* évaluer la qualité sans se ruiner ni se mentir (juge calibré, échantillonné), et *quoi ne pas ingérer* (PII) — l'outil n'est que le réceptacle.
- 🔴 **[Résilience & fallback LLM](../fiches/resilience-fallback-llm.md)** — un appel LLM est un appel réseau vers un service tiers faillible (429, 5xx, timeout, dérive de qualité) : un produit sérieux applique les réflexes de fiabilité distribuée — *retry* avec backoff, *timeout*, *fallback* vers un autre modèle/fournisseur, *circuit breaker* et **dégradation gracieuse**.
- 🔴 **[UX défensive (Defensive UX) pour produits LLM](../fiches/ux-defensive-llm.md)** — un LLM se trompe, hallucine et répond lentement *par construction* ; l'UX défensive conçoit l'interface en partant de cette faillibilité plutôt qu'en la niant — guider l'entrée, gérer l'erreur avec grâce, et garder l'humain aux commandes de la sortie.
<!-- /AUTO -->
