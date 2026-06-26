# Process d'enrichissement de la base de connaissances

Process **robuste et reproductible** pour ajouter de la connaissance au corpus à
partir d'une URL, d'un article ou d'un site web — avec **détection de doublons**
et **garantie de qualité**. Versionné (il vit avec le projet) ; la slash-command
Claude Code `/kb:ingest` exécute ce process.

## Principe

Pipeline en 7 étapes, gardé par des contrôles. **Aucune fiche n'est écrite avant
l'étape 6** (validation humaine). Tout est réversible jusque-là.

```
URL / article / site
  ├─[1] INGEST ........ récupérer + extraire le texte propre
  ├─[2] EXTRACT ....... découper en concepts candidats + mapper aux thèmes
  ├─[3] DEDUP ......... embeddings top-K → jugement de recouvrement
  │         └─ verdict par concept : NOUVEAU / FUSION / DOUBLON
  ├─[4] DRAFT ......... rédiger la fiche au format (ou préparer un patch de fusion)
  ├─[5] QUALITY GATE .. structure + sources + densité
  ├─[6] REVIEW ........ rapport + approbation explicite de l'utilisateur
  └─[7] COMMIT ........ écrire la fiche + régénérer les index
```

Le partage des rôles est **hybride** : les étapes déterministes (dédup, lint,
vérif sources, index) sont des scripts Python ; les étapes de jugement (extraction,
rédaction, appréciation du recouvrement et de la densité) sont portées par le LLM.

## Pré-requis (une fois)

```bash
python3 -m venv tools/.venv
tools/.venv/bin/pip install -r tools/requirements.txt
tools/.venv/bin/python tools/kb_embed.py        # construit l'index d'embeddings
```

Tous les `kb_*.py` se lancent avec `tools/.venv/bin/python` depuis le dossier
`tools/` (imports frères) ou via le chemin du module. Le cache d'embeddings
(`tools/.cache/`) et le venv (`tools/.venv/`) sont gitignorés.

---

## Étape 1 — INGEST

Récupérer le **contenu exact** de la source — **jamais** via `WebFetch` (qui ne
renvoie qu'un résumé produit par un petit modèle : omissions, chiffres et citations
hallucinés). Télécharger la page brute et la lire **directement** :

```bash
curl -sL -A "Mozilla/5.0" "<url>" | pandoc -f html -t gfm-raw_html
```

Si `curl`/`pandoc` échoue (paywall, JS, 403), **le signaler explicitement** et ne
pas ingérer à l'aveugle — ne jamais se rabattre sur un résumé de petit modèle.
Extraire ensuite le **texte utile** (sans menus, pubs, navigation).

- Conserver le **markdown brut** de la source dans `sources/<hub>/` (nouveau
  sous-dossier nommé d'après l'auteur/le site), comme pour les sources existantes.
- Noter l'**URL canonique** et le **titre** de la page : ils deviendront
  `source_url` et `source_titre`.

## Étape 2 — EXTRACT

Une source riche couvre souvent **plusieurs concepts**. Découper en concepts
candidats **atomiques** (un concept = une fiche potentielle). Pour chacun :

- formuler le concept en 1-2 phrases denses (ce texte servira à la dédup) ;
- proposer un **thème** parmi les 14 de la taxonomie (cf. `tools/kb_common.py`) ;
- proposer un **niveau** : 🔴 substance · 🟡 tradeoff · 🟢 survol ;
- repérer une éventuelle **source primaire** (papier arXiv fondateur).

Écarter d'emblée le hors-périmètre (le corpus traite agents IA & prompt engineering).

## Étape 3 — DEDUP

Pour **chaque** concept candidat, lancer la détection sémantique :

```bash
tools/.venv/bin/python tools/kb_dedup.py --json "texte dense du concept"
```

Sortie : `verdict` (pré-filtre) + les `candidats` (top-K fiches proches, scores).
Seuils (calibrés pour le modèle, cf. en-tête de `kb_dedup.py`) :

| Score du meilleur candidat | Pré-verdict | Action |
|---|---|---|
| ≥ 0.85 | DOUBLON | Lire la fiche candidate. Probable doublon → écarter ou **fusionner**. |
| 0.75 – 0.85 | RECOUVREMENT | **Lire** les fiches candidates. Décider : complément (fusion) ou angle vraiment neuf (nouvelle fiche). |
| < 0.75 | NOUVEAU | Probable inédit. Vérifier quand même le top-1 d'un œil. |

> **Le score n'est qu'un pré-filtre.** Le verdict final est un **jugement** :
> ouvrir les fiches candidates (`wiki/fiches/<slug>.md`) et juger le recouvrement réel.
> Verdict par concept : `NOUVEAU` · `FUSION dans <slug>` · `DOUBLON (écarté)`.

