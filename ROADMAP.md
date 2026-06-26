# Roadmap

Document de pilotage (non publié sur le site).
Statuts : ✅ fait · 🔜 prêt à lancer · 🧊 différé (à déclencher sur besoin réel).

## Buts du corpus

1. **Base de connaissances pour les collègues** — onboarding des nouveaux, approfondissement, découverte de sujets. Accès attendu par **plusieurs axes** : par **sujet**, par **niveau** de connaissance, par **type de contenu** (fiche, lien, vidéo…). Partage en **« tip of the day » / « knowledge nugget »** (consommable sans lire une fiche entière).
2. **Parcours de formation** — parcours différenciés par besoin/niveau (**SCORM**), **évaluation** (quiz, QCM). Suppose des connaissances **structurées pour la formation** et **validées par des experts**.

## Fait

- ✅ **Réorganisation** : corpus sous `wiki/` (séparé infra/travail) ; site Quartz → `wiki/` ; `.obsidian` adapté.
- ✅ **Récupération exacte des sources** : `curl | pandoc` (plus de résumé par petit modèle).
- ✅ **Dé-jargonisation des noms** : fichiers nommés par **contenu** (plus de `Q1/Q2/Q3`), familles par nom, **MOC → `themes/`**.
- ✅ **Navigation par altitude** : L1 fiche/recherche → **L2 `themes/`** (page par thème) → **L3 pages-sujet par objectif** → L4 carte `Accueil`.
- ✅ **Unification forte** : une **page par sujet** (`wiki/guides/`) réunissant **concepts + outils** ; outils tagués en frontmatter (`objectifs/famille/eco_icones/cout_icones/resume`), tables générées par `build_index.py` ; prose des familles dans `tools/familles.json`. Ancien recensement par domaine dissous. (Revu par agent : 0 perte.)
- ✅ **Outillage** : garde-fou Node ≥22 (`.nvmrc` + check build-site) ; garde-fous d'ingest (« 4 portes », « raffiner sans réécrire »).

## Chantiers (alignés sur les buts)

- 🔜 **Internationalisation (FR + EN)** — *important*. Traduire documents **+ noms de fichiers + liens** (aujourd'hui en français). ⚠️ Les slugs/liens FR actuels sont un coût ; choisir d'abord une **stratégie** (sous-arbres `fr/`+`en/` ; ou **identifiants stables ≠ libellés traduits** + génération bilingue) **avant** de grossir le corpus. Conditionne si on continue à créer des slugs FR.
- 🔜 **Axe « type de contenu »** — aujourd'hui : fiches concept + fiches outils seulement. Ajouter **lien** / **vidéo** (type de contenu + accès dédié).
- 🔜 **Accès par niveau** — page/vue générée « par niveau » (🔴/🟡/🟢), au-delà des requêtes Dataview d'`Accueil`.
- 🔜 **Nuggets / tip-of-the-day** — outiller le partage (rotation, export) au-delà de `kb_post.py` (preview aléatoire).
- 🔜 **Validation experte** — métadonnée de validation (qui / quand / statut) sur les fiches, prérequis des parcours de formation.
- 🧊 **Parcours de formation / SCORM** — séquençage, prérequis, export SCORM (gros chantier, dépend de la validation experte).
- 🧊 **Quiz / QCM** — génération et évaluation des connaissances par sujet.
- 🔜 **Nouveaux objectifs (pages-sujet)** — mécanisme en place : ajouter à `OBJECTIFS`, taguer fiches **et** outils, créer le fichier-sujet. Candidats : `securite`, `prompting-avance`, et remplir `pratiques-non-codeurs`.
- 🧊 **`tools/kb_fetch.py` mutualisé** — factoriser `curl | pandoc` **si** pages JS/SPA ou 403. Inline pour l'instant.
- 🧊 **`/kb:query` — élargir/préciser** : suggérer « plus large / plus précis » dans les réponses.
