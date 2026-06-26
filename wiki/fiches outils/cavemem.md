---
outil: "Cavemem"
titre: "Cavemem"
themes: [memoire]
type: "Serveur MCP / CLI (+ hooks IDE)"
url: https://github.com/JuliusBrussee/cavemem
modele_economique: "Open-source (MIT), gratuit"
cout_llm: "🟢🔑 — aucun LLM génératif ; embeddings locaux par défaut (🟢, pas de clé) ; provider distant OpenAI optionnel = clé requise (🔑), Ollama local aussi possible"
objectifs: [generer-code]
famille: "Connaissance du code : graphes, recherche & mémoire"
eco_icones: "🔓"
cout_icones: "🟢🔑"
resume: "Mémoire persistante cross-agent (CLI + MCP + hooks IDE) ; événements de session compressés (~75 %), SQLite local, interrogeable via MCP. Aucun LLM génératif ; embeddings **locaux par défaut** (🟢), provider distant **OpenAI** optionnel = clé requise (🔑)"
---

# Cavemem

**En une phrase** — système de mémoire persistante cross-agent pour assistants de codage : capture les événements de session, les compresse, et permet aux agents d'interroger leur historique via MCP — local par défaut, sans réseau ni cloud.

## Type & intégration
**CLI + serveur MCP + hooks IDE** (installable globalement via npm). Des hooks se déclenchent aux frontières de session pour compresser les observations ; les agents interrogent ensuite leur propre historique via des outils MCP. Écrit en **TypeScript** (88,8 %) + JS/Shell. Même auteur que [Caveman](caveman.md) et [Cavekit](cavekit.md).

## Modèle économique
**Open-source, licence MIT**, gratuit ; projet communautaire.

## Coût LLM
**🟢🔑** — aucun **LLM génératif** : stockage et recherche via **SQLite FTS5 + index vectoriel**, avec **embeddings locaux par défaut** (`embedding.provider: local`) → **sans clé, sans réseau** (🟢, « No network. No cloud. »). Option (vérifiée dans le README) : provider d'embeddings **distant** — `ollama` (local) ou **`openai`** → ce dernier **exige une clé** (🔑, BYOK sur les embeddings). Ce n'est **pas le mode par défaut**.

Ordre de grandeur : coût LLM nul en mode standard ; la compression déterministe des événements (~75 %) réduit aussi les tokens quand l'agent recharge sa mémoire.

## À quoi ça sert
Donner aux agents une **mémoire durable et partagée entre sessions/outils** : ce qui a été fait, décidé, observé, retrouvé rapidement et de façon compacte — sans dépendre du cloud. Cible la confidentialité (local-first) et l'économie de tokens.

## Notes / à creuser
- Famille « réduction de tokens / contexte » avec [CodeGraph](codegraph.md), [Polaris (polarismcp.com)](polaris.md), [Graphify](graphify.md) : Cavemem apporte l'angle **mémoire persistante** (entre sessions), là où les autres indexent le code/les docs.
- Local-first strict → bon argument confidentialité, comme [Polaris (polarismcp.com)](polaris.md).
- Complément naturel de [Caveman](caveman.md)/[Cavekit](cavekit.md) dans l'écosystème cave\*.

## Source
- Dépôt : https://github.com/JuliusBrussee/cavemem

*(vérifié le 2026-06-15 — README GitHub)*
