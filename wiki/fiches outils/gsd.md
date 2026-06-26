---
outil: "GSD (Get Shit Done)"
titre: "GSD (Get Shit Done)"
themes: [prompting]
type: "Framework de méta-prompting / spec-driven development pour agents de codage (couche par-dessus Claude Code & autres)"
url: https://github.com/open-gsd/gsd-core
modele_economique: "Open source (MIT), gratuit — ⚠️ créateur d'origine (TÂCHES) lié à un rug-pull crypto ; utiliser la continuation communautaire open-gsd"
cout_llm: "Intégré (🟢) — s'exécute DANS ton agent existant (Claude Code, Gemini CLI, Codex…), aucune clé d'API LLM dédiée requise ; coût = celui de ton client"
objectifs: [generer-code]
famille: "Workflow, méthodologie & développement spec-driven"
eco_icones: "🔓"
cout_icones: "🟢"
resume: "Framework open-source (MIT) de spec-driven dev par tâches : combat la dégradation de contexte en spawnant des sous-agents à contexte frais ; BYOK. **⚠️ Créateur d'origine (TÂCHES) lié à un rug-pull crypto $GSD + packages npm d'origine abandonnés → n'utiliser que la continuation communautaire `open-gsd` (voir fiche)**"
---

# GSD (Get Shit Done)

