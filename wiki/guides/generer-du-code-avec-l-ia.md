---
type: guide
titre: "Générer du code avec l'IA"
objectif: generer-code
description: "Parcours transverse : concepts et pratiques pour produire du code avec des agents IA, du cadrage à la vérification."
---

# 🧑‍💻 Générer du code avec l'IA

> **Guide par objectif (L3)** — un parcours transverse aux thèmes pour répondre à : *comment produire du code efficacement avec l'IA ?*
> Côté **outils**, voir [produire du code](../produire-du-code.md). Ce guide couvre les **concepts & pratiques**.

## En bref

L'écriture de code n'est plus le goulot : l'agent en produit beaucoup, vite. Le travail se déplace vers **cadrer, orchestrer, et surtout vérifier**. Bien utiliser l'IA pour coder, c'est concevoir le **système** autour de l'agent (le contexte, la boucle, les garde-fous) et garder la **compréhension** de ce qui est produit — pas piloter chaque ligne.

## Parcours de lecture conseillé

1. **Changer de posture** — le centre de gravité passe de l'écriture à la vérification et au jugement. Commencer par [Revue de code agentique](../fiches/revue-de-code-agentique.md), puis la [Dette de compréhension](../fiches/dette-de-comprehension.md) (le risque à ne pas céder), et [Loop engineering](../fiches/loop-engineering.md) (concevoir le système plutôt que prompter à la main).
2. **Comprendre comment l'agent code** — [le cadre canonique de l'agent](../fiches/agent-architecture-canonique.md), [CodeAct](../fiches/codeact.md) (le code comme espace d'action), l'[interface agent-ordinateur (ACI)](../fiches/aci-agent-computer-interface.md) et le pattern [Deep Agents](../fiches/deep-agents.md).
3. **Cadrer & décomposer le travail** — choisir la bonne forme avec [workflows vs agents](../fiches/workflows-vs-agents.md) et les [patterns de workflow](../fiches/patterns-de-workflow.md), puis découper via les [techniques de décomposition](../fiches/decomposition-techniques.md) et le [prompt chaining](../fiches/prompt-chaining.md).
4. **Orchestrer plusieurs agents** — quand on passe à la flotte : [types d'orchestration](../fiches/orchestration-types.md) et [structures multi-agents](../fiches/structures-multi-agents.md).
5. **Vérifier & fiabiliser** — le cœur du métier désormais : [reviewers hétérogènes](../fiches/reviewers-heterogenes.md), [Chain-of-Verification](../fiches/chain-of-verification.md), [eval-driven development](../fiches/eval-driven-development.md), [Reflexion](../fiches/reflexion.md) et le [human-in-the-loop statique vs dynamique](../fiches/hitl-statique-dynamique.md).
6. **Garder le contrôle** — [hooks déterministes vs mémoire probabiliste](../fiches/hooks-deterministes-vs-memoire-probabiliste.md) pour ancrer les invariants hors du jugement du modèle.

## Toutes les fiches de cet objectif

<!-- AUTO:objectif=generer-code -->
> ⚙️ **Index généré** — 19 fiche(s) taguée(s) `objectifs: [generer-code]`, régénéré par `tools/build_index.py`. La prose ci-dessus est curée à la main.

### 🧱 Fondamentaux des agents
- 🔴 **[ACI : concevoir l'interface agent-ordinateur](../fiches/aci-agent-computer-interface.md)** — soigner la définition des outils (noms, descriptions, formats) avec autant d'attention que les prompts : l'interface agent-ordinateur (ACI) est, pour un agent, l'équivalent de l'IHM pour un humain.
- 🔴 **[Les 5 patterns de workflow composables (Anthropic)](../fiches/patterns-de-workflow.md)** — un catalogue de patterns composables, du plus simple au plus complexe, à assembler soi-même plutôt qu'à déléguer à un framework.
- 🔴 **[Workflows vs agents : la distinction architecturale d'Anthropic](../fiches/workflows-vs-agents.md)** — distinguer **workflows** (LLM et outils orchestrés par des chemins de code prédéfinis) et **agents** (le LLM dirige dynamiquement son propre processus), au lieu de tout appeler « agentique ».
- 🟡 **[Deep Agents (pattern)](../fiches/deep-agents.md)** — patron d'architecture d'agent pour les tâches **long-horizon** : au lieu d'une simple boucle « réfléchir → appeler un outil → observer », on combine **planification explicite + sous-agents à contexte isolé + système de fichiers comme mémoire externe + prompt système détaillé** pour tenir la distance sans saturer le contexte.

### 🧠 Raisonnement & planification
- 🟡 **[Autoréflexion / Reflexion](../fiches/reflexion.md)** — après un échec, l'agent rédige une critique de ce qui n'a pas marché et rejoue la tâche avec cette critique gardée en mémoire.
- 🟡 **[Chain-of-Verification (CoVe)](../fiches/chain-of-verification.md)** — le modèle écrit une réponse, en dérive des questions de vérification factuelle, y répond isolément, puis corrige sa réponse à la lumière de ces vérifications.

### ✍️ Prompting
- 🔴 **[Techniques de décomposition](../fiches/decomposition-techniques.md)** — Casser explicitement un problème complexe en sous-problèmes plus simples, puis les résoudre un à un, pour fiabiliser la réponse finale.
- 🟡 **[Prompt chaining](../fiches/prompt-chaining.md)** — décomposer une tâche complexe en une séquence de prompts simples où la sortie de chaque étape alimente la suivante.

### 🔧 Outils & function-calling
- 🔴 **[CodeAct (le code comme espace d'action)](../fiches/codeact.md)** — l'agent émet du **code Python exécutable** comme action, au lieu d'appels d'outils en JSON rigide.
- 🔴 **[Le cadre canonique : Agent = LLM + Planification + Mémoire + Outils](../fiches/agent-architecture-canonique.md)** — la décomposition de référence d'un agent autonome : un LLM joue le rôle de cerveau (contrôleur), épaulé par trois composants — planification, mémoire et usage d'outils.

### 👥 Multi-agents
- 🟡 **[Structures multi-agents : hiérarchique / holonique / coalition / équipe](../fiches/structures-multi-agents.md)** — quatre façons d'organiser les agents : arbre de commandement, tout-et-partie, alliance temporaire, ou équipe interdépendante.
- 🟡 **[Types d'orchestration des agents IA](../fiches/orchestration-types.md)** — quatre façons de répartir la prise de décision entre agents : un chef unique, un collectif sans chef, des couches hiérarchiques, ou des organisations qui collaborent sans se partager les données.

### 📊 Évaluation
- 🔴 **[Eval-driven development](../fiches/eval-driven-development.md)** — Construire un système d'évaluation spécifique à ton domaine est la fondation d'un produit IA : c'est lui qui crée la flywheel données → évals → amélioration et débloque le reste.
- 🔴 **[Revue de code agentique : de l'écriture à la vérification](../fiches/revue-de-code-agentique.md)** — Quand les agents génèrent du code plus vite qu'on ne le lit, le goulot d'étranglement passe de l'écriture à la **vérification** : la revue devient la compétence la plus à fort levier, et l'humain passe « in the loop » à « on the loop ».
- 🟡 **[Reviewers hétérogènes : faible recouvrement entre outils](../fiches/reviewers-heterogenes.md)** — Les reviewers de code IA se recoupent très peu : il ne faut pas chercher « le meilleur » outil mais en faire tourner plusieurs aux forces complémentaires, comme un ensemble.

### ⚖️ Gouvernance, alignement & ops
- 🔴 **[Loop engineering : concevoir le système qui prompte l'agent](../fiches/loop-engineering.md)** — Le levier passe du prompt engineering au *loop engineering* : au lieu de prompter l'agent à la main, on conçoit un système autonome qui découvre le travail, le distribue à des agents, vérifie, documente et décide de la suite — sans humain entre les cycles.
- 🟡 **[Dette de compréhension & cognitive surrender](../fiches/dette-de-comprehension.md)** — Plus une boucle d'agents livre vite du code que tu n'as pas écrit, plus l'écart grandit entre ce qui existe et ce que tu comprends — une « dette » qui, ignorée, glisse vers la « capitulation cognitive ».
- 🟡 **[Hooks déterministes vs mémoire probabiliste (Skills / Memory / Hooks)](../fiches/hooks-deterministes-vs-memoire-probabiliste.md)** — Pour qu'un agent de code respecte une règle, le mécanisme compte plus que la formulation : une instruction en mémoire (CLAUDE.md) est du **contexte probabiliste** que le modèle *peut* suivre, alors qu'un **hook** est une commande shell exécutée déterministiquement à un point du cycle de vie, qui *garantit* l'action quoi que décide le modèle — d'où la triade « Skills = conseil, Memory = rappel, Hooks = loi ».
- 🟡 **[Human-in-the-loop : interruptions statiques vs dynamiques](../fiches/hitl-statique-dynamique.md)** — deux mécanismes LangGraph pour insérer un humain dans la boucle : des breakpoints prédéterminés autour d'un nœud (statiques) ou un appel `interrupt()` déclenché depuis l'intérieur d'un nœud selon l'état (dynamiques).
<!-- /AUTO -->
