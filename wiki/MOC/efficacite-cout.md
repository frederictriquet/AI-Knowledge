---
type: index
titre: "MOC — Efficacité & coût"
theme: efficacite-cout
---

# ⚡ Efficacité & coût

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Réduire coût et latence (routing, caching, décodage)._

## Concepts (5)

### 🟡 Tradeoff / intermédiaire
- **[Décodage contraint / sortie structurée](../fiches/constrained-decoding.md)** — forcer la sortie à respecter une grammaire/schéma (JSON, regex) en masquant les tokens invalides au décodage ; garantit un format parsable (≠ « demander gentiment » du JSON).
- **[Mise en cache sémantique](../fiches/semantic-caching.md)** — cacher requêtes, contexte et résultats par similarité sémantique, utilisé comme mécanisme de mémoire de l'agent.
- **[Routage & cascades de modèles](../fiches/model-routing-cascades.md)** — router chaque requête vers le modèle le moins cher CAPABLE, ou enchaîner du petit au gros (cascade) avec un juge de confiance ; réduit fortement le coût à qualité quasi constante.
- **[Sorties structurées (instructor / Pydantic)](../fiches/sorties-structurees-instructor.md)** — Obtenir d'un LLM des données typées et validées (via des modèles Pydantic) plutôt que de parser du texte libre, avec validation et retries automatiques.
- **[Speculative decoding](../fiches/speculative-decoding.md)** — un petit modèle « brouillon » propose plusieurs tokens, le gros modèle les VÉRIFIE en un pass ; accélère l'inférence sans changer la distribution de sortie.

## Outils (12)

- **[Agent Booster](../fiches%20outils/agent-booster.md)** — _Serveur MCP / CLI_
- **[Cavekit](../fiches%20outils/cavekit.md)** — _Plugin (Claude Code) + skills_
- **[Caveman](../fiches%20outils/caveman.md)** — _Skill (Claude Code + ~30 agents)_
- **[ECC](../fiches%20outils/ecc.md)** — _Système de harness d'agent (skills/agents/hooks/rules) — multi-plateforme, OSS + GitHub App_
- **[Headroom](../fiches%20outils/headroom.md)** — _CLI / Proxy / Serveur MCP / Bibliothèque_
- **[LiteLLM](../fiches%20outils/litellm.md)** — _Bibliothèque Python (SDK) + Proxy/Gateway self-host (open-source) + Enterprise_
- **[OpenRouter](../fiches%20outils/openrouter.md)** — _Service web (gateway LLM hébergé)_
- **[Portkey](../fiches%20outils/portkey.md)** — _AI Gateway open-source (MIT) self-host + Service web (SaaS managé)_
- **[Ref (ref.tools)](../fiches%20outils/ref.md)** — _Serveur MCP (documentation technique à jour)_
- **[Requesty](../fiches%20outils/requesty.md)** — _Service web (gateway LLM hébergé)_
- **[RTK (Rust Token Killer)](../fiches%20outils/rtk.md)** — _CLI (proxy)_
- **[Tokenade](../fiches%20outils/tokenade.md)** — _CLI_
