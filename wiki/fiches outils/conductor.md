---
outil: "Conductor"
titre: "Conductor"
themes: [multi-agents, frameworks-outillage]
type: "Application desktop Mac (orchestrateur d'agents de codage)"
url: https://www.conductor.build/
modele_economique: "App gratuite (propriétaire) ; section Enterprise — BYO abonnement Claude/Codex"
cout_llm: "Intégré — utilise ton abonnement/login Claude Code (ou Codex) existant, pas de coût LLM séparé"
objectifs: [generer-code]
famille: "Orchestrateurs & systèmes multi-agents de codage"
eco_icones: "🔒"
cout_icones: "🟢"
resume: "App Mac (Melty Labs, YC) qui lance en parallèle plusieurs agents Claude Code/Codex/Cursor dans des worktrees git isolés ; review et merge centralisés. **Gratuite mais propriétaire** (Enterprise à venir), utilise ton abonnement Claude/Codex existant. macOS + GitHub uniquement"
---

# Conductor

**En une phrase** — app Mac qui fait tourner plusieurs agents Claude Code (et Codex, Cursor) en parallèle, chacun dans une copie isolée du dépôt, pour voir, relire et merger leurs changements au même endroit.

## Type & intégration
**Application desktop macOS uniquement**, développée par **Melty Labs** (passée par Y Combinator). Orchestrateur d'agents de codage : chaque tâche obtient son **workspace = worktree git** dédié (branche, fichiers, terminal, diff, parcours de review). Conductor ne copie que les fichiers **suivis par git** (pas de duplication de `node_modules`/`.env`). Fonctionne avec ton **login Claude Code local** ; **dépôts GitHub-compatibles** seulement à ce stade.

## Modèle économique
**App gratuite**, **propriétaire** (closed-source). **Pas de page tarifs publique** (/pricing en 404) : aucune offre payante actuelle ; une offre **Enterprise/équipes est annoncée comme à venir** (roadmap, non tarifée). Tu apportes ton propre abonnement Claude ou Codex.

## Coût LLM
**Intégré** 🟢 — Conductor n'ajoute pas de coût de modèle : il s'appuie sur ton **abonnement Claude/Codex existant** (login Claude Code), pas sur des clés API facturées à part. Tu paies déjà l'abonnement de l'agent ; Conductor n'est que la couche d'orchestration.

⚠️ Comme pour [Superset (superset-sh)](superset.md), l'exécution **massivement parallèle** multiplie l'usage réel des agents → attention aux **limites de débit/quotas** de ton abonnement quand 5–10 agents tournent ensemble.

## À quoi ça sert
Paralléliser le travail de codage : lancer plusieurs agents sur des tâches différentes (ou la même, en variantes), suivre d'un coup d'œil ce que fait chacun, puis review/merge. Cible les développeurs Mac qui utilisent déjà Claude Code et veulent passer d'un agent à une **flotte**.

## Notes / à creuser
- **Concurrent direct de [Superset (superset-sh)](superset.md)** : même promesse (agents de codage parallèles, worktrees isolés). Différences : Conductor = **Mac only, gratuit, propriétaire, BYO abonnement** ; Superset = **multi-plateforme (Electron), source-available ELv2, BYOK clés**. Comparatifs existants : Conductor vs Intent (autre orchestrateur macOS).
- Distinct de [MindFlight Orchestrator (MFO)](mindflight-orchestrator.md) (orchestration de processus métier d'entreprise, pas de codage).
- À creuser : contenu/prix de l'offre Enterprise, support hors-GitHub, support Linux/Windows.

## Source
- Site officiel : https://www.conductor.build/ · Docs : https://docs.conductor.build/
- Revue : The New Stack (« Hands-On Review of Conductor »)

*(vérifié le 2026-06-15 — site officiel + recherche web)*
