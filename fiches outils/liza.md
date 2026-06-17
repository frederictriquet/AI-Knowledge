---
outil: "Liza"
type: "CLI (Go) — système multi-agents de codage"
url: https://github.com/liza-mas/liza
modele_economique: "Open-source (Apache 2.0), gratuit"
cout_llm: "Intégré — wrappe des agents CLI existants (BYO agent) ; pas de facturation au token via Liza"
---

# Liza

**En une phrase** — « Disciplined Multi Coding Agent System » : un orchestrateur qui *encadre mécaniquement* des agents de codage existants pour livrer du code de qualité production dès le premier passage, en imposant les bonnes pratiques par du code plutôt qu'en espérant que l'agent obéisse.

## Type & intégration
**CLI (binaire `liza`)** écrit en **Go** (~35 000 lignes + ~92 000 lignes de tests), open-source. Ce n'est ni un serveur MCP ni une lib : un orchestrateur/framework autonome qu'on installe et lance localement. Il **wrappe les CLIs d'agents existants** — Claude Code, Codex, Kimi, Mistral, Gemini, OpenCode — plutôt que d'appeler les API directement.

Architecture hybride : des **superviseurs déterministes en Go** imposent mécaniquement les transitions d'état, frontières de rôles, autorité de merge et portes TDD ; les **agents LLM** ne gèrent que le jugement, sous un **contrat comportemental**. État auditable dans `.liza/state.yaml` et `.liza/log.yaml`.

Trois modes : **Pairing**, **Adversarial Pairing**, et **Multi-Agent** (pipeline autonome spec→code, 13 rôles sur 4 phases : spécification, architecture, codage, intégration).

## Modèle économique
**Open-source, licence Apache 2.0**, gratuit. Projet communautaire (⚠️ risque « single-maintainer » : un auteur principal, pas de pipeline de contribution formel à ce stade).

## Coût LLM
**Intégré** 🟢 — pas de facturation au token via Liza : il s'appuie sur ta **configuration personnelle** d'agents (« your personal setup is used »), donc tes abonnements existants (BYO agent). Particularité : le mode multi-reviewer exige un **quorum à diversité de fournisseurs** (≥2 LLM distincts) pour éviter le biais mono-fournisseur → il faut **plusieurs credentials de providers**. Les modèles faibles peuvent échouer au « contract capability test ».

## À quoi ça sert
Combler l'écart « ça marchait dans la démo » : neutraliser **55+ modes d'échec documentés des LLM** (sycophantie, faux correctifs/« phantom fixes », scope creep, corruption de tests, complétions hallucinées), chacun mappé à une contre-mesure. Paires **doer/reviewer adverses** à autorité *contraignante* (le reviewer peut bloquer le merge), sprints autonomes, l'humain agissant en « circuit-breaker » entre les sprints.

## Positionnement concurrentiel
*(d'après le `specs/architecture/competition-survey` du dépôt)*

Liza se revendique seule dans la catégorie **« behavioral enforcement »** : confiance par contrainte *mécanique* (code), pas par prompt. Comparaisons clés :

- **BMAD-METHOD** (~45k★, JS) — méthodologie agile full-lifecycle (Analyse → Planning → Solutioning → Implémentation). Voisin philosophique, jugé **complémentaire** : BMAD en amont (méthodo, PRD, archi, UX) nourrit l'exécution disciplinée de Liza en aval. BMAD = humain-dans-la-boucle ; Liza = exécution autonome contrainte.
- **GSD** (~37k★) — concurrent direct le plus traction ; résout la dégradation de contexte (sous-agents frais), Liza résout les échecs *comportementaux* (même à contexte frais).
- **gstack** (~100k★) — suite workflow large ; pas d'autorité de revue contraignante ni de crash recovery, là où Liza ajoute un état de tâche détenu par le superviseur.
- **CrewAI** (~45k★) — framework général ; ses guardrails sont post-hoc, Liza prévient structurellement.
- **Symphony** (OpenAI, preview) — scheduler sans approbation/sandbox ; Liza = la supervision qu'on ajoute par-dessus.
- **Paperclip** (~14k★, ops business) et **Ruflo** (largeur : 60+ types d'agents, 215+ outils, routage ML) — Liza fait le pari inverse : **profondeur** (peu de rôles, enforcement comportemental).

Insight stratégique du document : « la couche scheduler/orchestrateur se banalise » tandis que « la confiance entreprise reste non résolue ». **Faiblesses assumées** : tâches triviales (cérémonie disproportionnée), besoins flous (pas de workflows de discovery produit), modèles trop faibles, coût de setup (multi-terminaux, multi-credentials).

## Notes / à creuser
- Famille 1b, mais **saveur « discipline/qualité »** distincte des runners parallèles ([[superset]], [[conductor]], [[supacode]], [[orca]]) qui visent surtout le **débit**. Liza vise la **fiabilité** par enforcement.
- Recoupe aussi le **spec-driven** ([[cavekit]]) par son pipeline spec→code, mais avec une couche d'enforcement mécanique en plus.
- Concurrents cités = candidats fiches : **BMAD**, **GSD**, **gstack**, **CrewAI**, **Ruflo**, **Paperclip**.

## Source
- Dépôt : https://github.com/liza-mas/liza · Docs : https://lizamas.mintlify.app/
- Comparatif : https://github.com/liza-mas/liza/tree/main/specs/architecture/competition-survey

*(vérifié le 2026-06-15 — README + competition-survey du dépôt + recherche web)*
