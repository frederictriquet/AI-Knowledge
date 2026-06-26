---
outil: "Supacode"
titre: "Supacode"
themes: [multi-agents, frameworks-outillage]
type: "Application desktop macOS native (orchestrateur d'agents de codage)"
url: https://supacode.sh/
modele_economique: "Source-available (FSL-1.1-ALv2 : clause anti-concurrence, bascule en Apache-2.0 après 2 ans) — beta gratuite (DMG / Homebrew). Éditeur : Supabit, LLC"
cout_llm: "Intégré — BYO agent ; utilise tes abonnements CLI existants (Claude Code, Codex…), pas de coût LLM propre"
objectifs: [generer-code]
famille: "Orchestrateurs & systèmes multi-agents de codage"
eco_icones: "🔓🔒"
cout_icones: "🟢"
resume: "App macOS native (sur libghostty, pas Electron) orchestrant 50+ agents de codage en parallèle dans des worktrees isolés ; « infinite canvas terminal board ». **Source-available (FSL-1.1, devient Apache-2.0 à 2 ans)**, beta gratuite, BYO agent. macOS 26 Tahoe requis"
---

# Supacode

**En une phrase** — application macOS native, « infinite canvas terminal board », qui orchestre des dizaines d'agents de codage CLI en parallèle, chacun dans son environnement isolé.

## Type & intégration
**App macOS native**, bâtie sur **libghostty / GhosttyKit** (le moteur du terminal Ghostty) — **pas Electron**, d'où un argument de **performance native**. Les agents tournent directement dans le terminal intégré, « no translation layer ». **Agent-agnostique** : Claude Code, OpenAI Codex, Opencode, tout agent CLI. Isolation par **worktrees git**. Intégration GitHub (PR, checks CI). ⚠️ Nécessite **macOS 26 Tahoe**.

## Modèle économique
⚠️ **Pas open-source au sens OSI** : licence **Functional Source License v1.1 (FSL-1.1-ALv2)** vérifiée dans le fichier LICENSE (Copyright 2026 **Supabit, LLC**). C'est du **source-available** avec clause **anti-concurrence** (interdit de revendre/substituer le logiciel comme produit concurrent), qui **bascule automatiquement en Apache-2.0 après 2 ans**. La landing dit « Fully open on GitHub » mais le code est sous FSL, pas sous une licence OSI. Distribué en **beta gratuite** (DMG / Homebrew). Dépôt : `supabitapp/supacode`.

## Coût LLM
**Intégré** 🟢 — Supacode n'embarque ni ne gère de LLM : philosophie **bring-your-own-agent**. Tu fais tourner tes agents CLI avec **leurs propres abonnements/identifiants** (Claude Code Pro/Max, Codex…), et tu gères ces coûts indépendamment. Supacode = la couche d'orchestration/UI, sans surcoût de modèle.

⚠️ Comme [Superset (superset-sh)](superset.md) et [Conductor](conductor.md), faire tourner **50+ agents en parallèle** démultiplie l'usage réel des agents → attention aux quotas/limites de débit de tes abonnements.

## À quoi ça sert
Pour les power users macOS « bleeding edge » : piloter une **flotte massive** d'agents de codage sur un canevas visuel, paralléliser fortement les tâches, garder chaque agent isolé. Outil encore jeune (early-stage) mais ambitieux sur le volume (50+).

## Notes / à creuser
- **Troisième orchestrateur d'agents de codage parallèles** du recensement, avec [Conductor](conductor.md) et [Superset (superset-sh)](superset.md). Positionnement Supacode : **natif (libghostty, pas Electron)**, **open-source/gratuit**, volume **50+ agents**, **canevas infini** ; mais **macOS 26 Tahoe requis** (barrière d'entrée).
- Comparaison rapide du sous-cluster :
  - **Supacode** — natif macOS, source-available (FSL-1.1, → Apache-2.0 à 2 ans), 50+ agents, Tahoe requis.
  - **Conductor** — Mac, gratuit propriétaire, BYO abonnement, GitHub only.
  - **Superset** — multi-plateforme (Electron), source-available ELv2, BYOK clés.
- Distinct de [MindFlight Orchestrator (MFO)](mindflight-orchestrator.md) (orchestration de processus métier, pas de codage).

## Source
- Site officiel : https://supacode.sh/
- Revues : everydev.ai, Ry Walker Research

*(vérifié le 2026-06-15 — landing officielle + recherche web)*
