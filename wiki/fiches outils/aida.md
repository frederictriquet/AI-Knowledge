---
outil: "AIDA (AI-Driven Security Assessment)"
titre: "AIDA (AI-Driven Security Assessment)"
themes: [securite]
type: "Agent autonome de pentest (CLI + dashboard web)"
url: https://github.com/Vasco0x4/AIDA
modele_economique: "Open-source (AGPL v3), gratuit — projet communautaire"
cout_llm: "Model-agnostic — défaut via Claude Code SANS clé d'API LLM (🟢) ; token seulement pour un endpoint Anthropic-compatible custom (--base-url/--api-key, « Claude Code only », optionnel, 🔑)"
objectifs: [mise-en-prod]
famille: "Agents autonomes spécialisés par domaine"
eco_icones: "🔓"
cout_icones: "🟢🔑"
resume: "Agent de pentest autonome open-source (AGPL v3) reliant un LLM à 400+ outils de sécurité (nmap, sqlmap, ffuf, nuclei + payloads Python) via MCP, en conteneur Docker ; reco → exploitation → scoring CVSS 4.0. Model-agnostic : tourne via Claude Code **sans clé d'API LLM** (défaut) ou endpoint Anthropic-compatible custom (`--api-key`, optionnel). ⚠️ Alpha, tests autorisés uniquement, usage local"
---

# AIDA (AI-Driven Security Assessment)

**En une phrase** — agent de test d'intrusion autonome qui transforme n'importe quel LLM en pentester : tu définis le périmètre, l'agent fait la reconnaissance, l'exploitation et la cartographie des vulnérabilités, tu revois les findings.

> 🔐 **Cadre d'usage** : outil de **sécurité offensive dual-use**, destiné aux **tests d'intrusion autorisés** (engagements de pentest, recherche, CTF, labs). À n'utiliser que sur des systèmes pour lesquels tu as une autorisation explicite.

## Type & intégration
**Agent CLI + dashboard web**. Backend **Python**, frontend **JavaScript/React**, exécution en **conteneur Docker** isolé. Relie l'IA à **400+ outils de pentest** (nmap, sqlmap, ffuf, nuclei…) et génère/exécute des **payloads Python à la volée** (encodage, logique spécifique à un protocole). Interface tool-calling : manipulation HTTP, stockage de credentials, exécution de commandes, scoring **CVSS 4.0** automatique des findings.

**Model-agnostic via MCP** : Claude (Claude Code CLI), Kimi CLI, Gemini, toute API OpenAI-compatible, modèles locaux ou API interchangeables.

## Modèle économique
**Open-source, licence AGPL v3**, gratuit. Projet communautaire (auteur : Vasco0x4) ; pas d'offre commerciale. ⚠️ **Alpha** : usage local recommandé sans durcissement de sécurité additionnel.

## Coût LLM
**Model-agnostic, clé d'API LLM *non* obligatoire** 🟢🔑 — AIDA n'embarque pas de LLM. Vérifié dans le README + `aida.py` :
- **Claude Code** (`python3 aida.py`, défaut) → utilise l'**auth de ton client Claude Code**, **sans clé dédiée** (🟢). Le modèle est « optional, uses CLI default if not specified ».
- **Endpoint Anthropic-compatible custom** : les options `--base-url` / `--api-key` — documentées **« Claude Code only »**, mappées sur `ANTHROPIC_BASE_URL` / `ANTHROPIC_AUTH_TOKEN` — servent à pointer vers une passerelle compatible ; *là seulement* tu fournis le token de cette passerelle (🔑). **Optionnel.**
- **Gemini CLI** via config MCP.

⚠️ **Précision** : le **README ne mentionne aucune clé d'API LLM** (juste `--base-url`). Les occurrences « api-key » du code sont surtout **non-LLM** : `.aida/api-key` (= token du **backend propre d'AIDA**, login interactif, env `AIDA_TOKEN`) et `--mcp-api-key` / `AIDA_MCP_API_KEY` (bearer du transport MCP HTTP).

Donc : pas de clé d'API LLM nécessaire via Claude Code. ⚠️ Quel que soit le mode, un pentest autonome enchaîne **beaucoup d'itérations** → tokens potentiellement **importants** selon le modèle.

## À quoi ça sert
Automatiser des évaluations de vulnérabilités sur applications web, APIs et infrastructures : reconnaissance, scan, exploitation, post-exploitation, le tout orchestré par le LLM avec garde-fou humain (revue des findings). Cible : pentesters, red teams, recherche en sécurité — en environnement autorisé.

## Notes / à creuser
- **Famille 10 (agents autonomes spécialisés par domaine)** : premier du genre ici — un agent dédié à un métier (sécurité offensive), distinct des agents de codage (famille 1) et des serveurs MCP « capacité » (famille 9, ex. [Firefox DevTools MCP](firefox-devtools-mcp.md)). AIDA *consomme* d'ailleurs des outils via MCP, comme la famille 9, mais en étant un **agent métier de bout en bout**.
- ⚠️ **Sécurité/éthique** : exécution conteneurisée recommandée ; risques classiques des agents offensifs (commandes destructrices, faux positifs, exfiltration). Tests autorisés uniquement.
- Écosystème du même auteur : **Neo-AI** (assistant IA pour terminal Linux) → candidat fiche.
- 🔎 **À creuser — composante backend** : `aida.py` s'authentifie auprès d'un `BACKEND_API_URL` via un token obtenu par **login interactif** (`.aida/api-key`, valable 1 an). AIDA n'est donc pas 100 % autonome/local : il y a un **service AIDA** côté serveur (rôle exact, gratuité, données échangées à vérifier).
- Statut alpha → fonctionnalités et stabilité évolutives.

## Source
- Dépôt : https://github.com/Vasco0x4/AIDA · README : github.com/Vasco0x4/AIDA/blob/main/README.md
- Annuaire MCP : lobehub.com/mcp/vasco0x4-aida

*(vérifié le 2026-06-15 — README GitHub + recherche web)*
