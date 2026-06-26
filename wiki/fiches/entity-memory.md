---
titre: "Mémoire à base d'entités / graphe"
type: "Concept"
theme: memoire
niveau: 🟡
source_url: https://arxiv.org/abs/2501.13956
source_titre: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"
---

# Mémoire à base d'entités / graphe

**En une phrase** — structurer la mémoire long-terme comme un **graphe d'entités et de relations** (qui / quoi / lien) plutôt qu'un simple store vectoriel.

## L'idée
Au lieu de stocker des chunks de texte indexés par embedding, on extrait des **entités** (personnes, lieux, objets) et les **relations** qui les lient, formant un graphe de connaissances mis à jour au fil des interactions. Récupérer un souvenir revient à parcourir ce graphe, ce qui préserve la cohérence sur le temps long : les faits contradictoires sont réconciliés au niveau de l'entité plutôt que dupliqués dans des passages flottants.

## Tradeoff / quand l'utiliser
Pertinent pour des assistants persistants devant suivre **des faits stables et reliés** sur de nombreuses sessions. Coût : l'extraction et la maintenance du graphe ajoutent des appels et de la complexité ; pour de la récupération purement sémantique sur des documents, un store vectoriel reste plus simple.

## Source primaire
Pas de papier canonique unique. Concept implémenté dans LangChain (entity memory), Zep/Graphiti et A-MEM (2024). Cité tel quel, sans identifiant arXiv inventé.

## Voir aussi
- [memgpt](memgpt.md)
- [memoire-court-long-terme](memoire-court-long-terme.md)
