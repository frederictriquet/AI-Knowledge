---
outil: "MCP Kali Server"
titre: "MCP Kali Server"
themes: [securite]
type: "Serveur MCP (pont d'exécution de commandes vers Kali Linux)"
url: https://www.kali.org/tools/mcp-kali-server/
modele_economique: "Open-source (licence MIT, vérifiée via API GitHub), gratuit — packagé dans Kali Linux ; dépôt Wh0am123/MCP-Kali-Server"
cout_llm: "Aucun LLM propre — pont/outil ; BYO client MCP (Claude, Copilot…)"
---

# MCP Kali Server

**En une phrase** — pont MCP qui donne à un agent IA l'accès à la boîte à outils de pentest de Kali Linux : l'agent appelle des outils MCP, qui exécutent les commandes (nmap, nxc, curl, gobuster…) sur une machine/conteneur Kali.

> 🔐 **Cadre d'usage** : outil de **sécurité offensive dual-use**. À réserver aux **tests d'intrusion autorisés** (engagements, CTF, labs HTB/THM) et à exécuter en **environnement isolé** avec contrôle d'accès strict.

## Type & intégration
**Serveur MCP** = **pont API** (Flask, Python) entre les clients MCP (Claude Desktop, GitHub Copilot, Cursor…) et une machine Linux/Kali. L'agent appelle des outils MCP → forwarding vers l'API Flask qui exécute les commandes dans l'environnement Kali (idéalement un **conteneur pré-configuré**). Désormais **packagé officiellement dans Kali** : `sudo apt install mcp-kali-server`. Dépôt amont : `github.com/Wh0am123/MCP-Kali-Server` (dépendances `python3-flask`, `python3-mcp`).

## Modèle économique
**Open-source, licence MIT** (vérifiée via l'API GitHub du dépôt amont `Wh0am123/MCP-Kali-Server`), gratuit ; packagé dans le dépôt d'outils de Kali Linux. Projet communautaire.

## Coût LLM
**Aucun LLM propre** 🟢 — c'est un pont/outil : le LLM (via ton client MCP) émet les requêtes, le serveur exécute les commandes. Pas de coût côté serveur ; tu apportes ton client (BYO abonnement/clé). Comme pour les MCP navigateur ([Firefox DevTools MCP](firefox-devtools-mcp.md), [Playwright MCP](playwright-mcp.md)), le coût LLM est celui de l'agent qui pilote.

## À quoi ça sert
Pentest assisté par IA en temps réel : reconnaissance, scan, interaction web, résolution de challenges CTF, machines HTB/THM — en laissant l'agent enchaîner les outils Kali sous supervision. Rend l'arsenal Kali « callable » par un LLM.

## Notes / à creuser
- **Famille 9 (automatisation & contrôle — volet système/sécurité)** : c'est un **serveur-capacité** (l'agent pilote l'outil), à distinguer de [AIDA (AI-Driven Security Assessment)](aida.md) qui est un **agent de pentest autonome de bout en bout** (famille 10). MCP Kali Server est « l'arsenal Kali exposé en MCP », pas l'orchestrateur.
- ⚠️ **Risque élevé** : un serveur d'**exécution de commandes** exposé à un LLM = surface d'attaque sérieuse (injection de prompt → commandes arbitraires). Isolation conteneur, réseau cloisonné, pas de secrets dans l'environnement, scope autorisé.
- **Plusieurs implémentations** « Kali MCP » coexistent : `Wh0am123/MCP-Kali-Server` (celle packagée par Kali) ; `zebbern/zebbern-kali-mcp` (~130 outils) ; diverses variantes Docker. Vérifier laquelle on déploie.
- Voisins/contexte : analyses critiques (penligent.ai) sur les limites du « Kali + Claude via MCP » pour des équipes pentest réelles.
- ⚠️ Au-delà du risque sécurité déjà noté, l'utilité réelle pour un pentest pro reste discutée : un LLM pilotant Kali produit souvent des enchaînements peu fiables / non reproductibles — à valider sur un vrai engagement avant d'en dépendre.

## Source
- Page Kali : https://www.kali.org/tools/mcp-kali-server/ · dépôt amont : https://github.com/Wh0am123/MCP-Kali-Server

*(vérifié le 2026-06-15 — page officielle Kali + recherche web)*
