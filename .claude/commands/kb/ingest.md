---
description: Intègre une source (URL/article) dans le corpus de concepts (fiches/) via le pipeline d'enrichissement.
argument-hint: <url ou chemin de source>
---
Intègre la source suivante dans la base de connaissances **concepts** (`fiches/`) : $ARGUMENTS

Commence par **lire `process/ENRICHISSEMENT.md`** et suis **strictement** son pipeline en 7 étapes :

1. **INGEST** — récupère le texte propre (WebFetch) ; archive le markdown brut dans `sources/<hub>/` ; note l'URL canonique + le titre (→ `source_url`, `source_titre`).
2. **EXTRACT** — découpe en concepts **atomiques** ; pour chacun : un thème (parmi les 14), un niveau (🔴 substance / 🟡 tradeoff / 🟢 survol), une source primaire éventuelle. Écarte le hors-périmètre (le corpus = agents IA & prompt engineering).
3. **DEDUP** — pour **chaque** concept : `tools/.venv/bin/python tools/kb_dedup.py --json "texte dense du concept"`. Le score n'est qu'un pré-filtre → ouvre les fiches candidates et juge fiche-à-fiche. Verdict : NOUVEAU / FUSION dans <slug> / DOUBLON (écarté).
4. **DRAFT** — rédige chaque fiche NOUVELLE au format du corpus (frontmatter complet avec `source_url` obligatoire, **En une phrase** autosuffisante, dense, « Voir aussi » vers des **fiches existantes**). Pour une FUSION, prépare un patch de la fiche cible, pas une nouvelle fiche.
5. **QUALITY GATE** — `tools/.venv/bin/python tools/kb_lint.py fiches/<slug>.md` puis `tools/.venv/bin/python tools/kb_check_sources.py fiches/<slug>.md`. **Ne jamais inventer d'identifiant arXiv** : non vérifiable → retirer `source_primaire`. Juge la densité/non-redondance.
6. **REVIEW** — présente un rapport (concepts, verdicts dédup avec scores + fiches candidates, drafts complets, résultat des 3 gates) et **attends mon approbation explicite**. N'écris rien avant.
7. **COMMIT** — après accord : écris les fiches (et patchs de fusion), puis `python3 tools/build_index.py` et `tools/.venv/bin/python tools/kb_embed.py`. Ajoute une entrée `INGEST` dans `log.md`. Ne commit (git) que si je le demande.

Tout est réversible jusqu'à l'étape 6 ; le dernier mot est à l'humain.
