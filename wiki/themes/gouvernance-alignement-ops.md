---
type: index
titre: "Thème — Gouvernance, alignement & ops"
theme: gouvernance-alignement-ops
---

# ⚖️ Gouvernance, alignement & ops

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Piloter, observer et gouverner les systèmes en production._

## Concepts (13)

### 🔴 Substance / cœur
- **[AgentOps](../fiches/agentops.md)** — le DevOps/MLOps des agents : instrumenter l'exécution en session → trace → étendue (span) pour rendre observable une boîte noire non déterministe, avec coût et latence par étape et routage multi-LLM.
- **[Constitutional AI & RLAIF](../fiches/constitutional-ai-rlaif.md)** — aligner un modèle via un ensemble de **principes écrits** : le modèle critique et révise ses propres sorties selon la « constitution », et l'on entraîne sur ce feedback IA (RLAIF) au lieu d'annotations humaines (RLHF).
- **[DSPy](../fiches/dspy.md)** — « programmer, pas prompter » : on déclare des signatures et des modules en Python, et des optimiseurs compilent automatiquement les prompts contre un metric, au lieu de les rédiger et bricoler à la main.
- **[DSPy : compilation & bootstrapping](../fiches/dspy-compilation-bootstrap.md)** — compiler un programme DSPy, c'est laisser un teleprompter *bootstrapper* automatiquement de bonnes démonstrations en simulant le pipeline, en filtrant les traces qui passent le metric, puis en sélectionnant les meilleurs candidats — et le papier montre que ce processus fait passer des LM modestes de 4–20 % à 49–88 % d'accuracy sur GSM8K en quelques minutes.
- **[DSPy : signatures, modules, optimiseurs](../fiches/dspy-signatures-modules-optimiseurs.md)** — DSPy remplace les « prompt templates » codés en dur par trois abstractions composables — *signatures* déclaratives, *modules* paramétrés (Predict, ChainOfThought, ReAct…) et *teleprompters* (optimiseurs) — pour qu'on programme un pipeline LM au lieu de rédiger des prompts.
- **[Loop engineering : concevoir le système qui prompte l'agent](../fiches/loop-engineering.md)** — Le levier passe du prompt engineering au *loop engineering* : au lieu de prompter l'agent à la main, on conçoit un système autonome qui découvre le travail, le distribue à des agents, vérifie, documente et décide de la suite — sans humain entre les cycles.
- **[Observabilité LLM : best practices (indépendantes de l'outil)](../fiches/observabilite-llm-best-practices.md)** — instrumenter une app LLM, ce n'est pas brancher un dashboard : c'est décider *quoi* tracer (span par étape de chaîne), *comment* évaluer la qualité sans se ruiner ni se mentir (juge calibré, échantillonné), et *quoi ne pas ingérer* (PII) — l'outil n'est que le réceptacle.
- **[Résilience & fallback LLM](../fiches/resilience-fallback-llm.md)** — un appel LLM est un appel réseau vers un service tiers faillible (429, 5xx, timeout, dérive de qualité) : un produit sérieux applique les réflexes de fiabilité distribuée — *retry* avec backoff, *timeout*, *fallback* vers un autre modèle/fournisseur, *circuit breaker* et **dégradation gracieuse**.
- **[UX défensive (Defensive UX) pour produits LLM](../fiches/ux-defensive-llm.md)** — un LLM se trompe, hallucine et répond lentement *par construction* ; l'UX défensive conçoit l'interface en partant de cette faillibilité plutôt qu'en la niant — guider l'entrée, gérer l'erreur avec grâce, et garder l'humain aux commandes de la sortie.
- **[Éthique & gouvernance des agents](../fiches/ethique-gouvernance.md)** — aligner les agents sur des documents de politique en langage naturel et organiser une supervision où l'humain décide pendant que l'IA interroge, le tout encadré par des agents de gouvernance, des sandbox éthiques et un kill switch.

### 🟡 Tradeoff / intermédiaire
- **[Dette de compréhension & cognitive surrender](../fiches/dette-de-comprehension.md)** — Plus une boucle d'agents livre vite du code que tu n'as pas écrit, plus l'écart grandit entre ce qui existe et ce que tu comprends — une « dette » qui, ignorée, glisse vers la « capitulation cognitive ».
- **[Hooks déterministes vs mémoire probabiliste (Skills / Memory / Hooks)](../fiches/hooks-deterministes-vs-memoire-probabiliste.md)** — Pour qu'un agent de code respecte une règle, le mécanisme compte plus que la formulation : une instruction en mémoire (CLAUDE.md) est du **contexte probabiliste** que le modèle *peut* suivre, alors qu'un **hook** est une commande shell exécutée déterministiquement à un point du cycle de vie, qui *garantit* l'action quoi que décide le modèle — d'où la triade « Skills = conseil, Memory = rappel, Hooks = loi ».
- **[Human-in-the-loop : interruptions statiques vs dynamiques](../fiches/hitl-statique-dynamique.md)** — deux mécanismes LangGraph pour insérer un humain dans la boucle : des breakpoints prédéterminés autour d'un nœud (statiques) ou un appel `interrupt()` déclenché depuis l'intérieur d'un nœud selon l'état (dynamiques).

## Outils (18)

- **[Ansvar Compliance MCP (suite)](../fiches%20outils/ansvar-compliance-mcp.md)** — _Suite de serveurs MCP (sources de données réglementaires / juridiques)_
- **[Arize Phoenix / Arize AX](../fiches%20outils/phoenix-arize.md)** — _Bibliothèque/app open-source (Phoenix) + Service web SaaS (Arize AX)_
- **[Cleric](../fiches%20outils/cleric.md)** — _Plateforme SaaS — AI SRE (investigation d'incidents)_
- **[ECC](../fiches%20outils/ecc.md)** — _Système de harness d'agent (skills/agents/hooks/rules) — multi-plateforme, OSS + GitHub App_
- **[Helicone](../fiches%20outils/helicone.md)** — _Service web (proxy/gateway) + self-host open-source_
- **[Langfuse](../fiches%20outils/langfuse.md)** — _Service web (cloud) + self-host open-source_
- **[LangSmith](../fiches%20outils/langsmith.md)** — _Service web (SaaS) + SDK_
- **[LiteLLM](../fiches%20outils/litellm.md)** — _Bibliothèque Python (SDK) + Proxy/Gateway self-host (open-source) + Enterprise_
- **[Mergify](../fiches%20outils/mergify.md)** — _Plateforme SaaS — merge queue & CI (détection de tests flaky)_
- **[MindFlight Orchestrator (MFO)](../fiches%20outils/mindflight-orchestrator.md)** — _Plateforme (orchestration d'agents IA / automatisation d'entreprise)_
- **[OpenRouter](../fiches%20outils/openrouter.md)** — _Service web (gateway LLM hébergé)_
- **[Paperclip](../fiches%20outils/paperclip.md)** — _Plateforme open-source d'orchestration et de gouvernance d'agents IA (« zero-human companies »)_
- **[Portkey](../fiches%20outils/portkey.md)** — _AI Gateway open-source (MIT) self-host + Service web (SaaS managé)_
- **[Relay.app](../fiches%20outils/relay-app.md)** — _Automatisation de workflows avec IA + human-in-the-loop (SaaS)_
- **[Requesty](../fiches%20outils/requesty.md)** — _Service web (gateway LLM hébergé)_
- **[Resolve.ai](../fiches%20outils/resolve-ai.md)** — _Plateforme SaaS — AI SRE / ingénierie de production_
- **[Sentry Seer](../fiches%20outils/sentry-seer.md)** — _Service web (add-on de Sentry)_
- **[Traversal](../fiches%20outils/traversal.md)** — _Plateforme SaaS — AI SRE (RCA à grande échelle)_
