# Instructions projet — base de connaissances IA

## INTERDIT : consigner de l'historique dans le contenu des fichiers

Les commentaires, docstrings et corps de fichiers (code **comme** fiches) documentent
**ce que la chose EST et FAIT**, au présent intemporel — jamais l'histoire de sa fabrication.

Sont **proscrits** dans le contenu d'un fichier :
- la narration du problème qu'un changement vient de corriger
  (« le maillon manquant », « ce qui manquait jusqu'ici », « désormais », « à présent ») ;
- la justification d'un choix passé ou la comparaison avant/après
  (« contrairement à avant », « non régressé », « maintenant on indexe aussi… », « nouvel axe ») ;
- toute trace du parcours de développement.

Écrire comme si le code/la fiche avait toujours été ainsi.

**Conserver un historique de décisions ou de choix est une décision de l'utilisateur**, pas une
initiative. Quand c'est voulu, ça va dans un fichier **prévu pour ça** — `log.md` (journal
append-only) ou un ADR dédié — **jamais** dans les commentaires/docstrings du code ni dans les fiches.
