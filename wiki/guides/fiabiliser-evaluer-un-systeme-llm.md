---
type: guide
titre: "Fiabiliser & évaluer un système LLM"
objectif: fiabilite
description: "Parcours transverse : mesurer, vérifier et garder sous contrôle un système à base de LLM — des évals aux garde-fous."
---

# 🎯 Fiabiliser & évaluer un système LLM

> **Guide par objectif (L3)** — comment savoir si un système LLM *marche*, et le garder fiable dans le temps ?
> Concepts/pratiques ci-dessous ; **outils** (observabilité, évaluation…) en **section Outils** en bas de page.

## En bref

Un système LLM ne se valide pas « à l'œil » : il se **mesure**. La compétence centrale est de partir des **données réelles**, d'en tirer des **évals** spécifiques, puis d'instrumenter la production pour fermer la boucle. La vérification (auto-critique, juges, garde-fous) vient encadrer ce que le modèle produit.

## Parcours de lecture conseillé

1. **Partir des données** — [Error analysis : regarde tes données](../fiches/error-analysis.md) avant tout tableau de bord.
2. **Construire des évals** — [Évaluer les LLM (évals spécifiques)](../fiches/evaluer-les-llm.md), [Eval-driven development](../fiches/eval-driven-development.md), [Évaluation de trajectoire](../fiches/evaluation-trajectoire.md) pour les agents.
3. **LLM-as-judge, bien fait** — [LLM-as-a-judge](../fiches/llm-as-a-judge.md), puis [le faire correctement](../fiches/llm-as-judge-correct.md) et la [vue d'Eugene](../fiches/llm-evaluators.md).
4. **Auto-vérification** — [Chain-of-Verification](../fiches/chain-of-verification.md), [techniques d'auto-critique](../fiches/self-criticism-techniques.md), [Self-Refine](../fiches/self-refine.md).
5. **Garde-fous & sécurité** — [garde-fou en nœud d'entrée](../fiches/guardrail-noeud-entree.md), [sécurité agentique](../fiches/securite-agentique.md).
6. **Tenir dans le temps** — [observabilité LLM](../fiches/observabilite-llm-best-practices.md), [data flywheel](../fiches/data-flywheel-feedback.md), [patterns pour systèmes LLM en production](../fiches/patterns-systemes-llm.md).

## Toutes les fiches de cet objectif

<!-- AUTO:objectif=fiabilite -->
> ⚙️ **Index généré** — 15 fiche(s) taguée(s) `objectifs: [fiabilite]`, régénéré par `tools/build_index.py`. La prose ci-dessus est curée à la main.

### 🧠 Raisonnement & planification
- 🟡 **[Chain-of-Verification (CoVe)](../fiches/chain-of-verification.md)** — le modèle écrit une réponse, en dérive des questions de vérification factuelle, y répond isolément, puis corrige sa réponse à la lumière de ces vérifications.
- 🟡 **[Self-Refine](../fiches/self-refine.md)** — un même modèle produit une sortie, génère sa propre critique, puis se révise, en boucle, sans aucun signal externe.

### ✍️ Prompting
- 🔴 **[Techniques d'auto-critique](../fiches/self-criticism-techniques.md)** — Faire évaluer, vérifier et corriger par le modèle sa propre sortie, en boucle si besoin, pour fiabiliser la réponse sans intervention humaine.

### 📊 Évaluation
- 🔴 **[Data flywheel : collecte de feedback](../fiches/data-flywheel-feedback.md)** — la donnée de production est le seul actif durable d'un produit LLM : capter le feedback utilisateur (explicite et implicite) crée un *flywheel* qui alimente à la fois les évals, le fine-tuning et les guardrails — l'avantage compétitif qui ne se copie pas.
- 🔴 **[Error analysis : regarde tes données](../fiches/error-analysis.md)** — Avant toute métrique, lis manuellement les traces de ton produit, annote les comportements indésirables, puis construis une taxonomie des failure modes et compte leur fréquence.
- 🔴 **[Eval-driven development](../fiches/eval-driven-development.md)** — Construire un système d'évaluation spécifique à ton domaine est la fondation d'un produit IA : c'est lui qui crée la flywheel données → évals → amélioration et débloque le reste.
- 🔴 **[LLM-as-a-judge : le faire correctement](../fiches/llm-as-judge-correct.md)** — Un LLM-as-a-judge n'a de valeur que s'il est aligné sur le jugement binaire pass/fail d'un expert métier via un protocole itératif (« Critique Shadowing »), pas via des scores 1-5 arbitraires.
- 🔴 **[Patterns pour systèmes LLM en production](../fiches/patterns-systemes-llm.md)** — Sept patterns pratiques pour transformer une démo LLM en produit fiable, organisés selon deux axes : améliorer la performance vs réduire coût/risque, et proche de la donnée vs proche de l'utilisateur.
- 🔴 **[Évaluation de trajectoire](../fiches/evaluation-trajectoire.md)** — évaluer la suite des décisions, appels d'outils et étapes intermédiaires qu'a empruntées l'agent, pas seulement la qualité de sa réponse finale.
- 🔴 **[Évaluer les LLM (évals spécifiques à la tâche)](../fiches/evaluer-les-llm.md)** — Les évals « sur étagère » corrèlent mal avec la performance applicative ; Eugene propose des évals concrètes, calibrées par tâche (classification, résumé, traduction, toxicité), sans jamais abandonner l'évaluation humaine.
- 🟡 **[LLM-as-a-judge](../fiches/llm-as-a-judge.md)** — utiliser un LLM, guidé par une rubrique de critères, pour noter automatiquement les sorties d'un agent quand il n'existe pas de vérité terrain à comparer.
- 🟡 **[LLM-evaluators (juges LLM) — vue d'Eugene](../fiches/llm-evaluators.md)** — Synthèse de deux douzaines d'articles sur les LLM-as-a-Judge : quand et comment les utiliser, leurs biais connus, et comment les aligner sur des critères humains.

### 🔐 Sécurité
- 🔴 **[Sécurité agentique](../fiches/securite-agentique.md)** — la surface d'attaque d'un agent (décision autonome + appel d'outils) est bien plus large que celle d'un LLM seul, et appelle des contre-mesures de type Zero Trust, moindre privilège et sandbox.
- 🟡 **[Garde-fou en nœud d'entrée (Granite Guardian)](../fiches/guardrail-noeud-entree.md)** — placer un détecteur de modération (HAP/PII via Granite Guardian) comme tout premier nœud du graphe, et router via une arête conditionnelle pour bloquer le contenu indésirable AVANT qu'il n'atteigne le LLM et les outils.

### ⚖️ Gouvernance, alignement & ops
- 🔴 **[Observabilité LLM : best practices (indépendantes de l'outil)](../fiches/observabilite-llm-best-practices.md)** — instrumenter une app LLM, ce n'est pas brancher un dashboard : c'est décider *quoi* tracer (span par étape de chaîne), *comment* évaluer la qualité sans se ruiner ni se mentir (juge calibré, échantillonné), et *quoi ne pas ingérer* (PII) — l'outil n'est que le réceptacle.
<!-- /AUTO -->

## Outils pour cet objectif

<!-- AUTO-OUTILS:objectif=fiabilite -->
> ⚙️ **Outils générés** — 13 outil(s) `objectifs: [fiabilite]`, groupés par famille. Régénéré par `tools/build_index.py` depuis le frontmatter des fiches outils.

<a id="fam-llmops-evaluation-observabilite"></a>
### LLMOps — évaluation & observabilité

*Maîtriser le comportement d'un LLM **en production** : **tracer** chaque exécution (déboguer une requête), **évaluer** la qualité (datasets, LLM-as-judge, CI), **observer** coûts, latence et erreurs dans le temps. Briques transverses du cycle de vie d'une appli IA — pas de l'assistance au codage.*
> **Cas particulier du coût LLM** : ces outils **observent tes propres appels** sans appeler de LLM eux-mêmes → 🟢 pour le tracing/observabilité. Mais l'**évaluation par LLM-as-judge** consomme des tokens → 🔑 BYOK (parfois revendu à l'usage). D'où la double icône 🟢🔑. Helicone (pur proxy d'observabilité) peut même *réduire* ta facture LLM via son cache.

| Outil | Type | Éco | Coût LLM | En bref |
|---|---|:--:|:--:|---|
| **[Arize Phoenix / Arize AX](https://phoenix.arize.com/)** · [📄](../fiches%20outils/phoenix-arize.md) | Bibliothèque/app open-source (Phoenix) + Service web SaaS (Arize AX) | 🔓🎁🔁💳 | 🟢🔑 | **Phoenix** : observabilité/éval LLM open-source (**Elastic License 2.0**), bâtie sur **OpenTelemetry/OpenInference** (framework-agnostique), self-host gratuit. **Arize AX** : SaaS de monitoring ML/LLM en prod (Free 25k spans/mois → Pro 50 $/mois, Enterprise self-host/SLA/SOC2). Tracing 🟢, éval (`phoenix-evals`) en BYOK |
| **[Braintrust](https://www.braintrust.dev/)** · [📄](../fiches%20outils/braintrust.md) | Service web (SaaS) + SDK | 🎁🔁💳 | 🟢🔑 | Plateforme LLMOps **propriétaire** centrée **évaluation/expérimentation** (datasets, scoring, playground) + logs. Starter gratuit (10 $ de crédits, 10k scores, 14j) → Pro 249 $/mois, Enterprise (on-prem/hybride). Facture data + scores + tokens (proxy LLM : 0,06/0,40 $ par Mtok in/out). Éval LLM-as-judge → tokens (BYOK/crédits) |
| **[Helicone](https://www.helicone.ai/)** · [📄](../fiches%20outils/helicone.md) | Service web (proxy/gateway) + self-host open-source | 🔓🎁🔁 | 🟢 | Observabilité LLM open-source (**Apache 2.0**) surtout via **proxy** : logs, coûts, latence, caching, rate-limit, fallbacks. Self-host gratuit ou cloud (Hobby gratuit 10k requêtes/mois → Pro 79 $, Team 799 $, Enterprise on-prem). Intercepte tes appels, n'en génère pas (🟢) ; le caching peut *réduire* ta facture LLM |
| **[Langfuse](https://langfuse.com/)** · [📄](../fiches%20outils/langfuse.md) | Service web (cloud) + self-host open-source | 🔓🎁🔁 | 🟢🔑 | Plateforme LLMOps open-source (cœur **MIT**, dossiers `ee` commerciaux) : tracing, évaluation, prompt management, datasets. Self-host gratuit ou cloud (Hobby gratuit 50k unités/mois → Core 29 $, Pro 199 $, Enterprise 2 499 $/mois). Obs sans coût LLM (🟢) ; éval LLM-as-judge en BYOK. Alternative OSS à LangSmith |
| **[LangSmith](https://www.langchain.com/langsmith)** · [📄](../fiches%20outils/langsmith.md) | Service web (SaaS) + SDK | 🎁🔁💳 | 🟢🔑 | Plateforme LLMOps **propriétaire** de LangChain : tracing, éval, monitoring ; très intégrée à LangChain/LangGraph mais utilisable sans. Developer gratuit (1 seat, 5k traces/mois) → Plus 39 $/seat/mois (10k traces puis 2,50 $/1k), Enterprise sur devis (**seul** à permettre le self-host/VPC). Obs 🟢, éval LLM-as-judge en BYOK |

<a id="fam-revue-de-code-par-ia"></a>
### Revue de code par IA

*Reviewers IA qui relisent les PR (résumé, bugs, sécurité) — le levier clé quand les agents produisent plus de code qu'on n'en relit. Le LLM est **fourni dans le prix** (📦), pas en BYOK. Cadre conceptuel : [📄 revue de code agentique](../fiches/revue-de-code-agentique.md).*
> **À retenir** : faible recouvrement entre outils (~93 % des findings ne sont vus que par un seul des 4) → en combiner plusieurs aux forces complémentaires (précision vs recall) ; traiter leurs verdicts comme des **signaux**, l'humain garde le merge.

| Outil | Type | Éco | Coût LLM | En bref |
|---|---|:--:|:--:|---|
| **[CodeRabbit](https://www.coderabbit.ai/)** · [📄](../fiches%20outils/coderabbit.md) | Service web (app GitHub/GitLab) + IDE / CLI | 🎁🔁💳 | 📦 | Reviewer IA de PR (GitHub/GitLab) : résumés, revue ligne à ligne, linters + SAST, fix en 1 clic. **Gratuit à vie pour repos publics** ; Pro 24 $, Pro Plus 48 $/user/mois, Enterprise (SSO, self-host). Meilleur **recall** au benchmark Martian (~49 % précision). LLM inclus |
| **[Cursor BugBot](https://cursor.com/bugbot)** · [📄](../fiches%20outils/cursor-bugbot.md) | Service web (app GitHub) | 🔒🔁💳 | 📦 | Reviewer IA de PR d'Anysphere (Cursor) ciblant les **bugs de logique** avec peu de faux positifs (orienté **précision**) ; modèles frontier + maison. Historiquement 40 $/user/mois → **bascule à l'usage** (~1–1,50 $/run, post-8 juin 2026). Compte Cursor requis |
| **[Greptile](https://www.greptile.com/)** · [📄](../fiches%20outils/greptile.md) | Service web (app GitHub) | 🎁🔁💳 | 📦 | Reviewer IA de PR avec **compréhension de toute la codebase** (fort sur l'architecture/contexte) ; ~82 % de bugs attrapés (recall > précision). Pro 30 $/seat/mois (50 revues incluses, +1 $/revue), Enterprise (self-host). Gratuit pour l'OSS qualifié, -50 % startups |
| **[Sentry Seer](https://docs.sentry.io/product/ai-in-sentry/seer/)** · [📄](../fiches%20outils/sentry-seer.md) | Service web (add-on de Sentry) | 🔒🔁💳 | 📦 | Agent IA de debugging de Sentry (Autofix, agent conversationnel, **Code Review**) : prédit les défaillances avant merge, fort sur la **sévérité prod** (adossé à ta télémétrie Sentry). Add-on facturé par contributeur actif (2+ PR/mois). LLM inclus |

<a id="fam-securite-outils-exposes-via-mcp"></a>
### Sécurité — outils exposés via MCP

*🔐 Outils de sécurité pilotables par l'agent : **offensif** (Kali, Burp, ZAP — tests autorisés uniquement, environnement isolé) et **défensif** (Snyk — scan de vulnérabilités de ton propre code).*

| Outil | Type | Éco | Coût LLM | En bref |
|---|---|:--:|:--:|---|
| **[Burp Suite MCP Server (PortSwigger)](https://github.com/PortSwigger/mcp-server)** · [📄](../fiches%20outils/burp-mcp-server.md) | Serveur MCP / extension Burp Suite (Kotlin) | 🔓 | 🟢 | Extension MCP **officielle** de Burp Suite (PortSwigger, GPL-3.0, Kotlin) connectant un client IA à Burp : analyse de requêtes/réponses, génération de payloads contextuels, analyse de JS obfusqué, failles de logique métier, prédiction d'endpoints. BApp Store, BYO client. ⚠️ Burp Community (gratuit) suffit ; Pro requis seulement pour Burp Collaborator (out-of-band). Tests autorisés |
| **[MCP Kali Server](https://www.kali.org/tools/mcp-kali-server/)** · [📄](../fiches%20outils/mcp-kali-server.md) | Serveur MCP (pont d'exécution de commandes vers Kali Linux) | 🔓 | 🟢 | Pont MCP (API Flask) packagé dans Kali (`apt install`) donnant à un agent IA l'accès aux outils de pentest Kali : exécution de commandes (nmap, nxc, curl, gobuster…). Pentest assisté, CTF, HTB/THM. ⚠️ Exécution de commandes — conteneur isolé, contrôle d'accès, tests autorisés uniquement |
| **[MCP ZAP Server](https://github.com/dtkmn/mcp-zap-server)** · [📄](../fiches%20outils/mcp-zap-server.md) | Serveur MCP — opérateur OWASP ZAP | 🔓 | 🟢 | Serveur MCP (Spring Boot, Apache 2.0, par dtkmn) exposant **OWASP ZAP** aux agents : spider, scan actif/passif, import OpenAPI, findings, rapports. Garde-fous « production » (auth API-key/JWT, scopes, rate limits, audit, état Postgres), Docker/Helm. Non affilié OWASP. ⚠️ Tests autorisés |
| **[Snyk MCP (serveur MCP du Snyk CLI)](https://snyk.io/articles/secure-ai-coding-with-snyk-now-supporting-model-context-protocol-mcp/)** · [📄](../fiches%20outils/snyk-mcp.md) | Serveur MCP (intégré au Snyk CLI) — sécurité défensive / AppSec | 🎁🔁 | 🟢 | 🛡️ **Défensif** : serveur MCP intégré au Snyk CLI permettant à un agent de lancer des scans Snyk Code (SAST) + Snyk Open Source (SCA) et récupérer les vulnérabilités — garde-fou du code généré par l'IA. Compatible Cursor/Copilot/Windsurf… Plateforme freemium (Free / Team dès 25 $/mois). Expérimental |
<!-- /AUTO-OUTILS -->
