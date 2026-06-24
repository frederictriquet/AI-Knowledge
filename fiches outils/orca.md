---
outil: "Orca"
titre: "Orca"
themes: [multi-agents, frameworks-outillage]
type: "Application desktop (Mac/Win/Linux) + mobile — Agent Development Environment (ADE)"
url: https://www.onorca.dev/
modele_economique: "Open-source (MIT), gratuit"
cout_llm: "Intégré — BYO agent ; utilise tes abonnements/clés existants (Claude Code, Codex, Gemini… 25+)"
---

# Orca

**En une phrase** — « Agent Development Environment » (ADE) open-source : un IDE pensé pour piloter une **flotte d'agents de codage en parallèle**, où chaque agent devient une carte Kanban dans son worktree git isolé.

## Type & intégration
**Application desktop multi-plateforme** (macOS, Windows, **Linux**) — et **mobile** — développée par **stablyai** (YC W2026). Environnement de type IDE pour agents : terminal, éditeur de fichiers, navigateur intégrés. **Agent-agnostique** : Claude Code, Codex, OpenCode, Gemini, Grok, Cursor CLI… 25+ agents CLI.

Fonctions notables :
- **Board Kanban** pour suivre la progression de chaque agent en drag-and-drop.
- **Worktrees git isolés** (pas de stash ni de switch de branche), une prompt → **5 agents en parallèle**, puis comparaison et merge.
- **Terminaux WebGL** inspirés de Ghostty (avec splits).
- **Navigateur Chromium intégré** avec « Design Mode ».
- **Worktrees SSH distants**, **account switching** entre plusieurs abonnements d'agents.
- Intégrations **GitHub** et **Linear**, annotation de diffs.

## Modèle économique
**Open-source, licence MIT**, **gratuit**, sans abonnement. Téléchargeable sur onorca.dev ou via GitHub Releases (github.com/stablyai/orca).

## Coût LLM
**Intégré** 🟢 — Orca n'embarque pas de LLM : philosophie **bring-your-own-agent**. Tu utilises tes **abonnements/clés existants** sur les agents (Claude Code Pro/Max, Codex, etc. ; API en BYOK possible). Orca = couche d'orchestration + UI, sans surcoût de modèle. L'`account switching` aide à jongler entre plusieurs abonnements.

⚠️ Comme tout le sous-cluster, exécuter une **flotte d'agents en parallèle** multiplie l'usage réel → surveiller quotas et limites de débit.

## À quoi ça sert
Gérer le travail de plusieurs agents comme un tableau de bord : lancer, comparer, annoter, merger. Positionnement « control center for parallel AI agents », promesse « ship 100x ». Le plus riche en fonctionnalités du sous-cluster (Kanban, browser, SSH, Linear, mobile).

## Notes / à creuser
- **Quatrième orchestrateur d'agents de codage parallèles** du recensement, avec [Superset (superset-sh)](superset.md), [Conductor](conductor.md), [Supacode](supacode.md). Positionnement Orca : **cross-platform (Mac/Win/Linux) + mobile**, **MIT open-source/gratuit**, fonctionnalités les plus larges (Kanban, navigateur Design Mode, worktrees SSH, Linear).
- Comparaison rapide du sous-cluster :
  - **Orca** — Mac/Win/Linux + mobile, MIT, Kanban + browser + SSH + Linear, 25+ agents.
  - **Supacode** — macOS natif (libghostty), open-source, 50+ agents, Tahoe requis.
  - **Conductor** — Mac, gratuit propriétaire, BYO abonnement, GitHub only.
  - **Superset** — multi-plateforme (Electron), source-available ELv2, BYOK clés.
- Distinct de [MindFlight Orchestrator (MFO)](mindflight-orchestrator.md) (orchestration de processus métier d'entreprise, pas de codage).

## Source
- Site officiel : https://www.onorca.dev/ (et orcabuild.ai) · Docs : https://www.onorca.dev/docs
- Dépôt : https://github.com/stablyai/orca

*(vérifié le 2026-06-15 — site officiel + GitHub + recherche web)*
