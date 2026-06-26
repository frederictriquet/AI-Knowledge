---
outil: "RTK (Rust Token Killer)"
titre: "RTK (Rust Token Killer)"
themes: [efficacite-cout]
type: "CLI (proxy)"
url: https://www.rtk-ai.app/
modele_economique: "Open-source (Apache 2.0), gratuit ; RTK Cloud (équipes) à venir, 15 $/dev/mois"
cout_llm: "Aucune inférence LLM — compresse la sortie des commandes avant le contexte (économise sur la facture)"
---

# RTK (Rust Token Killer)

**En une phrase** — proxy CLI en Rust qui intercepte et compresse la sortie des commandes terminal *avant* qu'elle n'entre dans le contexte du LLM, pour éliminer le bruit et économiser 60–90 % des tokens. *« Your AI agent is drowning in CLI noise. Fix it. »*

## Type & intégration
**Binaire Rust unique, zéro dépendance, zéro config** — un proxy transparent qui s'intercale entre le shell et l'assistant IA. Couvre 100+ commandes courantes (git, cargo, npm, ls, cat, find…). Intégration **Claude Code** via `rtk init --global` : installe un **hook PreToolUse** qui réécrit automatiquement les commandes Bash en équivalents `rtk` (transparent, 0 token d'overhead). Compatible aussi Cursor, Aider, Copilot…

Quatre stratégies : **filtrage, groupement, troncature, déduplication** — élague le répétitif (warnings, formatage, padding) en préservant l'essentiel (erreurs, échecs, diffs). Overhead < 10 ms/commande.

## Modèle économique
- **RTK (core)** : **open-source Apache 2.0**, totalement gratuit, sans limite d'usage, sans clé API, sans télémétrie, sans compte.
- **RTK Cloud** (liste d'attente) : analytics d'équipe (suivi centralisé des tokens) à partir de **15 $/dev/mois**.

## Coût LLM
**Aucune inférence LLM propre** 🟢. RTK ne fait pas tourner de modèle : il **compresse des sorties de commandes existantes**. Effet = économie directe sur la facture LLM de l'agent (tu gardes tes propres clés sur tes outils IA, BYOK). Résultats mesurés : ~89 % de bruit retiré sur 2 900+ commandes réelles (cargo test 91,8 %, git status 80,8 %, find 78,3 %) ; une session Claude Code de 30 min passe de ~118 000 à ~23 900 tokens (~80 %).

## À quoi ça sert
Allonger les sessions d'agent et réduire les coûts en supprimant le bruit des sorties CLI qui sature inutilement la fenêtre de contexte. Particulièrement pertinent pour qui paie les LLM à l'usage.

## Notes / à creuser
- **Famille « optimisation tokens »** : analogue le plus direct de [Tokenade](tokenade.md) (qui trim aussi les sorties de commandes), mais RTK est **open-source/gratuit** vs Tokenade propriétaire/freemium, et purement focalisé sur la **sortie des commandes shell**. Voir aussi [Caveman](caveman.md) (sortie du modèle) et [Ponytail](ponytail.md) (périmètre du code).
- 🛠️ **Utilisé dans l'environnement de l'utilisateur** : configuré globalement via un hook Claude Code (cf. `RTK.md` global) — toutes les commandes shell sont réécrites en `rtk <cmd>` de façon transparente.
- Métacommandes : `rtk gain` (analytics d'économies), `rtk discover`, `rtk proxy <cmd>` (exécution brute sans filtrage).

## Source
- Site officiel : https://www.rtk-ai.app/
- Dépôt : https://github.com/rtk-ai/rtk · Docs : https://mintlify.com/explore/rtk-ai/rtk

*(vérifié le 2026-06-15 — landing officielle + GitHub + recherche web)*
