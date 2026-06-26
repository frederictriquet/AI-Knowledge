# Outils IA — recensement

Base d'exploration des outils IA, organisée autour de **trois grands domaines d'usage** :

| Domaine | Fichier | Couverture |
|---------|---------|------------|
| **Produire du code** | [produire du code](guides/generer-du-code-avec-l-ia.md) | ✅ bien fournie |
| **Embarquer l'IA dans un produit** (LLM intégré, sécurité, agents métier) | [IA dans un produit](guides/mettre-de-l-ia-en-production.md) | 🟦 en cours |
| **L'IA pour ceux qui ne codent pas** (marketing, vente…) | [pour ceux qui ne codent pas](guides/ia-pour-ceux-qui-ne-codent-pas.md) | 🚧 à construire |

Chaque outil apparaît dans la **page-sujet** de son/ses objectif(s), regroupé par **famille** de fonction (tables générées depuis le frontmatter), et a une **fiche détaillée** dans [`fiches outils/`](fiches%20outils/). Les candidats encore à arbitrer sont dans [`outils candidats.md`](outils%20candidats.md).

🗺️ Vue transversale : [**SDLC × outils IA — quel outil pour quelle phase**](SDLC%20-%20outils%20IA%20par%20phase.md) (diagramme Mermaid).

## Familles par domaine

