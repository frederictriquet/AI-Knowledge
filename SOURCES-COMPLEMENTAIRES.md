# Sources complémentaires — backlog d'enrichissement

But : construire une couche **profonde et sourcée** au-dessus des bases IBM, pour corriger leurs deux
faiblesses (profondeur plafonnée, sourcing faible/non résolu). Ce document est un **backlog de
travail** : on y pioche une source, on en extrait du contenu, on crée/complète des fiches.

Bases existantes à enrichir :
- `ibm-guide-agents-ia/` — glossaire + `concepts/` (63 corpus + 38 hors-corpus).
- `ibm-guide-prompt-engineering/` — glossaire + `concepts/` (22 fiches).

**Critère de qualité** (pour entrer ici) : primaire ou vérifiable · documente modes d'échec/tradeoffs
mesurés · biais commercial faible ou transparent · à jour.

## État d'avancement (vague parallèle)

**Traité ☑ (8 bases sources, ~200 fiches/docs, 0 lien cassé)** : Lilian Weng · The Prompt Report ·
Anthropic Building Effective Agents · Hamel Husain (éval) · Simon Willison (sécurité) ·
Frontier reasoning (DeepSeek-R1 + Let's Verify) · Security references (OWASP / NIST AI 100-2 / MITRE ATLAS) ·
Benchmarks (SWE-bench, τ-bench, GAIA, WebArena) · DSPy (papier) · **Embrace The Red** (sécurité, PoC) · **Eugene Yan** (patterns produit/éval) · **Jason Liu** (RAG mesurable, sorties structurées).
Plus **`sources/SOURCES-PRIMAIRES.md`** : 30/30 identifiants arXiv vérifiés (✅, 0 incohérence) —
la source primaire derrière chaque fiche, corrigeant les `[n]` orphelins d'IBM.

**Partiel** : « Let's Verify Step by Step », SWE-bench, τ-bench, GAIA = abstract seul (pas de HTML arXiv).

**Différé (valeur marginale ou non auto-extractable)** : OpenAI Practical Guide & learnprompting & docs
frameworks & specs MCP/A2A/ACP (recouvrent des fiches existantes ; protocoles déjà cartographiés) ·
HELM/LMArena/MTEB & outils d'éval (Ragas/Inspect) · OpenAI Practical Guide · learnprompting · Latent Space ·
Tier 2 non auto-extractables (Chip Huyen *livre*, Karpathy *vidéos*, DeepLearning.AI *cours*).

---

## Conventions
- **Priorité** : `P1` (à faire en premier, levier max) · `P2` (solide) · `P3` (généraliste/optionnel).
- **Statut** : ☐ à traiter · ◐ en cours · ☑ traité.
- **Renforce** : concepts/fiches existants que la source approfondit (référence de planification — on
  ne modifie pas encore les fiches).
- **Ingestion** : voir §« Méthodes d'ingestion par type » plus bas (le pipeline IBM ne s'applique pas
  tel quel hors IBM).

---

## Tier 1 — indispensables (P1)

| ☐ | Source | Type | Apport vs IBM | Renforce |
|---|---|---|---|---|
| ☑ | **Lilian Weng — lilianweng.github.io** (« LLM Powered Autonomous Agents » ; « Prompt Engineering » ; « Adversarial Attacks on LLMs » ; « Why We Think ») | blog long-form sourcé | la version *profonde + citée* de ce qu'IBM survole | agents (composants, mémoire, planification, ReAct), prompting (CoT, ToT) — **traité : 4 posts + 8 fiches, voir `sources/lilian-weng/`** |
| ☑ | **Anthropic — « Building Effective Agents »** (+ docs Claude : prompt eng., Contextual Retrieval, agent SDK) | doc praticien | anti-hype ; distingue *workflows* vs *agents* ; contrepoids au cadrage commercial | orchestration, multi-agents, RAG (contextual-retrieval hors-corpus), prompt-engineering — **traité : post + 4 fiches, voir `sources/anthropic-effective-agents/`** |
| ☑ | **The Prompt Report — Schulhoff et al., 2024** (arXiv:2406.06608) | survey académique | taxonomie systématique 58 techniques, sourcée (IBM cite déjà Schulhoff) | toute la base prompting, techniques-catalogue — **traité : papier + taxonomie + 7 fiches, voir `sources/prompt-report/`** |
| ☑ | **Simon Willison — simonwillison.net** (prompt injection, lethal trifecta, tooling) | blog praticien | sécurité LLM rigoureuse ; source réelle de plusieurs fiches hors-corpus | prompt-injection, prevent-prompt-injection, lethal-trifecta, dual-llm-camel — **traité : 3 posts + 3 fiches, voir `sources/simon-willison/`** |

## Par domaine

