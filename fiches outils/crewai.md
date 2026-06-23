---
outil: "CrewAI"
titre: "CrewAI"
type: "Framework (bibliothèque Python) + plateforme cloud"
url: https://www.crewai.com
modele_economique: "Open-source (MIT, framework gratuit) + offre entreprise propriétaire (CrewAI AMP / Enterprise — cloud ou on-premise, tarif sur devis ; essai gratuit du control plane)"
cout_llm: "BYOK — tu branches tes propres clés API LLM (OpenAI par défaut, Anthropic, etc.) ou des modèles locaux (Ollama). Le coût des tokens est généralement le premier poste de dépense."
---

# CrewAI

**En une phrase** — Framework Python open-source pour **orchestrer des équipes d'agents IA autonomes jouant des rôles** (« Crews ») et des **workflows événementiels** (« Flows »), généraliste (pas spécifique au codage), doublé d'une plateforme entreprise (AMP) pour le déploiement, l'observabilité et la gouvernance en production.

## Type & intégration
**Bibliothèque Python** (`pip install crewai`) — un framework qu'on importe dans son propre code pour construire des systèmes multi-agents. Ce n'est ni un CLI clé-en-main, ni un serveur MCP, ni un agent prêt à l'emploi : c'est une **brique à assembler** dont le développeur écrit la logique.

Deux abstractions principales :
- **Crews** — équipes d'agents autonomes qui collaborent, chacun avec un rôle, un objectif, des outils ; ils se répartissent et délèguent les tâches.
- **Flows** — orchestration événementielle déterministe (contrôle fin du déroulé, branchements, état) pour des automatisations de niveau production.

Particularité technique revendiquée : **entièrement réécrit from scratch, indépendant de LangChain** (« lean, lightning-fast »), contrairement aux premières versions.

Côté production, **CrewAI AMP** (Agent Management Platform, ex-CrewAI Enterprise) fournit un control plane cloud ou on-premise : tracing temps réel, historique d'exécution, inspection pas-à-pas, connecteurs (Gmail, Slack, Salesforce, HubSpot…).

## Modèle économique
**Mixte : open-source + cloud entreprise.**
- **Framework** : open-source sous **licence MIT**, gratuit, usage personnel et commercial. ~53k+ ★ sur GitHub (dépôt `crewAIInc/crewAI`), communauté active.
- **CrewAI AMP / Enterprise** : offre **propriétaire** avec un **tier Free à 0 $** (éditeur visuel, copilote, intégration GitHub, **50 exécutions de workflow/mois**) puis **Enterprise sur devis** (prix non public). Ajoute déploiement managé, observabilité, sécurité avancée (PII masking, RBAC, secret manager, audit logs, SSO), conformité (SOC2, HIPAA), VPC isolés et support 24/7.

## Coût LLM
**BYOK 🔑** — CrewAI ne fournit pas de LLM. Tu fournis tes propres **clés API** (OpenAI par défaut, mais Anthropic, Gemini, etc. supportés via la couche d'abstraction LLM) ou tu pointes vers des **modèles locaux** (Ollama). Tu paies donc directement le fournisseur de modèle à l'usage.

**Ordre de grandeur** : comme tout système multi-agents, le coût explose vite — plusieurs agents qui s'échangent des messages, raisonnent et appellent des outils multiplient les appels LLM. Une exécution « Crew » non triviale peut consommer des **dizaines à centaines de milliers de tokens**, soit de quelques cents à plusieurs dollars par run selon le modèle (un modèle haut de gamme type Opus/GPT-4 coûte des ordres de grandeur de plus qu'un petit modèle ou un modèle local gratuit). La maîtrise des coûts (choix du modèle par agent, limites d'itérations) est un sujet à part entière.

## À quoi ça sert
Construire des **applications multi-agents généralistes** : pipelines de recherche/analyse, génération de contenu, automatisation de processus métier, agents connectés à des outils d'entreprise, assistants de support, etc. Le développeur compose des agents spécialisés qui collaborent sur une tâche complexe décomposée. Cible aussi bien le prototypage rapide (framework gratuit) que la mise en production gouvernée (AMP).

## Notes / à creuser
- **Famille différente des outils de codage clé-en-main** : CrewAI est un **framework multi-agents généraliste à construire**, pas un agent de codage prêt à l'emploi. À distinguer nettement de [Liza](liza.md) (orchestrateur de codage clé-en-main), [Kilo Code](kilo-code.md), [Trae](trae.md), [Supacode](supacode.md). Concurrents directs dans la même catégorie : **LangGraph** (LangChain), **AutoGen** (Microsoft), **OpenAI Agents SDK**, **LlamaIndex Agents**, Google ADK, Pydantic AI.
- **Lien avec [Liza](liza.md)** : CrewAI apparaît dans le comparatif concurrentiel de [Liza](liza.md) (`specs/architecture/competition-survey`). Liza le classe comme **framework général à guardrails *post-hoc*** : les garde-fous (validation, faithfulness scoring, guardrails de tâche) sont ajoutés autour des agents plutôt qu'imposés mécaniquement par construction — à l'opposé de l'approche déterministe « par le code » revendiquée par Liza. Les guardrails avancés sont surtout dans l'offre **payante AMP**, pas dans le framework de base.
- **Point d'attention coût** : multi-agents = consommation LLM potentiellement élevée et peu prévisible ; surveiller le nombre d'itérations et le choix des modèles.
- **À creuser** : maturité réelle des Flows vs Crews ; profondeur des guardrails open-source vs AMP ; tarif précis de l'Enterprise (sur devis, non public).

## Source
- Site officiel : https://www.crewai.com — *(vérifié le 2026-06-15)*
- Dépôt : https://github.com/crewAIInc/crewAI (MIT, ~53k+ ★) — *(vérifié le 2026-06-15)*
- CrewAI AMP : https://blog.crewai.com/crewai-amp-the-agent-management-platform/ — *(vérifié le 2026-06-15)*
- Comparatif concurrentiel de Liza : `liza-mas/liza/specs/architecture/competition-survey` — *(vérifié le 2026-06-15)*
