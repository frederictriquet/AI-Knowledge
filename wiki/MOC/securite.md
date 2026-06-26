---
type: index
titre: "MOC — Sécurité"
theme: securite
---

# 🔐 Sécurité

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Menaces, injections et défense des systèmes LLM._

## Concepts (21)

### 🔴 Substance / cœur
- **[ASCII Smuggling : cacher des instructions via les Unicode Tags](../fiches/unicode-tags-smuggling.md)** — Un bloc de caractères Unicode (Tags Unicode Block) qui reflète l'ASCII reste invisible à l'humain dans l'UI, mais les LLM l'interprètent — d'où une prompt injection indétectable à l'œil.
- **[Attaques adversariales sur les LLM (taxonomie de Weng)](../fiches/attaques-adversariales-llm.md)** — la mécanique réelle des attaques : à poids gelés et à l'inférence, on distingue cinq familles d'attaques, séparées surtout par l'axe boîte blanche (accès au gradient) vs boîte noire (API seule).
- **[ChatDev : ChatChain, CAMEL, déshallucination communicative](../fiches/chatdev-chatchain.md)** — un cadre qui simule une société de logiciels en cascade (conception/codage/test) via un dialogue à deux agents par phase, où l'assistant inverse délibérément les rôles pour réclamer des précisions avant de coder.
- **[Dual-LLM pattern & CaMeL](../fiches/dual-llm-camel.md)** — défendre contre l'injection *par conception* en séparant les rôles : un LLM privilégié planifie sans jamais lire le contenu non fiable, un LLM en quarantaine traite ce contenu sans aucun privilège.
- **[Injection de prompt](../fiches/prompt-injection.md)** — faire exécuter à un LLM des instructions malveillantes déguisées en entrée légitime, faille irréductible car prompt système et entrée utilisateur partagent le même type : du langage naturel.
- **[Injection de prompt : pourquoi c'est grave (et pourquoi les défenses naïves échouent)](../fiches/injection-pourquoi-cest-grave.md)** — Le problème fondamental (instructions et données partagent le même canal, indissociables), les scénarios d'exfiltration de données, et pourquoi filtrer ou échapper ne suffit pas : « en sécurité, 99 % ne suffit pas ».
- **[Injections IA : prompt injection directe et indirecte](../fiches/ai-injections-basics.md)** — Envoyer des données non fiables à un LLM est l'équivalent moderne d'une SQL Injection ou d'un XSS : l'attaquant reprogramme la « persona » et l'objectif de l'IA.
- **[Jailbreak (débridage)](../fiches/jailbreak.md)** — convaincre un LLM d'ignorer ses garde-fous d'alignement pour produire du contenu interdit, distinct de l'injection (qui déguise des instructions plutôt que de contourner les protections éthiques).
- **[La « lethal trifecta »](../fiches/lethal-trifecta.md)** — l'injection de prompt devient une fuite de données réelle uniquement quand un agent réunit trois capacités simultanées ; en supprimer une seule neutralise toute la classe d'attaque.
- **[Le Dual LLM pattern](../fiches/dual-llm-pattern.md)** — Architecture de défense : un Privileged LLM (avec outils et privilèges, ne voit JAMAIS le contenu non fiable) plus un Quarantined LLM (traite le contenu non fiable, sans privilèges) ; le privileged manipule des références symboliques, pas le texte non fiable.
- **[MITRE ATLAS](../fiches/mitre-atlas.md)** — La matrice des tactiques et techniques adverses contre les systèmes d'IA, calquée sur MITRE ATT&CK et adossée à des études de cas réelles.
- **[Microsoft 365 Copilot : de l'injection à l'exfiltration d'e-mails](../fiches/m365-copilot-exfil.md)** — Une chaîne d'exploitation complète sur M365 Copilot, amorcée par une simple prompt injection dans un e-mail, qui vole les e-mails et données personnelles de la victime.
- **[NIST AI 100-2 : taxonomie de l'adversarial ML](../fiches/nist-ai-100-2.md)** — La taxonomie officielle américaine de l'*adversarial machine learning*, qui distingue IA prédictive et IA générative et classe les attaques (évasion, empoisonnement, atteintes à la vie privée, prompt injection directe/indirecte) selon cinq axes.
- **[OWASP Top 10 for LLM Applications](../fiches/owasp-llm-top-10.md)** — Le référentiel communautaire de référence qui nomme les dix risques de sécurité les plus critiques des applications à base de LLM, désormais prolongé par un volet « Agentic AI ».
- **[Prévenir l'injection de prompt](../fiches/prevent-prompt-injection.md)** — catalogue de défenses partielles contre l'injection de prompt, à empiler en défense en profondeur, aucune n'étant infaillible (la seule garantie absolue serait de ne pas utiliser de LLM).
- **[Skeleton Key & jailbreaks multi-tours](../fiches/skeleton-key.md)** — technique de débridage Microsoft en plusieurs interactions (faire ajouter un avertissement puis produire le contenu interdit), à relativiser face à la menace single-shot, plus discrète mais plus urgente.
- **[Sécurité agentique](../fiches/securite-agentique.md)** — la surface d'attaque d'un agent (décision autonome + appel d'outils) est bien plus large que celle d'un LLM seul, et appelle des contre-mesures de type Zero Trust, moindre privilège et sandbox.
- **[Taxonomie du « prompt hacking »](../fiches/prompt-hacking-taxonomie.md)** — Le rapport structure la sécurité du prompting en trois blocs : types d'attaques (injection vs jailbreak), risques concrets, et mesures de durcissement — aucune n'étant totalement fiable.

### 🟡 Tradeoff / intermédiaire
- **[Garde-fou en nœud d'entrée (Granite Guardian)](../fiches/guardrail-noeud-entree.md)** — placer un détecteur de modération (HAP/PII via Granite Guardian) comme tout premier nœud du graphe, et router via une arête conditionnelle pour bloquer le contenu indésirable AVANT qu'il n'atteigne le LLM et les outils.
- **[OWASP Top 10 LLM & menaces agentiques](../fiches/owasp-llm-agentic.md)** — le référentiel de sécurité standard de fait : une taxonomie partagée des risques LLM, prolongée par un volet spécifique aux menaces agentiques.
- **[Spotlighting](../fiches/spotlighting.md)** — marquer explicitement les données non fiables dans le prompt pour que le modèle distingue « instructions » de « données » et n'exécute pas le contenu injecté.

## Outils (7)

- **[AIDA (AI-Driven Security Assessment)](../fiches%20outils/aida.md)** — _Agent autonome de pentest (CLI + dashboard web)_
- **[Burp Suite MCP Server (PortSwigger)](../fiches%20outils/burp-mcp-server.md)** — _Serveur MCP / extension Burp Suite (Kotlin)_
- **[ECC](../fiches%20outils/ecc.md)** — _Système de harness d'agent (skills/agents/hooks/rules) — multi-plateforme, OSS + GitHub App_
- **[MCP Kali Server](../fiches%20outils/mcp-kali-server.md)** — _Serveur MCP (pont d'exécution de commandes vers Kali Linux)_
- **[MCP ZAP Server](../fiches%20outils/mcp-zap-server.md)** — _Serveur MCP — opérateur OWASP ZAP_
- **[Shannon (Keygraph)](../fiches%20outils/shannon.md)** — _Agent CLI autonome (pentester IA white-box)_
- **[Snyk MCP (serveur MCP du Snyk CLI)](../fiches%20outils/snyk-mcp.md)** — _Serveur MCP (intégré au Snyk CLI) — sécurité défensive / AppSec_
