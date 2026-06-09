> Source : https://www.ibm.com/fr-fr/think/tutorials/implement-prompt-caching-langchain

# Implémenter la mise en cache des prompts avec LangChain pour créer des applications LLM efficaces

## Qu’est-ce que la mise en cache des prompts ?

La mise en cache des prompts permet de stocker et de réutiliser les réponses générées par les prompts exécutés en travaillant avec des modèles de langage comme [IBM® Granite](https://www.ibm.com/fr-fr/granite). Si la même entrée (prompt) est rencontrée à nouveau, au lieu de faire un nouvel appel d’API, l’application récupérera la réponse précédemment stockée dans le cache prompt.

La mise en cache des prompts est une sorte de « mémoire » pour votre application. Le système conserve les résultats des requêtes précédentes afin d’économiser du temps de calcul en évitant de répéter les requêtes pour une même entrée.

## Pourquoi est-ce important ?

La mise en cache des prompts est importante car elle évite les appels répétés à l’interface de programmation d’application. Pour ce faire, elle réutilise les réponses existantes pour les prompts identiques qui sont répétés. Cela se traduit par un temps de réponse plus court, des sorties cohérentes et une utilisation réduite de l’API, ce qui permet de respecter les limites de débit. Cela permet également de dimensionner le flux et d’assurer une résilience en cas de panne. La mise en cache des prompts est une fonctionnalité essentielle qui ajoute de la valeur à toute application d’IA rentable, efficace et conviviale.

## Prérequis

1.  Vous avez besoin d’un compte IBM® Cloud pour créer un projet [watsonx.ai®](https://www.ibm.com/fr-fr/products/watsonx-ai).

2.  Vous avez également besoin de la version 3.12.7 de Python

## Étapes 

#### Étape 1 : configurer l’environnement

Bien que vous puissiez choisir parmi plusieurs outils, ce tutoriel vous explique comment créer un compte IBM pour utiliser Jupyter Notebook.

1.  Connectez-vous à [watsonx.ai](https://dataplatform.cloud.ibm.com/registration/stepone?context=wx&apps=all) avec votre compte IBM Cloud.

2.  Créez un [projet watsonx.ai](https://www.ibm.com/docs/en/watsonx/saas?topic=projects-creating-project). Vous pouvez récupérer l’ID de votre projet à partir de ce dernier. Cliquez sur l’onglet Gérer. Ensuite, copiez l’ID du projet à partir de la section Details (Détails) de la page General (Général). Vous aurez besoin de cet ID pour ce tutoriel.

3.  Créez un [Jupyter Notebook](https://www.ibm.com/docs/en/watsonx/saas?topic=editor-creating-managing-notebooks). Cette étape ouvre un environnement Jupyter Notebook où vous pourrez copier le code de ce tutoriel. Sinon, vous pouvez télécharger ce notebook localement sur votre système et le charger comme actif dans votre projet watsonx.ai. Vous trouverez d’autres tutoriels Granite en consultant la Communauté IBM Granite.

#### Étape 2 : configurer une instance d’exécution watsonx.ai et une clé d’API

1.  Créez une instance de service d’[exécution watsonx.ai](https://cloud.ibm.com/catalog/services/watsonxai-runtime) (choisissez le forfait Lite, qui est une instance gratuite).

2.  Générez une [clé d’API](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html).

3.  Associez le service d’exécution watsonx.ai au projet que vous avez créé dans [watsonx.ai](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/assoc-services.html?context=cpdaas).

#### Étape 3 : installer les paquets

Nous avons besoin de bibliothèques pour travailler avec le cadre Langchain et WatsonxLLM. Commençons par installer les paquets requis. Ce tutoriel est créé avec Python 3.12.7.

*Remarque : si vous utilisez une ancienne version de pip, vous pouvez utiliser la commande *pip install --upgrade pip* pour installer facilement les derniers paquets susceptibles d’être incompatibles avec les anciennes versions. Mais si vous utilisez déjà la dernière version ou si vous avez récemment mis à jour vos paquets, vous pouvez ignorer cette commande*.

```
!pip install -q langchain langchain-ibm langchain_experimental langchain-text-splitters langchain_chroma transformers bs4 langchain_huggingface sentence-transformers
```

#### Étape 4 : importer les bibliothèques requises

**Le module os** est utilisé pour accéder aux variables d’environnement telles que les identifiants de projet et les clés d’API.

**WatsonxLLM** est un module langchain_ibm qui s’intègre aux LLM IBM Watson pour générer des sorties à partir de modèles d’IA générative.

**ChatWatsonx** permet des interactions de type chat à l’aide d’IBM watsonx et de LangChain.

**SimpleDirectoryReader** permet de charger et de lire des documents à partir d’un répertoire pour l’indexation avec LlamaIndex.

**GenParams** contient des clés de métadonnées pour configurer les paramètres de génération de texte Watsonx.

**SQLiteCache** permet de configurer une base de données SQLite local.cache.db pour éviter les appels API redondants et accélérer le développement et les tests.

Nous avons besoin de quelques bibliothèques et modules pour ce tutoriel. Veillez à importer les éléments suivants. S’ils ne sont pas installés, une installation pip résoudra rapidement le problème.

```python
import os
import getpass
import requests
import random
import json
from typing import Dict, List
from langchain_ibm import WatsonxLLM
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from langchain_ibm import WatsonxLLM
from langchain_ibm import ChatWatsonx
from llama_index.core import SimpleDirectoryReader
```

#### Étape 5 : lire les données textuelles

```python
from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader(
input_files=["~/Artificial Intelligence/Generative_AI/files/FIle2.txt"],
).load_data()

document_text = documents[0].text
print(document_text[:200] + "...")
```

#### Étape 6 : configurer les identifiants

Ce code configure des identifiants pour accéder à l’API IBM Watson Machine Learning (WML) et permet de s’assurer que l’ID du projet est correctement configuré.

- Les identifiants de dictionnaire sont créés avec l’*URL du service WML* et la *clé d’API*. La clé d’API est collectée en toute sécurité à l’aide de getpass.getpass pour éviter d’exposer les informations sensibles.
- le code tente de récupérer le PROJECT_ID à partir des variables d’environnement en utilisant os.environ. Si le PROJECT_ID n’est pas trouvé, l’utilisateur est invité à le saisir manuellement.

```json
credentials = {
"url": "https://us-south.ml.cloud.ibm.com",  # Replace with the correct region if needed
"apikey": getpass.getpass("Please enter your WML API key (hit enter): ")
}

# Set up project_id
try:
project_id = os.environ["PROJECT_ID"]
except KeyError:
project_id = input("Please enter your project_id (hit enter): ")
```

#### Étape 7 : initialiser le grand modèle de langage

Ce code initialise le LLM IBM Watson pour être utilisé dans l’application :

1.  Ce code crée une instance de watsonxLLM en utilisant le modèle ibm/granite-3-8b-instruct (Granite-3.1-8B-Instruct) conçu pour les tâches d’IA générative basées sur des instructions.
2.  Les valeurs url, apikey et projet_id des identifiants précédemment configurés sont transmises pour l’authentification et la connexion au service LLM d’IBM Watson.
3.  Configure le paramètre max_new_tokens pour limiter le nombre de tokens générés par le modèle dans chaque réponse (2 000 tokens dans ce cas).

Pour en savoir plus sur les paramètres du modèle tels que les limites minimales et maximales de token, reportez-vous à la documentation.

```
llm = WatsonxLLM(
model_id= "ibm/granite-3-8b-instruct",
url=URL,
apikey=WATSONX_APIKEY,
project_id=WATSONX_PROJECT_ID,
params={
GenParams.DECODING_METHOD: "greedy",
GenParams.TEMPERATURE: 0,
GenParams.MIN_NEW_TOKENS: 5,
GenParams.MAX_NEW_TOKENS: 2000,
GenParams.REPETITION_PENALTY:1.2,
GenParams.STOP_SEQUENCES: ["\n\n"]
}
)
```

#### Étape 8 : configurer le cache SQLite pour des réponses LLM plus rapides

**SQLiteCache** est un outil de mise en cache persistante proposé par LangChain qui stocke les réponses aux appels de LLM dans un fichier de base de données SQLite. SQLiteCache réduit intelligemment le temps de CPU en stockant les calculs coûteux, ce qui signifie qu’il se concentre sur la récupération des données au lieu de les recalculer. Au lieu de répéter l’ensemble du processus, il extrait simplement les résultats du disque, ce qui le rend efficace, fiable et réutilisable.

***La figure montre qu’avec la mise en cache des prompts, les résultats se chargent instantanément à partir du disque ; sans cette mise en cache, chaque requête perd du temps en réalisant des calculs redondants.***

```python
from langchain.cache import SQLiteCache
from langchain.globals import set_llm_cache
set_llm_cache(SQLiteCache(database_path=".langchain.db"))
```

```python
%%time
prompt = "System: You are a helpful assistant.\nUser: Why did Paul Graham start YC?\nAssistant:"
resp = llm.invoke(prompt)
print(resp)
```

Dans ce cas, le processeur n'a fonctionné que pendant 22 ms, mais le temps réel écoulé était de 1,43 seconde.

Cet exemple suggère que la majeure partie du temps a été consacrée à l’attente, probablement pour des opérations E/S (par exemple, lecture et écriture sur le disque, accès au réseau ou appel d’API).

**Maintenant, lançons le modèle une deuxième fois avec le prompt pour voir le temps de réponse.**

```
%%time
llm.predict(resp)
```

Il est clair qu’en utilisant SQLiteCache, l’unité centrale n’est utilisée que pendant 7,26 ms, alors que le temps réel est de 6,15 secondes.

Cela indique clairement qu’il faut bloquer les dépendances externes (comme l’attente de réponse d’un serveur).

## Conclusion

La mise en cache des prompts accélère et réduit le coût des requêtes API vers les grands modèles de langage comme GPT-4o. Les prompts mettent en cache des contenus tels que les tokens d’entrée et de sortie, les embeddings et les messages de l’utilisateur, un prompt système ou la sortie d’une fonction, qui utilise désormais un contenu mis en cache, et non des requêtes réseau pour une nouvelle révision. Cette méthode permet de réduire les tarifs, d’améliorer la latence de réponse et les indicateurs clés de performance (KPI).

La mise en cache des prompts peut s’avérer utile pour les chatbots, les systèmes RAG, le réglage fin et les assistants de code. Une stratégie de mise en cache robuste, qui inclut des fonctions telles que la lecture et l’écriture en cache, les messages système, le contrôle du cache et la durée de vie appropriée (TTL), permet d’améliorer le taux d’accès au cache et de réduire le taux d’échec.

Une utilisation cohérente des mêmes tokens de prompt, du préfixe de prompt et des instructions système favorise une performance constante des prompts dans les conversations à plusieurs tours et les requêtes ultérieures. Que vous utilisiez Python, un SDK, OpenAI ou un autre fournisseur, bien comprendre la mise en cache des prompts vous permettra de mieux la mettre en œuvre, quel que soit le cas d’utilisation.
