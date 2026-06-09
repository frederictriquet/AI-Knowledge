> Source : https://www.ibm.com/fr-fr/think/topics/ai-agent-planning

# Qu’est-ce que la planification par agent d’IA ?

La planification par agent d’IA désigne le processus par lequel un agent d’intelligence artificielle (IA) détermine une séquence d’actions pour atteindre un objectif donné. Elle implique la prise de décision, la hiérarchisation des objectifs et le séquençage des actions, souvent à l’aide de divers algorithmes et cadres de planification.

La planification par agent d’IA est un module commun à de nombreux types d’agents qui coexiste avec d’autres modules tels que la perception, le raisonnement, la prise de décision, l’action, la mémoire, la communication et l’apprentissage. La planification fonctionne en conjonction avec ces autres modules pour aider les agents à atteindre les résultats souhaités par leurs développeurs.

Tous les agents ne sont pas capables de planifier. Contrairement aux agents réactifs simples qui répondent immédiatement aux entrées, les agents de planification anticipent les états futurs et génèrent un plan d’action structuré avant l’exécution. La planification de l’IA est donc essentielle pour les tâches d’automatisation qui exigent une prise de décision, une optimisation et une adaptabilité en plusieurs étapes.

## Fonctionnement de la planification par agent d’IA

Les progrès réalisés dans le domaine des grands modèles de langage (LLM), tels que GPT d’OpenAI et les techniques associées impliquant des algorithmes de machine learning, ont entraîné l’essor de l’IA générative ces dernières années. De nouvelles avancées ont ensuite donné naissance au domaine émergent des agents autonomes.\
\
En intégrant des outils, des API, des interfaces matérielles et d’autres ressources externes, les systèmes d’IA agentique deviennent de plus en plus autonomes, capables de prendre des décisions en temps réel et habiles à résoudre des problèmes dans divers cas d’utilisation.

Les agents complexes ne peuvent pas agir sans prendre de décision, et ils ne peuvent pas prendre de bonnes décisions sans établir au préalable un plan. La planification agentique comprend plusieurs éléments clés qui interagissent pour favoriser une prise de décision optimale.

### Définition des objectifs

La première étape et la plus critique de la planification de l’IA consiste à définir un objectif clair. L’objectif sert de principe directeur à la prise de décision de l’agent, déterminant l’état final qu’il cherche à atteindre. Les objectifs peuvent être statiques, restant les mêmes tout au long du processus de planification, ou dynamiques, s’ajustant en fonction des conditions environnementales ou des interactions des utilisateurs.\
\
Ainsi, un véhicule autonome peut avoir pour objectif d’atteindre une destination précise de manière efficace tout en respectant les règles de sécurité. Sans un objectif bien défini, un agent manquerait de direction, ce qui entraînerait un comportement erratique ou inefficace.

Si l’objectif est complexe, les modèles d’IA agentique le décomposent en sous-objectifs plus petits et plus faciles à gérer lors d’un processus appelé décomposition des tâches. Cela permet au système de se concentrer sur des tâches complexes de manière hiérarchique.\
\
Les LLM jouent un rôle essentiel dans la décomposition des tâches, en divisant un objectif général en sous-tâches plus petites, puis en exécutant ces sous-tâches en plusieurs étapes. Par exemple, un utilisateur peut demander à un chatbot de planifier un voyage à l’aide d’un prompt en langage naturel.\
\
L’agent décomposera d’abord la tâche en plusieurs éléments, tels que la réservation des vols, la recherche d’hôtels et la planification d’un itinéraire. Une fois la tâche décomposée, l’agent utilisera des interfaces de programmation des applications (API) pour récupérer des données en temps réel, consulter les prix et même suggérer des destinations.

### Représentation de l’état

Pour une planification efficace, un agent doit acquérir une compréhension structurée de son environnement. Cette compréhension est obtenue grâce à la représentation de l’état, qui modélise les conditions actuelles, les contraintes et les facteurs contextuels qui influencent la prise de décision.\
\
Les agents disposent de certaines connaissances intégrées provenant de leurs données d’entraînement ou de leurs ensembles de données représentant des interactions précédentes, mais ils ont besoin de perception pour avoir une compréhension en temps réel de leur environnement. Les agents collectent des données via des entrées sensorielles, ce qui leur permet de modéliser leur environnement, ainsi que les entrées des utilisateurs et les données décrivant leur propre état interne.

