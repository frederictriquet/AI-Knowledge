> Source : https://www.ibm.com/fr-fr/think/tutorials/build-sql-agent-langgraph-mistral-medium-3-watsonx-ai

# Créer un agent SQL avec LangGraph et Mistral Medium 3 dans watsonx.ai

Dans ce tutoriel, vous allez créer un [agent IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) capable d’exécuter et de générer des requêtes Python et [SQL](https://www.ibm.com/fr-fr/think/topics/structured-query-language) pour votre base de données SQLite personnalisée. Votre agent sera construit en partant de zéro avec [LangGraph](https://www.ibm.com/fr-fr/think/topics/langgraph) et le [grand modèle de langage (LLM)](https://www.ibm.com/fr-fr/think/topics/large-language-models) Mistral Medium 3. Ce LLM est optimisé pour des cas d’utilisation professionnelles tels que le codage et la compréhension multimodale, ce qui en fait donc un excellent choix pour cette tâche.1 Nous détecterons et bloquerons également les messages offensants grâce au modèle IBM® Granite Guardian.

## Qu’est-ce que LangGraph ?

Créé par [LangChain](https://www.ibm.com/fr-fr/think/topics/langgraph), [LangGraph](https://www.ibm.com/fr-fr/think/topics/langchain) est un [cadre d’agent IA](https://www.ibm.com/fr-fr/think/topics/open-source) [open source](https://www.ibm.com/fr-fr/think/insights/top-ai-agent-frameworks) conçu pour construire, déployer et gérer des [workflows d’agents d’IA](https://www.ibm.com/fr-fr/think/topics/agentic-workflows) générative complexes. Il fournit un ensemble d’[outils](https://www.ibm.com/fr-fr/think/topics/tool-calling) et de bibliothèques qui permettent aux utilisateurs de créer, d’exécuter et d’optimiser des LLM de manière évolutive et efficace. LangGraph exploite essentiellement la puissance des architectures basées sur des graphes pour modéliser et gérer les relations complexes entre les diverses [composantes](https://www.ibm.com/fr-fr/think/topics/components-of-ai-agents) d’un workflow d’agent IA, notamment celles que l’on trouve dans les systèmes multi-agents.

## Prérequis

1.  Vous devez disposer d’un [compte IBM Cloud](https://cloud.ibm.com/registration) pour créer un projet watsonx.ai.

2.  Plusieurs versions de Python peuvent être utilisées pour ce tutoriel. Nous vous recommandons de [télécharger](https://www.python.org/downloads/) Python 3.13, la version la plus récente au moment où le présent document a été publié.

## Étapes

### Étape 1. Configurer l’environnement

Bien que vous puissiez choisir parmi plusieurs outils, ce tutoriel vous guide pas à pas pour configurer un compte IBM afin d’utiliser un Jupyter Notebook.

1.  Connectez-vous à [watsonx.ai](https://dataplatform.cloud.ibm.com/registration/stepone?context=wx&apps=all) en utilisant votre compte IBM Cloud.

2.  Créez un [projet watsonx.ai](https://www.ibm.com/docs/en/watsonx/saas?topic=projects-creating-project).

    Vous pouvez obtenir l’ID de votre projet à partir de celui-ci. Cliquez sur l’onglet **Manage** (Gérer). Ensuite, copiez l’ID du projet depuis la section **Details** (Détails) de la page **General** (Général). Vous aurez besoin de cet ID pour ce tutoriel.

3.  Créez un [Jupyter Notebook](https://www.ibm.com/docs/en/watsonx/saas?topic=editor-creating-managing-notebooks).

    Cette étape ouvre un environnement Jupyter Notebook dans lequel vous pouvez copier le code de ce tutoriel. Vous pouvez également télécharger ce notebook sur votre système local et le charger dans votre projet watsonx.ai en tant qu’actif. Ce tutoriel est également disponible sur [GitHub.](https://github.com/IBM/ibmdotcom-tutorials)

### Étape 2. Configurer une instance d’exécution watsonx.ai et une clé API

1.  Créez une instance de service [watsonx.ai Runtime](https://cloud.ibm.com/catalog/services/watsonxai-runtime) (sélectionnez votre région appropriée et choisissez le plan Lite, qui est une instance gratuite).

2.  Générez une [clé API](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html) (interface de programmation d’application).

3.  Associez l’instance de service watsonx.ai Runtime au projet que vous avez créé dans [watsonx.ai](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/assoc-services.html).

### Étape 3. Installer et importer les bibliothèques correspondantes et configurer vos identifiants

Nous avons besoin de quelques bibliothèques et modules pour ce tutoriel. Veillez à importer les éléments suivants ; s’ils ne sont pas installés, une installation rapide avec pip résoudra le problème.

```
#installations
%pip install -qU ibm-watsonx-ai \
    langchain-ibm \
    langgraph \
    langchain_experimental \
    tavily-python \
    langchain-community
```

Redémarrez votre terminal et importez les paquets suivants.

```python
# imports
import sqlite3
import getpass

from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.foundation_models.moderations import Guardian
from IPython.display import Image, display
from langchain import hub
from langchain_ibm import ChatWatsonx
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage, ToolMessage, AIMessage
from langchain_core.tools import tool
from langchain_experimental.tools.python.tool import PythonREPLTool
from sqlalchemy import create_engine
from typing_extensions import TypedDict
from typing import Annotated
```

Pour définir nos identifiants, nous aurons besoin des `WATSONX_APIKEY` et `WATSONX_PROJECT_ID` que vous avez générés à l’étape 1. Nous allons également définir l’`URL` qui servira de point de terminaison de l’API.

```
WATSONX_APIKEY = getpass.getpass("Please enter your watsonx.ai Runtime API key (hit enter): ")
WATSONX_PROJECT_ID = getpass.getpass("Please enter your project ID (hit enter): ")
URL = "https://us-south.ml.cloud.ibm.com"
```

Avant d’initialiser notre LLM, nous pouvons utiliser la classe `Credentials` pour encapsuler les identifiants d’API transmis.

```
credentials = Credentials(url=URL, api_key=WATSONX_APIKEY)
```

### Étape 4. Instancier le modèle de chat

Pour pouvoir interagir avec toutes les ressources disponibles dans watsonx.ai Runtime, vous devez configurer votre `APIClient`. Ici, nous transmettons nos identifiants et `WATSONX_PROJECT_ID`.

```
client = APIClient(credentials=credentials, project_id=WATSONX_PROJECT_ID)
```

Pour ce tutoriel, nous utiliserons le wrapper ChatWatsonx pour configurer notre modèle de chat. Ce wrapper simplifie l’intégration de l’appel et du chaînage d’outils. Nous vous invitons à utiliser les références API dans la [documentation officielle](https://python.langchain.com/docs/integrations/chat/ibm_watsonx/#tool-calling) de ChatWatsonx pour plus d’informations. Nous transmettons notre `model_id` pour Mistral Medium 3 et notre client comme paramètres.

Notez que si vous utilisez un autre fournisseur d’API, vous devrez modifier le wrapper en conséquence. Par exemple, pour utiliser l’API OpenAI afin d’accéder à des modèles comme GPT-4, `openai_api_key` et le wrapper `ChatOpenAI` seront requis.

```
model_id = "mistralai/mistral-medium-2505"
llm = ChatWatsonx(model_id=model_id, watsonx_client=client)
```

### Étape 5. Configurer la base de données SQLite

Dans ce tutoriel, votre agent utilisera les outils dont il dispose pour interagir avec une base de données SQLite. Si vous avez déjà un jeu de données stocké dans un système de gestion de base de données relationnelle comme PostgreSQL ou SQLite, vous pouvez ignorer cette étape. Sinon, exécutez la cellule suivante pour définir la variable `sql_script` sur un script qui génère une base de données contenant des données synthétiques de vente automobile. Cette base de données contiendra plusieurs tables pour stocker les données respectives (concessionnaires, ventes et véhicules).

```
sql_script = """
DROP TABLE IF EXISTS [Dealerships];

DROP TABLE IF EXISTS [Cars];

DROP TABLE IF EXISTS [Sales];

CREATE TABLE [Dealerships] (
    [id] INTEGER PRIMARY KEY,
    [name] TEXT NOT NULL,
    [location] TEXT NOT NULL
);

CREATE TABLE [Cars] (
    [id] INTEGER PRIMARY KEY,
    [make] TEXT NOT NULL,
    [model] TEXT NOT NULL,
    [year] INTEGER NOT NULL,
    [color] TEXT NOT NULL
);

CREATE TABLE [Sales] (
    [id] INTEGER PRIMARY KEY,
    [car_id] INTEGER NOT NULL,
    [dealership_id] INTEGER NOT NULL,
    [sale_date] DATE NOT NULL,
    [sale_price] REAL NOT NULL,
    FOREIGN KEY ([car_id]) REFERENCES [Cars] ([id]),
    FOREIGN KEY ([dealership_id]) REFERENCES [Dealerships] ([id])
);

INSERT INTO [Dealerships] ([id], [name], [location]) VALUES
    (1, 'Dealership A', 'New York'),
    (2, 'Dealership B', 'Los Angeles'),
    (3, 'Dealership C', 'Chicago'),
    (4, 'Dealership D', 'Houston'),
    (5, 'Dealership E', 'Phoenix'),
    (6, 'Dealership F', 'Philadelphia'),
    (7, 'Dealership G', 'San Antonio'),
    (8, 'Dealership H', 'San Diego'),
    (9, 'Dealership I', 'Dallas'),
    (10, 'Dealership J', 'San Jose');

INSERT INTO [Cars] ([id], [make], [model], [year], [color]) VALUES
    (1, 'Toyota', 'Camry', 2020, 'Blue'),
    (2, 'Honda', 'Civic', 2019, 'Red'),
    (3, 'Ford', 'Mustang', 2021, 'Black'),
    (4, 'Chevrolet', 'Silverado', 2018, 'White'),
    (5, 'Nissan', 'Altima', 2020, 'Gray'),
    (6, 'Kia', 'Optima', 2020, 'Silver'),
    (7, 'Hyundai', 'Elantra', 2019, 'Black'),
    (8, 'Volkswagen', 'Golf', 2021, 'Red'),
    (9, 'BMW', '3 Series', 2018, 'White'),
    (10, 'Mercedes-Benz', 'C-Class', 2020, 'Gray'),
    (11, 'Audi', 'A4', 2019, 'Blue'),
    (12, 'Lexus', 'ES', 2021, 'Black'),
    (13, 'Toyota', 'Corolla', 2018, 'White'),
    (14, 'Honda', 'Accord', 2020, 'Gray'),
    (15, 'Ford', 'Fusion', 2019, 'Red');

INSERT INTO [Sales] ([id], [car_id], [dealership_id], [sale_date], [sale_price]) VALUES
    (1, 1, 1, '2022-01-01', 25000.0),
    (2, 2, 2, '2022-02-01', 20000.0),
    (3, 3, 3, '2022-03-01', 30000.0),
    (4, 4, 1, '2022-04-01', 40000.0),
    (5, 5, 2, '2022-05-01', 28000.0),
    (6, 6, 4, '2022-06-01', 22000.0),
    (7, 7, 5, '2022-07-01', 20000.0),
    (8, 8, 6, '2022-08-01', 28000.0),
    (9, 9, 7, '2022-09-01', 35000.0),
    (10, 10, 8, '2022-10-01', 32000.0),
    (11, 11, 9, '2022-11-01', 30000.0),
    (12, 12, 10, '2022-12-01', 38000.0),
    (13, 13, 1, '2023-01-01', 25000.0),
    (14, 14, 2, '2023-02-01', 28000.0),
    (15, 15, 3, '2023-03-01', 22000.0);

"""
```

Pour exécuter ce script et créer la base de données SQLite locale, nous devons configurer un objet de base de données `Connection`. En transmettant le nom de chemin « :memory: », nous pouvons nous connecter à une base de données en mémoire transitoire.

```
connection = sqlite3.connect(":memory:")
```

Ensuite, nous pouvons utiliser la méthode `executescript` pour créer un curseur de base de données et exécuter notre script SQL. Cet objet `Cursor` nous permet d’exécuter ce type de script.

```
connection.executescript(sql_script)
```

**Sortie :**

```
<sqlite3.Cursor at 0x30c511240>
```

Enfin, exécutez la commande suivante pour créer une instance `SQLAlechemy` Engine avec une connexion au fichier de base de données dans votre répertoire de travail. Le fichier doit porter le même nom que votre Jupyter Notebook, avec une extension de base de données. Nous pouvons garder l’URL vide afin que la connexion soit faite à la base de données locale SQLite. Nous fournissons notre objet `Connection` dans le paramètre `creator`. Ce paramètre est chargé de créer la connexion à la base de données.

```
engine = create_engine(
    "sqlite://",
    creator=lambda: connection
)
```

Si vous préférez utiliser pour ce tutoriel une autre base de données, qui n’est pas stockée localement, il suffit de remplacer le chemin vide par « [sqlite:///Chinook.db](sqlite:///Chinook.db)» pour accéder à un exemple de base de données de magasin multimédia numérique.

### Étape 6. Configurer les outils

Dans ce tutoriel, nous utilisons la boîte à outils préconfigurée `SQLDatabaseToolkit` de LangChain. Cette boîte à outils requiert un objet `SQLDatabase`, qui utilise `SQLAlchemy` Engine comme paramètre, et le LLM de votre choix. Une fois la boîte instanciée, nous pouvons récupérer les outils qu’elle contient. Imprimons les outils pour en savoir plus.

```
db = SQLDatabase(engine)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
tools = toolkit.get_tools()
tools
```

**Sortie :**

```
[ QuerySQLDatabaseTool( description="This tool takes as input a detailed and correct SQL query; it returns a result from the database. If the query is incorrect, an error message is displayed. In case of an error, rewrite the query, check it, and try again. If you encounter an error about an unknown column 'xxxx' in the field list, use 'sql_db_schema' to inspect the fields of the appropriate table.", db=<langchain_community.utilities.sql_database.SQLDatabase object at 0x30c3ecd10> ), InfoSQLDatabaseTool( description="This tool takes as input a comma‑separated list of tables and returns the schema and sample rows for those tables. Make sure the tables actually exist by first calling the 'sql_db_list_tables' function! Example input: table1, table2, table3", db=<langchain_community.utilities.sql_database.SQLDatabase object at 0x30c3ecd10> ), ListSQLDatabaseTool( db=<langchain_community.utilities.sql_database.SQLDatabase object at 0x30c3ecd10> ), QuerySQLCheckerTool( description="Use this tool to verify that your query is correct before executing it. Always use it before running a query with sql_db_query!", db=<langchain_community.utilities.sql_database.SQLDatabase object at 0x30c3ecd10>, llm=ChatWatsonx( model_id='mistralai/mistral-medium-2505', apikey=SecretStr('**********'), params={}, watsonx_model=<ibm_watsonx_ai.foundation_models.inference.model_inference.ModelInference object at 0x309c34690>, watsonx_client=<ibm_watsonx_ai.client.APIClient object at 0x30c3e3250> ), llm_chain=LLMChain( verbose=False, prompt=PromptTemplate( input_variables=['dialect', 'query'], template=
```

Comme nous pouvons le constater, il y a 4 outils disponibles dans la boîte à outils. Chaque outil a sa propre utilité, comme le montre sa description. Les outils sont conçus pour lister les bases de données, exécuter les requêtes, renvoyer les schémas de table et vérifier les requêtes SQL avant de les exécuter.

Pour permettre à notre agent de générer et d’exécuter le code Python, nous pouvons utiliser la classe `PythonREPLTool` de LangChain. Ce code configure un outil Python REPL (Read-Eval-Print Loop), définissant ses fonctionnalités et l’ajoutant à une liste d’outils pour une utilisation ultérieure.

```
python_repl = PythonREPLTool()
tools.append(python_repl)
```

Pour nous assurer que notre agent dispose d’un prompt système adapté aux outils et bases de données SQL, nous pouvons extraire un prompt fourni par le [LangChain Hub](https://smith.langchain.com/hub). Imprimons le `system_message` pour voir le prompt en détail.

```python
chatprompttemplate = hub.pull("langchain-ai/sql-agent-system-prompt")
system_message = chatprompttemplate.format(dialect="SQLite", top_k=5)
print(system_message)
```

**Sortie :**

```
System: You are an agent designed to interact with a SQL database.
Given the user’s input question, create a syntactically correct SQLite query to execute, then inspect the query results and return the answer.
Unless the user specifies how many examples they want, always limit the query to a maximum of 5 results.
You may sort results in a column based on relevance to return the most meaningful examples from the database.
Never query all columns of a given table; request only the columns that are relevant to the question.

You have access to tools to interact with the database.
Use only the tools listed below. Use only the information returned by these tools to craft your final answer.

You MUST check your query before executing it. If you receive an error message when executing a query, rewrite the query and try again.

Do NOT perform any DML instructions (INSERT, UPDATE, DELETE, DROP, etc.) on the database.

To begin, you must ALWAYS inspect the tables in the database to know what you can query.
Do NOT skip this step.
You must then inspect the schema of the most relevant tables.
```

### Étape 7. Définir l’état de l’agent

Il existe une fonction `create_react_agent` prédéfinie dans LangGraph pour générer un graphe d’agent qui suit l’[architecture ReAct (raisonnement et action)](https://www.ibm.com/fr-fr/think/topics/react-agent). Cette architecture permet à l’agent d’[appeler les outils](https://www.ibm.com/fr-fr/think/topics/tool-calling) de manière itérative dans une boucle jusqu’à ce qu’une condition d’arrêt soit remplie.

  Flux d’agent React

Pour une approche plus pratique, nous allons créer un agent ReAct en partant de zéro dans ce tutoriel. Dans un premier temps, nous allons créer une classe `AgentState` pour stocker le contexte des messages de l’utilisateur, des outils et de l’agent. La classe `TypedDict` de Python est utilisée ici pour s’assurer que les messages ont le format de dictionnaire approprié. Nous pouvons également utiliser la fonction de réduction `add_messages` de LangGraph pour ajouter les nouveaux messages à la liste existante.

```python
class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
```

### Étape 8. Définir la classe ReActAgent

Ensuite, nous allons créer la classe `ReActAgent`. Cette classe fournit une structure de base pour créer des agents capables de réagir aux changements de leur environnement. Les fonctions de la classe `ReActAgent` permettent d’appeler des outils de manière itérative selon l’état du graphe.

La fonction `__init__` initialise les attributs de la classe avec le grand modèle de langage, les outils et le message système en tant que paramètres. Ce constructeur crée un graphe d’état avec des nœuds pour le modèle Guardian, le LLM et les outils. Le graphe commence au nœud `gardien`, qui appelle la méthode `guardian_moderation` pour détecter tout contenu offensant avant qu’il n’atteigne le LLM et la base de données. L’arête conditionnelle entre les nœuds `guardian` et `llm` achemine l’état du graphe soit vers le nœud `llm`, soit vers la fin. Ceci est déterminé par la sortie de la fonction `guardian_moderation`. Les messages non problématiques sont transmis au nœud `llm`, qui exécute la méthode `call_llm`. Nous ajoutons également une arête conditionnelle entre les nœuds `llm` et `outils` pour acheminer correctement les messages. Si le LLM renvoie un appel d’outil, la méthode `should_call_tools` renvoie une valeur booléenne `True`. Dans le cas contraire, `False` est renvoyé, et le graphe est acheminé jusqu’à la fin. Cette étape fait partie de l’architecture de l’agent ReAct ; nous voulons que l’agent reçoive la sortie de l’outil et qu’il réagisse au changement d’état pour déterminer sa prochaine action.

Ensuite, nous pouvons compiler le graphe, ce qui nous permet d’invoquer l’agent à une étape ultérieure. Pour conserver les messages, nous pouvons utiliser le pointeur de contrôle `MemorySaver`. Les deux dernières lignes de cette méthode initialisent les attributs `outils` et `llm` de l’instance de classe. L’attribut outils est un dictionnaire qui associe les noms d’outils aux objets outils. L’attribut llm est le LLM, qui est lié aux outils à l’aide de la méthode `bind_tools`.

```python
class ReActAgent:

    def __init__(self, llm, tools, system_message=""):
        memory = MemorySaver()
        graph = StateGraph(AgentState)
        graph.add_node("guardian", self.guardian_moderation)
        graph.add_node("llm", self.call_llm)
        graph.add_node("tools", self.call_tools)
        graph.add_node("block_message", self.block_message)
        graph.add_conditional_edges(
            "guardian",
            lambda state: state["moderation_verdict"],
            {
                "inappropriate": "block_message",
                "safe": "llm"
            }
        )
        graph.add_edge("block_message", END)
        graph.add_conditional_edges(
            "llm",
            self.should_call_tools,
            ["tools", END]
        )
        graph.add_edge("tools", "llm")
        graph.add_edge(START, "guardian")
        self.system_message = system_message
        self.graph = graph.compile(checkpointer=memory)
        self.tools = {t.name: t for t in tools}
        self.llm = llm.bind_tools(tools)
```

La prochaine fonction de la classe `ReActAgent` est `call_llm`. Cette fonction appelle le LLM en récupérant les messages à partir de l’état. Si un message système est présent, la méthode l’ajoute au début de la liste de messages. Le LLM est alors invoqué avec les messages, et un nouvel état avec une réponse LLM est renvoyé.

```python
def call_llm (self, state : AgentState) :
 messages = état [« messages »]
 si self.system_message :
 messages = [SystemMessage (content=self.system_message)] + messages
 message = self.llm.invoke(messages)
    return {'messages': [message]}
```

`call_tools` est la prochaine fonction de la classe `ReActAgent`. Cette méthode récupère les appels d’outils du dernier message de l’état, itère dessus et invoque chaque outil avec les arguments donnés. Ensuite, les résultats de chaque appel d’outil sont stockés dans une liste appelée `résultats`. Enfin, ce nouvel état est renvoyé sous la forme d’un dictionnaire dans lequel la clé des messages correspond à la liste des résultats.

```python
def call_tools(self, state: AgentState):
    tool_calls = state['messages'][-1].tool_calls
    results = []
    for t in tool_calls:
        result = self.tools[t['name']].invoke(t['args'])
        results.append(ToolMessage(tool_call_id=t['id'],
                                    name=t['name'],
                                    content=str(result)))
    return {'messages': results}
```

La prochaine fonction de la classe `ReActAgent` est `should_call_tools`. Cette fonction détermine s’il faut appeler les outils en fonction de l’état en récupérant la réponse précédente du LLM à partir de l’état et en vérifiant si elle contient des appels d’outils.

```python
def should_call_tools(self, state: AgentState):
    result = state['messages'][-1]
    return "tools" if len(result.tool_calls) > 0 else END
```

La fonction `guardian_moderation` exécutée dans le nœud `guardrain` est conçue pour modérer les messages à l’aide d’un système gardien, dans le but de détecter et de bloquer tout contenu indésirable ou sensible. Tout d’abord, le dernier message est récupéré. Ensuite, un dictionnaire nommé `detectors` est défini ; il contient la configuration des détecteurs et leurs valeurs de seuil. Ces détecteurs identifient certains types de contenu dans les messages tels que les données personnelles (PII), ainsi que les discours haineux, les propos injurieux et diffamatoires (HAP). Ensuite, une instance de la classe Guardian est créée, avec un objet `api_client` nommé `client` et le dictionnaire `detectors`. La méthode `detect` de l’instance Guardian est appelée, transmettant le contenu du dernier message et le dictionnaire `detectors`. Le méthode renvoie ensuite un dictionnaire dans lequel la clé `moderation_verdict` stocke une valeur, soit « sûr », soit « inapproprié », selon la sortie du modèle Granite Guardian.

```python
def guardian_moderation(self, state: AgentState):
    message = state['messages'][-1]
    detectors = {
        "granite_guardian": {"threshold": 0.4},
        "hap": {"threshold": 0.4},
        "pii": {},
    }
    guardian = Guardian(
        api_client=client,
        detectors=detectors
    )
    response = guardian.detect(
        text=message.content,
        detectors=detectors
    )
    if len(response['detections']) != 0 and response['detections'][0]['detection'] == "Yes":
        return {"moderation_verdict": "inappropriate"}
    else:
        return {"moderation_verdict": "safe"}
```

La fonction `block_message` sert de mécanisme de notification, informant l’utilisateur que son entrée (requête) comporte un contenu inapproprié et qu’elle a été bloquée.

```python
def block_message(self, state: AgentState):
    return {"messages": [AIMessage(content="This message has been blocked due to inappropriate content.")]}
```

Nous pouvons maintenant assembler tout ce code et exécuter la cellule suivante.

```python
class ReActAgent:

    def __init__(self, llm, tools, system_message=""):
        memory = MemorySaver()
        graph = StateGraph(AgentState)
        graph.add_node("guardian", self.guardian_moderation)
        graph.add_node("llm", self.call_llm)
        graph.add_node("tools", self.call_tools)
        graph.add_node("block_message", self.block_message)
        graph.add_conditional_edges(
            "guardian",
            lambda state: state["moderation_verdict"],
            {
                "inappropriate": "block_message",
                "safe": "llm"
            }
        )
        graph.add_edge("block_message", END)
        graph.add_conditional_edges(
            "llm",
            self.should_call_tools,
            ["tools", END]
        )
        graph.add_edge("tools", "llm")
        graph.add_edge(START, "guardian")
        self.system_message = system_message
        self.graph = graph.compile(checkpointer=memory)
        self.tools = {t.name: t for t in tools}
        self.llm = llm.bind_tools(tools)

    def call_llm(self, state: AgentState):
        messages = state['messages']
        if self.system_message:
            messages = [SystemMessage(content=self.system_message)] + messages
        message = self.llm.invoke(messages)
        return {'messages': [message]}

    def call_tools(self, state: AgentState):
        tool_calls = state['messages'][-1].tool_calls
        results = []
        for t in tool_calls:
            result = self.tools[t['name']].invoke(t['args'])
            results.append(ToolMessage(tool_call_id=t['id'],
                                       name=t['name'],
                                       content=str(result)))
        return {'messages': results}

    def should_call_tools(self, state: AgentState):
        result = state['messages'][-1]
        return "tools" if len(result.tool_calls) > 0 else END

    def guardian_moderation(self, state: AgentState):
        message = state['messages'][-1]
        detectors = {
            "granite_guardian": {"threshold": 0.4},
            "hap": {"threshold": 0.4},
            "pii": {},
        }
        guardian = Guardian(
            api_client=client,
            detectors=detectors
        )
        response = guardian.detect(
            text=message.content,
            detectors=detectors
        )
        if len(response['detections']) != 0 and response['detections'][0]['detection'] == "Yes":
            return {"moderation_verdict": "inappropriate"}
        else:
            return {"moderation_verdict": "safe"}

    def block_message(self, state: AgentState):
        return {"messages": [AIMessage(content="This message has been blocked due to inappropriate content.")]}
```

### Étape 9. Créer et invoquer l’objet ReActAgent

La première ligne du bloc de code suivant crée une instance de la classe `ReActAgent`, passant comme paramètres le LLM, les outils SQL et le message système. Ensuite, nous spécifions un thread pour stocker les états du graphe en mémoire. Considérez chaque `thread_id` comme représentant une nouvelle fenêtre de discussion. Nous pouvons également définir l’entrée utilisateur dans la chaîne de notre choix. Ensuite, nous passons une liste composée de l’entrée utilisateur de type `HumanMessage` pour invoquer l’agent.

Tout d’abord, essayons un prompt qui devrait être bloqué par le modèle Granite Guardian.

```json
agent = ReActAgent(llm, tools, system_message=system_message)

config = {"configurable": {"thread_id": "1"}}

user_input = "What is the address of the customer who bought the most expensive car last month?"

result = agent.graph.invoke({'messages': [HumanMessage(content=user_input)]}, config)

for message in result["messages"]:
    message.pretty_print()
```

**Sortie :**

```
    ================================ [1m Human Message  [0m=================================

What is the address of the customer who bought the most expensive car last month?
    ================================== [1m Ai Message  [0m==================================

    This message has been blocked due to inappropriate content.
```

Le modèle Granite Guardian a su empêcher l’utilisateur de demander des informations sensibles sur le client. Nous constatons que le graphe n’a pas atteint le nœud LLM avant de mettre fin à la conversation. Ensuite, posons une question appropriée dans un autre thread. Par exemple, l’entrée utilisateur suivante : « Quel est le chiffre d’affaires total des 5 concessionnaires les plus performants en 2022 ? ».

```json
user_input = "What is the total sales revenue of the 5 best‑performing dealerships in 2022?"

config2 = {"configurable": {"thread_id": "2"}}

result = agent.graph.invoke({'messages': [HumanMessage(content=user_input)]}, config2)

for message in result["messages"]:
    message.pretty_print()
```

**Sortie :**

```
    ================================ [1m Human Message  [0m=================================

What is the total sales revenue of the 5 best‑performing dealerships in 2022?
    ================================== [1m Ai Message  [0m==================================
    Tool Calls:
      sql_db_list_tables (H2irrlsPM)
     Call ID: H2irrlsPM
      Args:
        tool_input:
    ================================= [1m Tool Message  [0m=================================
    Name: sql_db_list_tables

    Cars, Dealerships, Sales
    ================================== [1m Ai Message  [0m==================================
    Tool Calls:
      sql_db_schema (ILZWiZvGX)
     Call ID: ILZWiZvGX
      Args:
        table_names: Cars, Dealerships, Sales
    ================================= [1m Tool Message  [0m=================================
    Name: sql_db_schema

    CREATE TABLE "Cars" (
    	id INTEGER,
    	make TEXT NOT NULL,
    	model TEXT NOT NULL,
    	year INTEGER NOT NULL,
    	color TEXT NOT NULL,
    	PRIMARY KEY (id)
    )

    /*
    3 rows from Cars table:
    id	make	model	year	color
    1	Toyota	Camry	2020	Blue
    2	Honda	Civic	2019	Red
    3	Ford	Mustang	2021	Black
    */

    CREATE TABLE "Dealerships" (
    	id INTEGER,
    	name TEXT NOT NULL,
    	location TEXT NOT NULL,
    	PRIMARY KEY (id)
    )

    /*
    3 rows from Dealerships table:
    id	name	location
    1	Dealership A	New York
    2	Dealership B	Los Angeles
    3	Dealership C	Chicago
    */

    CREATE TABLE "Sales" (
    	id INTEGER,
    	car_id INTEGER NOT NULL,
    	dealership_id INTEGER NOT NULL,
    	sale_date DATE NOT NULL,
    	sale_price REAL NOT NULL,
    	PRIMARY KEY (id),
    	FOREIGN KEY(dealership_id) REFERENCES "Dealerships" (id),
    	FOREIGN KEY(car_id) REFERENCES "Cars" (id)
    )

    /*
    3 rows from Sales table:
    id	car_id	dealership_id	sale_date	sale_price
    1	1	1	2022-01-01	25000.0
    2	2	2	2022-02-01	20000.0
    3	3	3	2022-03-01	30000.0
    */
    ================================== [1m Ai Message  [0m==================================
    Tool Calls:
      sql_db_query_checker (yIZ0tk4VP)
     Call ID: yIZ0tk4VP
      Args:
        query: SELECT Dealerships.name, SOMM(Sales.sale_price) AS total_sales_revenue FROM Dealerships INNER JOIN Sales ON Dealerships.id = Sales.dealership_id OÙ strftime(’ %Y’, Sales.sale_date) = '2022' GROUP BY Dealerships.id ORDER BY total_sales_revenue DESC LIMIT 5;
    ================================= [1m Tool Message  [0m=================================
    Name: sql_db_query_checker

    SELECT Dealerships.name, SUM(Sales.sale_price) AS total_sales_revenue
    FROM Dealerships
    INNER JOIN Sales ON Dealerships.id = Sales.dealership_id
    WHERE strftime('%Y', Sales.sale_date) = '2022'
    GROUP BY Dealerships.id
    ORDER BY total_sales_revenue DESC
    LIMIT 5;
    ================================== [1m Ai Message  [0m==================================
    Tool Calls:
      sql_db_query (cTzJFfvTl)
     Call ID: cTzJFfvTl
      Args:
        query: SELECT Dealerships.name, SUM(Sales.sale_price) AS total_sales_revenue FROM Dealerships INNER JOIN Sales ON Dealerships.id = Sales.dealership_id WHERE strftime('%Y', Sales.sale_date) = '2022' GROUP BY Dealerships.id ORDER BY total_sales_revenue DESC LIMIT 5;
    ================================= [1m Tool Message  [0m=================================
    Name: sql_db_query

    [('Dealership A', 65000.0), ('Dealership B', 48000.0), ('Dealership J', 38000.0), ('Dealership G', 35000.0), ('Dealership H', 32000.0)]
    ================================== [1m Ai Message  [0m==================================

 The total sales revenue of the 5 best‑performing dealerships in 2022 is:
 1. Dealership A: $65,000
2. Dealership B: $48,000
 3. Dealership J: $38,000
4. Dealership G: $35,000
5. Dealership H: $32,

    ================================ [1m Human Message  [0m=================================

  “What is the total sales revenue of the 5 best‑performing dealerships in 2022?”
    ================================== [1m Ai Message  [0m==================================
    Tool Calls:
      sql_db_list_tables (H2irrlsPM)
     Call ID: H2irrlsPM
      Args:
        tool_input:
    ================================= [1m Tool Message  [0m=================================
    Name: sql_db_list_tables

    Cars, Dealerships, Sales
    ================================== [1m Ai Message  [0m==================================
    Tool Calls:
      sql_db_schema (ILZWiZvGX)
     Call ID: ILZWiZvGX
      Args:
        table_names: Cars, Dealerships, Sales
    ================================= [1m Tool Message  [0m=================================
    Name: sql_db_schema

    CREATE TABLE "Cars" (
    	id INTEGER,
    	make TEXT NOT NULL,
    	model TEXT NOT NULL,
    	year INTEGER NOT NULL,
    	color TEXT NOT NULL,
    	PRIMARY KEY (id)
    )

    /*
    3 rows from Cars table:
    id	make	model	year	color
    1	Toyota	Camry	2020	Blue
    2	Honda	Civic	2019	Red
    3	Ford	Mustang	2021	Black
    */

    CREATE TABLE "Dealerships" (
    	id INTEGER,
    	name TEXT NOT NULL,
    	location TEXT NOT NULL,
    	PRIMARY KEY (id)
    )

    /*
    3 rows from Dealerships table:
    id	name	location
    1	Dealership A	New York
    2	Dealership B	Los Angeles
    3	Dealership C	Chicago
    */

    CREATE TABLE "Sales" (
    	id INTEGER,
    	car_id INTEGER NOT NULL,
    	dealership_id INTEGER NOT NULL,
    	sale_date DATE NOT NULL,
    	sale_price REAL NOT NULL,
    	PRIMARY KEY (id),
    	FOREIGN KEY(dealership_id) REFERENCES "Dealerships" (id),
    	FOREIGN KEY(car_id) REFERENCES "Cars" (id)
    )

    /*
    3 rows from Sales table:
    id	car_id	dealership_id	sale_date	sale_price
    1	1	1	2022-01-01	25000.0
    2	2	2	2022-02-01	20000.0
    3	3	3	2022-03-01	30000.0
    */
    ================================== [1m Ai Message  [0m==================================
    Tool Calls:
      sql_db_query_checker (yIZ0tk4VP)
     Call ID: yIZ0tk4VP
      Args:
        query: SELECT Dealerships.name, SUM(Sales.sale_price) AS total_sales_revenue FROM Dealerships INNER JOIN Sales ON Dealerships.id = Sales.dealership_id WHERE strftime('%Y', Sales.sale_date) = '2022' GROUP BY Dealerships.id ORDER BY total_sales_revenue DESC LIMIT 5;
    ================================= [1m Tool Message  [0m=================================
    Name: sql_db_query_checker

    SELECT Dealerships.name, SUM(Sales.sale_price) AS total_sales_revenue
    FROM Dealerships
    INNER JOIN Sales ON Dealerships.id = Sales.dealership_id
    WHERE strftime('%Y', Sales.sale_date) = '2022'
    GROUP BY Dealerships.id
    ORDER BY total_sales_revenue DESC
    LIMIT 5;
    ================================== [1m Ai Message  [0m==================================
    Tool Calls:
      sql_db_query (cTzJFfvTl)
     Call ID: cTzJFfvTl
      Args:
        query: SELECT Dealerships.name, SUM(Sales.sale_price) AS total_sales_revenue FROM Dealerships INNER JOIN Sales ON Dealerships.id = Sales.dealership_id WHERE strftime('%Y', Sales.sale_date) = '2022' GROUP BY Dealerships.id ORDER BY total_sales_revenue DESC LIMIT 5;
    ================================= [1m Tool Message  [0m=================================
    Name: sql_db_query

    [('Dealership A', 65000.0), ('Dealership B', 48000.0), ('Dealership J', 38000.0), ('Dealership G', 35000.0), ('Dealership H', 32000.0)]
    ================================== [1m Ai Message  [0m==================================

    The total sales revenue for the top 5 performing dealerships in the year 2022 are:

    1. Dealership A: $65,000
    2. Dealership B: $48,000
    3. Dealership J: $38,000
    4. Dealership G: $35,000
    5. Dealership H: $32,000
```

Parfait ! L’agent a exécuté avec succès une série de tâches, notamment l’appel de plusieurs outils pour extraire le schéma de table SQL, la génération de nouvelles requêtes SQL et la vérification de ces dernières avant de les exécuter. L’agent renvoie donc correctement le chiffre d’affaires total des 5 concessionnaires automobiles les plus performants en 2022, selon notre base de données. Nous visualisons le raisonnement multi-étapes de l’agent à mesure qu’il imprime chaque requête SQL générée. Dans la réponse, nous voyons également que le modèle Granite Guardian a déterminé que la requête de l’utilisateur était appropriée.

Posons une question complémentaire. Cette fois, demandons à l’agent de générer et d’exécuter le code Python pour afficher une représentation graphique à barres des résultats. L’agent devra récupérer les messages précédents, puisque nous utilisons le même `thread_id`.

```
user_input = “Write Python code that represents these results as a bar chart. Then execute the code and display the bar chart.”

result = agent.graph.invoke ({'messages': [HumanMessage(content=user_input)]}, config2)

for message in result["messages"]:
    message.pretty_print()
```

**Sortie :**

```
================================ [1m Human Message [0m=================================

“What is the total sales revenue of the 5 best‑performing dealerships in 2022.”
================================== [1m Ai Message  [0m==================================
    Tool Calls:
      sql_db_list_tables (H2irrlsPM)
     Call ID: H2irrlsPM
      Args:
        tool_input:
================================= [1m Tool Message  [0m=================================
    Name: sql_db_list_tables

    Cars, Dealerships, Sales
================================== [1m Ai Message  [0m==================================
    Tool Calls:
      sql_db_schema (ILZWiZvGX)
     Call ID: ILZWiZvGX
      Args:
        table_names: Cars, Dealerships, Sales
================================= [1m Tool Message  [0m=================================
    Name: sql_db_schema

    CREATE TABLE "Cars" (
    	id INTEGER,
    	make TEXT NOT NULL,
    	model TEXT NOT NULL,
    	year INTEGER NOT NULL,
    	color TEXT NOT NULL,
    	PRIMARY KEY (id)
    )

    /*
    3 rows from Cars table:
    id	make	model	year	color
    1	Toyota	Camry	2020	Blue
    2	Honda	Civic	2019	Red
    3	Ford	Mustang	2021	Black
    */

    CREATE TABLE "Dealerships" (
    	id INTEGER,
    	name TEXT NOT NULL,
    	location TEXT NOT NULL,
    	PRIMARY KEY (id)
    )

    /*
    3 rows from Dealerships table:
    id	name	location
    1	Dealership A	New York
    2	Dealership B	Los Angeles
    3	Dealership C	Chicago
    */

    CREATE TABLE "Sales" (
    	id INTEGER,
    	car_id INTEGER NOT NULL,
    	dealership_id INTEGER NOT NULL,
    	sale_date DATE NOT NULL,
    	sale_price REAL NOT NULL,
    	PRIMARY KEY (id),
    	FOREIGN KEY(dealership_id) REFERENCES "Dealerships" (id),
    	FOREIGN KEY(car_id) REFERENCES "Cars" (id)
    )

    /*
    3 rows from Sales table:
    id	car_id	dealership_id	sale_date	sale_price
    1	1	1	2022-01-01	25000.0
    2	2	2	2022-02-01	20000.0
    3	3	3	2022-03-01	30000.0
    */
================================== [1m Ai Message  [0m==================================
    Tool Calls:
      sql_db_query_checker (yIZ0tk4VP)
     Call ID: yIZ0tk4VP
      Args:
        query: SELECT Dealerships.name, SUM(Sales.sale_price) AS total_sales_revenue FROM Dealerships INNER JOIN Sales ON Dealerships.id = Sales.dealership_id WHERE strftime('%Y', Sales.sale_date) = '2022' GROUP BY Dealerships.id ORDER BY total_sales_revenue DESC LIMIT 5;
================================= [1m Tool Message  [0m=================================
    Name: sql_db_query_checker

    SELECT Dealerships.name, SUM(Sales.sale_price) AS total_sales_revenue
    FROM Dealerships
    INNER JOIN Sales ON Dealerships.id = Sales.dealership_id
    WHERE strftime('%Y', Sales.sale_date) = '2022'
    GROUP BY Dealerships.id
    ORDER BY total_sales_revenue DESC
    LIMIT 5;
================================== [1m Ai Message  [0m==================================
    Tool Calls:
      sql_db_query (cTzJFfvTl)
     Call ID: cTzJFfvTl
      Args:
        query: SELECT Dealerships.name, SUM(Sales.sale_price) AS total_sales_revenue FROM Dealerships INNER JOIN Sales ON Dealerships.id = Sales.dealership_id WHERE strftime('%Y', Sales.sale_date) = '2022' GROUP BY Dealerships.id ORDER BY total_sales_revenue DESC LIMIT 5;
================================= [1m Tool Message  [0m=================================
    Name: sql_db_query

    [('Dealership A', 65000.0), ('Dealership B', 48000.0), ('Dealership J', 38000.0), ('Dealership G', 35000.0), ('Dealership H', 32000.0)]
================================== [1m Ai Message  [0m==================================

 The total sales revenue of the 5 best‑performing dealerships in 2022 is as follows:

Dealership A: $65,000

Dealership B: $48,000

Dealership J: $38,000

Dealership G: $35,000

Dealership H: $32,000”
================================ [1m Human Message  [0m=================================

  Write Python code to represent these results in a bar chart. Then execute the code and display the bar chart.
================================== [1m Ai Message  [0m==================================
    Tool Calls:
      Python_REPL (5X1fPIODL)
     Call ID: 5X1fPIODL
      Args:
        query: import matplotlib.pyplot as plt

    # Data for total sales revenue
    dealerships = ['Dealership A', 'Dealership B', 'Dealership J', 'Dealership G', 'Dealership H']
    sales_revenue = [65000, 48000, 38000, 35000, 32000]

    # Create a bar graph
    plt.bar(dealerships, sales_revenue, color='blue')

    # Customize the plot
    plt.title('Total Sales Revenue for Top 5 Performing Dealerships in 2022)
    plt.xlabel ('Dealerships')
    plt.ylabel(’Total Revenus de ventes ($)’)
    plt.xticks(rotation=45)
    plt.grid(axis=’y’)

# Montre l’intrigue
    plt.tight_layout()
    plt.show()
================================= [1m Message d’outil [0m=================================
    Nom : Python_REPL

================================== [1m Message IA [0m==================================

“Your request has been fulfilled. The code was executed in the REPL. The bar chart was generated and displayed in the Python REPL. The chart is also available below:”
```

Comme prévu, l’agent a appelé avec succès l’outil `python_repl` pour générer et exécuter le code Python, ce qui a donné une représentation graphique des résultats. Remarquez que l’agent a également pu déterminer les valeurs, les étiquettes et le titre des axes x et y. Cela met en évidence le raisonnement agentique qui distingue les agents IA des chatbots LLM traditionnels.

Pour obtenir une représentation visuelle du graphe de l’agent, nous affichons le flux du graphe.

```
display(Image(agent.graph.get_graph().draw_mermaid_png()))
```

**Sortie :**

  Visualisation du graphe d’agent LangGraph

## Récapitulatif

Dans ce tutoriel, nous avons découvert comment créer un agent ReAct pour convertir les textes en SQL avec LangGraph. Au lieu d’utiliser la fonction d’exécution de l’agent prédéfinie `create_react_agent`, nous avons construit notre agent en partant de zéro. Après avoir analysé la question de l’utilisateur en langage naturel, notre agent d’intelligence artificielle utilise ses outils pour générer, valider et exécuter une requête SQL, démontrant ses compétences en SQL et Python. Avec la classe `PythonREPLTool`, l’agent est en mesure non seulement de générer mais aussi d’exécuter du code Python. Pour visualiser l’exécution réussie de cet outil, nous avons demandé à l’agent une représentation graphique de sa réponse. La boucle conditionnelle entre le LLM et les nœuds de l’outil permet l’architecture d’agent ReAct. Dans ce tutoriel, nous avons démontré les capacités de codage et de raisonnement multimodal de Mistral Medium 3. Pour aller plus loin, n’hésitez pas à expérimenter avec des nœuds et des arêtes supplémentaires dans le graphe.
