> Source : https://www.ibm.com/fr-fr/think/topics/agentic-reasoning

# Qu’est-ce que le raisonnement agentique ?

Le raisonnement agentique est une composante des agents IA qui gère la prise de décision. Il permet aux agents d’intelligence artificielle d’effectuer des tâches de manière autonome en appliquant une logique conditionnelle ou heuristique, en s’appuyant sur la perception et la mémoire, ce qui leur permet de poursuivre des objectifs et d’optimiser les résultats.

Les premiers modèles de machine learning suivaient un ensemble de règles préprogrammées pour parvenir à une décision. Les progrès de l’IA ont conduit à des modèles IA dotés de capacités de raisonnement plus évoluées, mais ceux-ci nécessitent toujours une intervention humaine pour convertir les informations en connaissances. Le raisonnement agentique va encore plus loin en permettant aux agents IA de transformer les connaissances en actions.

Le « moteur de raisonnement » alimente les phases de planification et d’appel d’outils des workflows agentiques. La planification décompose une tâche en raisonnements plus faciles à gérer, tandis que l’appel d’outils aide à éclairer la décision d’un agent IA grâce aux outils disponibles. Ces outils peuvent inclure des interfaces de programmation des applications (API), des jeux de données externes et des sources de données telles que des graphes de connaissances.

Pour les entreprises, l’IA agentique peut ancrer davantage le processus de raisonnement dans des preuves grâce à la génération augmentée de récupération (RAG). Les systèmes RAG peuvent récupérer des données métier et d’autres informations pertinentes qui peuvent être ajoutées au contexte d’un agent IA pour alimenter son raisonnement.

## Stratégies de raisonnement agentique

Le raisonnement agentique peut être abordé de différentes manières en fonction de l’architecture et du type d’agent. Voici quelques techniques courantes pour le raisonnement des agents IA, ainsi que leurs avantages et inconvénients respectifs :

**    ● Logique conditionnelle**

**    ● Heuristique**

**    ● ReAct (raisonnement + action)**

**    ● ReWOO (raisonnement sans observation)**

**    ● Autoréflexion**

**    ● Raisonnement multi-agents**

### Logique conditionnelle

Les agents IA simples suivent un ensemble de règles condition-action préprogrammées. Ces règles prennent généralement la forme d’instructions « si-alors », où la partie « si » spécifie la condition et la partie « alors » indique l’action. Lorsqu’une condition est remplie, l’agent exécute l’action correspondante.

Cette méthodologie est particulièrement adaptée aux cas d’utilisation spécifiques à un domaine. Dans le domaine financier, par exemple, un agent de détection des fraudes signale une transaction comme frauduleuse selon un ensemble de critères définis par une banque.

Avec la logique conditionnelle, l’IA agentique ne peut pas agir en conséquence si elle se trouve confrontée à un scénario qu’elle ne reconnaît pas. Pour pallier ce manque de flexibilité, les agents basés sur des modèles ont recours à leur mémoire et à leur perception pour stocker un modèle ou un état actuel de leur environnement. Cet état est mis à jour à mesure que l’agent reçoit de nouvelles informations. Les agents basés sur des modèles restent toutefois soumis à leurs règles condition-action.

Prenons l’exemple d’un robot qui se déplace dans un entrepôt pour stocker un produit sur une étagère. Il consulte un modèle de l’entrepôt pour connaître l’itinéraire à suivre, mais il peut modifier son chemin pour éviter un obstacle et poursuivre son parcours.

### Heuristique

Les systèmes d’agents IA peuvent également recourir à l’heuristique pour raisonner. Les agents basés sur des objectifs, par exemple, ont un objectif prédéfini. À l’aide d’un algorithme de recherche, ils identifient les séquences d’actions qui peuvent les aider à atteindre leur objectif, puis planifient ces actions avant de les exécuter.

Par exemple, un véhicule autonome peut être équipé d’un agent de navigation dont l’objectif est de suggérer en temps réel l’itinéraire le plus rapide pour atteindre une destination. Il peut rechercher différents itinéraires et recommander le plus rapide.

À l’instar des agents basés sur des objectifs, les agents basés sur l’utilité recherchent des séquences d’actions qui permettent d’atteindre un objectif, mais ils tiennent également compte de l’utilité. Ils emploient une fonction d’utilité pour déterminer le résultat le plus optimal. Dans l’exemple de l’agent de navigation, il peut être chargé de trouver non seulement l’itinéraire le plus rapide, mais aussi celui qui consommera le moins de carburant.

### ReAct (raisonnement + action)

Ce paradigme de raisonnement implique une boucle « penser-agir-observer » pour la résolution étape par étape des problèmes et l’amélioration itérative des réponses. Un agent est chargé de générer des traces de son processus de raisonnement,1 tout comme dans le raisonnement en chaîne de pensées des modèles d’IA générative et des grands modèles de langage (LLM). Il agit ensuite sur ce raisonnement et observe son résultat,2 actualisant son contexte avec un nouveau raisonnement basé sur ses observations. L’agent répète le cycle jusqu’à ce qu’il arrive à une réponse ou à une solution.2

