---
titre: "Loop engineering : concevoir le système qui prompte l'agent"
theme: gouvernance-alignement-ops
niveau: 🔴
source_url: https://addyosmani.com/blog/loop-engineering/
source_titre: "Loop Engineering — Addy Osmani"
---

# Loop engineering : concevoir le système qui prompte l'agent

**En une phrase** — Le levier passe du prompt engineering au *loop engineering* : au lieu de prompter l'agent à la main, on conçoit un système autonome qui découvre le travail, le distribue à des agents, vérifie, documente et décide de la suite — sans humain entre les cycles.

## Ce que dit la source
Osmani décrit un glissement : prompter = écrire un prompt, lire la sortie, écrire le suivant — ça ne passe pas à l'échelle. Le **loop engineering** remplace cette orchestration manuelle par une **boucle récursive** auto-alimentée (le **« Factory Model »**). Il distingue l'**agent harness engineering** (concevoir l'environnement d'**un seul** agent) du loop engineering (orchestrer la boucle elle-même). Une boucle se compose de ~6 briques, qu'il mappe sur Codex *et* Claude Code : (1) **Automations** — déclenchement planifié (`/loop`, `/goal`, GitHub Actions) ; (2) **Worktrees** — isoler le travail parallèle (`git worktree`) ; (3) **Skills** — codifier la connaissance projet (format `SKILL.md`) ; (4) **Plugins/Connectors** — outils externes via **MCP** ; (5) **Sub-agents** — séparer **idéation** et **vérification** ; (6) **State/Memory** persistante **sur disque** — la brique souvent oubliée, car « le modèle oublie tout entre les runs ». Exemple : une automation quotidienne lance un skill de triage (échecs CI + issues), spawn un worktree par finding, un sous-agent corrige, un autre vérifie contre les skills et les tests, des connecteurs ouvrent la PR et mettent à jour le ticket, des fichiers d'état préservent le progrès pour le cycle suivant.

## Pourquoi c'est utile
L'article fournit une **grille de lecture unifiée** de l'outillage agentique (les 6 composants = autant de catégories d'outils), nomme le déplacement du levier (du prompt vers la conception de boucle) et reste honnête : « prompter directement tes agents marche aussi ; les boucles ne sont pas universellement supérieures ».

## À retenir
- Loop engineering = orchestrer une boucle autonome ; agent harness engineering = outiller un seul agent.
- Les 6 briques : automations · worktrees · skills · plugins/MCP · sub-agents · **mémoire sur disque** (la plus oubliée).
- Séparer **idéation** et **vérification** dans des sous-agents distincts.
- Garde-fous : la vérification reste **ta** responsabilité ; surveiller le **coût en tokens** (une boucle non surveillée en brûle beaucoup) ; « build the loop, but build it like someone who intends to stay the engineer ».
- Ne pas sur-ingénierer : pour beaucoup de tâches, le prompt direct suffit.

## Voir aussi
- [Revue de code agentique : de l'écriture à la vérification](revue-de-code-agentique.md)
- [Dette de compréhension & cognitive surrender](dette-de-comprehension.md)
- [AgentOps](agentops.md)
- [Human-in-the-loop : interruptions statiques vs dynamiques](hitl-statique-dynamique.md)
