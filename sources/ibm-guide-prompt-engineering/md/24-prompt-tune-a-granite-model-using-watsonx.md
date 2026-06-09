> Source : https://www.ibm.com/fr-fr/think/tutorials/prompt-tune-a-granite-model-using-watsonx

# Utiliser la méthode de prompt-tuning pour optimiser un modèle Granite en Python avec watsonx

## Qu’est-ce que l’optimisation des prompts ?

Dans ce tutoriel, nous allons optimiser les prompts d'un [modèle IBM Granite](https://www.ibm.com/fr-fr/granite) à l’aide d’un jeu de données synthétique contenant les avis des clients sur une entreprise de toilettage pour chiens.

L’optimisation des prompts est un moyen efficace et peu coûteux d’adapter un modèle de fondation d’[intelligence artificielle (IA)](https://www.ibm.com/fr-fr/think/topics/artificial-intelligence?) à de nouvelles tâches en aval sans avoir à réentraîner l’ensemble du modèle ni à mettre à jour ses poids.

## Présentation de l’optimisation des LLM

Les[modèles de fondation sont](https://research.ibm.com/blog/what-are-foundation-models) construits sur de grands modèles de langage (LLM) et reçoivent de grandes quantités de données d’entraînement. Les cas d’utilisation courants des modèles de fondation sont les [chatbots](https://www.ibm.com/fr-fr/think/topics/chatbots?) et les assistants virtuels.[](https://www.ibm.com/fr-fr/think/topics/large-language-models?)

Il existe plusieurs façons d’améliorer l’interprétation des entrées et la qualité des réponses d’un modèle de fondation. Pour mieux comprendre ces nuances, comparons quelques-unes des méthodes.

- [**Prompt engineering**](https://www.ibm.com/fr-fr/think/topics/prompt-engineering?) est l’optimisation des réponses d’un modèle pré-entraîné en fournissant un prompt bien conçu. Aucune nouvelle donnée n’est introduite avec cette technique et le modèle reste tel quel. Avec cette méthode, le modèle reçoit une entrée et un prompt préparé. Par exemple, vous pouvez utiliser le prompt : « Traduire de l’anglais vers l’espagnol » avec l’entrée : « Bonjour ». Cette méthode nécessite plus de travail de la part de l’utilisateur. Cependant, cet effort manuel pour formuler des prompts efficaces aide les modèles d'[IA générative](https://www.ibm.com/fr-fr/think/topics/generative-ai?) à produire des réponses spécifiques à une tâche sans réentraîner l’ensemble du modèle de fondation.
- Le [**réglage fin**](https://www.ibm.com/fr-fr/think/topics/fine-tuning?) des grands modèles de langage implique de régler le même modèle en fournissant un grand nombre de jeux de données étiquetés. Le réglage fin modifie les poids du modèle et devient difficile à gérer à mesure que les tâches se diversifient. Cela nécessite une quantité importante de ressources de calcul. Cette méthode a tendance à être la plus précise, car le modèle peut être entraîné pour des cas d’utilisation très spécifiques.
- Contrairement au réglage fin, le [**prompt tuning**](https://research.ibm.com/blog/what-is-ai-prompt-tuning) ne modifie pas les poids du modèle pré-entraîné. Cette technique est efficace en paramètres, en ajustant les prompts pour guider les réponses du modèle dans la direction souhaitée. Le modèle reçoit une entrée et des prompts souples ajustables générés par l’IA elle-même. Ce contexte spécifique à une tâche guide le modèle massif pour adapter ses réponses à une tâche précise, même avec des données limitées.
- Tout comme pour le prompt tuning, le prefix-tuning implique que le modèle reçoive plusieurs exemples de sortie préférée. La différence ici est qu’un préfixe, c’est-à-dire une série de vecteurs spécifiques à une tâche, est également inclus. L’optimisation des préfixes implique à la fois des prompts souples et des prompts injectés dans les couches du modèle d’apprentissage profond. Ces « tokens virtuels » donnent au modèle ajusté la flexibilité nécessaire pour prendre en charge plusieurs nouvelles tâches à la fois. Cette méthode obtient des performances similaires à l’optimisation de toutes les couches et n’entraîne qu’environ 0,1 % des paramètres. L’optimisation des préfixes est même plus performante que le réglage fin dans les environnements à faibles données.

## Soft prompts vs hard prompts

Les prompts difficiles s’adressent à l’utilisateur et nécessitent une action de sa part. Un prompt difficile peut être considéré comme un modèle ou des instructions pour que le LLM génère des réponses. Un exemple de hard prompt est présenté ci-dessous. Nous vous invitons à consulter la page de documentation IBM pour en savoir plus sur ce type de prompt et sur plusieurs autres.

```
###For demonstration purposes only. It is not necessary to run this code block.
hard_prompt_template = """Generate a summary of the context that answers the question. Explain the answer in multiple steps if possible.
Answer style should match the context. Ideal Answer length is 2-3 sentences.\n\n{context}\nQuestion: {question}\nAnswer:
"""
```

Grâce à ce modèle de hard prompt, un LLM peut recevoir des instructions spécifiques sur la structure et le style de sortie préférés. Grâce à ce prompt explicite, le LLM serait plus susceptible de produire des réponses souhaitables de meilleure qualité.

Les soft prompts, contrairement aux hard prompts, ne sont pas écrits en langage naturel. Au lieu de cela, les prompts sont initialisés sous forme de vecteurs numériques générés par l’IA ajoutés au début de chaque entrée [embedding](https://www.ibm.com/fr-fr/think/topics/embedding?) qui distille les connaissances du modèle plus grand. Ce manque d’interprétabilité s’étend à l’IA qui choisit des prompts optimisés pour une tâche donnée. Souvent, l’IA n’est pas en mesure d’expliquer pourquoi elle a choisi ces embeddings. En comparaison à d’autres méthodes de prompting, ces tokens virtuels sont moins coûteux en calcul que le réglage fin, car le modèle lui-même reste gelé avec des poids fixes. Les prompts souples ont également tendance à surpasser les prompts durs conçus par l’humain.

Dans ce tutoriel, nous allons utiliser des prompts souples pour le réglage des prompts.

## Prérequis

Vous devez disposer d’un compte IBM Cloud pour créer un projet watsonx.ai.

## Étapes

### Étape 1. Configurer votre environnement

Bien que vous puissiez faire votre choix parmi plusieurs outils, ce tutoriel vous guide pas à pas pour configurer un compte IBM à l’aide d’un Jupyter Notebook.

1.  Connectez-vous à [watsonx.ai](https://dataplatform.cloud.ibm.com/registration/stepone) en utilisant votre compte IBM Cloud.

2.  Créez un [projet watsonx.ai](https://www.ibm.com/docs/en/watsonx/saas?topic=projects-creating-project).

    Vous pouvez obtenir l’ID de votre projet à partir de ce dernier. Cliquez sur l’onglet Manage (Gérer). Ensuite, copiez l’ID du projet dans la section Details (Détails) de la pageGeneral (Général). Vous aurez besoin de cet ID pour ce tutoriel.

3.  Créez un [Jupyter Notebook](https://www.ibm.com/docs/en/watsonx/saas?topic=editor-creating-managing-notebooks).

    Cette étape ouvre un environnement Notebook dans lequel vous pouvez copier le code de ce tutoriel pour implémenter le réglage des prompts par vous-même. Vous pouvez également télécharger ce notebook sur votre système local et le charger dans votre projet watsonx.ai en tant qu’actif. Ce Jupyter Notebook, ainsi que les jeux de données utilisés, se trouvent sur [GitHub.](https://github.com/IBM/ibmdotcom-tutorials)

### Étape 2. Configurer une instance d’exécution watsonx.ai et une clé d’API

1.  Créez une [instance de service d’exécution watsonx.ai](https://cloud.ibm.com/catalog/services/watsonxai-runtime) (sélectionnez votre région et choisissez le plan Lite, qui est une instance gratuite).

2.  Générez une [clé d’API](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html).

3.  Associez l'instance de service Runtime watsonx.ai au projet que vous avez créé dans [watsonx.ai](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/assoc-services.html).

### Étape 3. Installer et importer les bibliothèques pertinentes et configurer vos identifiants

Nous avons besoin de quelques bibliothèques et modules pour ce tutoriel. Assurez-vous d’importer les bibliothèques suivantes ; s’ils ne sont pas installés, vous pouvez résoudre ce problème en exécutant rapidement une commande pip install.

```python
#installations
%pip install ibm-watsonx-ai | tail -n 1
%pip install pandas | tail -n 1
%pip install wget | tail -n 1
%pip install scikit-learn | tail -n 1
%pip install matplotlib | tail -n 1 #imports
import wget
import pandas as pd

from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watsonx_ai.experiment import TuneExperiment
from ibm_watsonx_ai.helpers import DataConnection
from ibm_watsonx_ai.foundation_models import ModelInference
from sklearn.metrics import accuracy_score, f1_score
from datetime import datetime
```

Configurez vos identifiants. Entrez votre clé API et votre ID de projet.

```json
credentials = {
"url": "https://us-south.ml.cloud.ibm.com",
"apikey": "YOUR_API_KEY_HERE"
}

project_id = "YOUR_PROJECT_ID_HERE"
```

### Étape 4. Établir l’environnement et importer le jeu de données

Comme première étape de l’établissement de l’environnement, créez une instance d’APIClient avec vos identifiants de connexion et définissez votre identifiant de projet (project_id).

```
client = APIClient(credentials)
client.set.default_project(project_id)
```

**Output**: 

'SUCCESS'

Pour ce tutoriel, nous utiliserons un jeu de données synthétiques composé d’avis de clients sur une entreprise de toilettage pour chiens. En utilisant l’URL appropriée, nous pouvons connecter le jeu de données au client API.

Vous êtes libre d'utiliser le jeu de données de votre choix. Plusieurs jeux [de données open source](https://www.ibm.com/fr-fr/think/topics/open-source?) sont disponibles sur des plateformes telles que HuggingFace.

```
train_filename = 'dog_grooming_reviews_train_data.json'

url = "https://raw.githubusercontent.com/AnnaGutowska/think/main/tutorials/prompt-tuning-tutorial/" + train_filename
wget.download(url)

asset_details = client.data_assets.create(name=train_filename, file_path=train_filename)
asset_id = client.data_assets.get_id(asset_details)
```

**Output**:

Creating data asset...

SUCCESS

```python
print(asset_id)
```

**Output**: 

3b1db894-8d9e-428d-8fee-d96f328c7726

Pour obtenir des informations sur le formatage des avis clients, chargez les données dans un dataframe Pandas et imprimez quelques lignes qui affichent à la fois des avis positifs et négatifs. Une sortie (output) de « 1 » indique un avis positif et « 0 » est utilisé pour un avis négatif.

```
pd.set_option('display.max_colwidth', None)
df = pd.read_json(train_filename)
df[5:10]
```

**Output**:

  Jeu de données d'entraînement

### Étape 5. Régler le modèle.

La classe TuneExperiment est utilisée pour créer des expériences et planifier les réglages. Nous l'utilisons pour initialiser notre expérience et définir notre modèle de fondation, nos données d’entraînement et nos paramètres de base. L'objectif de cet exercice de prompt est, pour le LLM, d'adapter ses réponses aux évaluations de satisfaction client extraites de notre jeu de données. Il s’agit d’une tâche de classification, car les avis peuvent être classés comme positifs (« 1 ») ou négatifs (« 0 »).

Pour ce tutoriel, nous vous suggérons d'utiliser un [modèle IBM Granite](https://www.ibm.com/fr-fr/granite) comme grand modèle de langage afin d’obtenir des résultats similaires.

```
experiment = TuneExperiment(credentials,
project_id=project_id
)

prompt_tuner = experiment.prompt_tuner(name="prompt tuning tutorial",
task_id=experiment.Tasks.CLASSIFICATION,
base_model="ibm/granite-3-8b-instruct",
accumulate_steps=16,
batch_size=8,
learning_rate=0.001,
max_input_tokens=128,
max_output_tokens=2,
num_epochs=12,
tuning_type=experiment.PromptTuningTypes.PT,
init_text="Extract the satisfaction from the comment. Return simple '1' for satisfied customer or '0' for unsatisfied. Comment:",
init_method="text",
verbalizer="classify {0, 1} {{input}}",
auto_update_model=True
)
```

Maintenant que notre expérience de réglage est configurée, nous devons la connecter à notre jeu de données. Pour cela, utilisons la classe DataConnection. Cela nécessite l'asset_id que nous avons produit plus tôt lors de l'initiation de l'actif de données avec notre client API.

```
data_conn = DataConnection(data_asset_id=asset_id)
```

Vous pouvez utiliser le modèle d’IA de votre choix. Vous trouverez les modèles de fondation disponibles pour le réglage avec watsonx [ici](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-tuning-model-choose.html?context=wx&audience=wdp) ou en exécutant la commande suivante.

```
client.foundation_models.PromptTunableModels.show()
```

**Output**:

{'FLAN_T5_XL': 'google/flan-t5-xl', 'GRANITE_13B_INSTRUCT_V2': 'ibm/granite-13b-instruct-v2', 'LLAMA_2_13B_CHAT': 'meta-llama/llama-2-13b-chat'}

```
tuning_details = prompt_tuner.run(
training_data_references=[data_conn],
background_mode=False)
```

**Output**:

\##############################################\
\
Running '20671f17-ff53-470b-9bfe-04318ecb91d9'\
\
\##############################################\
\
\
pending......\
running....................................................................................................................................\
completed\
Training of '20671f17-ff53-470b-9bfe-04318ecb91d9' finished successfully.

### Étape 6. Évaluer les résultats du réglage.

Pour vérifier que notre réglage par prompt est terminé, nous pouvons consulter son statut. Si le statut qui s'affiche est autre que « terminé », veuillez attendre la fin du réglage avant de continuer.

```python
status = prompt_tuner.get_run_status()
print(status)
```

**Output**: 

Terminé

Nous pouvons maintenant récupérer le résumé du réglage par prompt. Dans ce résumé, vous verrez une valeur de perte. Pour chaque exécution d’entraînement, la fonction de perte mesure la différence entre les résultats prédits et les résultats réels. Par conséquent, une valeur de perte plus faible est privilégiée.

```
prompt_tuner.summary()
```

Nous pouvons également tracer la courbe d’apprentissage du réglage de notre modèle à l’aide de la fonction plot_learning_curve(). Une courbe descendante qui se rapproche de zéro indique que le modèle améliore la génération de sorties attendue. Pour en savoir plus sur l’interprétation des graphiques de la fonction de perte, consultez la documentation IBM watsonx correspondante.

```
prompt_tuner.plot_learning_curve()
```

**Output**:

  Graphiques de la courbe d'apprentissage

### Étape 7. Déployer le modèle optimisé.

Cette étape de déploiement du modèle réglé est critique pour réaliser l’étape suivante de comparaison des performances du modèle réglé avec celle du modèle préréglé.

Remarque : SERVING_NAME est défini sur la date et l’heure en cours, car il doit être une valeur unique.

```
model_id = prompt_tuner.get_model_id()

meta_props = {
client.deployments.ConfigurationMetaNames.NAME: "PROMP TUNE DEPLOYMENT",
client.deployments.ConfigurationMetaNames.ONLINE: {},
client.deployments.ConfigurationMetaNames.SERVING_NAME : datetime.now().strftime('%Y_%m_%d_%H%M%S')
}

deployment_details = client.deployments.create(model_id, meta_props)
```

**Output**: 

\######################################################################################\
\
Synchronous deployment creation for id: '6aa5dd5c-0cc4-44e0-9730-18303e88e14a' started\
\
\######################################################################################\
\
\
initializing.......................\
ready\
\
-----------------------------------------------------------------------------------------------\
Successfully finished deployment creation, deployment_id='24a97b84-47d0-4490-9f5f-21ed2376fdd6'\
-----------------------------------------------------------------------------------------------

### Étape 8. Tester le modèle optimisé.

Testons maintenant les performances du modèle ajusté et du modèle de fondation original pour voir les effets de notre processus d'optimisation. Commençons par charger le jeu de données de test. Ce jeu de données doit être un sous-ensemble de données qui n’était pas présent lors du réglage. Souvent, l’ensemble de test est également plus petit que l’ensemble d’apprentissage. En outre, chaque entrée du jeu de données comporte le prompt comme préfixe du commentaire de l'utilisateur.

```
test_filename = 'dog_grooming_reviews_test_data.json'
url = "https://raw.githubusercontent.com/AnnaGutowska/think/main/tutorials/prompt-tuning-tutorial/" + test_filename
wget.download(url)
data = pd.read_json(test_filename)
```

Voyons une petite partie du jeu de données pour mieux comprendre sa structure.

```
data.head()
```

**Output**:

  Tester le jeu de données

Lors du chargement du jeu de données de test, extrayons les entrées et les sorties.

```
prompts = list(data.input)
satisfaction = list(data.output)
prompts_batch = ["\n".join([prompt]) for prompt in prompts]
```

Nous pouvons également imprimer un échantillon d’entrée et de sortie de test pour mieux comprendre comment nous avons extrait le contenu du jeu de données.

```
prompts[0]
```

**Output**:

'Extract the satisfaction from the comment. Return simple 1 for satisfied customer or 0 for unsatisfied.\nComment: Long wait times.\nSatisfaction:\n'

Dans cet exemple, le prompt est présenté, suivi de l’avis du client sur les longs temps d’attente, puis la valeur 0 indique un avis négatif.

```
satisfaction[0]
```

**Output**: 

0

Maintenant que nous avons le jeu de données de test, testons la précision et le score F1 de notre modèle ajusté. Le score F1 est la moyenne de la précision et du rappel du modèle. Nous aurons besoin du déploiement_id. Notez que la variable concurrency_limit est définie sur 2 pour éviter d’atteindre la limite de débit de l’API. Il s’agit du nombre de requêtes qui seront envoyées en parallèle.

```python
deployment_id = deployment_details['metadata']['id']

tuned_model = ModelInference(
deployment_id=deployment_id,
api_client=client
)

tuned_model_results = tuned_model.generate_text(prompt=prompts_batch, concurrency_limit=2)
print(f'accuracy_score: {accuracy_score(satisfaction, [int(float(x)) for x in tuned_model_results])}, f1_score: {f1_score(satisfaction, [int(float(x)) for x in tuned_model_results])}')
```

**Output**:

accuracy_score: 0.9827586206896551, f1_score: 0.9827586206896551

Compte tenu de la précision élevée de notre modèle et de son score F1, testons les performances du même modèle Granite sans aucun réglage.

```python
base_model = ModelInference(
model_id="ibm/granite-3-8b-instruct",
api_client=client
)

base_model_results = base_model.generate_text(prompt=prompts_batch, concurrency_limit=2)

print(f'base model accuracy_score: {accuracy_score(satisfaction, [int(x) for x in base_model_results])}, base model f1_score: {f1_score(satisfaction, [int(x) for x in base_model_results])}')
```

**Output**:

modèle de base accuracy_score : 0,9310344827586207, modèle de base f1_score : 0,9298245614035088

Notre modèle ajusté surpasse le modèle de fondation pré-entraîné. Le modèle ajusté étant spécialisé dans l’extraction de scores de satisfaction, il peut être utilisé pour d’autres tâches d’extraction de satisfaction. Excellent travail !

## Récapitulatif

Dans ce tutoriel, vous avez optimisé un prompt sur un modèle IBM Granite à l’aide de l’API watsonx. Votre modèle ajusté et déployé a réussi à surpasser le modèle de fondation avec une précision supérieure d’environ 5 %.
