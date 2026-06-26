---
type: index
titre: "Thème — Évaluation"
theme: evaluation
---

# 📊 Évaluation

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Mesurer la qualité : évals, juges LLM, analyse d'erreurs._

## Concepts (14)

### 🔴 Substance / cœur
- **[Data flywheel : collecte de feedback](../fiches/data-flywheel-feedback.md)** — la donnée de production est le seul actif durable d'un produit LLM : capter le feedback utilisateur (explicite et implicite) crée un *flywheel* qui alimente à la fois les évals, le fine-tuning et les guardrails — l'avantage compétitif qui ne se copie pas.
- **[Error analysis : regarde tes données](../fiches/error-analysis.md)** — Avant toute métrique, lis manuellement les traces de ton produit, annote les comportements indésirables, puis construis une taxonomie des failure modes et compte leur fréquence.
- **[Eval-driven development](../fiches/eval-driven-development.md)** — Construire un système d'évaluation spécifique à ton domaine est la fondation d'un produit IA : c'est lui qui crée la flywheel données → évals → amélioration et débloque le reste.
- **[LLM-as-a-judge : le faire correctement](../fiches/llm-as-judge-correct.md)** — Un LLM-as-a-judge n'a de valeur que s'il est aligné sur le jugement binaire pass/fail d'un expert métier via un protocole itératif (« Critique Shadowing »), pas via des scores 1-5 arbitraires.
- **[Patterns pour systèmes LLM en production](../fiches/patterns-systemes-llm.md)** — Sept patterns pratiques pour transformer une démo LLM en produit fiable, organisés selon deux axes : améliorer la performance vs réduire coût/risque, et proche de la donnée vs proche de l'utilisateur.
- **[Revue de code agentique : de l'écriture à la vérification](../fiches/revue-de-code-agentique.md)** — Quand les agents génèrent du code plus vite qu'on ne le lit, le goulot d'étranglement passe de l'écriture à la **vérification** : la revue devient la compétence la plus à fort levier, et l'humain passe « in the loop » à « on the loop ».
- **[Évaluation de trajectoire](../fiches/evaluation-trajectoire.md)** — évaluer la suite des décisions, appels d'outils et étapes intermédiaires qu'a empruntées l'agent, pas seulement la qualité de sa réponse finale.
- **[Évaluer les LLM (évals spécifiques à la tâche)](../fiches/evaluer-les-llm.md)** — Les évals « sur étagère » corrèlent mal avec la performance applicative ; Eugene propose des évals concrètes, calibrées par tâche (classification, résumé, traduction, toxicité), sans jamais abandonner l'évaluation humaine.

### 🟡 Tradeoff / intermédiaire
- **[Contextual Retrieval](../fiches/contextual-retrieval.md)** — préfixer chaque chunk d'un court contexte (situant le chunk dans son document) *avant* l'embedding, pour réduire les échecs de récupération dus à des chunks ambigus.
- **[LLM-as-a-judge](../fiches/llm-as-a-judge.md)** — utiliser un LLM, guidé par une rubrique de critères, pour noter automatiquement les sorties d'un agent quand il n'existe pas de vérité terrain à comparer.
- **[LLM-evaluators (juges LLM) — vue d'Eugene](../fiches/llm-evaluators.md)** — Synthèse de deux douzaines d'articles sur les LLM-as-a-Judge : quand et comment les utiliser, leurs biais connus, et comment les aligner sur des critères humains.
- **[Reviewers hétérogènes : faible recouvrement entre outils](../fiches/reviewers-heterogenes.md)** — Les reviewers de code IA se recoupent très peu : il ne faut pas chercher « le meilleur » outil mais en faire tourner plusieurs aux forces complémentaires, comme un ensemble.
- **[Tool retrieval (RAG sur les outils)](../fiches/tool-retrieval.md)** — quand on a des centaines d'outils, en **récupérer dynamiquement** un sous-ensemble pertinent par requête au lieu de tous les exposer dans le prompt.

### 🟢 Survol / introductif
- **[RAG (Retrieval-Augmented Generation)](../fiches/rag.md)** — au lieu de répondre depuis sa seule mémoire d'entraînement, le LLM **récupère des passages pertinents dans une base externe** et les injecte dans le contexte pour ancrer sa réponse sur des sources.

## Outils (9)

- **[Arize Phoenix / Arize AX](../fiches%20outils/phoenix-arize.md)** — _Bibliothèque/app open-source (Phoenix) + Service web SaaS (Arize AX)_
- **[Braintrust](../fiches%20outils/braintrust.md)** — _Service web (SaaS) + SDK_
- **[CodeRabbit](../fiches%20outils/coderabbit.md)** — _Service web (app GitHub/GitLab) + IDE / CLI_
- **[Cursor BugBot](../fiches%20outils/cursor-bugbot.md)** — _Service web (app GitHub)_
- **[dupehound](../fiches%20outils/dupehound.md)** — _CLI / Serveur MCP_
- **[Greptile](../fiches%20outils/greptile.md)** — _Service web (app GitHub)_
- **[Langfuse](../fiches%20outils/langfuse.md)** — _Service web (cloud) + self-host open-source_
- **[LangSmith](../fiches%20outils/langsmith.md)** — _Service web (SaaS) + SDK_
- **[Sentry Seer](../fiches%20outils/sentry-seer.md)** — _Service web (add-on de Sentry)_
