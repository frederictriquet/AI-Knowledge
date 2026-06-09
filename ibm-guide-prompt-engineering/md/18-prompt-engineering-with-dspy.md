> Source : https://www.ibm.com/fr-fr/think/tutorials/prompt-engineering-with-dspy

# Prompt engineering avec DSPy

[DSPy](https://www.ibm.com/fr-fr/think/topics/dspy) est un cadre Python open source permettant de créer des applications [de grands modèles de langage](https://www.ibm.com/fr-fr/think/topics/large-language-models) (LLM) et d’affiner leur performance grâce au code, et non aux techniques ponctuelles d’optimisation des prompts. Le programme DSPy propose un moyen modulaire de configurer et d’affiner les applications LLM en optimisant les prompts pour obtenir des sorties précises. Le principal avantage de DSPy est qu’il vous permet d’effectuer vos tâches de [prompt engineering](https://www.ibm.com/fr-fr/think/topics/prompt-engineering) et de suivi grâce au code Python, sans avoir à suivre vous-même la performance du modèle.

La puissance de DSPy réside dans sa capacité à utiliser l’IA générative pour générer des textes en langage naturel, puis à tester les résultats pour créer des prompts efficaces. Cela vous permet de créer un système d’IA qui s’améliore automatiquement. Il prend en charge une grande variété d’interfaces pour les modèles de récupération et les modèles de langage. Vous pouvez exécuter les modèles localement, grâce à des systèmes comme ollama ou huggingface, ou les exécuter à l’aide d’une API si vous utilisez ChatGPT ou GPT-4 d’OpenAI. DSPy prend en charge une grande variété de cas d’utilisation tels que la [chaîne de pensée, ou chain of thought](https://www.ibm.com/fr-fr/think/topics/chain-of-thoughts) (CoT), la génération augmentée par récupération (RAG) et la synthèse. 

Dans ce tutoriel, vous allez suivre le workflow pour créer une application de réponse aux questions [RAG](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation) avec DSPy sur IBM watsonx. Vous utiliserez Llama 3 comme modèle de langage, et ColBERT comme modèle de récupération. Vous utiliserez DSPy pour affiner les prompts et structurer plusieurs approches de réponse aux questions, afin de découvrir comment obtenir de meilleures réponses, même à des questions très complexes.

## Configurer l’environnement

Bien que vous puissiez choisir parmi plusieurs outils, ce tutoriel vous explique comment créer un compte IBM pour utiliser Jupyter Notebook.

Connectez-vous à [watsonx.ai](https://dataplatform.cloud.ibm.com/registration/stepone?context=wx&apps=all) avec votre compte IBM Cloud.

Créez votre [projet watsonx.ai](https://dataplatform.cloud.ibm.com/registration/stepone?context=wx&apps=all).

Vous pouvez récupérer l’ID de votre projet à partir de ce dernier.

Cliquez ensuite sur l’onglet « Gérer » et copiez l’identifiant du projet à partir de la section « Détails » de la page « Général ». Vous avez besoin de cet identifiant lors de ce tutoriel.

Ensuite, créez un Jupyter Notebook dans l’environnement de votre choix. Vous allez copier le code de ce tutoriel dans le nouveau notebook. Vous pouvez également télécharger ce notebook à partir de GitHub vers votre système local, et le charger comme actif dans votre projet watsonx.ai.

## Configurer une instance de service Watson Machine Learning (WML) et une clé d’API

Créez une instance de service d’[exécution watsonx.ai](https://www.ibm.com/docs/en/watsonx/saas?topic=cloud-watsonxai-runtime-plans) (sélectionnez votre région et le [forfait Lite](https://www.ibm.com/docs/en/watsonx/saas?topic=runtime-watsonxai-plans), qui est une instance gratuite).

Générez une [clé d’API dans l’environnement d’exécution watsonx.ai.](https://www.ibm.com/docs/en/watsonxdata/standard/2.0.x?topic=started-generating-api-keys)

Associez le service d’exécution watsonx.ai au projet que vous avez créé dans [watsonx.ai](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/assoc-services.html).

## Installez la bibliothèque DSPy et configurez vos identifiants

Pour utiliser DSPy, vous effectuez une simple installation pip. Vous installerez également dotenv pour gérer les variables de votre environnement :

!pip install dspy-ai python-dotenv;

Ensuite, vous allez importer les bibliothèques nécessaires pour le reste de ce tutoriel :

```python
import dspy
from dspy import LM
from dspy.datasets import HotPotQA
from dspy.teleprompt import BootstrapFewShot
import json
import os

from dotenv import load_dotenv
load_dotenv(os.getcwd()+’/.env’, override=True)
```

Pour définir vos identifiants, vous avez besoin du WATSONX_APIKEY et du PROJECT_ID que vous avez générés à l’étape 1. Vous pouvez soit les stocker dans un fichier .env dans votre répertoire, ou remplacer le texte de l’espace réservé. Vous définissez également l’URL servant de point de terminaison de l’API.

```
os.environ[‘WX_URL’] = “https://us-south.ml.cloud.ibm.com”
os.environ[‘WX_APIKEY’] = os.getenv(“WATSONX_APIKEY”, “”)

WATSONX_APIKEY= os.getenv(“WATSONX_APIKEY”, “”)
PROJECT_ID = os.getenv(“PROJECT_ID”,””)
```

## Utiliser watsonx avec DSpy

Vous allez maintenant configurer DSPy pour qu’il fonctionne avec les modèles watsonx et la classe LM de DSPy. Cette classe vous permet d’appeler les API watsonx pour générer de nouveaux prompts, ainsi que des réponses à ces prompts, que vous pourrez tester. En dessous, DSPy utilise une autre bibliothèque, appelée [LiteLLM](https://docs.litellm.ai/docs/providers/watsonx), pour accéder aux services watsonx. LiteLLM fournit un wrapper simple pour appeler un large éventail d’API LLM en utilisant le format OpenAI, notamment Hugging Face, Azure et watsonx.

Afin de pouvoir accéder à votre compte watsonx, vous devez stocker un token à partir du service watsonx avec la clé d’API que vous avez générée lors de la première étape. Appelez la bibliothèque du système d’exploitation pour accéder à « https://iam.cloud.ibm.com/identity/token », récupérez votre token et stockez-le pour une utilisation ultérieure.

```
token = os.popen(‘curl -k -X POST \
--header “Content-Type: application/x-www-form-urlencoded” \
--header “Accept: application/json” \
--data-urlencode “grant_type=urn:ibm:params:oauth:grant-type:apikey” \
--data-urlencode “apikey=’ + WATSONX_APIKEY + ‘” \
“https://iam.cloud.ibm.com/identity/token”’).read()
```

Vous pouvez maintenant créer une instance LanguageModel qui utilise watsonx. Vous utiliserez le token que vous avez récupéré précédemment comme clé d’API, et le modèle « llama-3-8b-instruct » de Meta comme modèle de langage. Vous transmettrez le chemin d’accès à ce modèle à DSPy pour qu’il l’utilise comme modèle de langage, ainsi que la température souhaitée pour le modèle de langage. Pour découvrir comment configurer LiteLLM pour l’utiliser avec watsonx, consultez la [documentation GitHub.](https://docs.litellm.ai/docs/providers/watsonx) Dans ce cas, 0.7 vous offre une certaine créativité sans hallucination excessive.

```
lm = dspy.LM(‘watsonx/meta-llama/llama-3-8b-instruct’, api_key=WATSONX_APIKEY, api_base=”https://us-south.ml.cloud.ibm.com”)

dspy.configure(lm=lm, trace=[], temperature=0.7, experimental=True)
```

## Ajouter un modèle de récupération

Maintenant, vous chargez le modèle de récupération pour le R de votre RAG. Utilisez ColBERTv2 pour charger les extraits du jeu de données Wikipedia 2017. ColBERT est un modèle de récupération rapide et précis, qui permet une recherche BERT évolutive sur de grands corpus de textes en quelques dizaines de millisecondes. ColBERT n’est qu’une des nombreuses options disponibles pour récupérer des informations à partir d’une base de données vectorielle. Il est comparable à d’autres bases de données vectorielles telles que [Qdrant,](https://qdrant.tech/) [Milvus,](https://milvus.io/) [Pinecone,](https://www.pinecone.io/learn/retrieval-augmented-generation/) [Chroma](https://www.trychroma.com/) et [Weaviate.](https://weaviate.io/)

Les bases de données vectorielles contiennent des informations auxquelles le modèle de langage pourra rapidement accéder. Dans ce cas, vous allez utiliser un ensemble de résumés Wikipédia 2017 pour fournir un large éventail de faits que votre modèle de langage pourra utiliser à des fins de génération. Associer ColBERT au jeu de données Wiki 17 est particulièrement utile, puisque l’équipe DSPy en héberge une version gratuitement pour que tout le monde puisse l’utiliser. Cela vous permettra d’accéder à un large éventail d’informations sans avoir à ingérer les données, ni à configurer votre propre système de base de données vectorielle. L’un des inconvénients de ce jeu de données est qu'il ne contient rien sur les événements survenus après 2017. Pour notre démonstration, il est toutefois très utile.

Si vous souhaitez exécuter votre propre version de ColBERT avec vos propres données ou un jeu de données mis à jour, les tutoriels accessibles [ici](https://github.com/stanford-futuredata/ColBERT) vous seront utiles.

Ensuite, chargez le jeu de données HotPotQA et divisez-le en jeux d’entraînement et de test que vous pourrez utiliser pour tester votre chaîne de récupération. HotpotQA est un jeu de données question-réponse en langage naturel multi-sauts, avec une forte supervision des faits favorisant des systèmes question-réponse plus explicables. 

```
colbertv2_wiki17_abstracts = dspy.ColBERTv2(url=’http://20.102.90.50:2017/wiki17_abstracts’)
dspy.configure(rm=colbertv2_wiki17_abstracts)
```

## Test d’assurance qualité de base

Vous allez maintenant créer une signature qui sera utilisée pour votre exemple initial. Une signature est une classe qui définit les types d’entrée et de sortie d’un module, afin de garantir la compatibilité des différents modules du programme DSPy. Une signature combine plusieurs tâches, comme ingérer une question et produire une réponse et le raisonnement du modèle. La signature que vous utiliserez ici accepte une seule question et y répond :

```python
class BasicQA(dspy.Signature):
“””Answer questions with short factoid answers.”””

question = dspy.InputField()
answer = dspy.OutputField(desc=”often between 1 and 5 words”)
```

Vous disposez maintenant d’un prédicteur que vous pouvez tester simplement en appelant la méthode Predict de DSPy. Cette méthode utilisera la classe newBasicQA que vous avez définie précédemment lorsque vous transmettrez une question à DSPy.

```
# Define the predictor.
generate_answer = dspy.Predict(BasicQA)
```

Vous allez maintenant créer une question qui demande plusieurs éléments d’information pour y répondre correctement, et la tester avec une architecture qui utilise uniquement un modèle de langage. Pour répondre à la question, vous utiliserez la fonction generate_answer que vous venez de créer.

```python
# Call the predictor on a particular input.
test_question = “What country was the winner of the Nobel Prize in Literature in 2006 from and what was their name?”

pred = generate_answer(question=test_question)

if pred == None:
print(“ no answer “)
else:
# Print the input and the prediction.
print(f”Answer: Turkey, Orhan Pamuk”)
print(f”Predicted Answer: {pred.answer}”)
```

Le code renvoie ce qui suit (votre réponse peut être différente) :

```
Answer: Turkey, Orhan Pamuk
Predicted Answer: The winner was France and the author was Orhan Pamuk.
```

Orhan Pamuk a bien reçu le prix Nobel de littérature en 2006, mais il n’est pas originaire de France et la réponse n’est pas correcte. Vous allez maintenant enrichir le modèle à l’aide de la génération augmentée par récupération et demander à DSPy de concevoir de meilleurs prompts pour améliorer la performance.

## La génération augmentée de récupération (RAG)

La génération augmentée par récupération (RAG) est une architecture qui optimise les sorties d’un grand modèle de langage en utilisant les références d’une base de connaissances faisant autorité. Les données d’apprentissage sont ainsi complétées par des sources vérifiées avant que le modèle de langage ne génère une réponse. Les LLM sont entraînés sur de grands corpus et utilisent des milliards de paramètres pour générer une sortie, mais ils ne sont pas toujours en mesure d’accéder à des informations à jour ou précises à partir de leurs corpus d’entraînement. La RAG étend les capacités déjà puissantes des LLM à un domaine donné, sans qu’ils soit nécessaire d’entraîner à nouveau le modèle. Il s’agit d’un moyen puissant et potentiellement rentable d’améliorer les sorties des LLM, afin qu’ils restent pertinents, précis et utiles dans divers contextes.

Dans DSPy, vous utilisez une architecture RAG en ajoutant une étape de contexte dans la signature. Cette étape rassemble le contexte du modèle de récupération et l’ajoute au prompt du modèle de langage afin d’obtenir une meilleure réponse.

```python
class GenerateAnswer(dspy.Signature):
“””Answer questions with short factoid answers.”””

context = dspy.InputField(desc=”may contain relevant facts”)
question = dspy.InputField()
answer = dspy.OutputField(desc=”often between 1 and 5 words”)
```

Cette signature newGenerateAnswer peut être utilisée avec votre modèle RAG. Vous transmettez la GenerateAnswer au module « ChainOfThought » afin que le contexte récupéré ainsi que la question et la réponse utilisent une approche Chain of Thought.

Vous mettez également à jour la méthode forward afin de générer des passages contextuels à partir de la RAG et de les utiliser pour générer des réponses. DSPy appellera cette méthode « forward » chaque fois qu’il générera une réponse à une question, en recueillant le contexte du jeu de données ColBERT-Wiki 17 et en le transmettant au modèle de langage (dans ce cas, Llama 3.1). À mesure que chaque réponse est générée, DSPy compare la sortie à la sortie souhaitée pour s’assurer que les prompts aident le modèle à générer la bonne réponse.

```python
class RAG(dspy.Module):
def __init__(self, num_passages=3):
super().__init__()

self.retrieve = dspy.Retrieve(k=num_passages)
self.generate_answer = dspy.ChainOfThought(GenerateAnswer)

def forward(self, question):
context = self.retrieve(question).passages
prediction = self.generate_answer(context=context, question=question)
return dspy.Prediction(context=context, answer=prediction.answer)
```

Pour aider DSPy à concevoir les meilleurs prompts, vous avez besoin d’un jeu de données de test qu’il pourra utiliser pour tester les prompts, puis les évaluer.

Pour donner des questions de test à DSPy, vous chargerez le jeu de données HotPotQA. HotpotQA est un jeu de données question-réponse en langage naturel multi-sauts qui nécessite plusieurs récupérations et inférences pour arriver à la bonne réponse. Il s’agit d’un excellent outil pour tester la capacité des modèles à générer des faits justificatifs, afin d’entraîner et de tester des systèmes de type question-réponse plus explicables. 

Voici un exemple de question tiré du jeu de données : « Qui le président Franklin Roosevelt a-t-il nommé pour transmettre les votes du collège électoral au Congrès ? » Vous pouvez constater que cette question demande plusieurs éléments d’information pour y répondre correctement.

```
The answer is: “Robert Digges Wimberly Connor”.
```

Le contexte à l’appui provient des pages Wikipédia sur Robert Digges Wimberly Connor et sur la National Archives and Records Administration.

HotPotQA est recueilli et publié par une équipe de chercheurs en TAL de l’Université Carnegie Mellon, de l’Université de Stanford et de l’Université de Montréal. Plus d’informations sur HotPotQA sont disponibles sur leur [site GitHub.](https://hotpotqa.github.io/)

Après avoir chargé le jeu de données, divisez-le en ensembles d’entraînement et de test. Cela vous permet de tester la chaîne de récupération et d’aider DSPy à localiser les meilleurs prompts pour le modèle de langage.

```
# Load the dataset.
dataset = HotPotQA(train_seed=1, train_size=20, eval_seed=2023, dev_size=50, test_size=0)

# Tell DSPy that the ‘question’ field is the input. Any other fields are labels and/or metadata.
trainset = [x.with_inputs(‘question’) for x in dataset.train]
devset = [x.with_inputs(‘question’) for x in dataset.dev]
```

Ensuite, vous allez amorcer plus d’exemples pour permettre à DSPy de générer des prompts et de les évaluer. Callingcompile utilise toute l’architecture que vous avez configurée, ainsi que le jeu de données HotPotQA, pour générer et tester les prompts et obtenir la meilleure performance de votre modèle de langage.

```
 
```

```python
from dspy.teleprompt import BootstrapFewShot

# Validation logic: check that the predicted answer is correct.
# Also check that the retrieved context does actually contain that answer.
def validate_context_and_answer(example, pred, trace=None):
answer_EM = dspy.evaluate.answer_exact_match(example, pred)
answer_PM = dspy.evaluate.answer_passage_match(example, pred)
return answer_EM and answer_PM

# Set up a basic DSPy optimizer, which will compile your RAG program.
bfs_optimizer = BootstrapFewShot(metric=validate_context_and_answer)

# Compile!
compiled_rag = bfs_optimizer.compile(RAG(), trainset=trainset)
```

Maintenant que DSPy s’est chargé du prompt engineering, vous allez le tester avec la question personnalisée sur le prix Nobel 2006 que vous avez utilisée auparavant. Comme le modèle de recherche utilise des extraits de Wikipédia datant de 2017, il fonctionnera au mieux avec les connaissances susceptibles de figurer dans ce corpus :

```python
# Get the prediction. This contains `pred.context` and `pred.answer`.
pred = compiled_rag(test_question)

# Print the contexts and the answer.
print(f”Question: {test_question}”)
print(f”Predicted Answer: {pred.answer}”)
```

Vous avez maintenant la bonne réponse. 

```
    Question : De quel pays est originaire le lauréat du prix Nobel de littérature en 2006, et quel est son nom ?
    Réponse prédite : Turquie, Orhan Pamuk
```

Orhan Pamuk est originaire de Turquie, cette réponse est donc correcte. La version compilée de DSPy a non seulement trouvé la bonne réponse, mais l’a également formulée correctement : une réponse claire et concise. Examinons le contexte de cette réponse prédite pour voir comment le modèle est parvenu à la bonne réponse :

pred.context

Cela renvoie :

```
    [« Orhan Pamuk | Ferit Orhan Pamuk (connu sous le nom d’Orhan Pamuk, né le 7 juin 1952) est un romancier, scénariste et universitaire turc, lauréat du prix Nobel de littérature en 2006. L’un des romanciers les plus en vue de Turquie, son œuvre s’est vendue à plus de treize millions d’exemplaires dans soixante-trois langues, ce qui fait de lui l’écrivain le plus vendu du pays. »,
     « Prix Palanca 2006 | Les lauréats des Carlos Palanca Memorial Awards for Literature en 2006 (classement, titre de l’ouvrage récompensé, nom de l’auteur). »,
     « Miguel Donoso Pareja | Miguel Donoso Pareja (13 juillet 1931 — 16 mars 2015) était un écrivain équatorien qui a remporté le Premio Eugenio Espejo en 2006 (prix national de littérature décerné par le président de l’Équateur). »]
```

La réponse se trouve dans le premier élément de contexte renvoyé. Comme vous le voyez, DSPy a conçu des prompts optimaux en examinant l’historique du modèle de langage à l’aide de la méthode inspect_history() du modèle de langage.

```
lm.inspect_history()
```

Cet historique est très long, car il comprend tous les exemples du processus de compilation lors duquel DSPy a testé les prompts générés. La dernière partie de l’historique montre comment le modèle est parvenu à la bonne réponse et au bon format :

```
    [[ ## context ## ]]
    [1] « Orhan Pamuk | Ferit Orhan Pamuk (connu sous le nom d’Orhan Pamuk, né le 7 juin 1952) est un romancier, scénariste et universitaire turc, lauréat du prix Nobel de littérature en 2006. L’un des romanciers les plus en vue de Turquie, son œuvre s’est vendue à plus de treize millions d’exemplaires dans soixante-trois langues, ce qui fait de lui l’écrivain le plus vendu du pays. »
    [2] « Prix Palanca 2006 | Les lauréats des Carlos Palanca Memorial Awards for Literature en 2006 (classement, titre de l’ouvrage récompensé, nom de l’auteur). »
    [3] « Miguel Donoso Pareja | Miguel Donoso Pareja (13 juillet 1931 — 16 mars 2015) était un écrivain équatorien qui a remporté le Premio Eugenio Espejo en 2006 (prix national de littérature décerné par le président de l’Équateur). »]

    [[ ## question ## ]]
    De quel pays est originaire le lauréat du prix Nobel de littérature 2006, et quel est son nom ?

    Répondez avec les champs de sortie correspondants, en commençant par le champ `[[ ## reasoning ## ]]`, puis `[[ ## answer ## ]]`, puis en terminant par le marqueur pour `[[ ## completed ## ]]`.

    [31mResponse:[0m

    [32m[[ ## reasoning ## ]]
    Le texte mentionne le prix Nobel de littérature 2006 et précise qu’Orhan Pamuk, romancier turc, en est le lauréat.

    [[ ## answer ## ]]
    Turquie, Orhan Pamuk

    [[ ## completed ## ]][0m

```

Comme vous pouvez le constater, DSPy a utilisé le modèle pour générer le prompt :

Répondre avec les champs de sortie correspondants, en commençant par le champ `[[ ## reasoning ## ]]` , puis `[[ ## answer ## ]]` , puis en terminant par le marqueur pour `[[ ## completed ## ]]` .

Cela permet d’obtenir la réponse et le cadrage corrects.

## Résumé

Dans ce tutoriel, vous avez utilisé DSPy pour affiner un agent RAG à l’aide de la plateforme watsonx. Votre agent RAG se composait d’un modèle de langage, Llama 3, et d’un modèle de récupération, ColBERT. Vous avez ensuite utilisé DSPy à des fins de prompt engineering pour une tâche de réponse aux questions. Vous avez compilé votre modèle et fait générer un prompt optimisé.

Pour en savoir plus sur DSPy, consultez son [dépôt GitHub](https://github.com/stanfordnlp/dspy) qui regroupe tutoriels, démonstrations et documents.
