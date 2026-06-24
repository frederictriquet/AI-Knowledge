---
outil: "GitHub Spec Kit"
titre: "GitHub Spec Kit"
themes: [frameworks-outillage, prompting]
type: "Toolkit CLI (spec-driven development)"
url: https://github.com/github/spec-kit
modele_economique: "Open-source (MIT)"
cout_llm: "Intégré (tourne dans ton agent existant)"
---

# GitHub Spec Kit

**En une phrase** — Toolkit open-source de **spec-driven development** (GitHub) : la spec écrite devient l'artefact exécutable qui génère le code, via une CLI `Specify` et des commandes orchestrées par-dessus ton agent de codage.

## Type & intégration
CLI **Specify** (installée via `uv`/`pipx`, requiert Python 3.11+ et Git) qui pose un workflow séquentiel en slash-commands : `/speckit.constitution` → `/speckit.specify` → `/speckit.plan` → `/speckit.tasks` → `/speckit.implement`. **Ne fournit pas de LLM** : c'est une couche de méthode exécutée par un agent existant — Claude Code, GitHub Copilot, Cursor, Gemini CLI, Codex et 24+ autres.

## Modèle économique
**Open-source MIT**, gratuit.

## Coût LLM
**🟢 Intégré** : tourne dans ton agent (Claude Code, etc.) → pas de clé ni de coût LLM propre ; la consommation est celle de l'agent que tu utilises déjà.

## À quoi ça sert
Structurer le dev assisté par IA autour de specs durables (constitution → spec → plan → tâches → implémentation) plutôt que du prompt au fil de l'eau. Même famille que BMAD-METHOD, GSD, Superpowers.

## Notes / à creuser
- Émanation **officielle GitHub** → bonne pérennité a priori.
- Concurrent direct de la méthodo spec-driven de Kiro (AWS) et d'OpenSpec.
- ⚠️ Surcouche de méthode, pas un gain magique : sur des tâches simples le cérémonial spec→plan→tasks ajoute friction et tokens ; pertinent surtout sur des projets multi-étapes durables. Être « officiel GitHub » ne garantit ni traction ni maintenance.

## Source
https://github.com/github/spec-kit (LICENSE = MIT). *(vérifié le 2026-06-17)*