ReAct est performant pour les tâches spécifiques au langage naturel, et sa traçabilité améliore la transparence. Cependant, il peut également générer le même raisonnement et les mêmes actions à plusieurs reprises, ce qui peut entraîner des boucles infinies.2

### ReWOO (Raisonnement Sans Observation)

Contrairement à ReAct, ReWOO supprime l’étape d’observation et planifie à l’avance. Ce modèle de raisonnement agentique comprend trois modules : un module de planification, un module de travail et un module de résolution.3

Le module de planification décompose une tâche en sous-tâches et attribue chacune d’elles à un module de travail. Le module de travail intègre des outils pour étayer chaque sous-tâche avec des preuves et des faits. Enfin, le module de résolution synthétise toutes les sous-tâches et les preuves correspondantes afin de tirer une conclusion.3

ReWOO surpasse ReAct dans certains tests de référence en matière de traitement automatique du langage naturel (NLP). Cependant, l’ajout d’outils supplémentaires peut dégrader les performances de ReWOO, qui est peu performant dans des situations où il dispose d’un contexte limité sur son environnement.3

### Autoréflexion

L’IA agentique peut également inclure l’autoréflexion dans le cadre de l’évaluation et du perfectionnement de ses capacités de raisonnement. Langage Agent Tree Search (LATS) en est un exemple, partageant des similitudes avec le raisonnement par arbre de pensées dans les LLM.

LATS s’inspire de la méthode d’apprentissage par renforcement Monte Carlo, les chercheurs ayant adapté la recherche arborescente Monte Carlo pour les agents basés sur les LLM.4 LATS construit un arbre de décision qui représente un état sous forme de nœud et une action sous forme de branche, recherche dans l’arbre les options d’action possibles et fait appel à un évaluateur d’état pour choisir une action particulière.2 Il applique également une étape de raisonnement par autoréflexion, intégrant ses propres observations ainsi que les commentaires d’un modèle de langage afin d’identifier les erreurs de raisonnement et de recommander des alternatives.2 Les erreurs de raisonnement et les réflexions sont stockées en mémoire, servant de contexte supplémentaire pour les tâches ultérieures.4

LATS excelle dans des tâches plus complexes telles que le codage et la réponse interactive à des questions, ainsi que dans l’automatisation des [workflows](https://www.ibm.com/fr-fr/think/topics/ai-workflow), notamment la recherche et la navigation sur Internet.4 Cependant, une approche plus complexe et une étape supplémentaire d’autoréflexion rendent LATS plus gourmand en ressources et chronophage par rapport à des méthodes telles que ReAct.2

### Raisonnement multi-agents

Les systèmes multi-agents sont constitués de plusieurs agents IA qui collaborent pour résoudre des problèmes complexes. Chaque agent se spécialise dans un domaine particulier et peut appliquer sa propre stratégie de raisonnement agentique.

Toutefois, le processus décisionnel peut varier en fonction de l’architecture du système d’IA. Dans un écosystème hiérarchique ou vertical, un agent agit en tant que coordinateur de l’IA et décide des actions à entreprendre. Dans une architecture horizontale, les agents décident collectivement.

## Les défis du raisonnement agentique

Le raisonnement est au cœur des agents IA et peut se traduire par des capacités plus puissantes, mais il a également ses limites. Voici quelques défis liés au raisonnement agentique :

**    ● Complexité de calcul**

**    ● Interprétabilité**

**    ● Évolutivité**

### Complexité informatique

Le raisonnement agentique peut être difficile à mettre en œuvre. Le processus est également chronophage et nécessite une puissance de calcul importante, en particulier pour résoudre des problèmes complexes issus du monde réel. Les entreprises doivent trouver des moyens d’optimiser leurs stratégies de raisonnement agentique et être prêtes à investir dans les plateformes et les ressources d’IA nécessaires à leur développement.

### Interprétabilité

Le raisonnement agentique peut manquer d’explicabilité et de transparence quant à la manière dont les décisions ont été prises. Diverses méthodes peuvent aider à établir l’interprétabilité, et l’intégration de l’éthique de l’IA et de la supervision humaine dans le développement algorithmique est essentielle pour garantir que les moteurs de raisonnement agentique prennent des décisions équitables, éthiques et précises.

### Évolutivité

Les techniques de raisonnement agentique ne sont pas des solutions universelles, ce qui rend difficile leur adaptation à toutes les applications de l’IA. Les entreprises pourraient devoir adapter ces modèles de conception du raisonnement à chacun de leurs cas d’utilisation, une tâche longue et fastidieuse.

##### Notes de bas de page

*Tous les liens sont externes au site ibm.com*

1 ReAct: Synergizing Reasoning and Acting in Language Models, arXiv, 10 mars 2023

2 The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey, arXiv, 17 avril 2024

3 Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models, arXiv, 6 juin 2024

4 Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models, arXiv, 6 juin 2024
