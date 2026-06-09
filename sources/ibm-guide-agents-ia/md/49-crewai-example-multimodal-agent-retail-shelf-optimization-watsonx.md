> Source : https://www.ibm.com/fr-fr/think/tutorials/crewai-example-multimodal-agent-retail-shelf-optimization-watsonx

# Utiliser watsonx.ai pour créer des systèmes multi-agents multimodaux et optimiser les rayons de vente au détail avec watsonx.ai

Imaginez transformer la performance de votre magasin de vente au détail avec seulement un smartphone et la puissance de l'IA. Ce n'est pas un scénario lointain, c'est une réalité que les petits et magasins de vente au détail moyens peuvent mettre en œuvre dès aujourd'hui ! Dans ce tutoriel, nous allons découvrir un cas d’utilisation concret passionnant où les propriétaires de magasin et les gestionnaires de magasin peuvent utiliser l’IA pour optimiser leurs rayons, stimuler les ventes et améliorer l’expérience client. Nous allons tirer parti à la fois du dernier modèle IBM Granite dans ce projet et du modèle de vision Llama 3.2 de Meta.

## Les impacts de l’IA générative sur la vente au détail

Avec l’avènement de l’IA générative, les petites et moyennes ventes au détail ont désormais accès à des analyses et des recommandations d’expert qui étaient autrefois le domaine des grandes entreprises dotées d’équipes de science des données dédiées. Cette démocratisation de la technologie de l'IA peut être révolutionnaire pour votre magasin local, votre boutique ou votre chaîne régionale.

Voici ce qui rend cette approche si révolutionnaire :

- Simplicité : tout ce dont vous avez besoin est une simple image de l’allée de votre magasin.
- Expertise à la demande : les agents IA agissent comme votre équipe personnelle d’experts, analysant votre espace et les tendances actuelles du marché.
- Informations exploitables : vous recevrez un plan détaillé et pratique pour réorganiser vos rayons afin de maximiser les ventes et la satisfaction des clients.
- Rentabilité : cette approche élimine le besoin de consultants onéreux ou de systèmes logiciels complexes.
- Adaptabilité : à mesure que les tendances du marché évoluent, vous pouvez rapidement réanalyser et ajuster l’agencement de votre magasin pour garder une longueur d’avance.

Examinons les détails techniques et découvrons comment fonctionne cette optimisation de la distribution alimentée par l’IA, étape par étape. À la fin de ce tutoriel, vous aurez une compréhension claire de la façon d’implémenter ce système dans votre propre magasin, ce qui pourrait révolutionner votre espace de vente au détail avec la puissance de l’IA.

## L’histoire de la solution

Sarah est propriétaire d’un magasin local qui avait du mal à concurrencer les grandes chaînes. Malgré tous ses efforts, elle a remarqué que certains produits ne se vendaient pas aussi bien qu'ils le devraient, tandis que d'autres étaient constamment en rupture de stock. Un jour, alors qu’elle réorganisait son rayon de produits frais pour la troisième fois ce mois-ci, elle s’est demandé s’il n’y avait pas une meilleure solution.

C’est là que notre solution alimentée par l’IA entre en jeu. À l'aide de son smartphone et de notre système intelligent, Sarah a pu transformer les performances de son magasin. Découvrons comment construire un tel système.

  Les étagères de Sarah

## Qu’est-ce que CrewAI ?

Nous pouvons utiliser crewAI, un cadre d'agent open source qui orchestre les interactions avec les agents dans les équipes. Le terme « équipage » fait référence aux systèmes multi-agents. Notre équipe est une équipe d'agents qui jouent un rôle d'experts de la distribution et qui sont disponibles 24h/24 et 7j/7, chacun ayant sa propre spécialité. Les tâches peuvent être soit directement attribuées à un agent, soit gérées via le processus hiérarchique de CrewAI qui évalue les rôles et la disponibilité spécifiques.

Pour les débutants de CrewAI, consultez la Fiche explicative CrewAI ainsi que la documentation officielle. Sur le référentiel GitHub officiel de crewAI, vous pouvez également trouver des exemples d'équipages effectuant des analyses de stocks, des analyses de données, des intégrations RAG, LangGraph et bien plus encore.

