---
outil: "Superpowers"
titre: "Superpowers"
themes: [frameworks-outillage]
type: "Plugin / framework de skills agentiques (multi-plateforme)"
url: https://github.com/obra/superpowers
modele_economique: "Open-source (MIT), gratuit (sponsorships GitHub)"
cout_llm: "Intégré — tourne dans ton agent (Claude Code…), BYO LLM, pas de coût séparé"
---

# Superpowers

**En une phrase** — framework de skills agentiques *composables* doublé d'une méthodologie complète de développement logiciel, qui empêche l'agent de foncer tête baissée dans le code et lui impose design review, TDD et planification systématique.

## Type & intégration
**Plugin / framework de skills**, créé par **Jesse Vincent (`obra`)** et l'équipe de **Prime Radiant**. Multi-plateforme : Claude Code (marketplace officielle Anthropic), Codex CLI/App, Cursor, GitHub Copilot CLI, Gemini CLI, Factory Droid, OpenCode. Installation type Claude Code : `/plugin install superpowers@claude-plugins-official`.

S'appuie sur des **skills composables** qui se déclenchent automatiquement selon le contexte, et structure le travail en ~7 étapes : brainstorming → git worktrees → planification → exécution → TDD → revue de code (par sous-agents) → finition de branche. Inclut la capacité d'**écrire de nouvelles skills**.

## Modèle économique
**Open-source, licence MIT**, gratuit. L'auteur accepte des **sponsorships** (GitHub Sponsors) ; pas de tier commercial annoncé. Très populaire (**~237k★**, API GitHub), souvent présenté comme le plugin de skills phare de l'écosystème Claude Code — popularité ≠ adéquation à ton besoin (voir limite ci-dessous).

## Coût LLM
**Intégré** 🟢 — aucun LLM embarqué : Superpowers s'exécute dans ton agent (Claude Code et autres) et utilise **ton propre abonnement / tes clés** (BYO). Pas de coût LLM séparé ; la dépense réelle dépend de l'agent sous-jacent. Note : une méthodo plus rigoureuse (TDD, sous-agents de revue) peut augmenter le nombre d'étapes/tokens, en échange d'une meilleure qualité.

## À quoi ça sert
Imposer une vraie méthodologie d'ingénierie à un agent : sans elle, un Claude Code « vanilla » sur un projet complexe écrit du code sans tests, mélange les responsabilités et produit un prototype fragile. Superpowers force TDD, découpage en tâches de 2-5 min avec specs explicites, revue par sous-agents, debugging systématique. Adopté/documenté par des praticiens connus (ex. Simon Willison).

## Notes / à creuser
- ⚠️ **Quand NE PAS l'utiliser** : sur un correctif simple ou un script jetable, imposer brainstorming + worktrees + TDD + revue par sous-agents est du **surengineering** — surcoût en latence et en tokens (multiplication des étapes/sous-agents) pour un gain nul. Le bénéfice se concentre sur les projets complexes et durables.
- **Famille 4 (workflow/méthodologie)** : même catégorie que [Cavekit](cavekit.md), [BMAD-METHOD](bmad-method.md), [GSD (Get Shit Done)](gsd.md) et [gstack](gstack.md) — des surcouches qui structurent *comment* l'agent travaille. Superpowers est le plus populaire et le plus « méthodologie complète » du groupe (TDD + sous-agents + skills extensibles).
- Recoupe le sous-cluster 1b par l'usage de **sous-agents** pour la revue, mais reste une **méthodologie/skill** (pas un runner de flotte comme [Orca](orca.md)/[Superset (superset-sh)](superset.md)).
- Skills extensibles → on peut écrire les siennes ; écosystème de skills tierces.

## Source
- Dépôt : https://github.com/obra/superpowers · Plugin Claude : https://claude.com/plugins/superpowers
- Analyse : Simon Willison, « Superpowers: How I'm using coding agents in October 2025 » (simonwillison.net)

*(vérifié le 2026-06-15 — README GitHub + recherche web)*
