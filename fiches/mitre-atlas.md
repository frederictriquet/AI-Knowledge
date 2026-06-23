---
titre: "MITRE ATLAS"
type: "Concept"
theme: securite
niveau: 🔴
source_url: https://atlas.mitre.org/
---

# MITRE ATLAS

**En une phrase** — La matrice des tactiques et techniques adverses contre les systèmes d'IA, calquée sur MITRE ATT&CK et adossée à des études de cas réelles.

## Ce que dit la source

**MITRE ATLAS** est une base de connaissances des comportements adverses observés ou plausibles contre les systèmes d'IA, modelée sur le cadre **MITRE ATT&CK** dont elle est le pendant pour l'IA. Elle s'organise en **tactiques** (le « pourquoi » : l'objectif de chaque étape) déclinées en **techniques** (le « comment »), et documente des **case studies** (incidents réels et exercices de red team).

Volumétrie des données canoniques **ATLAS.yaml v5.6.0** : **16 tactiques**, **101 techniques** (`AML.Txxxx`), **57 études de cas** (`AML.CSxxxx`).

> ⚠️ **Snapshot figé.** Le fichier local [`md/ATLAS.yaml`](../sources/security-references/md/ATLAS.yaml) est une copie **v5.6.0** dont la première ligne porte l'avertissement officiel : _« This version of the ATLAS data is deprecated and is no longer being updated »_. Pratique pour interroger les techniques hors-ligne (grep/script), mais à reconfronter à [atlas.mitre.org](https://atlas.mitre.org/) pour toute version à jour.

Les 16 tactiques (ID `AML.TAxxxx`, descriptions résumées du YAML officiel), dans l'ordre de la matrice :

1. **Reconnaissance** (`AML.TA0002`) — rassembler des informations sur le système d'IA cible pour planifier les opérations.
2. **Resource Development** (`AML.TA0003`) — créer, acheter ou compromettre des ressources (artefacts IA, infrastructure, comptes).
3. **Initial Access** (`AML.TA0004`) — obtenir un premier accès au système d'IA.
4. **AI Model Access** (`AML.TA0000`) — accéder au modèle lui-même (API publique, accès indirect via un produit, ou connaissance interne).
5. **Execution** (`AML.TA0005`) — exécuter du code malveillant embarqué dans des artefacts IA ou logiciels.
6. **Persistence** (`AML.TA0006`) — maintenir l'accès (données empoisonnées, modèles manipulés laissés en place).
7. **Privilege Escalation** (`AML.TA0012`) — obtenir des permissions plus élevées.
8. **Defense Evasion** (`AML.TA0007`) — échapper à la détection des outils de sécurité dopés à l'IA.
9. **Credential Access** (`AML.TA0013`) — voler identifiants et mots de passe.
10. **Discovery** (`AML.TA0008`) — explorer l'environnement IA et le réseau interne.
11. **Lateral Movement** (`AML.TA0015`) — se déplacer vers d'autres composants (registres de modèles, bases vectorielles, pipelines, agents).
12. **Collection** (`AML.TA0009`) — rassembler artefacts IA et informations utiles à l'objectif.
13. **AI Attack Staging** (`AML.TA0001`) — préparer l'attaque sur mesure (modèles proxy, empoisonnement, données adverses).
14. **Command and Control** (`AML.TA0014`) — communiquer avec les systèmes IA compromis pour les contrôler.
15. **Exfiltration** (`AML.TA0010`) — voler artefacts IA ou informations sur le système.
16. **Impact** (`AML.TA0011`) — manipuler, interrompre, éroder la confiance ou détruire les systèmes et données IA.

> Note : la plupart des tactiques portent une `ATT&CK-reference` (renvoi explicite vers la tactique ATT&CK correspondante), confirmant l'alignement. Les tactiques **AI Model Access** et **AI Attack Staging** sont propres à ATLAS (sans équivalent ATT&CK), car spécifiques au cycle de vie ML. **Lateral Movement** mentionne explicitement les agents IA comme cible de valeur (permissions souvent supérieures à un compte utilisateur standard) — ajout récent (2025).

