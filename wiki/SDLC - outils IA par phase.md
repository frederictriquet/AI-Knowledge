# SDLC × outils IA — quel outil pour quelle phase

> Vue de synthèse : les phases du cycle de vie logiciel (SDLC) et les outils IA du recensement mobilisables à chaque étape. Dérivé de [produire du code](guides/generer-du-code-avec-l-ia.md) (+ sécurité depuis [Embarquer l'IA dans un produit](guides/mettre-de-l-ia-en-production.md)). Les **icônes de coût/licence** et la liste complète sont dans les tableaux par famille — ici on ne montre que le **mapping**.

```mermaid
flowchart TB
  classDef phase fill:#0d3b66,stroke:#0a2d4d,color:#fff;
  classDef trans fill:#3a2d5c,stroke:#241a3d,color:#fff;
  classDef gap fill:#5c3a3a,stroke:#3d2424,color:#fff;

  P["<b>1 · PLAN &amp; SPEC</b><br/><i>Workflow / méthodo / spec-driven</i><br/>BMAD-METHOD · GitHub Spec Kit · GSD<br/>Task Master · Superpowers · gstack · Cavekit · Pheromind⚠️"]
  C["<b>2 · COMPRENDRE / CONTEXTE</b><br/><i>Connaissance du code</i><br/>Serena · CodeGraph · GraphMind · Polaris · Graphify · Cavemem<br/><br/><i>Doc &amp; sources externes — MCP</i><br/>Context7 · Ref · GitMCP · Exa · MS Learn · AWS Docs"]
  D["<b>3 · CODER</b><br/><i>Agents &amp; IDE</i><br/>Kilo Code · Trae · Continue⚠️<br/><br/><i>Orchestrateurs multi-agents</i><br/>Conductor · Orca · Vibe Kanban · Superset · Supacode<br/>Liza · Ruflo · Multica · Sculptor<br/><br/><i>Terminal / shell</i> : Neo-AI"]
  TE["<b>4 · TESTER (web / UI)</b><br/><i>Automatisation de navigateur — MCP</i><br/>Playwright MCP · Chrome DevTools MCP · Firefox DevTools MCP"]
  R["<b>5 · REVOIR (PR)</b><br/><i>Revue de code par IA</i><br/>CodeRabbit · Greptile · Sentry Seer · Cursor BugBot"]
  S["<b>6 · SÉCURISER</b><br/><i>Défensif</i> : Snyk MCP (SAST/SCA)<br/><i>Offensif / pentest</i><br/>Kali MCP · Burp MCP · ZAP MCP · AIDA · Shannon"]
  O["<b>7 · LIVRER / DÉPLOYER / OPÉRER</b><br/><i>CI/CD, livraison &amp; ops IA</i><br/>Mergify (CI / merge / flaky)<br/>Cleric · Resolve.ai · Traversal (AI SRE / incident)"]

  T["<b>⚙️ TRANSVERSE — coût &amp; comportement</b><br/>RTK · Tokenade · Caveman · Ponytail<br/><i>réduisent tokens d'entrée/sortie & périmètre du code, à toutes les étapes</i>"]

  P --> C --> D --> TE --> R --> S --> O
  O -.->|itération suivante| P
  T -.->|s'applique partout| D

  class P,C,D,TE,R,S,O phase;
  class T trans;
```

## Mapping détaillé (vers les familles, pour les coûts & la liste complète)

| Phase SDLC | Familles d'outils (cliquer → tableau complet + coûts) |
|---|---|
| **1. Plan & spec** | [Workflow / méthodo / spec-driven](guides/generer-du-code-avec-l-ia.md#fam-workflow-methodologie-developpement-spec-driven) |
| **2. Comprendre / contexte** | [Connaissance du code](guides/generer-du-code-avec-l-ia.md#fam-connaissance-du-code-graphes-recherche-memoire) · [Doc & sources MCP](guides/generer-du-code-avec-l-ia.md#fam-documentation-sources-de-connaissances-externes-serveurs-mcp) |
| **3. Coder** | [Agents & IDE](guides/generer-du-code-avec-l-ia.md#fam-agents-ide-qui-codent) · [Orchestrateurs multi-agents](guides/generer-du-code-avec-l-ia.md#fam-orchestrateurs-systemes-multi-agents-de-codage) · [Terminal / shell](guides/generer-du-code-avec-l-ia.md#fam-assistants-ia-pour-terminal-shell) |
| **4. Tester (web/UI)** | [Automatisation de navigateur (MCP)](guides/generer-du-code-avec-l-ia.md#fam-automatisation-de-navigateur-serveurs-mcp) |
| **5. Revoir (PR)** | [Revue de code par IA](guides/generer-du-code-avec-l-ia.md#fam-revue-de-code-par-ia) |
| **6. Sécuriser** | [Sécurité via MCP](guides/mettre-de-l-ia-en-production.md#fam-securite-outils-exposes-via-mcp) · [Agents pentest](guides/mettre-de-l-ia-en-production.md#fam-agents-autonomes-specialises-par-domaine) |
| **7. Livrer / déployer / opérer** | [CI/CD, livraison & ops IA](guides/generer-du-code-avec-l-ia.md#fam-ci-cd-livraison-operations-assistes-par-ia) · [LLMOps](guides/fiabiliser-evaluer-un-systeme-llm.md#fam-llmops-evaluation-observabilite) *(si produit LLM)* |
| **Transverse** | [Optimisation tokens & comportement](guides/maitriser-le-cout-en-tokens.md#fam-optimisation-des-tokens-du-comportement-de-l-agent) |

## Notes honnêtes
- **Phase 7 (livrer / déployer / opérer)** : désormais couverte par la famille [CI/CD, livraison & ops IA](guides/generer-du-code-avec-l-ia.md#fam-ci-cd-livraison-operations-assistes-par-ia) — CI/merge/flaky (**Mergify**) et **AI SRE / incident** (**Cleric · Resolve.ai · Traversal**). Réserves assumées : les AI SRE sont des **SaaS propriétaires enterprise / sur devis** (LLM inclus 📦) et le volet ops **déborde vers « exploiter un produit »** (frontière avec *embarquer l'IA dans un produit*) ; l'[observabilité LLM](guides/fiabiliser-evaluer-un-systeme-llm.md#fam-llmops-evaluation-observabilite) (Langfuse, Helicone…) reste distincte (produit qui embarque un LLM, pas déploiement de code). Le CI-AI le plus « agent » (Datadog Bits AI Dev Agent, Aviator, Trunk) reste en **candidats non vérifiés**.
- **Outils exclus du diagramme car dépréciés** (encore dans les tableaux, avec ⚠️) : **Puppeteer MCP** (archivé), **Crystal** (→ Nimbalyst). **Continue** (⚠️ racheté par Cursor) et **Pheromind** (⚠️ statut flou) gardés mais marqués.
- Le SDLC est **itératif** (la flèche 7→1) : la plupart de ces outils servent à chaque tour de boucle, pas une seule fois.
- Beaucoup d'outils sont **multi-phases** (un agent comme Kilo aide aussi à comprendre/tester) ; ils sont rangés ici à leur **usage principal**.

*(synthèse générée le 2026-06-18 à partir des tableaux par domaine ; re-générer si les familles évoluent.)*