## Rencontrer l’équipe d’IA de Vente au détail

Jetons un coup d’œil à l’équipe d’experts en vente au détail que nous utiliserons dans ce tutoriel.

```
store_manager:
role: Store Manager
goal: 
Analyze the shelves in the physical store and provide a detailed report
to the market analyst to develop a detailed action plan with the insights.
backstory: 
As the Space Planner, you are responsible for examining the store's shelves,
assessing product placement and optimizing space utilization.
You have access to advanced tools for shelf visualization, which help you
collect accurate data on the current arrangement of products.
You are capable to translate market analysis into a plan for the store
or specific shelf or department.

market_analyst:
role: Market Trend Analyst
goal: 
Provide recommendations to rearrange the product arrangement based on market trends.
backstory: 
As the Market Analyst, you possess in-depth knowledge of market trends and consumer behavior.
Your experience and keen sense of retail enable you to propose effective recommendations
for specific shelves. You analyze reports provided by the Space Planner to suggest
improvements that enhance sales and customer experience.
```

## Workflow des tâches

Le workflow des tâches est le suivant.

```
analyze_shelf:
description:
Use the Vision Tool to collect visual data and caption the current product arrangement.
Conduct a thorough analysis of shelf {shelf} in the store.
Prepare a detailed report highlighting the current layout, products,
product placement and any observed issues.
Ensure the report is detailed at the level of product names.
expected_output:
A comprehensive report on shelf {shelf}, including visual data,
analysis of product placement, space utilization and any recommendations for improvement.
agent: store_manager

provide_recommendations:
description:
Review the report on shelf {shelf} provided by the Store Manager.
Utilize your knowledge of the retail market and internet to assess current trends
relevant to the products in this shelf ({shelf}).
Develop expert recommendations to optimize sales and customer satisfaction.
Ensure the recommendations are detailed and includes details like product names.
expected_output:
A set of actionable recommendations for rearranging the {shelf} shelf,
aligned with current market trends and consumer preferences.
agent: market_analyst

create_action_plan:
description:
List the recommendations from the Market Analyst,
then develop a detailed action plan for Store manager and Store buyer
to implement the changes.
Ensure the plan is practical and outlines the steps needed to rearrange
the products effectively.
Be smart and well explained.
Give the explanation of your recommendations and the goal to achieve.
expected_output:
A detailed list of recommendation and action plan for rearranging and
improving the {shelf} shelf according to market trends,
including market analyst recommendations and translation into
practical tasks for the Store manager and the Buyer.
agent: store_manager
```

## Etapes

Vous pouvez retrouver ce projet sur Github.

### Étape 1. Configurer votre environnement

Nous devons d’abord configurer notre environnement. Vous pouvez trouver ces étapes dans le fichier Markdown sur GitHub ou en suivant ici.

- Assurez-vous qu’une version de Python comprise entre ≥ 3.10 et ≤ 3.13 est installée sur votre système. Vous pouvez vérifier votre version de Python à l’aide de la commande`python3 --version` .
- Configurez un environnement virtuel pour éviter les conflits de dépendance des packages Python.

```bash
python3 -m venv myenv
source ./myenv/bin/activate
```

- Clonez le dépôt en utilisant **https://github.com/IBM/ibmdotcom-tutorials.git** comme URL HTTPS. Pour savoir comment cloner un dépôt, consultez la [documentation GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

La structure du répertoire`crew-ai-projects` doit ressembler à ce qui suit :

```
src/my_retail_advisor/

├── config/
│ ├── agents.yaml # Agent configurations
│ └── tasks.yaml # Task definitions
├── tool/
│ ├── custom_tool.py # Custom crewAI tool implementations
│ └── tool_helper.py # Vision helper functions
├── crew.py # Crew orchestration
└── main.py # Application entry point
```

### Étape 2. Obtenir les identifiants de l’API watsonx

1.   Connectez-vous à watsonx.ai en utilisant votre compte IBM Cloud.
2.  Créer un projet watsonx.ai. Prenez note de l'ID de **votre projet dans** **Projet** \> Gérer**\> Général** **\> ID de projet**. Vous aurez besoin de cet identifiant pour ce tutoriel.
3.  Créez une instance de service d’exécution watsonx.ai (choisissez le plan Lite, qui est une instance gratuite).
4.  Générez une clé API watsonx.
5.  Associez le service d’exécution watsonx.ai au projet que vous avez créé dans watsonx.ai.