La complexité de la représentation de l’état varie en fonction de la tâche. Par exemple, dans une partie d’échecs, l’état comprend la position de toutes les pièces sur l’échiquier, tandis que dans un système de navigation robotique, l’état peut inclure les coordonnées spatiales, les obstacles et les conditions du terrain.\
\
La précision de la représentation de l’état a un impact direct sur la capacité d’un agent à prendre des décisions éclairées, car elle détermine dans quelle mesure l’agent peut prédire les résultats de ses actions.

### Séquençage des actions

Une fois que l’agent a établi son objectif et évalué son environnement, il doit déterminer une séquence d’actions qui le fera passer de son état actuel à l’état souhaité. Ce processus, connu sous le nom de séquençage des actions, consiste à structurer un ensemble logique et efficace d’étapes que l’agent doit suivre.\
\
Celui-ci doit identifier les actions potentielles, réduire cette liste aux actions optimales, les classer par ordre de priorité et identifier les dépendances entre les actions et les étapes conditionnelles en fonction des changements potentiels de l’environnement. L’agent peut allouer des ressources à chaque étape de la séquence ou planifier des actions en fonction des contraintes environnementales.

Par exemple, un robot aspirateur doit définir le parcours le plus efficace pour nettoyer une pièce, en s’assurant de couvrir toutes les zones nécessaires sans répétitions inutiles. Si la séquence d’actions n’est pas bien planifiée, l’agent d’IA peut effectuer des étapes inefficaces ou redondantes, ce qui entraîne un gaspillage de ressources et une augmentation du temps d’exécution.

Le framework ReAct est une méthodologie utilisée dans l’IA pour gérer la prise de décision. Dans ce framework, le raisonnement fait référence au processus cognitif par lequel l’agent détermine quelles actions ou stratégies sont nécessaires pour atteindre un objectif spécifique.\
\
Cette phase est similaire à la phase de planification dans l’IA agentique, où l’agent génère une séquence d’étapes pour résoudre un problème ou accomplir une tâche. D’autres cadres émergents incluent ReWOO, RAISE et Reflexion, chacun ayant ses propres avantages et inconvénients.

### Optimisation et évaluation

La planification de l’IA implique souvent de sélectionner le chemin le plus optimal pour atteindre un objectif, en particulier lorsque plusieurs options sont disponibles. L’optimisation permet de s’assurer que la séquence d’actions choisie par un agent est la plus efficace, la plus rentable ou la plus avantageuse compte tenu des circonstances. Ce processus nécessite souvent d’évaluer différents facteurs tels que le temps, la consommation de ressources, les risques et les avantages potentiels.\
\
Par exemple, un robot d’entrepôt chargé de récupérer des articles doit déterminer l’itinéraire le plus court et le plus sûr pour éviter les collisions et réduire le temps d’opération. Sans une optimisation adéquate, les agents d’IA pourraient exécuter des plans fonctionnels mais sous-optimaux, ce qui entraînerait des inefficacités. Plusieurs méthodes peuvent être utilisées pour optimiser la prise de décision :

#### Recherche heuristique

Les algorithmes de recherche heuristique aident les agents à trouver des solutions optimales en estimant la meilleure voie à suivre pour atteindre un objectif. Ces algorithmes s’appuient sur des fonctions heuristiques, c’est-à-dire des estimations mathématiques de la proximité d’un état donné par rapport à l’objectif souhaité. Les recherches heuristiques sont particulièrement efficaces dans les environnements structurés où les agents doivent trouver rapidement des chemins optimaux.

#### Apprentissage par renforcement

L’apprentissage par renforcement permet aux agents d’optimiser leur planification par essais et erreurs, en identifiant les séquences d’actions qui conduisent aux meilleurs résultats au fil du temps. Un agent interagit avec un environnement, reçoit un retour d’information sous forme de récompense ou de sanction, et affine ses stratégies en conséquence.

#### Planification probabiliste

