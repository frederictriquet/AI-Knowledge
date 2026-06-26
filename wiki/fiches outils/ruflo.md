---
outil: "Ruflo"
titre: "Ruflo"
themes: [multi-agents]
type: "Meta-harnais / framework d'orchestration multi-agents pour Claude (open source, npm)"
url: https://github.com/ruvnet/ruflo
modele_economique: "Open source MIT, gratuit — pas d'abonnement ; tu apportes tes propres clés LLM (BYOK)"
cout_llm: "🟢🔑 — mode plugin Claude Code : via ton Claude Code (sans clé, 🟢) ; mode autonome multi-provider : BYOK (Claude/GPT/Gemini/Ollama via OpenRouter ou endpoint OpenAI-compatible, 🔑)"
objectifs: [generer-code]
famille: "Orchestrateurs & systèmes multi-agents de codage"
eco_icones: "🔓"
cout_icones: "🟢🔑"
resume: "Meta-harnais multi-agents open-source (MIT, ex-Claude Flow) qui transforme Claude Code en essaim : 60–100+ agents, ~215 outils MCP, routage ML, mémoire HNSW. 🟢 via Claude Code (mode plugin, sans clé) ou 🔑 BYOK multi-provider (OpenRouter/Ollama…) en mode autonome ; mise sur la *largeur* (vs la *profondeur* de Liza)"
---

# Ruflo

**En une phrase** — Ruflo (anciennement *Claude Flow*, par ruvnet) est un meta-harnais open source qui transforme Claude Code en essaim multi-agents : 60-100+ types d'agents spécialisés, ~210-215 outils MCP et un routage des tâches piloté par apprentissage automatique.

## Type & intégration
Framework / meta-harnais d'orchestration multi-agents pour Claude, distribué en paquet npm (`ruflo`). Trois modes d'intégration :
- **CLI** : `npx ruflo@latest init wizard`
- **Plugin Claude Code** : via la marketplace (`/plugin install ruflo-core@ruflo`)
- **Serveur MCP** : `npx ruflo@latest mcp start`

Il s'appuie sur les hooks de Claude Code pour des vérifications pré/post-exécution et orchestre des « swarms » d'agents (coder, tester, architect, security-architect, DevOps, data analyst, etc.). Mémoire persistante indexée (HNSW), « ReasoningBank » qui recherche des patterns passés par similarité (trigrammes/Jaccard), et routage des tâches vers les agents au meilleur historique (Q-learning / routage « SONA » neural annoncé à ~89 % de précision).

## Modèle économique
Logiciel libre sous **licence MIT**, gratuit, sur GitHub (`ruvnet/ruflo`, ~59,6k étoiles au moment de la vérification). Aucun abonnement ni API propriétaire. Le revenu/modèle commercial direct n'existe pas : c'est un projet open source communautaire.

## Coût LLM
**🟢🔑 — deux modes** (Ruflo ne revend pas de LLM ; vérifié sur le README le 2026-06-16) :
- **Mode plugin Claude Code** (`/plugin install`, « after init, just use Claude Code normally ») → tourne **via ton Claude Code**, **sans clé** (🟢, ton abonnement/login existant).
- **Mode autonome / multi-provider** → **BYOK** (🔑) : tu branches tes propres clés (Anthropic, OpenAI, Gemini, Cohere, Ollama local) ou un endpoint OpenAI-compatible via OpenRouter.

L'argument « ~75 % d'économies » repose sur le **routage multi-fournisseurs** + sélection de modèle adaptative (modèles moins chers pour les tâches simples), pas sur une tarification incluse. (Démo hébergée flo.ruv.io : sans clé ni compte.)

## À quoi ça sert
Construire et piloter des systèmes multi-agents autonomes par-dessus Claude Code (ou Codex) : développement logiciel coordonné (codage, tests, sécurité, architecture), workflows autonomes, intégration RAG, mémoire adaptative et auto-apprentissage de l'essaim. Cible : maximiser la **largeur** — beaucoup d'agents spécialisés et d'outils, avec un routage ML qui dispatche chaque tâche vers l'agent le plus performant.

## Notes / à creuser
- Pari architectural opposé à [Liza](liza.md) : Ruflo optimise la **largeur** (60+ types d'agents, ~215 outils MCP, routage ML, topologies de swarm, consensus byzantin, indexation HNSW) ; Liza optimise la **profondeur** (simplicité comportementale, ces concepts d'infra ayant été délibérément écartés par Liza).
- Chiffres à préciser : la doc oscille entre « 60+ » et « 100+ » agents, et « 210+ » vs « 215+ » outils MCP — ordres de grandeur cohérents, comptes exacts variables selon la version.
- Ancien nom : **Claude Flow**. Renommé Ruflo. À surveiller pour la continuité des références.
- Claims marketing (75 % d'économies, 89 % de précision de routage) à prendre avec prudence : non vérifiés indépendamment, dépendent du contexte d'usage.

## Source
- https://github.com/ruvnet/ruflo (dépôt officiel, MIT, tagline « leading agent meta-harness for Claude ») *(vérifié le 2026-06-15)*
- https://github.com/ruvnet/ruflo/wiki — Wiki (agents, configuration) *(vérifié le 2026-06-15)*
- https://deepwiki.com/ruvnet/ruflo/6.1-agent-types-and-configuration *(vérifié le 2026-06-15)*
- Comparatif concurrentiel « Liza » : https://raw.githubusercontent.com/liza-mas/liza/main/specs/architecture/competition-survey/mas-survey.md *(vérifié le 2026-06-15)*
