> Source : https://www.ibm.com/fr-fr/think/tutorials/ai-agent-evaluation

# Évaluation des agents IA, des prompts aux indicateurs

## Qu’est-ce qu’un agent IA ?

Un agent IA désigne un système logiciel capable d’effectuer des tâches de manière autonome pour le compte d’un utilisateur ou d’un autre système, en développant son workflow et en utilisant des outils externes si nécessaire.

Les agents vont bien au-delà du simple traitement et de la compréhension du langage. Ils sont capables de prise de décision, de résoudre des problèmes, d’interagir avec leur environnement et d’agir pour atteindre des objectifs.

Les agents IA sont désormais intégrés à diverses solutions d’entreprise, allant de l’automatisation et du génie logiciel, en passant par les interfaces conversationnelles et la mise en œuvre de la génération de code. S’appuyant sur de grands modèles de langage (LLM), ils sont capables de comprendre des instructions complexes, de les décomposer en étapes, d’interagir avec des ressources externes et de déterminer quand déployer certains outils ou services pour accomplir des tâches.

## Pourquoi est-il important d’évaluer les agents ?

L’évaluation de l’agent est une procédure importante lors de la création et du déploiement de systèmes autonomes d’IA, car elle permet de mesurer la capacité d’un agent à accomplir les tâches qui lui sont assignées, à prendre des décisions et à interagir avec les utilisateurs ou les environnements. De cette manière, nous pouvons garantir que les agents fonctionnent de manière fiable, efficace et éthique dans les cas d’utilisation prévus.

**Les principales raisons justifiant l’évaluation des agents sont les suivantes :**

- **Vérification fonctionnelle :** cette étape permet de vérifier les comportements et les actions de l’agent dans certaines conditions, ainsi que la réalisation de ses objectifs dans des contraintes définies.
- **Optimisation de la conception :** identifie les lacunes et les inefficacités dans le raisonnement, la planification ou l’utilisation des outils de l’agent, ce qui nous permet d’améliorer de manière itérative son architecture et son flux de travail.
- **Robustesse :** évalue la capacité de l’agent à faire face à des cas limites, des situations hostiles ou des conditions sous-optimales, ce qui peut améliorer la tolérance aux pannes et la résilience.
- **Indicateurs de performance et de ressources :** la latence, le débit, la consommation de tokens, la mémoire et d’autres indicateurs système peuvent être surveillés pour évaluer l’efficacité à l’exécution et minimiser les coûts d’exploitation.
- **Qualité de l’interaction avec l’utilisateur :** mesure la clarté, l’utilité, la cohérence et la pertinence des réponses de l’agent comme indicateur de la satisfaction de l’utilisateur ou de l’efficacité de la conversation.
- **Analyse de la réalisation des objectifs :** en utilisant des critères de réussite ou des tâches spécifiques de référence, nous pouvons évaluer avec quelle fiabilité et quelle précision l’agent a atteint ses objectifs.
- **Considérations éthiques et sécuritaires :** la production de l’agent peut être évaluée en termes d’équité, de partialité, de danger potentiel et de respect des procédures de sécurité.

## Indicateurs d’évaluation pour les agents IA

L’évaluation de la performance d’un agent IA utilise des indicateurs organisés en plusieurs classes formelles de performance : précision, temps de réponse (vitesse) et coût des ressources utilisées. La précision décrit la capacité de l’agent à fournir des réponses correctes et pertinentes, ainsi que sa capacité à remplir les fonctions prévues. Le temps de réponse mesure la rapidité avec laquelle l’agent traite la demande et produit le résultat. La réduction de la latence est particulièrement importante dans les programmes interactifs et en temps réel. Le coût mesure les ressources informatiques consommées par l’agent, telles que l’utilisation de tokens, l’appel d’une API ou le temps système. Ces indicateurs fournissent des lignes directrices pour améliorer les performances du système et limiter les coûts opérationnels.

Alors que les indicateurs clés tels que l’**exactitude**, l’**utilité** et la **cohérence** relèvent de la précision, le temps de réponse (latence) mesure des indicateurs tels que le **débit**, la **latence moyenne et** le **délai** **d’expiration**. Les indicateurs de coût comprennent l’ **utilisation de token**, le **temps de calcul**, le **nombre d’appels d’API** et la **consommation de mémoire**.

Dans ce tutoriel, nous allons découvrir les indicateurs clés d’**exactitude, utilité et cohérence** qui relèvent de la **précision**.

