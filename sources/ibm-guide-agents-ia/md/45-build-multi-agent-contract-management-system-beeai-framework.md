> Source : https://www.ibm.com/fr-fr/think/tutorials/build-multi-agent-contract-management-system-beeai-framework

# Créer un système de gestion de contrats multi-agent avec BeeAI et Granite

Dans ce tutoriel, vous allez créer un [système multi-agent](https://www.ibm.com/fr-fr/think/topics/multiagent-system) entièrement local avec [IBM® Granite](https://www.ibm.com/fr-fr/granite) en utilisant BeeAI en Python. Ces agents collaboreront pour négocier un accord contractuel de services d’aménagement paysager entre deux entreprises, en tenant compte des tendances du marché et des contraintes budgétaires internes. Le workflow sera composé d’un agent de conseil budgétaire, d’un agent de synthèse de contrat, d’un agent de recherche web et d’un agent de conseil en approvisionnement. Compte tenu du contrat, des données budgétaires, du secteur des services et des noms d’entreprise fournis par l’utilisateur, les agents collaborent pour produire un e-mail négociant les conditions du contrat en faveur du client.

## Qu’est-ce que BeeAI ?

BeeAI, développé par IBM® Research et désormais cédé à la Linux Foundation, est une plateforme d’[IA agentique](https://www.ibm.com/fr-fr/think/topics/agentic-ai) open source qui permet aux développeurs de créer des agents d’IA à partir de n’importe quel [cadre](https://www.ibm.com/fr-fr/think/insights/top-ai-agent-frameworks).1

Un [agent d’IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) désigne un système ou un programme créé à partir d’un [grand modèle de langage (LLM)](https://www.ibm.com/fr-fr/think/topics/large-language-models) afin d’effectuer des tâches de manière autonome pour le compte d’un utilisateur ou d’un autre système en concevant son propre workflow et en utilisant les [outils](https://www.ibm.com/fr-fr/think/topics/tool-calling) disponibles. Les agents d’IA sont plus avancés que les [chatbots](https://www.ibm.com/fr-fr/think/topics/chatbots) LLM traditionnels, car ils peuvent accéder à des outils prédéfinis, planifier des actions futures, et nécessitent peu ou pas d’intervention humaine pour résoudre et automatiser des problèmes complexes.

Le prédécesseur de BeeAI est le Bee Agent Framework, un cadre [open source](https://www.ibm.com/fr-fr/think/topics/open-source) spécifiquement conçu pour créer des agents LLM individuels. À l’inverse, BeeAI fournit un écosystème plus avancé pour construire et orchestrer des workflows multi-agents.

BeeAI est :

- Indépendant de tout cadre.
- Disponible en TypeScript et en Python.
- Basé sur [l’Agent Communication Protocol (ACP)](https://www.ibm.com/fr-fr/think/topics/agent-communication-protocol), conçu par IBM Research, qui va au-delà du [Model Context Protocol (MCP)](https://www.ibm.com/fr-fr/think/topics/model-context-protocol) en standardisant la manière dont les [agents communiquent](https://www.ibm.com/fr-fr/think/topics/ai-agent-communication) entre eux. L’ACP permet à des agents issus de différents frameworks tels que [LangGraph](https://www.ibm.com/fr-fr/think/topics/langgraph), [crewAI](https://www.ibm.com/fr-fr/think/topics/crew-ai) ou BeeAI de fonctionner dans un environnement d’exécution constant.2
- Intégré à Arize Phoenix, un outil open source permettant de tracer le comportement des agents et d’assurer leur observabilité. Vous trouverez plus d’informations sur le débogage des agents via les journaux et la télémétrie dans la documentation officielle.
- Capable de s’exécuter entièrement en local sur votre machine. Les agents peuvent également être déployés dans des environnements partagés.
- Composé d’interfaces unifiées pour diverses fonctionnalités, notamment les conversations, les embeddings et les sorties structurées, comme JSON, ce qui permet de changer de modèle sans modifier le code existant.

## Étapes

Ce guide étape par étape est disponible sur notre référentiel GitHub sous forme de Jupyter Notebook.

### Étape 1. Configurez votre environnement

Nous devons d’abord configurer notre environnement en respectant certaines conditions préalables.\
1. Dans ce tutoriel, nous n’utiliserons pas d’[interface de programmation d’application (API)](https://www.ibm.com/fr-fr/think/topics/api) comme celles disponibles via [IBM watsonx.ai](https://www.ibm.com/fr-fr/products/watsonx-ai) et OpenAI. À la place, nous pouvons installer la dernière version d’Ollama pour exécuter le modèle localement.\
Le moyen le plus simple d’installer Ollama pour macOS, Linux et Windows est de se rendre sur la page web : https://ollama.com/download. Cette étape consistera à installer une application de barre de menu pour exécuter le serveur Ollama en arrière-plan et vous tenir au courant des dernières versions.\
Vous pouvez également installer Ollama avec Homebrew dans votre terminal :

```bash
brew install ollama
```

Si vous procédez à l’installation à partir de Homebrew ou si vous construisez à partir d’une source, vous devez démarrer le serveur central :

```bash
ollama serve
```

2. Plusieurs LLM prennent en charge les appels d’outil, tels que les derniers modèles Llama de Meta et les modèles Mistral de Mistral AI. Pour ce tutoriel, nous utiliserons le modèle open source Granite 3.3 d’IBM. Ce modèle offre des capacités améliorées de raisonnement et de suivi d’instructions.3 Extrayez le dernier modèle Granite 3.3 en exécutant la commande suivante dans votre terminal :

```bash
ollama pull granite3.3:8b
```

3. Pour éviter les conflits de dépendance de paquet, configurons un environnement virtuel. Pour créer un environnement virtuel avec la version 3.11.9 de Python, exécutez la commande suivante dans votre terminal :

```bash
python3.12 -m venv .venv
```

Ensuite, pour activer l’environnement, exécutez :

```
source .venv/bin/activate
```

4. Votre fichier `requirements.txt` doit contenir les paquets suivants. Ces paquets sont indispensables pour créer des agents avec le cadre d’exigences BeeAI et intégrer les classes LangChain nécessaires à l’initialisation des outils.

```
beeai-framework
beeai-framework[duckduckgo]
langchain-core
langchain-community
pandas
```

Pour installer ces paquets, exécutez la commande suivante dans votre terminal :

```bash
pip install -r requirements.txt
```

5. Créez un nouveau fichier Python intitulé `bee-script.py` en exécutant cette commande dans votre terminal :

```
touch bee-script.py
```

En haut du nouveau fichier Python, incluez les instructions d’importation des bibliothèques et modules nécessaires.

```python
import asyncio
import pandas as pd
import os
import traceback
import sys

from beeai_framework.backend import ChatModel
from beeai_framework.tools.search.duckduckgo import DuckDuckGoSearchTool
from beeai_framework.workflows.agent import AgentWorkflow, AgentWorkflowInput
from beeai_framework.errors import FrameworkError
from beeai_framework.adapters.langchain import LangChainTool
from langchain_core.tools import StructuredTool
from typing import Any
```

### Étape 2. Instanciez votre agent et votre workflow

Dans une méthode principale asynchrone utilisant `asyncio` , incorporons les classes ChatModel et AgentWorkflow pour instancier notre LLM et notre workflow Granite. Nous pouvons simplement fournir l’ID du modèle Ollama ainsi qu’un nom de workflow. L’instanciation de ce workflow nous permet d’ajouter des agents et de créer notre système multi-agent. Ajoutez cette méthode principale à votre fichier Python.

```python
async def main() -> None:
llm = ChatModel.from_name("ollama:granite3.3:8b")
workflow = AgentWorkflow(name="Procurement")
```

Une représentation visuelle du workflow agentique est fournie ci-dessous :

  Workflow agentique pour la gestion des contrats

Nous assemblerons chaque composant de ce workflow lors des étapes suivantes.

### Étape 3. Demandez une entrée à l’utilisateur

Notre workflow repose sur les entrées utilisateur. Les entrées initiales requises sont les noms du client et du prestataire. L’utilisateur sera invité à entrer les données avec le texte suivant lors de l’exécution du workflow à une étape ultérieure. Ajoutez le code suivant à la méthode principale :

```
client_company = input("Please enter the client company: ") #Example: Company A
contractor_company = input("Please enter the contractor company: ") #Example: Company B
```

Nous aurons également besoin du nom des fichiers contenant le rapport budgétaire du client,`budget-data.csv` , et le contrat entre les deux entreprises, `contract.txt` . Dans notre exemple, le contrat concerne des services d’aménagement paysager fournis au client par le prestataire. Vous trouverez les fichiers d’exemple dans notre référentiel GitHub. La structure du projet doit ressembler à la suivante :

```
├── .venv/ # Virtual environment
├── bee-script.py # The Python script
├── contract.txt # The contract
└── budget-data.csv # Client's budget report
```

Dans le code suivant, nous vérifions également les extensions de fichier pour nous assurer qu’elles correspondent au format prévu. Si l’un des fichiers n’est pas du bon type, l’utilisateur sera invité à réessayer.

```json
client_budget_file = input(f"Enter the file name of the budget report for {client_company} (in the same directory level): ") #Example: budget_data.csv
while os.path.splitext(client_budget_file)[1].lower() != ".csv":
client_budget_file = input(f"Budget report must be in .csv format, please try again: ")

contract_file = input(f"Enter the file name of the contract between {client_company} and {contractor_company} (in the same directory level): ") #Example: contract.txt
while os.path.splitext(contract_file)[1].lower() != ".txt":
contract_file = input(f"Contract must be in .txt format, please try again: ")
```

La dernière entrée utilisateur requise est le secteur du service décrit dans le contrat : finance, construction ou autre.

```
service_industry = input(f"Enter the industry of the service described in this contract (e.g., finance, construction, etc.): ") #Example: landscaping
```

### Étape 4. Configurez l’outil budgétaire

Le premier outil que nous pouvons intégrer à notre système multi-agent est destiné à l’agent de conseil budgétaire. Cet agent est chargé de lire les données budgétaires du client. La fonction fournie à l’agent est`get_budget_data` , dans laquelle le fichier CSV contenant les données budgétaires est lu et un message d’erreur est renvoyé si le fichier n’existe pas ou si une erreur inattendue se produit. Pour accéder au fichier en utilisant le nom de fichier fourni par l’utilisateur, nous devons d’abord récupérer le répertoire actuel. Pour ce faire, nous pouvons utiliser la méthode`os` suivante :

```
current_directory = os.getcwd()
```

Maintenant, configurons la force motrice de l’agent, la fonction `get_budget_data` , qui utilise le répertoire actuel ainsi que l’entrée utilisateur pour accéder au fichier et le lire.

```python
def get_budget_data():
try:
budget = pd.read_csv(os.path.join(current_directory, client_budget_file))
except FileNotFoundError:
return client_budget_file + " not found. Please check correct file name."
except Exception as e:
return f"An error occurred: {e}"
return budget
```

Pour garantir une utilisation appropriée de cet outil, utilisons la classe `StructuredTool` de LangChain. Ici, nous fournissons la fonction, le nom de l’outil et la description de l’outil, et nous définissons le paramètre `return_direct` pour qu’il soit vrai ou faux. Ce dernier paramètre indique simplement à l’agent s’il doit renvoyer directement la production de l’outil ou la synthétiser.

```
get_budget = StructuredTool.from_function(
func=get_budget_data,
name="GetBudgetData",
description=f"Returns the budget data for {client_company}.",
return_direct=True,
)
```

Grâce à l’adaptateur LangChain de BeeAI, LangChainTool, nous pouvons finaliser l’initialisation de notre premier outil.

```
budget_tool = LangChainTool[Any](get_budget)
```

### Étape 5. Configurez l’outil contractuel

Le prochain outil que nous pouvons créer est destiné à l’agent de synthèse de contrat. Cet agent est chargé de lire le contrat entre le client et le prestataire. La fonction fournie à l’agent est `get_contract_data` , dans laquelle le fichier texte contenant le contrat est lu et un message d’erreur est renvoyé si le fichier n’existe pas ou si une erreur inattendue se produit. Le code requis pour cette étape est similaire à celui de l’étape 3.

```python
def get_contract_data():
try:
with open(os.path.join(current_directory, contract_file), 'r') as file:
content = file.read()
except FileNotFoundError:
return contract_file + " not found. Please check correct file name."
except Exception as e:
return f"An error occurred: {e}"
return content
```

```
get_contract = StructuredTool.from_function(
func=get_contract_data,
name="GetContractData",
description=f"Returns the contract details.",
return_direct=True,
)
```

```
contract_tool = LangChainTool[Any](get_contract)
```

### Étape 6. Établissez le workflow agentique

Dans cette étape, nous pouvons ajouter les différents agents à notre workflow. Fournissons aux agents de conseil budgétaire et de synthèse de contrat les outils personnalisés correspondants. Nous pouvons également définir le nom de l’agent, le rôle, les instructions, la liste d’outils et le LLM. 

```
workflow.add_agent(
name="Budget Advisor",
role="A diligent budget advisor",
instructions="You specialize in reading internal budget data in CSV format.",
tools=[budget_tool],
llm=llm,
)

workflow.add_agent(
name="Contract Synthesizer",
role="A diligent contract synthesizer",
instructions=f"You specialize in reading contracts.",
tools=[contract_tool],
llm=llm,
)
```

Pour rechercher sur le web les tendances du marché dans le secteur concerné, nous pouvons créer un agent ayant accès à l’outil LangChain prédéfini `DuckDuckGoSearchTool` . Cet outil récupère les données du web à l’aide du moteur de recherche DuckDuckGo.

```
workflow.add_agent(
name="Web Search",
role="A web searcher.",
instructions=f"You can search the web for market trends, specifically in the {service_industry} industry.",
tools=[DuckDuckGoSearchTool()],
llm=llm,
)
```

Le quatrième et dernier agent de notre système multi-agent est le conseiller en [approvisionnement](https://www.ibm.com/fr-fr/think/topics/ai-agents-in-procurement). Cet agent est chargé d’utiliser les informations récupérées et synthétisées par les autres agents pour écrire un e-mail convaincant au prestataire en faveur du client. L’e-mail doit tenir compte des tendances du marché et des contraintes budgétaires internes du client pour négocier les conditions du contrat. Cet agent n’a pas besoin d’outils externes, mais est piloté par ses instructions.

```
workflow.add_agent(
name="Procurement Advisor",
role="A procurement advisor",
instructions=f"You write professional emails to {contractor_company} with convincing negotiations that factor in market trends and internal budget constraints. You represent {client_company}.",
llm=llm,
)
```

### Étape 7. Exécutez le workflow agentique

Nous pouvons maintenant finaliser notre méthode principale avec tout le code créé jusqu’à présent. À la fin de la méthode principale, nous pouvons inclure l’exécution du workflow agentique. Compte tenu du mot-clé`await` , nous pouvons gérer efficacement l’exécution simultanée des tâches et attendre l’exécution de chaque tâche. Votre fichier Python doit contenir le code suivant :

```python
import asyncio
import pandas as pd
import os
import traceback
import sys

from beeai_framework.backend import ChatModel
from beeai_framework.tools.search.duckduckgo import DuckDuckGoSearchTool
from beeai_framework.workflows.agent import AgentWorkflow, AgentWorkflowInput
from beeai_framework.errors import FrameworkError
from beeai_framework.adapters.langchain import LangChainTool
from langchain_core.tools import StructuredTool
from typing import Any

async def main() -> None:

llm = ChatModel.from_name("ollama:granite3.3:8b")

workflow = AgentWorkflow(name="Procurement Agent")

client_company = input("Please enter the client company: ")
contractor_company = input("Please enter the contractor company name: ")

client_budget_file = input(f"Enter the file name of the budget report for {client_company} (in the same directory level): ")
while os.path.splitext(client_budget_file)[1].lower() != ".csv":
client_budget_file = input(f"Budget report must be in .csv format, please try again: ")

contract_file = input(f"Enter the file name of the contract between {client_company} and {contractor_company} (in the same directory level): ")
while os.path.splitext(contract_file)[1].lower() != ".txt":
contract_file = input(f"Contract must be in .txt format, please try again: ")

service_industry = input(f"Enter the industry of the service described in this contract (e.g., finance, construction, etc.): ")
```

```
current_directory = os.getcwd()
```

```python
def get_budget_data():
try:
budget = pd.read_csv(os.path.join(current_directory, client_budget_file))
except FileNotFoundError:
return client_budget_file + " not found. Please check correct file name."
except Exception as e:
return f"An error occurred: {e}"
return budget

get_budget = StructuredTool.from_function(
func=get_budget_data,
name="GetBudgetData",
description=f"Returns the budget data for {client_company}.",
return_direct=True,
)

budget_tool = LangChainTool[Any](get_budget)

def get_contract_data():
try:
with open(os.path.join(current_directory, contract_file), 'r') as file:
content = file.read()
except FileNotFoundError:
return contract_file + " not found. Please check correct file name."
except Exception as e:
return f"An error occurred: {e}"
return content

get_contract = StructuredTool.from_function(
func=get_contract_data,
name="GetContractData",
description=f"Returns the contract details.",
return_direct=True,
)

contract_tool = LangChainTool[Any](get_contract)

workflow.add_agent(
name="Budget Advisor",
role="A diligent budget advisor",
instructions="You specialize in reading internal budget data in CSV format.",
tools=[budget_tool],
llm=llm,
)

workflow.add_agent(
name="Contract Synthesizer",
role="A diligent contract synthesizer",
instructions=f"You specialize in reading contracts.",
tools=[contract_tool],
llm=llm,
)

workflow.add_agent(
name="Web Search",
role="A web searcher.",
instructions=f"You can search the web for market trends, specifically in the {service_industry} industry.",
tools=[DuckDuckGoSearchTool()],
llm=llm,
)

workflow.add_agent(
name="Procurement Advisor",
role="A procurement advisor",
instructions=f"You write professional emails to {contractor_company} with convincing negotiations that factor in market trends and internal budget constraints. You represent {client_company}.",
llm=llm,
)

response = await workflow.run(
inputs=[
AgentWorkflowInput(
prompt=f"Extract and summarize the key obligations, deliverables, and payment terms from the contract between {client_company} and {contractor_company}.",
),
AgentWorkflowInput(
prompt=f"Analyze the internal budget data for {client_company}.",
),
AgentWorkflowInput(
prompt=f"Write a formal email to {contractor_company}. In the email, negotiate the contract terms in favor of {client_company}, factoring in market trends and internal budget constraints.",
),
]
).on(
"success",
lambda data, event: print(
f"-> Step '{data.step}' has been completed with the following outcome.\n\n{data.state.final_answer}"     
),
)

print("Final email: ")
print(response.state.final_answer)

if __name__ == "__main__":
try:
asyncio.run(main())
except FrameworkError as e:
traceback.print_exc()
sys.exit(e.explain())
```

Pour obtenir un exemple de données contractuelles et budgétaires ainsi que le script final, consultez notre référentiel GitHub. Pour lancer le projet, nous pouvons exécuter la commande suivante dans notre terminal :

```bash
python bee-script.py
```

Utilisez cet *exemple d’entrée utilisateur* :

- *Indiquez le nom du client :* entreprise A
- *Indiquez le nom du prestataire :* entreprise B
- *Indiquez le nom du fichier de rapport budgétaire de l’entreprise A (au même niveau de répertoire) :* budget_data.csv
- *Indiquez le nom du fichier de contrat entre l’entreprise A et l’entreprise B (au même niveau de répertoire) :* contract.txt
- *Indiquez le secteur du service décrit dans ce contrat (par exemple, finance, construction ou autre) :* aménagement paysager

Le texte suivant est un *exemple de production* obtenu en exécutant ce workflow multi-agent.

**Production :**

------------------------------------------------------------------------

**-\> L’étape « Conseil budgétaire » a donné la production suivante :**

Le budget de l’entreprise A pour la période montre un écart total de -12 700 USD. Les écarts les plus importants concernent les salaires des employés (-5 000 USD), la publicité en ligne (-3 000 USD), la publicité imprimée (-2 000 USD), ainsi que la maintenance et les réparations (-1 000 USD). Des écarts plus faibles sont également constatés dans les domaines de la location, de l’électricité, de l’eau, de l’aménagement paysager et des services de nettoyage et d’entretien. -\> L’étape « Synthèse de contrat » a donné la production suivante :

Le contrat entre l’entreprise A et l’entreprise B concerne des services d’aménagement paysager de la propriété du client, dans le Delaware. Le paiement total à effectuer par l’entreprise A à la fin des travaux s’élève à 5 500 USD. Les deux parties ont convenu de se conformer aux lois et aux réglementations applicables dans le Delaware.

**-\> L’étape « Recherche sur le web » a donné la production suivante :**

Objet : Proposition de négociation relative aux services d’aménagement paysager

Chère équipe de l’entreprise B,

J’espère que vous allez bien.

Après un examen minutieux de nos données budgétaires internes et des tendances du marché dans le secteur de l’aménagement paysager, nous avons repéré des domaines dans lesquels nous pensons pouvoir procéder à des ajustements pour mieux respecter nos contraintes financières tout en maintenant une qualité élevée de service.

1.  **Étendue des travaux** : nous proposons une réduction de l’étendue des travaux pour nous concentrer sur les services essentiels qui ont une incidence directe sur l’attrait extérieur et la valeur de la propriété. Cela peut inclure l’élagage des arbres, la taille des arbustes et l’entretien des pelouses, ainsi que la plantation occasionnelle d’espèces colorées pour renforcer l’intérêt visuel.

2.  **Conditions de paiement** : compte tenu des tendances actuelles du marché, qui montrent une légère baisse des coûts d’aménagement paysager en raison de la concurrence accrue, nous vous demandons de bien vouloir reconsidérer le montant total du paiement. Nous proposons un paiement total révisé de 4 800 USD à l’achèvement des travaux, soit une réduction de 12 %.

3.  **Calendrier** : pour optimiser l’affectation des ressources et éviter de trop perturber nos opérations, nous suggérons de prolonger le calendrier du projet de deux semaines. Cet ajustement nous permettra de mieux gérer nos contraintes budgétaires internes sans compromettre la qualité des services.

Nous pensons que ces ajustements permettront aux deux parties d’obtenir un résultat mutuellement bénéfique tout en respectant les lois et réglementations applicables du Delaware. Nous vous remercions de votre compréhension et restons ouverts à d’autres discussions en vue de parvenir à un accord conforme aux tendances actuelles du marché et à nos contraintes budgétaires internes.

Je vous remercie de l’intérêt que vous porterez à cette affaire. Veuillez nous indiquer si vous acceptez les ajustements proposés ou si vous avez des contre-propositions à formuler.

Cordialement,

\[Votre nom\]

Entreprise A

**-\> L’étape « Conseil en approvisionnement » a donné le résultat suivant :**

La réponse finale a été envoyée à l’entreprise B, proposant un paiement total révisé de 4 800 USD à l’achèvement des travaux, soit une réduction de 12 %. La proposition comprend également un périmètre de travail réduit et un calendrier de projet prolongé.

Dernier e-mail : la réponse finale a été envoyée à l’entreprise B, proposant un paiement total révisé de 4 800 USD à l’achèvement des travaux, soit une réduction de 12 %. La proposition comprend également un périmètre de travail réduit et un calendrier de projet prolongé.

------------------------------------------------------------------------

 

De toute évidence, les agents ont correctement appelé les outils disponibles pour lire et synthétiser les données contractuelles et budgétaires et formuler un e-mail efficace dans lequel les conditions du contrat sont négociées en faveur du client. Nous pouvons voir la production de chaque agent dans le workflow et l’importance du rôle de chaque agent. Les informations clés telles que l’étendue des travaux d’aménagement paysager, les conditions de paiement et le calendrier du contrat sont mis en évidence dans l’e-mail. Nous pouvons également constater que la négociation s’appuie les tendances du marché en matière d’aménagement paysager à l’avantage du client. Enfin, le paiement total révisé de 4 800 USD proposé dans l’e-mail respecte le budget d’aménagement paysager de 5 200 USD du client. Cela semble parfait !

## Synthèse

Avec ce tutoriel, vous avez créé plusieurs agents BeeAI disposant chacun d’outils personnalisés. Chaque agent a joué un rôle crucial dans le cas d’utilisation de système de gestion de contrats. Pour aller plus loin, vous pouvez consulter les différents référentiels GitHub disponibles dans l’organisation GitHub i-am-bee et créer d’autres outils personnalisés. Dans les référentiels, vous trouverez également des notebooks de démarrage Python pour mieux comprendre les composants principaux de BeeAI, tels que `PromptTemplates` , `Messages` , `Mémoire` et `Emitter` , pour l’observabilité.