### Agents (P1–P2)
| ☐ | Source | Type | Apport | Renforce |
|---|---|---|---|---|
| ☐ | **OpenAI — A Practical Guide to Building Agents** | doc praticien | vue OpenAI, patterns d'orchestration | orchestration-types, supervisor-hierarchical-teams |
| ☑ | **Masterman et al. — Survey of Emerging AI Agent Architectures** (arXiv:2404.11584) | survey | déjà cité par IBM ; archis raisonnement/planif/outils | bdi, archi-*, react, rewoo |
| ☑ | **Papiers primaires agents** : ReAct (2210.03629), Reflexion (2303.11366), ReWOO (2305.18323), Voyager (2305.16291), Generative Agents (2304.03442), MemGPT (2310.08560) — *IDs à vérifier* | papiers arXiv | la substance + benchmarks derrière les fiches | react, reflexion, rewoo, voyager-skill-library, generative-agents-memory-stream, memgpt |

### Prompting (P1–P2)
| ☐ | Source | Type | Apport | Renforce |
|---|---|---|---|---|
| ☑ | **DSPy — docs officielles (Stanford NLP)** + github.com/stanfordnlp/dspy | docs + repo | source réelle ; remplace la description IBM | dspy, prompt-optimization |
| ☐ | **learnprompting.org** | guide communautaire | catalogue rigoureux, lié au Prompt Report | techniques-catalogue, few/zero-shot |
| ☑ | **Papiers primaires prompting** : ToT (2305.10601), CoT (2201.11903), Self-Consistency (2203.11171), DSP (Directional Stimulus), Prompt Tuning (Lester et al. 2021) — *à vérifier* | papiers arXiv | benchmarks + limites (ex. limite expressive du prompt tuning) | tree-of-thoughts, chain-of-thought, self-consistency, directional-stimulus-prompting, prompt-tuning |

### Sécurité (P1)
| ☐ | Source | Type | Apport | Renforce |
|---|---|---|---|---|
| ☑ | **OWASP Top 10 for LLM Applications** + **OWASP Agentic AI – Threats & Mitigations** | référentiel | le standard qu'IBM imite sans citer | securite-agentique, owasp-llm-agentic, prompt-injection |
| ☑ | **NIST AI 100-2 — Adversarial Machine Learning** | rapport officiel | le rapport qu'IBM résume (taxonomie complète) | prompt-injection, prevent-prompt-injection |
| ☑ | **MITRE ATLAS** (atlas.mitre.org) | matrice de menaces | tactiques/techniques adversariales structurées | securite-agentique, jailbreak |
| ☑ | **Embrace The Red — Johann Rehberger** (embracethered.com) | blog recherche | injection indirecte, exfiltration, PoC concrets | prompt-injection, lethal-trifecta — **traité : 3 posts + 3 fiches, `sources/embrace-the-red/`** |

### Évaluation (P1 — le plus rentable, angle mort IBM)
| ☐ | Source | Type | Apport | Renforce |
|---|---|---|---|---|
| ☑ | **Hamel Husain — hamel.dev** (« Your AI Product Needs Evals » + « A Field Guide… » + « LLM-as-a-Judge ») | blog praticien | méthodo d'éval de bout en bout (error analysis, eval-driven dev, LLM-as-judge rigoureux) | evaluation-trajectoire, llm-as-a-judge, taxonomie-erreurs-appel-fonction — **traité : 3 posts + 4 fiches, voir `sources/hamel-husain/`** |
| ☑ | **Benchmarks agents** : SWE-bench, τ-bench (tau-bench), GAIA, WebArena | benchmarks + papiers | mesure réelle des agents | evaluation-trajectoire, computer-use-gui-agents |
| ☐ | **HELM (Stanford CRFM)**, **LMArena/Chatbot Arena**, **MTEB** (retrieval) | classements/outils | évaluation comparative rigoureuse | llm-as-a-judge, reranking, rag-* |
| ☐ | **Outils d'éval** : Ragas (RAG), Inspect (UK AISI), Braintrust, DeepEval | docs/repos | éval outillée reproductible | evaluation, rag-agentique |

