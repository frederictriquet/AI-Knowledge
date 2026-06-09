> Source : https://www.ibm.com/fr-fr/think/topics/beeai

# Qu’est-ce que BeeAI ?

BeeAI est une plateforme [open source](https://www.ibm.com/fr-fr/think/topics/open-source) qui permet de découvrir, d’exécuter et de partager des [agents d’IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) de manière centralisée, sur tous les cadres des exigences. Développé par IBM, BeeAI est basé sur le protocole ACP (Agent Communication Protocol) et hébergé sur la Linux Foundation. Les équipes peuvent utiliser le cadre des exigences BeeAI pour déployer des agents en dehors de leurs écosystèmes respectifs.

## Que fait BeeAI ?

BeeAI fournit aux développeurs individuels et aux équipes une plateforme indépendante du cadre sur laquelle ils peuvent trouver, déployer et partager des agents d’[intelligence artificielle (IA)](https://www.ibm.com/fr-fr/think/topics/artificial-intelligence). La plateforme a été conçue pour relever les trois principaux défis liés à la collaboration avec des agents d’IA :

- **Écosystèmes cloisonnés :** chaque agent existe dans son propre cadre. BeeAI rassemble les agents dans un espace de travail centralisé pour rationaliser l’[orchestration des agents IA](https://www.ibm.com/fr-fr/think/topics/ai-agent-orchestration).

- **Évolutivité limitée :** BeeAI permet aux utilisateurs de déployer des agents sans avoir à gérer des procédures de configuration compliquées et personnalisées.

- **Découverte fragmentée :** les agents BeeAI sont situés dans un centre de découverte centralisé, ce qui facilite la recherche et l’expérimentation de l’[IA agentique](https://www.ibm.com/fr-fr/think/topics/agentic-ai).

Les développeurs individuels peuvent utiliser Bee pour rationaliser le processus d’exploration et de déploiement d’agents à utiliser dans le cadre de l’[automatisation agentique](https://www.ibm.com/fr-fr/think/topics/agentic-automation) et dans d’autres contextes. Pendant ce temps, les équipes peuvent partager le même espace de travail BeeAI via une instance centralisée pour collaborer en temps réel tout en gérant de manière centralisée les connexions et les [API](https://www.ibm.com/fr-fr/think/topics/api) de [grands modèles de langage (LLM)](https://www.ibm.com/fr-fr/think/topics/large-language-models).

Le catalogue de la communauté héberge tous les agents BeeAI disponibles sur la plateforme, à partir desquels ils peuvent être déployés sans configuration complexe. Les interfaces utilisateur standardisées permettent des expériences utilisateur cohérentes, et les conteneurs standard permettent aux développeurs de regrouper les agents à partir de n’importe quel cadre des exigences tout en contournant les problèmes de compatibilité.

## Utiliser des agents dans BeeAI

L’équipe de recherche d’IBM a développé BeeAI autour d’une suite de fonctionnalités principales qui lui permettent de fonctionner en tant qu’espace de travail agentique. En voici quelques exemples :

### Catalogue d’agents

Le référentiel d’IA agentique de BeeAI rassemble les équipes dans un espace de travail centralisé pour assurer des [workflows](https://www.ibm.com/fr-fr/think/topics/workflow) multi-agents plus fluides. Le catalogue d’agents BeeAI est l’un de ses principaux atouts : il est consultable et détaille les fonctionnalités de chaque agent proposé. Les développeurs peuvent identifier les schémas d’utilisation et sélectionner les agents en conséquence.

Les agents sont triés par type. BeeAI présente les agents conversationnels par le biais d’une interface de [chatbot](https://www.ibm.com/fr-fr/think/topics/chatbots). Les agents autonomes, quant à eux, constituent l’épine dorsale de nombreux workflows, car ils sont conçus pour fonctionner [de manière autonome](https://www.ibm.com/fr-fr/think/topics/automation) après avoir reçu une seule instruction.

Le catalogue communautaire recueille les agents créés par les utilisateurs. Ces deniers peuvent également envoyer les agents qu’ils ont créés sur GitHub par le biais de l’interface BeeAI.

### Environnements agnostiques

BeeAI utilise l’ACP pour normaliser l’utilisation des agents, quel que soit leur cadre. Les développeurs utilisent les outils qu’ils préfèrent avec les agents de leur choix. L’assistant de configuration interactif rationalise le processus de création d’environnement pour mettre à la disposition des équipes un espace de travail partagé pour leurs agents IA.

#### Configuration

Le processus de configuration comprend la saisie de clés d’API, des recommandations pour la [sélection du modèle](https://www.ibm.com/fr-fr/think/topics/model-selection), les tests de connexion et des options spécifiques au fournisseur telles que la fenêtre contextuelle d’Ollama. Parmi les fournisseurs de LLM disponibles, citons [Claude](https://www.ibm.com/fr-fr/think/topics/claude-ai) d’Anthropic, [GPT](https://www.ibm.com/fr-fr/think/topics/gpt) d’OpenAI, [DeepSeek](https://www.ibm.com/fr-fr/think/topics/deepseek) et watsonx d’IBM. Le Llama3 de Meta est disponible par le biais d’une connexion Ollama locale.

Les utilisateurs peuvent importer des agents localement ou à partir des dépôts GitHub, d’autres cadres tels que [LangChain](https://www.ibm.com/fr-fr/think/topics/langchain), et même créer leurs propres agents pour les utiliser dans BeeAI.

#### Exécuter les agents

BeeAI exécute chaque agent dans son propre conteneur avec des limites de ressources définies, ce qui permet une construction modulaire de [systèmes multi-agents](https://www.ibm.com/fr-fr/think/topics/multiagent-system). Les options d’entrée incluent un mode interactif pour communiquer avec l’agent, ainsi qu’une entrée multi-ligne pour partager des extraits de code Python et d’autres langages. Les interfaces utilisateur standardisées font que les interactions avec les agents au sein des [workflows agentiques](https://www.ibm.com/fr-fr/think/topics/agentic-workflows) sont prévisibles.

L’observabilité est intégrée à la plateforme grâce à la diffusion en continu de journaux en temps réel à partir de tout agent en cours d’exécution. BeeAI collecte des données de télémétrie avec OpenTelemetry et les envoie à l’instance Arize Phoenix désignée.

## Comment fonctionne BeeAI ?

BeeAI est conçu autour d’une expérience locale, hébergeant les agents sur divers appareils ou sur site pour donner aux utilisateurs un contrôle total sur leurs données. Voici les principaux composants :

- **Agents :** les agents dans BeeAI sont conteneurisés et communiquent grâce à l’ACP. L’une des caractéristiques déterminantes des agents IA est leur capacité à appeler des outils selon les besoins pour étendre leurs fonctionnalités.

- **Serveur BeeAI :** le serveur orchestre les agents, gère les cycles de vie et les configurations, achemine la communication entre les agents et les clients, et collecte les données de télémétrie.

- **Interface de ligne de commande et interface utilisateur BeeAI :** les utilisateurs interagissent avec BeeAI en deux modes. L’interface de ligne de commande (CLI) facilite l’utilisation de scripts et le contrôle des commandes, tandis que l’interface utilisateur graphique (UI) gère les interactions plus intuitives telles que les chats.

- **Intégration Python :** Le SDK ACP (kit de développement logiciel) permet aux développeurs d’intégrer BeeAI à leurs applications basées sur Python. BeeAI peut gérer les [workflows](https://www.ibm.com/fr-fr/think/topics/workflow) d’agent dans le contexte des applications Python (par exemple, pour l’[automatisation des tâches](https://www.ibm.com/fr-fr/think/topics/task-automation)).

- **Arise Phoenix pour la surveillance :** disponible dans BeeAI, Phoenix est un outil open source pour suivre et surveiller le comportement des agents.