**Produire du code**
[1. Agents & IDE de codage](guides/generer-du-code-avec-l-ia.md#fam-agents-ide-qui-codent) · [2. Connaissance du code](guides/generer-du-code-avec-l-ia.md#fam-connaissance-du-code-graphes-recherche-memoire) · [3. Optimisation tokens & comportement](guides/maitriser-le-cout-en-tokens.md#fam-optimisation-des-tokens-du-comportement-de-l-agent) · [4. Workflow / méthodologie / spec-driven](guides/generer-du-code-avec-l-ia.md#fam-workflow-methodologie-developpement-spec-driven) · [5. Automatisation de navigateur (MCP)](guides/generer-du-code-avec-l-ia.md#fam-automatisation-de-navigateur-serveurs-mcp) · [6. Assistants terminal / shell](guides/generer-du-code-avec-l-ia.md#fam-assistants-ia-pour-terminal-shell) · [**7. Revue de code par IA**](guides/generer-du-code-avec-l-ia.md#fam-revue-de-code-par-ia) · [**8. Documentation & sources MCP externes**](guides/generer-du-code-avec-l-ia.md#fam-documentation-sources-de-connaissances-externes-serveurs-mcp) · [**9. CI/CD, livraison & ops (IA)**](guides/generer-du-code-avec-l-ia.md#fam-ci-cd-livraison-operations-assistes-par-ia)

**Embarquer l'IA dans un produit**
[1. Infrastructure RAG / bases vectorielles](guides/mettre-de-l-ia-en-production.md#fam-infrastructure-rag-bases-vectorielles) · [2. Frameworks multi-agents généralistes](guides/mettre-de-l-ia-en-production.md#fam-frameworks-multi-agents-generalistes-pour-developpeurs) · [3. Sources de connaissances MCP (données métier)](guides/mettre-de-l-ia-en-production.md#fam-sources-de-connaissances-donnees-specialisees-serveurs-mcp) · [4. Orchestration multi-agents & automatisation d'entreprise](guides/mettre-de-l-ia-en-production.md#fam-orchestration-multi-agents-automatisation-d-entreprise) · [5. Agents autonomes spécialisés par domaine](guides/mettre-de-l-ia-en-production.md#fam-agents-autonomes-specialises-par-domaine) · [6. Sécurité — outils via MCP](guides/mettre-de-l-ia-en-production.md#fam-securite-outils-exposes-via-mcp) · [7. Contrôle d'ordinateur / desktop](guides/mettre-de-l-ia-en-production.md#fam-controle-d-ordinateur-desktop) · [**8. LLMOps — évaluation & observabilité**](guides/fiabiliser-evaluer-un-systeme-llm.md#fam-llmops-evaluation-observabilite) · [**9. Passerelles / routeurs LLM**](guides/maitriser-le-cout-en-tokens.md#fam-passerelles-routeurs-llm)

**L'IA pour ceux qui ne codent pas** — 🚧 à définir.

## Grille de lecture : composants d'une boucle → familles d'outils

Le *[loop engineering](fiches/loop-engineering.md)* (Addy Osmani) décrit une boucle d'agents autonome en **6 composants**. Chacun correspond à une famille du recensement — pratique pour naviguer entre **théorie** (`fiches/`) et **outils** (`fiches outils/`) :

| Composant de boucle | Famille(s) du recensement | Exemples d'outils |
|---------------------|---------------------------|-------------------|
| **Automations** (planification : `/loop`, `/goal`, GitHub Actions) | natif Claude Code/Codex + [Agents & IDE → orchestrateurs](guides/generer-du-code-avec-l-ia.md#fam-orchestrateurs-systemes-multi-agents-de-codage) | orchestrateurs qui planifient/relancent les agents |
| **Worktrees** (isoler le travail parallèle) | [Agents & IDE → orchestrateurs](guides/generer-du-code-avec-l-ia.md#fam-orchestrateurs-systemes-multi-agents-de-codage) | Conductor, Crystal, Orca, Supacode, Vibe Kanban |
| **Skills** (codifier la connaissance projet, `SKILL.md`) | [Workflow / spec-driven](guides/generer-du-code-avec-l-ia.md#fam-workflow-methodologie-developpement-spec-driven) | Superpowers, gstack, BMAD-METHOD, Cavekit, Spec Kit |
| **Plugins / Connectors** (outils externes via MCP) | [Nav. navigateur](guides/generer-du-code-avec-l-ia.md#fam-automatisation-de-navigateur-serveurs-mcp) & [Doc MCP](guides/generer-du-code-avec-l-ia.md#fam-documentation-sources-de-connaissances-externes-serveurs-mcp) · côté produit : [sources métier](guides/mettre-de-l-ia-en-production.md#fam-sources-de-connaissances-donnees-specialisees-serveurs-mcp), [sécurité](guides/mettre-de-l-ia-en-production.md#fam-securite-outils-exposes-via-mcp), [desktop](guides/mettre-de-l-ia-en-production.md#fam-controle-d-ordinateur-desktop) | navigateur (Playwright…), doc (Context7, Ref…), données (Ansvar), sécurité (Burp…) |
| **Sub-agents** (séparer idéation / vérification) | [Agents & IDE → orchestrateurs](guides/generer-du-code-avec-l-ia.md#fam-orchestrateurs-systemes-multi-agents-de-codage) & [Revue de code](guides/generer-du-code-avec-l-ia.md#fam-revue-de-code-par-ia) | Liza, Ruflo (disciplinés) ; CodeRabbit, Greptile (vérif) |
| **State / Memory** (mémoire persistante sur disque) | [Connaissance du code](guides/generer-du-code-avec-l-ia.md#fam-connaissance-du-code-graphes-recherche-memoire) | Cavemem, GraphMind, Serena |

## Légende

**Type** : Application · Serveur MCP · Plugin · Skill · CLI · Extension IDE · Bibliothèque · Service web

**Modèle économique** (icône) :

| Icône | Sens |
|-------|------|
| 🔓 | Open-source |
| 🎁 | Freemium (gratuit + offre payante) |
| 🔁 | Abonnement |
| 💳 | Paiement à l'usage |
| 🔒 | Propriétaire / payant |

**Coût LLM** — *qui fournit le LLM et comment c'est facturé* (icône) :

| Icône | Sens |
|-------|------|
| 🟢 | *Intégré* — tourne dans/avec Claude Code (ou un abonnement existant), ou observe tes propres appels → pas de coût LLM séparé |
| 📦 | *Inclus* — l'éditeur fournit le LLM dans le prix de l'outil → coût prévisible/plafonné |
| 💸 | *Revendu à l'usage* — l'éditeur fournit le LLM mais facture à la consommation (souvent avec marge) |
| 🔑 | *BYOK* (Bring Your Own Key) — tu fournis ta clé API et paies le fournisseur LLM directement à l'usage |
| ❓ | *Non vérifié* — mécanisme de coût LLM non documenté publiquement / non confirmé |

> Un même produit peut toucher plusieurs familles ; il est classé selon son usage principal. Format d'une ligne de tableau : `**[Nom](url)** · [📄](fiche) | Type | icône éco | icône LLM | résumé une ligne`.
