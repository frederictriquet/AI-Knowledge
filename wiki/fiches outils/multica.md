---
outil: "Multica"
titre: "Multica"
themes: [multi-agents, frameworks-outillage]
type: "Plateforme « managed agents » (orchestration d'agents de codage)"
url: https://multica.ai/
modele_economique: "Source-available (Apache 2.0 MODIFIÉE — clause anti-service-tiers, licence commerciale requise pour héberger/embarquer) + Multica Cloud (pas de pricing public)"
cout_llm: "Aucun coût LLM propre (🟢) — pilote tes agents CLI existants (qui portent leur auth) ; vendor-neutral, le code ne passe pas par les serveurs Multica"
---

# Multica

**En une phrase** — plateforme qui gère les agents de codage **comme de vrais coéquipiers** : on leur assigne des tâches sur un board, ils exécutent, rapportent l'avancement, commentent, et capitalisent des « skills » réutilisables.

## Type & intégration
**Plateforme open-core en Go** (`multica-ai/multica`, ~37k★). Couche d'orchestration / project-management pour agents : board de tâches (enqueue → claim → execute → complete/fail), suivi temps réel (WebSocket), bibliothèque de **skills** réutilisables, **dashboard multi-runtime** (daemons locaux + runtimes cloud, auto-détection des CLIs disponibles), timeline unifiée humains + agents. Vendor-neutral : compatible **12 agents** — Claude Code, Codex, GitHub Copilot CLI, OpenClaw, OpenCode, Hermes, Gemini, Pi, Cursor Agent, Kimi, Kiro CLI (+ Antigravity). Setup : `multica setup` (connecte à Multica Cloud) ou `multica setup self-host` (serveur complet via Docker/GHCR).

## Modèle économique
⚠️ **Pas open-source au sens OSI**, malgré le « fully open source » du site. Le fichier LICENSE est une **Apache License 2.0 *modifiée*** avec conditions additionnelles (vérifié) :
- **Clause anti-service-tiers** : interdiction d'utiliser le code pour fournir un **service hébergé** à des tiers ou d'**embarquer** Multica comme composant, sans **licence commerciale** de l'éditeur.
- (GitHub classe la licence en « Other / NOASSERTION ».)

→ Modèle **open-core / source-available** : self-host autorisé, mais la revente en service est réservée. **Multica Cloud** (version hébergée) existe — **aucune page tarifs publique** (/pricing en 404) ; un « Start free trial » est mis en avant.

## Coût LLM
**Aucun coût LLM propre** 🟢 — Multica **n'embarque pas de LLM** et n'ajoute pas de clé : elle **route les tâches vers tes agents CLI existants** (Claude Code, Codex, Cursor…), qui portent **leur propre authentification/abonnement**. « Le code ne passe pas par les serveurs Multica ». Le coût LLM est donc celui de tes agents sous-jacents (comme pour les autres orchestrateurs 1b). Aucun BYOK propre à Multica côté modèle.

## À quoi ça sert
Industrialiser le travail de plusieurs agents de codage en équipe : assigner des issues comme à des collègues, suivre l'avancement, faire collaborer humains + agents au même endroit, et réutiliser des compétences acquises. Cible les équipes de dev qui veulent traiter les agents comme des membres d'équipe gérés, pas comme des outils ponctuels.

## Notes / à creuser
- **Famille 1b (orchestrateurs & systèmes multi-agents de codage)** : proche de [Orca](orca.md), [Conductor](conductor.md), [Superset (superset-sh)](superset.md) (piloter plusieurs agents), mais avec un angle **« project management / teammates »** (board, assignation, skills) plutôt que worktrees parallèles purs. Distinct de [MindFlight Orchestrator (MFO)](mindflight-orchestrator.md) (processus métier, pas codage).
- Licence open-core comparable à celle de **Superset** (ELv2) / **Supacode** (FSL) : « ouvert mais pas revendable en service ».
- À creuser : tarif réel de Multica Cloud (non public), périmètre du free trial, ce que couvre la licence commerciale.

## Source
- Site : https://multica.ai/ · docs : https://multica.ai/docs · dépôt : https://github.com/multica-ai/multica (Go, ~37k★)
- LICENSE vérifiée : « modified version of the Apache License 2.0 » + clause anti-service-tiers (raw GitHub)

*(vérifié le 2026-06-15 — site officiel + API GitHub + fichier LICENSE + README)*

<!-- voisin direct : [Vibe Kanban](vibe-kanban.md) (kanban d'orchestration d'agents, Apache-2.0) -->

