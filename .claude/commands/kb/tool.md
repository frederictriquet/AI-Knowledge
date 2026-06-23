---
description: Ajoute un outil IA au recensement (vérif à la source → fiche → ligne de tableau → log).
argument-hint: <nom et/ou URL de l'outil>
---
Ajoute cet outil au recensement d'outils IA : $ARGUMENTS

> **Schéma de référence** : `process/SCHEMA.md` §4 (familles, format de fiche outil, légende d'icônes canonique, règle de vérif des coûts).

Process (convention projet — voir les mémoires `outils-ia-recensement` et `verifier-couts-outils-ia`) :

1. **Vérifier à la source** — WebFetch / WebSearch **depuis ce thread** (⚠️ les sous-agents n'ont pas d'accès réseau ici) : URL officielle, type, **licence exacte**, modèle économique + **pricing chiffré daté**, et surtout le **mécanisme de coût LLM**. Ne **jamais supposer** (licence/prix/coût) — toujours la source (LICENSE, page pricing, code).
2. **Classer** — choisir la **question** (Q1 produire du code · Q2 IA dans un produit · Q3 autres métiers) et la **famille** (cf. `outils IA.md`). Si aucune famille ne convient, en créer une et me le signaler.
3. **Icônes** — **source unique = la légende de [`outils IA.md`](outils%20IA.md)** (ne pas la redéfinir ici : si la grille évolue, elle évolue là-bas). Pour mémoire : éco 🔓🎁🔁💳🔒 ; coût LLM 🟢📦💸🔑❓ (combiner si plusieurs modes, ex. 🟢🔑).
   - ⚠️ **Piège récurrent du coût LLM** : un outil qui **pilote tes agents/abonnements existants** (Claude Code, Codex…) sans prendre de clé = **🟢**, *pas* 🔑. **🔑 (BYOK)** = tu fournis une **clé au tool lui-même** (framework, mode autonome). **💸** = l'éditeur **revend** les tokens. En cas de doute non tranchable à la source → **❓**.
4. **Fiche** — créer `fiches outils/<slug-kebab>.md` au format de `fiches outils/_TEMPLATE.md` ; terminer la section Source par `*(vérifié le AAAA-MM-JJ)*`.
5. **Tableau** — ajouter la ligne sous la bonne famille du fichier Q1/Q2 (et son ancre) : `**[Nom](url)** · [📄](fiches%20outils/slug.md) | Type | <éco> | <LLM> | résumé une ligne`.
6. **Journal** — ajouter une entrée `TOOL` dans `log.md`.

Signale tout statut sensible (déprécié, racheté, licence ambiguë, beta) avec ⚠️ dans la fiche **et** la ligne de tableau. Ne pas confondre `fiches/` (concepts) et `fiches outils/` (outils).

**Rappel de fraîcheur** : si le contexte de session (hook `SessionStart` → `kb_reminder.py`) signale des fiches périmées, glisse en clôture un court `→ /kb:refresh` (maintenance des données existantes).
