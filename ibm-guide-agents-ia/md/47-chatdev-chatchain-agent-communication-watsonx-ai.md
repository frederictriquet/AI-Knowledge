> Source : https://www.ibm.com/fr-fr/think/tutorials/chatdev-chatchain-agent-communication-watsonx-ai

# Utiliser ChatDev ChatChain pour communiquer avec les agents sur IBM watsonx.ai

Dans ce tutoriel, nous montrons comment créer un système d’IA collaboratif à l’aide du [cadre des exigences](https://www.ibm.com/fr-fr/think/topics/chatdev) ChatDev et découvrons sa structure de communication d’agent basée sur les rôles, ChatChain. ChatDev utilise un agent IA avec des rôles affectés pour simuler une société de logiciels virtuelle. Chaque agent intelligent collabore avec d’autres par le biais d’une communication structurée, en suivant un workflow séquentiel basé sur les phases du cycle de vie du développement logiciel.

Pour alimenter ces agents, nous avons intégré le logiciel [IBM watsonx.ai](https://www.ibm.com/fr-fr/products/watsonx-ai) interface de programmation des applications (API) en tant que backend de modèle. En tirant parti d’une intégration de watsonx.ai avec Hugging Face, nous avons configuré le cadre des exigences pour utiliser [Llama-4-Maverick](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8) afin de générer une solution logicielle simple. Cet exemple sert de base pour la découverte de ChatChain et d'autres mécanismes de communication internes des agents qui guident le comportement et la prise de décision des agents tout au long du workflow. 

À la fin de ce tutoriel, vous devez avoir une expérience pratique de la configuration et de l’exécution de ChatDev, et une compréhension plus claire de la façon dont les protocoles de communication des agents permettent une collaboration multi-agents efficace et fiable.

**IA collaborative** : systèmes d'intelligence artificielle conçus pour fonctionner aux côtés des humains ou des agents IA, souvent en utilisant l'apprentissage profond ou d'autres techniques avancées pour permettre la coopération, la prise de décision partagée et la résolution conjointe de problèmes afin d'atteindre des objectifs communs. 

**Collaboration multi-agent : **plusieurs agents autonomes qui partagent des informations et se coordonnent pour atteindre un objectif partagé. Ces agents peuvent avoir différents niveaux de connaissances, de capacités et de perspectives, et leur collaboration implique souvent la négociation, la planification et l'action coordonnée.

**Agents de jeu de rôle** : des agents IA qui simulent des rôles ou des personnages spécifiques pour interagir et collaborer de manière axée sur des objectifs. Ces rôles peuvent refléter des professions ou des personnages réels, ce qui permet des interactions plus contextuelles et axées sur les objectifs. 

**Protocoles de communication des agents : **des normes ou des cadres des exigences qui définissent la façon dont les agents IA interagissent entre eux en échangeant des messages de données structurés. Ces protocoles régissent le format, la sémantique et les règles de communication pour les agents qui se coordonnent au sein de systèmes multi-agents.

## IA collaborative dans Chatdev

[ChatDev](https://github.com/OpenBMB/ChatDev) est une implémentation de l’IA collaborative basée sur les rôles, dans laquelle les agents individuels assument des rôles spécialisés pour travailler à la réalisation d’un objectif partagé. Cette conception reflète les principes de l’intelligence collective (une collaboration essentiellement efficace) et positionne ChatDev comme une ressource précieuse pour étudier et faire progresser ce domaine.

ChatDev est un cadre des exigences multiagent open source développé par OpenBMB, une initiative de recherche axée sur l'avancement des outils d'IA et de l'intelligence artificielle générale (AGI). Le cadre utilise le processus de développement de logiciels comme domaine pratique pour étudier les agents IA collaboratifs. Chaque agent est alimenté par un grand modèle de langage (LLM) et invité à assumer des rôles spécifiques tels que PDG, directeur technique, concepteur, testeur et programmeur.[1](#f01)

A partir d’une brève entrée utilisateur descriptive, ces agents collaborent pour concevoir, mettre en œuvre et tester de manière itérative un projet logiciel complet. Chaque agent est implémenté en tant que classe Python qui communique de manière séquentielle à l’aide de prompts en langage naturel structurés. Ces invites suivent des modèles prédéfinis qui incluent le rôle de l’agent, des instructions spécifiques à la tâche et le contexte pertinent des interactions précédentes. Cette stratégie de modèle permet d’assurer la continuité et la cohérence en intégrant l’identité du rôle et la mémoire partagée dans le prompt lui-même par embedding.

L’équipe d’agents spécialisés de ChatDev travaille ensemble pour générer une solution logicielle simple à partir d’une entrée utilisateur d’une seule ligne décrivant son idée. 

**Entrée utilisateur : « Créer une application de liste de tâches » → Délégués du PDG au directeur technique → Attribution du directeur technique au développeur → Le développeur écrit le code → Le testeur valide**

### Comment fonctionne ChatDev

Les interactions avec les agents sont orchestrées par ChatChain, la logique de coordination personnalisée au sein du cadre des exigences ChatDev. La communication entre les agents se fait via un dialogue à plusieurs tours, ou un système de passage de messages, où les agents échangent séquentiellement des messages JSON structurés. Ces messages représentent des sorties et des mises à jour de contexte et agissent comme un tampon de mémoire partagée, permettant aux agents de s’appuyer sur les sorties des uns et des autres pendant les phases de développement.

Cette architecture permet une communication cohérente et une collaboration qui prend en compte le contexte en combinant les langages naturels et de programmation pour mener à bien le projet de bout en bout. Le processus repose sur une communication multi-agent coordonnée, avec des mécanismes internes agissant comme des protocoles pour orchestrer une [communication efficace d'agent IA](https://www.ibm.com/fr-fr/think/topics/ai-agent-communication) pour mener à bien chaque phase. 

Les utilisateurs peuvent surveiller et examiner le [workflow agentique](https://www.ibm.com/fr-fr/think/topics/agentic-workflows) à l’aide de l’outil Visualizer de ChatDev, une interface Web basée sur Flask qui prend en charge à la fois l’analyse post-exécution et la surveillance en temps réel. Le visualiseur propose plusieurs modes de visualisation, tels que Log Viewer pour inspecter les interactions avec les agents en temps réel, un revoir Viewer pour visualiser les journaux de conversation multi-agents enregistrés et un ChatChain Viewer pour examiner le flux de coordination des tâches. Cette interface interactive permet aux utilisateurs de déboguer, d’expérimenter et d’étudier la collaboration multi-agent dans un environnement structuré via un navigateur local.

### Remarque sur la compatibilité des modèles et la variabilité des résultats

Ce tutoriel utilise une version personnalisée de ChatDev adaptée spécifiquement à l’API IBM watsonx.ai. Bien que le ChatDev de base prenne en charge plusieurs fournisseurs de modèles, cette version a été modifiée à l’aide d’une approche pragmatique de « vibecoding », ce qui la rend fonctionnelle mais non testée de manière exhaustive sur tous les scénarios.

**Les principales adaptations comprennent :**

- Encadrement de l’API IBM watsonx pour se conformer à l’interface LLM attendue de ChatDev.

<!-- -->

- Ajustement des modèles d'invite pour travailler avec les exigences en matière de jetons et de formatage de l'API IBM watsonx.ai

<!-- -->

- Modification de la logique de sélection des modèles pour prendre en charge IBM watsonx.ai en tant qu’option de backend de modèle.

Cette implémentation montre comment ChatDev peut être étendu pour prendre en charge d’autres fournisseurs de LLM. D'autres fournisseurs de modèles (par exemple, OpenAI, Ollama) n'ont pas été testés avec cette version personnalisée de ChatDev et nécessiteraient des ajustements au niveau du code.

Comme pour de nombreux workflows d’IA générative, la production peut varier d’une exécution à l’autre. Alors que les agents produisent généralement un code et une documentation cohérents et bien structurés, les applications qui en résultent peuvent nécessiter un ajustement manuel pour devenir pleinement fonctionnelles. Des facteurs tels que la conception des prompts, la complexité des tâches et la variabilité inhérente des réponses des LLM contribuent tous à cette imprévisibilité.

Ce tutoriel sert d’introduction pratique aux systèmes multi-agents collaboratifs, en se concentrant sur la façon dont les agents communiquent et se coordonnent dans ChatDev. Il ne s’agit pas d’une solution prête pour la production, mais plutôt d’une base pour l’apprentissage, l’expérimentation et la découverte de la collaboration d’agents basée sur les LLM. Nous remercions les chercheurs à l'origine de ChatDev d'avoir mis leur travail en open source, rendant ainsi possible ce type d'exploration.

## Étapes

### Étape 1. Configurer votre environnement

Bien que ChatDev soit conçu pour être multiplateforme, les utilisateurs peuvent rencontrer des problèmes spécifiques à la plateforme lors de la configuration ou de l’exécution. Par exemple, PowerShell sous Windows peut nécessiter des ajustements des commandes shell destinées aux systèmes basés sur Unix. Les variations dans le système d’exploitation, les versions de Python et les architectures de processeur peuvent également affecter les performances ou le comportement. Pour garantir une configuration et une utilisation fluides, les utilisateurs doivent consulter la documentation officielle de ChatDev et les guides d’installation pour obtenir des informations de dépannage et des instructions spécifiques à l’environnement.

Dans cette optique, commençons par configurer l’environnement pour exécuter l’application. Vous pouvez suivre ces étapes dans le fichier Markdown dans le [dossier projet sur GitHub](https://github.com/IBM/ibmdotcom-tutorials/tree/main/docs/tutorials/projects/chatdev_watsonx_tutorial_) ou en suivant ici. 

1.   Assurez-vous que Python 3.11 est installé sur votre système.\
    \> Vous pouvez vérifier votre version de Python en utilisant`version python 3` commande. 
2.  Cloner le [référentiel Github](https://github.com/IBM/ibmdotcom-tutorials/tree/main).\
    \> Pour obtenir des informations détaillées sur le clonage d'un dépôt, consultez la [documentation GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository). 
3.  Verify que la structure du projet ressemble à ce qui suit :

```
tutorials/projects/chatdev_watsonx/ 

├── camel/ 
│   ├── model_backend.py  # Unified interface for interacting with multiple AI models 
│   ├── typing.py         # Defines various type classes including supported AI models  
│   ├── configs.py        # Defines the model parameters based on model interface 
│   ├── utils.py          # Various utility functions including model token limit configuration 
│   └── ... 
├── Visualizer/ 
│   └──app.py             # Runs a Flask application in a local web browser to view logs and ChatChain  
├── WareHouse             # Where the generated software is saved  
├── run.py                # Application entry point 
└── chatdev_watsonx.md    # A markdown version of this tutorial
```

### Étape 2. Obtenir les identifiants de l’API watsonx

1.  Connectez-vous à [watsonx.ai](https://dataplatform.cloud.ibm.com/registration/stepone?context=wx&apps=all) en utilisant votre compte IBM Cloud 
2.  Créer un [projet watsonx.ai](https://www.ibm.com/docs/en/watsonx/saas?topic=projects-creating-project). \> Prenez note de l'identifiant de votre projet dans Projet \> Gérer \> Général \> ID de projet. \
    Vous aurez besoin de cet identifiant pour ce tutoriel.
3.  Créez une instance de service d’exécution [watsonx.ai](https://cloud.ibm.com/catalog/services/watsonxai-runtime) (choisissez le plan Lite, qui est une instance gratuite).
4.  Générez une [clé API](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html) watsonx .
5.  Associez le service d’exécution watsonx.ai au projet que vous avez créé dans [watsonx.ai](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/assoc-services.html?context=cpdaas). 

### Étape 3. Créer un environnement virtuel

À partir du répertoire de projet du tutoriel, créez un environnement virtuel à l’aide de Python 3.11 :

```bash
  python3.11 -m venv venv 
source venv/bin/activate
```

### Étape 4. Installer le fichier Requirements.TX

Cela installe les dépendances du projet.

```bash
  pip install -r requirements.txt 
```

### Étape 5. Définir les variables d’environnement pour l’intégration des LLM

La variable est définie pour la session en cours du terminal (la fermeture du terminal les réinitialisera).

Bien que ce tutoriel utilise IBM watsonx.ai comme backend de modèle, le cadre des exigences sous-jacent de ChatDev a été conçu à l'origine pour prendre en charge plusieurs fournisseurs LLM, y compris OpenAI par défaut. Certaines parties du code (par exemple, la logique de sélection des modèles ou les interfaces partagées) font toujours référence à`OpenAI_API_KEY` variable d’environnement. Pour éviter les erreurs d'exécution, une valeur fictive est requise même si OpenAI n'est pas utilisé. 

```bash
export OPENAI_API_KEY="your_openai_api_key_or_dummy_value" 
export WATSONX_URL="https://us-south.ml.cloud.ibm.com" 
export WATSONX_APIKEY="your_watsonx_api_key" 
export WATSONX_PROJECT_ID="your_watsonx_project_id"
```

### Étape 6. (Facultatif) Exécuter l’application de visualisation pour l’interface ChatDev

Vous pouvez éventuellement exécuter le visualiseur de ChatDev, une interface graphique basée sur Flask qui vous permet d’inspecter les journaux des agents en temps réel, de Découvrir le workflow ou de revoir les boîtes de dialogue des agents enregistrées. Cet outil est utile pour déboguer, surveiller ou étudier les interactions avec les agents, mais il n’est pas requis pour exécuter le workflow multi-agent principal de ChatDev.

Pour lancer le visualiseur, vous devez d’abord installer Flash :

```bash
pip install flask
```

 

Ensuite, lancez l'application : 

```bash
python visualizer/app.py
```

 

Une fois en cours d’exécution, ouvrez un navigateur et accédez : `https://127.0.0.1:8000/`

### Étape 7. Configuration LLM (facultatif)

Remarque : ce tutoriel utilise une version de ChatDev préconfigurée pour utiliser l'API IBM watsonx.ai comme backend de modèle. Aucune configuration supplémentaire ni modification de la configuration du modèle n’est nécessaire pour que le tutoriel fonctionne correctement. Bien que personnalisable, la modification des configurations des LLM peut générer des productions incomplètes, incorrectes et variées.

ChatDev est construit à partir du cadre des exigences CAMEL, qui gère les rôles, les tâches et les interactions des agents avec les modèles de langage. L’implémentation originale utilise l’API OpenAI comme backend de modèle pour s’interfacer avec les modèles ChatGPT tels que GPT-4 et utilise GPT-3.5-turbo par défaut. Le projet open source est également conçu pour prendre en charge plusieurs modèles de fournisseurs LLM via une interface de modèle unifiée.

Passez cette étape si vous prévoyez d’utiliser la configuration IBM watsonx®.ai par défaut. Pour l'expérimentation, le type de modèle, les paramètres et les limites de token peuvent être ajustés pour fonctionner avec l'API IBM watsonx.

- **Type de modèle**

Pour tester différents **types de** modèles, mettez à jour`watsonx` entrée dans la`Type de modèle` enum in`camel/typing.py`

```python
# camel/typing.py 

class ModelType(Enum):
WATSONX = "meta-llama/llama-4-maverick-17b-128e-instruct-fp8" # Model identifier used by the Watsonx APIThe model parameters can be configured within camel/configs.py under the WatsonxConfig data class.
```

 

- **Paramètres de modèle**

Les **paramètres du** modèle peuvent être configurés dans`camel/configs.py`  dans le cadre de la `WatsonxConfig`  classe de données.

```python
# camel/configs.py 

@dataclass(frozen=True) 
class WatsonxConfig: 
"""Defines the parameters for generating completions using watsonx.ai models.""" 

temperature: float = 0.3 
top_k: int = 100 
top_p: float = 0.0
```

 

- **Limite de token**

Le **limite de** token pour le modèle peut être configurée dans le`camel/utils.py` .zip.

```python
# camel/utils.py 

def get_model_token_limit(model: ModelType) -> int: 
if model == ModelType.WATSONX: 
return 128000  # Token limit for Watsonx.ai models
```

### Étape 8. Exécuter le script pour générer une application

Cette étape exécute le workflow ChatDev principal. Lorsque vous exécutez ce script, les agents simulent un processus collaboratif de développement de logiciels basé sur vos entrées. Le code généré, la documentation et les artefacts associés seront enregistrés dans le répertoire WareHouse du projet. Vous pouvez inspecter les journaux ou revoir les conversations à l’aide du visualiseur.

Le script accepte les arguments suivants :

- `–-task`  : la description de la solution logicielle souhaitée

<!-- -->

- **`–-name`** : le nom de l’application ou du projet

<!-- -->

- **`–-model`** : le modèle IA à utiliser (doit être défini sur`watsonx` pour ce tutoriel)

Exemple de script :

```bash
python3 run.py --task "Build a simple website using Flask for a local bookstore called 'Turn the Page'. The website should include a homepage, an about page, and a product page. " --name "bookstore-site" --model "WATSONX"
```

**Remarque :** bien que l’architecture de ChatDev soit extensible, cette version du tutoriel ne fonctionne de manière fiable qu’avec`watsonx` . Son extension à d’autres fournisseurs de LLM nécessite de modifier`camel/model_backend.py` et la logique de configuration associée.

## Exemple de sortie

Le produit logiciel final est enregistré dans le`Entrepôt de données` dans un sous-répertoire portant le nom du projet, le nom de l'Entreprise par défaut et un horodatage.

Une sortie typique pourrait ressembler à ceci :

```
├── WareHouse/ 
└── bookstore-site_DefaultOrganization_20250506162935/ 
├── templates/      # Web page templates 
│   └── about.html 
│   └── index.html 
│   └── products.html 
├── manual.md      # The project’s README with instructions to run the software 
├── main.py        #The main application file for the website 
├── requirements.txt          # Project dependencies 
├── ChatChainConfig.json      # System design for collaborative agent workflows 
├── RoleConfig.json       # System prompts for agent roles 
├── PhaseConfig.json      # System prompts for phases 
└── bookstore-site_DefaultOrganization_20250506162935.log  # Log of the agent dialogue
```

*La sortie peut varier d'une exécution à l'autre en raison de la nature probabiliste des outils d'IA générative.*

Ce répertoire contient un projet logiciel complet généré par des agents IA. En plus du code d'application et de la documentation, vous trouverez des fichiers de configuration qui définissent :

- Rôles d’agent (RoleConfig.json)

<!-- -->

- Phases de développement (PhaseConfig.json)

<!-- -->

- Workflow d’agent (ChatChainConfig.json)

<!-- -->

- Un journal de boîte de dialogue qui peut être remanié dans le visualiseur de ChatDev

Pour exécuter l’application, suivez les instructions du`manuel.md` .zip.

## Comment ChatDev gère la communication avec les agents

L’interopérabilité des agents fait référence à la capacité des agents autonomes à comprendre, communiquer et collaborer efficacement à l’aide d’un protocole ou d’une norme partagé. Cette capacité est essentielle pour faire évoluer les systèmes d’IA agentique entre les tâches, l’intégration de grands jeux de données et la résolution de problèmes complexes de manière collaborative.

Les systèmes multi-agents utilisent souvent des protocoles de communication d'agent (ACP), qui fournissent des normes pour la communication d'agent à agent, en utilisant des mécanismes de communication internes tels que des langages de communication d'agent (ACL), tels que KQML ou FIPA-ACL. Ceux-ci définissent des « actes de communication » standard (par exemple, informer, demander, interroger) pour permettre un dialogue structuré et une coordination dans des environnements dynamiques.

ChatDev adopte cependant une approche différente. L’interopérabilité des agents est assurée grâce à ChatChain, un mécanisme de communication qui structure le workflow de coordination des agents. ChatChain gère un flux d’informations synchrone basé sur des tournants entre les agents, tout au long des étapes du processus de développement logiciel. Bien qu’il ne soit pas basé sur des ACL formels, ChatChain facilite un échange de type protocole en utilisant des conventions optimisées par LLM.

La communication avec les agents de ChatDev repose sur :

- **Modèles de prompts** : au début de chaque phase, les agents participants reçoivent chacun un prompt structuré indiquant leur rôle, leur tâche en cours et l’historique des conversations pertinentes. ChatDev utilise une invite pour intégrer ces informations directement dans le prompt, ce qui permet de maintenir la cohérence et l’alignement des objectifs entre les interactions.

<!-- -->

- **Formats de message structurés** : les agents communiquent via des messages JSON structurés qui encodent les sorties et les mises à jour de contexte. Cela permet un échange de données cohérent et une traçabilité tout au long du workflow.

<!-- -->

- **Conditionnement des rôles** : chaque agent est initialisé par un prompt qui renforce le rôle qui lui est assigné, y compris les responsabilités, les objectifs et les attentes comportementales, une stratégie en matière de déshallucination communicative.

Ensemble, ces mécanismes forment un cadre des exigences léger et Évolutif qui permet à ChatDev de générer des logiciels de manière collaborative à partir d’un prompt. Cela illustre comment la collaboration structurée basée sur les LLM peut stimuler les workflows traditionnels multi-agents.

### ChatChain

ChatChain est le principal mécanisme de communication de ChatDev, qui orchestre la séquence des interactions avec les agents tout au long du workflow de développement logiciel. Il structure la collaboration dans un processus itératif de type chaîne composé de phases distinctes, chacune avec des objectifs et des modèles de communication spécifiques.

Au cours de chaque phase, ChatChain démarre un dialogue à double agent entre deux agents spécifiques au rôle (par exemple, PDG et directrice technique, programmeur et réviseur). L’un agit généralement comme instructeur, l’autre comme assistant. Ces échanges structurés à plusieurs tournants rationalisent la prise de décision en collaboration tout en préservant la clarté des rôles et des responsabilités clairement définis. Les prompts pour chaque phase intègrent des instructions pour les tâches, une identité de rôle et un contexte pertinent pour guider l’interaction.

Le workflow global de ChatDev suit un modèle en cascade modifié, une méthodologie traditionnelle d’ingénierie logicielle qui divise les tâches en trois phases séquentielles : **conception**, **codage** et **test**. Les phases de codage et de test sont ensuite divisées en sous-tâches pour refléter un processus de développement itératif.

Par défaut, ChatChain divise le workflow en plusieurs étapes automatisées et ordonnées :

1.  **Analyse de la demande** : définissez la structure et les composants clés de l’application. \

2.  **Sélection du langage** : décidez quel langage de programmation utiliser pour créer et exécuter le logiciel.

3.  **Codage** : les agents écrivent le code pour créer l’application.

4.  **CodeCompleteAll** : compléter le code, y compris les fonctions ou classes manquantes.

5.  **CodeReview** : revoir et modifier le code pour les fonctionnalités.

6.  **Test** : exécutez le logiciel et modifiez le code en fonction du rapport de test.

7.  **EnvironmentDoc**: documenter l’environnement.

8.  **Manuel**: documenter et rédiger un manuel pour l’application.

Chaque phase est définie par un objet de configuration spécifiant les attributs qui définissent son comportement et ses propriétés. Par exemple, la`Need_reflect` l'attribut déclenche une réflexion post-phase où les agents analysent et affinent les résultats de l'interaction précédente.

### Invites de création

Pour guider une bonne communication entre les agents, ChatDev utilise l’invite d’initiation comme stratégie d’initialisation de l’agent avant chaque tour de sous-tâche. L'inception par Prompt engineering est une technique qui peut être utilisée pour intégrer les rôles, les objectifs et les responsabilités afin d'assurer une communication efficace avec les agents.

Prenons un exemple de la façon dont l'invite d'inception guide deux agents pour démarrer, maintenir et terminer une sous-tâche. 

#### Exemple d’invite d’initiation dans ChatDev

Avant chaque sous-tâche, chaque agent reçoit des prompts en tant que paramètres qui définissent des instructions, des caractéristiques, des responsabilités et des objectifs spécifiques au rôle. Deux exemples sont :`assistant_role_prompt` et`User_role_prompt` . Ces paramètres définissent les rôles et les responsabilités attribués à chaque agent participant à la conversation, en fonction du contexte de la tâche.

Voici les prompts de rôle système basés sur les rôles d'agent pour le formateur et l'assistant dans la phase LanguageChoose :

```json
// RoleConfig.json 

{ 
"Chief Executive Officer": [ 
"{chatdev_prompt}", 
"You are Chief Executive Officer. Now, we are both working at ChatDev and we 
share a common interest in collaborating to successfully complete a task 
assigned by a new customer.", 
"Your main responsibilities include being an active decision-maker on users' 
demands and other key policy issues, leader, manager, and executor. Your 
decision-making role involves high-level decisions about policy and strategy; 
and your communicator role can involve speaking to the organization's 
management and employees.", 
"Here is a new customer's task: {task}.", 
"To complete the task, I will give you one or more instructions, and you 
must help me to write a specific solution that appropriately solves the 
requested instruction based on your expertise and my needs." 
], 
"Chief Technology Officer": [ 
"{chatdev_prompt}", 
"You are Chief Technology Officer. we are both working at ChatDev. We share 
a common interest in collaborating to successfully complete a task assigned 
by a new customer.", 
"You are very familiar to information technology. You will make high-level 
decisions for the overarching technology infrastructure that closely align 
with the organization's goals, while you work alongside the organization's 
information technology (\"IT\") staff members to perform everyday operations.", 
"Here is a new customer's task: {task}.", 
"To complete the task, You must write a response that appropriately solves 
the requested instruction based on your expertise and customer's needs." 
],
```

 

Ces deux prompts initialisent le comportement souhaité des agents en décrivant leur rôle, leur expertise et leurs responsabilités. La stratégie de prompt guide également le comportement et les réponses des rôles respectifs pendant les interactions en donnant des instructions personnalisées sur la façon d’accomplir la tâche attribuée.

La communication avec les agents est guidée efficacement par des prompts minutieuses qui permettent de s’assurer que les deux rôles ont des attentes claires et peuvent collaborer efficacement.

### Déshallucination communicative

Pour remédier aux hallucinations de codage potentielles (génération de code incomplète ou incorrecte), ChatDev utilise un modèle de communication appelé déhallucination communicative. Ce schéma est essentiel pour structurer la conversation lors du processus de révision de code.

Le processus d'avis de code comporte deux phases,`CodeReviewComment` et`CodeReviewModification` . Les agents Code Review et Programmer effectuent des itérations entre ces deux phases jusqu’à ce que deux modifications consécutives restent inchangées, ou après 10 cycles. Prenons un exemple de déshallucination communicative tiré d'un journal de projet.

#### Exemple de déshallucination communicationnelle dans ChatDev

Dans cet exemple, l’agent de révision de code détecte une erreur dans la production de l’agent programmeur et la communique, ainsi que la suggestion de corriger le problème dans le code source. L’agent programmeur corrige ensuite sa sortie d’origine en fonction de ces commentaires.

Voici une partie de la production de l'agent de révision de code lors d'une itération du`CodeReviewComment` phase:

```
/* bookstore-site_DefaultOrganization_20250506162935.log */ 
... 

## Step 7: Highest Priority Comment 
A high-priority comment is that the templates directory needs to be created, and 
the HTML files should be placed inside it for the application to find and render 
them correctly. Without this setup, running `app.py` will result in a 
`TemplateNotFound` error because Flask looks for templates in a `templates` 
folder by default. 

## Step 8: Instructions for Fixing 
To fix this, create a new directory named `templates` in the same directory 
where `app.py`
```

 

L'agent programmeur répond avec le code corrigé au cours de la prochaine`CodeReviewModification` phase:

```
/* bookstore-site_DefaultOrganization_20250506162935.log */ 

Here is the list of your developed codes: main.py, index.html, about.html, products.html. 

### main.py 
```python 
... 

### templates/index.html 

```html 
<!-- 
Homepage template for Turn the Page bookstore website. 
Provides navigation links to other pages. 
--> 
... 

</html> 
### templates/about.html 
```html 
<!--  About page template for Turn the Page bookstore website. 
Provides information about the bookstore and navigation links. --> 
… 
</html>
```

 

Le réviseur et le programmeur continuent soit d’affiner le code pendant un maximum de 10 itérations, soit jusqu’à ce qu’un consensus soit atteint après deux phases de modification consécutives et identiques.

Le schéma de déshallucination de la communication permet de s’assurer que le code final est exact, complet et conforme aux exigences prévues grâce à un raffinement itératif, tout en facilitant l’exécution efficace des sous-tâches.

## Conclusion

Dans ce tutoriel, nous avons découvert comment ChatDev permet l’IA collaborative en simulant une société de logiciels virtuelle composée d’agents d’IA basés sur les rôles. En utilisant l’API IBM watsonx.ai comme backend du modèle, ChatDev guide les agents tout au long du cycle de vie du développement logiciel en utilisant une communication structurée dans les langues naturelles et de programmation.

Bien que ChatDev n’utilise pas de protocole formel de communication d’agent, il assure l’interopérabilité entre agents grâce aux capacités naturelles du LLM avec des techniques de communication d’agents telles que ChatChain, l’invite d’inception et la déshallucination conversationnelle. Cela souligne l'importance d'orchestrer une communication efficace avec les agents pour une collaboration réussie et améliorer la qualité des résultats. 

Avec des outils de visualisation intégrés pour surveiller et revoir les interactions avec les agents, ChatDev fournit une plateforme puissante pour étudier les workflows multi-agents et la dynamique de Teamworks . Elle démontre le potentiel réel de l’IA collaborative dans la création de logiciels et au-delà.
