> Source : https://www.ibm.com/fr-fr/think/topics/ai-agent-protocols

# Que sont les protocoles des agents IA ?

Les protocoles d’agents IA établissent des normes de communication entre les agents d’[intelligence artificielle](https://www.ibm.com/fr-fr/think/topics/artificial-intelligence), et entre les [agents IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) et d’autres systèmes. Ces protocoles spécifient la syntaxe, la structure et la séquence des messages, ainsi que les conventions de communication (par exemple, quel rôle les agents ont dans les conversations, quand et comment ils répondent aux messages).

Les systèmes d’IA basés sur des agents s’exécutent souvent en [silos](https://www.ibm.com/fr-fr/think/topics/data-silos). Ils sont construits par différents fournisseurs utilisant divers [cadres d’agent IA](https://www.ibm.com/fr-fr/think/insights/top-ai-agent-frameworks) et des [architectures agentiques](https://www.ibm.com/fr-fr/think/topics/agentic-architecture) distinctes. L’intégration en situation réelle devient un défi, et le couplage de ces systèmes fragmentés nécessite des connecteurs sur mesure pour tous les types d’interaction possibles avec les agents.

C’est là que les protocoles entrent en jeu. Ils transforment les [systèmes multi-agents](https://www.ibm.com/fr-fr/think/topics/multiagent-system) disparates en écosystème interconnecté. Ici, les agents alimentés par l’IA partagent un moyen de se découvrir, de se comprendre et de collaborer.

Bien que les protocoles agentiques fassent partie de l’[orchestration des agents IA](https://www.ibm.com/fr-fr/think/topics/ai-agent-orchestration), ils ne servent pas d’orchestrateurs. Ils normalisent la communication, mais ils ne gèrent ni la coordination, ni l’exécution ni l’optimisation des [workflows agentiques](https://www.ibm.com/fr-fr/think/topics/agentic-workflows).

## Avantages des protocoles de l’agent IA

Les protocoles d’agent IA offrent les avantages suivants :

- [Interopérabilité](https://www.ibm.com/fr-fr/think/topics/interoperability)

- Développement simplifié des agents

- Standardisation et intégration plus fluide

### Interopérabilité

Les protocoles d’agent cassent les silos, permettant aux [IA agentiques](https://www.ibm.com/fr-fr/think/topics/agentic-ai) de communiquer les unes avec les autres, quelle que soit leur implémentation sous-jacente. Ils favorisent une [collaboration fluide entre les agents](https://www.ibm.com/fr-fr/think/topics/multi-agent-collaboration) à travers les appareils, environnements et plateformes.

### Développement simplifié des agents

Parce que les protocoles s’attaquent aux subtilités de l’interaction agentique et éliminent la complexité grâce aux kits de développement logiciel ([SDK](https://www.ibm.com/fr-fr/think/topics/api-vs-sdk)), ils permettent de rationaliser la création des systèmes multi-agents. Les développeurs d’IA peuvent se concentrer davantage sur la création de nouvelles fonctionnalités d’agent et sur l’amélioration des fonctionnalités existantes.

### Standardisation et intégration plus fluide

Les protocoles d’agent IA offrent un moyen de communication défini et structuré. Et comme bon nombre de ces protocoles standardisés reposent sur des technologies établies, ils garantissent la compatibilité avec les piles technologiques actuelles, facilitant l’intégration en entreprise.

## Exemples de protocoles d’agents IA

De nombreux protocoles n’en sont qu’à leurs débuts. Ils n’ont donc pas encore été largement utilisés, ni appliqués à grande échelle. Ce manque de maturité signifie que les entreprises doivent être prêtes à s’adapter aux changements de dernière minute et à l’évolution des spécifications.

Au fur et à mesure que la technologie agentique évolue, de nouveaux protocoles peuvent émerger. Voici quelques protocoles d’agent IA actuellement disponibles :

- Protocole Agent2Agent (A2A)

- Agent Communication Protocol (ACP)

- Agent network protocol (ANP)

- Protocole d’interaction agent-interface utilisateur (AG-UI)

- Agora

- Protocole LMOS

- Model Context Protocol (MCP) 

### Protocole Agent2Agent (A2A)

Le [protocole A2A](https://www.ibm.com/fr-fr/think/topics/agent2agent-protocol) est une [norme ouverte](https://www.ibm.com/fr-fr/think/topics/open-standards-vs-open-source-explanation) pour [la communication des agents IA](https://www.ibm.com/fr-fr/think/topics/ai-agent-communication), initialement lancée par Google et désormais gérée par la Linux Foundation. Il suit un modèle client-serveur avec un [workflow](https://www.ibm.com/fr-fr/think/topics/ai-workflow) en trois étapes :

1.  On parle de **découverte** lorsqu’une entité (un utilisateur humain ou un agent IA) lance une demande de tâche à un agent client, qui recherche alors des agents à distance pour déterminer la meilleure solution.
2.  Une fois que l’agent client a identifié un agent distant capable d’accomplir la tâche, il procède à l’**authentification**. L’agent distant est responsable de [l’autorisation](https://www.ibm.com/fr-fr/think/topics/authentication-vs-authorization) et de l’octroi des droits de [contrôle d’accès](https://www.ibm.com/fr-fr/think/topics/rbac).
3.  La **communication** se poursuit : l’agent client envoie la tâche, et l’agent distant la traite. La communication d’agent à agent se fait via HTTPS pour garantir un transport sécurisé, le format d’échange de données étant JSON-RPC (Remote Procedure Call) 2.0.

### Agent Communication Protocol (ACP)

Comme A2A, le protocole [ACP (Agent Communication Protocol)](https://www.ibm.com/fr-fr/think/topics/agent-communication-protocol) est une norme ouverte pour la communication d’agent à agent, initialement introduite par [BeeAI](https://www.ibm.com/fr-fr/think/topics/beeai) d’IBM et qui fait désormais partie de la Linux Foundation.

Ses principaux composants sont un client ACP et un serveur ACP. Le client ACP envoie des requêtes au serveur ACP par le biais d’une [API RESTful](https://www.ibm.com/fr-fr/think/topics/rest-apis) via HTTP. Le serveur ACP héberge un ou plusieurs agents derrière un point de terminaison HTTP unique, et achemine les tâches vers l’agent approprié.

Voici quelques autres fonctionnalités d'ACP :

- Le [protocole](https://research.ibm.com/blog/agent-communication-protocol-ai) peut être utilisé avec des outils HTTP standard comme Postman, et même un navigateur, mais des SDK sont également disponibles.

- La découverte peut se faire en ligne en interrogeant directement les serveurs AC et les fichiers manifestes publics à des URL bien connues. La découverte hors ligne se fait par le biais d’un registre centralisé ou en incorporant les [métadonnées](https://www.ibm.com/fr-fr/think/topics/metadata) des agents directement dans leurs paquets de distribution.

- ACP accepte différents types de messages comme l’audio, les images, le texte, les vidéos ou les formats binaires personnalisés.

### Protocole de réseau d’agents (ANP)

[ANP (Agent Network Protocol)](https://www.agent-network-protocol.com/) est un protocole [open source](https://www.ibm.com/fr-fr/think/topics/open-source) dont l’objectif est d’être « le HTTP de l’ère agentique ». À ce titre, il utilise HTTP pour le transport des données et JSON-LD (JSON for Linked Data) pour le formatage des données.

ANP adopte une architecture pair-à-pair composée de trois couches :

- La **couche d’identité** met en œuvre [chiffrement de bout en bout](https://www.ibm.com/fr-fr/think/topics/end-to-end-encryption) pour une communication sécurisée et [authentification](https://www.ibm.com/fr-fr/think/topics/authentication) d’identité décentralisée basée sur la norme W3C DID (Decentralized Identifiers).

- La **couche méta-protocole** permet aux agents de négocier et de s’accorder sur la façon de communiquer.

- La **couche de protocole d’application** permet aux agents autonomes de décrire leurs capacités et prend en charge la découverte d’agents.

### Protocole d’interaction agent-utilisateur (AG-UI)

Le [protocole AG-UI (Agent-User Interaction)](https://docs.ag-ui.com/introduction) vise à normaliser la manière dont les agents IA back-end se connectent aux applications front-end ou destinées à l’utilisateur. Il est conçu pour une interaction homme-agent en temps réel, comme les conversations avec les [assistants IA](https://www.ibm.com/fr-fr/think/topics/ai-agents-vs-ai-assistants) et les [chatbots](https://www.ibm.com/fr-fr/think/topics/chatbots), la diffusion en direct des mises à jour d’état et d’autres [automatisations](https://www.ibm.com/fr-fr/think/topics/agentic-automation) impliquant une approche [l’humain dans la boucle](https://www.ibm.com/fr-fr/think/topics/human-in-the-loop).

L’architecture orientée événements d’AG-UI permet aux agents IA de produire des événements en fonction de certains déclencheurs du système ou des entrées utilisateur. Le protocole définit un certain nombre de catégories d’événements, notamment l’envoi et la réception de messages, l’[appel d’outils](https://www.ibm.com/fr-fr/think/topics/tool-calling) et l’exécution des tâches.

Sa couche middleware prend en charge plusieurs méthodes de transport telles que les [événements envoyés par le serveur (SSE)](https://community.ibm.com/community/user/blogs/abishek-s/2024/11/28/the-power-of-server-sent-events-sse), les [webhooks et les WebSockets.](https://www.redhat.com/en/topics/automation/what-is-a-webhook) AG-UI permet également à un proxy sécurisé d’acheminer les requêtes entre les agents et les interfaces utilisateur.

### Agora

[Agora](https://agoraprotocol.org/) est un protocole de communication entre agents alimenté par de [grands modèles de langage](https://www.ibm.com/fr-fr/think/topics/large-language-models) (LLM). Il s’appuie sur quelques capacités essentielles des [agents LLM](https://research.ibm.com/blog/what-are-ai-agents-llm) : [compréhension du langage naturel](https://www.ibm.com/fr-fr/think/topics/natural-language-understanding), suivi d’instructions, écriture et exécution du code, négociation autonome.

Les agents LLM peuvent mettre en œuvre et prendre en charge leurs propres protocoles, qu’ils décrivent en texte brut dans un document de protocole. La première partie du document contient des métadonnées indiquant le nom et la description du protocole, et s’il s’agit d’un seul ou de plusieurs cycles de conversation. La deuxième partie décrit le mode de communication, avec des instructions en langage naturel et en code. Les agents négocient ensuite de manière autonome le protocole à adopter.

Agora utilise HTTPS pour la transmission des données, et JSON pour le formatage. Il utilise également un système d’identification basé sur le hachage pour les documents de protocole.

### Protocole LMOS

Développé par l’Eclipse Foundation, le [protocole LMOS (Language Model Operating System)](https://eclipse.dev/lmos/docs/lmos_protocol/introduction/) vise à créer un Internet des agents (IoA), un écosystème multi-agents à l’échelle d’Internet. Comme ANP, son architecture structurée se compose de trois couches :

- La **couche d’identité et de sécurité** assure une communication chiffrée et prend en charge différents schémas d’authentification, notamment W3C DID et OAuth 2.0.

- La **couche de protocole de transport** permet aux agents de choisir et d’adapter le protocole de transport qui convient à leur objectif pour chaque interaction.

- La **couche de protocole d’application** décrit les formats pour la description des agents et des outils, les méthodes de découverte, un modèle de données sémantique et un sous-protocole Websocket.

Le protocole LMOS utilise JSON-LD pour décrire les capacités des outils et des agents, ainsi que d’autres métadonnées. La découverte se fait soit de manière dynamique, en interrogeant un annuaire centralisé, soit par le biais de réseaux décentralisés.

### Model Context Protocol (MCP)

Introduit par Anthropic, le [Model Context Protocol (MCP)](https://www.ibm.com/fr-fr/think/topics/model-context-protocol) fournit aux [modèles d’IA](https://www.ibm.com/fr-fr/think/topics/ai-model) un moyen standardisé d’obtenir le contexte dont ils ont besoin pour effectuer leurs tâches. Dans le domaine agentique, MCP sert de niveau permettant aux agents IA de se connecter et de communiquer avec les services et outils externes tels que les [API](https://www.ibm.com/fr-fr/think/topics/api), les bases de données, les fichiers, les recherches Web et d’autres sources de données.

MCP englobe ces trois éléments architecturaux clés :

- L’**hôte MCP** contient une logique d’orchestration et peut connecter chaque client MCP à un serveur MCP. Il peut héberger plusieurs clients.

- Le **client MCP** convertit les requêtes utilisateur dans un format structuré que le protocole peut traiter. Chaque client entretient une relation individuelle avec le serveur MCP. Les clients gèrent les sessions, analysent et vérifient les réponses, et gèrent les erreurs.

- Le **serveur MCP** convertit les requêtes utilisateur en actions. Les serveurs, généralement des dépôts GitHub disponibles dans différents langages de programmation, donnent accès à des outils. Ils peuvent également être utilisés pour connecter [l’inférence LLM](https://www.ibm.com/fr-fr/think/topics/ai-inference) au SDK MCP par le biais des fournisseurs de plateformes d’IA comme IBM et OpenAI.

Dans la couche de transport entre les clients et les serveurs, les messages sont transmis au format JSON-RPC 2.0 en utilisant soit une entrée/sortie standard (stdio) pour la messagerie légère et synchrone, soit SSE pour les appels asynchrones pilotés par les événements.

## Facteurs d’évaluation d’un protocole d’agents d’IA

En l’absence de [références](https://research.ibm.com/blog/AI-agent-benchmarks) pour une évaluation standardisée, les entreprises doivent procéder à leur propre évaluation du protocole qui répond le mieux à leurs besoins métier. Ils devront peut-être commencer par un petit [cas d’utilisation](https://www.ibm.com/fr-fr/think/topics/ai-agent-use-cases) contrôlé, combiné à des tests complets et rigoureux.

Voici quelques aspects à prendre en compte lors de l’évaluation des protocoles d’agents :

- Efficacité

- Fiabilité

- Évolutivité

- Sécurité

### Efficacité

Idéalement, les protocoles sont conçus pour limiter la [latence,](https://www.ibm.com/fr-fr/think/topics/latency) ce qui permet un transfert de données et des temps de réponse rapides. Bien que certains frais de communication soient à prévoir, ils doivent être réduits au minimum.

### Fiabilité

Les protocoles des agents IA doivent être capables de gérer l’évolution des conditions du réseau tout au long des workflows, avec des mécanismes en place pour gérer les défaillances ou les interruptions. Par exemple, l’ACP est conçu avec une communication asynchrone par défaut, ce qui convient aux tâches complexes ou de longue durée. En revanche, A2A prend en charge le streaming en temps réel en utilisant le SSE pour les productions importantes ou longues ou les mises à jour d’état continues.

### Évolutivité

Les protocoles doivent être suffisamment robustes pour s’adapter à la croissance des écosystèmes d’agents sans pour autant perdre en performances. L’évaluation de l’évolutivité peut inclure l’augmentation du nombre d’agents ou de liens vers des outils externes sur une période donnée, de manière progressive ou soudaine, afin d’observer le fonctionnement d’un protocole dans ces conditions.

### Sécurité

Le maintien de la sécurité est primordial, et les protocoles des agents intègrent de plus en plus de garde-fous. Il s’agit notamment de l’authentification, du [chiffrement](https://www.ibm.com/fr-fr/think/topics/encryption) et du contrôle d’accès.
