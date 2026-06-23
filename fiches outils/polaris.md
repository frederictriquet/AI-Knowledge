---
outil: "Polaris (polarismcp.com)"
titre: "Polaris (polarismcp.com)"
type: "Serveur MCP / CLI"
url: https://polarismcp.com/
modele_economique: "Open-source (MIT) ; offre Pro payante en préparation"
cout_llm: "Aucun coût LLM propre — embeddings locaux (ONNX), pas d'inférence LLM (réduit la conso de tokens)"
---

# Polaris

**En une phrase** — serveur MCP local-first de recherche sémantique : il indexe la documentation d'un projet et permet aux agents de codage de récupérer des réponses classées, sans cloud ni clé API.

> ⚠️ Homonymie : ne pas confondre avec **Apache Polaris** (catalogue de data lakehouse) et son propre « Polaris MCP Server ». Cette fiche concerne **polarismcp.com**.

## Type & intégration
**Serveur MCP / outil CLI** : un binaire autonome qui tourne **en local** et s'intègre à Claude Code, Cursor, Codex via le Model Context Protocol. Il remplace la récupération de docs par grep par une **recherche hybride** : vecteur (embeddings) + BM25 + ranking.

## Modèle économique
- **Polaris (core)** : open-source, **licence MIT**, gratuit, sur GitHub.
- **Polaris Pro** : abonnement payant **en développement** (−50 % de lancement pour les inscrits à la waitlist).

→ Trajectoire freemium : socle ouvert gratuit + offre Pro à venir.

## Coût LLM
**Aucun coût LLM propre** 🟢. Polaris **ne fait pas d'inférence LLM** : il utilise un **modèle ONNX embarqué** pour calculer les embeddings localement — aucune clé API, aucun service cloud, aucune télémétrie. Comme [CodeGraph](codegraph.md), il *réduit* la facture de l'agent en évitant les coûteux cycles grep-puis-lecture : démo annoncée à **10–40× moins de tokens** consommés.

Ordre de grandeur : coût d'inférence LLM nul côté Polaris ; gain net de tokens côté agent.

## À quoi ça sert
Donner à un agent un accès efficace et pertinent à la **documentation locale** d'un projet (et autres docs) sans tout relire. Cible : développeurs sous Claude Code / Cursor / Codex qui veulent une recherche performante, **100 % locale et privée** (pas de dépendance cloud).

## Notes / à creuser
- Famille proche de [CodeGraph](codegraph.md) (graphe de code, local, sans LLM) et [Graphify](graphify.md) (graphe multi-modal, lui *avec* LLM) : tous visent à réduire tokens/tool-calls des agents, par des moyens différents. Polaris se concentre sur la **recherche sémantique de docs**, en local.
- Local-first + ONNX → bon argument confidentialité.
- Surveiller le contenu/prix de Polaris Pro à sa sortie.

## Source
- Site officiel : https://polarismcp.com/
- Dépôt GitHub (core MIT) — voir lien depuis le site

*(vérifié le 2026-06-15 — landing officielle + recherche web)*