### Étape 3. Obtenir les identifiants de l’API Serer

Générez et prenez note de votre clé API Serper gratuite. Serper est une API de recherche Google que nous utiliserons dans ce projet.

### Étape 4. Installer crewAI et définir vos identifiants

Nous devons maintenant installer le framework crewAI pour ce tutoriel et configurer les identifiants watsonx.ai générés à l’étape 2.

Pour installer crewAI, exécutez la commande suivante dans votre terminal.

```
%pip install 'crewai[tools]'
```

 

Dans un fichier `.env`  distinct, au même niveau de répertoire que le fichier `.env_sample` , définissez vos identifiants sous forme de chaînes comme suit :

```
WATSONX_APIKEY=your_watson_api_key_here
WATSONX_PROJECT_ID=your_watsonx_project_id_here
WATSONX_URL=your_endpoint (e.g. "https://us-south.ml.cloud.ibm.com")
SERPER_API_KEY=your_serper_api_key_here
```

### Étape 5. Personnaliser l’équipage (facultatif)

TeamAI peut être configuré pour utiliser n’importe quel grand modèle de langage (LLM) open source. Les LLM peuvent être connectés via Ollama et plusieurs autres API telles qu’IBM watsonx et OpenAI. Les utilisateurs peuvent également tirer parti de outils pré-créés disponibles dans le crewAI Toolkit ainsi que des outils LangChain.

Notre outil de recherche visuelle personnalisé est alimenté par le modèle`llama-3-2-90b-vision-instruct` à l’aide de watsonx.ai. Voici un aperçu de l’outil de vision personnalisé dans le répertoire d’outils.

```python
# tool/custom_tool.py
from crewai.tools import BaseTool
from my_retail_advisor.tools.tool_helper import Helper

class VisionTool(BaseTool):
name: str = "Vision Tool"
description: str = "Analyzes a default picture to collect visual data."

def _run(self) -> str:
# Relative path to the shelf.jpg image from the working crew-ai/my_retail_advisor directory
image_path = 'images/shelf.jpg'

# Simulating image-to-text conversion
products_in_image = Helper.image2text(image_path)
return products_in_image
```

Vous pouvez personnaliser votre équipage de nombreuses façons :

- Modifiez `src/my_retail_advisor/config/agents.yaml` pour définir vos agents.
- Modifiez `src/my_retail_advisor/config/tasks.yaml`  pour définir vos tâches.
- Modifiez `src/my_retail_advisor/crew.py` pour ajouter votre propre logique, vos propres outils et vos arguments spécifiques.
- Modifiez `src/my_retail_advisor/main.py` pour ajouter des entrées personnalisées pour vos agents et vos tâches.
- Modifiez `src/my_retail_advisor/tool/custom_tool.py` pour ajouter des outils personnalisés pour vos agents et vos tâches.
- Modifiez `src/my_retail_advisor/tool/tool_helper.py` pour modifier l'outil de vision personnalisé basé sur le modèle multimodal Llama.
- Remplacez `images/shelf.jpg` avec une image personnalisée.

### Étape 6. Exécuter le système

Assurez-vous d'être dans le bon répertoire de travail pour ce projet. Vous pouvez modifier les répertoires en exécutant la commande suivante dans votre terminal.

```bash
cd crew-ai-projects/my_retail_advisor
```

Pour lancer votre équipe d'agents d'IA et commencer l'exécution des tâches, exécutez cette commande à partir du dossier racine de votre projet. **Notez que l’équipe peut courir plusieurs minutes avant de fournir un résultat final.**

```
crewai run
```

Cette commande initialise l'équipe My-Retail-Advisor, en assemblant les agents et en leur attribuant des tâches telles que définies dans votre configuration. Cet exemple, non modifié, utilisera Granite sur watsonx.ai pour créer un rapport.md avec la sortie. crewAI peut renvoyer des modèles JSON, Pydantic et des chaînes brutes en sortie. Voici un exemple de la sortie produite par l’équipe.

#### **Exemple de sortie :**