### Frameworks & specs (P2 — remplacer descriptions/legacy IBM)
| ☐ | Source | Type | Apport | Renforce |
|---|---|---|---|---|
| ☐ | **LangGraph / CrewAI / LlamaIndex — docs officielles** | docs | API courante (vs LangChain legacy d'IBM) | langgraph, crewai, llamaindex, prompt-chaining |
| ☐ | **Spec MCP** (modelcontextprotocol.io) · **A2A** (a2aproject.github.io) · **ACP** (agentcommunicationprotocol.dev) | specs | la source des fiches protocoles | mcp, a2a, acp, autres-protocoles |
| ☐ | **API docs Anthropic / OpenAI** (prompt caching, structured output, tool use) | docs | clarifie KV-cache vs response-cache, JSON mode | prompt-caching, constrained-decoding, tool-calling |

### Frontière — modèles de raisonnement (P1 — angle mort majeur d'IBM)
| ☐ | Source | Type | Apport | Renforce |
|---|---|---|---|---|
| ☑ | **DeepSeek-R1** (arXiv:2501.12948) + **o1 system card** | papier + rapport | RL de raisonnement, test-time compute | inference-time-scaling, process-reward-models |
| ☑ | **« Let's Verify Step by Step »** — Lightman et al. (2305.20050) | papier | process reward models | process-reward-models |
| ☐ | **Blogs recherche** : Anthropic / OpenAI / Google DeepMind | blogs labos | frontière, peu de biais commercial | divers 🔴 |

## Tier 2 — solides, généralistes (P2–P3)
| ☐ | Source | Type | Apport |
|---|---|---|---|
| ☐ | **Chip Huyen — *AI Engineering*** (livre) | livre | pendant système/rigoureux des sujets IBM |
| ☑ | **Eugene Yan — eugeneyan.com** | blog | patterns ML/LLM en production |
| ☑ | **Jason Liu — instructor** (structured output) | docs/repo | sorties structurées, vue praticien |
| ☐ | **Latent Space** (podcast/newsletter) | média | interviews praticiens haute densité |
| ☐ | **Karpathy** (« Zero to Hero », « Intro to LLMs ») | vidéos | internals des LLM (jamais couvert par IBM) |
| ☐ | **DeepLearning.AI** short courses | cours | structuré sur agents/RAG/DSPy/evals |

---

## Méthodes d'ingestion par type

Le pipeline IBM (`extract.py`, sélecteur `body-article-8`) **ne s'applique pas tel quel** hors IBM.
Approche par type :

- **Blog HTML** (Weng, Willison, Yan, Hamel, Embrace The Red) → `curl` + conversion. **Outil prêt :
  `sources/extract_generic.py`** (bs4+lxml+pandoc) — cible `.post-content`/`article`/`main`,
  absolutise liens & images, supprime les ancres de titres, convertit `<img>`/`<a>` bruts, et
  **préserve la section References** (le sourcing recherché). Validé sur Lilian Weng (Hugo/PaperMod).
  Pour un autre thème, ajuster le sélecteur de contenu. Risque : structures hétérogènes → vérifier.
- **Papier arXiv** → **préférer la version HTML** `arxiv.org/html/<id>` (LaTeXML, propre) et la passer
  à `sources/extract_generic.py` avec `selector="article"` + base URL à slash final (pour les images).
  Validé sur The Prompt Report (41k mots, références préservées). Fallback : `ar5iv.labs.arxiv.org/html/<id>`,
  ou le PDF (`arxiv.org/pdf/<id>`) lu directement / `pdftotext`. Pour un survey, le cœur de valeur est
  la **taxonomie** : en faire un document de référence dédié + des fiches par famille. Ne pas se fier
  au seul abstract.
- **Docs framework / spec** (LangGraph, DSPy, MCP, API) → souvent versionnées ; cibler les pages
  conceptuelles + exemples. Pour les libs, **context7 MCP** peut fournir la doc à jour.
- **Repo GitHub** (DSPy, ColBERT, benchmarks) → lire README + exemples ; extraire les conventions
  d'API réelles (corrige le « legacy » d'IBM).
- **Référentiels** (OWASP, NIST, MITRE ATLAS) → documents structurés (HTML/PDF) ; mapper leur
  taxonomie sur les fiches sécurité existantes.
- **Livre / vidéo / cours** → **pas d'extraction automatique** ; notes manuelles ciblées, à consigner
  comme fiches `synthèse` plutôt que `extraction`.

## Conventions de sortie (à décider au lancement)
- Nouvelle base par source majeure (ex. `sources/lilian-weng/`) **ou** fiches directement dans une
  base `concepts/` thématique transverse — à trancher selon le volume.
- Réutiliser le gabarit de fiche (En une phrase / Ce que dit la source / Tradeoff / Source primaire /
  Voir aussi) + tags 🟢/🟡/🔴 et provenance.
- **Quand une source approfondit une fiche IBM existante** : créer la fiche enrichie et y lier la
  fiche IBM (cross-link), sans écraser l'original (traçabilité de provenance).

## Ordre recommandé pour démarrer
1. **Lilian Weng** (agents + prompting d'un coup, profond + sourcé) — P1, levier max.
2. **The Prompt Report** (upgrade rigoureux de toute la base prompting) — P1.
3. **Anthropic « Building Effective Agents »** (recadrage workflows/agents) — P1.
4. **Bloc sécurité** : Willison + OWASP + NIST + ATLAS — P1, comble la profondeur défensive.
5. **Bloc éval** : Hamel + benchmarks — P1, l'angle mort le plus rentable.
6. **Frontière** : DeepSeek-R1 + test-time compute — P1, comble le retard « pré-reasoning-models ».
