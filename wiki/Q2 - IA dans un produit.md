# Q2 — Embarquer l'IA dans un produit

> **Question** : comment utiliser l'IA **dans un produit** (LLM intégré, sécurité, agents métier…) ? Briques pour *construire et exploiter une application qui embarque un LLM* — pas l'assistance au codage.
>
> Index général et légende des icônes : [`outils IA.md`](outils%20IA.md). Autres questions : [Q1 — Produire du code](Q1%20-%20produire%20du%20code.md) · [Q3 — IA dans les autres métiers](Q3%20-%20IA%20dans%20les%20autres%20métiers.md).

<!-- format d'une ligne : **[Nom](url-officielle)** · [📄](fiches%20outils/nom.md) | Type | icône éco | icône LLM | résumé une ligne -->

<a id="fam-1"></a>
## 1. Infrastructure RAG / bases vectorielles
*Briques techniques sur lesquelles on bâtit des applications de recherche/RAG.*

> **Clé de lecture du coût LLM** : une base vectorielle **stocke et recherche des vecteurs** que tu fournis (BYO embeddings) → elle n'appelle pas de LLM, d'où **🟢** partout. Plusieurs proposent en **option** la génération d'embeddings hébergée (facturée au token) ou via ta clé provider (BYOK) — détaillé dans chaque fiche. Choix structurant : **rester dans Postgres** (pgvector), **embarqué** (Chroma, LanceDB), **serveur open-source** (Qdrant, Weaviate, Milvus) ou **managé propriétaire** (Pinecone, turbopuffer).

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[Chroma (ChromaDB)](https://www.trychroma.com/products/chromadb)** · [📄](fiches%20outils/chroma.md) | Base de données vectorielle (lib + Cloud) | 🔓🎁💳 | 🟢 | Base vectorielle open-source (Apache 2.0) pour RAG / recherche sémantique ; self-hosted gratuit ou Chroma Cloud serverless (Starter gratuit + à l'usage, Team 250 $/mois+). Stocke les embeddings, ne les génère pas (BYOK) |
| **[pgvector](https://github.com/pgvector/pgvector)** · [📄](fiches%20outils/pgvector.md) | Extension PostgreSQL (open-source) | 🔓 | 🟢 | **Extension Postgres** (pas une base à part) : type `vector` + index HNSW/IVFFlat. Licence PostgreSQL, **gratuite**, dispo chez Supabase/Neon/RDS/Cloud SQL/Azure → coût = celui de ta base. Vecteurs + SQL/JOIN/ACID au même endroit. Suffit jusqu'à ~dizaines de M de vecteurs ; au-delà, base dédiée |
| **[Qdrant](https://qdrant.tech/)** · [📄](fiches%20outils/qdrant.md) | Base vectorielle open-source (Rust) self-host + Cloud | 🔓🎁💳 | 🟢 | Moteur **open-source Apache 2.0 en Rust**, perf + **filtrage avancé** (filterable HNSW), quantization binaire (×32). Self-host `docker run` ou Cloud (free tier 1 Go à vie, puis à l'heure). FastEmbed local / Cloud Inference au token. Simple sous ~100 M vecteurs |
| **[Weaviate](https://weaviate.io/)** · [📄](fiches%20outils/weaviate.md) | Base vectorielle open-source (Go) self-host + Cloud | 🔓🎁💳 | 🟢 | **Open-source BSD-3 (Go)**, « batteries-included » : recherche hybride dense+BM25, vectorizers et generative search intégrés. Self-host gratuit ou Weaviate Cloud (Free → Flex 45 $ → Plus 280 $…, facturé aux dimensions stockées). HNSW **en RAM** = facteur dimensionnant |
| **[Milvus](https://milvus.io/)** · [📄](fiches%20outils/milvus.md) | Base vectorielle open-source distribuée + Zilliz Cloud | 🔓🎁💳 | 🟢 | **Open-source Apache 2.0** (LF AI & Data), pensé **échelle massive** (dizaines de Md de vecteurs), architecture distribuée K8s + GPU (CAGRA). Lite (embarqué) / Standalone / Distributed. Managé = **Zilliz Cloud** (Free → Serverless 4 $/M vCU). Ops distribuées plus lourdes |
| **[LanceDB](https://lancedb.com/)** · [📄](fiches%20outils/lancedb.md) | Base vectorielle **embarquée** open-source + Cloud/Enterprise | 🔓 | 🟢 | **Embarquée** (« SQLite du vectoriel »), open-source Apache 2.0, format columnar **Lance**, natif **object storage** (S3), **multimodal**, sans serveur à opérer. Cloud/Enterprise (BYOC) **prix non publics**. Local-first / pipelines ML. Écritures concurrentes limitées |
| **[Pinecone](https://www.pinecone.io/)** · [📄](fiches%20outils/pinecone.md) | Base vectorielle managée (propriétaire, SaaS) | 🔒🎁💳 | 🟢 | **Managée propriétaire, zéro-ops** (AWS/Azure/GCP), serverless, milliards de vecteurs. Starter gratuit → Standard 50 $/mois min, à l'usage (stockage 0,33 $/Go, reads/writes au M). Pinecone Inference (embeddings/rerank) en option. Lock-in mais simple |
| **[turbopuffer](https://turbopuffer.com/)** · [📄](fiches%20outils/turbopuffer.md) | Recherche vectorielle + full-text **serverless** (propriétaire) | 🔒💳 | 🟢 | **Serverless sur object storage** (~10× moins cher à l'échelle), vectoriel + BM25. Pay-as-you-go, min **64 $/mois** (Launch) → 256 $ → 4 096 $+. Latence froide 300–500 ms assumée. Traction forte (Cursor, Anthropic, Notion). Prix unitaires non publics en clair |

<a id="fam-2"></a>
## 2. Frameworks multi-agents généralistes (pour développeurs)
*Bibliothèques pour bâtir ses propres systèmes multi-agents — généralistes, pas spécifiques au codage.*

> **Clé de lecture** : ces frameworks **orchestrent** des appels modèle → tous **🔑 BYOK** (tu fournis tes clés ; ils ne facturent pas les tokens, sauf gateway optionnel). L'axe de choix : **bas niveau/contrôle** (LangGraph), **conversationnel** (AutoGen/AG2), **minimaliste** (OpenAI Agents SDK), **rôles** (CrewAI), **data/RAG** (LlamaIndex), **type-safe** (Pydantic AI), **TypeScript** (Mastra). Plusieurs ont une **fiche notion** dans `fiches/` (théorie) en plus de la fiche outil (produit/prix).

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[CrewAI](https://www.crewai.com)** · [📄](fiches%20outils/crewai.md) | Framework Python + plateforme cloud (AMP) | 🔓🔒 | 🔑 | Framework Python open-source (MIT) pour orchestrer des équipes d'agents IA autonomes (Crews) et des workflows (Flows), généraliste ; plateforme entreprise payante (AMP). BYOK |
| **[LangGraph](https://www.langchain.com/langgraph)** · [📄](fiches%20outils/langgraph.md) | Bibliothèque Python/TS (graphes stateful) + plateforme | 🔓🎁💳 | 🔑 | **Orchestration bas niveau** (LangChain Inc.), MIT : graphes avec cycles, persistance/checkpoints, human-in-the-loop, exécution durable. Le contrôle fin du flux. Plateforme managée (LangSmith Deployment) : Developer 0 $ → Plus 39 $/siège → Enterprise. Concept : [📄 notion](fiches/langgraph.md) |
| **[deepagents](https://github.com/langchain-ai/deepagents)** · [📄](fiches%20outils/deepagents.md) | Bibliothèque Python (+ JS/TS) — harness d'agents | 🔓 | 🔑 | **Harness haut niveau « batteries-included »** (LangChain, MIT, ~25k★) bâti sur LangGraph/`create_agent` : agents **long-horizon** clés en main — outil de **planification**, **sous-agents** à contexte isolé, **système de fichiers virtuel**, gestion/résumé auto du contexte, mémoire cross-session, human-in-the-loop, skills. Model-agnostic (frontier/open-weight/local), BYOK |
| **[AutoGen / AG2](https://microsoft.github.io/autogen/)** · [📄](fiches%20outils/autogen-ag2.md) | Framework Python multi-agents conversationnels | 🔓 | 🔑 | Agents **conversationnels** (GroupChat). ⚠️ **3 lignées** : AutoGen (Microsoft, MIT, **maintenance mode**) → successeur **Microsoft Agent Framework** (GA avr. 2026) ; **AG2** (fork communautaire, Apache 2.0, actif). Choisir selon l'écosystème. Concept : [📄 notion](fiches/autogen-ag2.md) |
| **[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)** · [📄](fiches%20outils/openai-agents-sdk.md) | SDK Python + TS (agents légers) | 🔓 | 🔑 | **Minimaliste** (MIT) : Agents, Handoffs, Guardrails, Sessions + tracing gratuit. Successeur en production de **Swarm**. Provider-agnostic (100+ LLM via LiteLLM). Pré-1.0. Bon point d'entrée léger |
| **[LlamaIndex](https://www.llamaindex.ai/)** · [📄](fiches%20outils/llamaindex.md) | Framework Python/TS (data/RAG + agents) + LlamaCloud | 🔓🎁💳 | 🔑 | **RAG-first** (MIT) : connecteurs, indexation, query, Workflows agentiques. Force = **LlamaParse** (parsing OCR de docs complexes). LlamaCloud à l'usage (crédits : Free 10k → Starter 50 $ → Pro 500 $). Concept : [📄 notion](fiches/llamaindex.md) |
| **[Pydantic AI](https://ai.pydantic.dev/)** · [📄](fiches%20outils/pydantic-ai.md) | Framework d'agents Python type-safe | 🔓🎁 | 🔑 | **Type-safe** (MIT) par l'équipe Pydantic : sorties structurées validées, « FastAPI feeling », DI, MCP/A2A. Model-agnostic. Observabilité via **Logfire** (freemium : Team 49 $ → Growth 249 $). Mûr (>v1.0) |
| **[Mastra](https://mastra.ai/)** · [📄](fiches%20outils/mastra.md) | Framework d'agents **TypeScript** + Mastra Cloud | 🔓🎁💳 | 🔑 | **TypeScript-natif** (Apache 2.0, cœur ; team Gatsby) : agents, workflows, RAG, mémoire, evals, sur Vercel AI SDK. Comble le vide vs l'écosystème Python. Mastra Cloud (beta) : Starter 0 $ → Teams 250 $. YC W25, seed 13 M$ |

<a id="fam-3"></a>
## 3. Sources de connaissances & données spécialisées (serveurs MCP)
*Serveurs MCP exposant aux agents des corpus de données/connaissances faisant autorité (réglementations, référentiels…), sans génération LLM.*

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[Ansvar Compliance MCP (suite)](https://github.com/Ansvar-Systems)** · [📄](fiches%20outils/ansvar-compliance-mcp.md) | Suite de serveurs MCP (sources réglementaires) | 🔓🎁 | 🟢 | Suite de ~150 serveurs MCP open-source (Ansvar AI, Stockholm) exposant le texte *verbatim* de réglementations : UE (GDPR, AI Act, DORA, NIS2…), droit par pays (UK, FR, DE…), protection des données/cybersécurité/concurrence/finance par autorité. Zéro résumé LLM (BYOK côté client), Apache 2.0, self-host ou Gateway (Free 100 requêtes/j/siège ; Premium 249 €/siège/mois). ⚠️ Volet US retiré (404) |

<a id="fam-4"></a>
## 4. Orchestration multi-agents & automatisation d'entreprise
*Plateformes qui coordonnent des agents IA dans les processus métier (au-delà du codage).*

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[MindFlight Orchestrator](https://www.mindflight.be/)** · [📄](fiches%20outils/mindflight-orchestrator.md) | Plateforme (orchestration d'agents IA) | 🔒 | ❓ | Plateforme B2B belge d'orchestration d'agents IA (« AI Operating System ») : connecte CRM/ERP/email…, agents comme workflows dynamiques, multi-provider (OpenAI, Anthropic, Mistral… ou local). Propriétaire, prix sur devis |
| **[Paperclip](https://github.com/paperclipai/paperclip)** · [📄](fiches%20outils/paperclip.md) | Plateforme open-source (orchestration & gouvernance d'agents) | 🔓 | 🟢 | Plateforme open-source (MIT) modélisant une équipe d'agents IA en entreprise — organigramme, budgets, portes d'approbation — pour des « zero-human companies » sous contrôle humain. **BYO Agent** : orchestre tes agents existants (Claude Code, Codex, Cursor…) qui portent leur propre auth → pas de clé LLM propre à Paperclip ; suivi de budget par agent. Auto-hébergeable |
| **[Flowise](https://flowiseai.com/)** · [📄](fiches%20outils/flowise.md) | Builder visuel d'apps/agents LLM (low-code) + Cloud | 🔓🎁 | 🔑 | Builder **drag-and-drop open-source (Apache 2.0, ~54k★)** d'apps/chaînes/agents LLM ; self-host gratuit ou Flowise Cloud managé. BYOK. Voisin de Sim, Dify, Langflow |
| **[Sim (Sim Studio)](https://www.sim.ai/)** · [📄](fiches%20outils/sim.md) | Builder visuel de workflows d'agents + Cloud | 🔓🎁🔁 | 🔑 | Plateforme **open-source (Apache 2.0, YC)** de construction/orchestration de workflows d'agents (canvas visuel, 1 000+ intégrations, tous les grands LLM) ; cloud (gratuit ~1 000 crédits → ~20–25 $/mois) ou self-host. BYOK |
| **[Gumloop](https://www.gumloop.com/)** · [📄](fiches%20outils/gumloop.md) | Builder no-code d'automatisations IA (SaaS) | 🔒🎁🔁 | 📦🔑 | Plateforme **no-code** propriétaire d'automatisation IA (Série B 50 M$, Benchmark) ; modèle de **crédits** (Free 5k/mois → Pro 37 $/mois → Enterprise). IA incluse via crédits, ou BYOK. Cible non-dev. Voisin de Relay.app, Zapier AI |
| **[Relay.app](https://www.relay.app/)** · [📄](fiches%20outils/relay-app.md) | Automatisation de workflows + human-in-the-loop (SaaS) | 🔒🎁🔁 | 📦🔑 | Automatisation propriétaire avec **human-in-the-loop** natif (étapes de validation humaine) + assistant IA en langage naturel (GPT/Claude/Gemini). Free → Pro 19 $ → Team 59 $/mois. Crédits IA inclus ou BYOK. Le différenciateur vs Zapier |

<a id="fam-5"></a>
## 5. Agents autonomes spécialisés par domaine
*Agents IA dédiés à un domaine métier précis (ici : sécurité offensive / pentest), au-delà du codage généraliste.*

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[AIDA](https://github.com/Vasco0x4/AIDA)** · [📄](fiches%20outils/aida.md) | Agent CLI + dashboard (pentest autonome) | 🔓 | 🟢🔑 | Agent de pentest autonome open-source (AGPL v3) reliant un LLM à 400+ outils de sécurité (nmap, sqlmap, ffuf, nuclei + payloads Python) via MCP, en conteneur Docker ; reco → exploitation → scoring CVSS 4.0. Model-agnostic : tourne via Claude Code **sans clé d'API LLM** (défaut) ou endpoint Anthropic-compatible custom (`--api-key`, optionnel). ⚠️ Alpha, tests autorisés uniquement, usage local |
| **[Shannon](https://github.com/KeygraphHQ/shannon)** · [📄](fiches%20outils/shannon.md) | Agent CLI (pentester IA white-box) | 🔓🔒 | 🟢🔑 | Pentester IA autonome **white-box** open-core (Shannon Lite AGPL-3.0) par Keygraph : analyse le code source + exécute de vrais exploits (preuve par exploitation) sur web/API ; multi-agent recon→analyse→exploitation→reporting, 96 % sur XBOW Benchmark. Credentials LLM requis mais OAuth d'abonnement Claude OK (pas que clé brute). Pro public dès 50 $/dev/mois. Pas de backend Keygraph pour Lite. ⚠️ Jamais en prod, env. jetable |

<a id="fam-6"></a>
## 6. Sécurité — outils exposés via MCP
*🔐 Outils de sécurité pilotables par l'agent : **offensif** (Kali, Burp, ZAP — tests autorisés uniquement, environnement isolé) et **défensif** (Snyk — scan de vulnérabilités de ton propre code).*

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[MCP Kali Server](https://www.kali.org/tools/mcp-kali-server/)** · [📄](fiches%20outils/mcp-kali-server.md) | Serveur MCP (exécution de commandes / pont Kali) | 🔓 | 🟢 | Pont MCP (API Flask) packagé dans Kali (`apt install`) donnant à un agent IA l'accès aux outils de pentest Kali : exécution de commandes (nmap, nxc, curl, gobuster…). Pentest assisté, CTF, HTB/THM. ⚠️ Exécution de commandes — conteneur isolé, contrôle d'accès, tests autorisés uniquement |
| **[Burp Suite MCP Server](https://github.com/PortSwigger/mcp-server)** · [📄](fiches%20outils/burp-mcp-server.md) | Serveur MCP / extension Burp Suite | 🔓 | 🟢 | Extension MCP **officielle** de Burp Suite (PortSwigger, GPL-3.0, Kotlin) connectant un client IA à Burp : analyse de requêtes/réponses, génération de payloads contextuels, analyse de JS obfusqué, failles de logique métier, prédiction d'endpoints. BApp Store, BYO client. ⚠️ Burp Community (gratuit) suffit ; Pro requis seulement pour Burp Collaborator (out-of-band). Tests autorisés |
| **[MCP ZAP Server](https://github.com/dtkmn/mcp-zap-server)** · [📄](fiches%20outils/mcp-zap-server.md) | Serveur MCP — opérateur OWASP ZAP | 🔓 | 🟢 | Serveur MCP (Spring Boot, Apache 2.0, par dtkmn) exposant **OWASP ZAP** aux agents : spider, scan actif/passif, import OpenAPI, findings, rapports. Garde-fous « production » (auth API-key/JWT, scopes, rate limits, audit, état Postgres), Docker/Helm. Non affilié OWASP. ⚠️ Tests autorisés |
| **[Snyk MCP](https://snyk.io/articles/secure-ai-coding-with-snyk-now-supporting-model-context-protocol-mcp/)** · [📄](fiches%20outils/snyk-mcp.md) | Serveur MCP (Snyk CLI) — sécurité **défensive** | 🎁🔁 | 🟢 | 🛡️ **Défensif** : serveur MCP intégré au Snyk CLI permettant à un agent de lancer des scans Snyk Code (SAST) + Snyk Open Source (SCA) et récupérer les vulnérabilités — garde-fou du code généré par l'IA. Compatible Cursor/Copilot/Windsurf… Plateforme freemium (Free / Team dès 25 $/mois). Expérimental |

<a id="fam-7"></a>
## 7. Contrôle d'ordinateur / desktop
*Donner au modèle une capacité d'**action** directe sur un environnement. **computer use** fait exception aux serveurs MCP : c'est le modèle lui-même qui agit, facturé en tokens API → 💸.*

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[Computer use (Anthropic)](https://docs.claude.com/en/docs/agents-and-tools/tool-use/computer-use-tool)** · [📄](fiches%20outils/computer-use.md) | Capacité/outil de modèle (API Anthropic) + démo open-source | 🔒💳 | 💸 | Outil de l'API Anthropic où **Claude lui-même** voit des screenshots et pilote souris/clavier ; ≠ MCP : c'est le modèle qui agit → **facturé en tokens API** (images comprises, coût potentiellement élevé). À exécuter en environnement isolé |

<a id="fam-8"></a>
## 8. LLMOps — évaluation & observabilité
*Maîtriser le comportement d'un LLM **en production** : **tracer** chaque exécution (déboguer une requête), **évaluer** la qualité (datasets, LLM-as-judge, CI), **observer** coûts, latence et erreurs dans le temps. Briques transverses du cycle de vie d'une appli IA — pas de l'assistance au codage.*

> **Cas particulier du coût LLM** : ces outils **observent tes propres appels** sans appeler de LLM eux-mêmes → 🟢 pour le tracing/observabilité. Mais l'**évaluation par LLM-as-judge** consomme des tokens → 🔑 BYOK (parfois revendu à l'usage). D'où la double icône 🟢🔑. Helicone (pur proxy d'observabilité) peut même *réduire* ta facture LLM via son cache.

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[Langfuse](https://langfuse.com/)** · [📄](fiches%20outils/langfuse.md) | Service web + self-host (open-source) | 🔓🎁🔁 | 🟢🔑 | Plateforme LLMOps open-source (cœur **MIT**, dossiers `ee` commerciaux) : tracing, évaluation, prompt management, datasets. Self-host gratuit ou cloud (Hobby gratuit 50k unités/mois → Core 29 $, Pro 199 $, Enterprise 2 499 $/mois). Obs sans coût LLM (🟢) ; éval LLM-as-judge en BYOK. Alternative OSS à LangSmith |
| **[LangSmith](https://www.langchain.com/langsmith)** · [📄](fiches%20outils/langsmith.md) | Service web (SaaS) + SDK | 🎁🔁💳 | 🟢🔑 | Plateforme LLMOps **propriétaire** de LangChain : tracing, éval, monitoring ; très intégrée à LangChain/LangGraph mais utilisable sans. Developer gratuit (1 seat, 5k traces/mois) → Plus 39 $/seat/mois (10k traces puis 2,50 $/1k), Enterprise sur devis (**seul** à permettre le self-host/VPC). Obs 🟢, éval LLM-as-judge en BYOK |
| **[Braintrust](https://www.braintrust.dev/)** · [📄](fiches%20outils/braintrust.md) | Service web (SaaS) + SDK | 🎁🔁💳 | 🟢🔑 | Plateforme LLMOps **propriétaire** centrée **évaluation/expérimentation** (datasets, scoring, playground) + logs. Starter gratuit (10 $ de crédits, 10k scores, 14j) → Pro 249 $/mois, Enterprise (on-prem/hybride). Facture data + scores + tokens (proxy LLM : 0,06/0,40 $ par Mtok in/out). Éval LLM-as-judge → tokens (BYOK/crédits) |
| **[Helicone](https://www.helicone.ai/)** · [📄](fiches%20outils/helicone.md) | Service web (proxy/gateway) + self-host (open-source) | 🔓🎁🔁 | 🟢 | Observabilité LLM open-source (**Apache 2.0**) surtout via **proxy** : logs, coûts, latence, caching, rate-limit, fallbacks. Self-host gratuit ou cloud (Hobby gratuit 10k requêtes/mois → Pro 79 $, Team 799 $, Enterprise on-prem). Intercepte tes appels, n'en génère pas (🟢) ; le caching peut *réduire* ta facture LLM |
| **[Arize Phoenix / Arize AX](https://phoenix.arize.com/)** · [📄](fiches%20outils/phoenix-arize.md) | Bibliothèque/app open-source (Phoenix) + Service web SaaS (Arize AX) | 🔓🎁🔁💳 | 🟢🔑 | **Phoenix** : observabilité/éval LLM open-source (**Elastic License 2.0**), bâtie sur **OpenTelemetry/OpenInference** (framework-agnostique), self-host gratuit. **Arize AX** : SaaS de monitoring ML/LLM en prod (Free 25k spans/mois → Pro 50 $/mois, Enterprise self-host/SLA/SOC2). Tracing 🟢, éval (`phoenix-evals`) en BYOK |

<a id="fam-9"></a>
## 9. Passerelles / routeurs LLM
*Une **API unique** (compatible OpenAI) devant des dizaines de fournisseurs : router selon prix/perf, basculer en **fallback** si un fournisseur tombe, mutualiser clés, budgets et observabilité. Brique directement liée à la **maîtrise du coût** et à la résilience multi-provider d'un produit. Notion de fond : [observabilité LLM — best practices](fiches/observabilite-llm-best-practices.md).*

> **Clé de lecture du coût LLM** : deux modèles s'opposent. Les gateways **self-host / pass-through** ([LiteLLM](fiches%20outils/litellm.md), [Portkey](fiches%20outils/portkey.md)) ne facturent **pas** les tokens — tu gardes ta relation directe au fournisseur (🔑 BYOK). Les gateways **hébergés** ([OpenRouter](fiches%20outils/openrouter.md), [Requesty](fiches%20outils/requesty.md)) peuvent **revendre l'inférence** avec frais/marge (💸), tout en offrant souvent un mode BYOK (🔑).

| Outil | Type | Modèle éco | Coût LLM | En bref |
|-------|------|:----------:|:--------:|---------|
| **[OpenRouter](https://openrouter.ai/)** · [📄](fiches%20outils/openrouter.md) | Service web (gateway hébergé) | 🔒💳 | 💸🔑 | Gateway hébergé : 1 API (format OpenAI) vers **400+ modèles / 60+ fournisseurs**, routing prix/perf + failover. **Aucune marge sur l'inférence** ; se rémunère sur l'**achat de crédits** (5,5 % carte, min 0,80 $ ; 5,0 % crypto). Mode BYOK aussi (migre vers un abonnement fixe, montant non publié). Le plus « marketplace clé-en-main » |
| **[LiteLLM](https://www.litellm.ai/)** · [📄](fiches%20outils/litellm.md) | Bibliothèque Python (SDK) + Proxy self-host | 🔓🎁 | 🔑 | Cœur **open-source MIT** (BerriAI) : SDK (dans le code) **ou** proxy/gateway self-host (clés virtuelles, budgets, multi-tenant). API unifiée vers 100+ LLM, routing/fallback. **Pass-through pur** : ne facture pas les tokens (BYOK). Enterprise payant (SSO/RBAC/audit, self-managed, prix non publiés) |
| **[Portkey](https://portkey.ai/)** · [📄](fiches%20outils/portkey.md) | AI Gateway open-source (MIT) self-host + SaaS managé | 🔓🎁🔁 | 🔑 | **Open-core MIT** : gateway < 1 ms par-dessus 1 600+ modèles + guardrails (50+), observabilité (OTel), caching sémantique, prompt management. **BYOK pass-through** (ne marque pas les tokens). SaaS facturé au volume de logs (Developer gratuit 10k → Production 49 $/mois → Enterprise). Control plane « enterprise » |
| **[Requesty](https://www.requesty.ai/)** · [📄](fiches%20outils/requesty.md) | Service web (gateway hébergé) | 🔒🎁💳 | 💸🔑 | Gateway hébergé **EU-first / RGPD** (« alternative européenne à OpenRouter ») : 400+ modèles, smart routing, caching, observabilité. Free 200 req/j → pay-as-you-go **+5 % de marge** sur le tarif fournisseur → Enterprise (SSO/RBAC/PII/résidence EU). BYOK supporté (% de frais non documenté). **Early-stage** (seed 3 M$ sept. 2025) |
