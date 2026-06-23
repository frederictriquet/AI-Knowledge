---
outil: "Puppeteer MCP"
titre: "Puppeteer MCP"
type: "Serveur MCP (automatisation navigateur)"
url: "https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer"
modele_economique: "Open source (MIT) — gratuit. ⚠️ Serveur de référence officiel archivé/déprécié depuis mai 2025."
cout_llm: "Aucun LLM propre — aucun LLM intégré, le serveur expose des outils consommés par le client MCP (Claude, etc.)"
---

# Puppeteer MCP

**En une phrase** — Serveur MCP de référence (historique) qui pilote Chrome/Chromium via Puppeteer pour permettre à un LLM de naviguer, cliquer, remplir des formulaires, capturer des écrans et exécuter du JavaScript dans un vrai navigateur — aujourd'hui **archivé et déprécié**.

## Type & intégration
Serveur MCP local (Node.js), distribué via `npx -y @modelcontextprotocol/server-puppeteer` ou en image Docker (Chromium headless). Il s'intègre à tout client MCP (Claude Desktop, Claude Code, VS Code, etc.) et expose un petit jeu d'outils fixes :
- `puppeteer_navigate` (aller à une URL)
- `puppeteer_screenshot` (capture page/élément, base64)
- `puppeteer_click`, `puppeteer_hover`, `puppeteer_fill`, `puppeteer_select` (interactions via sélecteurs CSS)
- `puppeteer_evaluate` (exécuter du JS dans la console)

Il expose aussi des ressources : logs de console et captures d'écran nommées. C'est un serveur Chromium uniquement, orienté capture d'écran, avec une surface d'outils volontairement réduite.

Famille « Automatisation & contrôle (navigateur/système) via MCP », aux côtés de [Playwright MCP](playwright-mcp.md) (multi-navigateurs, snapshot d'accessibilité, activement maintenu) et [Firefox DevTools MCP](firefox-devtools-mcp.md) (Firefox). Comparé à Playwright MCP, Puppeteer MCP est plus limité (Chromium seul, pilotage par captures plutôt que par arbre d'accessibilité).

## Modèle économique
Logiciel libre sous licence **MIT**, donc gratuit et redistribuable. Aucun service payant ni revente : on l'exécute soi-même localement. Le code source vit désormais dans le dépôt `modelcontextprotocol/servers-archived`.

## Coût LLM
**BYOK** : le serveur n'embarque aucun modèle. Il ne fait qu'exposer des outils d'automatisation navigateur ; le raisonnement et les appels d'outils sont effectués par le LLM du client MCP (par ex. Claude). Le coût en tokens vient donc du client, et peut être élevé : le pilotage par captures d'écran renvoie des images au modèle, et chaque interaction consomme des allers-retours d'outils.

## À quoi ça sert
- Donner à un agent LLM la capacité de naviguer sur des pages web réelles, remplir/soumettre des formulaires, cliquer, et capturer l'état visuel.
- Scraping piloté par IA, tests exploratoires, automatisation de tâches web simples.
- Exécuter du JavaScript arbitraire dans le contexte d'une page.

## Notes / à creuser
⚠️ **Statut : déprécié et archivé.** Le dépôt de référence a été archivé le 29 mai 2025 (déplacé dans `modelcontextprotocol/servers-archived`, en lecture seule, sans garanties de sécurité ni maintenance). Le paquet npm `@modelcontextprotocol/server-puppeteer` reste téléchargé (~90k/mois) mais est officiellement déprécié.

⚠️ **Sécurité** : avertissements connus — le serveur lance un navigateur sur votre machine et peut accéder aux fichiers locaux et aux IP internes/locales. Des vulnérabilités ont été signalées (SSRF, injection de prompt indirecte, contournement de sandbox — issue #3662 du dépôt). À ne pas utiliser tel quel en environnement sensible.

**Successeur recommandé** : **Chrome DevTools MCP** (`ChromeDevTools/chrome-devtools-mcp`), serveur officiel de l'équipe Chrome de Google, construit sur le Chrome DevTools Protocol (et qui s'appuie d'ailleurs lui-même sur Puppeteer en interne). Il offre une surface bien plus riche (inspection du DOM, trafic réseau, traces de performance/Core Web Vitals, messages de console) et est activement maintenu. [Playwright MCP](playwright-mcp.md) (Microsoft) est l'autre alternative fréquemment citée, multi-navigateurs.

**Homonymes / forks** : plusieurs « puppeteer-mcp » coexistent et prêtent à confusion — le serveur de référence officiel déprécié décrit ici ; des forks communautaires comme `@hisma/server-puppeteer` (mise à jour du SDK MCP) ; et des implémentations indépendantes comme `puppeteer-mcp-server` (par ex. de Meraj Mehrabi), inspirées de l'original mais distinctes. Vérifier précisément le paquet/dépôt visé avant usage.

## Source
- Dépôt archivé : https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer *(vérifié le 2026-06-15)*
- Dépôt des serveurs de référence (issues #3662 sécurité, #4118 SDK) : https://github.com/modelcontextprotocol/servers *(vérifié le 2026-06-15)*
- Paquet npm : https://www.npmjs.com/package/@modelcontextprotocol/server-puppeteer *(vérifié le 2026-06-15)*
- Successeur — Chrome DevTools MCP : https://github.com/ChromeDevTools/chrome-devtools-mcp *(vérifié le 2026-06-15)*
