---
outil: "Cavekit"
titre: "Cavekit"
type: "Plugin (Claude Code) + skills"
url: https://github.com/JuliusBrussee/cavekit
modele_economique: "Open-source (MIT), gratuit"
cout_llm: "Intégré — tourne dans Claude Code, pas de coût LLM séparé"
---

# Cavekit

**En une phrase** — plugin Claude Code de développement *spec-driven* : il transforme une intention en langage naturel en spécifications durables, puis les exécute, avec des specs qui survivent aux resets de contexte.

## Type & intégration
**Plugin Claude Code** (installable via la marketplace) et **framework de skills**. Spécifications en **Markdown** + commandes shell. Tourne entièrement dans Claude Code. Du même auteur que [Caveman](caveman.md) et [Cavemem](cavemem.md) (Julius Brussee).

## Modèle économique
**Open-source, licence MIT**, gratuit ; projet communautaire.

## Coût LLM
**Intégré** 🟢 — utilise Claude via Claude Code, aucune clé API ni coût séparé. Mise en avant de l'**efficacité tokens** grâce à l'« encodage caveman » (specs compressées, ~75 % de tokens en moins vs specs en prose).

## À quoi ça sert
Combler l'écart entre **planification et exécution** en dev assisté par IA : maintenir des **spécifications durables** qui survivent aux resets de contexte, et **rétropropager automatiquement** les échecs de tests dans les specs (moins de suivi manuel). Philosophie v4 : « one spec, three commands, no orchestration ».

## Notes / à creuser
- La v3.1.0 incluait une **peer-review cross-modèle** (via Codex) ; la **v4 l'a retirée** au profit de la simplicité.
- Écosystème « cave\* » de Julius Brussee : [Caveman](caveman.md) (compression de la sortie), [Cavemem](cavemem.md) (mémoire persistante), Cavekit (spec-driven). L'encodage caveman est le fil rouge.

## Source
- Dépôt : https://github.com/JuliusBrussee/cavekit

*(vérifié le 2026-06-15 — README GitHub)*
