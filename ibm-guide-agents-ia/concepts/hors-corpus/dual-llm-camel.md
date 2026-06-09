# Dual-LLM pattern & CaMeL

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. [Glossaire](../../GLOSSAIRE-PATTERNS.md) · Pertinence 🔴 substance

**En une phrase** — défendre contre l'injection *par conception* en séparant les rôles : un LLM privilégié planifie sans jamais lire le contenu non fiable, un LLM en quarantaine traite ce contenu sans aucun privilège.

## L'idée
Le **Dual LLM pattern** scinde l'agent en deux. Le **Privileged LLM** orchestre, appelle les outils et voit les données sensibles, mais ne reçoit jamais directement le texte non fiable : il manipule ce dernier par références opaques. Le **Quarantined LLM** traite le contenu non fiable (résumer, extraire) mais ne peut déclencher aucune action. Une injection cachée dans le contenu n'atteint donc jamais le LLM qui a le pouvoir d'agir. **CaMeL** (Google DeepMind) durcit l'idée : un interpréteur extrait le plan du LLM privilégié sous forme de code, et un système de **capabilities** trace les flux de données pour bloquer les actions non autorisées, même si le LLM quarantaine est compromis.

## Tradeoff / quand l'utiliser
Approche la plus solide face à l'injection indirecte, au prix d'une architecture plus lourde (deux modèles, plan structuré, suivi des capacités) et de cas d'usage qui ne se plient pas tous à la séparation plan/contenu.

## Source primaire
Simon Willison, 2023, *Dual LLM pattern* (blog, simonwillison.net) ; Google DeepMind, 2025, *Defeating Prompt Injections by Design* (CaMeL), arXiv *arXiv:2503.18813 *(arXiv vérifié)**.

## Voir aussi
- [lethal-trifecta](lethal-trifecta.md) (hors-corpus sœur)
- [securite-agentique](../securite-agentique.md) (corpus)
