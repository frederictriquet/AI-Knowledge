# Q1 — Produire du code avec l'IA

> **Question** : comment utiliser l'IA pour **produire du code** ? Outils qui servent le *développeur pendant qu'il code* (peu importe ce qu'il code).
>
> Index général et légende des icônes : [`outils IA.md`](outils%20IA.md). Autres questions : [Q2 — IA dans un produit](Q2%20-%20IA%20dans%20un%20produit.md) · [Q3 — IA dans les autres métiers](Q3%20-%20IA%20dans%20les%20autres%20métiers.md).

<!-- format d'une ligne : **[Nom](url-officielle)** · [📄](fiches%20outils/nom.md) | Type | icône éco | icône LLM | résumé une ligne -->

<a id="fam-1"></a>
## 1. Agents & IDE de codage
*Font le travail de codage — ou orchestrent les agents qui le font.*

<a id="fam-1a"></a>
### 1a. Agents & IDE qui codent

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[Kilo Code](https://kilo.ai/)** · [📄](fiches%20outils/kilo-code.md) | Extension IDE / CLI | 🔓🎁💳 | 🔑💸 | Agent de codage IA open-source (VS Code, JetBrains, CLI) ; 500+ modèles, tokens au prix coûtant via gateway ou BYOK |
| **[Trae](https://www.trae.ai/)** · [📄](fiches%20outils/trae.md) | Application (IDE) | 🎁🔁 | 📦💸 | IDE IA de ByteDance basé sur VS Code ; modèles premium (Claude, GPT, DeepSeek) fournis via un système de **crédits** (tokens × tarif modèle, plafond par palier), abonnements Lite/Pro/Pro+/Ultra 3–100 $/mois |
| **[Continue](https://www.continue.dev/)** · [📄](fiches%20outils/continue.md) | Extension IDE (VS Code/JetBrains) + CLI | 🔓 | 🔑 | Assistant de codage IA open-source (Apache 2.0), **model-agnostic** (BYOK), + Continue Hub (assistants/règles/modèles partagés). Principale alternative OSS à Copilot/Cursor. ⚠️ **Racheté par Cursor** (avr. 2026) → produit standalone en arrêt, le code OSS subsiste |

<a id="fam-1b"></a>
### 1b. Orchestrateurs & systèmes multi-agents de codage
*Pilotent plusieurs agents de codage — en parallèle (flottes en worktrees git isolés) ou en pipeline discipliné avec revue adverse.*

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[Superset](https://github.com/superset-sh/superset)** · [📄](fiches%20outils/superset.md) | Application desktop (orchestrateur d'agents) | 🔓🔒 | 🟢 | App Electron « IDE pour l'ère des agents » : orchestre en parallèle plusieurs agents de codage CLI (Claude Code, Codex, Cursor…) dans des worktrees git isolés. Source-available (Elastic License 2.0). **BYO agent** : pilote tes agents existants (pas de clé LLM propre). ⚠️ ≠ Apache Superset (BI) |
| **[Conductor](https://www.conductor.build/)** · [📄](fiches%20outils/conductor.md) | Application desktop Mac (orchestrateur d'agents) | 🔒 | 🟢 | App Mac (Melty Labs, YC) qui lance en parallèle plusieurs agents Claude Code/Codex/Cursor dans des worktrees git isolés ; review et merge centralisés. **Gratuite mais propriétaire** (Enterprise à venir), utilise ton abonnement Claude/Codex existant. macOS + GitHub uniquement |
| **[Supacode](https://supacode.sh/)** · [📄](fiches%20outils/supacode.md) | Application desktop Mac (orchestrateur d'agents) | 🔓🔒 | 🟢 | App macOS native (sur libghostty, pas Electron) orchestrant 50+ agents de codage en parallèle dans des worktrees isolés ; « infinite canvas terminal board ». **Source-available (FSL-1.1, devient Apache-2.0 à 2 ans)**, beta gratuite, BYO agent. macOS 26 Tahoe requis |
| **[Orca](https://www.onorca.dev/)** · [📄](fiches%20outils/orca.md) | Application desktop (Mac/Win/Linux) + mobile — ADE | 🔓 | 🟢 | « Agent Development Environment » open-source (stablyai, YC) pour piloter une flotte d'agents de codage en parallèle : board Kanban, worktrees git isolés, terminaux WebGL, navigateur Chromium intégré, worktrees SSH, intégrations GitHub/Linear. Gratuit MIT, BYO agent (25+) |
| **[Liza](https://github.com/liza-mas/liza)** · [📄](fiches%20outils/liza.md) | CLI (Go) — système multi-agents discipliné | 🔓 | 🟢 | Système multi-agents de codage *discipliné* (Apache 2.0, Go) : encadre des agents existants (Claude Code, Codex, Gemini…) avec contrats comportementaux, paires adverses doer/reviewer et superviseurs déterministes ; neutralise 55+ modes d'échec LLM, pipeline autonome spec→code. BYO agent |
| **[Ruflo](https://github.com/ruvnet/ruflo)** · [📄](fiches%20outils/ruflo.md) | Meta-harnais multi-agents (CLI / npm) | 🔓 | 🟢🔑 | Meta-harnais multi-agents open-source (MIT, ex-Claude Flow) qui transforme Claude Code en essaim : 60–100+ agents, ~215 outils MCP, routage ML, mémoire HNSW. 🟢 via Claude Code (mode plugin, sans clé) ou 🔑 BYOK multi-provider (OpenRouter/Ollama…) en mode autonome ; mise sur la *largeur* (vs la *profondeur* de Liza) |
| **[Multica](https://multica.ai/)** · [📄](fiches%20outils/multica.md) | Plateforme « managed agents » (Go) | 🔓🔒 | 🟢 | Plateforme « managed agents » en Go (~37k★) gérant les agents de codage comme des coéquipiers : board de tâches, file, skills réutilisables, dashboard multi-runtime (local + cloud), 12 agents (Claude Code, Codex, Cursor…). Self-host ou Multica Cloud (pas de pricing public). ⚠️ Licence Apache 2.0 **modifiée** (clause anti-service-tiers → pas OSI). Le code ne passe pas par leurs serveurs. BYO agent |
| **[Vibe Kanban](https://www.vibekanban.com/)** · [📄](fiches%20outils/vibe-kanban.md) | Plateforme kanban (orchestration d'agents de codage) | 🔓 | 🟢 | Kanban d'orchestration (Bloop AI, **Apache-2.0**, ~27k★) : board planning→progress→review→done, exécution parallèle en worktrees git, navigateur intégré ; 10+ agents (Claude Code, Codex, Gemini, OpenCode, Cursor, Aider…). Gratuit, BYO agent. ⚠️ Produit commercial en *sunsetting* → désormais open-source communautaire |
| **[Crystal](https://github.com/stravu/crystal)** · [📄](fiches%20outils/crystal.md) | Application desktop (Electron) | 🔓 | 🟢 | App Electron (Stravu, **MIT**) lançant plusieurs sessions **Claude Code / Codex en parallèle** dans des worktrees git isolés ; test/compare/merge. BYO agent. ⚠️ **Déprécié (fév. 2026)** → successeur **Nimbalyst** |
| **[Sculptor](https://imbue.com/sculptor/)** · [📄](fiches%20outils/sculptor.md) | Application desktop Mac (orchestrateur d'agents) | 🔒 | 🟢🔑 | App Mac (Imbue) orchestrant des agents **Claude Code en conteneurs Docker isolés** + Pairing Mode (test local instantané) + dev containers (démarrage en secondes). **Gratuit en beta**, propriétaire. BYO Anthropic (clé API ou abonnement Claude Pro/Max) |

<a id="fam-2"></a>
## 2. Connaissance du code : graphes, recherche & mémoire
*Donnent à l'agent une compréhension structurée du projet (et de l'historique), en réduisant le contexte à charger.*

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[CodeGraph](https://colbymchenry.github.io/codegraph/)** · [📄](fiches%20outils/codegraph.md) | Serveur MCP / CLI | 🔓 | 🟢 | Indexe une codebase en graphe de connaissances local (tree-sitter + SQLite) exposé aux agents via MCP ; déterministe, sans LLM, réduit tool calls et tokens |
| **[Graphify](https://graphify.net/)** · [📄](fiches%20outils/graphify.md) | Skill | 🔓 | 🟢 | Skill open-source (Claude Code) construisant un graphe de connaissances multi-modal (code, docs, PDF, images) via tree-sitter + extraction sémantique LLM ; consomme des tokens à l'indexation |
| **[Polaris](https://polarismcp.com/)** · [📄](fiches%20outils/polaris.md) | Serveur MCP / CLI | 🔓 | 🟢 | Serveur MCP de recherche sémantique locale dans la doc projet (embeddings ONNX, hybride vecteur+BM25) ; sans LLM ni cloud, réduit les tokens 10–40×. Core MIT, Pro payant en préparation |
| **[GraphMind](https://getgraphmind.com/)** · [📄](fiches%20outils/graphmind.md) | App / Serveur MCP / CLI | 🔓🎁 | 🟢🔑 | Transforme la codebase en graphe de connaissances + mémoire persistante cross-session ; 25 outils MCP, jusqu'à 5 700× moins de tokens que grep. Pas de LLM génératif ; embeddings **locaux gratuits** (🟢) ou **distants Voyage/OpenAI** sur tiers payants (🔑). Core MIT gratuit, abonnements 9–19 €/mois. Made in Paris |
| **[Cavemem](https://github.com/JuliusBrussee/cavemem)** · [📄](fiches%20outils/cavemem.md) | Serveur MCP / CLI | 🔓 | 🟢🔑 | Mémoire persistante cross-agent (CLI + MCP + hooks IDE) ; événements de session compressés (~75 %), SQLite local, interrogeable via MCP. Aucun LLM génératif ; embeddings **locaux par défaut** (🟢), provider distant **OpenAI** optionnel = clé requise (🔑) |
| **[Serena](https://github.com/oraios/serena)** · [📄](fiches%20outils/serena.md) | Serveur MCP / toolkit | 🔓 | 🟢 | Toolkit MCP (Python, Oraios) donnant aux agents des capacités IDE via LSP : recherche **et édition/refactoring** sémantiques au niveau symbole sur 40+ langages (pas du grep). MIT open-source (plugin JetBrains payant en option), BYO client |
| **[Agent Booster](https://github.com/sseshachala/agent-booster)** · [📄](fiches%20outils/agent-booster.md) | Serveur MCP / CLI | 🔓 | 🟢 | Index de **symboles** (tree-sitter + embeddings **locaux** `all-MiniLM-L6-v2`) qui détourne les *Read* de l'agent : renvoie les symboles pertinents au lieu du fichier entier → 60–90 % de tokens en moins. Hooks pour Claude Code/Cursor/Windsurf/Codex ; MIT, sans LLM ni clé. ⚠️ Homonyme du `agent-booster` de ruvnet (autre produit) |

<a id="fam-3"></a>
## 3. Optimisation des tokens & du comportement de l'agent
*Réduisent ce que l'agent consomme (entrée) ou produit (sortie / périmètre du code).*

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[RTK (Rust Token Killer)](https://www.rtk-ai.app/)** · [📄](fiches%20outils/rtk.md) | CLI (proxy) | 🔓 | 🟢 | Proxy CLI open-source (binaire Rust unique) qui compresse la sortie des commandes terminal avant le contexte LLM (60–90 % de tokens en moins) ; hook PreToolUse dans Claude Code, sans clé ni télémétrie. RTK Cloud (équipes) à venir, 15 $/dev/mois |
| **[Headroom](https://github.com/headroomlabs-ai/headroom)** · [📄](fiches%20outils/headroom.md) | CLI / Proxy / Serveur MCP / Bibliothèque | 🔓 | 🟢 | Couche de compression de contexte open-source (Apache 2.0) : réduit 60–95 % des tokens (JSON, code AST, logs, RAG, historique) **avant** l'appel, par compression **déterministe sans LLM**. Multi-format (lib Py/TS, proxy, wrapper d'agents, MCP, middleware) ; local, se place devant la clé/abonnement existant (pas de clé propre) |
| **[Tokenade](https://tokenade.net/)** · [📄](fiches%20outils/tokenade.md) | CLI | 🎁🔁 | 🟢 | CLI propriétaire qui réduit jusqu'à 88 % des tokens envoyés aux LLM par les agents (recherche sémantique, trim des sorties, chargement sélectif d'outils MCP) ; gratuit jusqu'à 20 M tokens, Pro 9,90 $/mois |
| **[Caveman](https://github.com/juliusbrussee/caveman)** · [📄](fiches%20outils/caveman.md) | Skill | 🔓 | 🟢 | Skill open-source (Claude Code + ~30 agents) qui coupe ~65 % des tokens de sortie en faisant « parler comme un homme des cavernes » ; code/chemins préservés, niveaux lite/full/ultra/wenyan |
| **[Ponytail](https://github.com/DietrichGebert/ponytail)** · [📄](fiches%20outils/ponytail.md) | Skill / Plugin | 🔓 | 🟢 | Skill open-source (Claude Code, Codex, Gemini, Cursor…) qui pousse l'agent à coder « comme le dev senior le plus paresseux » : anti-over-engineering (YAGNI, stdlib d'abord). 80–94 % de code en moins annoncé, niveaux lite/full/ultra |
| **[dupehound](https://github.com/Rafaelpta/dupehound)** · [📄](fiches%20outils/dupehound.md) | CLI / Serveur MCP | 🔓 | 🟢 | Détecteur de **code dupliqué** (Rust, MIT) pour bases écrites par l'IA : empreinte structurelle (tree-sitter + winnowing) → repère les fonctions dupliquées même renommées, même sans LLM ni clé. `scan`/`history`/`check` (gate CI + « slop score ») + mode **MCP** pour que l'agent réutilise au lieu de réécrire. ⚠️ Jeune (v0.1.2, juin 2026) |

<a id="fam-4"></a>
## 4. Workflow, méthodologie & développement spec-driven
*Structurent le processus de dev assisté par IA (méthodologies, rôles, specs, workflows guidés) par-dessus un agent existant.*

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[Cavekit](https://github.com/JuliusBrussee/cavekit)** · [📄](fiches%20outils/cavekit.md) | Plugin | 🔓 | 🟢 | Plugin Claude Code de développement spec-driven : specs durables survivant aux resets de contexte, backprop des échecs de test ; encodage « caveman » pour réduire les tokens |
| **[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)** · [📄](fiches%20outils/bmad-method.md) | Framework / méthodologie (agents IA pour IDE) | 🔓 | 🟢 | Méthodologie open-source (MIT, ~49k★) de dev agile piloté par IA : 21 agents-personas et 50+ workflows guidés, du brainstorming au déploiement, dans ton IDE (Claude Code, Cursor). BYOK |
| **[GSD (Get Shit Done)](https://github.com/open-gsd/gsd-core)** · [📄](fiches%20outils/gsd.md) | Framework méta-prompting / spec-driven (surcouche d'agent) | 🔓 | 🟢 | Framework open-source (MIT) de spec-driven dev par tâches : combat la dégradation de contexte en spawnant des sous-agents à contexte frais ; BYOK. **⚠️ Créateur d'origine (TÂCHES) lié à un rug-pull crypto $GSD + packages npm d'origine abandonnés → n'utiliser que la continuation communautaire `open-gsd` (voir fiche)** |
| **[gstack](https://github.com/garrytan/gstack)** · [📄](fiches%20outils/gstack.md) | Suite de skills / workflow (Claude Code) | 🔓 | 🟢 | Config Claude Code open-source de Garry Tan (YC) : 23+ skills « opinionated » faisant jouer à l'agent les rôles d'une équipe (CEO, Designer, QA…) pour démultiplier le dev solo |
| **[Superpowers](https://github.com/obra/superpowers)** · [📄](fiches%20outils/superpowers.md) | Plugin / framework de skills (multi-agents) | 🔓 | 🟢 | Framework de skills agentiques + méthodologie de dev par Jesse Vincent (obra), ~93k★, n°1 des plugins Claude Code : impose brainstorming, worktrees, TDD, revue par sous-agents. Multi-plateforme, MIT, tourne dans ton agent |
| **[GitHub Spec Kit](https://github.com/github/spec-kit)** · [📄](fiches%20outils/spec-kit.md) | Toolkit CLI (spec-driven) | 🔓 | 🟢 | Toolkit **officiel GitHub** (MIT) de spec-driven dev : CLI `Specify` + commandes `/speckit.*` (constitution→spec→plan→tasks→implement) par-dessus ton agent (Claude Code, Copilot, Cursor, Gemini, Codex, 24+). Pas de LLM propre |
| **[Task Master](https://github.com/eyaltoledano/claude-task-master)** · [📄](fiches%20outils/task-master.md) | CLI + Serveur MCP | 🔓🎁 | 🟢🔑 | Transforme un PRD en **tâches structurées** (dépendances, priorités) ; CLI + MCP intégré à Claude Code, Cursor, Windsurf (~25k★). Cœur MIT gratuit (BYOK 15+ providers) ; offre équipe payante **Hamster Studio** (+ mode hébergé sans clé) |
| **[Pheromind](https://github.com/ChrisRoyse/Pheromind)** · [📄](fiches%20outils/pheromind.md) | Framework d'orchestration multi-agents (swarm) | 🔓 | 🟢 | Orchestration multi-agents par **« intelligence en essaim à base de phéromones »** (coordination indirecte via un médium partagé) au-dessus d'un agent existant. ⚠️ **Statut flou** : repo public mais IP/offre commerciale revendiquée, licence non confirmée — arbitrer prudemment |

<a id="fam-5"></a>
## 5. Automatisation de navigateur (serveurs MCP)
*Pilotent un navigateur depuis l'agent — surtout pour **tester** les applis web qu'on développe (et scraping/contrôle). Coût LLM côté client → 🟢.*

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[Firefox DevTools MCP](https://github.com/freema/firefox-devtools-mcp)** · [📄](fiches%20outils/firefox-devtools-mcp.md) | Serveur MCP (automatisation navigateur) | 🔓 | 🟢 | Serveur MCP open-source (TypeScript) pour piloter/inspecter Firefox via WebDriver BiDi : navigation, DOM, réseau, console, screenshots, eval JS, préférences/extensions. Tests, scraping, contrôle navigateur. Local uniquement (Firefox + Node). Double licence MIT/Apache 2.0 |
| **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** · [📄](fiches%20outils/playwright-mcp.md) | Serveur MCP (automatisation navigateur) | 🔓 | 🟢 | Serveur MCP officiel Microsoft (Apache 2.0) pilotant Chromium/Firefox/WebKit via l'**arbre d'accessibilité** (pas des screenshots) → rapide et économe en tokens. Tests, scraping, contrôle navigateur |
| **[Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)** · [📄](fiches%20outils/chrome-devtools-mcp.md) | Serveur MCP (automatisation navigateur) | 🔓 | 🟢 | Serveur MCP officiel de l'équipe Chrome (Google, Apache 2.0) pilotant Chrome via CDP + Puppeteer ; se démarque par les **traces de performance** et le débogage réseau/DOM/console |
| **[Puppeteer MCP](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer)** · [📄](fiches%20outils/puppeteer-mcp.md) | Serveur MCP (automatisation navigateur) | 🔓 | 🟢 | ⚠️ **Déprécié/archivé (mai 2025)** : serveur MCP de référence pilotant Chromium via Puppeteer (7 outils), vulnérabilités connues. Successeurs recommandés : Chrome DevTools MCP / Playwright MCP |

<a id="fam-6"></a>
## 6. Assistants IA pour terminal / shell
*Compagnons IA conversationnels intégrés au terminal : exécution de commandes (avec garde-fou), analyse système, aide CLI.*

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[Neo-AI](https://github.com/Vasco0x4/Neo-AI)** · [📄](fiches%20outils/neo-ai.md) | CLI (assistant terminal Linux) | 🔓 | 🟢🔑 | Assistant IA pour terminal Linux open-source (BSD-3, Python, par Vasco0x4) : exécute des commandes avec contexte + approbation, analyse système (logs, fichiers, santé), volet cybersécurité (scan réseau, CTF). LLM local (LM Studio) ou cloud (OpenAI/Claude). ⚠️ Beta, Linux |

<a id="fam-7"></a>
## 7. Revue de code par IA
*Reviewers IA qui relisent les PR (résumé, bugs, sécurité) — le levier clé quand les agents produisent plus de code qu'on n'en relit. Le LLM est **fourni dans le prix** (📦), pas en BYOK. Cadre conceptuel : [📄 revue de code agentique](fiches/revue-de-code-agentique.md).*

> **À retenir** : faible recouvrement entre outils (~93 % des findings ne sont vus que par un seul des 4) → en combiner plusieurs aux forces complémentaires (précision vs recall) ; traiter leurs verdicts comme des **signaux**, l'humain garde le merge.

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[CodeRabbit](https://www.coderabbit.ai/)** · [📄](fiches%20outils/coderabbit.md) | Service web (app GitHub/GitLab) + IDE/CLI | 🎁🔁💳 | 📦 | Reviewer IA de PR (GitHub/GitLab) : résumés, revue ligne à ligne, linters + SAST, fix en 1 clic. **Gratuit à vie pour repos publics** ; Pro 24 $, Pro Plus 48 $/user/mois, Enterprise (SSO, self-host). Meilleur **recall** au benchmark Martian (~49 % précision). LLM inclus |
| **[Greptile](https://www.greptile.com/)** · [📄](fiches%20outils/greptile.md) | Service web (app GitHub) | 🎁🔁💳 | 📦 | Reviewer IA de PR avec **compréhension de toute la codebase** (fort sur l'architecture/contexte) ; ~82 % de bugs attrapés (recall > précision). Pro 30 $/seat/mois (50 revues incluses, +1 $/revue), Enterprise (self-host). Gratuit pour l'OSS qualifié, -50 % startups |
| **[Sentry Seer](https://docs.sentry.io/product/ai-in-sentry/seer/)** · [📄](fiches%20outils/sentry-seer.md) | Service web (add-on Sentry) | 🔒🔁💳 | 📦 | Agent IA de debugging de Sentry (Autofix, agent conversationnel, **Code Review**) : prédit les défaillances avant merge, fort sur la **sévérité prod** (adossé à ta télémétrie Sentry). Add-on facturé par contributeur actif (2+ PR/mois). LLM inclus |
| **[Cursor BugBot](https://cursor.com/bugbot)** · [📄](fiches%20outils/cursor-bugbot.md) | Service web (app GitHub) | 🔒🔁💳 | 📦 | Reviewer IA de PR d'Anysphere (Cursor) ciblant les **bugs de logique** avec peu de faux positifs (orienté **précision**) ; modèles frontier + maison. Historiquement 40 $/user/mois → **bascule à l'usage** (~1–1,50 $/run, post-8 juin 2026). Compte Cursor requis |

<a id="fam-8"></a>
## 8. Documentation & sources de connaissances externes (serveurs MCP)
*Servent à l'agent des **connaissances externes à jour** — doc de librairies, repos GitHub, doc éditeur (Microsoft/AWS), web — pour produire du code juste sans halluciner les signatures. Tournent dans l'agent (coût LLM côté client → 🟢) et visent à *réduire* les tokens. ⚠️ Exception : **Exa** s'appuie sur une API de recherche **payante à l'usage** (coût distinct du LLM).*

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[Ref](https://ref.tools/)** · [📄](fiches%20outils/ref.md) | Serveur MCP (doc technique à jour) | 🎁🔁 | 🟢 | Sert aux agents la **doc technique à jour** (libs/APIs publiques + repos/PDF privés), pré-chunkée → *juste les tokens utiles* (réduit le « context rot »). Client MCP open-source ; service hébergé freemium (Free 200 crédits → Basic 19 $, Pro 50 $, Max 200 $/mois). Voisin de Context7 |
| **[Context7](https://context7.com/)** · [📄](fiches%20outils/context7.md) | Serveur MCP (doc de libs) | 🔓🎁 | 🟢 | Serveur MCP **open-source (MIT, Upstash)** injectant la **doc à jour et versionnée** des librairies + exemples de code (`resolve-library-id`, `query-docs`). Hébergé (`mcp.context7.com`) ou local ; gratuit, clé API gratuite pour + de quota. 30+ agents. **Déjà connecté dans cette session** |
| **[GitMCP](https://gitmcp.io/)** · [📄](fiches%20outils/gitmcp.md) | Serveur MCP distant (repo GitHub) | 🔓 | 🟢 | Transforme **n'importe quel repo GitHub** en serveur MCP distant : remplacer `github.com` par `gitmcp.io` → l'agent lit `llms.txt`/`readme` pour le contexte. Gratuit (idosal/git-mcp). ⚠️ Licence non confirmée à la source |
| **[Exa MCP](https://github.com/exa-labs/exa-mcp-server)** · [📄](fiches%20outils/exa-mcp.md) | Serveur MCP (recherche web) | 🔓💳 | 🟢 | Donne à l'agent la **recherche web/code/entreprise** via l'API neuronale **Exa** (`web_search_exa`, `web_fetch_exa`). Serveur MCP **MIT** gratuit, mais **clé Exa requise** (API payante à l'usage, tier gratuit). Plus large que la doc de libs. 🟢 côté LLM, mais coût de recherche Exa à l'usage |
| **[Microsoft Learn MCP](https://learn.microsoft.com/training/support/mcp)** · [📄](fiches%20outils/microsoft-learn-mcp.md) | Serveur MCP distant (doc Microsoft) | 🔒 | 🟢 | Serveur MCP **officiel Microsoft** (HTTP streamable) servant la doc Microsoft/Azure officielle (service « Ask Learn », refresh quotidien) : recherche doc, article complet, exemples. **Gratuit, sans authentification** ; propriétaire (service hébergé) |
| **[AWS Documentation MCP](https://github.com/awslabs/mcp)** · [📄](fiches%20outils/aws-documentation-mcp.md) | Serveur MCP local (doc AWS) | 🔓 | 🟢 | Serveur MCP **officiel AWS Labs (Apache 2.0)** : recherche/lecture de la **doc AWS** officielle, API refs, What's New (stdio local). Gratuit, open-source ; un des serveurs du repo `awslabs/mcp`. Install 1-clic (Cursor, VS Code, Kiro) |

<a id="fam-9"></a>
## 9. CI/CD, livraison & opérations assistés par IA
*Le **bout droit** du SDLC : **livrer** le code (CI/merge/tests flaky) et **exploiter** la prod (**AI SRE** : investigation d'incidents, RCA, self-healing). ⚠️ Le volet ops déborde vers « exploiter un produit » (frontière Q2). LLM exécuté par l'éditeur (SaaS) → **📦 inclus** ; les AI SRE sont surtout **enterprise / sur devis**.*

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[Mergify](https://mergify.com/)** · [📄](fiches%20outils/mergify.md) | Plateforme SaaS (merge queue & CI) | 🎁🔁 | 📦 | Merge queue (« keep main green ») + CI Insights (auto-retry) + Test Insights (détecte/quarantaine/corrige les tests **flaky**) + Stacks. Cœur surtout déterministe (IA légère sur le flaky). Freemium (gratuit OSS, payant par contributeur — prix exacts à vérifier) |
| **[Cleric](https://cleric.ai/)** · [📄](fiches%20outils/cleric.md) | Plateforme SaaS (AI SRE) | 🔒 | 📦 | Agent **AI SRE** : enquête d'incidents, RCA, recommandations ; branché sur ta stack (Datadog/Grafana/PagerDuty…). **Read-only par défaut**, write quand prêt. Gartner Cool Vendor 2025. Enterprise / sur devis |
| **[Resolve.ai](https://resolve.ai/)** · [📄](fiches%20outils/resolve-ai.md) | Plateforme SaaS (AI SRE / on-call) | 🔒 | 📦 | Agents IA d'astreinte/incident/prod (objectif ~80 % d'auto-résolution, garde-fous) ; sécurité entreprise (SSO/RBAC, pas d'entraînement sur tes données). Clients Coinbase/DoorDash… Enterprise / sur devis |
| **[Traversal](https://traversal.com/)** · [📄](fiches%20outils/traversal.md) | Plateforme SaaS (AI SRE, RCA à l'échelle) | 🔒 | 📦 | « AI SRE pour systèmes complexes » : World Model + Causal Search pour la RCA à grande échelle, triage, self-healing ; option **BYOC** (ton cloud). Git/monitoring/incident. Enterprise / sur devis |

> **Candidats non vérifiés** (à arbitrer, cf. `outils candidats.md`) : **Datadog Bits AI Dev Agent** (fix autonome de flaky → draft PR), **Aviator**, **Trunk** (CI/flaky) ; **Rootly**, **PagerDuty AIOps** (incident/AIOps).
