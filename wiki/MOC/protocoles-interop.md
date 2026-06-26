---
type: index
titre: "MOC — Protocoles & interopérabilité"
theme: protocoles-interop
---

# 🔌 Protocoles & interopérabilité

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Standards d'interopérabilité (MCP, A2A…)._

## Concepts (5)

### 🔴 Substance / cœur
- **[MCP (Model Context Protocol)](../fiches/mcp.md)** — le standard ouvert (Anthropic, 2024) qui branche un modèle sur des outils/données externes via un trio hôte/client/serveur en JSON-RPC 2.0 ; l'« USB-C » de l'intégration d'outils, pas un framework d'orchestration.

### 🟡 Tradeoff / intermédiaire
- **[A2A (Agent2Agent)](../fiches/a2a.md)** — le protocole agent↔agent (Google, avril 2025, désormais Linux Foundation) où chaque agent publie une Agent Card découvrable, puis dialogue en JSON-RPC 2.0 sur HTTPS avec SSE pour le streaming.
- **[ACP (Agent Communication Protocol)](../fiches/acp.md)** — le protocole agent↔agent de BeeAI/IBM, fondé sur REST/HTTP léger (vs JSON-RPC), asynchrone par défaut, avec découverte hors-ligne ; il a fusionné avec A2A sous la Linux Foundation.
- **[Autres protocoles : ANP / AG-UI / Agora / LMOS](../fiches/autres-protocoles.md)** — quatre protocoles émergents au-delà du trio MCP/A2A/ACP : ANP (P2P + identité W3C DID), AG-UI (UI temps réel orientée événements), Agora (négociation de protocole en langage naturel) et LMOS (Internet of Agents d'Eclipse).
- **[KQML & FIPA-ACL](../fiches/kqml-fipa-acl.md)** — les deux langages de communication d'agents (ACL) historiques qui ont normalisé les « actes de communication » (informer, demander, interroger) bien avant les LLM, et que la plupart des frameworks actuels ignorent au profit du langage naturel.

## Outils (0)

- _(aucun)_
