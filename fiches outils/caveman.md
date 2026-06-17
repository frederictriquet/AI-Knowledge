---
outil: "Caveman"
type: "Skill (Claude Code + ~30 agents)"
url: https://github.com/juliusbrussee/caveman
modele_economique: "Open-source (MIT), gratuit (sponsorships acceptés)"
cout_llm: "Intégré — pas de LLM propre ; réduit la consommation de tokens de l'agent"
---

# Caveman

**En une phrase** — skill open-source qui force l'agent à répondre « comme un homme des cavernes » (fragments, zéro fioriture) pour couper ~65 % des tokens de sortie, sans perdre en exactitude technique. *« Why use many token when few token do trick. »* 🪨

## Type & intégration
**Skill** pour Claude Code (activation automatique chaque session via un fichier-flag), compatible avec ~30 autres agents (Codex, Gemini, Cursor, Windsurf, Cline, Copilot…). Déclenchable par `/caveman` ou « talk like caveman », arrêt par « normal mode ». Écrit principalement en JavaScript (+ Python, PowerShell, Shell).

## Modèle économique
**Open-source, licence MIT**, « free forever ». L'auteur (Julius Brussee) accepte des **sponsorships**, mais l'outil reste gratuit.

## Coût LLM
**Intégré** 🟢 — Caveman n'a **pas de LLM propre** et n'ajoute aucun coût : c'est une consigne de style qui s'applique au LLM de l'agent (Claude Code, etc.). Son effet est l'inverse d'un coût : il **réduit** les tokens de sortie (~65 %), et compresse aussi les fichiers mémoire (~46 % en moyenne) → économies directes sur la facture de l'agent.

Bonus contre-intuitif cité : un article de mars 2026 indique que contraindre les gros modèles à des réponses brèves aurait *amélioré* l'exactitude de 26 points sur certains benchmarks → la concision peut aider le raisonnement.

## À quoi ça sert
Diminuer le coût et la latence d'un agent en supprimant le verbiage de ses réponses, tout en gardant **code et chemins préservés byte-for-byte**. Plusieurs niveaux de compression : **lite, full, ultra, wenyan**. Fonctions annexes : génération de messages de commit, compression de revues de PR, statistiques d'usage de tokens.

## Notes / à creuser
- Même famille « réduction de tokens » que [[codegraph]] / [[polaris]] / [[graphify]], mais par un angle différent : ici on compresse la **sortie** du modèle (style), pas l'**entrée**/le contexte.
- Écosystème du même auteur : [[cavekit]] (plugin Claude Code, développement spec-driven), [[cavemem]] (mémoire persistante cross-agent, compressée, locale). L'encodage « caveman » est le fil rouge des trois.
- Niveau « wenyan » = compression façon chinois classique, très agressive.

## Source
- Dépôt : https://github.com/juliusbrussee/caveman
- Releases : https://github.com/JuliusBrussee/caveman/releases

*(vérifié le 2026-06-15 — README GitHub + recherche web)*
