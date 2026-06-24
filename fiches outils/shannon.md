---
outil: "Shannon (Keygraph)"
titre: "Shannon (Keygraph)"
themes: [securite]
type: "Agent CLI autonome (pentester IA white-box)"
url: https://github.com/KeygraphHQ/shannon
modele_economique: "Open-core : Shannon Lite (AGPL-3.0, open-source, sans backend Keygraph) + Shannon Pro (commercial, prix PUBLIC dès 50 $/dev/mois)"
cout_llm: "Credentials LLM requis MAIS pas que clé brute : OAuth d'abonnement Claude OK (🟢) ou clé API/Bedrock/Vertex (🔑) → 🟢🔑"
---

# Shannon (Keygraph)

**En une phrase** — pentester IA autonome *white-box* qui analyse ton code source, identifie les vecteurs d'attaque et **exécute de vrais exploits** pour prouver les vulnérabilités avant la mise en production. S'il ne peut pas l'exploiter, il ne le reporte pas.

> 🔐 **Cadre d'usage** : sécurité offensive. ⚠️ **Ne jamais lancer contre la production** ni des cibles non autorisées — Shannon **mute l'état applicatif** (crée des utilisateurs, déclenche des requêtes). Exécution en environnement **sandbox / staging / jetable** uniquement, sur des cibles autorisées.

## Type & intégration
**Agent autonome CLI** (lancé via `npx` + Docker), à **workflows multi-agents orchestrés**, écrit en **TypeScript** (~95 %). Approche **white-box** : nécessite l'accès au **code source**. Quatre phases : **reconnaissance → analyse de vulnérabilités (parallèle) → exploitation (parallèle) → reporting**. Cible les failles activement exploitables : injection, XSS, SSRF, authentification/autorisation cassées. Génère des **rapports « proof-by-exploitation »** (PoC reproductible) plutôt que des findings spéculatifs.

## Modèle économique
**Open-core**, par la société **Keygraph** :
- **Shannon Lite** : cœur **open-source AGPL-3.0** (sur GitHub), pour tests strictement autorisés.
- **Shannon Pro** : plateforme AppSec commerciale tout-en-un — black-box, **agentic SAST**, **SCA avec analyse de reachability**, détection de secrets, test de logique métier, intégration **CI/CD**, fonctions entreprise. **Prix public : dès 50 $/dev/mois** (+ add-ons), Enterprise self-hosted sur devis ; programme communautaire gratuit (assos/startups ≤20 devs).

✅ Vérifié (grep du code source) : **aucun backend/compte/télémétrie Keygraph requis pour Lite** — pas d'appel `api.keygraph.io`, pas de posthog/sentry ; les « login » du code concernent l'app **cible** testée.

Argument : combler les « 364 jours » entre deux pentests annuels en intégrant le test continu.

## Coût LLM
**🟢🔑 — credentials LLM obligatoires, mais PAS forcément une clé API payante.** Vérifié dans le code : le preflight échoue sans l'un de `ANTHROPIC_API_KEY` / `CLAUDE_CODE_OAUTH_TOKEN` / `ANTHROPIC_AUTH_TOKEN` (ou Bedrock/Vertex). Mais le setup propose une méthode **OAuth Token** + des presets de retry « subscription » → Shannon Lite **peut tourner sur un abonnement Claude/Claude Code (OAuth), sans clé API brute** (🟢), ou en BYOK clé/Bedrock/Vertex (🔑). Coût selon la **complexité** ; un scan dure ~**1–1,5 h** → tokens potentiellement **significatifs** (analyse de code + exploitation multi-agents).

## À quoi ça sert
Trouver et **prouver** des vulnérabilités exploitables en continu (CI/CD, avant prod), avec une faible part de faux positifs grâce à la validation par exploitation. Performance mise en avant : **96,15 %** de réussite sur le **XBOW Benchmark** (sans indice, source-aware).

## Notes / à creuser
- **Famille 10 (agents autonomes spécialisés)** : deuxième pentester autonome avec [AIDA (AI-Driven Security Assessment)](aida.md). Différences : **Shannon = white-box** (analyse le code source) + **open-core** (Lite AGPL / Pro commercial) + benchmark fort, centré Claude/BYOK ; **AIDA = boîte à outils 400+ via MCP**, AGPL, alpha, model-agnostic. Approches complémentaires (white-box vs tooling).
- ⚠️ Agent qui **exécute des exploits réels** → garde-fous d'environnement essentiels (jetable, isolé, autorisé).
- Variantes tierces vues : `unicodeveloper/shannon` (skill « Automated Pentesting from Keygraph Shannon »), fork `IgorOffline/KeygraphHQ-shannon`. Officiel = `KeygraphHQ/shannon`.

## Source
- Dépôt : https://github.com/KeygraphHQ/shannon · open-source : https://keygraph.io/open-source

*(vérifié le 2026-06-15 — README GitHub + site Keygraph + recherche web)*
