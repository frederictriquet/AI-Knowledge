# SCHÉMA du corpus — couche 3 (single source of truth)

> **Rôle** : ce fichier est le **schéma** du wiki, au sens du pattern *[LLM Wiki](../wiki/fiches/llm-wiki-karpathy.md)* de Karpathy (couche 3 : « le schéma qui dicte structure et workflows »). Il dit **ce que sont les choses et où vivent les règles**. Toutes les commandes `/kb:*` s'y réfèrent.
>
> **Principe anti-drift** : pour les valeurs ayant déjà une **source exécutable/canonique**, ce schéma **ne les recopie pas** — il y **renvoie**. Si une règle évolue, elle évolue **à sa source**, pas ici en double.

---

## 1. Le modèle en 3 couches (Karpathy, appliqué ici)

1. **Sources brutes** (immuables) → `sources/<hub>/` : markdown archivé des articles/pages ingérés.
2. **Le wiki** (possédé par le LLM, valeur cumulative) → deux sous-systèmes :
   - **Concepts** : `wiki/fiches/` (théorie : patterns, archi, méthodes…).
   - **Outils** : le **recensement** (`wiki/fiches outils/` + 3 tableaux par domaine + hub `wiki/outils IA.md`).
3. **Le schéma** (ce fichier) + l'**outillage** (`tools/`) + le **journal** (`wiki/log.md`).

Insight directeur : l'effort est **déplacé au write-time** (ingest/maj), pas au read-time. Le LLM fait le **bookkeeping** (la paperasse : trouver/mettre à jour les pages + renvois) ; l'humain garde la **curation** (quoi garder, arbitrages, validation).

---

## 2. Carte des fichiers

