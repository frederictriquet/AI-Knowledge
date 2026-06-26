---
outil: "Crystal"
titre: "Crystal"
themes: [multi-agents, frameworks-outillage]
type: "Application desktop (Electron) — orchestrateur d'agents"
url: https://github.com/stravu/crystal
modele_economique: "Open-source (MIT) — ⚠️ déprécié, successeur Nimbalyst"
cout_llm: "Intégré (BYO agent : ton Claude Code / Codex)"
objectifs: [generer-code]
famille: "Orchestrateurs & systèmes multi-agents de codage"
eco_icones: "🔓"
cout_icones: "🟢"
resume: "App Electron (Stravu, **MIT**) lançant plusieurs sessions **Claude Code / Codex en parallèle** dans des worktrees git isolés ; test/compare/merge. BYO agent. ⚠️ **Déprécié (fév. 2026)** → successeur **Nimbalyst**"
---

# Crystal

**En une phrase** — App desktop (Electron, Stravu) pour lancer et comparer **plusieurs sessions Claude Code / Codex en parallèle** dans des worktrees git isolés, puis fusionner la meilleure approche.

## Type & intégration
Application desktop locale : on crée plusieurs sessions d'agent sur des worktrees git distincts, on les fait travailler en parallèle sur des variantes, on inspecte/teste et on merge. ⚠️ **Déprécié (fév. 2026)** : remplacé par **Nimbalyst** (successeur actif — ajoute session kanban, éditeurs visuels markdown/mockups/diagrammes, app iOS). Crystal reste utilisable mais n'est plus maintenu.

## Modèle économique
**Open-source MIT**, gratuit. Crystal n'ajoute aucun coût propre ; tu utilises tes abonnements/clés Claude Code ou Codex existants.

## Coût LLM
**🟢 BYO agent** : Crystal pilote des agents que tu fournis (Claude Code, Codex) avec leur propre auth → pas de clé LLM ni de facturation propre à Crystal.

## À quoi ça sert
Paralléliser le travail d'un agent de codage (tester plusieurs pistes en même temps plutôt qu'en séquentiel) sans gérer les worktrees à la main. Même famille que Conductor, Orca, Vibe Kanban.

## Notes / à creuser
- ⚠️ Préférer **Nimbalyst** pour un usage durable (Crystal n'est plus mis à jour).
- Concurrents maintenus : Conductor, Orca, Supacode, Vibe Kanban.

## Source
https://github.com/stravu/crystal · https://nimbalyst.com/crystal/ (annonce de succession). *(vérifié le 2026-06-17)*
