---
outil: "BMAD-METHOD"
titre: "BMAD-METHOD"
type: "Framework / méthodologie (agents IA pour IDE)"
url: https://github.com/bmad-code-org/BMAD-METHOD
modele_economique: "Open-source (licence MIT) — 100% gratuit, sans paywall ni contenu réservé"
cout_llm: "Intégré (🟢) — tourne DANS ton client IA (Claude Code, Cursor…), aucune clé d'API LLM dédiée requise ; le coût LLM est celui de ton client"
---

# BMAD-METHOD

**En une phrase** — Framework open-source de développement agile piloté par l'IA (« Breakthrough Method for Agile AI-Driven Development ») qui orchestre une vingtaine d'agents-personas spécialisés (PM, Architecte, Dev, UX…) à travers des workflows guidés couvrant tout le cycle produit, du brainstorming au déploiement.

## Type & intégration
Ce n'est pas une application qui tourne seule mais une **méthodologie + un ensemble d'agents et de workflows** que l'on installe dans son projet (via `npx bmad-method install`) puis que l'on pilote depuis son IDE/agent IA habituel (Claude Code, Cursor, etc.). Écrit majoritairement en JavaScript/Node (avec du HTML pour la doc et du Python pour certains outils ; prérequis Node ≥ 20.12, Python ≥ 3.10, `uv`). Il fournit 21 agents spécialisés et 50+ workflows guidés, ainsi qu'un « Party Mode » réunissant plusieurs personas dans une même session. Version courante v6.8.0 (mi-2026).

Le cycle est structuré en quatre grandes phases : **Analyse → Planning → Solutioning → Implémentation**, avec une intelligence « scale-adaptive » qui s'ajuste du simple bug-fix au système d'entreprise.

## Modèle économique
**Open-source sous licence MIT**, entièrement gratuit. Le projet revendique l'absence de paywall, de contenu réservé ou de Discord fermé. Forte traction communautaire : ~49k★, ~5,7k forks, plus d'une centaine de contributeurs, un site de doc multilingue (5 langues) et un système de « marketplace ». Quelques ressources d'écosystème autour de l'auteur (bmadcode.com, chaîne YouTube, Discord communautaire).

## Coût LLM
**Intégré 🟢 — aucune clé d'API LLM requise** (vérifié : 0 mention de clé/BYOK dans le README ; prérequis = seulement Node/Python pour l'installeur). BMAD est un ensemble de prompts/agents Markdown qui **tourne DANS ton client IA** (Claude Code, Cursor…) et consomme donc le LLM via **ce client** (ton abonnement existant), sans clé propre ni surcoût. Option « web bundles » (Gemini Gems / Custom GPTs) pour planifier sur un abonnement web plat. Le coût LLM dépend de ta propre consommation côté client. Comme la méthode multiplie les agents et workflows (analyse, planning, architecture, implémentation, revue…) sur des sessions longues, l'usage de tokens peut être conséquent en ordre de grandeur, mais cela reste ta facture LLM directe.

## À quoi ça sert
Cadrer et exécuter un projet logiciel (ou de jeu) de bout en bout avec l'IA comme collaboratrice experte plutôt que comme exécutante autonome : brainstorming, recherche marché/domaine, PRFAQ (Working Backwards d'Amazon), design UX, PRD, architecture, puis implémentation, tests, sécurité, DevOps et documentation traités comme des phases de premier rang. La philosophie affichée : l'IA « te guide à travers un processus structuré pour faire ressortir ta meilleure réflexion », sans penser à ta place.

## Notes / à creuser
- BMAD apparaît dans le comparatif concurrentiel de [Liza](liza.md) (`liza-vs-bmad-comparison.md`). Le document les présente comme **architecturalement complémentaires** plutôt que concurrents : BMAD est fort sur la **découverte produit amont** (idéation, planning, périmètre organisationnel large), là où Liza reste volontairement légère ; à l'inverse, Liza mise sur l'**exécution downstream** et l'**application mécanique** de contraintes.
- Limites pointées par le comparatif Liza (à vérifier indépendamment, source partiale) : (1) discipline **au niveau du prompt** sans garde-fous mécaniques (rien n'empêche techniquement un agent de contourner le workflow ou de merger sans revue) ; (2) **perte d'état entre sessions** (chat frais par workflow, pas de persistance inter-workflows) ; (3) **exécution séquentielle** par conception — pas de coordination d'agents en parallèle sur le même code.
- Plusieurs forks communautaires existent (homonymie : `macelik/bmad-method`, `ResourcefulAI/bmad-method`, `EvolutionAPI/BMAD-METHOD-BY-EVOLUTION`, etc.) ; le dépôt de référence est bien **`bmad-code-org/BMAD-METHOD`**.
- Branches notables : `v6-alpha`, `V4` — versionnage actif.

## Source
- Dépôt officiel : https://github.com/bmad-code-org/BMAD-METHOD *(vérifié le 2026-06-15)*
- Site : https://bmadcode.com — Doc : https://docs.bmad-method.org *(références citées par le dépôt ; non rechargées une à une)*
- Comparatif Liza : https://raw.githubusercontent.com/liza-mas/liza/main/specs/architecture/competition-survey/liza-vs-bmad-comparison.md *(vérifié le 2026-06-15 ; source partiale, point de vue concurrent)*