| Chemin | Contenu | Édité par | Canonique pour |
|--------|---------|-----------|----------------|
| `wiki/fiches/*.md` | Fiches **concept** | LLM (via `/kb:ingest`) | la théorie |
| `wiki/fiches outils/*.md` | Fiches **outil** | LLM (via `/kb:tool`) | le détail produit |
| `wiki/fiches outils/_TEMPLATE.md` | Gabarit de fiche outil | humain | **format des fiches outils** |
| `wiki/outils IA.md` | Hub du recensement + **légende des icônes** | humain/LLM | **la légende éco/coût LLM** |
| `wiki/produire-du-code.md` · `wiki/ia-dans-un-produit.md` · `wiki/ia-pour-ceux-qui-ne-codent-pas.md` | Tableaux d'outils par **famille**, un par domaine | LLM | **les familles** (numérotées par fichier) |
| `outils candidats.md` | Backlog d'outils à arbitrer (cases `- [ ]`) | humain coche, LLM ajoute | — |
| `wiki/log.md` | Journal **append-only** (fichier réservé OKF) | LLM (via `/kb:log`) | l'historique orienté connaissance |
| `wiki/index.md`, `wiki/INDEX-THEMATIQUE.md`, `wiki/RAPPORT-CORPUS.md`, `wiki/MOC/*.md` | **Générés** par `tools/build_index.py` (`wiki/index.md` = point d'entrée réservé OKF ; `wiki/MOC/<theme>.md` = hub par thème reliant concepts + outils) | ❌ ne pas éditer à la main | dérivés du frontmatter |
| `wiki/guides/*.md` | **Guides par objectif (L3)** : parcours transverses orientés tâche (cf. §3.3) | **hybride** : prose curée par l'humain + bloc `<!-- AUTO -->` régénéré par `build_index.py` | **les parcours par objectif** |
| `process/ENRICHISSEMENT.md` | **Pipeline ingest** détaillé (7 étapes) + setup venv | humain | **le workflow d'ingest** |
| `process/SCHEMA.md` | **Ce fichier** | humain | structure, conventions, carte |
| `tools/*.py` (+ `tools/.venv`, gitignoré) | Outillage déterministe | humain | dédup/lint/index/embeddings |

⚠️ Ne pas confondre **`wiki/fiches/`** (concepts) et **`wiki/fiches outils/`** (outils) : deux sous-systèmes distincts.

---

## 3. Schéma d'une fiche **concept** (`wiki/fiches/`)

Le **gate de structure** est exécuté par `tools/kb_lint.py` (= source de vérité **machine**). Une fiche est conforme si :

**Frontmatter** (YAML) :
- `titre` — obligatoire.
- `type` — obligatoire (**conformité OKF**, cf. §9) ; valeur maison = `"Concept"` (distingue les fiches concept des fiches outils, qui portent déjà leur type produit).
- `theme` — obligatoire, **∈ la taxonomie des 14 thèmes** (voir §3.1).
- `niveau` — obligatoire, **∈ {🔴, 🟡, 🟢}** (voir §3.2).
- `source_url` — obligatoire, commençant par `http(s)://`.
- `source_titre` — recommandé (libellé lisible de la source).
- `objectifs` — *optionnel*, **liste** de slugs ∈ vocabulaire `OBJECTIFS` (`kb_common.py`) ; axe L3 orthogonal au thème (cf. §3.3). Rattache la fiche à un/des guide(s). Validé par `kb_lint`.

**Corps** :
- Accroche **`**En une phrase**`** — *obligatoire* (erreur sinon), autosuffisante et dense.
- Une **section de jugement** — attendue (avertissement sinon) : le jugement, pas le résumé. Libellés acceptés par le lint : `## Tradeoff…`, `## Insight…`, `## Pourquoi c'est utile`, `## Points clés`, `## À retenir`, `## Quand l'utiliser`, `## Synthèse…`.
- Une section **`## Voir aussi`** — attendue, avec des **wikilinks** `[libellé](slug.md)` vers des fiches **existantes** (un lien cassé = erreur).

> Style maison observé (non imposé par le lint, mais cohérent) : sections `## L'idée` / `## Ce que dit la source`, `## Pourquoi c'est utile`, `## Points clés`. Garder dense, une idée **atomique** par fiche.

### 3.1 Les 14 thèmes
**Source de vérité exécutable = `tools/kb_common.py` (`THEMES`)** ; `kb_lint` refuse tout thème hors liste. Pour mémoire (slugs) :
`fondamentaux-agents` · `raisonnement-planification` · `prompting` · `outils-function-calling` · `rag-contexte` · `memoire` · `multi-agents` · `protocoles-interop` · `frameworks-outillage` · `evaluation` · `benchmarks` · `securite` · `efficacite-cout` · `gouvernance-alignement-ops`.
*(Modifier la taxonomie = éditer `kb_common.py` ET `build_index.py`, pas seulement ici.)*

### 3.2 Échelle de niveau
`🔴` substance / cœur · `🟡` tradeoff / intermédiaire · `🟢` survol / introductif. *(sémantique fixée à l'EXTRACT d'`ENRICHISSEMENT.md` ; le lint ne vérifie que l'appartenance à l'ensemble.)*

### 3.3 Navigation par altitude & guides par objectif (L3)
Le corpus se parcourt à **quatre altitudes**, du précis au large :
- **L1 — fiche / recherche** : le concept atomique ; pour le précis arbitraire, `kb_search` / `/kb:query`.
- **L2 — MOC thématique** (`wiki/MOC/<theme>.md`, générée) : tout un **domaine** (les 14 thèmes).
- **L3 — guide par objectif** (`wiki/guides/<slug>.md`) : un **but transverse** orienté tâche (« générer du code avec l'IA »…), qui croise plusieurs thèmes.
- **L4 — carte racine** (`wiki/Accueil.md`) : les grandes portes d'entrée.

L'**axe objectif** (frontmatter `objectifs`, multi-valué) est au concept ce que la **famille Q** est à l'outil : un second axe **orthogonal au thème** (thème = *à propos de quoi* ; objectif = *pour quel but*). Vocabulaire contrôlé = `OBJECTIFS` dans `kb_common.py`.

**Mécanique d'un guide (hybride)** : le fichier porte `type: guide` + `objectif: <slug>` dans son frontmatter ; sa **prose est curée** (intro + parcours de lecture) ; un bloc délimité par `<!-- AUTO:objectif=<slug> -->` … `<!-- /AUTO -->` est **régénéré** par `build_index.py` (liste des fiches taguées, groupées par thème, avec accroche). On évite ainsi décharge plate **et** désync. *(Ajouter un objectif = l'ajouter à `OBJECTIFS`, taguer les fiches, créer le fichier guide avec les marqueurs.)*

---

## 4. Schéma du **recensement d'outils**

- **Périmètre & rangement** : chaque outil va dans **un domaine** (produire du code · embarquer l'IA dans un produit · pour ceux qui ne codent pas) et **une famille** (les familles sont **définies et numérotées par fichier-domaine** ; carte dans `wiki/outils IA.md`). Créer une famille si aucune ne convient (et le signaler).
- **Axe topique (`themes`)** : en plus de la famille Q, chaque fiche outil porte `themes: [...]` — une **liste de thèmes pris dans la taxonomie des 14** (cf. §3.1). Axe **orthogonal** à la famille (Q = *pour quel job* ; thème = *à propos de quoi*) et **partagé avec les concepts** (qui portent `theme`, singulier) : c'est l'axe commun qui relie les deux corpus pour la recherche (`kb_search`), les pages MOC et le graphe. `build_index.py` signale dans `wiki/RAPPORT-CORPUS.md` tout outil sans `themes` ou avec un thème hors taxonomie.
- **Pages-hub MOC** : `wiki/MOC/<theme>.md`, **générées** par `build_index.py` (une par thème), listent les **concepts ET les outils** du thème ; `wiki/INDEX-THEMATIQUE.md` en est le sommaire. ❌ ne pas éditer à la main.
- **Fiche outil** : `wiki/fiches outils/<slug-kebab>.md`, au format de **`wiki/fiches outils/_TEMPLATE.md`** (frontmatter `outil/titre/themes/type/url/modele_economique/cout_llm` + sections Type & intégration / Modèle économique / Coût LLM / À quoi ça sert / Notes / Source). Terminer la Source par **`*(vérifié le AAAA-MM-JJ)*`**.
- **Ligne de tableau** : `**[Nom](url)** · [📄](wiki/fiches%20outils/slug.md) | Type | <éco> | <coût LLM> | résumé une ligne`.
- **Icônes (éco + coût LLM)** : **source unique = la légende de [`wiki/outils IA.md`](../wiki/outils%20IA.md)**. Ne pas la redéfinir ailleurs.
- **Règle d'or des coûts** (cf. [[verifier-couts-outils-ia]]) : **vérifier à la source, ne jamais supposer** licence/prix/coût LLM ; **dater** les chiffres relevés. Piège récurrent : un outil qui **pilote tes agents existants** (sans prendre de clé) = **🟢**, ≠ **🔑 BYOK** (clé fournie à l'outil) ≠ **💸** (tokens revendus) ; doute non tranchable → **❓**.

---

## 5. Les opérations (commandes `/kb:*`)

| Commande | Rôle | Écrit ? |
|----------|------|---------|
| `/kb:analyze <url>` | Analyse critique d'un article + lien au corpus | ❌ propose seulement |
| `/kb:ingest <src>` | Pipeline d'ingestion concept (→ `wiki/fiches/`), cf. `ENRICHISSEMENT.md` | ✍️ **après validation humaine (étape 6)** |
| `/kb:tool <nom/url>` | Ajoute un outil au recensement (vérif source → fiche → ligne → log) | ✍️ oui (invocation explicite) |
| `/kb:query <question>` | Répond depuis le corpus, avec citations ; signale les manques | ❌ propose de reverser |
| `/kb:lint` | Santé du corpus (structure/sources/fraîcheur/doublons) + audit | ✍️ index régénéré ; corrections sur accord |
| `/kb:refresh [outil\|--stale\|--all]` | Re-vérifie à la source + propage la maj/dépréciation partout (fiche + tableaux + log) | ✍️ **mixte** : auto si mécanique, ton OK si factuel |
| `/kb:log [TYPE] <msg>` | Entrée horodatée dans `wiki/log.md` | ✍️ append-only |

**Invariants communs** (à respecter par toutes les commandes) :
1. **L'humain garde le dernier mot** : pas d'écriture sur les opérations à fort enjeu sans validation (ingest, corrections de lint non triviales). `analyze`/`query` **proposent** sans écrire.
2. **Vérifier à la source, ne pas supposer** (surtout coûts/licences) ; **WebFetch/WebSearch depuis le thread principal** — ⚠️ les sous-agents n'ont **pas** d'accès réseau ici.
3. **Tracer** dans `wiki/log.md` les opérations qui modifient le corpus (types ci-dessous).
4. Renvoyer à **ce schéma** plutôt que redéfinir format/thèmes/légende.

---

## 6. Outillage déterministe (`tools/`) & venv

`tools/*.py` font la part **calculable** (dédup par embeddings, lint de structure, index, fraîcheur). **Prérequis** : un venv `tools/.venv` (gitignoré) — setup dans `ENRICHISSEMENT.md` (`python3 -m venv tools/.venv` + `pip install -r tools/requirements.txt` + `kb_embed.py`). Convention : `kb_*.py` se lancent avec `tools/.venv/bin/python` ; `build_index.py` tourne avec `python3` (sans dépendance lourde).

- `kb_lint.py` — structure des fiches concept (§3) · `kb_check_sources.py` — sources/arXiv · `kb_dedup.py` — similarité sémantique (pré-filtre, concepts) · `kb_embed.py` — index d'embeddings (concepts + outils) · `kb_search.py` — recherche hybride locale (lexical + sémantique, 0 LLM) sur les deux corpus · `kb_staleness.py` — fraîcheur des fiches outils (> 90 j / non datées) · `kb_reminder.py` — rappel one-liner « N fiches à rafraîchir » (vide si rien) · `build_index.py` — (re)génère `wiki/INDEX-THEMATIQUE.md`, `wiki/RAPPORT-CORPUS.md`, `wiki/index.md` et `wiki/MOC/*.md`.

**Rappel de maintenance (sans cron)** : un hook **`SessionStart`** (`.claude/settings.json`) lance `kb_reminder.py` à l'ouverture du projet et surface, le cas échéant, « ⚠️ N fiche(s) outil à rafraîchir → `/kb:refresh` ». Renfort passif : `/kb:query` et `/kb:tool` glissent le même rappel en clôture s'il y a lieu. Le refresh lui-même reste **déclenché par l'humain** (`/kb:refresh`).

---

## 7. Journal (`wiki/log.md`)

**Append-only**, plus récent en bas. Format `AAAA-MM-JJ  TYPE  message`. Types (source : en-tête de `wiki/log.md`) : `INGEST` · `TOOL` · `STRUCT` · `UPDATE` · `DEPRECATE` · `LINT` · `NOTE`.

---

## 8. Principes Karpathy (rappel directeur)
- Wiki **maintenu** (valeur cumulative) ≠ RAG **recalculé** à chaque requête.
- Goulot d'un KB = le **bookkeeping** → c'est ce que le LLM automate ; à l'humain le **curatorial**.
- Partage **hybride** : déterministe pour ce qui se calcule, LLM pour ce qui se juge.

---

## 9. Conformité OKF (Open Knowledge Format)

Le corpus est **conforme [OKF](https://okf.md/spec/)** — un plancher d'interopérabilité « minimum de cérémonie » qui permet à un agent/outil tiers de naviguer le bundle sans connaître nos conventions. **Ce schéma reste la source de vérité** : c'est un **sur-ensemble strict** d'OKF (OKF tolère champs en plus et validation locale plus sévère). Adopter OKF n'a donc rien retiré.

Ce qui assure la conformité :
- **`type` non-vide** dans le frontmatter de **toute** fiche (seul champ obligatoire OKF) : `"Concept"` pour `wiki/fiches/`, le type produit pour `wiki/fiches outils/`. Vérifié par `kb_lint.py`.
- **Liens markdown relatifs** `[libellé](slug.md)` partout (les wikilinks Obsidian `[[slug]]` ont été convertis ; ne pas en réintroduire).
- **Fichiers réservés** : `wiki/index.md` (point d'entrée, généré par `build_index.py`) et `wiki/log.md` (journal append-only daté).

> Volontairement **non adopté** (cérémonie sans gain ici) : renommage des clés FR→EN, chemins absolus `/path/concept.md` (casseraient Obsidian). Nos `theme`/`niveau`/icônes éco-coût restent le contrat riche, par-dessus le plancher OKF.
