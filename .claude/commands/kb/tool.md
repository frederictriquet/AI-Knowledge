---
description: Ajoute un outil IA au recensement (vérif à la source → fiche + frontmatter → régénération des tables → log).
argument-hint: <nom et/ou URL de l'outil>
---
Ajoute cet outil au recensement d'outils IA : $ARGUMENTS

> **Schéma de référence** : `process/SCHEMA.md` §4 (familles, format de fiche outil, légende d'icônes canonique, règle de vérif des coûts).

Process (convention projet — voir les mémoires `outils-ia-recensement` et `verifier-couts-outils-ia`) :

1. **Vérifier à la source** — WebFetch / WebSearch **depuis ce thread** (⚠️ les sous-agents n'ont pas d'accès réseau ici) : URL officielle, type, **licence exacte**, modèle économique + **pricing chiffré daté**, et surtout le **mécanisme de coût LLM**. Ne **jamais supposer** (licence/prix/coût) — toujours la source (LICENSE, page pricing, code).
2. **Classer** — choisir le(s) **`objectifs`** (parmi `OBJECTIFS` : generer-code · fiabilite · couts · mise-en-prod · pratiques-non-codeurs ; **multi-valué**, un outil peut servir plusieurs buts) et la **`famille`** (cf. carte dans `wiki/outils IA.md`). Famille nouvelle → la créer et ajouter sa prose (intro + éventuelle « clé de lecture ») dans `tools/familles.json`. Choisir aussi 1–3 **`themes`** (taxonomie des 14, §3.1) — axe topique partagé avec les concepts.
3. **Icônes** — **source unique = la légende de [`wiki/outils IA.md`](wiki/outils%20IA.md)**. éco 🔓🎁🔁💳🔒 ; coût LLM 🟢📦💸🔑❓ (combiner si besoin, ex. 🟢🔑).
   - ⚠️ **Piège récurrent du coût LLM** : un outil qui **pilote tes agents/abonnements existants** (Claude Code, Codex…) sans prendre de clé = **🟢**, *pas* 🔑. **🔑 (BYOK)** = tu fournis une **clé au tool lui-même**. **💸** = l'éditeur **revend** les tokens. Doute non tranchable → **❓**.
4. **Fiche + frontmatter** — créer `wiki/fiches outils/<slug-kebab>.md` au format de `wiki/fiches outils/_TEMPLATE.md`. Renseigner le frontmatter **complet**, dont les clés qui pilotent la génération des tables : `objectifs: [...]`, `famille: "..."`, `eco_icones: "..."`, `cout_icones: "..."`, `resume: "résumé une ligne"` (+ `themes`). Le **`resume`** porte le ⚠️ si statut sensible (déprécié, racheté, beta). Terminer la section Source par `*(vérifié le AAAA-MM-JJ)*`.
5. **Régénérer** — `python3 tools/build_index.py` : la **ligne de tableau de l'outil est générée automatiquement** dans la/les page(s)-sujet de ses `objectifs` (groupée par `famille`) — **ne pas éditer de table à la main**. Puis `tools/.venv/bin/python tools/kb_embed.py` (rend l'outil cherchable via `kb_search`).
6. **Journal** — ajouter une entrée `TOOL` dans `wiki/log.md`.

Ne pas confondre `wiki/fiches/` (concepts) et `wiki/fiches outils/` (outils).

**Rappel de fraîcheur** : si le contexte de session (hook `SessionStart` → `kb_reminder.py`) signale des fiches périmées, glisse en clôture un court `→ /kb:refresh` (maintenance des données existantes).
