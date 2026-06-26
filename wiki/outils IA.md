# Outils IA — recensement

Base d'exploration des outils IA, organisée autour de **trois grands domaines d'usage** :

| Domaine | Fichier | Couverture |
|---------|---------|------------|
| **Produire du code** | [produire du code](produire-du-code.md) | ✅ bien fournie |
| **Embarquer l'IA dans un produit** (LLM intégré, sécurité, agents métier) | [IA dans un produit](ia-dans-un-produit.md) | 🟦 en cours |
| **L'IA pour ceux qui ne codent pas** (marketing, vente…) | [pour ceux qui ne codent pas](ia-pour-ceux-qui-ne-codent-pas.md) | 🚧 à construire |

Chaque outil a une ligne dans le tableau de son domaine (regroupé par **famille** de fonction) et une **fiche détaillée** dans [`fiches outils/`](fiches%20outils/). Les candidats encore à arbitrer sont dans [`outils candidats.md`](outils%20candidats.md).

🗺️ Vue transversale : [**SDLC × outils IA — quel outil pour quelle phase**](SDLC%20-%20outils%20IA%20par%20phase.md) (diagramme Mermaid).

## Familles par domaine

**Produire du code**
[1. Agents & IDE de codage](produire-du-code.md#fam-1) · [2. Connaissance du code](produire-du-code.md#fam-2) · [3. Optimisation tokens & comportement](produire-du-code.md#fam-3) · [4. Workflow / méthodologie / spec-driven](produire-du-code.md#fam-4) · [5. Automatisation de navigateur (MCP)](produire-du-code.md#fam-5) · [6. Assistants terminal / shell](produire-du-code.md#fam-6) · [**7. Revue de code par IA**](produire-du-code.md#fam-7) · [**8. Documentation & sources MCP externes**](produire-du-code.md#fam-8) · [**9. CI/CD, livraison & ops (IA)**](produire-du-code.md#fam-9)

**Embarquer l'IA dans un produit**
[1. Infrastructure RAG / bases vectorielles](ia-dans-un-produit.md#fam-1) · [2. Frameworks multi-agents généralistes](ia-dans-un-produit.md#fam-2) · [3. Sources de connaissances MCP (données métier)](ia-dans-un-produit.md#fam-3) · [4. Orchestration multi-agents & automatisation d'entreprise](ia-dans-un-produit.md#fam-4) · [5. Agents autonomes spécialisés par domaine](ia-dans-un-produit.md#fam-5) · [6. Sécurité — outils via MCP](ia-dans-un-produit.md#fam-6) · [7. Contrôle d'ordinateur / desktop](ia-dans-un-produit.md#fam-7) · [**8. LLMOps — évaluation & observabilité**](ia-dans-un-produit.md#fam-8) · [**9. Passerelles / routeurs LLM**](ia-dans-un-produit.md#fam-9)

**L'IA pour ceux qui ne codent pas** — 🚧 à définir.

## Grille de lecture : composants d'une boucle → familles d'outils

Le *[loop engineering](fiches/loop-engineering.md)* (Addy Osmani) décrit une boucle d'agents autonome en **6 composants**. Chacun correspond à une famille du recensement — pratique pour naviguer entre **théorie** (`fiches/`) et **outils** (`fiches outils/`) :

| Composant de boucle | Famille(s) du recensement | Exemples d'outils |
|---------------------|---------------------------|-------------------|
| **Automations** (planification : `/loop`, `/goal`, GitHub Actions) | natif Claude Code/Codex + [Agents & IDE → orchestrateurs](produire-du-code.md#fam-1b) | orchestrateurs qui planifient/relancent les agents |
| **Worktrees** (isoler le travail parallèle) | [Agents & IDE → orchestrateurs](produire-du-code.md#fam-1b) | Conductor, Crystal, Orca, Supacode, Vibe Kanban |
| **Skills** (codifier la connaissance projet, `SKILL.md`) | [Workflow / spec-driven](produire-du-code.md#fam-4) | Superpowers, gstack, BMAD-METHOD, Cavekit, Spec Kit |
| **Plugins / Connectors** (outils externes via MCP) | [Nav. navigateur](produire-du-code.md#fam-5) & [Doc MCP](produire-du-code.md#fam-8) · côté produit : [sources métier](ia-dans-un-produit.md#fam-3), [sécurité](ia-dans-un-produit.md#fam-6), [desktop](ia-dans-un-produit.md#fam-7) | navigateur (Playwright…), doc (Context7, Ref…), données (Ansvar), sécurité (Burp…) |
| **Sub-agents** (séparer idéation / vérification) | [Agents & IDE → orchestrateurs](produire-du-code.md#fam-1b) & [Revue de code](produire-du-code.md#fam-7) | Liza, Ruflo (disciplinés) ; CodeRabbit, Greptile (vérif) |
| **State / Memory** (mémoire persistante sur disque) | [Connaissance du code](produire-du-code.md#fam-2) | Cavemem, GraphMind, Serena |

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
