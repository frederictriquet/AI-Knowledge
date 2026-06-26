---
type: guide
titre: "Fiabiliser & évaluer un système LLM"
objectif: fiabilite
description: "Parcours transverse : mesurer, vérifier et garder sous contrôle un système à base de LLM — des évals aux garde-fous."
---

# 🎯 Fiabiliser & évaluer un système LLM

> **Guide par objectif (L3)** — comment savoir si un système LLM *marche*, et le garder fiable dans le temps ?
> Côté **outils**, voir les familles observabilité/évaluation de [IA dans un produit](../ia-dans-un-produit.md).

## En bref

Un système LLM ne se valide pas « à l'œil » : il se **mesure**. La compétence centrale est de partir des **données réelles**, d'en tirer des **évals** spécifiques, puis d'instrumenter la production pour fermer la boucle. La vérification (auto-critique, juges, garde-fous) vient encadrer ce que le modèle produit.

## Parcours de lecture conseillé

1. **Partir des données** — [Error analysis : regarde tes données](../fiches/error-analysis.md) avant tout tableau de bord.
2. **Construire des évals** — [Évaluer les LLM (évals spécifiques)](../fiches/evaluer-les-llm.md), [Eval-driven development](../fiches/eval-driven-development.md), [Évaluation de trajectoire](../fiches/evaluation-trajectoire.md) pour les agents.
3. **LLM-as-judge, bien fait** — [LLM-as-a-judge](../fiches/llm-as-a-judge.md), puis [le faire correctement](../fiches/llm-as-judge-correct.md) et la [vue d'Eugene](../fiches/llm-evaluators.md).
4. **Auto-vérification** — [Chain-of-Verification](../fiches/chain-of-verification.md), [techniques d'auto-critique](../fiches/self-criticism-techniques.md), [Self-Refine](../fiches/self-refine.md).
5. **Garde-fous & sécurité** — [garde-fou en nœud d'entrée](../fiches/guardrail-noeud-entree.md), [sécurité agentique](../fiches/securite-agentique.md).
6. **Tenir dans le temps** — [observabilité LLM](../fiches/observabilite-llm-best-practices.md), [data flywheel](../fiches/data-flywheel-feedback.md), [patterns pour systèmes LLM en production](../fiches/patterns-systemes-llm.md).

## Toutes les fiches de cet objectif

<!-- AUTO:objectif=fiabilite -->
> ⚙️ **Index généré** — 15 fiche(s) taguée(s) `objectifs: [fiabilite]`, régénéré par `tools/build_index.py`. La prose ci-dessus est curée à la main.

### 🧠 Raisonnement & planification
- 🟡 **[Chain-of-Verification (CoVe)](../fiches/chain-of-verification.md)** — le modèle écrit une réponse, en dérive des questions de vérification factuelle, y répond isolément, puis corrige sa réponse à la lumière de ces vérifications.
- 🟡 **[Self-Refine](../fiches/self-refine.md)** — un même modèle produit une sortie, génère sa propre critique, puis se révise, en boucle, sans aucun signal externe.

### ✍️ Prompting
- 🔴 **[Techniques d'auto-critique](../fiches/self-criticism-techniques.md)** — Faire évaluer, vérifier et corriger par le modèle sa propre sortie, en boucle si besoin, pour fiabiliser la réponse sans intervention humaine.

### 📊 Évaluation
- 🔴 **[Data flywheel : collecte de feedback](../fiches/data-flywheel-feedback.md)** — la donnée de production est le seul actif durable d'un produit LLM : capter le feedback utilisateur (explicite et implicite) crée un *flywheel* qui alimente à la fois les évals, le fine-tuning et les guardrails — l'avantage compétitif qui ne se copie pas.
- 🔴 **[Error analysis : regarde tes données](../fiches/error-analysis.md)** — Avant toute métrique, lis manuellement les traces de ton produit, annote les comportements indésirables, puis construis une taxonomie des failure modes et compte leur fréquence.
- 🔴 **[Eval-driven development](../fiches/eval-driven-development.md)** — Construire un système d'évaluation spécifique à ton domaine est la fondation d'un produit IA : c'est lui qui crée la flywheel données → évals → amélioration et débloque le reste.
- 🔴 **[LLM-as-a-judge : le faire correctement](../fiches/llm-as-judge-correct.md)** — Un LLM-as-a-judge n'a de valeur que s'il est aligné sur le jugement binaire pass/fail d'un expert métier via un protocole itératif (« Critique Shadowing »), pas via des scores 1-5 arbitraires.
- 🔴 **[Patterns pour systèmes LLM en production](../fiches/patterns-systemes-llm.md)** — Sept patterns pratiques pour transformer une démo LLM en produit fiable, organisés selon deux axes : améliorer la performance vs réduire coût/risque, et proche de la donnée vs proche de l'utilisateur.
- 🔴 **[Évaluation de trajectoire](../fiches/evaluation-trajectoire.md)** — évaluer la suite des décisions, appels d'outils et étapes intermédiaires qu'a empruntées l'agent, pas seulement la qualité de sa réponse finale.
- 🔴 **[Évaluer les LLM (évals spécifiques à la tâche)](../fiches/evaluer-les-llm.md)** — Les évals « sur étagère » corrèlent mal avec la performance applicative ; Eugene propose des évals concrètes, calibrées par tâche (classification, résumé, traduction, toxicité), sans jamais abandonner l'évaluation humaine.
- 🟡 **[LLM-as-a-judge](../fiches/llm-as-a-judge.md)** — utiliser un LLM, guidé par une rubrique de critères, pour noter automatiquement les sorties d'un agent quand il n'existe pas de vérité terrain à comparer.
- 🟡 **[LLM-evaluators (juges LLM) — vue d'Eugene](../fiches/llm-evaluators.md)** — Synthèse de deux douzaines d'articles sur les LLM-as-a-Judge : quand et comment les utiliser, leurs biais connus, et comment les aligner sur des critères humains.

### 🔐 Sécurité
- 🔴 **[Sécurité agentique](../fiches/securite-agentique.md)** — la surface d'attaque d'un agent (décision autonome + appel d'outils) est bien plus large que celle d'un LLM seul, et appelle des contre-mesures de type Zero Trust, moindre privilège et sandbox.
- 🟡 **[Garde-fou en nœud d'entrée (Granite Guardian)](../fiches/guardrail-noeud-entree.md)** — placer un détecteur de modération (HAP/PII via Granite Guardian) comme tout premier nœud du graphe, et router via une arête conditionnelle pour bloquer le contenu indésirable AVANT qu'il n'atteigne le LLM et les outils.

### ⚖️ Gouvernance, alignement & ops
- 🔴 **[Observabilité LLM : best practices (indépendantes de l'outil)](../fiches/observabilite-llm-best-practices.md)** — instrumenter une app LLM, ce n'est pas brancher un dashboard : c'est décider *quoi* tracer (span par étape de chaîne), *comment* évaluer la qualité sans se ruiner ni se mentir (juge calibré, échantillonné), et *quoi ne pas ingérer* (PII) — l'outil n'est que le réceptacle.
<!-- /AUTO -->
