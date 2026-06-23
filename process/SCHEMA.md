# SCHÉMA du corpus — couche 3 (single source of truth)

> **Rôle** : ce fichier est le **schéma** du wiki, au sens du pattern *[LLM Wiki](../fiches/llm-wiki-karpathy.md)* de Karpathy (couche 3 : « le schéma qui dicte structure et workflows »). Il dit **ce que sont les choses et où vivent les règles**. Toutes les commandes `/kb:*` s'y réfèrent.
>
> **Principe anti-drift** : pour les valeurs ayant déjà une **source exécutable/canonique**, ce schéma **ne les recopie pas** — il y **renvoie**. Si une règle évolue, elle évolue **à sa source**, pas ici en double.

---

## 1. Le modèle en 3 couches (Karpathy, appliqué ici)

1. **Sources brutes** (immuables) → `sources/<hub>/` : markdown archivé des articles/pages ingérés.
2. **Le wiki** (possédé par le LLM, valeur cumulative) → deux sous-systèmes :
   - **Concepts** : `fiches/` (théorie : patterns, archi, méthodes…).
   - **Outils** : le **recensement** (`fiches outils/` + tableaux `Q1/Q2/Q3` + hub `outils IA.md`).
3. **Le schéma** (ce fichier) + l'**outillage** (`tools/`) + le **journal** (`log.md`).

Insight directeur : l'effort est **déplacé au write-time** (ingest/maj), pas au read-time. Le LLM fait le **bookkeeping** (la paperasse : trouver/mettre à jour les pages + renvois) ; l'humain garde la **curation** (quoi garder, arbitrages, validation).

---

## 2. Carte des fichiers