## Étape 4 — DRAFT

Pour chaque concept `NOUVEAU`, rédiger une fiche respectant **strictement** le
format du corpus (cf. n'importe quelle fiche, ex. `wiki/fiches/react.md`) :

```yaml
---
titre: "Titre humain court"
theme: <un des 14 thèmes>
niveau: 🔴 | 🟡 | 🟢
source_url: https://…                      # OBLIGATOIRE
source_titre: "Titre de la page source"    # recommandé
source_primaire: "Auteur, Titre (arXiv:XXXX.XXXXX)"   # si papier fondateur
---

# Titre

**En une phrase** — l'accroche, autosuffisante (sert de post).

## En détail
Explication dense de ce que dit la source. Public tech senior.

## Exemple
UN cas concret et marquant tiré de la source (scénario déroulé, code, payload,
chiffres, citation) — rend la fiche auto-suffisante. 4-6 lignes, pas de paraphrase
de la substance ni de redite d'un chiffre déjà cité au-dessus.

## Tradeoff / insight pour un senior
Le point non trivial : quand l'utiliser, limites, piège.

## Source primaire
Le papier fondateur, si existe.

## Voir aussi
- [Fiche connexe](slug-existant.md)
```

- Slug du fichier : `kebab-case` du concept, unique. Un concept = un fichier.
- Densité élevée, pas de remplissage. Pas d'images ni de code (sauf cité).
- Les liens « Voir aussi » doivent pointer vers des **fiches existantes** (les
  candidats de l'étape 3 sont d'excellents liens).

Pour un concept `FUSION`, préparer un **patch** de la fiche cible (ajout d'un
paragraphe ou d'une nuance), pas une nouvelle fiche.

## Étape 5 — QUALITY GATE

Trois contrôles, à passer sur chaque draft avant de le proposer.

**a. Conformité de structure** (déterministe) :
```bash
tools/.venv/bin/python tools/kb_lint.py wiki/fiches/<nouveau-slug>.md
```
Corriger toute erreur ❌ (frontmatter, thème hors taxonomie, niveau, accroche
manquante, wikilink cassé). Les ⚠️ sont à examiner, non bloquants.

**b. Vérification factuelle des sources** (déterministe, réseau) :
```bash
tools/.venv/bin/python tools/kb_check_sources.py wiki/fiches/<nouveau-slug>.md
```
`source_url` doit répondre (HTTP < 400). Si un arXiv est cité, son titre réel doit
être cohérent avec la fiche. **Ne jamais inventer un identifiant arXiv** : s'il
n'est pas vérifiable, retirer le champ `source_primaire`.

**c. Densité & non-redondance** (jugement LLM) :
- la fiche apporte-t-elle une info non triviale **absente** des candidats dédup ?
- n'est-elle pas une paraphrase d'une fiche existante ?
- le niveau d'écriture senior est-il tenu (pas de généralités creuses) ?

## Étape 6 — REVIEW (validation humaine obligatoire)

Présenter à l'utilisateur un **rapport synthétique** :

- concepts extraits de la source ;
- pour chacun : verdict dédup (avec scores et fiches candidates), décision
  (nouveau / fusion / écarté) ;
- les drafts complets ;
- résultats des trois gates (lint ✅/❌, sources ✅/❌, note de densité).

**Attendre l'approbation explicite.** Rien n'est écrit ni committé sans accord.

## Étape 7 — COMMIT

Après accord :

1. Écrire les fiches validées dans `wiki/fiches/` (et appliquer les patchs de fusion).
2. Régénérer les index et l'index d'embeddings :
   ```bash
   python3 tools/build_index.py
   tools/.venv/bin/python tools/kb_embed.py     # incrémental : n'encode que le nouveau
   ```
3. Commit **uniquement si l'utilisateur le demande** (convention du projet).
   Message en anglais, conventional commits : `feat: add <concept> fiche`.

---

## Garanties offertes

- **Doublons** : tout concept est comparé sémantiquement à l'intégralité du corpus
  (embeddings) puis jugé fiche-à-fiche. Détecte aussi les doublons reformulés.
- **Qualité** : structure validée mécaniquement, sources vérifiées factuellement
  (URL + arXiv réel), densité jugée, et **dernier mot à l'humain**.
- **Reproductibilité** : les parties critiques sont des scripts déterministes,
  versionnés, recalibrables.

## Maintenance

- Changer de modèle d'embeddings → ajuster `MODELE` dans `kb_embed.py` puis
  **recalibrer** les seuils de `kb_dedup.py` (relancer l'analyse de distribution
  des plus proches voisins) et `kb_embed.py --rebuild`.
- Les seuils de dédup actuels sont calibrés pour
  `paraphrase-multilingual-MiniLM-L12-v2` (médiane du plus proche voisin ≈ 0.70).
