---
outil: "Playwright MCP"
type: "Serveur MCP (automatisation navigateur)"
url: https://github.com/microsoft/playwright-mcp
modele_economique: "Open-source (Apache 2.0, Microsoft) — gratuit, sans backend propriétaire"
cout_llm: "Aucun LLM propre — l'outil ne consomme aucun jeton ; le coût LLM dépend du client MCP qui l'orchestre"
---

# Playwright MCP

**En une phrase** — Serveur MCP officiel de Microsoft qui permet à un agent LLM de piloter un vrai navigateur (clics, saisie, navigation, extraction) en s'appuyant sur l'arbre d'accessibilité de la page plutôt que sur des captures d'écran.

## Type & intégration
Serveur MCP (Model Context Protocol) open-source, distribué en paquet npm `@playwright/mcp` et exécutable via `npx @playwright/mcp@latest` (Node.js 18+). Une image Docker officielle existe (`mcr.microsoft.com/playwright/mcp`).

Il s'intègre comme n'importe quel serveur MCP dans de nombreux clients : Claude Code, Claude Desktop, Cursor, VS Code, Windsurf, Goose, Cline, GitHub Copilot, LM Studio, Warp, etc.

Particularité technique majeure : il pilote le navigateur via l'**arbre d'accessibilité** (accessibility tree) de Playwright, sérialisé en un format texte type YAML optimisé pour les LLM, et non via des screenshots / vision par pixels. Conséquences : déterministe, rapide, économe en jetons, et ne nécessite pas de modèle multimodal. Navigateurs supportés via le moteur Playwright : **Chromium, Firefox et WebKit** (plus les canaux Chrome et Microsoft Edge).

## Modèle économique
Entièrement gratuit et open-source. Licence **Apache 2.0**, copyright Microsoft Corporation. Aucun service hébergé ni licence payante ; le code s'exécute en local (ou dans un conteneur que l'on héberge soi-même).

## Coût LLM
L'outil en lui-même n'appelle aucun LLM et ne consomme pas de jetons : c'est un exécuteur d'actions navigateur. Le coût provient du **client MCP** qui orchestre les appels (par ex. Claude Code), donc **BYOK** — vous payez le modèle de votre client. Atout : comme l'état de page est exposé sous forme d'arbre d'accessibilité textuel compact (et non d'images), la consommation de jetons est nettement plus faible qu'avec une approche par captures d'écran.

## À quoi ça sert
- Donner à un agent IA la capacité d'agir réellement sur le web : remplir des formulaires, cliquer, naviguer, extraire des données structurées.
- Boucles agentiques persistantes : automatisation exploratoire, tests auto-réparants, scraping assisté, workflows autonomes longs.
- Alternative « structurée » aux approches « computer use » par vision : plus rapide et plus fiable lorsque la page expose une bonne sémantique d'accessibilité.

## Notes / à creuser
- Famille « Automatisation & contrôle (navigateur/système) via MCP », aux côtés de [[firefox-devtools-mcp]]. Différence d'approche : Playwright MCP s'appuie sur l'**arbre d'accessibilité** (sémantique, multi-moteur), là où firefox-devtools-mcp passe par le protocole bas-niveau **WebDriver BiDi** / DevTools de Firefox (introspection plus fine du navigateur, mais ciblée Firefox).
- Voisins / concurrents directs : **Puppeteer MCP** (équivalent côté Puppeteer, Chromium) et **Chrome DevTools MCP** (officiel Google, débogage/perf via DevTools de Chrome).
- Limite de l'approche accessibility-tree : sur des pages mal balisées (sémantique d'accessibilité pauvre, canvas, contenu purement visuel), un agent peut être moins efficace qu'avec une approche par vision.
- Projet très actif (33k+ étoiles GitHub, releases fréquentes alignées sur les versions de Playwright).

## Source
- https://github.com/microsoft/playwright-mcp *(vérifié le 2026-06-15)*
- https://raw.githubusercontent.com/microsoft/playwright-mcp/main/LICENSE — licence Apache 2.0 *(vérifié le 2026-06-15)*
- https://www.npmjs.com/package/@playwright/mcp — paquet npm `@playwright/mcp` *(référence)*