Dans des scénarios concrets, les agents d’IA opèrent souvent dans des environnements incertains où les résultats ne sont pas déterministes. Les méthodes de planification probabiliste tiennent compte de l’incertitude en évaluant plusieurs résultats possibles et en sélectionnant les actions présentant l’utilité attendue la plus élevée.

### Collaboration

La planification mono-agent est une chose, mais dans un système multi-agents, les agents d’IA doivent travailler de manière autonome tout en interagissant entre eux pour atteindre des objectifs individuels ou collectifs.\
\
Dans un système multi-agents, le processus de planification des agents d’IA est plus complexe que dans un système mono-agent, car ils doivent non seulement planifier leurs propres actions, mais également tenir compte des actions des autres agents et de la manière dont leurs décisions interagissent avec celles des autres.

En fonction de l’architecture agentique, chaque agent dans le système a généralement ses propres objectifs, qui peuvent impliquer l’accomplissement de tâches spécifiques ou l’optimisation d’une fonction de récompense. Dans de nombreux systèmes multi-agents, les agents doivent travailler ensemble pour atteindre des objectifs partagés.\
\
Ceux-ci peuvent être définis par un système global ou émerger des interactions entre les agents. Les agents ont besoin de mécanismes pour communiquer et harmoniser leurs objectifs, en particulier dans les scénarios coopératifs. Cela peut se faire par le biais de messages explicites, de définitions de tâches partagées ou d’une coordination implicite.

La planification dans les systèmes multi-agents peut être centralisée, où une seule entité ou un seul contrôleur, généralement un agent LLM, génère le plan pour l’ensemble du système.\
\
Chaque agent reçoit des instructions ou des plans de cette autorité centrale. Elle peut également être décentralisée, les agents générant leurs propres plans mais travaillant en collaboration pour s’assurer qu’ils se coordonnent entre eux et contribuent aux objectifs globaux, ce qui nécessite souvent une communication et une négociation.\
\
Ce processus décisionnel collaboratif améliore l’efficacité, réduit les biais dans l’exécution des tâches, aide à éviter les hallucinations grâce à la validation croisée et à la recherche d’un consensus, et encourage les agents à travailler vers un objectif commun.

## Après la planification

Les phases des workflows d’IA agentique ne se déroulent pas toujours de manière linéaire étape par étape. Si ces phases sont souvent distinctes dans leur conceptualisation, elles sont fréquemment interdépendantes ou itératives dans la pratique, en fonction de la nature de la tâche et de la complexité de l’environnement dans lequel l’agent évolue.

Les solutions d’IA peuvent différer selon leur conception, mais dans un workflow agentique classique, la phase suivante après la planification est l’exécution d’actions, où l’agent effectue les actions définies dans le plan. Cela implique l’exécution de tâches et l’interaction avec des systèmes ou des bases de connaissances externes grâce à la génération augmentée par récupération (RAG), à l’utilisation d’outils et à l’appel de fonction (appel d’outil).\
\
La création d’agents d’IA dotés de ces capacités peut nécessiter le recours à LangChain. Les scripts Python, les structures de données JSON et d’autres outils de programmation améliorent la capacité de l’IA à prendre des décisions.

Après avoir exécuté leurs plans, certains agents peuvent se servir de leur mémoire pour tirer des enseignements de leurs expériences et adapter leur comportement en conséquence.

Dans des environnements dynamiques, le processus de planification doit être adaptatif. Les agents reçoivent en permanence des informations sur l’environnement et les actions des autres agents et doivent ajuster leurs plans en conséquence. Cela peut passer par la révision des objectifs, l’adaptation des séquences d’actions ou la prise en compte de nouveaux agents entrant ou sortant du système.

Lorsqu’un agent détecte que son plan actuel n’est plus viable (par exemple, en raison d’un conflit avec un autre agent ou d’un changement dans l’environnement), il peut procéder à une nouvelle planification pour ajuster sa stratégie. Les agents peuvent ajuster leurs stratégies à l’aide du raisonnement par chaîne de pensée, un processus dans lequel ils réfléchissent aux étapes nécessaires pour atteindre leur objectif avant d’agir.
