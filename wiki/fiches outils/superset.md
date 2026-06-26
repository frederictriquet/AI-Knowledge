---
outil: "Superset (superset-sh)"
titre: "Superset (superset-sh)"
themes: [multi-agents, frameworks-outillage]
type: "Application desktop (orchestrateur d'agents de codage)"
url: https://github.com/superset-sh/superset
modele_economique: "Source-available (Elastic License 2.0) — app téléchargeable, modèle commercial non précisé"
cout_llm: "Aucun coût LLM propre (🟢) — orchestre tes agents existants (Claude Code, Codex…) qui portent leur propre auth (abonnement/login) ; aucune clé LLM à fournir à Superset"
objectifs: [generer-code]
famille: "Orchestrateurs & systèmes multi-agents de codage"
eco_icones: "🔓🔒"
cout_icones: "🟢"
resume: "App Electron « IDE pour l'ère des agents » : orchestre en parallèle plusieurs agents de codage CLI (Claude Code, Codex, Cursor…) dans des worktrees git isolés. Source-available (Elastic License 2.0). **BYO agent** : pilote tes agents existants (pas de clé LLM propre). ⚠️ ≠ Apache Superset (BI)"
---

# Superset (superset-sh)

**En une phrase** — application desktop « IDE/terminal pour l'ère des agents » qui permet de lancer et piloter en parallèle une armée d'agents de codage CLI (Claude Code, Codex, Cursor…), chacun isolé dans son propre worktree git.

> ⚠️ Homonymie : **rien à voir avec Apache Superset** (l'outil de BI/dataviz). Cette fiche concerne **superset-sh/superset**, un orchestrateur d'agents de codage.

## Type & intégration
**Application desktop Electron** (TypeScript 95 %, React, TailwindCSS, runtime Bun, Turborepo). Fonctionne comme **orchestrateur / gestionnaire d'agents**, pas comme un agent ni un serveur MCP. **Agent-agnostique** : compatible avec n'importe quel agent de codage qui tourne dans un terminal (Claude Code, OpenCode, Cursor, Codex…).

Fonctions clés :
- **Exécution parallèle** : 10+ agents simultanément sur la machine.
- **Isolation par worktree git** : chaque tâche a sa branche et son répertoire de travail.
- **Monitoring d'agents**, **diff viewer** intégré, **presets de workspace**, ouverture dans l'éditeur.

## Modèle économique
**Source-available** sous **Elastic License 2.0 (ELv2)** : code public et utilisable, mais avec **restrictions sur l'usage commercial** sans licence explicite → *pas open-source au sens OSI*. App téléchargeable ; modèle de monétisation non détaillé (probable offre commerciale/cloud à terme). Équipe basée à San Francisco.

## Coût LLM
**Aucun coût LLM propre** 🟢 — Superset **n'utilise pas de LLM** lui-même : il **pilote tes agents existants** (Claude Code, Codex, Cursor…), qui portent **leur propre authentification** (abonnement Claude/login ou clé). Le README confirme : « **No … third-party credentials needed** » au setup, et « **You choose which agents, providers, and integrations to connect** ». Donc **pas de clé LLM à fournir à Superset** — même logique que [Orca](orca.md), [Conductor](conductor.md), [Supacode](supacode.md) ; le coût LLM est celui des agents sous-jacents. *(coût LLM 🟢 vérifié sur le README, 2026-06-16.)*

⚠️ Attention au coût en mode parallèle : lancer 10+ agents en simultané **multiplie** la consommation de tokens des agents sous-jacents.

## À quoi ça sert
Coordonner le travail de plusieurs agents autonomes : paralléliser des tâches, éviter le coût de context-switching, revoir/merger les résultats. Pertinent à mesure que les outils passent du chat à des **workers CLI** autonomes qu'on fait tourner en flotte.

## Notes / à creuser
- Famille « agents & IDE de codage », mais au niveau **méta** : il ne code pas, il fait tourner ceux qui codent (ex. [Kilo Code](kilo-code.md) et autres agents CLI).
- À distinguer de [MindFlight Orchestrator (MFO)](mindflight-orchestrator.md) : MFO orchestre des agents pour des **processus métier d'entreprise** ; Superset orchestre des **agents de codage** pour des développeurs.
- À creuser : tarif d'une éventuelle offre Pro/cloud, gestion des coûts en exécution massivement parallèle.

## Source
- Dépôt : https://github.com/superset-sh/superset · Site : https://superset.sh/ · Docs : https://superset-sh-superset.mintlify.app/

*(vérifié le 2026-06-15 — README GitHub + recherche web)*
