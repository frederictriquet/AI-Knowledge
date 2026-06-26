---
description: Ajoute un outil IA au recensement (vérif à la source → fiche → ligne de tableau → log).
argument-hint: <nom et/ou URL de l'outil>
---
Ajoute cet outil au recensement d'outils IA : $ARGUMENTS

> **Schéma de référence** : `process/SCHEMA.md` §4 (familles, format de fiche outil, légende d'icônes canonique, règle de vérif des coûts).

Process (convention projet — voir les mémoires `outils-ia-recensement` et `verifier-couts-outils-ia`) :

1. **Vérifier à la source** — WebFetch / WebSearch **depuis ce thread** (⚠️ les sous-agents n'ont pas d'accès réseau ici) : URL officielle, type, **licence exacte**, modèle économique + **pricing chiffré daté**, et surtout le **mécanisme de coût LLM**. Ne **jamais supposer** (licence/prix/coût) — toujours la source (LICENSE, page pricing, code).
2. **Classer** — choisir la **question** (Q1 produire du code · Q2 IA dans un produit · Q3 autres métiers) et la **famille** (cf. `wiki/outils IA.md`). Si aucune famille ne convient, en créer une et me le signaler. Choisir aussi 1–3 **`themes`** dans la taxonomie des 14 (§3.1) — l'axe topique partagé avec les concepts (alimente recherche `kb_search`, MOC, graphe).
3. **Icônes** — **source unique = la légende de [`wiki/outils IA.md`](wiki/outils%20IA.md)** (ne pas la redéfinir ici : si la grille évolue, elle évolue là-bas). Pour mémoire : éco 🔓🎁🔁💳🔒 ; coût LLM 🟢📦💸🔑❓ (combiner si plusieurs modes, ex. 🟢🔑).
   - ⚠️ **Piège récurrent du coût LLM** : un outil qui **pilote tes agents/abonnements existants** (Claude Code, Codex…) sans prendre de clé = **🟢**, *pas* 🔑. **🔑 (BYOK)** = tu fournis une **clé au tool lui-même** (framework, mode autonome). **💸** = l'éditeur **revend** les tokens. En cas de doute non tranchable à la source → **❓**.
4. **Fiche** — créer `wiki/fiches outils/<slug-kebab>.md` au format de `wiki/fiches outils/_TEMPLATE.md` (renseigner `themes: [...]`) ; terminer la section Source par `*(vérifié le AAAA-MM-JJ)*`.
5. **Tableau** — ajouter la ligne sous la bonne famille du fichier Q1/Q2 (et son ancre) : `**[Nom](url)** · [📄](wiki/fiches%20outils/slug.md) | Type | <éco> | <LLM> | résumé une ligne`.
6. **Régénérer** — `python3 tools/build_index.py` (rafraîchit les MOC + l'index) puis `tools/.venv/bin/python tools/kb_embed.py` (rend l'outil cherchable via `kb_search`).
7. **Journal** — ajouter une entrée `TOOL` dans `wiki/log.md`.

Signale tout statut sensible (déprécié, racheté, licence ambiguë, beta) avec ⚠️ dans la fiche **et** la ligne de tableau. Ne pas confondre `wiki/fiches/` (concepts) et `wiki/fiches outils/` (outils).

**Rappel de fraîcheur** : si le contexte de session (hook `SessionStart` → `kb_reminder.py`) signale des fiches périmées, glisse en clôture un court `→ /kb:refresh` (maintenance des données existantes).
