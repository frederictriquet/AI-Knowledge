> Source : https://www.ibm.com/fr-fr/think/tutorials/prompt-chaining-langchain

# Chaînage de prompts avec LangChain : un aperçu complet

##

Le chaînage de prompts est un concept fondamental dans la création de workflows avancés à l'aide de grands modèles de langage (LLM). Il consiste à relier plusieurs prompts en une séquence logique, où la sortie d’un prompt sert d’entrée pour le suivant. Cette approche modulaire est puissante pour résoudre des tâches complexes telles que le traitement de texte en plusieurs étapes, le résumé, la réponse aux questions et plus encore.

**LangChain** est un framework polyvalent conçu pour simplifier la création de tels workflows. Il fournit des outils pour gérer des LLM tels que les [modèles IBM Granite](https://www.ibm.com/fr-fr/products/watsonx-ai/foundation-models) ou les modèles GPT (generative pre-trained transformer) d’OpenAI, définir des prompts personnalisés et les organiser en chaînes réutilisables. En abstrayant la complexité de la gestion des prompts, LangChain permet aux développeurs de se concentrer sur la résolution de problèmes plutôt que sur l'orchestration des interactions avec les LLM.

Dans ce tutoriel, nous allons :

1.  Découvrir différents types de chaînage de prompt (séquentiel, ramifié, itératif et autres).
2.  Implémenter un exemple de chaînage générique combinant des types de chaînage séquentiel, ramifié et itératif.
3.  Tirez parti des classes intégrées de LangChain telles que PromptTemplate, LLMChain et SequentialChain pour définir et gérer le workflow.

## Comment LangChain gère le chaînage de prompt

LangChain fournit un cadre puissant pour créer des workflows modulaires dans les applications de chatbot. En combinant des invites structurées, un chaînage dynamique et une intégration avancée des LLM, il permet aux développeurs de créer des pipelines évolutifs et adaptatifs qui exploitent les techniques RAG et produisent des sorties structurées comme JSON. Voici comment LangChain gère efficacement le chaînage de prompts :

**Abstraction des invites :** LangChain s’appuie sur from_template pour concevoir des workflows d’entrée/sortie structurés pour chaque étape, ce qui facilite la gestion d’opérations complexes de chatbot. 

**Intégration des LLM :** le framework s’intègre de manière fluide avec divers LLM, tels qu'IBM Granite, OpenAI et Hugging Face, permettant un ajustement fin pour des tâches personnalisées.

**Gestion de la chaîne :** SequentialChain et SimpleSequentialChain de LangChain permettent des workflows modulaires pour les pipelines de chatbot, tandis que stroutputparser garantit des sorties structurées comme JSON. 

**Workflows dynamiques :** grâce à des outils comme ConditionalChain et les modèles de message système, LangChain prend en charge des workflows adaptatifs, conformes aux principes de la génération augmentée par récupération (RAG) pour la génération dynamique de contenu.

  Figure - 1 : Schéma du chaînage de prompts à l'aide de LangChain

À la fin de ce tutoriel, vous aurez une solide compréhension de la façon d’utiliser LangChain pour créer des workflows modulaires et extensibles pour une large gamme d’applications.

## Types de chaînage de prompts

Le chaînage d'invites vous permet de concevoir des flux de travaux dans lesquels les sorties d'une étape sont transmises à la suivante. Différents types de chaînage prennent en charge différents workflows, allant de simples tâches séquentielles à des processus plus complexes et dynamiques. Voici un bref aperçu des types de chaînage de prompts :

- Chaînage séquentiel : le plus simple, où la sortie d’une invite est directement transmise en entrée à la suivante, idéal pour des tâches à progression linéaire. Cette option est idéale pour les tâches avec une progression linéaire.[\[1\]](#f01)

<!-- -->

- Chaînage de branches : une sortie unique est divisée en plusieurs workflows parallèles, chacun traitant la sortie indépendamment. Chaque branche traite la sortie indépendamment. [\[2\]](#f02)

<!-- -->

- Chaînage itératif : exécution répétée d’une invite ou d’une chaîne jusqu’à ce qu’une condition spécifiée soit remplie, utile pour affiner les résultats. Cette option sert à affiner les résultats.[\[3\]](#f03)

<!-- -->

- Chaînage hiérarchique : décompose une tâche volumineuse en sous-tâches plus petites exécutées hiérarchiquement, les sorties de niveau inférieur alimentant les tâches supérieures. Les sorties de niveau inférieur alimentent les tâches de niveau supérieur. [\[4\]](#f04)

<!-- -->

- Chaînage conditionnel : choisit dynamiquement l’étape suivante en fonction de la sortie précédente, permettant la prise de décision dans les workflows.

<!-- -->

- Chaînage multimodal : intègre des invites traitant différents types de données (texte, images, audio), adapté aux applications multimodales. Il convient aux applications combinant plusieurs modalités. [\[2\]](#f02)

<!-- -->

- Chaînage dynamique : adapte le workflow en fonction des sorties en temps réel ou de l’évolution des conditions, offrant une flexibilité accrue. Il ajoute de la flexibilité au chaînage de prompts. [\[5\]](#f05)

<!-- -->

- Chaînage récursif : divise de grandes entrées en blocs plus petits pour un traitement individuel avant de combiner les résultats, pratique pour les documents volumineux. Il est utile pour gérer des documents ou des ensembles de données volumineux. [\[6\]](#f06)

<!-- -->

- Chaînage inverse : part d’une sortie attendue et remonte pour déterminer les entrées ou étapes nécessaires, idéal pour la résolution de problèmes et le débogage. Il est idéal pour la résolution de problèmes et le débogage. [\[5\]](#f05)

Chaque type de chaînage répond à des cas d’utilisation spécifiques, il est donc essentiel de choisir celui qui convient en fonction de la complexité et des exigences de la tâche.

## Cas d'utilisation - traitement de texte en plusieurs étapes

Dans ce workflow, nous traitons les commentaires des clients à l’aide de modèles de chat et du prompt engineering pour créer un pipeline de traitement de texte évolutif. Les étapes suivantes du tutoriel illustrent les techniques de chaînage séquentiel, ramifié et itératif optimisées par l’IA générative.

**Extraction de mots-clés (chaînage séquentiel)**

- Le texte d’entrée ou l’entrée utilisateur en langage naturel est traité via un prompt pour identifier les mots-clés significatifs.
- Cette étape utilise le chaînage séquentiel afin de s’assurer que les mots-clés extraits alimentent directement les tâches suivantes.

**Génération d’un résumé des sentiments (chaînage ramifié)**

- Les mots-clés extraits sont transmis à un modèle de chat pour produire un résumé des sentiments.
- Le chaînage ramifié permet de suivre des chemins parallèles pour la synthèse, ce qui aide à adapter les sorties selon le contexte.

**Affinement du résumé des sentiments (chaînage itératif)**

- Si le résumé des sentiments ne satisfait pas les critères de qualité prédéfinis, il passe par un prompt de raffinement.
- Le chaînage itératif permet de retraiter la sortie jusqu’à atteindre le niveau de précision attendu.

**Sortie finale**

- Le résumé des sentiments affiné est fourni en tant que sortie finale, fournissant des informations sophistiquées à l’utilisateur.
- Cette approche illustre l’intégration du prompt engineering, de l’IA générative et des techniques de chaînage avancées.

Elle combine chaînage séquentiel, ramifié et itératif en Python, avec des modèles de chat et du prompt engineering. Cela garantit un traitement robuste des commentaires clients, en utilisant l’IA générative pour l’extraction de mots-clés, l’analyse des sentiments et leur affinement.

## Prérequis

Vous devez disposer d’un compte IBM Cloud pour créer un projet watsonx.ai .

## Étapes

#### Étape 1. Configurer votre environnement

Bien que vous puissiez faire votre choix parmi plusieurs outils, ce tutoriel vous guide pas à pas pour configurer un compte IBM à l’aide d’un Jupyter Notebook.

1.  Connectez-vous à watsonx.ai en utilisant votre compte IBM Cloud.
2.  Créez un projet watsonx.ai. Vous pouvez obtenir l’ID de votre projet à partir de ce dernier. Cliquez sur l’onglet **Manage** (Gérer). Ensuite, copiez l’ID du projet depuis la section **Details** (Détails) de la page **General** (Général). Vous aurez besoin de cet ID pour ce tutoriel.
3.  Créez un Jupyter Notebook.

Cette étape ouvre un environnement de notebook dans lequel vous pouvez copier le code de ce tutoriel. Vous pouvez également télécharger ce notebook sur votre système local et le charger dans votre projet watsonx.ai en tant qu’actif. Pour voir d'autres tutoriels Granite, consultez la Communauté IBM®  Granite. Ce tutoriel est également disponible sur GitHub.

#### Étape 2. Configurer le service d’exécution watsonx.ai et une clé API

1.  Créez une instance de service Runtime watsonx.ai (choisissez le plan Lite, qui est une instance gratuite).
2.  Générez une clé d’API.
3.  Associez le service Runtime watsonx.ai au projet que vous avez créé dans watsonx.ai.

#### Étape 3. Installer les packages

Nous avons besoin de bibliothèques pour travailler avec le framework LangChain et watsonxLLM. Commençons par installer les packages requis.

*Remarque : si vous utilisez une ancienne version de pip, vous pouvez exécuter la commande pip install --upgrade pip pour la mettre à jour. Cette étape vous permet d’installer facilement les paquets les plus récents, qui pourraient ne pas être compatibles avec une ancienne version. Mais si vous utilisez déjà la dernière version ou si vous avez récemment mis à jour vos packages, vous pouvez ignorer cette commande.*

```
!pip install --upgrade pip
%pip install langchain
!pip install langchain-ibm
```

#### Étape 4. Importer les bibliothèques requises

Ce bloc de code importe les bibliothèques et outils Python essentiels pour créer et gérer une application LLM à l’aide de LangChain et XXX Watson LLM. 

Le module **os** est utilisé pour accéder aux variables d’environnement, telles que les identifiants de projet ou les clés API.

**WatsonxLLM** est un module de langchain_ibm qui intègre IBM Watson LLM pour générer des résultats à partir de modèles d’IA générative.

**PromptTemplate** permet de créer des modèles réutilisables pour les prompts, garantissant ainsi la structure des entrées et la flexibilité dans le prompt engineering.

**LLMChain** crée des chaînes de tâches individuelles, tandis que

**SequencialChain** associe plusieurs étapes dans un seul workflow et getpass récupère en toute sécurité les informations sensibles (par exemple, les clés API) sans les exposer à l’écran.\

```python
import os
from langchain_ibm import WatsonxLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import getpass
```

#### Étape 5. Configurer les identifiants

Ce code configure les identifiants nécessaires pour accéder à l’*API IBM Watson Machine Learning (WML)* et garantit la configuration correcte de l’ID du projet (**PROJECT_ID**).

- Les **identifiants** d’un dictionnaire sont créés avec *l’URL et la clé API du service WML*. La clé API est collectée en toute sécurité à l’aide de **'getpass.getpass'** pour éviter d’exposer des informations sensibles.
- Le code tente d’extraire le **PROJECT_ID** à partir des variables d’environnement en utilisant la fonction **os.environ**. Si le **PROJECT_ID** n'est pas trouvé,l’utilisateur est invité à le saisir manuellement via un prompt.

```json
# Set up credentials
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

#### Étape 6. Initialiser un grand modèle de langage

Ce code initialise **IBM WatsonxLLM** pour une utilisation dans l’application :

1.  Ce code crée une instance de **watsonxLLM** à l’aide du **modèle ibm/granite-3-8b-instruct,** conçu pour les tâches d’IA générative basées sur des instructions.
2.  Les valeurs **url**, **apikey** et **projet_id** des identifiants précédemment configurés sont transmises pour l’authentification et la connexion au *service IBM Watson* LLM.
3.  Configure le paramètre **max_new_tokens** pour limiter le nombre de tokens générés par le modèle dans chaque réponse (150 tokens dans ce cas).

Cette étape prépare **WatsonxLLM** à générer des réponses dans le cadre du workflow.

```json
# Initialize the IBM LLM
llm = WatsonxLLM(
model_id="ibm/granite-3-8b-instruct",
url=credentials["url"],
apikey=credentials["apikey"],
project_id=project_id,
params={
"max_new_tokens": 150
}
)   
```

#### Étape 7. Définir des modèles de prompt

Ce code définit des modèles de prompt pour les trois étapes du workflow de traitement de texte :

1.  **Extraction de mots-clés :** *keyword_prompt* est conçu pour extraire les mots-clés les plus significatifs du texte fourni. Il utilise l'espace réservé *{text}* pour insérer l'entrée de manière dynamique.
2.  **Génération d'un résumé des sentiments :** s*entiment_prompt* prend les *{keywords}* extraits comme entrée et génère un résumé des sentiments des commentaires. Le modèle garantit que la génération de sentiments se concentre sur les mots clés fournis.
3.  **Affinement du résumé :** *refine_prompt* améliore le récapitulatif des sentiments en utilisant *{sentiment_summary}* comme entrée. L’objectif est de rendre la sortie concise et précise.

Ces instances de **PromptTemplate** permettent un prompt engineering réutilisable et structuré pour l’**application LLM**.

```
# Define Prompt Templates

# Prompt for extracting keywords
keyword_prompt = PromptTemplate(
input_variables=["text"],
template="Extract the most important keywords from the following text:\n{text}\n\nKeywords:"
)

# Prompt for generating sentiment summary
sentiment_prompt = PromptTemplate(
input_variables=["keywords"],
template="Using the following keywords, summarize the sentiment of the feedback:\nKeywords: {keywords}\n\nSentiment Summary:"
)

# Prompt for refining the summary
refine_prompt = PromptTemplate(
input_variables=["sentiment_summary"],
template="Refine the following sentiment summary to make it more concise and precise:\n{sentiment_summary}\n\nRefined Summary:"
)
```

#### Étape 8. Créer des chaînes

Ce code définit des chaînes LLM qui connectent les prompts au LLM IBM Watson initialisé, en attribuant des clés de sortie uniques pour chaque étape :

1.  **Chaîne de mots-clés :** *keyword_chain* utilise *keyword_prompt* pour extraire des mots-clés à partir du texte d’entrée. Le résultat est stocké sous la clé unique « keywords » pour être utilisé dans les étapes suivantes.
2.  **Chaîne de sentiments :** *sentiment_chain* prend les mots-clés extraits et génère un résumé de sentiment à l’aide de *sentiment_prompt*. La sortie est définie comme « sentiment_summary ».
3.  **Chaîne d’affinage :** *refine_chain* traite le résumé de sentiment généré à l’aide de *refine_prompt*. La sortie affinée finale est stockée avec la clé « refined_summary ».

Ces **instances LLMChain** permettent une exécution modulaire des tâches, facilitant un workflow d’application LLM étape par étape.

```
# Define Chains with Unique Keys

# Chain to extract keywords
keyword_chain = LLMChain(
llm=llm,
prompt=keyword_prompt,
output_key="keywords"  # Unique key for extracted keywords
)

# Chain to generate sentiment summary
sentiment_chain = LLMChain(
llm=llm,
prompt=sentiment_prompt,
output_key="sentiment_summary"  # Unique key for sentiment summary
)

# Chain to refine the sentiment summary
refine_chain = LLMChain(
llm=llm,
prompt=refine_prompt,
output_key="refined_summary"  # Final refined output
)
```

#### Étape 9. Combiner les chaînes

Ce code combine les chaînes précédemment définies en un workflow séquentiel, permettant un processus étape par étape pour l’entrée de texte. Le **SequentialChain** relie *keyword_chain*, *sentiment_chain* et *refine_chain* dans un ordre défini, en veillant à ce que la sortie d’une chaîne serve d’entrée pour la suivante. Le workflow est configuré pour accepter du texte comme entrée initiale, avec le résultat final — un résumé de sentiment affiné — stocké sous la clé **"refined_summary"**. Cette configuration permet une exécution rationalisée et efficace de l’application LLM, garantissant un pipeline de traitement cohérent et modulaire.

```
# Combine Chains into a Sequential Workflow

workflow = SequentialChain(
chains=[keyword_chain, sentiment_chain, refine_chain],
input_variables=["text"],  # Initial input for the workflow
output_variables=["refined_summary"]  # Final output of the workflow
)
```

#### Étape 10. Exécuter le workflow

Dans ce bloc de code, nous exécuterons l’intégralité du workflow. Tout d’abord, nous avons une chaîne de commentaires multilignes définie comme **feedback_text**, contenant à la fois des commentaires positifs et négatifs sur une application. La méthode **workflow.run** traite les commentaires à travers les chaînes séquentielles (extraction des mots-clés, analyse des sentiments et affinement) en utilisant l’entrée fournie. Le résumé des sentiments affiné est imprimé directement en tant que résultat final.

```python
# Example Input Text

feedback_text = """
I really enjoy the features of this app, but it crashes frequently, making it hard to use.
The customer support is helpful, but response times are slow.

I tried to reachout to the support team, but they never responded

For me, the customer support was very much helpful. Ihis is very helpful app. Thank you for grate services.
"""

# Run the Workflow

result = workflow.run({"text": feedback_text})

# Display the Output

print("Refined Sentiment Summary:")
print(result)  # Directly print the result since it is a string
```

**SORTIE**

Résumé affiné du sentiment :

Le sentiment de l'utilisateur est principalement négatif en raison des pannes récurrentes de l'application et de la lenteur des réponses du support client, malgré l'appréciation des fonctionnalités et l'utilité occasionnelle du support client. Pour améliorer la satisfaction des utilisateurs, l’équipe de développement doit se concentrer sur la résolution des pannes d’application et l’accélération des réponses du support client.

***Le résumé des sentiments est une évaluation concise et claire des commentaires. Elle met en évidence l’appréciation de l’utilisateur pour les fonctionnalités de l’application, mais exprime la frustration face aux pannes fréquentes et à la lenteur du support client, reflétant la capacité du flux de travail à extraire efficacement des informations critiques.***

## Choisir le type de chaînage approprié

La sélection du type de chaînage approprié pour l’application du LLM implique l’évaluation de facteurs clés pour garantir l’efficacité et la cohérence :

**Complexité des tâches :** utilisez des workflows exécutables pour les tâches comportant plusieurs étapes. Les exemples few-shot ou chatprompttemplate peuvent aider à structurer des tâches complexes nécessitant différents prompts.

**Dépendance :** si les sorties d’une étape sont utilisées comme entrées pour le prompt suivant, utilisez le chaînage séquentiel. Les analyseurs de sortie assurent une transition fluide des sorties vers des entrées structurées.

**Adaptabilité :** pour les workflows dynamiques, tels que ceux impliquant des agents LangChain, le chaînage itératif permet des ajustements en temps réel des paramètres et des prompts. 

**Modalité des données :** choisissez des workflows compatibles avec différents types de données. Utilisez des méthodes d'embedding pour les données textuelles et vectorielles ou le langage d'expression LangChain pour des opérations flexibles.

En tenant compte de ces facteurs, vous pouvez créer une application robuste et adaptable avec des workflows cohérents.

## Récapitulatif

Le chaînage de prompts est une technique polyvalente permettant de créer des workflows sophistiqués de traitement automatique du langage naturel (NLP). Dans ce tutoriel, nous avons découvert différents types de chaînage et présenté un exemple générique d’intégration de plusieurs approches de chaînage. En expérimentant ces méthodes, vous pouvez déverrouiller tout le potentiel des modèles de langage pour les applications du monde réel.
