# Corpus IA — agents & prompt engineering

Base de connaissances condensée et **sourcée** sur l'IA agentique et le prompt engineering, bâtie à partir des hubs **IBM Think** puis enrichie de sources externes de référence (Lilian Weng, Anthropic, Hamel Husain, Eugene Yan, Simon Willison, The Prompt Report, DeepSeek, OWASP/NIST/MITRE…).

## À quoi ça sert

1. **Monter en compétences** — une fiche par concept, dense, avec le lien vers la source primaire pour approfondir.
2. **Produire des posts courts** (messagerie interne) — chaque fiche tient en une accroche (« En une phrase ») + un lien « pour approfondir ».
3. **Affirmer une expertise** (LinkedIn) — même matière, format public.

## Par où commencer

- **[Accueil.md](Accueil.md)** — note d'accueil pour la consultation dans **Obsidian** (modes d'usage, points d'entrée, requêtes Dataview). Sur GitHub, c'est ce README qui sert d'entrée.
- **[INDEX-THEMATIQUE.md](INDEX-THEMATIQUE.md)** — le point d'entrée : les 158 fiches rangées par **thème** (tous corpus confondus), avec niveau, provenance et lien source. ⚙️ généré.
- **[RAPPORT-CORPUS.md](RAPPORT-CORPUS.md)** — état du corpus : couverture par thème, fiches sans source, doublons. ⚙️ généré.
- **[log.md](log.md)** — journal append-only des opérations sur le corpus (ingest / tool / struct / lint…), inspiré du pattern *LLM Wiki*.

## Structure

```
fiches/      158 fiches à plat — la base de connaissances. Structure portée par le frontmatter.
sources/     matériaux bruts qui ont produit les fiches :
             ├ ibm-guide-agents-ia/, ibm-guide-prompt-engineering/  (pages md + html des hubs IBM)
             ├ lilian-weng/, hamel-husain/, …                       (md + README par source externe)
             └ SOURCES-PRIMAIRES.md, SOURCES-COMPLEMENTAIRES.md, METHODOLOGIE-IBM-THINK.md
tools/       build_index.py (génère les 2 index) · classification-themes.md (table de travail)
```

## Anatomie d'une fiche

Chaque fiche `fiches/<slug>.md` commence par un **frontmatter** qui porte toute la structure :

```yaml
---
titre: ReAct
theme: raisonnement-planification      # une des 14 catégories (voir INDEX-THEMATIQUE)
niveau: 🟢                             # 🔴 substance · 🟡 tradeoff · 🟢 survol
source_url: https://www.ibm.com/fr-fr/think/topics/react-agent
source_titre: "Qu'est-ce qu'un agent ReAct ? — IBM Think"
source_primaire: "Yao et al. (arXiv:2210.03629)"   # optionnel : papier d'origine
---
```

Suit le corps : **En une phrase** (l'accroche pour un post) · ce que dit la source · **Exemple** (un cas concret sourcé, qui rend la fiche auto-suffisante) · tradeoff/insight · source primaire · voir aussi.

## Ajouter ou mettre à jour une fiche

### Process outillé (recommandé) — à partir d'une URL / d'un article

Le process **[process/ENRICHISSEMENT.md](process/ENRICHISSEMENT.md)** intègre une
source en garantissant **détection de doublons** (embeddings sémantiques) et
**qualité** (structure, sources vérifiées, validation humaine). Piloté par le skill
Claude Code `/enrich <url>`. Pré-requis une fois :

```bash
python3 -m venv tools/.venv && tools/.venv/bin/pip install -r tools/requirements.txt
tools/.venv/bin/python tools/kb_embed.py
```

Outils déterministes réutilisables seuls :

```bash
tools/.venv/bin/python tools/kb_dedup.py "texte d'un concept"   # doublons sémantiques
tools/.venv/bin/python tools/kb_lint.py --all                   # conformité de structure
tools/.venv/bin/python tools/kb_check_sources.py fiches/x.md    # URL + arXiv réels
tools/.venv/bin/python tools/kb_post.py                         # preview de post (fiche au hasard)
python3 tools/kb_staleness.py                                   # fiches outils à re-vérifier (date de vérif > 90 j)
```

### À la main

1. Créer/éditer `fiches/<slug>.md` avec le frontmatter ci-dessus (le `source_url` est **obligatoire**).
2. Régénérer les index :

```bash
python3 tools/build_index.py
```

Le rapport signale toute fiche sans `source_url`, les thèmes peu couverts et les doublons de titre.

## Commandes (slash-commands)

Le process est outillé par des slash-commands Claude Code (`.claude/commands/kb/`, namespace `kb`) :

| Commande | Rôle |
|----------|------|
| `/kb:ingest <url>` | Intègre une source en fiche(s) concept — pipeline `process/ENRICHISSEMENT.md` (dédup, gates, validation humaine) |
| `/kb:tool <nom/url>` | Ajoute un outil au recensement : vérif à la source → fiche `fiches outils/` → ligne de tableau Q1/Q2 → log |
| `/kb:analyze <url>` | Analyse critique d'un article (sans rien écrire), avec lien au corpus + propositions |
| `/kb:query <question>` | Répond depuis le wiki, avec citations des fiches |
| `/kb:lint` | Contrôles de santé (structure, sources, fraîcheur, doublons) + audit de contradictions optionnel |
| `/kb:refresh [outil\|--stale\|--all]` | Re-vérifie un/les outil(s) à la source et propage la maj partout (fiche + tableaux + log) ; déprécie si besoin. Niveau « mixte » (auto si mécanique, ton OK si factuel). Lancé à la demande |
| `/kb:log [TYPE] <msg>` | Ajoute une entrée au journal `log.md` (append-only) |

Le **schéma** du corpus (structure, conventions, carte des fichiers) est dans [`process/SCHEMA.md`](process/SCHEMA.md) — couche 3 du pattern, référencée par toutes les commandes.

Ces commandes correspondent aux opérations du pattern *[LLM Wiki](fiches/llm-wiki-karpathy.md)* : **ingest** (`/kb:ingest`, `/kb:tool`), **query** (`/kb:query`), **lint/maintenance** (`/kb:lint`, `/kb:refresh`), + journal (`/kb:log`).

> ⚠️ `.claude/` est gitignoré → ces commandes sont **locales** à ta machine. Pour les versionner avec le projet, remplace `.claude/` par `.claude/*` + `!.claude/commands/` dans `.gitignore`.

## Les 14 thèmes

Fondamentaux des agents · Raisonnement & planification · Prompting · Outils & function-calling · RAG & contexte · Mémoire · Multi-agents · Protocoles & interopérabilité · Frameworks & outillage · Évaluation · Benchmarks · Sécurité · Efficacité & coût · Gouvernance, alignement & ops.
