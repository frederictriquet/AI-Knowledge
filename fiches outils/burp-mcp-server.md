---
outil: "Burp Suite MCP Server (PortSwigger)"
titre: "Burp Suite MCP Server (PortSwigger)"
themes: [securite]
type: "Serveur MCP / extension Burp Suite (Kotlin)"
url: https://github.com/PortSwigger/mcp-server
modele_economique: "Open-source (GPL-3.0) — extension gratuite ; nécessite Burp Suite (Community gratuit / Pro payant)"
cout_llm: "Aucun LLM propre — pont/extension ; BYO client MCP (Claude Desktop…)"
---

# Burp Suite MCP Server (PortSwigger)

**En une phrase** — extension **officielle** de Burp Suite qui expose ses capacités via le Model Context Protocol, permettant à un client IA (Claude Desktop…) d'interagir programmatiquement avec Burp pour assister le test de sécurité web.

> 🔐 **Cadre d'usage** : sécurité offensive — à réserver aux tests d'intrusion **autorisés**. (Risque moindre que l'exécution de commandes brute : l'assistance se fait *dans* Burp, mais reste un outil offensif.)

## Type & intégration
**Extension Burp Suite** (Java/**Kotlin** ~99 %) qui fait tourner un **serveur MCP en SSE** sur `localhost:9876`, avec un **proxy stdio** packagé pour les clients comme Claude Desktop (installation auto pour Claude Desktop). Les outils MCP exposés sont définis dans le code (`Tools.kt`). Disponible dans le **BApp Store** de PortSwigger. Installation : build du JAR via Gradle, puis chargement comme extension Burp. Option de sécurité « autoriser les outils qui éditent la config » désactivable.

S'inscrit dans la stratégie plus large **« Burp AI »** de PortSwigger.

## Modèle économique
- **Extension : open-source GPL-3.0**, gratuite (sur GitHub, ~900★).
- **Burp Suite lui-même** : requis pour l'utiliser — mais **Burp Community (gratuit) suffit** pour l'extension MCP (vérifié). **Seule** la fonctionnalité **Burp Collaborator** (tests out-of-band) requiert **Burp Pro** (payant). Donc pas besoin de Pro pour la majorité des usages.

## Coût LLM
**Aucun LLM propre** 🟢 — l'extension est un pont : le LLM vient de **ton client MCP** (BYO abonnement/clé, ex. Claude). Pas de coût côté extension. Comme [MCP Kali Server](mcp-kali-server.md) et les MCP navigateur ([Firefox DevTools MCP](firefox-devtools-mcp.md)), le coût LLM est celui de l'agent qui pilote.

## À quoi ça sert
Doper le pentest web manuel avec l'IA, sans quitter Burp :
- Envoyer requêtes/réponses à l'IA pour analyser le comportement d'un endpoint et ses faiblesses.
- **Générer des payloads contextuels** pour des points d'injection.
- Analyser du **JavaScript obfusqué** (sections sensibles).
- Repérer des **failles de logique métier** sur des process multi-étapes.
- **Prédire des endpoints** et repérer des appels API sensibles.

## Notes / à creuser
- **Famille 9 (automatisation & contrôle — volet sécurité)** : serveur-capacité officiel d'un éditeur (PortSwigger), à distinguer des **agents autonomes** [AIDA (AI-Driven Security Assessment)](aida.md)/[Shannon (Keygraph)](shannon.md) (famille 10). Sibling sécurité de [MCP Kali Server](mcp-kali-server.md) (Kali) — l'un expose Burp, l'autre l'arsenal Kali.
- Avantage « officiel » : maintenu par l'éditeur de Burp, intégration propre (BApp Store), vs implémentations communautaires de MCP sécurité.
- ⚠️ Exposer Burp à un LLM = données de test sensibles envoyées au modèle ; prudence avec un LLM cloud sur des cibles/clients réels.

## Source
- Dépôt : https://github.com/PortSwigger/mcp-server · BApp Store : portswigger.net/bappstore/9952290f04ed4f628e624d0aa9dccebc
- Contexte : blog PortSwigger « Burp AI »

*(vérifié le 2026-06-15 — README GitHub + BApp Store + recherche web)*
