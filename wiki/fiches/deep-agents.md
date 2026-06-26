---
titre: "Deep Agents (pattern)"
type: "Concept"
theme: fondamentaux-agents
niveau: 🟡
source_url: https://blog.langchain.com/deep-agents/
---

# Deep Agents (pattern)

**En une phrase** — patron d'architecture d'agent pour les tâches **long-horizon** : au lieu d'une simple boucle « réfléchir → appeler un outil → observer », on combine **planification explicite + sous-agents à contexte isolé + système de fichiers comme mémoire externe + prompt système détaillé** pour tenir la distance sans saturer le contexte.

## L'idée
Une boucle ReAct « plate » se dégrade sur les tâches longues : le contexte se remplit (« context rot »), le plan se perd, les détails s'effacent. Le pattern *deep agents* — articulé par LangChain, **inspiré de Claude Code et de Deep Research (Anthropic)** — corrige ça avec **quatre piliers** :

1. **Prompt système détaillé** — instructions riches (quand planifier, quand déléguer, comment se servir des fichiers), souvent avec exemples. C'est le « cerveau » du harness.
2. **Outil de planification** — un outil de *to-do* (souvent quasi no-op, ex. `write_todos`) qui **force l'agent à expliciter et ré-ancrer son plan** dans le contexte récent, contre la dérive.
3. **Sous-agents à contexte isolé** — déléguer une sous-tâche à un agent **au contexte propre** (« context quarantine ») : le détail reste chez le sous-agent, seul le résultat remonte → le contexte de l'agent principal reste **mince**.
4. **Système de fichiers (mémoire externe)** — lire/écrire/éditer des fichiers pour **décharger** le contexte et **persister** l'état entre étapes/sessions, au lieu de tout garder dans la fenêtre.

L'effet net : le contexte de l'orchestrateur reste **lean**, la mémoire vit **dehors** (fichiers), le travail lourd est **délégué** à des sous-agents jetables, et le plan est **ré-affirmé** régulièrement.

## Tradeoff / quand l'utiliser
- **Pour** : tâches **multi-étapes / longues** (recherche approfondie, gros refactor, workflow métier) où une boucle simple s'effondre.
- **Contre** : **surcoût en tokens et en latence** (planification, spawns de sous-agents, I/O fichiers) → **disproportionné** pour une tâche courte, où un ReAct/function-calling direct suffit. Exige un **modèle capable** (bon tool-calling + suivi d'instructions) et ajoute de la **complexité d'orchestration**.
- À situer par rapport à [react](react.md) (boucle de base), à l'[architecture canonique d'agent](agent-architecture-canonique.md) et aux [structures multi-agents](structures-multi-agents.md) : *deep agents* est une **recette de harness** qui assemble planification, délégation et mémoire externe — pas un nouvel algorithme.

## Source primaire
LangChain, *Deep Agents* — articulation du pattern (planning tool, sub-agents, virtual file system, detailed system prompt). Blog : https://blog.langchain.com/deep-agents/ ; doc : https://docs.langchain.com/oss/python/deepagents/overview *(vérifié — HTTP 200, 2026-06-17)*. Inspirations citées : Claude Code et Deep Research (Anthropic).

## Voir aussi
- [react](react.md) · [react-vs-function-calling](react-vs-function-calling.md) — la boucle de base que ce pattern dépasse
- [agent-architecture-canonique](agent-architecture-canonique.md) · [structures-multi-agents](structures-multi-agents.md) · [orchestration-types](orchestration-types.md) — délégation / sous-agents
- [planification-goal-state-action](planification-goal-state-action.md) · [self-reflection-agents](self-reflection-agents.md) — le pilier planification
- [memoire-court-long-terme](memoire-court-long-terme.md) · [voyager-skill-library](voyager-skill-library.md) — mémoire externe & skills
- Implémentation produit : `deepagents` (LangChain) → [fiche outil](../fiches%20outils/deepagents.md)
