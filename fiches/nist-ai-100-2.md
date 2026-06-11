---
titre: "NIST AI 100-2 : taxonomie de l'adversarial ML"
type: "Concept"
theme: securite
niveau: 🔴
source_url: https://csrc.nist.gov/pubs/ai/100/2/e2025/final
---

# NIST AI 100-2 : taxonomie de l'adversarial ML

**En une phrase** — La taxonomie officielle américaine de l'*adversarial machine learning*, qui distingue IA prédictive et IA générative et classe les attaques (évasion, empoisonnement, atteintes à la vie privée, prompt injection directe/indirecte) selon cinq axes.

## Ce que dit la source

Le rapport *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations* (NIST Trustworthy and Responsible AI) propose une **taxonomie et une terminologie communes** de l'AML, hiérarchisées par types de méthodes ML, étapes du cycle de vie, et objectifs/capacités/connaissances de l'attaquant (abstract verbatim de la page CSRC).

Le rapport **classe chaque attaque selon cinq axes** (texte verbatim de l'Executive Summary) : (i) le **type de système IA**, (ii) l'**étape du cycle de vie ML** où l'attaque est montée, (iii) les **buts et objectifs de l'attaquant** (propriétés du système qu'il cherche à violer), (iv) les **capacités et l'accès** de l'attaquant, (v) la **connaissance** qu'il a du processus d'apprentissage.

Structure de la taxonomie (table des matières verbatim du PDF) :

**2. Predictive AI (PredAI) Taxonomy**
- 2.1 Classification : stages of learning ; attacker goals & objectives ; capabilities ; knowledge ; data modality.
- 2.2 **Evasion Attacks** — white-box, black-box, transferability, real world, mitigations.
- 2.3 **Poisoning Attacks** — availability poisoning, targeted, backdoor, **model poisoning**, real world.
- 2.4 **Privacy Attacks** — data reconstruction, membership inference, property inference, model extraction.

**3. Generative AI (GenAI) Taxonomy**
- 3.1 Classification : GenAI stages of learning ; attacker goals & objectives ; capabilities.
- 3.2 **Supply Chain Attacks** — data poisoning, model poisoning.
- 3.3 **Direct Prompting Attacks** — techniques d'attaque, **information extraction**, mitigations.
- 3.4 **Indirect Prompt Injection Attacks** — availability, integrity, **privacy compromise**, mitigations.
- 3.5 **Security of Agents**.
- 3.6 Benchmarks for AML Vulnerabilities.

**4. Key Challenges and Discussion** — dont les arbitrages entre attributs de l'IA digne de confiance (*trade-offs between the attributes of Trustworthy AI*).

> Distinction structurante (Executive Summary, verbatim) : la taxonomie sépare **systèmes prédictifs** et **génératifs**, et considère les composants du système IA (données, modèle, processus d'entraînement/test/déploiement, contexte logiciel) — notamment les cas où un modèle GenAI a accès à des **données privées** ou est **équipé d'outils agissant sur le monde réel**.
>
> Sur les axes de connaissance de l'attaquant, le rapport emploie **white-box**, **black-box** et **gray-box** *(présence confirmée dans le texte ; détail de chaque définition à vérifier dans le corps du rapport)*. Le report s'appuie sur le **NIST AI Risk Management Framework** pour les notions de sécurité, résilience et robustesse, sans recommander de seuil de tolérance au risque.

## Exemple
Le rapport ancre la taxonomie dans des cas réels. Côté évasion GenAI, il cite l'**attaque ASCII-art** : une illustration ASCII d'un terme interdit fait produire au chatbot l'information nuisible alors qu'il censurerait correctement le mot en clair — « la distance sémantique entre les deux prompts est exactement nulle ». Côté empoisonnement réel, il documente **Tay.AI** (chatbot Microsoft empoisonné en moins de 24 h en 2016 via l'apprentissage en ligne), les campagnes de millions d'e-mails contre le filtre anti-spam de Gmail, et un incident sur VirusTotal (variantes d'un ransomware soumises pour fausser sa classification).

## Pourquoi c'est utile

C'est le **rapport de référence officiel** pour la sécurité de l'IA adversariale. Il fournit la grille fine : évasion vs empoisonnement vs privacy pour le prédictif, et — côté génératif, le plus pertinent pour les agents — la séparation nette entre **direct prompting** et **indirect prompt injection**, plus une section dédiée **Security of Agents**. Vocabulaire normatif et aligné sur l'AI RMF.

## Points clés

- Deux familles : **PredAI** et **GenAI**, chacune avec sa taxonomie.
- 5 axes de classification : type de système, étape du cycle, buts, capacités, connaissance.
- PredAI : **évasion**, **empoisonnement** (disponibilité / ciblé / backdoor / modèle), **privacy** (reconstruction, membership/property inference, extraction de modèle).
- GenAI : **supply chain**, **direct prompting**, **indirect prompt injection** (availability / integrity / privacy), **Security of Agents**, benchmarks.
- Adossé au **NIST AI Risk Management Framework** ; pas de prescription de tolérance au risque.

## Voir aussi

- [Injection de prompt](prompt-injection.md)
- [Injection : pourquoi c'est grave](injection-pourquoi-cest-grave.md)
- [OWASP Top 10 LLM](owasp-llm-top-10.md) · [MITRE ATLAS](mitre-atlas.md)
- Lien officiel : <https://csrc.nist.gov/pubs/ai/100/2/e2025/final> · DOI : <https://doi.org/10.6028/NIST.AI.100-2e2025>
