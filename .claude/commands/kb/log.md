---
description: Add a timestamped entry to the wiki/log.md journal (append-only).
argument-hint: "[TYPE] <message>"
allowed-tools: Edit
---
Add an entry to the `wiki/log.md` journal: $ARGUMENTS

> **Types**: `process/SCHEMA.md` §7 (= header of `wiki/log.md`).

- Format: `YYYY-MM-DD  TYPE  message`, with **today's date**.
- If the TYPE is not provided, choose the right one among: `INGEST` · `TOOL` · `STRUCT` · `UPDATE` · `DEPRECATE` · `LINT` · `NOTE` (see the header of `wiki/log.md`).
- **Append-only**: add the line **at the end** of the file, never rewrite existing content.