> ## ⚠️ AVERTISSEMENT — à lire avant d'installer
> Selon plusieurs sources communautaires et presse (Reddit r/ClaudeAI, AI Weekly, « security heads-up » Skool), le **créateur original** de GSD — **TÂCHES / Lex Christopherson** — est associé à un **rug pull** sur un token crypto **$GSD** (≈ mai 2026) : valeur drainée, comptes sociaux supprimés, créateur devenu injoignable.
> - **Risque concret = chaîne d'approvisionnement** : les **packages npm d'origine restent publiés sans mainteneur**. Une faille ou un compromis futur ne serait corrigé par personne. Les experts recommandent de **désinstaller / éviter les packages d'origine**.
> - **Le code lui-même** (MIT) n'est pas accusé de contenir du malware : le problème est l'**abandon** + l'**historique crypto douteux** du mainteneur d'origine (réputation, pérennité, confiance).
> - ✅ **Voie sûre** : la **continuation communautaire** sous l'organisation **`open-gsd`** (lancée comme *get-shit-done-redux*, miroir MIT bit-for-bit **sans référence au token**, audit de sécurité communautaire ; dépôt canonique actuel **`open-gsd/gsd-core`**, install `npx @opengsd/gsd-core@latest`).
>
> *(rug pull = arnaque où le promoteur d'un projet/token retire brutalement les fonds et disparaît. Avertissement basé sur des rapports communautaires/presse — non confirmé par une source judiciaire ; le redirect officiel du dépôt d'origine, lui, ne mentionne pas l'affaire.)*

**En une phrase** — Système open source de méta-prompting et de développement piloté par specs qui combat la « dégradation de contexte » (context rot) des agents de codage en faisant spawner par de fins orchestrateurs des sous-agents au contexte frais (fenêtres ~200K propres) pour chaque opération significative.

## Type & intégration
Ce n'est pas un agent autonome ni un produit hébergé : c'est une **couche de méthode / framework** (installée via `npx @opengsd/gsd-core@latest`, paquet Node.js) qui s'installe par-dessus un agent de codage existant. Multi-runtime : Claude Code, OpenCode, Gemini CLI, Kimi CLI, Kilo, Codex, GitHub Copilot, Cursor, Windsurf, et d'autres (la doc évoque ~14 runtimes). Il structure le travail selon une boucle de phases (discuss → plan → execute → verify → ship) et environ 15 agents spécialisés (recherche, planification, exécution, vérification). Les orchestrateurs restent fins (10-15 % de contexte) et délèguent à des sous-agents jetables ; l'état est persisté dans des artefacts fichiers (ex. `STATE.md`, `CONTEXT.md`) recombinés via commits git.

## Modèle économique
Projet **open source sous licence MIT**, gratuit. Créé par le développeur **TÂCHES**, lancé en décembre 2025, très populaire (le dépôt historique `gsd-build/get-shit-done` a dépassé ~64k★ avant migration). Pas de revente, pas d'abonnement propre au framework. ⚠️ Mais **modèle de confiance compromis** : monétisation parallèle via un **token crypto $GSD** dont le créateur aurait fait un rug pull (voir avertissement en tête). La continuation **`open-gsd`** est restée purement open-source, sans token.

## Coût LLM
**Intégré 🟢 — aucune clé d'API LLM dédiée** (vérifié : 0 mention de clé/BYOK dans le README). GSD est un framework de méta-prompting Markdown qui **pilote l'agent que tu utilises déjà** ; le coût des tokens est celui de ton runtime (abonnement Claude Code, accès Gemini, etc.), via **ce client**, sans clé propre à GSD. À noter : l'architecture multiplie les sous-agents à contexte frais, ce qui peut augmenter la consommation totale de tokens en échange d'une meilleure qualité maintenue sur de longues sessions.

## À quoi ça sert
Maintenir la qualité de génération de code sur de longues sessions en évitant le « context rot » (réponses qui raccourcissent, instructions oubliées, code incohérent quand la fenêtre se remplit). GSD découpe le travail en plans atomiques, exécute chacun dans un sous-agent au contexte propre, garde la session principale autour de 30-40 % d'occupation, et recolle les résultats. Cible : développement piloté par specs (spec-driven), recherche/planification/vérification structurées plutôt qu'un prompt monolithique.

## Notes / à creuser
- **⚠️ Homonymie levée** : « GSD » est un acronyme courant. Le bon outil est bien **Get Shit Done par TÂCHES** (framework spec-driven pour agents de codage), à ne pas confondre avec d'autres « GSD » (« Git. Ship. Done », gestionnaires de tâches type *getting things done*, etc.).
- **⚠️ Migration de dépôt — et la popularité est restée sur le repo compromis** : le dépôt historique `gsd-build/get-shit-done` (~64k★, par TÂCHES) n'est **plus le foyer actif** et redirige vers le canonique **`open-gsd/gsd-core`**. Or ce canonique « sûr » ne pèse que **~5k★** (API GitHub, 2026-06-24) : les ~64k★ qui font la réputation de « GSD » appartiennent au dépôt rug-pullé, **pas** à la lignée recommandée. À pondérer fortement : tu adoptes un fork communautaire jeune et peu étoilé, pas le phénomène à 64k★.
- **⚠️ Affaire du rug-pull (voir avertissement en tête)** : à distinguer deux choses — (1) la **migration technique** vers `open-gsd`, propre ; (2) l'**affaire crypto $GSD** du créateur d'origine, qui motive justement de **n'utiliser que la lignée `open-gsd`** (sans token, auditée) et d'**éviter les packages npm d'origine** restés sans mainteneur.
- Positionnement vs [Liza](liza.md) : dans le comparatif de Liza, GSD est présenté comme l'archétype des « orchestrateurs LLM qui délèguent à des sous-agents », par opposition à l'architecture *Go-on-LLM* de Liza où des superviseurs **déterministes** imposent mécaniquement des garanties que les agents ne peuvent contourner. Liza souligne aussi que le *file-path passing* et le dimensionnement plan-vers-contexte sont des pratiques communes, pas des innovations propres à GSD.
- Comparable conceptuellement à d'autres surcouches méthodologiques sur agents (specs, sous-agents) — à recouper avec les autres fiches de surcouches/orchestrateurs.

## Source
- Dépôt canonique : https://github.com/open-gsd/gsd-core *(vérifié le 2026-06-15)*
- Dépôt historique (superseded, par TÂCHES, ~64k★) : https://github.com/gsd-build/get-shit-done *(vérifié le 2026-06-15)*
- Comparatif Liza : https://github.com/liza-mas/liza/tree/main/specs/architecture/competition-survey (mas-survey.md) *(vérifié le 2026-06-15)*
- ⚠️ **Avertissement rug-pull** : Reddit r/ClaudeAI (post « if you use the Get Shit Done (GSD) AI tool you need to… ») — fetch direct bloqué ; AI Weekly « Get-Shit-Done creator rug-pulls $GSD token, vanishes » (aiweekly.co/alerts) ; « Security heads-up: the GSD tool » (skool.com/ai-automation-society) *(consultés via recherche web le 2026-06-15)*
- Articles : augmentcode.com/learn/gsd-58k-stars-claude-code ; dev.to (guides GSD) *(vérifié le 2026-06-15)*
