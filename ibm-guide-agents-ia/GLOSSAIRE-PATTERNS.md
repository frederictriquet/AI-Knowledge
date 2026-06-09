# Glossaire des patterns agentiques — carte pour ingénieur confirmé (v2, vérifiée)

Décodage des notions du guide IBM en langage d'ingénieur. **Cette v2 est réconciliée
avec une lecture intégrale des 77 fichiers** (la v1 contenait des patterns inventés et
des sources erronées — voir l'encart ci-dessous).

**Tags de pertinence**
- 🟢 **pur-nom** : idée que tu appliques déjà ; il te manquait l'étiquette.
- 🟡 **tradeoff** : idée simple mais compromis chiffré/non évident. ~5 min.
- 🔴 **substance** : non trivial même pour un senior, ou source primaire à lire.

**Tags de provenance**
- ✅ **présent** dans le corpus IBM (fichier indiqué).
- ➕ **hors-corpus** : ajout depuis l'état de l'art (le corpus ne le mentionne pas).

> ⚠️ **Correction vs glossaire v1.** Étaient **inventés / absents du corpus** : Toolformer,
> MemGPT, Self-RAG, PAL, MRKL, LLM Compiler, Society of Mind. La mémoire avait été attribuée
> à tort à *Generative Agents* — le corpus cite en réalité **CoALA**. Étaient **manqués** :
> LATS, RAISE, BDI, structures holonique/coalition, DroidSpeak, KQML/FIPA-ACL, CAMEL/ChatChain/
> MacNet, slopsquatting, taxonomie des erreurs d'appel de fonction, Alignment Studio/RADAR,
> et le paysage complet à 7 protocoles.

---

## 1. Raisonnement & prompting

| Pattern | Décodage ingénieur | Pertinence | Provenance | Source primaire |
|---|---|---|---|---|
| **[Chain-of-Thought (CoT)](concepts/chain-of-thought.md)** | « Écris ton raisonnement avant la réponse ». | 🟢 | ✅ (01,10,18,28) | Wei et al., 2022 (➕ — non citée par IBM) |
| **[ReAct](concepts/react.md)** | Boucle `pensée → action(outil) → observation`. Squelette de la plupart des agents. | 🟢 | ✅ (18,28,01,17) | **Cité** (18,28) : Yao et al., *ReAct*, arXiv:2210.03629 |
| **[ReWOO](concepts/rewoo.md)** | Planifie tout d'avance (Planner), exécute sans rappeler le LLM (Worker), synthétise (Solver). | 🟡 | ✅ (30,18,01,17,31) | **Cité** (30) : Binfeng Xu et al., 2023, arXiv:2305.18323. Chiffres : HotpotQA 42,4 %@2k tokens vs ReAct 40,8 %@10k |
| **[Autoréflexion / Reflexion](concepts/reflexion.md)** | L'agent critique son échec et réessaie en intégrant la critique en mémoire. | 🟡 | ✅ (17,18,28) | Shinn et al., 2023 (➕) |
| **[LATS](concepts/lats.md)** (Language Agent Tree Search) | MCTS appliqué aux agents LLM : arbre de raisonnement-action + autoréflexion stockée. | 🔴 | ✅ (18) | **Cité** (18) : *LATS*, arXiv (≈2310.04406). Plus coûteux que ReAct/ReWOO |
| **[RAISE](concepts/raise.md)** | Variante de ReAct avec composant mémoire (court/long terme) ajouté à la boucle. | 🟡 | ✅ (17) | Cité par nom seul (pas de lien) |
| **[Tree of Thoughts (ToT)](concepts/tree-of-thoughts.md)** | CoT en arbre : explorer/élaguer/backtracker plusieurs branches. | 🔴 | ✅ (18,10) | Yao et al., 2023 (➕ — nommé sans citation) |
| **[Logique conditionnelle / heuristique](concepts/logique-conditionnelle-heuristique.md)** | `if/else` et scores câblés dans la boucle. | 🟢 | ✅ (18) | — (programmation classique) |

> Insight transverse (fichier 18, sourcé) : ReAct = risque de boucles infinies ; ReWOO = sans
> observation, gagne en tokens mais se dégrade si trop d'outils/contexte limité ; LATS = meilleur
> mais coûteux. C'est *le* comparatif à retenir, et il est réellement dans le corpus.
> **Garde-fou LATS** : ne le réserver qu'aux problèmes décomposables **avec vérificateur objectif**
> (tests, compilateur, juge crédible) où l'on peut cramer beaucoup d'appels ; avant lui, épuiser
> Self-Consistency et Reflexion ; et ne jamais réimplémenter MCTS soi-même (LangGraph / LlamaIndex).

---

## 2. Outils & augmentation

| Pattern | Décodage ingénieur | Pertinence | Provenance | Source |
|---|---|---|---|---|
| **[Tool / function calling](concepts/tool-calling.md)** | Le modèle émet un appel structuré (JSON + `tool_call_id`) que ton code exécute. | 🟢 | ✅ (19,20,21,52) | — |
| **[ReAct vs function calling](concepts/react-vs-function-calling.md)** | Function calling = plus rapide/économe sur tâches prévisibles ; ReAct = meilleur sur l'imprévisible, au prix des tokens de boucle. | 🟡 | ✅ (28) | comparatif IBM (utile) |
| **[Tool grounding](concepts/tool-grounding.md)** | Donner à l'agent des outils qui exposent l'**état légal vérifiable** (ex. coups d'échecs légaux) pour l'empêcher d'halluciner. | 🟡 | ✅ (21) | tutoriel échecs, bonne illustration |
| **[LLM-dans-un-outil](concepts/llm-dans-un-outil.md)** | Un outil utilise lui-même un appel LLM (ex. classifieur de pertinence yes/no). | 🟡 | ✅ (20) | tutoriel Ollama |
| **[MRKL Systems](concepts/hors-corpus/mrkl.md)** | LLM-**routeur** devant des modules experts. La décision de routage est **neuronale** (prompting ou apprise), pas des règles câblées — ancêtre direct de ReAct/function calling. | 🟡 | ➕ **hors-corpus** | Karpas et al., 2022, arXiv:2205.00445 |
| **[LLM Compiler](concepts/hors-corpus/llm-compiler.md)** | Planifie un **DAG** d'appels d'outils, exécute en **parallèle** les branches indépendantes. Décision (planner/joiner) par prompting, exécution par ordonnanceur déterministe (`$1`/`$2`). | 🟡 | ➕ **hors-corpus** | Kim et al., 2023, arXiv:2312.04511 |
| ~~Toolformer / PAL~~ | — | — | ➕ **absents du corpus** | Fiches : [Toolformer](concepts/hors-corpus/toolformer.md) · [PAL](concepts/hors-corpus/pal.md) |

---

## 3. RAG & gestion du contexte

| Pattern | Décodage ingénieur | Pertinence | Provenance | Source |
|---|---|---|---|---|
| **[RAG](concepts/rag.md)** (Retrieval-Augmented Generation) | Récupérer des passages externes (recherche sémantique sur embeddings) et les injecter dans le prompt pour ancrer la réponse. Base statique : une passe récup → génération. | 🟢 | ✅ (64,65,66,67,68) | fondamental, présent dans tout le corpus |
| **[RAG agentique](concepts/rag-agentique.md)** | Un agent **devant** la récupération : décide s'il faut chercher, où, reformule, itère. | 🟡 | ✅ (64,65,41) | — |
| **[Sous-types RAG agentique](concepts/sous-types-rag-agentique.md)** | **agent de routage**, **query planning** (décompose/recombine), **agents ReAct**, **plan-and-execute** (exécute tout le plan sans réinvoquer le planificateur → moins de coût/latence). | 🟡 | ✅ (64) | distinction utile et sourcée dans le texte |
| **[Semantic caching](concepts/semantic-caching.md)** | Mettre en cache requêtes/contexte/résultats par similarité sémantique. | 🟡 | ✅ (64) | mécanisme mémoire concret |
| **[Corrective RAG (cRAG)](concepts/corrective-rag.md)** | Un *grader* LLM note les passages ; si mauvais → fallback (recherche web) + réécriture de requête. | 🟡 | ✅ (68) | **Paper CRAG NON cité** par IBM (Yan et al., 2024 ➕). Outil réel cité : Tavily |
| **[Vérification de source](concepts/verification-de-source.md)** | Étape LLM qui rejette un passage récupéré s'il vient d'une source hors-périmètre (anti-contamination du contexte). | 🔴 | ✅ (68) | garde-fou rarement explicité — vraie valeur |
| **[Agentic chunking](concepts/agentic-chunking.md)** | Un LLM découpe par unité de sens + enrichit chaque chunk de métadonnées (titre/résumé). | 🟡 | ✅ (66,67) | chunking sémantique attribué à **Greg Kamradt** (66). NB : le tuto 67 le réduit à un seul prompt — bien en deçà |
| **[Stratégies de chunking](concepts/strategies-de-chunking.md)** | fixe (+overlap), récursif (`RecursiveCharacterTextSplitter`), sémantique, agentique. | 🟢 | ✅ (66) | — |
| ~~Self-RAG~~ | — | — | ➕ **absent du corpus** | Fiche : [Self-RAG](concepts/hors-corpus/self-rag.md) |

---

## 4. Mémoire

| Pattern | Décodage ingénieur | Pertinence | Provenance | Source |
|---|---|---|---|---|
| **[Court terme vs long terme](concepts/memoire-court-long-terme.md)** | CT = fenêtre de contexte/buffer circulaire. LT = store externe (vecteur, KG, RAG) relu à la demande. | 🟢 | ✅ (15,10) | — |
| **[Épisodique / sémantique / procédurale](concepts/memoire-episodique-semantique-procedurale.md)** | Traces / faits / savoir-faire. | 🟡 | ✅ (15) | **Cité** (15) : **CoALA** (*Cognitive Architectures for Language Agents*, Princeton, 2024, arXiv:2309.02427) — c'est LA source à lire, pas Generative Agents |
| **[Case-based reasoning](concepts/case-based-reasoning.md)** | Réutiliser des cas passés similaires. | 🟡 | ✅ (15) | — |
| ~~MemGPT / Generative Agents~~ | — | — | ➕ **absents du corpus** | Fiche : [MemGPT](concepts/hors-corpus/memgpt.md) (Generative Agents : non retenu) |

---

## 5. Planification

| Pattern | Décodage ingénieur | Pertinence | Provenance | Source |
|---|---|---|---|---|
| **[Goal / state / action sequencing](concepts/planification-goal-state-action.md)** | objectif → état → séquence d'actions (vocab planification classique, STRIPS-like). | 🟢 | ✅ (17,03) | — |
| **[Planification probabiliste](concepts/planification-probabiliste.md)** | Décision sous incertitude par utilité attendue (MDP). | 🟡 | ✅ (17,27) | seule voie citée pour la visibilité partielle |
| **[Decomposition-first vs interleaved](concepts/decomposition-first-vs-interleaved.md)** | Tout planifier d'abord (ReWOO) vs au fil de l'eau (ReAct). | 🟡 | ✅ (17,30) | *le* tradeoff structurant |

---

## 6. Types d'agents & architectures

| Pattern | Décodage | Pertinence | Provenance | Source |
|---|---|---|---|---|
| **[Taxonomie 5 types](concepts/taxonomie-5-types-agents.md)** (réflexe simple, réflexe-modèle, objectif, utilité, apprenant) | Manuel d'IA. Mapping LLM lâche. | 🟢 | ✅ (08,09,01,69,…) | Russell & Norvig, AIMA (➕ — jamais cité par IBM) |
| **[Agent apprenant](concepts/agent-apprenant.md)** (performance/apprentissage/critique/générateur-de-problèmes) | Modèle canonique AIMA de l'agent apprenant. | 🟢 | ✅ (14,01) | AIMA (➕) |
| **[BDI](concepts/bdi.md)** (Belief-Desire-Intention) | Architecture croyance/désir/intention, antérieure aux LLM. | 🟡 | ✅ (22) | ancrée (22) dans **Bandura, 2001**, *Social cognitive theory*, doi:10.1146/annurev.psych.52.1.1 |
| **[Vertical / horizontal / hybride](concepts/archi-vertical-horizontal-hybride.md)** | leader centralisé (point de défaillance unique) vs pairs (délibération lente) vs mixte. | 🟡 | ✅ (22,03) | + survey **Masterman et al., arXiv:2404.11584** (cité en 22) |
| **[Réactif / délibératif / cognitif](concepts/archi-reactif-deliberatif-cognitif.md)** | sans état / planifié / mémoire+apprentissage. | 🟢 | ✅ (22) | — |

---

## 7. Multi-agents, collaboration & orchestration

| Pattern | Décodage | Pertinence | Provenance | Source |
|---|---|---|---|---|
| **[Réseaux centralisés / décentralisés](concepts/reseaux-centralises-decentralises.md)** | orchestrateur unique vs pair-à-pair. | 🟡 | ✅ (25,23,13) | — |
| **[Structures : hiérarchique / holonique / coalition / équipe](concepts/structures-multi-agents.md)** | Manager→subordonnés / holons (tout-et-partie, sous-agents partagés) / regroupement temporaire autonome / rôles interdépendants. | 🟡 | ✅ (25) | vocab SMA classique ; **holonique** et **coalition** sont les seuls non évidents |
| **[Flocking / swarming](concepts/flocking-swarming.md)** | heuristiques bio-inspirées (séparation/alignement/cohésion). | 🟡 | ✅ (25) | — |
| **[Collaboration : règles / rôles / modèles](concepts/strategies-collaboration.md)** | scripté / par rôle / par raisonnement bayésien-MDP (pour l'incertitude). | 🟡 | ✅ (27) | — |
| **[Orchestration : centralisée/décentralisée/hiérarchique/fédérée](concepts/orchestration-types.md)** | la **fédérée** répond aux contraintes confidentialité/réglementaires (santé, banque). | 🟡 | ✅ (23) | seul point un peu fin |
| **[OpenAI Swarm](concepts/openai-swarm.md)** (routines + handoffs) | passation entre agents par routines. | 🟢 | ✅ (27) | — |

**Frameworks** (🟢 — implémentations, pas concepts) : [LangChain](concepts/langchain.md) (Chase, 2022), **[LangGraph](concepts/langgraph.md)** (graphe d'états — le plus sérieux pour le contrôle de flux), [CrewAI](concepts/crewai.md) (J. Moura ; rôles/tâches/process séquentiel-hiérarchique), [AutoGen](concepts/autogen-ag2.md) (**Chi Wang et al., 2024** ; fork communautaire **AG2**), [MetaGPT](concepts/metagpt-pattern.md), [ChatDev](concepts/chatdev-chatchain.md), [BeeAI](concepts/beeai.md), [LlamaIndex](concepts/llamaindex.md) (workflows événementiels), [Semantic Kernel](concepts/semantic-kernel.md), [LangFlow](concepts/langflow.md) (no-code), [AutoGPT](concepts/autogpt.md) (Toran B. Richards, 2023) & [BabyAGI](concepts/babyagi.md) (Yohei Nakajima, 2023) — démonstrateurs historiques, valeur surtout muséale.

### Les frameworks « usine logicielle » qui ont une vraie substance (🔴)
| Concept | Décodage | Provenance | Source |
|---|---|---|---|
| **[MetaGPT : communication structurée + feedback exécutable](concepts/metagpt-pattern.md)** | Les agents échangent des **documents/diagrammes schématisés** (pas du dialogue libre → moins d'hallucination), et l'agent ingénieur **exécute ses propres tests** en boucle (≤3) pour s'auto-corriger. | ✅ (56) | **Paper cité** : *MetaGPT*, arXiv:2308.00352 |
| **[ChatDev : ChatChain + CAMEL + déshallucination communicative](concepts/chatdev-chatchain.md)** | Dialogue instructeur/assistant en phases (cascade) ; l'assistant **renverse les rôles pour demander des précisions** avant de coder (réduit les hallucinations) ; repose sur le framework **CAMEL**. | 🔴 | ✅ (46,47) | dépôt OpenBMB/ChatDev |
| **[MacNet](concepts/macnet.md)** | Structure >1000 agents en DAG (ordre topologique) ; « loi d'évolutivité collaborative » (croissance logistique). | 🔴 | ✅ (46) | — |

---

## 8. Communication & protocoles d'interopérabilité

> Zone la plus « actuelle » du corpus. Le fichier **32** compare **7 protocoles** — bien plus que le trio que j'avais donné. Lire les **specs**, pas les fiches.

| Protocole | Décodage | Pertinence | Provenance | Spec citée |
|---|---|---|---|---|
| **[MCP](concepts/mcp.md)** (Model Context Protocol) | agent↔**outils**. Hôte/client/serveur, JSON-RPC 2.0, transports **stdio** & **HTTP streamable** (ex-HTTP+SSE). Primitives : Ressources (sans effet de bord) / Outils (effets de bord) / Prompts. | 🔴 | ✅ (37,38,32,33) | Anthropic, 2024 (URL `modelcontextprotocol.io` **non citée** explicitement) |
| **[A2A](concepts/a2a.md)** (Agent2Agent) | agent↔agent. Découverte via **Agent Card** (`.well-known/agent-card.json`) → auth → JSON-RPC/HTTPS + SSE/webhooks. Agents « opaques ». | 🟡 | ✅ (35,36,32) | **a2aproject.github.io/A2A** (Google→Linux Foundation) |
| **[ACP](concepts/acp.md)** (Agent Communication Protocol) | agent↔agent, **REST/HTTP** léger (vs JSON-RPC), async, découverte hors-ligne (scale-to-zero). | 🟡 | ✅ (33,34,32) | **agentcommunicationprotocol.dev** (BeeAI/IBM). A **fusionné avec A2A** sous la Linux Foundation (36) |
| **[ANP / AG-UI / Agora / LMOS](concepts/autres-protocoles.md)** | P2P+W3C DID / event-driven UI / **négociation de protocole en langage naturel** / Internet of Agents (Eclipse). | 🟡 | ✅ (32) | agent-network-protocol.com, docs.ag-ui.com, agoraprotocol.org, eclipse.dev/lmos |
| **[KQML / FIPA-ACL](concepts/kqml-fipa-acl.md)** | ACL historiques (DARPA, années 90) — référents que beaucoup ignorent. | 🟡 | ✅ (13,47) | Labrou et al., U. Maryland, 1999 (cité en 13) |
| **[DroidSpeak](concepts/droidspeak.md)** | Partage de **cache KV** entre LLM pour accélérer la comm inter-agents (perte de précision minimale). | 🔴 | ✅ (13) | Liu et al., UChicago/Microsoft, déc. 2024 (cité par titre) |

> Argument concret (33) : pourquoi MCP est inadapté au multi-agent (pas de streaming delta,
> pas de mémoire partagée multi-serveurs, ne contraint pas le schéma de message). Utile.

---

## 9. Production : éval, ops, sécurité, gouvernance

> **La vraie zone de profondeur pour un senior.** Confirmé par la lecture intégrale.

| Pattern | Décodage | Pertinence | Provenance | Source |
|---|---|---|---|---|
| **[Évaluation de trajectoire](concepts/evaluation-trajectoire.md)** | Évaluer la **suite de décisions/appels**, pas seulement la réponse finale. | 🔴 | ✅ (60) | — |
| **[Taxonomie d'erreurs d'appel de fonction](concepts/taxonomie-erreurs-appel-fonction.md)** | Règles (nom incorrect, paramètre manquant, type erroné, valeur hors-ensemble, **paramètre halluciné**) **+** LLM-judge sémantique (**ancrage de la valeur de paramètre**, **conversion d'unités**). | 🔴 | ✅ (60) | la pépite opérationnelle du corpus |
| **[LLM-as-a-judge](concepts/llm-as-a-judge.md)** | Noter les sorties avec un LLM + rubrique. | 🟡 | ✅ (60,61) | à calibrer (biais auto-préférence/position) |
| **[AgentOps](concepts/agentops.md)** | Observabilité/tracing **session→trace→span**, coût & latence par étape, routage multi-LLM. | 🔴 | ✅ (07) | bâti sur **OpenTelemetry (OTEL)** ; cite Adam Silverman (Agency AI), EU AI Act |
| **[HITL statique vs dynamique](concepts/hitl-statique-dynamique.md)** | breakpoints `interrupt_before/after` (reprise `update_state`) vs fonction `interrupt()` (reprise `Command(resume=)`). | 🟡 | ✅ (63) | pattern LangGraph concret et réutilisable |
| **[Guardrail en nœud d'entrée](concepts/guardrail-noeud-entree.md)** | Détecteur de modération (**Granite Guardian** HAP/PII) placé **en amont** du LLM via arête conditionnelle. | 🟡 | ✅ (54,63) | tutoriels SQL/brevets |

**[Sécurité agentique](concepts/securite-agentique.md)** (🔴 — surface réellement nouvelle, fichier 62 ; proche d'OWASP sans le citer) :
- **Injection de prompt** directe **et indirecte** (cachée dans une source récupérée ; vecteur multimodal).
- **Empoisonnement de mémoire** (≠ empoisonnement des données d'entraînement).
- **Slopsquatting** : exploiter les **hallucinations de noms de bibliothèques** d'un agent codeur → attaque supply-chain. *(terme à connaître)*
- Manipulation d'outils/API, compromission de privilège, mouvement latéral, **RCE**, échecs en cascade / DDoS via agent.
- Contre-mesures : Zero Trust, moindre privilège (RBAC/ABAC), sandbox, durcissement & validation des prompts (entrée **et** sortie).

**[Éthique & gouvernance](concepts/ethique-gouvernance.md)** (fichier 59 — le plus dense et sourcé du corpus) :
- **Alignment Studio** : aligner un LLM sur des **documents de politique en langage naturel** (qu'il *adopte* le comportement, pas juste le vocabulaire). *Source : IEEE Internet Computing, 09/2024 ; Kush Varshney, IBM.*
- **Collaboration contradictoire** : l'humain garde la décision, l'IA interroge/affine — **inversion** du schéma habituel, cadrée comme question de dignité.
- **RADAR** : apprentissage contradictoire entre deux LLM (détection de texte généré). *HKCU + IBM Research.*
- **Granite Guardian 3.1** : détecte les **hallucinations d'appel de fonction**.
- Sources externes réelles citées : Bostrom (optimiseur de trombones), rapport DHS 04/2024, rapport DeepMind 04/2024.
- **Gouvernance** (58) : agents de gouvernance (moniteurs d'autres agents), sandbox éthique, **kill switch**, endiguement — pistes, peu détaillées.

---

## Compléments hors-corpus (état de l'art)

**38 patterns absents du guide IBM**, ajoutés depuis l'état de l'art (index : [`concepts/hors-corpus/`](concepts/hors-corpus/README.md)). Sourcés depuis la littérature, identifiants arXiv à vérifier.

- **Patterns initiaux (1er lot)** — [Toolformer](concepts/hors-corpus/toolformer.md) 🔴 · [MemGPT (Letta)](concepts/hors-corpus/memgpt.md) 🔴 · [Self-RAG](concepts/hors-corpus/self-rag.md) 🔴 · [PAL (Program-Aided LM)](concepts/hors-corpus/pal.md) 🟡 · [MRKL Systems](concepts/hors-corpus/mrkl.md) 🟡 · [LLM Compiler](concepts/hors-corpus/llm-compiler.md) 🟡 · [Multi-agent debate / Society of Mind](concepts/hors-corpus/society-of-mind-debate.md) 🔴
- **Raisonnement & prompting** — [Self-Consistency](concepts/hors-corpus/self-consistency.md) 🟡 · [Self-Refine](concepts/hors-corpus/self-refine.md) 🟡 · [Chain-of-Verification (CoVe)](concepts/hors-corpus/chain-of-verification.md) 🟡 · [Least-to-Most prompting](concepts/hors-corpus/least-to-most.md) 🟡 · [Step-Back prompting](concepts/hors-corpus/step-back.md) 🟡 · [Graph of Thoughts (GoT)](concepts/hors-corpus/graph-of-thoughts.md) 🔴
- **Modèles de raisonnement & test-time compute** — [Modèles de raisonnement & test-time compute](concepts/hors-corpus/inference-time-scaling.md) 🔴 · [Process Reward Models (PRM)](concepts/hors-corpus/process-reward-models.md) 🔴
- **Conception d'agents moderne** — [CodeAct (le code comme action)](concepts/hors-corpus/codeact.md) 🔴 · [Computer-use & agents GUI](concepts/hors-corpus/computer-use-gui-agents.md) 🔴 · [Voyager & bibliothèque de compétences](concepts/hors-corpus/voyager-skill-library.md) 🔴 · [Tool retrieval (RAG sur les outils)](concepts/hors-corpus/tool-retrieval.md) 🟡
- **RAG avancé** — [HyDE](concepts/hors-corpus/hyde.md) 🟡 · [GraphRAG](concepts/hors-corpus/graphrag.md) 🔴 · [RAPTOR](concepts/hors-corpus/raptor.md) 🟡 · [Reranking (cross-encoders)](concepts/hors-corpus/reranking.md) 🟡 · [Contextual Retrieval](concepts/hors-corpus/contextual-retrieval.md) 🟡
- **Sécurité — défense** — [La « lethal trifecta »](concepts/hors-corpus/lethal-trifecta.md) 🔴 · [Dual-LLM pattern & CaMeL](concepts/hors-corpus/dual-llm-camel.md) 🔴 · [Spotlighting](concepts/hors-corpus/spotlighting.md) 🟡 · [OWASP Top 10 LLM & menaces agentiques](concepts/hors-corpus/owasp-llm-agentic.md) 🟡
- **Efficacité & coût** — [Routage & cascades de modèles](concepts/hors-corpus/model-routing-cascades.md) 🟡 · [Décodage contraint / sortie structurée](concepts/hors-corpus/constrained-decoding.md) 🟡 · [Prompt caching](concepts/hors-corpus/prompt-caching.md) 🟡 · [Speculative decoding](concepts/hors-corpus/speculative-decoding.md) 🟡
- **Multi-agents — compléments** — [Mixture-of-Agents (MoA)](concepts/hors-corpus/mixture-of-agents.md) 🔴 · [Superviseur & équipes hiérarchiques](concepts/hors-corpus/supervisor-hierarchical-teams.md) 🟡 · [Architecture blackboard](concepts/hors-corpus/blackboard-architecture.md) 🟡
- **Mémoire & alignement — compléments** — [Generative Agents — memory stream](concepts/hors-corpus/generative-agents-memory-stream.md) 🔴 · [Mémoire à base d'entités / graphe](concepts/hors-corpus/entity-memory.md) 🟡 · [Constitutional AI & RLAIF](concepts/hors-corpus/constitutional-ai-rlaif.md) 🔴

---
## Verdict d'usage (confirmé par la lecture intégrale)

**~65-70 % du corpus = un nom sur une idée que tu maîtrises.** La substance réelle se concentre sur :

- 🔴 **À lire vraiment** : fichier **18** (raisonnement, comparatif sourcé ReAct/ReWOO/LATS), **32** (paysage des 7 protocoles), **59** (éthique : Alignment Studio, collaboration contradictoire), **60** (taxonomie d'erreurs d'appel de fonction), **62** (sécurité/slopsquatting), **07** (AgentOps/OTEL), **56** (MetaGPT). Tutoriels à valeur architecturale : **54** (guardrail en nœud), **63** (HITL statique/dynamique), **68** (vérification de source cRAG).
- 🟡 **À survoler** : RAG agentique (64), mémoire/CoALA (15), structures multi-agents (25), ChatDev (46).
- 🟢 **À ignorer** : types AIMA, composants, frameworks descriptifs, cas d'usage sectoriels (71-76, interchangeables sauf 72/74).

**Sources primaires à privilégier** (réellement ancrées) : ReWOO (arXiv:2305.18323), ReAct (arXiv:2210.03629), LATS, MetaGPT (arXiv:2308.00352), CoALA (arXiv:2309.02427), survey Masterman (arXiv:2404.11584), et les **specs** MCP / A2A / ACP. Vérifie les identifiants arXiv avant de citer.
