---
description: Contrôles de santé du corpus (structure, sources, fraîcheur, doublons) + audit optionnel.
allowed-tools: Bash(python3 tools/build_index.py), Bash(python3 tools/kb_staleness.py:*), Bash(tools/.venv/bin/python tools/kb_lint.py:*), Bash(tools/.venv/bin/python tools/kb_check_sources.py:*), Read, Grep, Glob, Agent, Edit
---
**Préalable** : les contrôles déterministes utilisent le venv `tools/.venv` (gitignoré). S'il est absent → suivre le setup de `process/ENRICHISSEMENT.md` (`python3 -m venv tools/.venv` + `pip install -r tools/requirements.txt`) avant de lancer ; sinon les `kb_*.py` échouent.

> **Schéma de référence** : `process/SCHEMA.md` §3 (règles de structure des fiches) & §6 (outillage).

Lance les contrôles de santé de la base, puis fais-moi une synthèse `✅ / ⚠️ / ❌` par contrôle avec la liste des fiches à corriger.

1. **Structure** (déterministe) : `tools/.venv/bin/python tools/kb_lint.py --all`
2. **Index & doublons de titre** : `python3 tools/build_index.py` — ⚠️ **régénère** `wiki/INDEX-THEMATIQUE.md` et `wiki/RAPPORT-CORPUS.md` (ce n'est pas qu'une lecture) ; lis le rapport généré.
3. **Fraîcheur des fiches outils** : `python3 tools/kb_staleness.py` (fiches « vérifié le > 90 j » ou non datées)
4. **Sources** : `tools/.venv/bin/python tools/kb_check_sources.py wiki/fiches/<slug>.md` sur les fiches modifiées récemment (sinon, mentionne que tu sautes ce contrôle).

Ensuite, **propose** (sans le lancer d'office) un **audit de contradictions** plus profond : un sous-agent lit `wiki/fiches/`, `wiki/fiches outils/`, les tableaux par domaine et `wiki/outils IA.md` pour repérer faits contradictoires, statuts périmés non propagés et liens/ancres `#fam-N` cassés. Si je dis oui : lance-le, applique les corrections **réelles** (avec mon accord pour les non triviales), et ajoute une entrée `LINT` dans `wiki/log.md`.
