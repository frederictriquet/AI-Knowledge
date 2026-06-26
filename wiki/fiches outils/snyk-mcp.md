---
outil: "Snyk MCP (serveur MCP du Snyk CLI)"
titre: "Snyk MCP (serveur MCP du Snyk CLI)"
themes: [securite]
type: "Serveur MCP (intégré au Snyk CLI) — sécurité défensive / AppSec"
url: https://snyk.io/articles/secure-ai-coding-with-snyk-now-supporting-model-context-protocol-mcp/
modele_economique: "Plateforme propriétaire freemium — Free + Team (dès ~25 $/mois) + Enterprise ; MCP inclus dans le CLI/les plans"
cout_llm: "Aucun LLM propre — le serveur lance des scans ; BYO client MCP (Cursor, Copilot, Windsurf…)"
objectifs: [mise-en-prod, fiabilite]
famille: "Sécurité — outils exposés via MCP"
eco_icones: "🎁🔁"
cout_icones: "🟢"
resume: "🛡️ **Défensif** : serveur MCP intégré au Snyk CLI permettant à un agent de lancer des scans Snyk Code (SAST) + Snyk Open Source (SCA) et récupérer les vulnérabilités — garde-fou du code généré par l'IA. Compatible Cursor/Copilot/Windsurf… Plateforme freemium (Free / Team dès 25 $/mois). Expérimental"
---

# Snyk MCP (serveur MCP du Snyk CLI)

**En une phrase** — Snyk (plateforme de sécurité applicative pour développeurs) expose ses scans via un serveur MCP intégré à son CLI, pour qu'un agent de codage **détecte les vulnérabilités du code et des dépendances** au fil de la génération — un garde-fou *défensif* des workflows IA.

## Type & intégration
**Serveur MCP intégré au Snyk CLI** (≥ 1.1296.2, **expérimental**), transports **stdio** et **SSE**. Compatible avec les assistants supportant MCP : GitHub Copilot, Continue, Cursor, Windsurf, Qodo, Devin… Outils exposés : déclencher un scan **Snyk Code (SAST)** et **Snyk Open Source (SCA)**, authentification/statut Snyk, récupération des findings dans l'outil connecté. (Snyk couvre aussi conteneurs, IaC, APIs sur sa plateforme.)

## Modèle économique
**Plateforme propriétaire, freemium** : plans **Free** et **Team** (à partir de ~25 $/mois), **Enterprise** sur devis. Le serveur MCP n'a pas de prix propre — c'est une **fonctionnalité du Snyk CLI**, incluse dans les plans existants. (Des composants comme `snyk-ls`/CLI ont une part ouverte sur GitHub, mais la plateforme reste commerciale.)

## Coût LLM
**Aucun LLM propre** 🟢 — le serveur exécute des scans et renvoie des résultats ; le LLM vient de ton client MCP (BYO abonnement/clé). Pas de coût LLM côté Snyk MCP. Le coût « produit » est celui de ton **plan Snyk**, séparé du coût du LLM.

## À quoi ça sert
**Sécuriser le code généré par l'IA en temps réel** : l'agent (Cursor, Copilot…) peut, en langage naturel, lancer un scan Snyk sur le projet, voir les vulnérabilités (code + dépendances open-source) et les corriger dans la foulée. Positionné comme **« developer guardrails for agentic workflows »** : éviter que le vibe-coding n'introduise des failles non détectées.

## Notes / à creuser
- **Famille 9b (sécurité via MCP), volet *défensif*** : à l'inverse des outils **offensifs** du même sous-groupe — [MCP Kali Server](mcp-kali-server.md), [Burp Suite MCP Server (PortSwigger)](burp-mcp-server.md), [MCP ZAP Server](mcp-zap-server.md) (pentest) — Snyk scanne **ton propre code** pour le durcir. Même mécanique (capacité exposée en MCP), finalité opposée.
- Complément naturel des agents de codage (famille 1, ex. [Kilo Code](kilo-code.md)) et des méthodologies (famille 4, ex. [Superpowers](superpowers.md)) : la couche « sécurité » du pipeline IA.
- ⚠️ Statut **expérimental** → API/outils susceptibles d'évoluer.
- Existe aussi des serveurs MCP Snyk **communautaires** (`punkpeye/mcp-snyk`, `snyk/studio-mcp`) ; l'officiel est celui du CLI.

## Source
- Article : https://snyk.io/articles/secure-ai-coding-with-snyk-now-supporting-model-context-protocol-mcp/ · plans : https://snyk.io/plans/
- Docs : docs.snyk.io (Snyk Studio / guardrails agentiques) ; blog « Scan AI-generated code in Cursor with Snyk MCP »

*(vérifié le 2026-06-15 — article Snyk + recherche web)*
