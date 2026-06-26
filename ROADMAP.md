# Roadmap

Suites de travail. Document de pilotage (non publié sur le site).
Statuts : ✅ fait · 🔜 prêt à lancer · 🧊 différé (à déclencher sur besoin réel).

## Fait

- ✅ **Réorganisation** : tout le corpus sous `wiki/` (séparé de l'infra/travail). Scripts, site (Quartz → `wiki/`), `.obsidian` adaptés.
- ✅ **Récupération exacte des sources** : `curl | pandoc` au lieu du résumé `WebFetch` (`/kb:analyze` + pipeline d'ingest).
- ✅ **Navigation par altitude** — modèle L1 fiche/recherche → L2 MOC → L3 guide par objectif → L4 carte racine (cf. `process/SCHEMA.md` §3.3) :
  - ✅ **L3** — facet `objectifs` + génération hybride (prose curée + bloc `<!-- AUTO -->`). Guides livrés : **generer-code**, **fiabilite**, **couts**, **mise-en-prod**.
  - ✅ **L4** — `wiki/Accueil.md` refondu en carte racine orientée questions (« je veux faire… / j'explore… / je cherche un outil / question précise »).
  - ✅ **L2** — MOC enrichies (intro de thème, regroupement par niveau, accroche par fiche).
- ✅ **Garde-fou Node** : `.nvmrc` (`22`) + vérification de version en tête de `scripts/build-site.sh`.
- ✅ **Garde-fous d'ingest** (idées OKF) dans `ENRICHISSEMENT.md` : « 4 portes » anti-bruit (création vs fusion) + règle « raffiner, ne pas réécrire ».

## Suites possibles

- 🔜 **Nouveaux objectifs L3** (le mécanisme est en place : ajouter à `OBJECTIFS`, taguer, créer le guide). Candidats : `autres-metiers` (recoupe Q3), `securite`, `prompting-avance`…
- 🧊 **L1 — élargir/préciser** : suggérer « plus large / plus précis » dans les réponses de `/kb:query`.
- 🧊 **`tools/kb_fetch.py` mutualisé** : factoriser la ligne `curl | pandoc` (user-agent, retries, fallback) **si** on rencontre des pages JS/SPA ou 403. Inline pour l'instant (choix assumé).
