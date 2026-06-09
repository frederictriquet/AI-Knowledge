> Source : https://www.ibm.com/fr-fr/think/tutorials/deploy-langgraph-react-agent-manage-it-support-tickets-watsonx-ai

# Déploiement d’un agent de support informatique LangGraph ReAct avec IBM Granite sur watsonx.ai

Dans ce tutoriel, vous allez créer un [agent IA ReAct (raisonnement et action)](https://www.ibm.com/fr-fr/think/topics/react-agent) avec le cadre d’exigences open source [LangGraph](https://www.ibm.com/fr-fr/think/topics/langgraph) en utilisant un [modèle IBM Granite](https://www.ibm.com/fr-fr/granite) via l’API [IBM watsonx.ai](https://www.ibm.com/fr-fr/products/watsonx-ai) [](https://www.ibm.com/fr-fr/think/topics/api) en Python. Le cas d’utilisation consiste à gérer les tickets d’assistance informatique existants et à en créer de nouveaux.

## Qu’est-ce qu’un agent ReAct ?

Un [agent d’intelligence artificielle (IA)](https://www.ibm.com/fr-fr/think/topics/ai-agents) désigne un système ou un programme capable d’exécuter des tâches de manière autonome pour le compte d’un utilisateur ou d’un autre système, en concevant son workflow agentique et en utilisant les outils disponibles. Les agents d’IA générative utilisent les techniques avancées de [traitement automatique du langage naturel](https://www.ibm.com/fr-fr/think/topics/natural-language-processing) (NLP) des [grands modèles de langage (LLM)](https://www.ibm.com/fr-fr/think/topics/large-language-models) pour comprendre et répondre aux entrées utilisateur, étape par étape, et déterminer quand faire appel à des outils externes. Le [raisonnement](https://www.ibm.com/fr-fr/think/topics/agentic-reasoning) est l’un des [principaux composants des agents IA](https://www.ibm.com/fr-fr/think/topics/components-of-ai-agents). Lors de l’acquisition de nouvelles informations par le biais d’un [appel d’outil](https://www.ibm.com/fr-fr/think/topics/tool-calling), d’une intervention humaine ou d’autres agents, le paradigme de raisonnement guide les prochaines étapes de l’agent.

À chaque action et réponse d’outil, le paradigme ReAct (raisonnement et action) demande aux agents de « réfléchir » et de planifier les étapes suivantes. Ce raisonnement lent, étape par étape, nous donne des informations sur la façon dont l’agent utilise le contexte actualisé pour formuler des conclusions. Comme ce processus de réflexion est continu, il est souvent appelé « boucle de réflexion, d’action et d’observation » et constitue une forme de [prompting par chaîne de pensée](https://www.ibm.com/fr-fr/think/topics/chain-of-thoughts).

## Utiliser LangGraph pour créer des agents React

Ce tutoriel utilisera [LangGraph](https://www.ibm.com/fr-fr/think/topics/langgraph), un cadre d’exigences open source conçu pour créer, déployer et gérer des workflows complexes d’agent d’IA générative. La fonction prédéfinie `create_react_agent` fournie par LangGraph permet de créer facilement un agent simple et personnalisé. Les agents ReAct simples, comme celui de ce tutoriel décrit à la figure 1, sont composés de deux nœuds. L’un des nœuds est responsable de l’appel du modèle et l’autre de l’utilisation des outils. Parmi les outils courants figurent l’outil prédéfini LangChain Wikipedia, l’outil DuckDuckGoSearchRun et même la [génération augmentée de récupération (RAG).](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation) Dans les cas avec une entrée d’action complexe, un autre nœud peut être ajouté (voir figure 2) pour s’assurer que l’agent renvoie une production structurée.

  Diagramme d’architecture de l’agent ReAct

Dans LangGraph, la fonctionnalité « état » sert de banque de mémoire qui enregistre et suit toutes les informations précieuses traitées par chaque itération du système d’IA. Ces graphiques avec état permettent à l’agent de se rappeler d’informations antérieures et d’un contexte précieux. La structure cyclique du graphique ReAct est exploitée lorsque le résultat d’une étape dépend des étapes précédentes de la boucle. Les nœuds ou « acteurs » du graphique encodent la logique de l’agent et sont connectés par des edges. Ces edges sont essentiellement des fonctions Python qui déterminent le prochain nœud à exécuter en fonction de l’état actuel.

## Prérequis

Vous avez besoin [d’un compte IBM Cloud](https://cloud.ibm.com/registration) pour créer un [compte watsonx.ai](https://www.ibm.com/fr-fr/products/watsonx-ai) projet.

## Etapes

Pour utiliser [l’interface de programmation d’applications (API)](https://www.ibm.com/fr-fr/think/topics/api) watsonx, vous devrez suivre les étapes suivantes. Notez que vous pouvez également accéder à ce tutoriel sur GitHub. 

###

## Étape 1. Générer vos identifiants watsonx.ai

1.  Se connecter à [watsonx.ai](https://dataplatform.cloud.ibm.com/registration/stepone) en utilisant votre compte IBM Cloud.

2.  Créez une instance de service d’exécution [watsonx.ai](https://cloud.ibm.com/catalog/services/watsonxai-runtime) (sélectionnez votre région et choisissez le plan Lite, qui est une instance gratuite).

3.

    Générez une [clé d'interface de programmation des applications](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html).

###

## Étape 2. Configurer le projet dans votre IDE

Pour commencer facilement à déployer des agents sur watsonx.ai, clonez ce référentiel GitHub et accédez au projet d'agent ReAct d'assistance informatique. Pour ce faire, vous pouvez exécuter la commande suivante dans votre terminal.

```bash
git clone git@github.com:IBM/ibmdotcom-tutorials.git
cd react-agent-langgraph-it-support/base/langgraph-react-agent/
```

Ensuite, installez Poetry si ce n’est pas déjà fait. Poetry est un outil permettant de gérer les dépendances et l’empaquetage Python.

```
pipx install --python 3.11 poetry
```

Puis, activez votre environnement virtuel.

```
source $(poetry -q env use 3.11 && poetry env info --path)/bin/activate
```

Au lieu d’utiliser la commande `pip install` , le paquet Poetry nous permet d’ajouter des dépendances en exécutant la commande suivante dans le terminal. Cette étape installe les dépendances du référentiel reflétées dans le fichier `pyproject.toml` dans votre environnement virtuel distinct.

```
poetry install
```

L’ajout d’un répertoire de travail à PYTHONPATH est nécessaire pour les étapes suivantes. Dans votre terminal, exécutez :  

```bash
export PYTHONPATH=$(pwd):${PYTHONPATH}
```

Pour configurer votre environnement, suivez les instructions du fichier README.md sur Github. Cette configuration nécessite l’exécution de plusieurs commandes sur votre IDE ou votre ligne de commande.

### Étape 3. Définissez les variables d’environnement

Dans le fichier`config.toml` , vous trouverez les identifiants vierges suivants, que vous devez remplir avant de tenter de déployer votre agent. Vos`watsonx_apikey` et`watsonx_url` ont été initialisées à l’étape 1 de ce tutoriel. Ensuite, suivez le formulaire simple qui se trouve sur la page [Accès développeur](https://dataplatform.cloud.ibm.com/developer-access) pour sélectionner votre espace de déploiement ou en créer un nouveau. Vous pourrez y récupérer votre`space_id` nécessaire pour connecter notre agent au déploiement de watsonx.ai. Enfin, votre`model_id` est défini sur le modèle IBM Granite 3.2.

```
[deployment]
watsonx_apikey = ""
watsonx_url = ""  # should follow the format: `https://{REGION}.ml.cloud.ibm.com`
space_id = "" # found in the "Manage" tab of your Deployment or in the Developer Access page here: https://dataplatform.cloud.ibm.com/developer-access

[deployment.custom]
# during creation of deployment additional parameters can be provided inside `CUSTOM` object for further referencing
# please refer to the API docs: https://cloud.ibm.com/apidocs/machine-learning-cp#deployments-create
model_id = "ibm/granite-3-2-8b-instruct"
thread_id = "thread-1" # More info here: https://langchain-ai.github.io/langgraph/how-tos/persistence/
```

### Étape 4. Importez vos données dans IBM Cloud Object Storage

Notre agent a besoin d’une source de données pour fournir des informations actualisées et ajouter de nouvelles données. Nous stockerons notre fichier de données dans IBM Cloud Object Storage.

1.  Tout d’abord, connectez-vous à [IBM Cloud](https://cloud.ibm.com/objectstorage/overview). Ensuite, créez un [nouveau projet](https://cloud.ibm.com/projects).
2.  Dans le menu de gauche, sélectionnez [Liste des ressources](https://cloud.ibm.com/resources). À l’aide du bouton Créer une ressource, créez une nouvelle instance de Cloud Object Storage ou utilisez simplement [ce lien](https://cloud.ibm.com/objectstorage/create?catalog_query=aHR0cHM6Ly9jbG91ZC5pYm0uY29tL2NhdGFsb2c%2FY2F0ZWdvcnk9c3RvcmFnZSNhbGxfcHJvZHVjdHM%3D).
3.  Ouvrez votre nouvelle instance de stockage IBM Cloud et créez un nouveau compartiment. Pour ce tutoriel, vous pouvez sélectionner Smart Tier, qui est la version gratuite. Lorsque vous y serez invité, importez votre fichier. Pour le fichier d’exemple, reportez-vous au fichier tickets.csv du référentiel GitHub fourni en lien à l’étape 2.

### Étape 5. Établissez la connexion de vos données

Pour fournir une fonctionnalité de gestion de tickets informatiques à l’agent ReAct, nous devons nous connecter à notre source de données dans IBM Cloud Object Storage. Pour cette étape, nous pouvons utiliser la bibliothèque `ibm_boto3` [](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-python).\
\
Dans `tools.py` , les `COS_ENDPOINT` , `COS_INSTANCE_CRN` , `BUCKET_NAME` et `CSV_FILE_NAME` doivent être remplis avec les informations appropriées en utilisant les détails du compartiment qui se trouvent dans votre instance Cloud Object Storage sous l’onglet Configuration. 

```
  COS_ENDPOINT = ""       #find in your COS bucket configuration
COS_INSTANCE_CRN = ""   #find in your COS bucket configuration
BUCKET_NAME = ""        #find in your COS bucket configuration
CSV_FILE_NAME = "filename.csv" #you can use the provided tickets.csv sample file 

cos = ibm_boto3.client(
"s3",
ibm_api_key_id=dep_config["watsonx_apikey"],
ibm_service_instance_id=COS_INSTANCE_CRN,
config=Config(signature_version="oauth"),
endpoint_url=COS_ENDPOINT,
)
```

### Étape 6. Créez vos outils personnalisés

Notre agent pourra à la fois lire et écrire des données dans notre fichier. Commençons par créer l’outil de lecture de données à l’aide du décorateur`@tool` LangChain. \
\
Nous avons ajouté cet outil`find_tickets` au fichier`tools.py` . Cet outil récupère l’objet de données du Cloud Object Storage et le renvoie sous forme de dataframe Pandas. Sinon, une exception est déclenchée. 

```python
  @tool 
def find_tickets():
"""Returns a list of of all tickets."""
try:
response = cos.get_object(Bucket=BUCKET_NAME, Key=CSV_FILE_NAME)
csv_data = pd.read_csv(response['Body']) 
print("Ticket file loaded successfully:")
return csv_data
except Exception as e:
print(f"Error loading file from COS: {e}")
return None
```

 

Ensuite, nous avons ajouté l’outil `create_ticket` . 

```python
  @tool 
def create_ticket(issue: str, urgency:str):
"""Creates a tickets for a customer issue. Request a detailed explanation of the customer issue and urgency level before creating a ticket.

Args:
issue (str): A description of the issue.
urgency (str): A category value for the level of urgency. Can be "low", "medium", or "high".

Returns:
The new ticket.
"""
try:
# retrieve the existing item to reload the contents
response = cos.get_object(Bucket=BUCKET_NAME, Key=CSV_FILE_NAME)
existing_body_df = pd.read_csv(response['Body'])
new_ticket = {"issue": issue, "date_added":datetime.now().strftime("%m-%d-%Y"), "urgency":urgency, "status":"open"}
# Add a new row (i.e. ticket) using loc[]
existing_body_df.loc[len(existing_body_df)] = new_ticket

cos.put_object(Bucket=BUCKET_NAME, Key=CSV_FILE_NAME, Body=existing_body_df.to_json())
return "New ticket successfully created!"
except Exception as e:
print("Unable to create new ticket. Please try again.")
```

Cet outil tient utilise la description du problème par l’utilisateur et l’urgence du problème comme arguments. Une nouvelle ligne est ajoutée à notre fichier dans COS avec ces informations et un nouveau ticket est ainsi créé. Sinon, une exception est déclenchée. \
\
Le dernier outil que nous devons ajouter à notre fichier `tools.py` est `get_todays_date` , qui utilise le module `datetime` pour renvoyer la date du jour au format MM-JJ-AAAA. Cet outil sera utile pour accéder à la date du jour, que l’agent n’a aucun autre moyen de récupérer puisque le LLM n’a pas été entraîné sur ces données. 

```python
  @tool
def get_todays_date():
"""Returns today's date in MM-DD-YYYY format."""
date = datetime.now().strftime("%m-%d-%Y")
return date 
```

Pour permettre à nos agents d’accéder à ces outils, nous les avons ajoutés à la liste `TOOLS` dans le fichier du module `extensions` nommé `init.py` . Cette liste doit constituer le sommaire de votre fichier `init.py` dans le répertoire `src/langgraph_react_agent` .

```python
  from .tools import (
find_tickets,
get_todays_date,
create_ticket
)

TOOLS = [
find_tickets,
get_todays_date,
create_ticket
]
```

\
Ces outils sont importés dans le fichier `agent.py` et transmis à la fonction LangGraph prédéfinie `create_react_agent`  servant d’exécuteur d’agent. Parmi les autres paramètres figurent le grand modèle de langage initialisé en utilisant la classe `ChatWatsonx` , qui permet de faire un appel d’outil sur watsonx.ai, l’économiseur de mémoire et l’invite du système. Notez que certains prompts se comporteront mieux que d’autres et qu’un certain niveau de prompt engineering peut donc être nécessaire selon le LLM choisi. \
\
Avant de déployer votre agent, pensez à ajouter toutes les informations nécessaires dans le fichier `config.toml` . 

### Étape 7. Discutez avec votre agent

Il existe trois façons de discuter avec votre agent.

#### Option 1. Interroger l’agent localement

\
Exécutez le script d’exécution du service d’IA local.

```
  poetry run python examples/execute_ai_service_locally.py
```

#### \
Option 2. Déployer l’agent sur l’interface de chat intégrée dans watsonx.ai

\
La dernière option consiste à accéder à l’agent dans l’espace Déploiements de watsonx.ai. Pour ce faire, sélectionnez « Déploiements » dans le menu de gauche. Choisissez ensuite votre espace de déploiement, cliquez sur l’onglet « Actifs », sélectionnez votre actif`online ai_service` , sélectionnez une nouvelle fois l’actif portant l’étiquette « wx-agent » et ouvrez l’onglet « Aperçu ». Vous pouvez maintenant discuter avec l’agent dans l’interface de chat interactive. Chacune de ces trois options doit donner une production similaire.

#### Option 3. Déployer et discuter avec l’agent dans votre IDE

Pour exécuter le script de déploiement, initialisez la variable `deployment_id`  dans le fichier `query_existing_deployment.py` .\
\
Vous pouvez obtenir le `deployment_id` de votre déploiement en exécutant le fichier `scripts/deploy.py` .\
\
Exécutez ensuite le script de déploiement. 

```
  poetry run python scripts/deploy.py
```

Puis, exécutez le script pour interroger le déploiement.

```
  poetry run python examples/query_existing_deployment.py
```

\
Pour les besoins de ce tutoriel, choisissons l’option 2 et interrogeons notre agent déployé sur watsonx.ai sous la forme d’un chatbot agentique. Fournissons à l’agent des prompts qui nécessiteraient l’utilisation d’outils. En suivant les étapes de l’option 3, vous devriez voir une interface de chat sur watsonx.ai. Nous pouvons y saisir notre prompt. \
\
Commençons par vérifier si l’outil`create_ticket` est invoqué. Demandons à l’agent de créer un nouveau ticket.

  Interroger l'agent déployé sur watsonx.ai pour créer un nouveau ticket

Comme vous pouvez le voir dans la réponse finale de l’agent, le système d’IA a bien utilisé la résolution de problèmes pour créer un nouveau ticket avec l’outil `create_ticket` . Il est utile d’avoir une visibilité sur les appels d’outil pour le débogage. Maintenant, vérifions si le ticket a bien été ajouté à notre fichier de données servant de base de connaissances à l’agent. 

  Interroger l'agent déployé sur watsonx.ai pour récupérer des tickets récents

Super ! L’agent a bien ajouté le ticket au fichier.

## Conclusion

Dans ce tutoriel, vous avez créé un agent avec le cadre d’exigences ReAct, qui utilise la prise de décision pour résoudre des tâches complexes telles que la récupération et la création de tickets d’assistance. Il existe plusieurs modèles IA qui permettent un appel d’outil agentique, tels que Gemini de Google, Granite d’IBM et GPT-4 d’OpenAI. Dans notre projet, nous avons utilisé un modèle IA IBM Granite via l’API watsonx.ai. Le modèle s’est comporté comme prévu, localement et lors du déploiement sur watsonx.ai. Pour aller plus loin, consultez les modèles multi-agents LlamaIndex et crewAI disponibles dans le référentiel GitHub watsonx-developer-hub pour créer des agents IA.
