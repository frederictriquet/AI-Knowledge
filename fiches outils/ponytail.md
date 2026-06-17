---
outil: "Ponytail"
type: "Skill / Plugin (multi-agents)"
url: https://github.com/DietrichGebert/ponytail
modele_economique: "Open-source (MIT), gratuit"
cout_llm: "Intégré — pas de LLM propre (BYOK / tourne dans l'agent) ; réduit le code généré donc le coût"
---

# Ponytail

**En une phrase** — skill qui fait penser l'agent IA « comme le dev senior le plus paresseux de la pièce » : le meilleur code est celui qu'on n'écrit jamais. 🐴

## Type & intégration
**Skill / plugin multi-plateforme** :
- **Skills** (avec commandes) pour les hôtes skill-capables : Claude Code, Codex, OpenCode, Gemini CLI, Pi.
- **Adaptateurs « instruction-only »** (ruleset always-on, sans commandes) pour Cursor, Windsurf, Cline, Copilot, Kiro, Antigravity.

Écrit en **JavaScript** (98,8 %), hooks de cycle de vie de plugin en Node.js. Niveaux d'intensité : **lite, full (défaut), ultra**. Inclut un skill `/ponytail-review` : revue de code ciblée anti-over-engineering (repère ce qu'il faut supprimer — stdlib réinventées, dépendances inutiles, abstractions spéculatives).

## Modèle économique
**Open-source, licence MIT**, gratuit ; pas de modèle commercial apparent.

## Coût LLM
**Intégré** 🟢 — pas de LLM propre : Ponytail est une consigne de comportement qui s'applique au modèle de l'agent (BYOK / clés de l'utilisateur). Effet sur le coût : il **réduit le code généré** (80–94 % de code en moins annoncé) → 47–77 % de coûts en moins et 3–6× plus rapide selon le dépôt. Économie par *moindre production*, pas par compression.

## À quoi ça sert
Lutter contre le **sur-engineering** des agents : questionner si la tâche doit exister (YAGNI), préférer la bibliothèque standard au code custom, réutiliser les dépendances existantes, « une ligne plutôt que cinquante ». Pour qui veut des diffs plus petits, plus simples et plus maintenables.

## Notes / à creuser
- **Famille « skills qui façonnent le comportement de l'agent »** avec [[caveman]] : Caveman compresse le *style de sortie*, Ponytail réduit le *périmètre du code*. Les deux baissent tokens et coûts, par des leviers différents. (Voir aussi le cluster contexte : [[codegraph]], [[polaris]], [[graphmind]], [[tokenade]].)
- Approche purement « prompt/règles » → zéro dépendance lourde, portable sur de nombreux agents.
- Chiffres de gain (80–94 % de code en moins) à prendre comme communication du projet, à vérifier sur ses propres cas.

## Source
- Dépôt : https://github.com/DietrichGebert/ponytail
- Skill : https://www.openagentskill.com/skills/dietrichgebert-ponytail

*(vérifié le 2026-06-15 — README GitHub + recherche web)*
