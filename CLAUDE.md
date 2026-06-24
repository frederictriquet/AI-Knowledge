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

## OBLIGATOIRE : fiches honnêtes au service de la décision

La base sert à **faire des choix**. Une fiche (outil **comme** concept) doit **aider à décider, pas vendre**. Dire la vérité sans embellir, **même si l'outil est populaire**. Pour toute fiche, par défaut :

- **énoncer les limites, les angles morts, et à qui / quand l'outil NE convient PAS** ;
- **pondérer le hype et les chiffres auto-déclarés** (stars, « production-ready », benchmarks/tests maison, « used by X ») : les **attribuer à leur source** et signaler s'ils ne sont **pas vérifiés indépendamment** ;
- **comparer aux alternatives** quand un peer plus simple, plus sobre ou plus sûr existe ;
- **ne jamais reprendre l'argumentaire de l'éditeur tel quel** ; vérifier les faits à la source (licence/prix/coût/maturité), cf. la règle de vérif des coûts (`process/SCHEMA.md` §4).

Le coût (en tokens et en argent) est une **préoccupation transverse** : le rendre explicite, y compris le coût propre de l'outil (pas seulement ce qu'il fait gagner).
