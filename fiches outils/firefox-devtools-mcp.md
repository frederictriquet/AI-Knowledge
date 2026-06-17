---
outil: "Firefox DevTools MCP"
type: "Serveur MCP (automatisation / inspection navigateur)"
url: https://github.com/freema/firefox-devtools-mcp
modele_economique: "Open-source, double licence MIT / Apache 2.0 — gratuit"
cout_llm: "Aucun LLM propre — outil pour agents ; BYO client (Claude, Cursor…)"
---

# Firefox DevTools MCP

**En une phrase** — serveur MCP qui permet à un agent IA de **piloter et inspecter Firefox** (DevTools) via WebDriver BiDi : naviguer, lire le DOM, capturer le réseau et la console, faire des screenshots, exécuter du JS dans la page.

## Type & intégration
**Serveur MCP**, écrit en **TypeScript** (~84 %), s'appuyant sur **WebDriver BiDi** (via Selenium WebDriver / le protocole de remote debugging de Firefox). Se branche sur Claude Code, Claude Desktop, Cursor, Cline, et tout client MCP. Lancement : `npx firefox-devtools-mcp@latest` (ou la variante `@mozilla/...`, voir lignée ci-dessous), ou via Docker.

Capacités exposées comme outils MCP :
- Navigation et gestion de pages
- Inspection du **DOM** (snapshots + UID)
- Capture et inspection des **requêtes réseau**
- Accès aux **messages console**
- **Screenshots**
- **Évaluation de JavaScript** dans le contexte de la page
- Gestion des **préférences Firefox** et des **extensions**

⚠️ **Local uniquement** : nécessite un Firefox (100+) et Node.js (≥20.19) installés ; ne tourne pas sur du cloud hébergé. Profil Firefox dédié recommandé (sécurité).

## Modèle économique
**Open-source**, **double licence MIT / Apache 2.0** (usage flexible), gratuit. Pas d'offre commerciale.

## Coût LLM
**Aucun LLM propre** 🟢 — c'est un *outil que l'agent utilise*, pas un modèle. Aucun coût côté serveur ; tu apportes ton client IA (BYO abonnement/clé, ex. Claude). Le coût LLM est celui de ton agent.

## À quoi ça sert
Donner à un agent un **navigateur Firefox pilotable** : tests E2E/QA, scraping, reproduction de bugs web, vérification visuelle, automatisation de parcours. Complète les agents de codage quand il faut *agir dans un navigateur réel* (ex. vérifier qu'un changement front fonctionne).

## Notes / à creuser
- **Famille 9 (automatisation/contrôle via MCP)** : première du genre ici — capacité d'**action** sur un environnement externe, distincte des sources de données ([[ansvar-compliance-mcp]]) ou de la connaissance du code ([[serena]]). Voisins de catégorie : Playwright MCP, Puppeteer MCP, Chrome DevTools MCP, computer-use.
- ✅ **Lignée clarifiée** (vérifié via API GitHub) : `freema/firefox-devtools-mcp` **redirige désormais vers `mozilla/firefox-devtools-mcp`** — le projet a été **transféré à Mozilla** (dépôt officiel maintenu). Double licence **MIT OU Apache-2.0** confirmée (fichiers LICENSE-MIT / LICENSE-APACHE ; GitHub affiche NOASSERTION du fait de la double licence). Pour un usage durable, pointer vers le repo Mozilla.
- WebDriver BiDi = standard moderne (vs CDP côté Chrome) → bonne fidélité d'inspection.

## Source
- Dépôt (demandé) : https://github.com/freema/firefox-devtools-mcp · npm : `firefox-devtools-mcp`
- Officiel Mozilla : https://github.com/mozilla/firefox-devtools-mcp · doc : firefox-source-docs.mozilla.org/ai-agent-tools/firefox-devtools-mcp.html

*(vérifié le 2026-06-15 — README GitHub + recherche web)*
