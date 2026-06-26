---
outil: "dupehound"
titre: "dupehound"
themes: [evaluation]
type: "CLI / Serveur MCP"
url: https://github.com/Rafaelpta/dupehound
modele_economique: "Open-source"
cout_llm: "Intégré"
---

# dupehound

**En une phrase** — détecteur de **code dupliqué** open-source (MIT, Rust) pensé pour les bases où l'IA écrit le plus gros du code : repère les fonctions dupliquées **même quand identifiants et littéraux sont renommés**, par empreinte de la *structure* (pas du texte), 100 % local et déterministe — **sans LLM ni clé**.

## Type & intégration
**CLI** + mode **serveur MCP**. Quatre usages :
- `scan` — rapporte les clusters de duplication + un **« slop score »** au niveau du repo.
- `history` — trace la duplication le long de l'historique git.
- `check` — **gate CI** qui échoue quand un changement duplique du code existant.
- `mcp` — tourne en **serveur MCP**, exposant des outils que l'agent de codage appelle **en cours d'édition** (« est-ce que ça existe déjà ? » → réutiliser au lieu de réécrire).

Sous le capot : parsing **tree-sitter** + algorithme de **winnowing** (fingerprinting). Implémenté en Rust.

## Modèle économique
**Open-source, gratuit**, licence **MIT**.

## Coût LLM
**🟢 Intégré.** dupehound **n'utilise aucun LLM** : « no network, API keys, or AI required », analyse statique déterministe, locale et hors-ligne. En mode MCP il tourne *dans/à côté* de l'agent (Claude Code…) sans clé propre → pas de coût LLM séparé.

## À quoi ça sert
Lutter contre la **duplication / le « slop »** générés par les agents de codage : leur faire **réutiliser** le code existant plutôt que le réécrire (via MCP, mid-edit), mesurer la dette de duplication (slop score, courbe historique) et **bloquer en CI** les PR qui re-dupliquent. Voisin par l'intention de [Ponytail](ponytail.md) (anti-over-engineering : moins de code) — mais ici par **mesure déterministe** de la duplication, pas par steering de prompt. À distinguer des reviewers IA de la famille [Revue de code par IA](../produire-du-code.md#fam-7), qui sont eux à base de LLM.

## Notes / à creuser
- **Jeune** : v0.1.2 (juin 2026), ~64★. Périmètre/robustesse à valider sur de gros repos multi-langages.
- Le « slop score » est une heuristique maison — utile comme **signal de tendance**, à ne pas absolutiser.
- Détection structurelle (renommages tolérés) ≠ détection sémantique : deux implémentations vraiment différentes d'une même intention ne seront pas vues comme doublons.

## Source
- Repo : https://github.com/Rafaelpta/dupehound — README (fonction, commandes `scan`/`history`/`check`/`mcp`, « no AI required »), licence MIT, v0.1.2. *(vérifié le 2026-06-23)*
