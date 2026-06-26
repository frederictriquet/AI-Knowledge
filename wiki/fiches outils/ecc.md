---
outil: "ECC"
titre: "ECC"
themes: [frameworks-outillage, gouvernance-alignement-ops, securite, efficacite-cout]
type: "Système de harness d'agent (skills/agents/hooks/rules) — multi-plateforme, OSS + GitHub App"
url: https://github.com/affaan-m/ECC
modele_economique: "Open-source (MIT) gratuit ; ECC Pro (GitHub App, repos privés) 19 $/siège/mois + tier gratuit ; sponsoring GitHub dès 5 $/mois"
cout_llm: "🟢🔑 mixte — pilote le harness hôte sans clé ; BYOK multi-provider (Anthropic/OpenAI/Ollama local) pour les modules autonomes"
---

# ECC

**En une phrase** — « operator system » open-source qui empile sur ton agent existant (Claude Code, Cursor, Codex, OpenCode…) une infrastructure complète — skills, sous-agents, hooks, *instincts* appris, mémoire persistante, scanner de sécurité — pour standardiser le travail agentique multi-harness.

## Type & intégration
**Surcouche de harness multi-plateforme** (par `affaan-m`). S'installe par-dessus l'agent hôte (`/plugin install ecc@ecc`, ou `./install.sh --profile [full|core|minimal]`). Annonce **67 agents, 261 skills, 92 shims de commandes legacy, 15 événements de hook, 6 serveurs MCP**, 12+ écosystèmes langage. Briques nommées : **Skills** (surface principale, remplace les slash-commands), **Agents** (sous-agents délégués), **Hooks** (automations sur événements), **Rules** (guidelines par langage), **Instincts** (patterns appris avec *confidence scoring*, « Continuous Learning v2 »), **AgentShield** (audit de sécurité, dépôt séparé). Adapter pattern (`adapter.js`) pour réutiliser les scripts entre harnesses.

## Modèle économique
**Open-source MIT** (*« MIT-licensed forever »*), gratuit. Couche commerciale : **ECC Pro** = GitHub App hébergée pour **repos privés**, **19 $/siège/mois**, avec tiers free/pro/enterprise sur le GitHub Marketplace (« ECC Tools »). Financement OSS via **GitHub Sponsors dès 5 $/mois** (paliers de sponsoring jusqu'à 3 700 $/mois = placement logo, *pas* d'accès produit). *(constaté 2026-06-24)*

## Coût LLM
**🟢🔑 mixte.** Le **cœur** (skills, hooks, rules, instincts en YAML, injection de contexte, `/learn`) tourne **dans ta session hôte** → consomme ton abonnement/agent existant, **sans clé propre** (🟢). Mais ECC embarque un **vrai layer LLM multi-provider** (`src/llm/providers/` : Anthropic, OpenAI, **Ollama en local**, …) utilisé par les **modules autonomes** — `security-scan`/**AgentShield** (« Requires ANTHROPIC_API_KEY »), `autonomous-agent-harness` (`curl api.anthropic.com`) — qui demandent **ta clé** (🔑 BYOK ; option locale Ollama = gratuite). Inclut un `cost-tracker.js` qui instrumente le coût token (cohérent avec son discours d'optimisation).

## À quoi ça sert
Standardiser et outiller le travail multi-agents : mêmes skills/hooks/rules/sécurité across Claude Code, Cursor, Codex, OpenCode. Cible le dev qui jongle entre plusieurs harnesses et veut un socle commun + apprentissage persistant (instincts) + garde-fous (`beforeShellExecution`, AgentShield).

## Notes / à creuser
- **Famille 4 (workflow/méthodologie)** : peer de [Superpowers](superpowers.md), [gstack](gstack.md), [BMAD-METHOD](bmad-method.md), [GSD](gsd.md), [Cavekit](cavekit.md) et du méta-harnais [Ruflo](ruflo.md). Positionnement le plus **maximaliste** du groupe (« operator system » tout-en-un) là où les peers sont plus focalisés.
- ⚠️ **Jeune malgré le discours « production »** : dépôt **créé le 2026-01-18** (~5 mois), mais se présente comme *« production-ready »* « evolved over 10+ months » — formulation à prendre avec prudence. **v2.0.0** (juin 2026).
- ⚠️ **Hype ≠ valeur prouvée** : **220,8k★ / 33,8k forks** (confirmés API GitHub) atteints en ~5 mois. C'est dans la fourchette haute des harnesses (Superpowers ~237k, gstack ~114k) — donc *pas* une anomalie, mais un niveau d'étoiles élevé reste un **signal de viralité/promotion, pas une preuve d'usage en production**. Aucun benchmark externe.
- ⚠️ **Métriques internes auto-déclarées non vérifiées** : « 997+ tests », « AgentShield 1282 tests / 98 % couverture / 102 règles », « 261 skills » — chiffres du README, non audités.
- ⚠️ **Tension avec son propre discours** : prêche la sobriété de contexte (« keep under 10 MCPs, under 80 tools » ; une description d'outil MCP grignote la fenêtre 200k → ~70k) tout en livrant 261 skills + 67 agents + 6 MCP + injection SessionStart (8000 car.) → risque du **bloat de contexte** qu'il dénonce ; à installer en profil `core`/`minimal` plutôt que `full`.
- ⚠️ **Mono-mainteneur** : *« a single maintainer ships weekly across 7 harnesses »* → risque de soutenabilité/bus-factor pour un usage « production ».
- **Pour un choix** : intérêt réel si tu veux un socle *unifié multi-harness* avec apprentissage + sécurité intégrés. Mais pour la plupart des besoins, un peer **focalisé** (Superpowers pour la méthodo, Spec Kit pour le spec-driven) est plus simple, plus sobre en contexte et moins risqué qu'un système tout-en-un jeune et volumineux.

## Source
- Dépôt : https://github.com/affaan-m/ECC (licence MIT, JavaScript) · Pricing : https://ecc.tools/pricing · AgentShield : https://github.com/affaan-m/agentshield
- Stats & code vérifiés via l'API GitHub et lecture des fichiers (`src/llm/providers/`, `.cursor/hooks/`, `SPONSORING.md`, README).

*(vérifié le 2026-06-24 — API GitHub + lecture du code + README)*
