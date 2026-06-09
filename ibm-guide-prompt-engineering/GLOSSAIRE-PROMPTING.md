# Glossaire des techniques de prompting — carte pour ingénieur confirmé

Décodage du guide IBM « Guide 2026 du prompt engineering » en langage d'ingénieur, réconcilié avec
une **lecture intégrale des 25 articles**. Chaque entrée pointe vers sa fiche détaillée
(`concepts/`) et, le cas échéant, vers la **base sœur « agents IA »** (concept commun).

**Tags de pertinence** — 🟢 pur-nom (tu l'appliques déjà) · 🟡 tradeoff (compromis non évident) ·
🔴 substance (à lire). **Provenance** : ✅ présent dans le corpus IBM (n° de fichier).

> 🔗 Base compagne : [glossaire « agents IA »](../ibm-guide-agents-ia/GLOSSAIRE-PATTERNS.md).
> Plusieurs concepts sont communs aux deux (CoT, ToT, self-consistency, injection/jailbreak, caching).

---

## 1. Fondamentaux & comparaison

| Concept | Décodage | Pertinence | Source corpus |
|---|---|---|---|
| [Qu'est-ce que le prompt engineering](concepts/prompt-engineering.md) | la discipline de conception d'instructions textuelles. | 🟢 ✅ | 01 |
| [Catalogue des techniques](concepts/techniques-catalogue.md) | index des ~18 techniques (zero/few-shot, CoT, ToT, ART, ReAct, DSP…). | 🟢 ✅ | 02 |
| [RAG vs fine-tuning vs prompt engineering](concepts/rag-vs-fine-tuning-vs-prompt-engineering.md) | 3 leviers complémentaires (coût/contrôle/fraîcheur). | 🟡 ✅ | 03 |

## 2. Apprentissage en contexte (« shots »)

| Concept | Décodage | Pertinence | Source |
|---|---|---|---|
| [Zero-shot](concepts/zero-shot-prompting.md) | tâche sans exemple ; peut surpasser few-shot avec une meilleure structure (Reynolds & McDonell 2021). | 🟢 ✅ | 08 |
| [One-shot](concepts/one-shot-prompting.md) | un seul exemple ; l'article penche surtout vers la vision. | 🟢 ✅ | 09 |
| [Few-shot](concepts/few-shot-prompting.md) | quelques exemples ; sélection sémantique via RAG. | 🟢 ✅ | 10 |
| [In-context learning (ICL)](concepts/in-context-learning.md) | apprendre depuis les démos, **poids gelés** ; cadrages bayésien & descente de gradient implicite. | 🔴 ✅ | 23 |

## 3. Raisonnement & structuration du prompt

| Concept | Décodage | Pertinence | Source / cross-link |
|---|---|---|---|
| [Chain-of-Thought (CoT)](concepts/chain-of-thought.md) | « écris ton raisonnement avant la réponse ». | 🟢 ✅ | 20 · [base agents](../ibm-guide-agents-ia/concepts/chain-of-thought.md) |
| [Self-Consistency](concepts/self-consistency.md) | plusieurs CoT + vote majoritaire (« cohérence propre »). | 🟡 ✅ | 02/06/20 · [base agents (hors-corpus)](../ibm-guide-agents-ia/concepts/hors-corpus/self-consistency.md) |
| [Tree of Thoughts (ToT)](concepts/tree-of-thoughts.md) | CoT en arbre + recherche ; critique d'efficacité, *Thought of Search*. | 🔴 ✅ | 06 · [base agents](../ibm-guide-agents-ia/concepts/tree-of-thoughts.md) |
| [Méta-prompting](concepts/meta-prompting.md) | template réutilisable par classe de tâches (fondement catégoriel). | 🟡 ✅ | 07 |
| [Prompt chaining](concepts/prompt-chaining.md) | décomposer en chaîne de prompts simples (9 sous-types). | 🟡 ✅ | 04/05 · [ReWOO (agents)](../ibm-guide-agents-ia/concepts/rewoo.md) |
| [Directional Stimulus Prompting (DSP)](concepts/directional-stimulus-prompting.md) | un **petit policy model** (SFT+RL) génère des stimuli pour piloter un LLM gelé. | 🔴 ✅ | 21 |
| [Role prompting](concepts/role-prompting.md) | assigner un persona dans le prompt système. | 🟢 ✅ | 22 |

## 4. Optimisation & programmation des prompts

| Concept | Décodage | Pertinence | Source |
|---|---|---|---|
| [Optimisation des prompts](concepts/prompt-optimization.md) | amélioration automatique par feedback/métaprompts (CFPO, PROMST). | 🟡 ✅ | 16 |
| [DSPy](concepts/dspy.md) | « programmer, pas prompter » : signatures + optimiseurs qui **compilent** les prompts. | 🔴 ✅ | 17/18 |

## 5. Réglage & efficacité

| Concept | Décodage | Pertinence | Source / cross-link |
|---|---|---|---|
| [Prompt tuning (soft prompts)](concepts/prompt-tuning.md) | PEFT : vecteurs continus entraînés, backbone gelé. **≠ prompt engineering textuel** ; limite expressive vs LoRA. | 🔴 ✅ | 24/25 |
| [Prompt caching](concepts/prompt-caching.md) | ⚠️ le tuto fait du **cache de réponses** exact-match, pas du KV-cache de préfixe. | 🟡 ✅ | 19 · [agents : prompt-caching](../ibm-guide-agents-ia/concepts/hors-corpus/prompt-caching.md) · [semantic-caching](../ibm-guide-agents-ia/concepts/semantic-caching.md) |

## 6. Sécurité du prompt

| Concept | Décodage | Pertinence | Source / cross-link |
|---|---|---|---|
| [Injection de prompt](concepts/prompt-injection.md) | exécution d'instructions malveillantes (directe/indirecte) ; irréductible (même type de données). | 🔴 ✅ | 11/13 · [sécurité agentique](../ibm-guide-agents-ia/concepts/securite-agentique.md) · [lethal trifecta](../ibm-guide-agents-ia/concepts/hors-corpus/lethal-trifecta.md) |
| [Prévenir l'injection](concepts/prevent-prompt-injection.md) | catalogue de défenses, aucune complète. | 🔴 ✅ | 12 · [spotlighting](../ibm-guide-agents-ia/concepts/hors-corpus/spotlighting.md) · [dual-LLM/CaMeL](../ibm-guide-agents-ia/concepts/hors-corpus/dual-llm-camel.md) |
| [Jailbreak](concepts/jailbreak.md) | contourner l'alignement (Crescendo, Deceptive Delight, many-shot). | 🔴 ✅ | 14 |
| [Skeleton Key & multi-tours](concepts/skeleton-key.md) | technique Microsoft multi-interactions ; la menace **single-shot** reste prioritaire (Chenta Lee, IBM). | 🔴 ✅ | 15 |

---

## Verdict d'usage (pour un senior)

- 🔴 **À lire** : ICL (23, cadrages théoriques), ToT (06, seule vraie biblio + *Thought of Search*),
  DSP (21, policy-model SFT+RL), DSPy (17/18), prompt tuning (25, **limite expressive**),
  et le bloc sécurité (11–15 : chronologie, irréductibilité, jailbreaks multi-tours).
- 🟡 **À survoler** : prompt chaining, méta-prompting, self-consistency, optimisation, comparatif RAG/FT/PE.
- 🟢 **À ignorer** : définitions, zero/one/few-shot, role prompting, catalogue.

**Distinction clé du corpus** : ne pas confondre **prompt engineering** (texte) et **prompt tuning**
(soft prompts entraînés, PEFT) — ce sont deux familles différentes.

**Sources réellement ancrées** (rares) : ToT (Yao et al., arXiv:2305.10601 ; Katz et al., NeurIPS 2024),
ICL (GPT-3, *Language Models are Few-Shot Learners*), DSPy (github.com/stanfordnlp/dspy), NIST
*Adversarial Machine Learning*, et la chronologie d'injection (Goodside, Willison, Greshake et al. 2023).
Le reste du corpus porte des renvois `[n]` **non résolus**. Vérifier tout identifiant avant citation.