| Chemin | Contenu | Édité par | Canonique pour |
|--------|---------|-----------|----------------|
| `fiches/*.md` | Fiches **concept** | LLM (via `/kb:ingest`) | la théorie |
| `fiches outils/*.md` | Fiches **outil** | LLM (via `/kb:tool`) | le détail produit |
| `fiches outils/_TEMPLATE.md` | Gabarit de fiche outil | humain | **format des fiches outils** |
| `outils IA.md` | Hub du recensement + **légende des icônes** | humain/LLM | **la légende éco/coût LLM** |
| `Q1 - produire du code.md` · `Q2 - IA dans un produit.md` · `Q3 - IA dans les autres métiers.md` | Tableaux d'outils par **famille**, une par question | LLM | **les familles** (numérotées par fichier) |
| `outils candidats.md` | Backlog d'outils à arbitrer (cases `- [ ]`) | humain coche, LLM ajoute | — |
| `log.md` | Journal **append-only** (fichier réservé OKF) | LLM (via `/kb:log`) | l'historique orienté connaissance |
| `index.md`, `INDEX-THEMATIQUE.md`, `RAPPORT-CORPUS.md` | **Générés** par `tools/build_index.py` (`index.md` = point d'entrée réservé OKF) | ❌ ne pas éditer à la main | dérivés du frontmatter |
| `process/ENRICHISSEMENT.md` | **Pipeline ingest** détaillé (7 étapes) + setup venv | humain | **le workflow d'ingest** |
| `process/SCHEMA.md` | **Ce fichier** | humain | structure, conventions, carte |
| `tools/*.py` (+ `tools/.venv`, gitignoré) | Outillage déterministe | humain | dédup/lint/index/embeddings |

⚠️ Ne pas confondre **`fiches/`** (concepts) et **`fiches outils/`** (outils) : deux sous-systèmes distincts.

---

## 3. Schéma d'une fiche **concept** (`fiches/`)

Le **gate de structure** est exécuté par `tools/kb_lint.py` (= source de vérité **machine**). Une fiche est conforme si :

**Frontmatter** (YAML) :
- `titre` — obligatoire.
- `type` — obligatoire (**conformité OKF**, cf. §9) ; valeur maison = `"Concept"` (distingue les fiches concept des fiches outils, qui portent déjà leur type produit).
- `theme` — obligatoire, **∈ la taxonomie des 14 thèmes** (voir §3.1).
- `niveau` — obligatoire, **∈ {🔴, 🟡, 🟢}** (voir §3.2).
- `source_url` — obligatoire, commençant par `http(s)://`.
- `source_titre` — recommandé (libellé lisible de la source).

**Corps** :
- Accroche **`**En une phrase**`** — *obligatoire* (erreur sinon), autosuffisante et dense.
- Une section **`## Tradeoff …`** ou **`## Insight …`** — attendue (avertissement sinon) : le jugement, pas le résumé.
- Une section **`## Voir aussi`** — attendue, avec des **wikilinks** `[libellé](slug.md)` vers des fiches **existantes** (un lien cassé = erreur).

> Style maison observé (non imposé par le lint, mais cohérent) : sections `## L'idée` / `## Ce que dit la source`, `## Pourquoi c'est utile`, `## Points clés`. Garder dense, une idée **atomique** par fiche.

### 3.1 Les 14 thèmes
**Source de vérité exécutable = `tools/kb_common.py` (`THEMES`)** ; `kb_lint` refuse tout thème hors liste. Pour mémoire (slugs) :
`fondamentaux-agents` · `raisonnement-planification` · `prompting` · `outils-function-calling` · `rag-contexte` · `memoire` · `multi-agents` · `protocoles-interop` · `frameworks-outillage` · `evaluation` · `benchmarks` · `securite` · `efficacite-cout` · `gouvernance-alignement-ops`.
*(Modifier la taxonomie = éditer `kb_common.py` ET `build_index.py`, pas seulement ici.)*

### 3.2 Échelle de niveau
`🔴` substance / cœur · `🟡` tradeoff / intermédiaire · `🟢` survol / introductif. *(sémantique fixée à l'EXTRACT d'`ENRICHISSEMENT.md` ; le lint ne vérifie que l'appartenance à l'ensemble.)*

---

## 4. Schéma du **recensement d'outils**

- **Périmètre & rangement** : chaque outil va dans **une question** (Q1 produire du code · Q2 IA dans un produit · Q3 autres métiers) et **une famille** (les familles sont **définies et numérotées par fichier-question** ; carte dans `outils IA.md`). Créer une famille si aucune ne convient (et le signaler).
- **Fiche outil** : `fiches outils/<slug-kebab>.md`, au format de **`fiches outils/_TEMPLATE.md`** (frontmatter `outil/type/url/modele_economique/cout_llm` + sections Type & intégration / Modèle économique / Coût LLM / À quoi ça sert / Notes / Source). Terminer la Source par **`*(vérifié le AAAA-MM-JJ)*`**.
- **Ligne de tableau** : `**[Nom](url)** · [📄](fiches%20outils/slug.md) | Type | <éco> | <coût LLM> | résumé une ligne`.
- **Icônes (éco + coût LLM)** : **source unique = la légende de [`outils IA.md`](../outils%20IA.md)**. Ne pas la redéfinir ailleurs.
- **Règle d'or des coûts** (cf. [[verifier-couts-outils-ia]]) : **vérifier à la source, ne jamais supposer** licence/prix/coût LLM ; **dater** les chiffres relevés. Piège récurrent : un outil qui **pilote tes agents existants** (sans prendre de clé) = **🟢**, ≠ **🔑 BYOK** (clé fournie à l'outil) ≠ **💸** (tokens revendus) ; doute non tranchable → **❓**.

---

## 5. Les opérations (commandes `/kb:*`)

| Commande | Rôle | Écrit ? |
|----------|------|---------|
| `/kb:analyze <url>` | Analyse critique d'un article + lien au corpus | ❌ propose seulement |
| `/kb:ingest <src>` | Pipeline d'ingestion concept (→ `fiches/`), cf. `ENRICHISSEMENT.md` | ✍️ **après validation humaine (étape 6)** |
| `/kb:tool <nom/url>` | Ajoute un outil au recensement (vérif source → fiche → ligne → log) | ✍️ oui (invocation explicite) |
| `/kb:query <question>` | Répond depuis le corpus, avec citations ; signale les manques | ❌ propose de reverser |
| `/kb:lint` | Santé du corpus (structure/sources/fraîcheur/doublons) + audit | ✍️ index régénéré ; corrections sur accord |
| `/kb:refresh [outil\|--stale\|--all]` | Re-vérifie à la source + propage la maj/dépréciation partout (fiche + tableaux + log) | ✍️ **mixte** : auto si mécanique, ton OK si factuel |
| `/kb:log [TYPE] <msg>` | Entrée horodatée dans `log.md` | ✍️ append-only |

