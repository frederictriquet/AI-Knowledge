---
outil: "gstack"
type: "Suite de skills / workflow open-source pour agents de codage IA (Claude Code et compatibles)"
url: https://github.com/garrytan/gstack
modele_economique: "Open-source gratuit (licence MIT) — aucun tier payant ; tu paies uniquement ton agent IA (abonnement Claude Code, API, etc.)"
cout_llm: "Intégré — gstack n'embarque aucun LLM ; il tourne dans/avec ton agent existant (Claude Code, Codex, Cursor...) et consomme son abonnement / sa clé API (BYOK côté agent)"
---

# gstack

**En une phrase** — La configuration personnelle open-source de Garry Tan (CEO de Y Combinator) pour Claude Code : une suite de skills / slash-commands « opinionated » qui font jouer à l'agent IA les rôles d'une équipe complète (CEO, Designer, Eng Manager, Release Manager, Doc Engineer, QA) afin de donner à un développeur solo un effet de levier à l'échelle d'une équipe.

## Type & intégration
Collection de skills (slash-commands) et d'outils helpers (Bun/TypeScript, daemon Chromium persistant pour la QA navigateur) à installer dans un agent de codage IA. Conçue d'abord pour **Claude Code**, mais portable vers une dizaine d'autres hôtes via le standard `SKILL.md` : OpenAI Codex CLI, GitHub Copilot, VS Code, Cursor, etc. Les skills couvrent tout le cycle : produit/planification, implémentation, revue, QA navigateur, design, release/deploy, gestion de mémoire et garde-fous de sécurité. Méthodologie « sprint » imposée : think → plan → build → review → test → ship → reflect, en parallèle sur plusieurs projets.

## Modèle économique
Projet **open-source, licence MIT, entièrement gratuit**. Pas de tier premium, pas de waitlist, pas de revente. Le dépôt a connu une croissance virale (≈90k★ en moins de deux mois, ≈110k★ à mi-2026). Garry Tan revendique avoir expédié 600 000+ lignes de code de production en 60 jours avec cette configuration tout en dirigeant YC à plein temps.

## Coût LLM
**Intégré** au sens de notre grille : gstack n'embarque ni ne facture aucun LLM. C'est une couche de workflow qui s'exécute *dans* un agent de codage IA déjà installé et consomme son moteur. Le coût d'inférence est donc porté par l'agent hôte (abonnement Claude Code, clé API Anthropic, etc.) — autrement dit BYOK / abonnement côté agent, pas côté gstack.

## À quoi ça sert
Donner à un développeur seul un effet de levier maximal (« leverage ») en transformant un agent de codage généraliste en une équipe de spécialistes gouvernée par un processus. L'idée centrale : les agents IA ont besoin d'un *process* (rôles, revues, QA, garde-fous) et pas seulement de prompts. Concrètement on lance des commandes type `/plan-ceo-review`, `/review`, `/browse`, `/qa`, `/codex` pour orchestrer planification, implémentation, revue de code (incluant détection de failles), tests navigateur et release.

## Notes / à creuser
- Apparaît dans le comparatif concurrentiel de [[liza]] (`specs/architecture/competition-survey/mas-survey.md`) comme exemple de « suite/workflow large optimisant la productivité du développeur solo ». Philosophie revendiquée (ETHOS.md) : *Boil the Lake*, *Search Before Building*, *User Sovereignty* — « optimiser pour donner à un humain actif un large banc de workflows spécialisés et des boucles de feedback rapides ».
- Souvent comparé à d'autres frameworks d'orchestration pour Claude Code : **Superpowers**, **GSD**, **GSTACK** (cf. blog Pulumi).
- Homonymie levée : il existe d'autres « gstack » sans rapport (topics GitHub divers, `gstack-opencode` qui est un portage tiers). L'outil visé ici est bien `garrytan/gstack`, lié aux agents de codage IA.

## Source
- https://github.com/garrytan/gstack — dépôt officiel (README, licence MIT, ≈110k★) *(vérifié le 2026-06-15)*
- https://raw.githubusercontent.com/liza-mas/liza/main/specs/architecture/competition-survey/mas-survey.md — positionnement dans le comparatif Liza *(vérifié le 2026-06-15)*
- https://www.pulumi.com/blog/claude-code-orchestration-frameworks/ — comparaison Superpowers / GSD / GSTACK *(vérifié le 2026-06-15)*