- **Exactitude :** l’exactitude évalue si les réponses de l’agent sont factuellement exactes et logiquement vraies par rapport au prompt fourni ou à la tâche à accomplir. Cet indicateur est souvent la mesure la plus élémentaire, en particulier dans des domaines tels que la santé, le conseil juridique ou l’assistance technique.
- **Utilité :** l’utilité évalue dans quelle mesure la réponse de l’agent est utile ou exploitable pour l’intention de l’utilisateur. Même si une réponse est factuellement correcte, elle peut ne pas être utile si elle ne propose pas de solution ou d’étapes suivantes.
- **Cohérence :** elle est liée à la fluidité, tant logique que narrative. Elle est importante dans les interactions à plusieurs tours et dans les interactions où le raisonnement s’effectue en plusieurs étapes. La cohérence fait référence au fait que l’agent « a du sens » du début à la fin.

Vous développerez un agent de voyage et évaluerez ses performances à l’aide d’un « LLM-as-a-judge » (LLM en tant que juge).

## Prérequis

1.  Vous devez disposer d’un [compte IBM® Cloud](https://cloud.ibm.com/registration?utm_source=ibm_developer&utm_content=in_content_link&utm_id=tutorials_awb-implement-xgboost-in-python&cm_sp=ibmdev-_-developer-_-trial) pour créer un projet [watsonx.ai](https://www.ibm.com/fr-fr/products/watsonx-ai).

2.  Vous avez également besoin de la version 3.12.7 de Python

## Étapes

### Étape 1. Configurez votre environnement

Bien que vous puissiez choisir parmi plusieurs outils, ce tutoriel vous explique comment configurer un compte IBM pour utiliser un Jupyter Notebook.

1.  Connectez-vous à [watsonx.ai](https://dataplatform.cloud.ibm.com/registration/stepone?context=wx&apps=all) en utilisant votre compte IBM Cloud.

2.  Créez un [projet watsonx.ai](https://www.ibm.com/docs/en/watsonx/saas?topic=projects-creating-project). Vous pouvez obtenir l’ID de votre projet à partir de celui-ci. Cliquez sur l’onglet **Manage (Gérer)**. Ensuite, copiez l’ID du projet dans la section **Details (Détails)** de la page**General (Général)**. Vous aurez besoin de cet ID pour ce tutoriel.

3.  Créez un [Jupyter Notebook](https://www.ibm.com/docs/en/watsonx/saas?topic=editor-creating-managing-notebooks). Cette étape ouvre un environnement Jupyter Notebook dans lequel vous pouvez copier le code de ce tutoriel. Vous pouvez également télécharger ce notebook sur votre système local et le charger dans votre projet watsonx.ai en tant qu’actif. Vous trouverez d’autres tutoriels IBM® Granite auprès de la Communauté IBM Granite.

### Étape 2. Configurez une instance d’exécution watsonx.ai et une clé d’API

1.  Créez une instance de service d’exécution [watsonx.ai](https://cloud.ibm.com/catalog/services/watsonxai-runtime) (sélectionnez votre région et choisissez le plan Lite, qui est une instance gratuite).

2.  Générez une interface de programmation des applications [clé](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html).

3.  Associez l’instance de service d’exécution watsonx.ai au projet que vous avez créé dans [watsonx.ai](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/assoc-services.html).

### Étape 3. Installez et importez les bibliothèques pertinentes et configurer vos identifiants

Nous avons besoin de quelques bibliothèques et modules pour ce tutoriel. Veuillez vous assurer d’importer les éléments suivants. S’ils ne sont pas installés, une rapide commande pip install vous permettra d’y remédier.

*Remarque, ce tutoriel a été réalisé en utilisant Python 3.12.7.*

```
!pip install -q langchain langchain-ibm langchain_experimental langchain-text-splitters langchain_chroma transformers bs4 langchain_huggingface sentence-transformers
```

```python
import os
import getpass
import requests
import random
import json
from typing import Type
from typing import Dict, List
from langchain_ibm import WatsonxLLM
from langchain_ibm import ChatWatsonx
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from langchain_ibm import WatsonxEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents.agent_types import AgentType
from langchain.prompts import ChatPromptTemplate
from langchain.evaluation import load_evaluator
from langchain.agents import initialize_agent, Tool
```

Pour définir nos identifiants, nous avons besoin des **WATSONX_APIKEY et WATSONX_PROJECT_ID** que vous avez générés à l’étape 1. Nous allons également définir l’URL qui servira de point de terminaison d’API. Votre point de terminaison d’API peut varier en fonction de votre emplacement géographique.

```
WATSONX_APIKEY = getpass.getpass("Please enter your watsonx.ai Runtime API key (hit enter): ")
WATSONX_PROJECT_ID = getpass.getpass("Please enter your project ID (hit enter): ")
URL = "https://us-south.ml.cloud.ibm.com"
```

### Étape 4. Initialisez votre LLM

Nous utiliserons le modèle d’instruction Granite 3 – 8B pour ce tutoriel. Pour initialiser le LLM, nous devons définir les paramètres du modèle. Pour en savoir plus sur ces paramètres de modèle, tels que les limites minimales et maximales de jetons, reportez-vous à la [documentation](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#metanames.GenTextParamsMetaNames).

```json
llm = ChatWatsonx(model_id="ibm/granite-3-8b-instruct",
url = URL,
apikey = WATSONX_APIKEY,
project_id = WATSONX_PROJECT_ID,
params = {"decoding_method": "greedy","temperature": 0, "min_new_tokens": 5,
"max_new_tokens": 2000})
```

### Étape 5. Créez un assistant de voyage

Créons un assistant de voyage destiné à aider les utilisateurs à organiser leurs voyages.

Nous allons créer une application simple qui aidera les utilisateurs dans l’organisation de leurs voyages en récupérant des informations sur les compagnies aériennes et les hôtels en réponse à leurs demandes en se connectant à une API de voyage externe. Afin d’intégrer les agents IA pour la planification dynamique des voyages, nous disposerons d’une fonction simple qui effectue des requêtes API et les intègre dans un outil.

```python
def travel_api(query: str) -> str:
# Example of connecting to a real travel API
response = requests.get("https://www.partners.skyscanner.net", params={"query": query})
if response.status_code == 200:
return response.json().get("result", "No results found.")
return "Error contacting travel API."
```

```
travel_tool = Tool(
name="TravelPlannerTool",
func=travel_api,
description="Connects to a travel API to find flights and hotels for a given city and date"
)
```

```
agent = initialize_agent(
tools=[travel_tool],
llm=llm,
agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
verbose=True,
handle_parsing_errors= "Check your output and make sure it conforms! Do not output an action and a final answer at the same time."
)
```

```python
query = "What are the best places to visit in India during winters?"
response = agent.invoke(query)
print("\n--- Travel Agent Response ---")
print(response)
```

### Étape 6. Lancez une évaluation et obtenez le score

Enfin, nous lançons une évaluation et nous imprimons le score d’évaluation final. Afin d’évaluer le planificateur de voyage en utilisant trois critères distincts (exactitude, utilité et cohérence), un prompt structuré est développé pour un évaluateur LLM.

```python
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

evaluation_prompt = PromptTemplate(
input_variables=["input", "prediction"],
template="""
You are an evaluation agent.

### User Input:
{input}

### Agent's Response:
{prediction}

Evaluate this response based on:
- Correctness (Is the information factually accurate?)
- Helpfulness (Is it useful and actionable?)
- Coherence (Is it well-written and logically structured?)

Reply in this format:
Correctness: <score>/5 - <reason>
Helpfulness: <score>/5 - <reason>
Coherence: <score>/5 - <reason>
"""
)
```

```
eval_input = evaluation_prompt.format(input=query, prediction=response)
evaluation_result = agent.invoke(eval_input)
```

Le résultat montre une évaluation à la fois qualitative et quantitative du planificateur de voyages, générée à l’aide de trois critères : exactitude, utilité et cohérence.

Voyons ce que chaque score et chaque indicateur signifie dans le contexte du résultat fourni par l’agent :

- **L’exactitude** nous indique dans quelle mesure la réponse est factuellement exacte et logique. Dans l’exemple précédent, le contenu factuel est correct, d’où le score d’exactitude de 5 sur 5.
- L’**utilité** indique dans quelle mesure la réponse est utile et pertinente par rapport aux besoins de l’utilisateur. Un score de 5 sur 5 dans ce scénario signifie que le plan de voyage proposé par l’IA est utile et conçu de manière réfléchie. Le score indique qu’il est utile pour quelqu’un qui recherche les meilleurs endroits à visiter en Inde pendant l’hiver pour la première fois.
- La **cohérence** indique si le planificateur est organisé de manière logique et facile à lire. Notre exemple a reçu un score de cohérence élevé de 5.

 

## Conclusion

Pour évaluer la capacité d’un agent à répondre réellement aux besoins des utilisateurs, des critères tels que la cohérence, l’utilité et la précision jouent un rôle central. Que l’on travaille avec OpenAI, IBM Granite ou d’autres modèles de LLM en tant que service, il est essentiel de s’appuyer sur des méthodes d’évaluation structurées (jeux de données d’évaluation, tests de référence, annotations et vérité terrain) pour tester minutieusement les résultats finaux. Dans les cas d’utilisation pratiques tels que les chatbots ou le support client basé sur la RAG, les cadres des exigences open source comme LangGraph sont inestimables. Ils permettent une automatisation évolutive, un routage fiable et des cycles d’itération rapides. Ces technologies facilitent également l’alimentation des systèmes d’IA générative, le débogage des comportements et l’optimisation et la configuration des workflows complexes. En définissant soigneusement les cas de test et en surveillant les indicateurs d’observabilité tels que le coût de calcul, le prix et la latence, les équipes peuvent améliorer de manière constante les performances du système. En fin de compte, appliquer une approche d’évaluation fiable et reproductible apporte de la rigueur aux systèmes de machine learning et renforce leur fiabilité au fil du temps.
