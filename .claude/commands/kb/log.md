---
description: Ajoute une entrée horodatée au journal log.md (append-only).
argument-hint: "[TYPE] <message>"
allowed-tools: Edit
---
Ajoute une entrée au journal `log.md` : $ARGUMENTS

> **Types** : `process/SCHEMA.md` §7 (= en-tête de `log.md`).

- Format : `AAAA-MM-JJ  TYPE  message`, avec la **date du jour**.
- Si le TYPE n'est pas fourni, choisis le bon parmi : `INGEST` · `TOOL` · `STRUCT` · `UPDATE` · `DEPRECATE` · `LINT` · `NOTE` (cf. l'en-tête de `log.md`).
- **Append-only** : ajoute la ligne **à la fin** du fichier, ne réécris jamais l'existant.
