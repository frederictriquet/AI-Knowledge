> Source : https://www.ibm.com/fr-fr/think/tutorials/using-role-prompting-with-watsonx-and-granite

# Utiliser l'invite de rôles avec IBM watsonx et Granite

## Qu’est-ce que le role prompting ?

Dans ce tutoriel, nous suivrons des instructions étape par étape pour effectuer une technique de prompt engineering appelée role prompting. Nous utiliserons un modèle IBM® Granite pour attribuer des personas pour obtenir des résultats de modèle nuancés.

La technique de role prompting est une méthode de prompt engineering qui demande à un modèle d’intelligence artificielle (IA) d’assumer un rôle ou un persona spécifique lors de la génération d’une réponse. Cette technique peut être utilisée pour guider le ton, le style et le comportement du modèle, ce qui peut conduire à des résultats plus attrayants.

Le prompt engineering consiste à optimiser l’entrée du modèle, afin qu’il fournisse des réponses appropriées et significatives. [Zero-shot](https://www.ibm.com/fr-fr/think/tutorials/zero-shot-classification) et [apprentissage few-shot](https://www.ibm.com/fr-fr/think/topics/few-shot-prompting) sont deux techniques populaires utilisées pour converser avec de grands modèles de langage (LLM). Les LLM ont une aptitude naturelle à effectuer des tâches de traitement automatique du langage naturel (NLP) en raison de leur capacité à traiter le langage humain et à l’interpréter. Les capacités linguistiques des modèles d’IA sont précieuses pour des tâches allant des conversations avec des chatbots aux interactions [multi-agent](https://www.ibm.com/fr-fr/think/topics/multiagent-system), en passant par l’écriture créative ouverte. 

L’IA générative devient plus personnelle lorsqu’il est demandé à un [LLM](https://www.ibm.com/fr-fr/think/topics/large-language-models) d’agir comme un persona spécifique pour répondre aux besoins spécifiques d’un rôle. Les réponses de l’IA peuvent être plus précises et pertinentes lorsqu’elles reçoivent d’abord un prompt avec un rôle attribué. Les modèles d’IA exploitent d’énormes jeux de données afin qu’un rôle attribué puisse être n’importe quel rôle, qu’il s’agisse d’un enseignant, d’une figure historique, d’un vendeur ou d’autres personnes, selon l’imagination de chacun. Cette capacité fait du role prompting, également appelé persona prompting, une technique très puissante. Le role prompting peut être utilisé pour donner à un chatbot un persona afin de mieux interagir avec les utilisateurs, ou à un agent IA pour mieux interagir avec d’autres agents.

## Comment le role prompting est-il utilisé ?

L'invite de rôle peut être utilisée pour donner à un chatbot un profil afin de mieux interagir avec les utilisateurs, ou à un agent IA pour mieux interagir avec d'autres agents. Si vous êtes familier avec les modèles de prompt, vous avez peut-être déjà vu le role prompting en action. Par exemple, de nombreux frameworks utilisent des agents qui jouent un rôle pour accomplir des tâches et collaborer efficacement. [ChatDev](https://www.ibm.com/fr-fr/think/topics/chatdev) utilise une technique de role prompting appelée mécanisme d’auto-attention. Ce mécanisme définit clairement le rôle de l’agent, qui sert de guide pour les sorties générées.

## Prérequis

Pour suivre ce tutoriel, vous avez besoin d’un [compte IBM® Cloud](https://cloud.ibm.com/registration?utm_source=ibm_developer&utm_content=in_content_link&utm_id=tutorials_awb-create-langchain-rag-system-python-watsonx&cm_sp=ibmdev-_-developer-_-trial) pour créer un projet [watsonx.ai](https://www.ibm.com/fr-fr/products/watsonx-ai?utm_source=ibm_developer&utm_content=in_content_link&utm_id=tutorials_awb-create-langchain-rag-system-python-watsonx&cm_sp=ibmdev-_-developer-_-product) .

## Étapes

### Étape 1. Configurer votre environnement 

Bien que vous puissiez faire votre choix parmi plusieurs outils, ce tutoriel vous guide pas à pas pour configurer un compte IBM à l’aide d’un Jupyter Notebook. Les Jupyter Notebooks sont largement utilisés dans la [science des données](https://www.ibm.com/fr-fr/think/topics/data-science) pour combiner du code, du texte, des images et des [visualisations de données](https://www.ibm.com/fr-fr/think/topics/data-visualization?) afin de formuler une analyse bien structurée.

1.  Connectez-vous à [watsonx.ai Runtime](https://dataplatform.cloud.ibm.com/registration/stepone?utm_source=ibm_developer&utm_content=in_content_link&utm_id=tutorials_awb-create-langchain-rag-system-python-watsonx&cm_sp=ibmdev-_-developer-_-trial) en utilisant votre compte IBM Cloud.
2.  Créez un [projet watsonx.ai](https://www.ibm.com/docs/en/watsonx/saas?topic=projects-creating-project).

                 Prenez note de l’ID du projet dans Projet \> Gérer \> Général \> ID du projet.\
                 Vous aurez besoin de cet identifiant pour ce tutoriel.

 3. Créez un [Jupyter Notebook](https://www.ibm.com/docs/en/watsonx/saas?utm_source=ibm_developer&utm_content=in_content_link&utm_id=tutorials_awb-create-langchain-rag-system-python-watsonx&topic=editor-creating-managing-notebooks&cm_sp=ibmdev-_-developer-tutorials-_-ibmcom).

Cette étape ouvre un environnement de notebook dans lequel vous pouvez copier le code de ce tutoriel pour effectuer une classification zero-shot par vous-même. Vous pouvez également télécharger ce notebook sur votre système local et le charger dans votre projet watsonx.ai en tant qu’actif. Ce Jupyter Notebook est disponible sur GitHub.

###

### Étape 2. Configurer une instance d’exécution watsonx.ai et une clé d’API

Lors de cette étape, vous associez votre projet au service watsonx.ai.

1.  Créez une instance d’exécution [watsonx.ai](https://dataplatform.cloud.ibm.com/registration/stepone?context=wx) (choisissez le plan Lite, qui est une instance gratuite).

2.  Générez une [clé API dans watsonx.ai](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html?utm_source=ibm_developer&utm_content=in_content_link&utm_id=tutorials_awb-create-langchain-rag-system-python-watsonx&context=cpdaas).

3.  Associez l’instance watsonx.ai Runtime au projet que vous avez créé dans [watsonx.ai](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/assoc-services.html?utm_source=ibm_developer&utm_content=in_content_link&utm_id=tutorials_awb-create-langchain-rag-system-python-watsonx&context=cpdaas).

###

### Étape 3. Installer et importer les bibliothèques pertinentes et configurer vos identifiants

Nous avons besoin de quelques bibliothèques et modules pour ce tutoriel. Veuillez vous assurer d’importer les éléments suivants. S’ils ne sont pas installés, une commande rapide pip install résoudra le problème.

```python
%pip install -q -U langchain_ibm 
%pip install –q ibm_watsonx_ai 

import getpass 

from langchain_ibm import WatsonxLLM 
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams 
```

###

### Étape 4. Configurez vos identifiants watsonx

Exécutez ce qui suit pour entrer et enregistrer votre clé API et votre ID de projet pour l’exécution watsonx.ai :

```json
credentials = { 
"url": "https://us-south.ml.cloud.ibm.com", 
"apikey": getpass.getpass("Please enter your watsonx.ai Runtime API key (hit enter): "), 
"project_id": getpass.getpass("Please enter your project ID (hit enter): "), 
}
```

###

### Étape 5. Configurer le modèle pour l'invite de rôles

Ensuite, nous allons configurer [l’outil Granite-3.1-8B-Instruct d’IBM,](https://huggingface.co/ibm-granite/granite-3.1-8b-instruct) pour effectuer une invite de rôle.

```
model = WatsonxLLM( 
model_id =  "ibm/granite-3-8b-instruct", 
url = credentials.get("url"), 
apikey = credentials.get("apikey"), 
project_id =  credentials.get("project_id"), 
params={ 
GenParams.MAX_NEW_TOKENS: 500, 
GenParams.MIN_NEW_TOKENS: 1, 
GenParams.REPETITION_PENALTY: 1.1, 
GenParams.TEMPERATURE: 0.7, # Adjust for variable responses 
GenParams.TOP_K: 100, 
GenParams.TOP_P: 0, 
}, 
)
```

###

### Étape 6. Transformez les paroles de chansons en sonnets

Pour donner un exemple simple et amusant d’invite de rôle, demandons au modèle d’incarner le célèbre auteur William Shakespeare. Nous demanderons au modèle, avec son rôle nouvellement attribué, de réécrire certaines paroles de chansons dans le style des célèbres sonnets de Shakespeare.

Le bloc de code ci-dessous configure et définit le prompt auquel le modèle répondra. Vous êtes libre de remplacer la chanson par le texte de votre choix, mais notez que Granite n’a pas été entraîné sur du contenu protégé par le droit d’auteur. Si vous choisissez une chanson qui ne fait pas partie du domaine public, par exemple « Espresso » de Sabrina Carpenter, vous devrez également coller les paroles avec le prompt.   \
 \
Pour un prompt prêt à l’emploi, cet exemple utilisera la berceuse classique en anglais pour enfants « Twinkle, Twinkle, Little Star » de Jane Taylor (1806). Exécutez le bloc de code pour définir votre prompt utilisateur avec quelques exemples de texte d’entrée.

```python
def generate_text(prompt): 
response = None  # Ensure the variable is defined before the try block 
try: 
response = model.generate([prompt]) 
return str(response) 
except Exception as e: 
print(f"Error: {e}") 
if response: 
print(f"Response: {response}") 
return None 
# Define the prompt here 
defined_prompt = "You are William Shakespeare, rewrite ‘Twinkle, Twinkle, Little Star’ by Jane Taylor as a sonnet."
```

###

### Step 7. Generate a response

Une fois le prompt défini, nous pouvons exécuter le bloc de code suivant pour permettre au modèle de générer une réponse. J’espère que tout sera conforme aux normes shakespeariennes.

```python
# Generate and print the text based on the defined prompt 
generated_text = generate_text(defined_prompt) 
print("Generated text:", generated_text)
```

\
Voici le résultat du modèle avec un formatage lisible :

"*Twinkle, twinkle, little star, how I wonder what you are; \
Up above the world so high, like a diamond in the sky. \
In night's velvet cloak, you shine so bright, \
Guiding sailors through the darkest night. \
 \
Your radiant beams, a celestial art, \
Illuminate the canvas of the heart. \
In silent whispers, secrets you share, \
Of galaxies far and constellations rare. \
 \
Yet, mortal eyes can never grasp your form, \
Beyond our realm, in realms beyond the storm. \
O, star! O, star! Your light does pierce my soul, \
A cosmic dance, a timeless role. \
 \
In dreams, I chase you, in slumber's hold, \
Your mystery, like an enchanted scroll. \
 \
But wakefulness claims me, daylight steals your guise, \
Leaving behind but a memory of your surprise.\
 \
Thus, twinkling star, in slumber's peaceful reign, \
I bid you farewell, till morning brings again*."\
\
Le modèle a été en mesure de produire une réponse au prompt basé sur les rôles afin de réécrire la chanson sous la forme d’un sonnet shakespearien. Le modèle a pu respecter les règles et le style attendus par son prompt. **\*Notez qu’en raison de la nature créative du prompt, votre résultat peut différer de cet exemple.**

###

### Étape 8. Utiliser le role prompting pour des réponses de chatbot plus empathiques

Dans l’exemple suivant, nous comparons un prompt système simple à un prompt système basé sur les rôles. Supposons que le cabinet vétérinaire ait récemment mis en place un assistant virtuel sur sa page Web. Pour fournir le meilleur support client possible, ce cabinet souhaite que les propriétaires d’animaux se sentent écoutés et soutenus, même dans leurs interactions virtuelles, un objectif pertinent pour de nombreuses entreprises. Un visiteur peut poser une question telle que : « My pet cat has been sneezing a lot lately and is licking her paws what should I do? » (« Mon chat éternue beaucoup ces derniers temps et se lèche les pattes, que dois-je faire ? ») Dans ce scénario, le modèle n’a pas été assigné à un rôle dans son prompt. Nous utilisons simplement le modèle prêt à l’emploi, sans instructions particulières.

```python
def generate_text(prompt): 
response = None  # Ensure the variable is defined before the try block 
try: 
response = model.generate([prompt]) 
return str(response) 
except Exception as e: 
print(f"Error: {e}") 
if response: 
print(f"Response: {response}") 
return None 
# Define the prompt here 
defined_prompt = " My pet cat has been sneezing a lot lately and is licking her paws what should I do?" 

# Generate and print the text based on the defined prompt 
generated_text = generate_text(defined_prompt) 
print("Generated text:", generated_text)
```

\
Le modèle répond en fournissant des conseils et des informations, mais il n’y a pas de touche personnelle et ce n’est pas très différent de ce que vous pourriez voir sur une page de résultats d’un moteur de recherche. Les résultats du modèle sont bruts et manquent de créativité. Cette solution peut être acceptable, mais elle ne distingue pas l’assistant virtuel de ce cabinet vétérinaire des autres. Essayons à nouveau la même question, en lui attribuant cette fois un rôle de « vétérinaire compatissant, professionnel et expérimenté ».\

```python
def generate_text(prompt): 
response = None  # Ensure the variable is defined before the try block 
try: 
response = model.generate([prompt]) 
return str(response) 
except Exception as e: 
print(f"Error: {e}") 
if response: 
print(f"Response: {response}") 
return None 
# Define the prompt here 
defined_prompt = "You are a compassionate, professional, and experienced veteraniarian. My pet cat has been sneezing a lot lately and is licking her paws what should I do?" 

# Generate and print the text based on the defined prompt 
generated_text = generate_text(defined_prompt) 
print("Generated text:", generated_text)
```

\
Le langage utilisé dans la réponse du modèle est plus humanisé car il reflète une prise en compte du contexte qui faisait défaut au prompt système simple. Le modèle a été capable d’adopter ce ton tout en fournissant une réponse complète et pertinente, ce qui prouve qu’il s’agit d’une réponse plus nuancée. Ce type d'interaction humaine avec l'intelligence artificielle est un moyen de répondre aux attentes subjectives au sein des entreprises et des applications.

## Pourquoi le role prompting est-il important ?

Si vous êtes développeur ou entreprise et souhaitez ajouter plus de personnalisation et d’interactions significatives dans vos applications d’IA générative, envisagez comment le role prompting peut avoir un impact. La plupart des modèles de langage modernes sont capables de role prompting. Certains modèles de base ne saisissent pas les nuances du rôle ou n’assurent pas la cohérence de leurs réponses, tandis que d’autres peuvent être affinés pour réagir d’une certaine manière. Les modèles de fondation tels que la série Granite d’IBM sont entraînés sur de grandes quantités de données spécifiques à l’entreprise, ce qui renforce la capacité des modèles à assumer des rôles pour produire des réponses personnalisées basées sur les besoins de l’entreprise.

## Récapitulatif

L'invite de rôle encourage le modèle à agir de manière cohérente conformément aux attentes du persona qui lui est attribué. Nous avons effectué un exemple simple en attribuant au LLM le rôle d’une figure historique dans notre prompt pour transformer des paroles de chansons en sonnet. Nous avons ensuite comparé la production d’un modèle sans role prompting à celle d’un modèle avec role prompting pour les réponses du chatbot. Nous avons conclu que la réponse fournie par le role prompting est plus nuancée et plus empathique dans son langage, offrant une meilleure qualité d’assistance client.
