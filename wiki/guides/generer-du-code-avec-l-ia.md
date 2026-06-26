---
type: guide
titre: "Générer du code avec l'IA"
objectif: generer-code
description: "Parcours transverse : concepts et pratiques pour produire du code avec des agents IA, du cadrage à la vérification."
---

# 🧑‍💻 Générer du code avec l'IA

> **Guide par objectif (L3)** — un parcours transverse aux thèmes pour répondre à : *comment produire du code efficacement avec l'IA ?*
> Cette page réunit les **concepts/pratiques** (parcours ci-dessous) et les **outils** (section en bas de page).

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

## Outils pour cet objectif

<!-- AUTO-OUTILS:objectif=generer-code -->
> ⚙️ **Outils générés** — 48 outil(s) `objectifs: [generer-code]`, groupés par famille. Régénéré par `tools/build_index.py` depuis le frontmatter des fiches outils.

<a id="fam-agents-ide-qui-codent"></a>
### Agents & IDE qui codent

*Font le travail de codage — ou orchestrent les agents qui le font.*

| Outil | Type | Éco | Coût LLM | En bref |
|---|---|:--:|:--:|---|
| **[Continue](https://www.continue.dev/)** · [📄](../fiches%20outils/continue.md) | Extension IDE (VS Code / JetBrains) + CLI | 🔓 | 🔑 | Assistant de codage IA open-source (Apache 2.0), **model-agnostic** (BYOK), + Continue Hub (assistants/règles/modèles partagés). Principale alternative OSS à Copilot/Cursor. ⚠️ **Racheté par Cursor** (avr. 2026) → produit standalone en arrêt, le code OSS subsiste |
| **[Kilo Code](https://kilo.ai/)** · [📄](../fiches%20outils/kilo-code.md) | Extension IDE / CLI | 🔓🎁💳 | 🔑💸 | Agent de codage IA open-source (VS Code, JetBrains, CLI) ; 500+ modèles, tokens au prix coûtant via gateway ou BYOK |
| **[Trae](https://www.trae.ai/)** · [📄](../fiches%20outils/trae.md) | Application (IDE) | 🎁🔁 | 📦💸 | IDE IA de ByteDance basé sur VS Code ; modèles premium (Claude, GPT, DeepSeek) fournis via un système de **crédits** (tokens × tarif modèle, plafond par palier), abonnements Lite/Pro/Pro+/Ultra 3–100 $/mois |

<a id="fam-assistants-ia-pour-terminal-shell"></a>
### Assistants IA pour terminal / shell

*Compagnons IA conversationnels intégrés au terminal : exécution de commandes (avec garde-fou), analyse système, aide CLI.*

| Outil | Type | Éco | Coût LLM | En bref |
|---|---|:--:|:--:|---|
| **[Neo-AI](https://github.com/Vasco0x4/Neo-AI)** · [📄](../fiches%20outils/neo-ai.md) | CLI — assistant IA pour terminal Linux | 🔓 | 🟢🔑 | Assistant IA pour terminal Linux open-source (BSD-3, Python, par Vasco0x4) : exécute des commandes avec contexte + approbation, analyse système (logs, fichiers, santé), volet cybersécurité (scan réseau, CTF). LLM local (LM Studio) ou cloud (OpenAI/Claude). ⚠️ Beta, Linux |

<a id="fam-automatisation-de-navigateur-serveurs-mcp"></a>
### Automatisation de navigateur (serveurs MCP)

*Pilotent un navigateur depuis l'agent — surtout pour **tester** les applis web qu'on développe (et scraping/contrôle). Coût LLM côté client → 🟢.*

| Outil | Type | Éco | Coût LLM | En bref |
|---|---|:--:|:--:|---|
| **[Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)** · [📄](../fiches%20outils/chrome-devtools-mcp.md) | Serveur MCP (automatisation navigateur) | 🔓 | 🟢 | Serveur MCP officiel de l'équipe Chrome (Google, Apache 2.0) pilotant Chrome via CDP + Puppeteer ; se démarque par les **traces de performance** et le débogage réseau/DOM/console |
| **[Firefox DevTools MCP](https://github.com/freema/firefox-devtools-mcp)** · [📄](../fiches%20outils/firefox-devtools-mcp.md) | Serveur MCP (automatisation / inspection navigateur) | 🔓 | 🟢 | Serveur MCP open-source (TypeScript) pour piloter/inspecter Firefox via WebDriver BiDi : navigation, DOM, réseau, console, screenshots, eval JS, préférences/extensions. Tests, scraping, contrôle navigateur. Local uniquement (Firefox + Node). Double licence MIT/Apache 2.0 |
| **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** · [📄](../fiches%20outils/playwright-mcp.md) | Serveur MCP (automatisation navigateur) | 🔓 | 🟢 | Serveur MCP officiel Microsoft (Apache 2.0) pilotant Chromium/Firefox/WebKit via l'**arbre d'accessibilité** (pas des screenshots) → rapide et économe en tokens. Tests, scraping, contrôle navigateur |
| **[Puppeteer MCP](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer)** · [📄](../fiches%20outils/puppeteer-mcp.md) | Serveur MCP (automatisation navigateur) | 🔓 | 🟢 | ⚠️ **Déprécié/archivé (mai 2025)** : serveur MCP de référence pilotant Chromium via Puppeteer (7 outils), vulnérabilités connues. Successeurs recommandés : Chrome DevTools MCP / Playwright MCP |

<a id="fam-ci-cd-livraison-operations-assistes-par-ia"></a>
### CI/CD, livraison & opérations assistés par IA

*Le **bout droit** du SDLC : **livrer** le code (CI/merge/tests flaky) et **exploiter** la prod (**AI SRE** : investigation d'incidents, RCA, self-healing). ⚠️ Le volet ops déborde vers « exploiter un produit » (frontière avec *embarquer l'IA dans un produit*). LLM exécuté par l'éditeur (SaaS) → **📦 inclus** ; les AI SRE sont surtout **enterprise / sur devis**.*
> **Candidats non vérifiés** (à arbitrer, cf. `outils candidats.md`) : **Datadog Bits AI Dev Agent** (fix autonome de flaky → draft PR), **Aviator**, **Trunk** (CI/flaky) ; **Rootly**, **PagerDuty AIOps** (incident/AIOps).

| Outil | Type | Éco | Coût LLM | En bref |
|---|---|:--:|:--:|---|
| **[Cleric](https://cleric.ai/)** · [📄](../fiches%20outils/cleric.md) | Plateforme SaaS — AI SRE (investigation d'incidents) | 🔒 | 📦 | Agent **AI SRE** : enquête d'incidents, RCA, recommandations ; branché sur ta stack (Datadog/Grafana/PagerDuty…). **Read-only par défaut**, write quand prêt. Gartner Cool Vendor 2025. Enterprise / sur devis |
| **[Mergify](https://mergify.com/)** · [📄](../fiches%20outils/mergify.md) | Plateforme SaaS — merge queue & CI (détection de tests flaky) | 🎁🔁 | 📦 | Merge queue (« keep main green ») + CI Insights (auto-retry) + Test Insights (détecte/quarantaine/corrige les tests **flaky**) + Stacks. Cœur surtout déterministe (IA légère sur le flaky). Freemium (gratuit OSS, payant par contributeur — prix exacts à vérifier) |
| **[Resolve.ai](https://resolve.ai/)** · [📄](../fiches%20outils/resolve-ai.md) | Plateforme SaaS — AI SRE / ingénierie de production | 🔒 | 📦 | Agents IA d'astreinte/incident/prod (objectif ~80 % d'auto-résolution, garde-fous) ; sécurité entreprise (SSO/RBAC, pas d'entraînement sur tes données). Clients Coinbase/DoorDash… Enterprise / sur devis |
| **[Traversal](https://traversal.com/)** · [📄](../fiches%20outils/traversal.md) | Plateforme SaaS — AI SRE (RCA à grande échelle) | 🔒 | 📦 | « AI SRE pour systèmes complexes » : World Model + Causal Search pour la RCA à grande échelle, triage, self-healing ; option **BYOC** (ton cloud). Git/monitoring/incident. Enterprise / sur devis |

<a id="fam-connaissance-du-code-graphes-recherche-memoire"></a>
### Connaissance du code : graphes, recherche & mémoire

*Donnent à l'agent une compréhension structurée du projet (et de l'historique), en réduisant le contexte à charger.*

| Outil | Type | Éco | Coût LLM | En bref |
|---|---|:--:|:--:|---|
| **[Agent Booster](https://github.com/sseshachala/agent-booster)** · [📄](../fiches%20outils/agent-booster.md) | Serveur MCP / CLI | 🔓 | 🟢 | Index de **symboles** (tree-sitter + embeddings **locaux** `all-MiniLM-L6-v2`) qui détourne les *Read* de l'agent : renvoie les symboles pertinents au lieu du fichier entier → 60–90 % de tokens en moins. Hooks pour Claude Code/Cursor/Windsurf/Codex ; MIT, sans LLM ni clé. ⚠️ Homonyme du `agent-booster` de ruvnet (autre produit) |
| **[Cavemem](https://github.com/JuliusBrussee/cavemem)** · [📄](../fiches%20outils/cavemem.md) | Serveur MCP / CLI (+ hooks IDE) | 🔓 | 🟢🔑 | Mémoire persistante cross-agent (CLI + MCP + hooks IDE) ; événements de session compressés (~75 %), SQLite local, interrogeable via MCP. Aucun LLM génératif ; embeddings **locaux par défaut** (🟢), provider distant **OpenAI** optionnel = clé requise (🔑) |
| **[CodeGraph](https://colbymchenry.github.io/codegraph/)** · [📄](../fiches%20outils/codegraph.md) | Serveur MCP / CLI | 🔓 | 🟢 | Indexe une codebase en graphe de connaissances local (tree-sitter + SQLite) exposé aux agents via MCP ; déterministe, sans LLM, réduit tool calls et tokens |
| **[Graphify](https://graphify.net/)** · [📄](../fiches%20outils/graphify.md) | Skill (assistants de codage IA / Claude Code) | 🔓 | 🟢 | Skill open-source (Claude Code) construisant un graphe de connaissances multi-modal (code, docs, PDF, images) via tree-sitter + extraction sémantique LLM ; consomme des tokens à l'indexation |
| **[GraphMind](https://getgraphmind.com/)** · [📄](../fiches%20outils/graphmind.md) | Application desktop / Serveur MCP / CLI | 🔓🎁 | 🟢🔑 | Transforme la codebase en graphe de connaissances + mémoire persistante cross-session ; 25 outils MCP, jusqu'à 5 700× moins de tokens que grep. Pas de LLM génératif ; embeddings **locaux gratuits** (🟢) ou **distants Voyage/OpenAI** sur tiers payants (🔑). Core MIT gratuit, abonnements 9–19 €/mois. Made in Paris |
| **[Polaris (polarismcp.com)](https://polarismcp.com/)** · [📄](../fiches%20outils/polaris.md) | Serveur MCP / CLI | 🔓 | 🟢 | Serveur MCP de recherche sémantique locale dans la doc projet (embeddings ONNX, hybride vecteur+BM25) ; sans LLM ni cloud, réduit les tokens 10–40×. Core MIT, Pro payant en préparation |
| **[Serena](https://github.com/oraios/serena)** · [📄](../fiches%20outils/serena.md) | Serveur MCP / toolkit d'agent de codage | 🔓 | 🟢 | Toolkit MCP (Python, Oraios) donnant aux agents des capacités IDE via LSP : recherche **et édition/refactoring** sémantiques au niveau symbole sur 40+ langages (pas du grep). MIT open-source (plugin JetBrains payant en option), BYO client |

<a id="fam-documentation-sources-de-connaissances-externes-serveurs-mcp"></a>
### Documentation & sources de connaissances externes (serveurs MCP)

*Servent à l'agent des **connaissances externes à jour** — doc de librairies, repos GitHub, doc éditeur (Microsoft/AWS), web — pour produire du code juste sans halluciner les signatures. Tournent dans l'agent (coût LLM côté client → 🟢) et visent à *réduire* les tokens. ⚠️ Exception : **Exa** s'appuie sur une API de recherche **payante à l'usage** (coût distinct du LLM).*

| Outil | Type | Éco | Coût LLM | En bref |
|---|---|:--:|:--:|---|
| **[AWS Documentation MCP](https://github.com/awslabs/mcp)** · [📄](../fiches%20outils/aws-documentation-mcp.md) | Serveur MCP local (doc AWS officielle) | 🔓 | 🟢 | Serveur MCP **officiel AWS Labs (Apache 2.0)** : recherche/lecture de la **doc AWS** officielle, API refs, What's New (stdio local). Gratuit, open-source ; un des serveurs du repo `awslabs/mcp`. Install 1-clic (Cursor, VS Code, Kiro) |
| **[Context7](https://context7.com/)** · [📄](../fiches%20outils/context7.md) | Serveur MCP (doc de librairies) — open-source + hébergé | 🔓🎁 | 🟢 | Serveur MCP **open-source (MIT, Upstash)** injectant la **doc à jour et versionnée** des librairies + exemples de code (`resolve-library-id`, `query-docs`). Hébergé (`mcp.context7.com`) ou local ; gratuit, clé API gratuite pour + de quota. 30+ agents. **Déjà connecté dans cette session** |
| **[Exa MCP](https://github.com/exa-labs/exa-mcp-server)** · [📄](../fiches%20outils/exa-mcp.md) | Serveur MCP (recherche web / neuronale) | 🔓💳 | 🟢 | Donne à l'agent la **recherche web/code/entreprise** via l'API neuronale **Exa** (`web_search_exa`, `web_fetch_exa`). Serveur MCP **MIT** gratuit, mais **clé Exa requise** (API payante à l'usage, tier gratuit). Plus large que la doc de libs. 🟢 côté LLM, mais coût de recherche Exa à l'usage |
| **[GitMCP](https://gitmcp.io/)** · [📄](../fiches%20outils/gitmcp.md) | Serveur MCP distant (repo GitHub → MCP) | 🔓 | 🟢 | Transforme **n'importe quel repo GitHub** en serveur MCP distant : remplacer `github.com` par `gitmcp.io` → l'agent lit `llms.txt`/`readme` pour le contexte. Gratuit (idosal/git-mcp). ⚠️ Licence non confirmée à la source |
| **[Microsoft Learn MCP](https://learn.microsoft.com/training/support/mcp)** · [📄](../fiches%20outils/microsoft-learn-mcp.md) | Serveur MCP distant (doc Microsoft officielle) | 🔒 | 🟢 | Serveur MCP **officiel Microsoft** (HTTP streamable) servant la doc Microsoft/Azure officielle (service « Ask Learn », refresh quotidien) : recherche doc, article complet, exemples. **Gratuit, sans authentification** ; propriétaire (service hébergé) |
| **[Ref (ref.tools)](https://ref.tools/)** · [📄](../fiches%20outils/ref.md) | Serveur MCP (documentation technique à jour) | 🎁🔁 | 🟢 | Sert aux agents la **doc technique à jour** (libs/APIs publiques + repos/PDF privés), pré-chunkée → *juste les tokens utiles* (réduit le « context rot »). Client MCP open-source ; service hébergé freemium (Free 200 crédits → Basic 19 $, Pro 50 $, Max 200 $/mois). Voisin de Context7 |

<a id="fam-orchestrateurs-systemes-multi-agents-de-codage"></a>
### Orchestrateurs & systèmes multi-agents de codage

*Pilotent plusieurs agents de codage — en parallèle (flottes en worktrees git isolés) ou en pipeline discipliné avec revue adverse.*

| Outil | Type | Éco | Coût LLM | En bref |
|---|---|:--:|:--:|---|
| **[Conductor](https://www.conductor.build/)** · [📄](../fiches%20outils/conductor.md) | Application desktop Mac (orchestrateur d'agents de codage) | 🔒 | 🟢 | App Mac (Melty Labs, YC) qui lance en parallèle plusieurs agents Claude Code/Codex/Cursor dans des worktrees git isolés ; review et merge centralisés. **Gratuite mais propriétaire** (Enterprise à venir), utilise ton abonnement Claude/Codex existant. macOS + GitHub uniquement |
| **[Crystal](https://github.com/stravu/crystal)** · [📄](../fiches%20outils/crystal.md) | Application desktop (Electron) — orchestrateur d'agents | 🔓 | 🟢 | App Electron (Stravu, **MIT**) lançant plusieurs sessions **Claude Code / Codex en parallèle** dans des worktrees git isolés ; test/compare/merge. BYO agent. ⚠️ **Déprécié (fév. 2026)** → successeur **Nimbalyst** |
| **[Liza](https://github.com/liza-mas/liza)** · [📄](../fiches%20outils/liza.md) | CLI (Go) — système multi-agents de codage | 🔓 | 🟢 | Système multi-agents de codage *discipliné* (Apache 2.0, Go) : encadre des agents existants (Claude Code, Codex, Gemini…) avec contrats comportementaux, paires adverses doer/reviewer et superviseurs déterministes ; neutralise 55+ modes d'échec LLM, pipeline autonome spec→code. BYO agent |
| **[Multica](https://multica.ai/)** · [📄](../fiches%20outils/multica.md) | Plateforme « managed agents » (orchestration d'agents de codage) | 🔓🔒 | 🟢 | Plateforme « managed agents » en Go (~37k★) gérant les agents de codage comme des coéquipiers : board de tâches, file, skills réutilisables, dashboard multi-runtime (local + cloud), 12 agents (Claude Code, Codex, Cursor…). Self-host ou Multica Cloud (pas de pricing public). ⚠️ Licence Apache 2.0 **modifiée** (clause anti-service-tiers → pas OSI). Le code ne passe pas par leurs serveurs. BYO agent |
| **[Orca](https://www.onorca.dev/)** · [📄](../fiches%20outils/orca.md) | Application desktop (Mac/Win/Linux) + mobile — Agent Development Environment (ADE) | 🔓 | 🟢 | « Agent Development Environment » open-source (stablyai, YC) pour piloter une flotte d'agents de codage en parallèle : board Kanban, worktrees git isolés, terminaux WebGL, navigateur Chromium intégré, worktrees SSH, intégrations GitHub/Linear. Gratuit MIT, BYO agent (25+) |
| **[Ruflo](https://github.com/ruvnet/ruflo)** · [📄](../fiches%20outils/ruflo.md) | Meta-harnais / framework d'orchestration multi-agents pour Claude (open source, npm) | 🔓 | 🟢🔑 | Meta-harnais multi-agents open-source (MIT, ex-Claude Flow) qui transforme Claude Code en essaim : 60–100+ agents, ~215 outils MCP, routage ML, mémoire HNSW. 🟢 via Claude Code (mode plugin, sans clé) ou 🔑 BYOK multi-provider (OpenRouter/Ollama…) en mode autonome ; mise sur la *largeur* (vs la *profondeur* de Liza) |
| **[Sculptor](https://imbue.com/sculptor/)** · [📄](../fiches%20outils/sculptor.md) | Application desktop Mac — orchestrateur d'agents | 🔒 | 🟢🔑 | App Mac (Imbue) orchestrant des agents **Claude Code en conteneurs Docker isolés** + Pairing Mode (test local instantané) + dev containers (démarrage en secondes). **Gratuit en beta**, propriétaire. BYO Anthropic (clé API ou abonnement Claude Pro/Max) |
| **[Supacode](https://supacode.sh/)** · [📄](../fiches%20outils/supacode.md) | Application desktop macOS native (orchestrateur d'agents de codage) | 🔓🔒 | 🟢 | App macOS native (sur libghostty, pas Electron) orchestrant 50+ agents de codage en parallèle dans des worktrees isolés ; « infinite canvas terminal board ». **Source-available (FSL-1.1, devient Apache-2.0 à 2 ans)**, beta gratuite, BYO agent. macOS 26 Tahoe requis |
| **[Superset (superset-sh)](https://github.com/superset-sh/superset)** · [📄](../fiches%20outils/superset.md) | Application desktop (orchestrateur d'agents de codage) | 🔓🔒 | 🟢 | App Electron « IDE pour l'ère des agents » : orchestre en parallèle plusieurs agents de codage CLI (Claude Code, Codex, Cursor…) dans des worktrees git isolés. Source-available (Elastic License 2.0). **BYO agent** : pilote tes agents existants (pas de clé LLM propre). ⚠️ ≠ Apache Superset (BI) |
| **[Vibe Kanban](https://www.vibekanban.com/)** · [📄](../fiches%20outils/vibe-kanban.md) | Plateforme kanban / orchestration d'agents de codage (web) | 🔓 | 🟢 | Kanban d'orchestration (Bloop AI, **Apache-2.0**, ~27k★) : board planning→progress→review→done, exécution parallèle en worktrees git, navigateur intégré ; 10+ agents (Claude Code, Codex, Gemini, OpenCode, Cursor, Aider…). Gratuit, BYO agent. ⚠️ Produit commercial en *sunsetting* → désormais open-source communautaire |

<a id="fam-revue-de-code-par-ia"></a>
### Revue de code par IA

*Reviewers IA qui relisent les PR (résumé, bugs, sécurité) — le levier clé quand les agents produisent plus de code qu'on n'en relit. Le LLM est **fourni dans le prix** (📦), pas en BYOK. Cadre conceptuel : [📄 revue de code agentique](../fiches/revue-de-code-agentique.md).*
> **À retenir** : faible recouvrement entre outils (~93 % des findings ne sont vus que par un seul des 4) → en combiner plusieurs aux forces complémentaires (précision vs recall) ; traiter leurs verdicts comme des **signaux**, l'humain garde le merge.

| Outil | Type | Éco | Coût LLM | En bref |
|---|---|:--:|:--:|---|
| **[CodeRabbit](https://www.coderabbit.ai/)** · [📄](../fiches%20outils/coderabbit.md) | Service web (app GitHub/GitLab) + IDE / CLI | 🎁🔁💳 | 📦 | Reviewer IA de PR (GitHub/GitLab) : résumés, revue ligne à ligne, linters + SAST, fix en 1 clic. **Gratuit à vie pour repos publics** ; Pro 24 $, Pro Plus 48 $/user/mois, Enterprise (SSO, self-host). Meilleur **recall** au benchmark Martian (~49 % précision). LLM inclus |
| **[Cursor BugBot](https://cursor.com/bugbot)** · [📄](../fiches%20outils/cursor-bugbot.md) | Service web (app GitHub) | 🔒🔁💳 | 📦 | Reviewer IA de PR d'Anysphere (Cursor) ciblant les **bugs de logique** avec peu de faux positifs (orienté **précision**) ; modèles frontier + maison. Historiquement 40 $/user/mois → **bascule à l'usage** (~1–1,50 $/run, post-8 juin 2026). Compte Cursor requis |
| **[Greptile](https://www.greptile.com/)** · [📄](../fiches%20outils/greptile.md) | Service web (app GitHub) | 🎁🔁💳 | 📦 | Reviewer IA de PR avec **compréhension de toute la codebase** (fort sur l'architecture/contexte) ; ~82 % de bugs attrapés (recall > précision). Pro 30 $/seat/mois (50 revues incluses, +1 $/revue), Enterprise (self-host). Gratuit pour l'OSS qualifié, -50 % startups |
| **[Sentry Seer](https://docs.sentry.io/product/ai-in-sentry/seer/)** · [📄](../fiches%20outils/sentry-seer.md) | Service web (add-on de Sentry) | 🔒🔁💳 | 📦 | Agent IA de debugging de Sentry (Autofix, agent conversationnel, **Code Review**) : prédit les défaillances avant merge, fort sur la **sévérité prod** (adossé à ta télémétrie Sentry). Add-on facturé par contributeur actif (2+ PR/mois). LLM inclus |

<a id="fam-workflow-methodologie-developpement-spec-driven"></a>
### Workflow, méthodologie & développement spec-driven

*Structurent le processus de dev assisté par IA (méthodologies, rôles, specs, workflows guidés) par-dessus un agent existant.*

| Outil | Type | Éco | Coût LLM | En bref |
|---|---|:--:|:--:|---|
| **[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)** · [📄](../fiches%20outils/bmad-method.md) | Framework / méthodologie (agents IA pour IDE) | 🔓 | 🟢 | Méthodologie open-source (MIT, ~49k★) de dev agile piloté par IA : 21 agents-personas et 50+ workflows guidés, du brainstorming au déploiement, dans ton IDE (Claude Code, Cursor). BYOK |
| **[Cavekit](https://github.com/JuliusBrussee/cavekit)** · [📄](../fiches%20outils/cavekit.md) | Plugin (Claude Code) + skills | 🔓 | 🟢 | Plugin Claude Code de développement spec-driven : specs durables survivant aux resets de contexte, backprop des échecs de test ; encodage « caveman » pour réduire les tokens |
| **[ECC](https://github.com/affaan-m/ECC)** · [📄](../fiches%20outils/ecc.md) | Système de harness d'agent (skills/agents/hooks/rules) — multi-plateforme, OSS + GitHub App | 🔓🎁🔁 | 🟢🔑 | « Operator system » tout-en-un (MIT) : 261 skills, 67 agents, hooks, instincts appris, mémoire, AgentShield, multi-harness (Claude Code/Cursor/Codex…). ECC Pro 19 $/siège/mois (repos privés). ⚠️ Très jeune (créé 2026-01) malgré le discours « production » ; **maximaliste**, en tension avec sa propre règle « <10 MCP/<80 outils » ; mono-mainteneur ; 220k★ en 5 mois = hype ≠ valeur prouvée ; métriques internes auto-déclarées. Peers plus focalisés (Superpowers, Spec Kit) souvent préférables |
| **[GitHub Spec Kit](https://github.com/github/spec-kit)** · [📄](../fiches%20outils/spec-kit.md) | Toolkit CLI (spec-driven development) | 🔓 | 🟢 | Toolkit **officiel GitHub** (MIT) de spec-driven dev : CLI `Specify` + commandes `/speckit.*` (constitution→spec→plan→tasks→implement) par-dessus ton agent (Claude Code, Copilot, Cursor, Gemini, Codex, 24+). Pas de LLM propre |
| **[GSD (Get Shit Done)](https://github.com/open-gsd/gsd-core)** · [📄](../fiches%20outils/gsd.md) | Framework de méta-prompting / spec-driven development pour agents de codage (couche par-dessus Claude Code & autres) | 🔓 | 🟢 | Framework open-source (MIT) de spec-driven dev par tâches : combat la dégradation de contexte en spawnant des sous-agents à contexte frais ; BYOK. **⚠️ Créateur d'origine (TÂCHES) lié à un rug-pull crypto $GSD + packages npm d'origine abandonnés → n'utiliser que la continuation communautaire `open-gsd` (voir fiche)** |
| **[gstack](https://github.com/garrytan/gstack)** · [📄](../fiches%20outils/gstack.md) | Suite de skills / workflow open-source pour agents de codage IA (Claude Code et compatibles) | 🔓 | 🟢 | Config Claude Code open-source de Garry Tan (YC) : 23+ skills « opinionated » faisant jouer à l'agent les rôles d'une équipe (CEO, Designer, QA…) pour démultiplier le dev solo |
| **[Pheromind](https://github.com/ChrisRoyse/Pheromind)** · [📄](../fiches%20outils/pheromind.md) | Framework d'orchestration multi-agents (swarm) | 🔓 | 🟢 | Orchestration multi-agents par **« intelligence en essaim à base de phéromones »** (coordination indirecte via un médium partagé) au-dessus d'un agent existant. ⚠️ **Statut flou** : repo public mais IP/offre commerciale revendiquée, licence non confirmée — arbitrer prudemment |
| **[Superpowers](https://github.com/obra/superpowers)** · [📄](../fiches%20outils/superpowers.md) | Plugin / framework de skills agentiques (multi-plateforme) | 🔓 | 🟢 | Framework de skills agentiques + méthodologie de dev par Jesse Vincent (obra), ~93k★, n°1 des plugins Claude Code : impose brainstorming, worktrees, TDD, revue par sous-agents. Multi-plateforme, MIT, tourne dans ton agent |
| **[Task Master (Taskmaster)](https://github.com/eyaltoledano/claude-task-master)** · [📄](../fiches%20outils/task-master.md) | CLI + Serveur MCP (gestion de tâches pour agents) | 🔓🎁 | 🟢🔑 | Transforme un PRD en **tâches structurées** (dépendances, priorités) ; CLI + MCP intégré à Claude Code, Cursor, Windsurf (~25k★). Cœur MIT gratuit (BYOK 15+ providers) ; offre équipe payante **Hamster Studio** (+ mode hébergé sans clé) |
<!-- /AUTO-OUTILS -->
