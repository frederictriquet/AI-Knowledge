# 🗺️ Accueil — carte de la base

Note d'entrée pour la **consultation dans Obsidian**. (Sur GitHub, l'entrée reste [README.md](README.md).)

Cette base se **consulte**, elle ne se lit pas de bout en bout. Trois modes :

- **Naviguer** — vue graphe, backlinks, recherche, et les index ci-dessous.
- **Interroger** — poser une question via un agent (commande `/kb:query`) : il lit les bonnes fiches et cite ses sources.
- **Produire** — piocher une accroche « **En une phrase** » + son lien source pour un post.

> Les liens internes sont en **markdown** (`[texte](note.md)`) **par choix** : cliquables sur GitHub *et* exploités par le graphe/backlinks d'Obsidian (les wikilinks `[[ ]]`, eux, ne s'affichent pas sur GitHub). Voir l'entrée de décision dans [log.md](log.md).

## Points d'entrée

- 📚 **Concepts** — [INDEX-THEMATIQUE.md](INDEX-THEMATIQUE.md) (fiches par thème) · état du corpus : [RAPPORT-CORPUS.md](RAPPORT-CORPUS.md)
- 🧰 **Outils** — [outils IA.md](outils%20IA.md) (index + 3 questions) → [Q1 — produire du code](Q1%20-%20produire%20du%20code.md) · [Q2 — IA dans un produit](Q2%20-%20IA%20dans%20un%20produit.md) · [Q3 — autres métiers](Q3%20-%20IA%20dans%20les%20autres%20métiers.md) · à arbitrer : [outils candidats.md](outils%20candidats.md)
- 🪵 **Journal** — [log.md](log.md)
- ⚙️ **Process & commandes** — [README.md](README.md) (slash-commands `/kb:*`)

## Requêtes Dataview

> Nécessite le plugin communautaire **Dataview**. Sans lui, ces blocs s'affichent comme du code (sans effet).

**Concepts 🔴 (substance), par thème :**
```dataview
TABLE niveau, theme FROM "fiches" WHERE niveau = "🔴" SORT theme ASC
```

**Toutes les fiches d'un thème (adapter la valeur) :**
```dataview
LIST FROM "fiches" WHERE theme = "securite"
```

**Outils — type, modèle éco, coût LLM :**
```dataview
TABLE type, modele_economique AS "éco", cout_llm AS "coût LLM" FROM "fiches outils" SORT outil ASC
```

**Outils en BYOK (clé API à fournir) :**
```dataview
LIST FROM "fiches outils" WHERE contains(cout_llm, "BYOK")
```

## Réglages Obsidian conseillés (optionnels)

- **Exclure les dossiers non-fiches** du graphe/recherche : `Réglages → Fichiers et liens → Filtres exclus` → ajouter `tools/`, `sources/`, `.claude/`.
- **Format des liens** : garder « chemin relatif » (pas « wikilink ») → compatibilité GitHub conservée.
- `fiches outils/_TEMPLATE.md` peut être déclaré comme modèle (plugin **Templates**) pour créer une nouvelle fiche outil.
