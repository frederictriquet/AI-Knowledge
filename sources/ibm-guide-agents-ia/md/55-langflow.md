> Source : https://www.ibm.com/fr-fr/think/topics/langflow

# Qu’est-ce que LangFlow ?

LangFlow est un outil [open source](https://www.ibm.com/fr-fr/think/topics/open-source) [low code](https://www.ibm.com/fr-fr/think/topics/low-code) permettant de créer des [agents IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) et d’autres applications d’IA via une interface visuelle. LangFlow aide à orchestrer [grands modèles de langage](https://www.ibm.com/fr-fr/think/topics/large-language-models), [API](https://www.ibm.com/fr-fr/think/topics/api), [bases de données vectorielles](https://www.ibm.com/fr-fr/think/topics/vector-database) et composants personnalisés dans les [workflows agentiques](https://www.ibm.com/fr-fr/think/topics/agentic-workflows), sans compétences avancées en programmation.

## À quoi sert LangFlow ?

LangFlow est utilisé pour créer des applications d’IA agentique au sein d’une interface utilisateur graphique (GUI) low code ou [no-code.](https://www.ibm.com/fr-fr/think/topics/no-code) Les utilisateurs connectent les composants entre eux, et les connexions déterminent le flux de données dans l’application. 

S’il crée un [chatbot](https://www.ibm.com/fr-fr/think/topics/agentic-ai) d’[IA agentique](https://www.ibm.com/fr-fr/think/topics/chatbots) pour automatiser le service client, l’utilisateur peut d’abord connecter une interface de chat à un [grand modèle de langage (LLM)](https://www.ibm.com/fr-fr/think/topics/large-language-models).

Il peut également relier le LLM à la [base de données vectorielle](https://www.ibm.com/fr-fr/think/topics/vector-database) de son entreprise pour créer un système de [génération augmentée par récupération (RAG)](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation) permettant au LLM de consulter des données telles que l’historique des commandes clients. 

Le LLM peut accéder aux outils grâce aux [clés d’API](https://www.ibm.com/fr-fr/think/topics/api-key), qui peuvent également être intégrées au [workflow d’IA](https://www.ibm.com/fr-fr/think/topics/ai-workflow) comme composants modulaires. Pour compléter l’application agentique, le LLM sera lié à un second composant de chat pour renvoyer la sortie à l’utilisateur par le biais du chatbot.

## Principales caractéristiques et fonctions de LangFlow

LangFlow doit son succès à ses caractéristiques et fonctionnalités conviviales : 

- Interface visuelle low code ou no-code

<!-- -->

- Nombreuses intégrations 

<!-- -->

- Bibliothèque de composants 

<!-- -->

- Flux exportables 

<!-- -->

- Code source ouvert

### Interface visuelle low code ou no-code

LangFlow doit sa facilité d’utilisation à sa présentation. Les utilisateurs peuvent créer des applications d’IA grâce à une interface visuelle modulaire par glisser-déposer.

Chaque composant du processus [de machine learning (ML)](https://www.ibm.com/fr-fr/think/topics/machine-learning) est positionné en séquence et connecté aux autres composants selon les besoins du workflow d’IA. 

L’interface visuelle transforme un projet de codage complexe en [organigramme](https://www.ibm.com/fr-fr/think/topics/flowchart) intuitif, doté de connexions qui déterminent le flux de données à travers le système d’[intelligence artificielle](https://www.ibm.com/fr-fr/think/topics/artificial-intelligence) (IA).

Les débutants peuvent utiliser LangFlow pour rationaliser l’[orchestration de l’IA](https://www.ibm.com/fr-fr/think/topics/ai-orchestration) en ajoutant différents modèles, composants et sources de données selon les besoins. Par ailleurs, les utilisateurs [Python](https://developer.ibm.com/languages/python/) peuvent créer c dans LangFlow. 

À titre d’exemple no-code, LangFlow permet aux utilisateurs d’effectuer [un réglage limité](https://www.ibm.com/fr-fr/think/topics/hyperparameter-tuning) des hyperparamètres pour les LLM de leur choix à l’aide d’un simple curseur.

Les utilisateurs peuvent ajuster la [température](https://www.ibm.com/fr-fr/think/topics/llm-temperature) (un hyperparamètre qui contrôle le degré d’aléatoire dans une sortie LLM) avec un simple coup de pouce vers la gauche ou la droite.

#### LangFlow est-il considéré comme du codage dynamique ?

LangFlow diffère du [vibe coding](https://www.ibm.com/fr-fr/think/topics/vibe-coding), qui consiste pour l’utilisateur à donner des instructions à un LLM avec des prompts en langage naturel pour générer du code. L’utilisateur indique au LLM ce que le code devra faire et s’appuie sur le LLM pour générer ce code. 

LangFlow permet aux utilisateurs de créer l’application d’IA qu’ils souhaitent et remplace le codage par des composants modulaires prédéfinis. Les utilisateurs peuvent toujours utiliser du code pour créer des composants personnalisés et parvenir à une [automatisation agentique](https://www.ibm.com/fr-fr/think/topics/agentic-automation) plus avancée.

### Des intégrations nombreuses

LangFlow offre une grande flexibilité grâce à son large éventail d’’intégrations. LangFlow prend en charge l’intégration avec de nombreux cadres ML et couvre le même éventail d’API, de bases de données vectorielles et d’autres options de connexion que son cadre parent [LangChain](https://www.ibm.com/fr-fr/think/topics/langchain). 

LangFlow prend également en charge le chaînage de LLM : plusieurs modèles sont connectés en séquence au sein d’un seul et même pipeline.

Ne pas confondre le chaînage avec l’orchestration multi-agents. Avec cette dernière, plusieurs agents, dont chacun peut utiliser son propre LLM, ses propres outils ou sources de données, collaborent sur une tâche partagée. La conception modulaire de LangFlow prend en charge les deux approches.

#### Quelle est la différence entre LangFlow et LangChain ?

[LangChain](https://www.ibm.com/fr-fr/think/topics/langchain) est un cadre de ML open source à base de code pour le développement de l’IA. LangFlow est un outil visuel qui s’appuie sur des cadres tels que LangChain pour permettre aux utilisateurs de créer et de prototyper rapidement leurs applications LLM.

LangFlow a été développé à l’origine sur LangChain et y est toujours étroitement lié, mais il prend désormais en charge d’autres cadres et intégrations. 

[LangGraph](https://www.ibm.com/fr-fr/think/topics/langgraph) est une plateforme de la même famille qui permet de construire des systèmes agentiques. Mais au lieu d’utiliser une interface graphique modulaire, LangGraph représente les systèmes agentiques sous forme de graphes, tout en offrant un contrôle plus granulaire.

### Bibliothèque de composants

La bibliothèque de composants contient tous les composants que les utilisateurs peuvent ajouter à leurs workflows : des LLM tels que la famille [GPT](https://www.ibm.com/fr-fr/think/topics/gpt) d’OpenAI, Llama et autres modèles Meta, interfaces de chat, calculatrices, navigateurs Web et plus encore. LangFlow regroupe les composants en deux catégories : 

- **Les composants centraux**, qui constituent l’épine dorsale de la plupart des créations LangFlow. 

<!-- -->

- **Offres groupées** proposées par les fournisseurs pour prendre en charge certaines intégrations tierces.

### Flux exportables

Les projets LangFlow peuvent être exportés sous forme de flux au format JSON. Les créateurs peuvent exporter leurs flux et les partager avec d’autres utilisateurs, qui peuvent ensuite les importer dans leur propre instance LangFlow, les utiliser et les modifier. Les flux exportables améliorent la collaboration et rationalisent le workflow des projets en rendant les flux réutilisables.

### Open source

Comme son cadre parent LangChain, LangFlow est open source, ce qui signifie que son code est accessible au public à des fins d’inspection, de contribution et de modification. Les outils d’IA open source permettent d’accroître l’explicabilité de l’IA et d’assurer une transparence opérationnelle.

Cependant, utiliser un LLM ou tout autre composant à source fermée dans LangFlow ne permet pas le même type d’accès à son fonctionnement interne.

## Cas d’utilisation de LangFlow

La facilité d’utilisation de LangFlow en fait un outil idéal pour rationaliser et [automatiser les workflows](https://www.ibm.com/fr-fr/think/topics/workflow-automation) avec l’IA agentique. Voici quelques cas d’utilisation concrets de LangFlow : 

- Prototypage rapide

<!-- -->

- Développement d’agents IA 

<!-- -->

- Applications RAG 

<!-- -->

- Automatisation du service client

### Prototypage rapide

L’interface graphique par glisser-déposer de LangFlow se prête bien au prototypage rapide des applications d’IA. Les utilisateurs peuvent élaborer un pipeline avec les composants modulaires de LangFlow, le partager avec d’autres, le tester et itérer si nécessaire.

L’intégration avec [Hugging Face](https://www.ibm.com/fr-fr/think/topics/hugging-face) Spaces permet également une démonstration rapide du ML.

### Le développement d’agents d’IA

L’un des principaux cas d’utilisation de LangFlow est le développement d’agents IA no-code. Grâce à la bibliothèque de composants, les utilisateurs peuvent connecter le LLM à des outils, des bases de données et d’autres modules complémentaires, pour permettre à l’agent d’accéder à ce dont il a besoin pour remplir la fonction prévue.

Les utilisateurs peuvent également relier les LLM ou créer des systèmes multi-agents.

### Applications RAG

Grâce aux composants d’interfaces de chat et de bases de données vectorielles, LangFlow peut facilement créer des systèmes [RAG](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation "RAG"). Les prompts en langage naturel sont convertis en [embeddings](https://www.ibm.com/fr-fr/think/topics/embedding), que le modèle de récupération utilise pour interroger la base de données vectorielle connectée. 

La base de données contient des informations relatives au cas d’utilisation du système. Par exemple, un système RAG conçu pour aider les nouveaux employés à s’intégrer se référera aux documents de formation dans le jeu de données. Ensuite, le LLM combinera les données récupérées grâce au prompt pour renvoyer une sortie en langage naturel à l’utilisateur.

### L’automatisation du service client

Les chatbots sont souvent utilisés pour automatiser le service client.

Les clients interagissent d’abord avec le chatbot, qui récupère les données pertinentes telles que l’historique des commandes et les informations sur les produits. Si la requête du client s’avère trop complexe, le chatbot peut la faire remonter à un agent humain. 

Les utilisateurs LangFlow peuvent rapidement créer un chatbot de service client avec quelques composants seulement : 

1.  Une **entrée de chat** reçoit les requêtes des clients en langage naturel.
2.  Un **composant embedding** convertit l’entrée en plongement vectoriel pour la recherche sémantique.
3.   Une **base de données vectorielles** contenant des données sur les entreprises est interrogée pour trouver des embeddings similaires.
4.   Un **LLM** combine les données récupérées avec la requête du client pour générer une réponse. 
5.   Une **sortie de chat** renvoie la réponse à l’utilisateur en langage naturel.
