---
description: Analyse critique d'un article (sans rien écrire), avec lien au corpus.
argument-hint: <url>
---
Analyse l'article suivant : $ARGUMENTS

> **Schéma** (carte du corpus, familles d'outils) : `process/SCHEMA.md` §2 & §4.

Objectif : une **analyse**, pas un simple résumé — et **rien n'est écrit** par défaut.

1. Récupère le **contenu exact** de la page — **jamais** via `WebFetch` (qui ne renvoie qu'un résumé produit par un petit modèle, source d'omissions et d'hallucinations). Télécharge la page brute et lis-la **toi-même** :
   ```bash
   curl -sL -A "Mozilla/5.0" "$ARGUMENTS" | pandoc -f html -t gfm-raw_html
   ```
   Lis intégralement la sortie : c'est le texte réel de l'auteur, avec ses chiffres, noms et citations exacts. Si `curl`/`pandoc` échoue (paywall, JS, 403), **signale-le explicitement** et n'analyse pas à l'aveugle — ne te rabats jamais sur un résumé de petit modèle.
2. Restitue fidèlement : thèse centrale, problème, **concepts/termes forgés** (avec leurs noms), cadres/taxonomies/étapes, recommandations, outils cités, citations marquantes.
3. **Évaluation critique** : ce qui est solide vs à nuancer ; les **angles morts** (en particulier le **coût** en tokens, préoccupation transverse du projet).
4. **Lien au corpus** : quelles fiches `wiki/fiches/` existantes ça recoupe ou complète, et quels outils/familles du recensement ça touche.
5. **Propose** (sans l'exécuter) : la/les fiche(s) concept à créer via `/kb:ingest`, et/ou des outils à ajouter via `/kb:tool`. Attends mon feu vert.
