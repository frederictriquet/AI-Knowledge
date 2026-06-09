# Self-Consistency

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. [Glossaire](../../GLOSSAIRE-PATTERNS.md) · Pertinence 🟡 tradeoff

**En une phrase** — au lieu d'une seule chaîne de raisonnement, on en échantillonne plusieurs avec une température non nulle, puis on vote à la majorité sur la réponse finale.

## L'idée
Le Chain-of-Thought greedy produit une unique trajectoire, fragile : une erreur précoce contamine tout. Self-Consistency exploite le fait qu'un problème admet plusieurs chemins de raisonnement valides convergeant vers la **même** réponse. On génère N chaînes diverses (sampling), on ignore le raisonnement intermédiaire et on retient la réponse la plus fréquente. La diversité des chemins agit comme un correcteur d'erreurs statistique.

## Tradeoff / quand l'utiliser
Robustesse quasi gratuite côté ingénierie (aucun fine-tuning, aucun outil externe), mais coût d'inférence multiplié par N (souvent 5 à 40 échantillons). À privilégier sur les tâches arithmétiques, symboliques ou de raisonnement à réponse vérifiable et discrète, où le vote majoritaire a un sens. À éviter pour les sorties ouvertes/longues, où « voter » n'a pas de définition claire et où le coût ne se justifie pas.

## Source primaire
Wang et al., 2022, *Self-Consistency Improves Chain of Thought Reasoning in Language Models*, arXiv:2203.11171. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [chain-of-thought](../chain-of-thought.md) (corpus)
- [tree-of-thoughts](../tree-of-thoughts.md) (corpus)
- (base prompt engineering) [Self-Consistency](../../../ibm-guide-prompt-engineering/concepts/self-consistency.md)