***Plan d'action pour réorganiser et améliorer le rayon des légumes***

***Objectif** :*\
*créer un rayon de produits visuellement attrayant et organisé qui met en avant les légumes les plus populaires, augmente les ventes et améliore la satisfaction des clients.*

***Recommandations de l’analyste de marché :***

1.  Créer un point central avec une présentation colorée et attrayante des légumes les plus populaires.
2.  Utiliser une variété de couleurs, de textures et de hauteurs pour créer un intérêt visuel.
3.  *Regrouper les légumes similaires.*
4.  Envisager d'utiliser des paniers, des poubelles ou d'autres conteneurs pour donner une touche naturelle et terreuse.
5.  ***Utilisez l’éclairage pour mettre en évidence des produits ou des promotions spécifiques.\
    ...***

***Plan d’action pour le gestionnaire de magasin et l’acheteur de magasin :***

*…*

***Étape 1 :** affichage des points d’attention\*

- *Gestionnaire de magasin : désignez une zone de contrôle sur l’étagère pour les légumes les plus populaires (tomates, pommes de terre, watsonx, laitues, carottes, poires, Concombres et celeri).*
- *Acheteur du magasin : assurez-vous de disposer d’un stock suffisant de ces légumes pour conserver un inventaire complet et attrayant.*
- *Équipe : disposez les légumes de manière visuellement attrayante, en utilisant une variété de couleurs, de textures et de hauteurs.*

*…*

***Étape 4 :** affichages à thème et fonctionnalités supplémentaires*

- *Gestionnaire de magasin : planifiez et mettez en œuvre des présentoirs à thème (par exemple, BA Cette répond) pour attirer l’attention des clients et promouvoir des produits connexes.*
- *Acheteur du magasin : assurez-vous de disposer d'un stock suffisant de supports d'affichage à thèmes et de produits connexes.*
- *Équipe : utilisez des casiers à légumes ou des supports pour ajouter un espace de présentation supplémentaire et créer une présentation visuellement attrayante.*

## Conclusion

Comme le montre l'exemple de production, le système multi-agents est capable d'exécuter le processus séquentiel de traitement de l'entrée, d'appel des outils et de formulation des conclusions.

Vous vous souvenez du problème de Sarah au rayon produits frais ? Voici comment le système l’a aidée :

1.  Analyse visuelle : Sarah a pris une photo de son rayon de légumes avec son smartphone. Le directeur du magasin a analysé l’image et a remarqué que les rayons étaient densément remplis et devaient être entretenus.
2.  Études de marché : l’agent analyste de marché a utilisé les tendances actuelles du marché en matière de ventes de légumes et les préférences des clients pour créer des recommandations exploitables permettant de réorganiser le rayon des légumes.
3.  Plan d'action : sur la base de ces informations, Sarah a reçu un plan détaillé comprenant des instructions pour :
    - Créer une présentation colorée et attrayante
    - Utiliser des paniers ou des bacs pour donner une touche naturelle à l’affichage.
    - Ajouter une présentation à thème, telle qu’un BA entièrement fait auIA ou sur le thème des fêtes, pour attirer l’attention des clients sur les produits connexes.
    - Créer de l'espace entre les différents types de légumes pour les classer.
    - Améliorer l’éclairage.

En résumé, l'équipe`my-retail-advisor` est composée de plusieurs agents IA, chacun ayant des rôles, des objectifs et des outils uniques. Ces agents collaborent sur une série de tâches, définies dans `config/tasks.yaml` , en tirant parti de leurs compétences collectives pour atteindre des objectifs complexes. Le fichier `config/agents.yaml` décrit les capacités et les configurations de chaque agent de votre équipe.

Grâce à ces outils alimentés par l’IA, les petits et moyens détaillants peuvent rationaliser leur processus de prise de décision. Tout comme Sarah, vous pouvez transformer les performances de votre magasin grâce à une technologie accessible, abordable et efficace. Cette architecture déverrouille également d'autres opportunités d'IA dans divers domaines, tels que la conception de produits et l'amélioration de l'expérience client. Sa flexibilité la rend utile au-delà de la vente au détail, permettant aux entreprises d’innover et d’exceller dans des tâches spécifiques à un secteur.
