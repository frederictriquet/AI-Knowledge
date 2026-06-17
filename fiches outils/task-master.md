---
outil: "Task Master (Taskmaster)"
type: "CLI + Serveur MCP (gestion de tâches pour agents)"
url: https://github.com/eyaltoledano/claude-task-master
modele_economique: "Open-source (MIT) + offre équipe payante (Hamster Studio)"
cout_llm: "BYOK (15+ providers) — ou hébergé via Hamster"
---

# Task Master (Taskmaster)

**En une phrase** — Outil (CLI + serveur MCP, par eyaltoledano) qui transforme un PRD en **liste de tâches structurées** (dépendances, priorités, critères d'acceptation) pour passer du « vibe coding » à une exécution prévisible par les agents.

## Type & intégration
Fonctionne en **CLI** autonome **et** en **serveur MCP** : intégration native à Claude Code, et support de Cursor, Windsurf, VS Code via MCP — l'agent appelle directement les commandes (générer/découper/ordonner les tâches). ~25k★ sur GitHub.

## Modèle économique
**Cœur open-source MIT**, gratuit pour le dev solo. Offre payante : **Hamster Studio** (plateforme équipe : briefs collaboratifs, édition temps réel, plans d'équipe, sync issue-tracker).

## Coût LLM
- **🔑 BYOK** (mode local) : tes propres clés, 15+ providers (Anthropic, OpenAI, Gemini, Perplexity, Ollama…).
- **🟢 Hébergé** (mode « connected to Hamster ») : inférence hébergée sans clé.

## À quoi ça sert
Donner à l'agent un **plan de tâches discipliné** issu d'une spec/PRD, et le garder sur les rails sur des projets multi-étapes. Complément des méthodos spec-driven (Spec Kit, BMAD).

## Notes / à creuser
- Distinguer le cœur CLI/MCP gratuit (MIT) de la plateforme Hamster (payante, équipe).
- Très populaire dans l'écosystème Cursor/Claude Code.

## Source
https://github.com/eyaltoledano/claude-task-master · https://tryhamster.com/product/taskmaster. *(vérifié le 2026-06-17)*
