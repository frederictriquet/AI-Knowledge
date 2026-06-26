# Outils IA — recensement

Base d'exploration des outils IA, organisée autour de **trois grandes questions** : *comment utiliser l'IA…*

| | Question | Fichier | Couverture |
|---|----------|---------|------------|
| **Q1** | …pour **produire du code** ? | [Q1 — produire du code](Q1%20-%20produire%20du%20code.md) | ✅ bien fournie |
| **Q2** | …**dans un produit** (LLM intégré, sécurité, agents métier) ? | [Q2 — IA dans un produit](Q2%20-%20IA%20dans%20un%20produit.md) | 🟦 en cours |
| **Q3** | …**au quotidien dans les autres métiers** (marketing, vente…) ? | [Q3 — IA dans les autres métiers](Q3%20-%20IA%20dans%20les%20autres%20métiers.md) | 🚧 à construire |

Chaque outil a une ligne dans le tableau de sa question (regroupé par **famille** de fonction) et une **fiche détaillée** dans [`fiches outils/`](fiches%20outils/). Les candidats encore à arbitrer sont dans [`outils candidats.md`](outils%20candidats.md).

🗺️ Vue transversale : [**SDLC × outils IA — quel outil pour quelle phase**](SDLC%20-%20outils%20IA%20par%20phase.md) (diagramme Mermaid).

## Familles par question

**Q1 — Produire du code**
[1. Agents & IDE de codage](Q1%20-%20produire%20du%20code.md#fam-1) · [2. Connaissance du code](Q1%20-%20produire%20du%20code.md#fam-2) · [3. Optimisation tokens & comportement](Q1%20-%20produire%20du%20code.md#fam-3) · [4. Workflow / méthodologie / spec-driven](Q1%20-%20produire%20du%20code.md#fam-4) · [5. Automatisation de navigateur (MCP)](Q1%20-%20produire%20du%20code.md#fam-5) · [6. Assistants terminal / shell](Q1%20-%20produire%20du%20code.md#fam-6) · [**7. Revue de code par IA**](Q1%20-%20produire%20du%20code.md#fam-7) · [**8. Documentation & sources MCP externes**](Q1%20-%20produire%20du%20code.md#fam-8) · [**9. CI/CD, livraison & ops (IA)**](Q1%20-%20produire%20du%20code.md#fam-9)

**Q2 — IA dans un produit**
[1. Infrastructure RAG / bases vectorielles](Q2%20-%20IA%20dans%20un%20produit.md#fam-1) · [2. Frameworks multi-agents généralistes](Q2%20-%20IA%20dans%20un%20produit.md#fam-2) · [3. Sources de connaissances MCP (données métier)](Q2%20-%20IA%20dans%20un%20produit.md#fam-3) · [4. Orchestration multi-agents & automatisation d'entreprise](Q2%20-%20IA%20dans%20un%20produit.md#fam-4) · [5. Agents autonomes spécialisés par domaine](Q2%20-%20IA%20dans%20un%20produit.md#fam-5) · [6. Sécurité — outils via MCP](Q2%20-%20IA%20dans%20un%20produit.md#fam-6) · [7. Contrôle d'ordinateur / desktop](Q2%20-%20IA%20dans%20un%20produit.md#fam-7) · [**8. LLMOps — évaluation & observabilité**](Q2%20-%20IA%20dans%20un%20produit.md#fam-8) · [**9. Passerelles / routeurs LLM**](Q2%20-%20IA%20dans%20un%20produit.md#fam-9)

**Q3 — IA dans les autres métiers** — 🚧 à définir.

## Grille de lecture : composants d'une boucle → familles d'outils

Le *[loop engineering](fiches/loop-engineering.md)* (Addy Osmani) décrit une boucle d'agents autonome en **6 composants**. Chacun correspond à une famille du recensement — pratique pour naviguer entre **théorie** (`fiches/`) et **outils** (`fiches outils/`) :

| Composant de boucle | Famille(s) du recensement | Exemples d'outils |
|---------------------|---------------------------|-------------------|
| **Automations** (planification : `/loop`, `/goal`, GitHub Actions) | natif Claude Code/Codex + [Q1 fam. 1b](Q1%20-%20produire%20du%20code.md#fam-1b) | orchestrateurs qui planifient/relancent les agents |
| **Worktrees** (isoler le travail parallèle) | [Q1 fam. 1b](Q1%20-%20produire%20du%20code.md#fam-1b) | Conductor, Crystal, Orca, Supacode, Vibe Kanban |
| **Skills** (codifier la connaissance projet, `SKILL.md`) | [Q1 fam. 4](Q1%20-%20produire%20du%20code.md#fam-4) | Superpowers, gstack, BMAD-METHOD, Cavekit, Spec Kit |
| **Plugins / Connectors** (outils externes via MCP) | [Q1 fam. 5](Q1%20-%20produire%20du%20code.md#fam-5) & [8](Q1%20-%20produire%20du%20code.md#fam-8) · [Q2 fam. 3](Q2%20-%20IA%20dans%20un%20produit.md#fam-3), [6](Q2%20-%20IA%20dans%20un%20produit.md#fam-6), [7](Q2%20-%20IA%20dans%20un%20produit.md#fam-7) | navigateur (Playwright…), doc (Context7, Ref…), données (Ansvar), sécurité (Burp…) |
| **Sub-agents** (séparer idéation / vérification) | [Q1 fam. 1b](Q1%20-%20produire%20du%20code.md#fam-1b) & [7](Q1%20-%20produire%20du%20code.md#fam-7) | Liza, Ruflo (disciplinés) ; CodeRabbit, Greptile (vérif) |
| **State / Memory** (mémoire persistante sur disque) | [Q1 fam. 2](Q1%20-%20produire%20du%20code.md#fam-2) | Cavemem, GraphMind, Serena |

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
