# 🗺️ Accueil — carte de la base

Note d'entrée pour la **consultation dans Obsidian**. (Sur GitHub, l'entrée reste [README.md](README.md).)

Cette base se **consulte**, elle ne se lit pas de bout en bout. On y entre à **quatre altitudes**, du large au précis — choisis selon ton besoin.

## 🧭 « Je veux faire… » — guides par objectif (L3)

Parcours transverses aux thèmes, orientés tâche. Le meilleur point d'entrée quand on part d'un **but**.

- [Générer du code avec l'IA](guides/generer-du-code-avec-l-ia.md)
- [Fiabiliser & évaluer un système LLM](guides/fiabiliser-evaluer-un-systeme-llm.md)
- [Maîtriser le coût en tokens](guides/maitriser-le-cout-en-tokens.md)
- [Mettre de l'IA en production](guides/mettre-de-l-ia-en-production.md)

## 📚 « J'explore un sujet » — par thème (L2)

- [INDEX-THEMATIQUE.md](INDEX-THEMATIQUE.md) — les 14 thèmes, chacun ouvrant une page-hub (MOC) concepts + outils · état du corpus : [RAPPORT-CORPUS.md](RAPPORT-CORPUS.md)

## 🧰 « Je cherche un outil » — recensement

- [outils IA.md](outils%20IA.md) (index + légende) → [Q1 — produire du code](Q1%20-%20produire%20du%20code.md) · [Q2 — IA dans un produit](Q2%20-%20IA%20dans%20un%20produit.md) · [Q3 — autres métiers](Q3%20-%20IA%20dans%20les%20autres%20métiers.md) · à arbitrer : [outils candidats.md](outils%20candidats.md)

## ❓ « J'ai une question précise » (L1)

- Poser la question via l'agent — commande `/kb:query` : il lit les bonnes fiches et **cite ses sources**.
- Sinon : recherche, vue graphe, backlinks, ou piocher une accroche « **En une phrase** » + son lien source pour un post.

- 🪵 **Journal** — [log.md](log.md) · ⚙️ **Process & commandes** — [README.md](README.md) (slash-commands `/kb:*`)

> Les liens internes sont en **markdown** (`[texte](note.md)`) **par choix** : cliquables sur GitHub *et* exploités par le graphe/backlinks d'Obsidian (les wikilinks `[[ ]]`, eux, ne s'affichent pas sur GitHub). Voir l'entrée de décision dans [log.md](log.md).

## Requêtes Dataview

> Nécessite le plugin communautaire **Dataview**. Sans lui, ces blocs s'affichent comme du code (sans effet).

**Concepts 🔴 (substance), par thème :**
```dataview
TABLE niveau, theme FROM "wiki/fiches" WHERE niveau = "🔴" SORT theme ASC
```

**Toutes les fiches d'un thème (adapter la valeur) :**
```dataview
LIST FROM "wiki/fiches" WHERE theme = "securite"
```

**Outils — type, modèle éco, coût LLM :**
```dataview
TABLE type, modele_economique AS "éco", cout_llm AS "coût LLM" FROM "wiki/fiches outils" SORT outil ASC
```

**Outils en BYOK (clé API à fournir) :**
```dataview
LIST FROM "wiki/fiches outils" WHERE contains(cout_llm, "BYOK")
```

## Réglages Obsidian conseillés (optionnels)

- **Exclure les dossiers non-fiches** du graphe/recherche : `Réglages → Fichiers et liens → Filtres exclus` → ajouter `tools/`, `sources/`, `.claude/`.
- **Format des liens** : garder « chemin relatif » (pas « wikilink ») → compatibilité GitHub conservée.
- `fiches outils/_TEMPLATE.md` peut être déclaré comme modèle (plugin **Templates**) pour créer une nouvelle fiche outil.
