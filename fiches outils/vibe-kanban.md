---
outil: "Vibe Kanban"
titre: "Vibe Kanban"
themes: [multi-agents, frameworks-outillage]
type: "Plateforme kanban / orchestration d'agents de codage (web)"
url: https://www.vibekanban.com/
modele_economique: "Open-source (Apache-2.0, vérifié), gratuit — produit commercial en sunsetting, devient communautaire. Éditeur : Bloop AI Limited"
cout_llm: "Aucun coût LLM propre (🟢) — BYO agent ; tu paies seulement les services d'IA sous-jacents (Claude Code, Codex…)"
---

# Vibe Kanban

**En une phrase** — tableau Kanban qui orchestre des agents de codage IA : tu planifies des tâches, tu les confies à des agents qui travaillent en parallèle (chacun dans son worktree git), puis tu relis et merges — l'humain passe au rôle de planification/revue.

## Type & intégration
**Plateforme web d'orchestration** par **Bloop AI Limited** (dépôt `BloopAI/vibe-kanban`, ~27k★). Workflow en colonnes : **planning → in progress → in review → done**. Fonctionnalités : **exécution parallèle isolée** (chaque tâche dans son **worktree git**, pas d'interférence avec la branche principale), revue de code avec commentaires, test des changements via un **navigateur intégré**. Orchestre de nombreux exécuteurs : **Claude Code, Codex/ChatGPT, Gemini, OpenCode, Cursor, Amp, Aider, Copilot, Windsurf**… Traction : ~30 000 utilisateurs actifs, ~100 000 PR créées.

## Modèle économique
**Open-source, licence Apache-2.0** (vérifié via l'API GitHub — vraie licence OSI, contrairement à [Multica](multica.md) en Apache *modifiée*). **Gratuit**. ⚠️ **Statut** : Bloop AI **arrête (sunsetting) le produit commercial** ; le projet **continue en open-source, maintenu par la communauté**. À surveiller pour la pérennité (rythme de maintenance post-sunset).

## Coût LLM
**Aucun coût LLM propre** 🟢 — Vibe Kanban est un orchestrateur : tu **branches ton propre agent** (Claude Code, Codex…) et **tu paies uniquement les services d'IA sous-jacents** que tu utilises. Vibe Kanban lui-même est gratuit et n'ajoute pas de coût modèle. Comme les autres orchestrateurs 1b, le coût LLM = celui de tes agents/abonnements.

## À quoi ça sert
Réorganiser le cycle de dev autour d'agents parallèles : planifier les tâches, lancer plusieurs agents simultanément en isolation, suivre/relire/merger depuis un board unique. Pour les développeurs qui veulent superviser une « équipe » d'agents plutôt que piloter un seul agent à la fois.

## Notes / à creuser
- **Famille 1b (orchestrateurs & systèmes multi-agents de codage)** : très proche de [Multica](multica.md) (board + agents-coéquipiers), [Orca](orca.md), [Conductor](conductor.md), [Superset (superset-sh)](superset.md) — exécution parallèle en worktrees git. Vibe Kanban se distingue par sa **vraie licence Apache-2.0** (vs open-core/source-available de Multica/Superset/Supacode) et son **navigateur intégré** pour tester.
- ⚠️ **Sunsetting commercial** : l'avenir repose sur la communauté → vérifier l'activité du dépôt avant de s'y engager en production.
- Le sous-cluster « orchestrateurs d'agents de codage » est très fourni (Superset, Conductor, Supacode, Orca, Multica, Vibe Kanban) — marché en forte effervescence et consolidation.

## Source
- Site : https://www.vibekanban.com/ · dépôt : https://github.com/BloopAI/vibe-kanban (Apache-2.0, ~27k★, vérifié API GitHub)

*(vérifié le 2026-06-15 — site officiel + API GitHub [licence Apache-2.0] + recherche web)*
