---
description: Répond à une question à partir du wiki (fiches + recensement), avec citations.
argument-hint: <question>
---
Réponds à cette question **à partir de la base de connaissances** : $ARGUMENTS

> **Carte du corpus** (où chercher) : `process/SCHEMA.md` §2.

1. **Cherche** les pages pertinentes : `wiki/concepts/` (concepts — t'appuyer sur `wiki/themes-index.md`), `wiki/tools/` + tableaux par domaine + `wiki/tools-hub.md` (outils). Utilise grep ; au besoin `tools/.venv/bin/python tools/kb_dedup.py --json "reformulation de la question"` pour trouver les fiches sémantiquement proches.
2. **Synthétise** une réponse dense, en **citant les fiches** mobilisées (chemin `wiki/concepts/<slug>.md` ou `wiki/tools/<slug>.md`).
3. **Distingue** ce qui vient du corpus de ce que tu ajoutes de toi-même ; signale explicitement les **manques** (sujet non/mal couvert).
4. Si l'exploration a produit une synthèse réutilisable, **propose** de la reverser dans le corpus (`/kb:ingest` ou nouvelle fiche). Ne l'écris pas sans mon accord.
5. **Rappel de fraîcheur** : si un rappel figure déjà dans le contexte de session (hook `SessionStart` → `kb_reminder.py`) — ou, à défaut, si `python3 tools/kb_staleness.py` signale des fiches PÉRIMÉ/NON DATÉ — termine par une ligne courte `→ lance /kb:refresh pour re-vérifier N fiche(s)`.
