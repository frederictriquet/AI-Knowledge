> Source : https://www.ibm.com/fr-fr/think/topics/agent2agent-protocol

# Qu’est-ce que le protocole A2A (Agent2Agent) ?

Le protocole Agent2Agent (A2A) est un protocole de communication pour les agents [d'intelligence artificielle (IA)](https://www.ibm.com/fr-fr/think/topics/artificial-intelligence), initialement lancé par Google en avril 2025. Ce protocole ouvert est conçu pour les [systèmes multi-agents](https://www.ibm.com/fr-fr/think/topics/multiagent-system), permettant [l’interopérabilité](https://www.ibm.com/fr-fr/think/topics/interoperability) entre les [agents d’IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) de divers fournisseurs ou ceux conçus à l’aide de différents [cadres d’exigences d’agents d’IA](https://www.ibm.com/fr-fr/think/insights/top-ai-agent-frameworks).

L’A2A est une [norme ouverte](https://www.ibm.com/fr-fr/think/topics/open-standards-vs-open-source-explanation) pour la [communication des agents d'IA](https://www.ibm.com/fr-fr/think/topics/ai-agent-communication), similaire à l’[Agent Communication Protocol (ACP)](https://www.ibm.com/fr-fr/think/topics/agent-communication-protocol) lancé par [BeeAI](https://beeai.dev/) d'IBM. Alors que les premiers cadres d’exigences pour l'[orchestration des agents](https://www.ibm.com/fr-fr/think/topics/ai-agent-orchestration) comme [crewAI](https://www.ibm.com/fr-fr/think/topics/crew-ai) et [LangChain](https://www.ibm.com/fr-fr/think/topics/langchain) automatisent les [flux de travail](https://www.ibm.com/fr-fr/think/topics/agentic-workflows) multi-agents au sein de leurs propres écosystèmes, le protocole A2A agit comme un niveau de messagerie qui permet à ces agents de « parler » entre eux malgré leurs [architectures agentiques](https://www.ibm.com/fr-fr/think/topics/agentic-architecture) distinctes.

Voyez A2A comme un langage commun ou un traducteur universel pour les écosystèmes d'agents. Il vise à [décloisonner](https://www.ibm.com/fr-fr/think/topics/data-silos) et à améliorer l'interopérabilité des agents.

Le protocole A2A a été initialement lancé par Google et d'autres partenaires technologiques sur la plateforme cloud en avril 2025.1 Il est désormais hébergé par la Linux Foundation en tant que projet [open source](https://www.ibm.com/fr-fr/think/topics/open-source) Agent2Agent (A2A).2

## Quelle est la différence entre MCP et A2A ?

Lancé par Anthropic en 2024, le [Model Context Protocol (MCP)](https://www.ibm.com/fr-fr/think/topics/model-context-protocol) sert de couche de normalisation permettant aux applications d'IA de communiquer efficacement avec des services externes, tels que les [API (interfaces de programmation des applications)](https://www.ibm.com/fr-fr/think/topics/api), les sources de données, les fonctions prédéfinies et d'autres outils. Le protocole A2A, quant à lui, se concentre sur la [collaboration entre agents](https://www.ibm.com/fr-fr/think/topics/multi-agent-collaboration) , facilitant la communication entre les agents d’IA.

Les deux protocoles sont complémentaires. Ainsi, un magasin de vente au détail peut avoir son propre agent d'inventaire qui utilise le MCP pour interagir avec les [bases de données](https://www.ibm.com/fr-fr/think/topics/database) conservant des informations sur les produits et les niveaux de stock. Si l'agent de gestion des stocks détecte que les produits sont en rupture, il en informe un agent de commande interne, qui utilise l’A2A pour communiquer avec les agents des fournisseurs externes et passer des commandes.

## Composants architecturaux principaux du protocole A2A

Le protocole Agent2Agent comprend plusieurs éléments constitutifs pour les interactions avec les agents :

- Client A2A (agent client)

<!-- -->

- Serveur A2A (agent distant)

<!-- -->

- Fiche d'agent

<!-- -->

- Tâche

<!-- -->

- Message

<!-- -->

- Artéfact

<!-- -->

- Partie

### Client A2A (agent client)

Le client A2A, également appelé agent client, peut être une application, un service ou un autre agent d’IA qui délègue des demandes à des agents distants. Il utilise le protocole Agent2Agent pour démarrer la communication.

### Serveur A2A (agent distant)

Le serveur A2A, également appelé agent distant, prend en charge les requêtes, gère les tâches et répond avec des mises à jour de statut ou des résultats. Il expose un point de terminaison HTTP compatible avec le protocole Agent2Agent.

### Fiche d'agent

Ce fichier JSON présente les [métadonnées](https://www.ibm.com/fr-fr/think/topics/metadata) [de l'IA agentique](https://www.ibm.com/fr-fr/think/topics/agentic-ai) et est accessible via une URL. Il contient des informations de base sur un agent, notamment son nom, sa description, sa version, l’URL du point de terminaison du service, les modalités ou les types de données pris en charge et les exigences d’[authentification](https://www.ibm.com/fr-fr/think/topics/authentication).

Les fiches d'agent sont similaires aux fiches de modèle pour les [grands modèles linguistiques (LLM)](https://www.ibm.com/fr-fr/think/topics/large-language-models). Elles mettent également en avant les capacités et les compétences d’un agent, servant de carte de visite, de CV ou de profil LinkedIn qui permet aux agents de se découvrir.

### Tâche

Une tâche représente une unité de travail nécessaire pour accomplir une requête.. Elle possède un identifiant unique et passe par un cycle de vie d’états définis (envoyée, active, entrée requise, terminée, échouée). Les tâches servent au traitement à plusieurs tours ou à la collaboration de longue durée entre agents.

### Message

En tant qu'unité de communication fondamentale, un message décrit un seul échange ou un seul tour dans une conversation. Il contient une ou plusieurs parties contenant le contenu réel.

Les messages transmettent les réponses, le contexte, les instructions, les invites, les questions, les réponses et les mises à jour de statut. En fonction de l’expéditeur, chaque message possède un rôle associé, qui peut être un rôle d’agent pour les messages envoyés par le serveur ou un rôle d’utilisateur pour les messages envoyés par le client.

### Artéfact

Un artéfact est un produit tangible généré par le serveur A2A à la suite de son travail. Il peut s’agir d’un document, d’une image, d’une feuille de calcul ou de tout autre livrable. Comme les messages, les artéfacts sont constitués d’une ou de plusieurs parties et peuvent être diffusés en continu de manière incrémentielle.

### Partie

Une partie est un élément de contenu à l'intérieur d'un message ou d’un artefact. Les parties sont de différents types en fonction des données qu'elles contiennent. Un TextPart est un conteneur de texte, un FilePart représente des fichiers et un DataPart englobe des données JSON (JavaScript Object Notation) structurées.

## Fonctionnement du protocole A2A

Le protocole A2A suit la configuration d’un modèle client-serveur avec un flux de travail en trois étapes :

1.  Découverte
2.  Authentification
3.  Communication

### Découverte

Le flux de travail A2A commence lorsqu’une entité (un utilisateur humain ou un autre agent d’IA) effectue une demande à l’agent client. Ainsi, un utilisateur peut demander de l’aide pour planifier un voyage ou un agent d’IA passe une commande d’un article en faible stock pour un magasin de vente au détail.

Un agent client poursuit ensuite le processus de découverte, en recherchant des agents distants et en récupérant leurs fiches d'agent pour déterminer la meilleure solution pour la tâche.

### Authentification

Une fois que l'agent client identifie un agent distant capable d'accomplir la tâche désignée, il passe par l'authentification en fonction du schéma de sécurité indiqué dans la fiche d'agent. L’A2A prend en charge les schémas de sécurité harmonisés sur la spécification OpenAPI, tels que les clés API, OAuth 2.0 et OpenID Connect Discovery.

Lorsque l’agent client a été correctement authentifié, l’agent distant est responsable de l’[autorisation](https://www.ibm.com/fr-fr/think/topics/authentication-vs-authorization) et de l’octroi des autorisations de contrôle d’accès.

### Communication

La communication commence par un agent client qui envoie une tâche à l'agent distant choisi. La communication d'agent à agent se fait via HTTPS pour un échange sécurisé, en utilisant JSON-RPC (Remote Procedure Call) 2.0 comme format pour l'échange de données.

L’agent distant traite ensuite la tâche. S’il a besoin de plus d’informations, il en informe l’agent client pour lui demander des informations supplémentaires. Une fois la tâche terminée, l’agent distant envoie un message à l’agent client, ainsi que tous les artéfacts générés.

L’A2A fournit également des fonctionnalités de gestion pour les tâches plus complexes qui ne peuvent pas être effectuées immédiatement, telles que celles qui nécessitent une intervention humaine ou impliquent plusieurs étapes. Dans le cas de tâches de longue durée qui prennent des heures ou des jours, ou si un agent client est déconnecté, le protocole A2A permet des mises à jour asynchrones via des notifications push envoyées à un webhook sécurisé fourni par le client. Pour les sorties volumineuses ou longues, ou les mises à jour de statut continues, le protocole A2A prend en charge la diffusion en temps réel à l’aide d’[évènements envoyés par le serveur (SSE)](https://community.ibm.com/community/user/blogs/abishek-s/2024/11/28/the-power-of-server-sent-events-sse).

## Avantages du protocole A2A

Le protocole Agent2Agent offre les avantages suivants pour la communication des agents au sein des systèmes d’IA réels :

- Confidentialité

<!-- -->

- Intégration transparente

<!-- -->

- Sécurité

### Confidentialité

Le protocole traite l’IA agentique comme des agents opaques. Cette opacité signifie que les agents autonomes peuvent collaborer sans avoir à révéler leur fonctionnement interne, comme la mémoire interne, la logique propriétaire ou les mises en oeuvre d’outils particulières. Cela permet de préserver la [confidentialité des données](https://www.ibm.com/fr-fr/think/topics/data-privacy) et la propriété intellectuelle.

### Intégration transparente

L’A2A repose sur des normes établies, notamment HTTP, JSON-RPC et SSE. Cela facilite l’adoption du protocole par les entreprises et contribue à garantir leur compatibilité avec leur infrastructure technologique actuelle.

### Sécurité

Le protocole Agent2Agent est conçu dans un souci de sécurité. Il prend en charge les mécanismes d’authentification et d’autorisation dédié aux entreprises et permet un échange d’informations sécurisé.

## L’avenir de l’A2A

Le protocole A2A n'en est qu'à ses débuts. Les entreprises peuvent donc s'attendre à des améliorations à mesure que le protocole évolue. Parmi ces améliorations, citons l’inclusion formelle de schémas d’autorisation et d’identifiants facultatifs dans les fiches d’agent, une méthode de vérification dynamique des compétences imprévues ou non prises en charge, la prise en charge de la négociation dynamique de l’[expérience utilisateur](https://www.ibm.com/fr-fr/think/topics/user-experience) dans les tâches (comme l’ajout de son ou de vidéo en cours de conversation), et en améliorant les méthodes de notifications push et la fiabilité de la diffusion.3

Pour en savoir plus, consultez le [site officiel d’A2A](https://a2aproject.github.io/A2A/) et découvrez les concepts clés et les spécifications du protocole, parcourez les tutoriels [Python](https://developer.ibm.com/languages/python/) et téléchargez les kits de développement logiciel. L’A2A dispose également d'un [site Github](https://github.com/a2aproject/a2a-samples) comprenant des exemples de code et des démonstrations.
