---
outil: "Chrome DevTools MCP"
titre: "Chrome DevTools MCP"
type: "Serveur MCP (automatisation navigateur)"
url: https://github.com/ChromeDevTools/chrome-devtools-mcp
modele_economique: "Open-source (Apache 2.0) — projet officiel de l'équipe Chrome (Google), gratuit, distribué via npm"
cout_llm: "Aucun LLM propre — aucun LLM intégré ; le serveur s'utilise depuis un agent (Claude, Cursor, Copilot…) qui apporte son propre modèle"
---

# Chrome DevTools MCP

**En une phrase** — Serveur MCP officiel de l'équipe Chrome (Google) qui donne à un agent de code le contrôle d'un Chrome réel via le Chrome DevTools Protocol et Puppeteer, avec un accent marqué sur les traces de performance et le débogage approfondi.

## Type & intégration
Serveur MCP (Model Context Protocol) écrit en TypeScript, exécuté sous Node.js (version LTS) et lancé typiquement via `npx chrome-devtools-mcp@latest`. Il se branche sur n'importe quel client MCP (Claude Code/Desktop, Cursor, GitHub Copilot, etc.) par une configuration JSON standard. Sous le capot, il combine le **Chrome DevTools Protocol (CDP)** pour l'inspection bas niveau et **Puppeteer** pour piloter le navigateur et attendre automatiquement la fin des actions.

## Modèle économique
Open-source sous licence **Apache 2.0**, gratuit. C'est un dépôt officiel de l'organisation `ChromeDevTools` (Google), activement maintenu (largement étoilé, publications fréquentes, ex. v1.2.0). Aucun coût de licence ; la seule dépendance est un Chrome/Chromium local.

## Coût LLM
Aucun modèle de langage n'est embarqué : c'est un pur fournisseur d'outils pour un agent externe. Le coût LLM est donc celui de l'agent appelant (BYOK). À noter que l'inspection riche (traces de performance, snapshots DOM, logs réseau/console) peut renvoyer des sorties volumineuses : à surveiller pour la consommation de contexte de l'agent.

## À quoi ça sert
- **Traces de performance** : enregistrement et extraction d'« insights » actionnables (angle distinctif via CDP).
- **Débogage navigateur** : inspection des requêtes réseau, messages de console (avec stack traces source-mappées), snapshots mémoire/heap.
- **Automatisation** : navigation, clics, remplissage de formulaires, captures d'écran/snapshots, évaluation de scripts dans le DOM, le tout avec attente automatique des résultats.

Cas d'usage : laisser un agent reproduire un bug, mesurer la performance d'une page, ou inspecter un état réseau/DOM vivant.

## Notes / à creuser
- Famille « Automatisation & contrôle (navigateur) via MCP », aux côtés de [Playwright MCP](playwright-mcp.md) (Microsoft), [Puppeteer MCP](puppeteer-mcp.md) (l'ancien serveur Puppeteer, déprécié) et [Firefox DevTools MCP](firefox-devtools-mcp.md).
- **Positionnement vs le Puppeteer MCP déprécié** : le serveur officiel `@modelcontextprotocol/server-puppeteer` est déprécié. Le successeur généralement recommandé pour l'automatisation cross-navigateur est plutôt **[Playwright MCP](playwright-mcp.md)** (snapshots d'accessibilité, multi-navigateurs). Chrome DevTools MCP n'est donc pas un simple remplaçant 1:1 de Puppeteer MCP : il se démarque par l'angle **CDP + traces de performance + débogage Chrome approfondi**, là où Playwright MCP vise l'interaction DOM déterministe à grande échelle.
- Spécifique à Chrome/Chromium (pas de cross-navigateur natif), contrairement à Playwright MCP.
- Il existe plusieurs forks/implémentations communautaires homonymes (benjaminr, ctrlShiftBryan, diegorafs…) ; la fiche vise le dépôt officiel `ChromeDevTools/chrome-devtools-mcp`.

## Source
- https://github.com/ChromeDevTools/chrome-devtools-mcp
- https://www.npmjs.com/package/chrome-devtools-mcp
- https://mcpservers.org/servers/github-com-chromedevtools-chrome-devtools-mcp *(vérifié le 2026-06-15)*
