---
titre: "One-shot prompting"
theme: prompting
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/one-shot-prompting
source_titre: "Qu’est-ce que l’apprentissage one-shot ?"---

# One-shot prompting

> Fiche du glossaire prompting · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [../md/09-one-shot-prompting.md](../sources/ibm-guide-prompt-engineering/md/09-one-shot-prompting.md)

**En une phrase** — fournir au modèle un seul exemple bien conçu pour qu'il généralise une tâche, à mi-chemin entre zero-shot et few-shot.

## Ce que dit le corpus
Le one-shot repose sur un unique prompt-exemple pour obtenir le résultat souhaité, utile quand collecter de grands volumes de données d'entraînement n'est pas pratique. IBM mentionne les LLM GPT-3/GPT-4 et Granite. Notablement, l'article penche surtout vers la vision : il détaille des mécanismes orientés image/vidéo — prompting visuel contextuel (masques de segmentation, cadres de sélection, points clés), projection adaptative des caractéristiques (variations temporelles en reconnaissance d'actions vidéo), zoom sur l'attention (attention croisée support/requête) — aux côtés du prompting par connaissances, plus généraliste. Avantages : efficacité (moins de données), rapidité de déploiement, flexibilité. Limites : risque de biais hérités des données pré-entraînées, variabilité de précision sur tâches complexes. Cas d'usage : chatbots, création de contenu, recommandations personnalisées, reconnaissance d'actions vidéo.

## Tradeoff / insight pour un senior
Le glissement vers la vision est révélateur : « one-shot » côté NLP signifie un exemple dans le prompt, mais l'article mélange ce sens avec le one-shot learning du computer vision (segmentation, détection), deux lignées de recherche distinctes. Pour un usage LLM textuel, ne retenir que le mécanisme « un exemple dans le contexte » et ignorer les sections vision spécialisées.

## Source primaire
Non citée nommément par IBM — notes de bas de page numérotées non résolues dans le texte lu (hors-corpus pour le détail).

## Voir aussi
- [zero-shot-prompting](zero-shot-prompting.md)
- [few-shot-prompting](few-shot-prompting.md)
