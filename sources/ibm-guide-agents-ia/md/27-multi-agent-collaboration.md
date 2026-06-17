> Source : https://www.ibm.com/fr-fr/think/topics/multi-agent-collaboration

# Qu’est-ce que la collaboration multi-agent ?

L’évolution des [grands modèles de langage (LLM)](https://www.ibm.com/fr-fr/think/topics/large-language-models) vers l’intégration d’agents d’IA a bouleversé le paysage de [l’intelligence artificielle (IA)](https://www.ibm.com/fr-fr/think/topics/artificial-intelligence). Aujourd’hui, les systèmes multi-agents (MAS) inaugurent une nouvelle génération de produits et de services de développement logiciel IA natifs.  

Les applications traditionnelles des LLM propulsés par [l’IA générative](https://www.ibm.com/fr-fr/think/topics/generative-ai) étaient principalement axées sur l’amélioration de la productivité, la réponse à des questions ou le résumé d’informations. Mais avec l’introduction des [agents d’IA](https://www.ibm.com/fr-fr/think/topics/ai-agent-types) et la possibilité pour ces agents de [communiquer entre eux](https://www.ibm.com/fr-fr/think/topics/ai-agent-communication), il est désormais possible de créer des workflows autonomes réduisant significativement le travail manuel impliqué dans la recherche, le support, l’analyse ou les opérations. Désormais, les [systèmes multi-agents](https://www.ibm.com/fr-fr/think/topics/multiagent-system) gèrent des tâches complexes du monde réel telles que le triage pour le service client, l’analyse financière, le dépannage technique et la surveillance de la conformité. Ces systèmes sont devenus évolutifs, autonomes, et ils peuvent être améliorés en continu.

Les actions coordonnées de plusieurs agents indépendants dans un système distribué, chacun disposant de connaissances locales et de capacités décisionnelles, relèvent de la **collaboration multi-agent**.

Dans ce cadre, les agents coopèrent via des protocoles de communication établis pour échanger des informations sur leur état, répartir les responsabilités et coordonner leurs actions. La coopération implique souvent des méthodes de décomposition du travail, de répartition des ressources, de résolution de conflits et de planification coopérative. Elle peut être explicite (via échange de messages) ou implicite (via modifications de l’environnement partagé). Ces systèmes sont conçus pour favoriser l’évolutivité, la tolérance aux pannes et un comportement coopératif émergent, sans contrôle centralisé. Analogie : imaginez une flotte de drones explorant une zone sinistrée à la recherche de survivants ou d’informations. Chaque drone suit son propre itinéraire, évite les autres drones, rapporte ce qu’il découvre et change de direction en cas d’événement inattendu. Cette scène illustre la collaboration multi-agent : chaque drone agit individuellement tout en coopérant collectivement, comme des assistants. Sans qu’un chef unique ne les coordonne, ils travaillent ensemble, se synchronisent et partagent ce qu’ils voient. C’est ainsi qu’une flotte autonome d’agents peut résoudre intelligemment, rapidement et collectivement des problèmes complexes.

Cette architecture collaborative redéfinit l’architecture produit, donnant naissance à de nouveaux cas d’utilisation pouvant s’exécuter presque en continu, s’adapter à une demande croissante et apprendre/optimiser en permanence sans intervention manuelle. Le processus d’automatisation agentique est rendu possible grâce à des agents spécialisés dotés de capacités adaptatives conçues pour traiter des tâches spécifiques avec précision et autonomie. Des agents d’IA spécialisés travaillent ensemble en temps réel pour fournir des services intelligents, personnalisés et de bout en bout dans des [chatbots](https://www.ibm.com/fr-fr/think/topics/chatbots) (via le cadre RAG), un nouveau type d’application multi-agent.[1](#f01)

## Pourquoi les agents doivent-ils collaborer ?

La coopération entre plusieurs agents est une exigence cruciale dans la conception et le déploiement de systèmes intelligents, en particulier dans des environnements complexes, distribués et soumis à des contraintes de confidentialité. La collaboration multi-agent offre de nombreux avantages architecturaux, computationnels et opérationnels, en comparaison avec d’autres types d’[architectures agentiques](https://www.ibm.com/fr-fr/think/topics/agentic-architecture), notamment les systèmes mono-agents. C’est particulièrement vrai dans les systèmes en temps réel, distribués et complexes, où différents niveaux de confidentialité entrent intrinsèquement en jeu. Les systèmes multi-agents (MAS) permettent à des agents autonomes et décentralisés de collaborer pour atteindre des objectifs collectifs ou interdépendants, dépassant ainsi certaines limites structurelles des systèmes mono-agents contraints. Par exemple, les systèmes monolithiques ne peuvent évoluer que dans une certaine mesure et souffrent souvent de limitations en matière de latence ou de polyvalence fonctionnelle. Chaque agent conserve un certain niveau d’autonomie, effectue des calculs localement et coopère avec d’autres agents via des protocoles de communication pour partager des connaissances partielles de leur environnement, prendre des décisions conjointes et coordonner une stratégie de contrôle distribuée. Cette évolutivité modulaire permet l’intégration fluide de nouveaux agents ou sous-systèmes, tout en assurant un comportement adaptatif dans des environnements dynamiques en temps réel. Par exemple, dans un système de santé intelligent, un sous-ensemble ou l’ensemble des agents peuvent se voir attribuer des missions spécifiques à leur domaine : surveiller les signaux physiologiques, identifier des anomalies, recommander des traitements ou gérer des données personnelles de patients en conformité avec la réglementation. Leur coopération permet également d’assurer la continuité, la précision et la tolérance aux pannes tout au long du processus. La capacité à normaliser les calculs entre agents augmente l’efficacité computationnelle en mutualisant les paramètres entre agents et en éliminant le besoin de calculs centralisés.[2](#f02)

## Comment les agents des systèmes multi-agents collaborent-ils ?

Pour comprendre le fonctionnement des systèmes multi-agents, décomposons le processus coopératif en une séquence d’étapes bien coordonnées, chacune illustrant la manière dont des entités autonomes interagissent, se répartissent les tâches et coopèrent pour accomplir des missions complexes.

Les agents **collaborent et se coordonnent** via des canaux structurés, chaque agent étant un composant intelligent reposant sur cinq éléments clés :

a. **Le [modèle de fondation](https://www.ibm.com/fr-fr/think/topics/foundation-models) (𝑚) :** c’est le moteur de raisonnement principal de l’agent, lui permettant de générer et de comprendre le langage naturel.

b. **L’objectif (𝑜) :** il définit la tâche ou la mission que l’agent cherche à accomplir.

c. **L’environnement (𝑒) :** c’est le contexte dans lequel l’agent opère, pouvant inclure d’autres agents, des outils, une mémoire partagée ou des [interfaces de programmation d’applications (API)](https://www.ibm.com/fr-fr/think/topics/api).

d. **La perception (𝑥)** : ce sont les informations que l’agent reçoit de son environnement ou d’autres agents en entrée.

e. **La sortie ou action (𝑦) :** il s’agit de la réponse ou du comportement de l’agent en fonction de son objectif et de son raisonnement.

On parle de collaboration lorsque plusieurs [agents d’IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) coopèrent en tant qu’équipe pour accomplir une tâche. Pendant la phase de collaboration, le système reçoit une **tâche**, soit de l’utilisateur, soit de l’environnement. Il détermine quels **agents** sont nécessaires et quel **rôle** chacun jouera.

Le système divise les problèmes complexes en éléments plus gérables. Cela peut être réalisé par un planificateur ou par le modèle de langage disposant de capacités de raisonnement. La communication entre agents s’effectue via une mémoire partagée ou par des sorties intermédiaires. Les tâches sont ensuite exécutées par les agents de manière parallèle, séquentielle ou dynamique.

Les résultats produits par les différents agents sont compilés pour former une réponse cohérente. L’orchestrateur ou l’agent final exécute l’action ou fournit la réponse complète à l’utilisateur.[3](#f03)

  La Figure 1 présente le fonctionnement de la collaboration multi-agent. Ce cadre définit les dimensions clés qui caractérisent les mécanismes de collaboration entre les agents.

### Stratégies de collaboration entre agents

Les agents collaborent selon différentes stratégies qui définissent comment ils interagissent, se coordonnent et contribuent aux objectifs communs. Voici quelques-unes des approches les plus courantes :

**- Collaboration basée sur des règles** :

Dans ce type de collaboration, les interactions entre agents sont strictement régies par un ensemble de règles ou de directives précises. Ces règles indiquent comment les agents doivent agir, communiquer et prendre des décisions de manière prévisible. La capacité d’apprentissage ou d’adaptation est limitée, les agents se conformant à une politique fixe fondée sur certaines conditions ou entrées. Ce type de collaboration repose souvent sur des instructions conditionnelles, des automates d’état ou des cadres logiques. Ce type de collaboration est particulièrement efficace pour les tâches très structurées ou prévisibles, où la cohérence est essentielle.

**Avantages et inconvénients :** cette méthode est efficace et équitable, mais elle n’est ni très adaptable ni très évolutive, en particulier dans les situations complexes ou changeantes.

**- Collaboration basée sur les rôles :**

Dans cette approche, les agents se voient attribuer des rôles ou responsabilités spécifiques en accord avec une structure organisationnelle ou un cadre de communication. Chaque rôle est associé à un ensemble de fonctions, de permissions et d’objectifs, souvent liés à une partie distincte de l’objectif global du système. Les agents travaillent de façon semi-indépendante dans leur rôle, tout en coopérant à l’échelle du système par partage d’informations. Ce modèle s’inspire des dynamiques humaines, dans lesquelles les individus remplissent des rôles différents (chef, observateur, exécuteur…). Il est particulièrement utile pour décomposer les tâches, concevoir des systèmes modulaires et permettre la collaboration efficace d’agents aux compétences variées.

**Avantages et inconvénients :** permet une collaboration modulaire et experte, mais peut rencontrer des limitations de flexibilité et dépend fortement de l’intégration fluide des agents.

**- Collaboration basée sur des modèles :**

Ici, les agents construisent des modèles internes pour comprendre leur propre état, leur environnement, les autres agents, et l’objectif collectif. Ces modèles sont généralement probabilistes ou appris, ce qui permet aux agents de planifier leurs actions même en situation d’incertitude. Leurs interactions reposent sur la mise à jour de leurs croyances, la formulation d’inférences et la prédiction des résultats, ce qui leur permet d’adopter des stratégies flexibles et contextuelles. Les méthodes couramment utilisées incluent le raisonnement bayésien, les processus de décision markoviens (MDP) et divers modèles de [machine learning](https://www.ibm.com/fr-fr/think/topics/machine-learning). Cette approche est particulièrement utile dans les situations où les agents doivent réfléchir à des facteurs inconnus, s’adapter à des changements ou collaborer sans visibilité complète.

**Avantages et inconvénients :** offre une grande flexibilité et des capacités décisionnelles solides, mais avec une complexité importante et un coût computationnel élevé.[4](#f04)

### Cadres

Plusieurs cadres bien connus sont en cours de développement, chacun utilisant ses propres méthodes pour permettre aux agents de collaborer efficacement dans des applications réelles. Découvrons les cadres les plus couramment utilisés :

**1.** **Cadre IBM Bee Agent : **il s’agit d’une application [open source](https://www.ibm.com/fr-fr/think/topics/open-source) qui facilite le développement et l’administration de processus multi-agents évolutifs. Elle établit les bases pour des applications dans lesquelles plusieurs agents d’IA collaborent pour accomplir des tâches complexes, en utilisant des LLM comme IBM Granite, gpt-4 et Llama 3. Avec des composants prêts à l’emploi pour les agents, les outils, la gestion de la mémoire et la surveillance, ce framework se distingue par sa conception modulaire. La sérialisation des états d’agents est l’une de ses caractéristiques les plus remarquables. Cette capacité permet d’interrompre et de reprendre des procédures complexes sans perte de données. Son accent sur le contrôle en production, l’extensibilité et la modularité permet de créer des systèmes multi-agents sophistiqués pour un large éventail d’applications, avec des plans pour des avancées futures dans l’orchestration multi-agent.

**2. Agents LangChain : **LangChain est un cadre robuste qui permet de créer des applications basées sur des modèles de langage, reposant sur une architecture fortement orientée agent. Cela signifie que les agents peuvent percevoir leur environnement et utiliser les nombreux outils disponibles pour recueillir des informations, les interpréter et agir en conséquence. Au sein même de LangChain, les développeurs ont accès à de nombreux outils et intégrations facilitant la conception d’agents capables de raisonner de manière complexe, de prendre des décisions dynamiques et d’accomplir des tâches. LangChain permet au développeur d’exploiter tout le potentiel des grands modèles de langage (LLM) pour construire des systèmes intelligents capables d’exécuter des tâches sophistiquées comme les réponses contextuelles aux questions, les [workflows](https://www.ibm.com/fr-fr/think/topics/workflow) multi-étapes ou encore la génération de langage naturel.

3. **Cadre Swarm d’OpenAI : **cette structure propose une nouvelle manière de coordonner plusieurs agents autour de routines et de transmissions de tâches. Au lieu d’agir indépendamment, chaque agent est vu comme une unité spécialisée dotée d’outils personnalisés et de consignes spécifiques. Le transfert d’une tâche ou d’une conversation d’un agent à un autre permet une expérience utilisateur fluide, chaque agent étant spécialisé dans un rôle précis. Cette approche améliore l’efficacité, la modularité et la réactivité du système dans son ensemble. Le terme Swarm met l’accent sur une coordination légère et une exécution efficace des tâches, ce qui permet de déployer ce système à plus grande échelle dans des situations concrètes.[5](#f05)

## Solutions d’entreprise

#### **watsonx Orchestrate**

[watsonx Orchestrate](https://www.ibm.com/fr-fr/products/watsonx-orchestrate) simplifie la collaboration multi-agent grâce à une collection de composants interconnectés qui orchestrent ensemble des [workflows alimentés par l’IA](https://www.ibm.com/fr-fr/think/topics/ai-workflow). Les skills sont des agents indépendants qui exécutent des tâches spécifiques, comme l’envoi d’e-mails ou l’interrogation de données. Ils sont décrits et enregistrés dans un registre de compétences qui détaille leurs capacités et leurs métadonnées. Lorsqu’un utilisateur soumet une requête, un analyseur d’intention (Intent Parser) utilise le [traitement automatique du langage naturel (NLP)](https://www.ibm.com/fr-fr/think/topics/natural-language-processing) pour interpréter l’entrée de l’utilisateur et la relier aux compétences.

Le Flow Orchestrator fournit la logique d’exécution et le déroulement du flux, y compris l’enchaînement des tâches, les bifurcations, les erreurs et les relances, pour garantir que les agents sont exécutés dans l’ordre requis et que les étapes échouées puissent être réessayées. L’orchestrateur de flux permet également l’exécution simultanée des agents lorsque c’est nécessaire. Le contexte partagé et la mémoire commune (Shared Context et Memory Store) offrent un espace de stockage commun pour les données, les résultats intermédiaires et les décisions, permettant aux agents d’être conscients les uns des autres et de conserver la continuité tout au long du processus. L’assistant LLM utilise de grands modèles de langage pour raisonner, s’adapter à un contexte en évolution et combler les lacunes en connaissances tout en collaborant. 

L’interface humaine (Human Interface) permet à l’utilisateur de voir le flux et de gérer le [workflow agentique](https://www.ibm.com/fr-fr/think/topics/agentic-workflows) s’il souhaite s’impliquer. Ces composants permettent une collaboration multi-agent, garantissant que watsonx Orchestrate peut gérer des workflows multi-agents complexes de manière autonome, tout en permettant une intervention humaine si besoin.[6](#f06)

## Prévisions pour l’avenir

**Intelligence collective émergente :** alors que des agents autonomes commencent à collaborer via un **cadre** bien défini, avec des **garde-fous** garantissant l’alignement, la sécurité et la pertinence des tâches, des comportements intelligents émergent : dépassant les capacités individuelles de chaque agent pris séparément. L’exactitude, la pertinence, l’efficacité, l’explicabilité et la cohérence globale du système sont quelques-uns des multiples indicateurs permettant d’évaluer et d’améliorer en continu l’efficacité de ces systèmes.

L’intelligence collective donne à ces systèmes la capacité de résoudre des problèmes complexes et multidimensionnels grâce à un raisonnement distribué et à une décomposition des tâches, aboutissant à **[l’automatisation](https://www.ibm.com/fr-fr/think/topics/automation), à la prise de décision** et à **l’orchestration** de workflows en plusieurs étapes.
