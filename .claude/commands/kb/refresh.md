---
description: Re-vérifie à la source les outils du recensement (prix/licence/statut) et propage la maj partout (fiche + lignes de tableau + log) ; déprécie si besoin. Lancé à la demande.
argument-hint: "[nom d'outil | --stale | --all]  (défaut : --stale)"
allowed-tools: WebFetch, WebSearch, Bash(python3 tools/kb_staleness.py:*), Bash(tools/.venv/bin/python tools/kb_lint.py:*), Bash(python3 tools/build_index.py), Bash(curl:*), Read, Grep, Glob, Edit
---
Rafraîchis le recensement d'outils à partir de la **source** : $ARGUMENTS

> **Schéma de référence** : `process/SCHEMA.md` §4 (recensement, légende canonique, règle de vérif des coûts). ⚠️ **Vérifier à la source, ne jamais supposer** licence/prix/coût LLM ; WebFetch/WebSearch — et `curl -A` (UA navigateur) si 403 — **depuis ce thread** (les sous-agents n'ont pas le réseau ici).

**Niveau d'application — « Mixte »** :
- ✅ **Auto** (sans demander) : re-dater `*(verified on YYYY-MM-DD)*` quand **rien n'a changé** ; propager un fait/statut **déjà confirmé** de façon **cohérente sur tous les points de contact** ; corriger liens/ancres cassés.
- ⏸️ **Sur ton OK** (montrer le diff d'abord) : tout **changement factuel** (prix, licence, modèle éco, **icônes coût LLM**) et toute **dépréciation** (rachat, sunset, archivage, 404).

1. **Cibles** — `--stale` (ou aucun argument) → `python3 tools/kb_staleness.py` (catégories PÉRIMÉ > 90 j + NON DATÉ) ; un **nom/slug** → cette fiche seule ; `--all` → toutes les fiches de `wiki/tools/`.
2. **Pour chaque cible** — lire la fiche (URL officielle + faits enregistrés : licence, prix daté, statut, icônes éco/coût LLM), puis **re-vérifier à la source** : page officielle + **pricing**, **fichier LICENSE**, **API GitHub** (`api.github.com/repos/…` : `license.spdx_id`, `archived`, redirection de `full_name`), dépôt/README. Recouper les chiffres ; ne rien inventer.
3. **Diff & verdict** par outil : `inchangé` · `à mettre à jour` (préciser *quoi* : prix/licence/éco/coût LLM) · `à déprécier` (mort / racheté / sunset / archivé / 404).
4. **Points de contact** — la donnée d'un outil vit dans **son frontmatter** (`wiki/tools/<slug>.md` : `pricing_model`/`llm_cost`, `eco_icons`/`llm_cost_icons`, `summary`, `objectives`, `family`). Les tables des pages-sujet sont **générées** depuis ce frontmatter → mettre à jour la **fiche** (pas les tables). Vérifier aussi les **liens croisés** d'autres fiches, `wiki/tools-hub.md` (légende/carte) et `tool-candidates.md`. Le ⚠️ statut sensible va dans le `summary`.
5. **Appliquer** selon le niveau Mixte ; **toujours re-dater** la section Source des fiches touchées. Après édition : `tools/.venv/bin/python tools/kb_lint.py wiki/concepts/…` si une fiche concept est touchée, et **`python3 tools/build_index.py`** pour régénérer index/MOC **et les tables d'outils des pages-sujet** dès qu'un frontmatter change.
6. **Journal** — une entrée `UPDATE` (fait changé) ou `DEPRECATE` (retrait/rachat) **par outil concerné** dans `wiki/log.md`. Si tout est inchangé : un seul `LINT`/`NOTE` récapitulatif (dates rafraîchies).
7. **Digest final** — tableau `outil → verdict`, distinguant ce qui a été **auto-appliqué** de ce qui **attend ton OK**, avec les **sources consultées (datées)**.

Ne déprécier/écraser un fait que sur **preuve à la source**. Doute non tranchable → marquer `❓`/⚠️ et me le signaler, ne pas trancher.
