# Computer-use & agents GUI

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. [Glossaire](../../GLOSSAIRE-PATTERNS.md) · Pertinence 🔴 substance

**En une phrase** — piloter un navigateur ou un OS comme un humain, via **captures d'écran** en entrée et **actions** (clic, frappe, défilement) en sortie.

## L'idée
Plutôt que des API ou des outils dédiés, l'agent GUI perçoit l'écran (pixels, parfois arbre d'accessibilité) et agit aux **coordonnées** : il clique, tape, fait défiler. Cela ouvre toute interface logicielle, même sans API. Anthropic Computer Use industrialise cette boucle perception-action ; SeeAct (Zheng et al.) utilise GPT-4V pour des agents web. Des benchmarks comme WebArena (sites réalistes) et OSWorld mesurent la réussite de tâches multi-étapes dans des environnements réels.

## Tradeoff / quand l'utiliser
Utile quand **aucune API n'existe** ou pour automatiser des parcours visuels. Contrepartie : fragile (UI qui change, ancrage de coordonnées imprécis), lent, et **risqué** (actions destructrices, captures de données sensibles) ; à sandboxer et superviser.

## Source primaire
Anthropic, 2024, *Computer Use* (documentation produit) ; Zhou et al., 2023, *WebArena: A Realistic Web Environment for Building Autonomous Agents*, arXiv:2307.13854 *(arXiv vérifié — HTTP 200 + titre)* ; Zheng et al., 2024, *SeeAct* (GPT-4V web agent) *(arXiv vérifié — HTTP 200 + titre)*.

## Voir aussi
- [codeact](codeact.md) (hors-corpus sœur)
- [tool-calling](../tool-calling.md) (corpus)