**Invariants communs** (à respecter par toutes les commandes) :
1. **L'humain garde le dernier mot** : pas d'écriture sur les opérations à fort enjeu sans validation (ingest, corrections de lint non triviales). `analyze`/`query` **proposent** sans écrire.
2. **Vérifier à la source, ne pas supposer** (surtout coûts/licences) ; **WebFetch/WebSearch depuis le thread principal** — ⚠️ les sous-agents n'ont **pas** d'accès réseau ici.
3. **Tracer** dans `log.md` les opérations qui modifient le corpus (types ci-dessous).
4. Renvoyer à **ce schéma** plutôt que redéfinir format/thèmes/légende.

---

## 6. Outillage déterministe (`tools/`) & venv

`tools/*.py` font la part **calculable** (dédup par embeddings, lint de structure, index, fraîcheur). **Prérequis** : un venv `tools/.venv` (gitignoré) — setup dans `ENRICHISSEMENT.md` (`python3 -m venv tools/.venv` + `pip install -r tools/requirements.txt` + `kb_embed.py`). Convention : `kb_*.py` se lancent avec `tools/.venv/bin/python` ; `build_index.py` tourne avec `python3` (sans dépendance lourde).

- `kb_lint.py` — structure des fiches concept (§3) · `kb_check_sources.py` — sources/arXiv · `kb_dedup.py` — similarité sémantique (pré-filtre) · `kb_embed.py` — index d'embeddings · `kb_staleness.py` — fraîcheur des fiches outils (> 90 j / non datées) · `kb_reminder.py` — rappel one-liner « N fiches à rafraîchir » (vide si rien) · `build_index.py` — (re)génère `INDEX-THEMATIQUE.md` + `RAPPORT-CORPUS.md`.

**Rappel de maintenance (sans cron)** : un hook **`SessionStart`** (`.claude/settings.json`) lance `kb_reminder.py` à l'ouverture du projet et surface, le cas échéant, « ⚠️ N fiche(s) outil à rafraîchir → `/kb:refresh` ». Renfort passif : `/kb:query` et `/kb:tool` glissent le même rappel en clôture s'il y a lieu. Le refresh lui-même reste **déclenché par l'humain** (`/kb:refresh`).

---

## 7. Journal (`log.md`)

**Append-only**, plus récent en bas. Format `AAAA-MM-JJ  TYPE  message`. Types (source : en-tête de `log.md`) : `INGEST` · `TOOL` · `STRUCT` · `UPDATE` · `DEPRECATE` · `LINT` · `NOTE`.

---

## 8. Principes Karpathy (rappel directeur)
- Wiki **maintenu** (valeur cumulative) ≠ RAG **recalculé** à chaque requête.
- Goulot d'un KB = le **bookkeeping** → c'est ce que le LLM automate ; à l'humain le **curatorial**.
- Partage **hybride** : déterministe pour ce qui se calcule, LLM pour ce qui se juge.

---

## 9. Conformité OKF (Open Knowledge Format)

Le corpus est **conforme [OKF](https://okf.md/spec/)** — un plancher d'interopérabilité « minimum de cérémonie » qui permet à un agent/outil tiers de naviguer le bundle sans connaître nos conventions. **Ce schéma reste la source de vérité** : c'est un **sur-ensemble strict** d'OKF (OKF tolère champs en plus et validation locale plus sévère). Adopter OKF n'a donc rien retiré.

Ce qui assure la conformité :
- **`type` non-vide** dans le frontmatter de **toute** fiche (seul champ obligatoire OKF) : `"Concept"` pour `fiches/`, le type produit pour `fiches outils/`. Vérifié par `kb_lint.py`.
- **Liens markdown relatifs** `[libellé](slug.md)` partout (les wikilinks Obsidian `[[slug]]` ont été convertis ; ne pas en réintroduire).
- **Fichiers réservés** : `index.md` (point d'entrée, généré par `build_index.py`) et `log.md` (journal append-only daté).

> Volontairement **non adopté** (cérémonie sans gain ici) : renommage des clés FR→EN, chemins absolus `/path/concept.md` (casseraient Obsidian). Nos `theme`/`niveau`/icônes éco-coût restent le contrat riche, par-dessus le plancher OKF.