## Techniques clés (extraites d'ATLAS.yaml)

Sélection de 14 techniques `AML.Txxxx` pertinentes pour les LLM et agents, extraites verbatim (id + nom) du fichier canonique `md/ATLAS.yaml` v5.6.0 ; la description en une ligne reprend la première phrase de la `description` officielle de chaque technique.

- **AML.T0051** — LLM Prompt Injection : des prompts malveillants en entrée d'un LLM le poussent à agir de façon non prévue.
- **AML.T0054** — LLM Jailbreak : induire un LLM à ignorer, contourner ou outrepasser ses comportements d'alignement/sûreté et ses garde-fous pour obtenir des sorties qu'il devrait retenir.
- **AML.T0056** — Extract LLM System Prompt : tenter d'extraire le prompt système d'un LLM.
- **AML.T0057** — LLM Data Leakage : forger des prompts qui amènent le LLM à divulguer des informations sensibles.
- **AML.T0020** — Poison Training Data : empoisonner les jeux de données utilisés par un modèle en modifiant les données sous-jacentes ou leurs labels.
- **AML.T0070** — RAG Poisoning : injecter du contenu malveillant dans les données indexées par un système RAG pour contaminer un futur fil via les résultats de recherche.
- **AML.T0053** — AI Agent Tool Invocation : utiliser son accès à un agent IA pour invoquer les outils auxquels l'agent a accès.
- **AML.T0080** — AI Agent Context Poisoning : manipuler le contexte utilisé par le LLM d'un agent IA pour influencer ses réponses ou les actions qu'il entreprend.
- **AML.T0086** — Exfiltration via AI Agent Tool Invocation : invoquer des outils d'agent capables d'écriture pour exfiltrer des données vers un adversaire.
- **AML.T0110** — AI Agent Tool Poisoning : obtenir la persistance en empoisonnant les outils des agents IA, y compris les outils intégrés ou exposés via des connexions Model Context Protocol (MCP).
- **AML.T0061** — LLM Prompt Self-Replication : utiliser une injection de prompt conçue pour que le LLM réplique le prompt dans sa propre sortie.
- **AML.T0068** — LLM Prompt Obfuscation : masquer ou obscurcir des injections de prompt ou du contenu de récupération pour échapper à la détection (humains, garde-fous LLM, autres mécanismes).
- **AML.T0010** — AI Supply Chain Compromise : obtenir un accès initial en compromettant les portions propres à la chaîne d'approvisionnement IA.
- **AML.T0029** — Denial of AI Service : cibler des systèmes dopés à l'IA avec un flot de requêtes pour dégrader ou arrêter le service.

## Pourquoi c'est utile

Là où OWASP nomme des *risques*, ATLAS fournit la **chaîne d'attaque** : une grammaire tactiques→techniques qui situe chaque menace dans le cycle de vie d'un adversaire (de la reconnaissance à l'impact), avec des incidents réels documentés. Cette vue « kill-chain IA » permet de cartographier un garde-fou agentique face à une technique adverse précise.

## Points clés

- Pendant de **MITRE ATT&CK** pour l'IA (mêmes tactiques + extensions spécifiques IA).
- **16 tactiques**, **101 techniques**, **57 études de cas** (données v5.6.0).
- Deux tactiques propres à l'IA : **AI Model Access** et **AI Attack Staging**.
- Tactiques 2025 orientées agents : **Lateral Movement** cible registres de modèles, bases vectorielles, pipelines et agents.
- Outil de threat modeling et de red teaming, étayé par des cas réels.

## Voir aussi

- [Sécurité agentique](securite-agentique.md)
- [Attaques adversariales](attaques-adversariales-llm.md)
- [OWASP Top 10 LLM](owasp-llm-top-10.md) · [NIST AI 100-2](nist-ai-100-2.md)
- Lien officiel : <https://atlas.mitre.org/>
