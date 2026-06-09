---
titre: "Graph of Thoughts (GoT)"
theme: raisonnement-planification
niveau: 🔴
source_url: https://arxiv.org/abs/2308.09687---

# Graph of Thoughts (GoT)

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. Glossaire · Pertinence 🔴 substance

**En une phrase** — on modélise le raisonnement comme un graphe arbitraire de pensées où l'on peut non seulement ramifier, mais aussi **fusionner** plusieurs pensées, boucler et raffiner, là où Tree-of-Thoughts se limite à un arbre.

## L'idée
GoT représente chaque pensée intermédiaire comme un nœud d'un graphe ; les arêtes encodent des transformations. Au-delà de la simple expansion arborescente, il autorise des opérations impossibles dans un arbre : **agrégation** (fusionner plusieurs solutions partielles en une meilleure), **raffinement** (boucle d'amélioration sur un même nœud) et génération. Un contrôleur orchestre ces opérations et note les nœuds. Cette structure capture mieux les problèmes où des sous-solutions doivent être recombinées (tri, fusion de documents, agrégation).

## Tradeoff / quand l'utiliser
Plus **expressif** que ToT : il modélise des dépendances que l'arbre ne peut pas (fusion de branches). En contrepartie, il est plus coûteux et complexe à orchestrer — il faut définir le graphe, les opérations de fusion et la fonction de notation. À réserver aux tâches où la recombinaison de solutions partielles apporte un gain mesurable ; pour de l'exploration purement divergente, ToT suffit et coûte moins.

## Source primaire
Besta et al., 2023, *Graph of Thoughts: Solving Elaborate Problems with Large Language Models*, arXiv:2308.09687. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [tree-of-thoughts](tree-of-thoughts.md) (corpus)
- [lats](lats.md) (corpus)
