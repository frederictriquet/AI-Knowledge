---
titre: "Hooks déterministes vs mémoire probabiliste (Skills / Memory / Hooks)"
type: "Concept"
theme: gouvernance-alignement-ops
niveau: 🟡
source_url: https://code.claude.com/docs/en/memory
source_titre: "Claude Code Docs — How Claude remembers your project (memory) & Automate actions with hooks"
---

# Hooks déterministes vs mémoire probabiliste (Skills / Memory / Hooks)

**En une phrase** — Pour qu'un agent de code respecte une règle, le mécanisme compte plus que la formulation : une instruction en mémoire (CLAUDE.md) est du **contexte probabiliste** que le modèle *peut* suivre, alors qu'un **hook** est une commande shell exécutée déterministiquement à un point du cycle de vie, qui *garantit* l'action quoi que décide le modèle — d'où la triade « Skills = conseil, Memory = rappel, Hooks = loi ».

## En détail
La doc Claude Code distingue trois leviers pour piloter un agent, par **force d'engagement croissante** :

- **Skills** (`SKILL.md`) — *conseil chargé à la demande.* « Claude uses skills when relevant, or you can invoke one directly with `/skill-name` » ; surtout « a skill's body loads only when it's used » : la procédure ne coûte du contexte que lorsqu'elle sert. C'est de la capacité *optionnelle*, déclenchée par jugement du modèle (ou explicitement par l'humain).
- **Memory / CLAUDE.md** — *rappel.* Chargé au début de chaque session, mais « Claude treats [it] as context, not enforced configuration » : livré « as a user message after the system prompt (…) there's no guarantee of strict compliance, especially for vague or conflicting instructions ». La mémoire *incline* le comportement ; elle ne le contraint pas.
- **Hooks** — *loi.* « Hooks are user-defined shell commands that execute at specific points in Claude Code's lifecycle. They provide **deterministic control** (…) ensuring certain actions **always happen rather than relying on the LLM to choose** to run them. » Un `PreToolUse` hook peut **bloquer** une action (ex. édition d'un fichier protégé, ou « check Gmail avant de drafter un e-mail ») : « To block an action regardless of what Claude decides, use a PreToolUse hook instead. »

La ligne de partage est la **nature de l'exécution**, pas le ton de la consigne : Skills et Memory passent par le LLM (probabiliste, peut être ignoré sous dérive de contexte) ; un Hook est un programme externe (déterministe, s'applique toujours). Corollaire opérationnel donné par la doc : si une instruction *doit* tourner à un moment précis (avant chaque commit, après chaque édition), elle ne se met pas en CLAUDE.md — elle s'écrit en hook.

## Tradeoff / insight pour un senior
- **N'écris pas en mémoire ce qui doit être garanti.** Toute règle « always do X / never do Y » à enjeu (sécurité, secrets, branche protégée, gate de qualité) confiée à CLAUDE.md *finira* par être violée — non par négligence du modèle, mais parce que la consigne est probabiliste par construction. Promeus-la en hook. À l'inverse, mettre en hook ce qui relève du goût (style, préférences) rigidifie inutilement.
- **Coût de contexte = critère de choix, pas seulement la fiabilité.** CLAUDE.md est chargé *en entier* à chaque session et consomme des tokens à chaque tour (cible < 200 lignes) ; un Skill ne coûte qu'à l'usage ; un Hook ne consomme **aucun** token de contexte (il vit hors du modèle). Donc : une procédure longue et occasionnelle → Skill ; une garantie transverse → Hook ; un fait que le modèle se trompe sans lui → CLAUDE.md. Empiler des règles « au cas où » dans CLAUDE.md dégrade à la fois le coût *et* l'adhérence (« Longer files (…) reduce adherence »).
- **Filtre d'écriture de CLAUDE.md** : n'y garder que ce que le modèle rate sans (le savoir public — React, SQL… — est du gaspillage de tokens). Le contre-intuitif : la ligne de style « évidente » est souvent celle que le modèle connaît déjà, et l'invariant obscur qu'on hésite à garder est la seule ligne porteuse.
- **Garde-fou ≠ alignement par prompt.** Le hook est l'incarnation, côté agent de code, du principe de [garde-fou en nœud d'entrée](guardrail-noeud-entree.md) et du [Dual LLM pattern](dual-llm-pattern.md) : la sécurité tient parce qu'elle est *hors* du LLM, pas parce qu'on l'a bien demandé.

## Voir aussi
- [Loop engineering : concevoir le système qui prompte l'agent](loop-engineering.md)
- [Garde-fou en nœud d'entrée (Granite Guardian)](guardrail-noeud-entree.md)
- [Le Dual LLM pattern](dual-llm-pattern.md)
- [Human-in-the-loop : interruptions statiques vs dynamiques](hitl-statique-dynamique.md)
- [LLM Wiki : un wiki maintenu par le LLM plutôt que du RAG](llm-wiki-karpathy.md)
