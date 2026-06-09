> Source : https://www.ibm.com/fr-fr/think/topics/agentic-ai

# Qu’est-ce que l’IA agentique ?

L’IA agentique est un système d’[intelligence artificielle](https://www.ibm.com/fr-fr/think/artificial-intelligence) capable d’atteindre un objectif précis avec une supervision limitée. Il se compose d’agents IA, de modèles de machine learning capables d’imiter la prise de décision humaine pour résoudre des problèmes en temps réel. Dans un système multi-agent, chaque agent exécute une tâche spécifique et leurs actions sont coordonnées grâce à l’[orchestration de l’IA](https://www.ibm.com/fr-fr/think/topics/ai-orchestration).

Contrairement aux modèles IA traditionnels, qui fonctionnent selon des contraintes prédéfinies et nécessitent une intervention humaine, l’IA agentique fait preuve d’autonomie, d’un comportement orienté objectif et d’adaptabilité. Le terme « agentique » fait référence à l’agentivité (pouvoir d’action) de ces modèles, c’est-à-dire à leur capacité à agir de manière indépendante et ciblée.

L’IA agentique s’appuie sur les techniques d’IA générative en utilisant de grands modèles de langage pour fonctionner dans des environnements dynamiques.

Alors que les modèles génératifs *créent* du contenu à partir de schémas appris, l’IA agentique étend cette capacité en appliquant les résultats génératifs à des objectifs spécifiques. Un modèle d’IA générative comme ChatGPT d’OpenAI peut produire du texte, des images ou du code, mais un système d’IA agentique peut utiliser ce contenu généré pour effectuer des tâches complexes de manière autonome, en faisant appel à des outils externes.

Les agents peuvent, par exemple, non seulement vous indiquer le meilleur moment pour gravir le mont Everest en fonction de votre emploi du temps, mais il peut également réserver votre vol et votre hôtel.

## Quels sont les avantages de l’IA agentique ?

1.  Autonomes
2.  Proactifs
3.  Spécialisés
4.  Adaptables
5.  Intuitifs

Les systèmes agentiques présentent de nombreux avantages par rapport à leurs prédécesseurs génératifs, qui sont limités par les informations contenues dans les jeux de données sur lesquels les modèles sont entraînés.

### Autonomes

L’avancée la plus importante des systèmes agentiques, c’est l’autonomie dont ils peuvent faire preuve pour effectuer des tâches sans supervision humaine constante. Les systèmes agentiques peuvent s’attaquer à des objectifs à long terme, gérer des tâches de résolution de problèmes à plusieurs étapes et en suivre les progrès au fil du temps.

### Proactifs

Les systèmes agentiques allient la flexibilité des LLM, qui peuvent générer des réponses ou des actions basées sur une compréhension nuancée et dépendante du contexte, aux fonctionnalités structurées, déterministes et fiables de la programmation traditionnelle. Cette approche permet aux agents « de penser » et « d’agir » davantage comme des humains.

Les LLM ne peuvent pas interagir directement avec des outils ou des bases de données externes, ni configurer des systèmes pour surveiller et collecter des données en temps réel, mais les agents le peuvent.

Les agents peuvent effectuer des recherches sur le Web, appeler des interfaces de programmation d’applications (API) et interroger des bases de données, puis utiliser ces informations pour prendre des décisions et appliquer des mesures.

### Spécialisés

Les agents peuvent se spécialiser dans des tâches spécifiques. Certains agents simples sont faits pour exécuter une seule tâche répétitive de manière fiable. D’autres peuvent utiliser des capacités de perception et de mémoire pour résoudre des problèmes plus complexes.

Une architecture agentique pourrait être constituée d’un modèle de « conducteur » alimenté par un LLM supervisant les tâches et les décisions et encadrant d’autres agents plus simples. De telles architectures sont idéales pour les workflows séquentiels, mais elles sont sujettes à des goulots d’étranglement.

D’autres architectures sont plus horizontales, avec des agents travaillant de concert de manière décentralisée, mais elles peuvent être plus lentes qu’avec une hiérarchie verticale. Des applications d’IA différentes exigent des architectures différentes.

### Adaptables

Les agents peuvent apprendre de leurs expériences, tenir compte des commentaires et ajuster leur comportement en conséquence. Avec les bons garde-fous, les systèmes agentiques peuvent s’améliorer en continu. Les systèmes multiagents sont dotés des capacités d’évolutivité nécessaires pour parvenir à terme à gérer des initiatives de grande ampleur.

### Intuitifs

Les systèmes agentiques étant alimentés par des LLM, les utilisateurs peuvent interagir avec eux avec des prompts en langage naturel. En d’autres termes, des interfaces logicielles entières (l’ensemble des onglets, listes déroulantes, tableaux, curseurs, fenêtres contextuelles et autres éléments d’interface utilisateur de votre plateforme SaaS) peuvent être remplacées par de simples commandes écrites ou vocales en langage naturel.

Théoriquement, toute expérience des utilisateurs avec un logiciel peut désormais être réduite à « parler » avec un agent, qui peut récupérer les informations nécessaires et prendre des mesures en conséquence.

Cet avantage en termes de productivité n’est vraiment pas négligeable, si l’on considère le temps qu’il faut aux travailleurs pour apprendre et maîtriser de nouvelles interfaces et de nouveaux outils.

## Comment fonctionne l’IA agentique ?

Les outils d’IA agentique peuvent prendre de nombreuses formes, et différents  problèmes appellent l’utilisation de différents cadres, mais voici les étapes généralement suivies par les systèmes agentiques pour exécuter leurs opérations.

### Perception

L’IA agentique commence par collecter des données de son environnement par le biais de capteurs, d’API, de bases de données ou d’interactions avec l’utilisateur. Cette étape permet de s’assurer que le système dispose d’informations actualisées qu’il peut analyser et exploiter.

### Raisonnement

Une fois les données collectées, l’IA les traite pour en extraire des informations significatives. Grâce au traitement automatique du langage naturel (NLP), à la vision par ordinateur ou à d’autres capacités d’IA, elle interprète les requêtes des utilisateurs, détecte des schémas et s’efforce de comprendre le contexte général. Cette capacité permet à l’IA de déterminer les mesures à prendre en fonction de la situation.

### Définition des objectifs

L’IA fixe un cap en fonction des objectifs prédéfinis ou des entrées de l’utilisateur. Elle élabore ensuite une stratégie pour atteindre ces objectifs, souvent en utilisant des arbres de décision, l’apprentissage par renforcement ou d’autres algorithmes de planification.

### Prise de décision

L’IA évalue plusieurs actions possibles et choisit l’option la plus optimale en fonction de facteurs tels que l’efficacité, la précision et les résultats prédits. Elle peut utiliser des modèles probabilistes, des fonctions d’utilité ou un raisonnement basé sur le machine learning pour déterminer le meilleur plan d’action.

### Exécution

Après avoir sélectionné une action, l’IA l’exécute, soit en interagissant avec des systèmes externes (API, données, robots), soit en fournissant des réponses aux utilisateurs.

### Apprentissage et adaptation

Après avoir exécuté une action, l’IA évalue le résultat et recueille des commentaires afin d’améliorer les décisions futures. Grâce à l’apprentissage par renforcement ou à l’apprentissage autosupervisé, l’IA affine ses stratégies au fil du temps, elle n’en sera que plus efficace pour gérer des tâches similaires à l’avenir.

### Orchestration

L’orchestration de l’IA désigne la coordination et la gestion des systèmes et des agents. Les plateformes d’orchestration automatisent les [workflows d’IA](https://www.ibm.com/fr-fr/think/topics/ai-workflow), suivent la progression des tâches, gèrent l’utilisation des ressources, surveillent le flux de données et la mémoire, et interviennent en cas d’échec.

Avec la bonne architecture, des dizaines, des centaines, voire des milliers d’agents pourraient théoriquement travailler en symbiose pour une productivité harmonieuse.

## Exemples d’IA agentique

Les solutions d’IA agentique peuvent être déployées pour la quasi-totalité des cas d’utilisation de l’IA, dans n’importe quel écosystème réel. Les agents peuvent s’intégrer dans des workflows complexes pour exécuter des processus métier de manière autonome.

- Un bot de trading alimenté par l’IA peut analyser en direct les cours des actions et les indicateurs économiques pour effectuer une analyse prédictive et exécuter des transactions.

- Dans les véhicules autonomes, les sources de données en temps réel telles que le GPS et les données des capteurs peuvent améliorer la navigation et la sécurité.

- Dans le domaine de la santé, les agents peuvent surveiller les données des patients, ajuster les recommandations de traitement en fonction des nouveaux résultats d’examen et fournir des commentaires en temps réel aux cliniciens via des chatbots.

- Dans le domaine de la cybersécurité, les agents peuvent assurer la surveillance continue du trafic réseau, des journaux système et du comportement des utilisateurs pour détecter les anomalies susceptibles d’indiquer des vulnérabilités à des logiciels malveillants, des attaques par hameçonnage ou des tentatives d’accès non autorisé.

- L’IA peut rationaliser la gestion de la chaîne d’approvisionnement grâce à l’automatisation et à l’optimisation des processus, en passant des commandes de manière autonome auprès des fournisseurs ou en ajustant les calendriers de production pour maintenir des niveaux de stock optimaux.

## Les défis liés aux systèmes d’IA agentique

Les systèmes d’IA agentique représentent un immense potentiel pour les entreprises. Leur autonomie est leur principal avantage, mais cette caractéristique peut avoir de graves conséquences en cas de « déraillement ». Les risques habituels liés à l’IA s’appliquent, mais ils peuvent être amplifiés dans les systèmes agentiques.

De nombreux systèmes d’IA agentique utilisent l’apprentissage par renforcement, qui implique la maximisation d’une fonction de récompense. Si le système de récompense est mal conçu, l’IA pourrait exploiter des failles pour obtenir des « scores élevés » de manière imprévue.

Voici quelques exemples :

- Un agent chargé de maximiser l’engagement sur les réseaux sociaux qui donnerait la priorité aux contenus sensationnels ou trompeurs, diffusant par inadvertance de la désinformation.

- Un robot d’entrepôt optimisant la vitesse des opérations mais endommageant les produits au passage.

- Une IA de négociation financière destinée à maximiser les profits qui s’engage dans des pratiques de trading risquées ou contraires à l’éthique, déclenchant une instabilité du marché.

- Une IA de modération de contenu conçue pour réduire les discours nuisibles qui censurerait des discussions légitimes.

Certains systèmes d’IA agentique peuvent finir par « s’auto-renforcer », intensifiant leurs comportements dans une direction imprévue. Ce problème survient lorsque l’IA s’optimise de manière trop agressive sur un indicateur particulier sans mesures de protection.

Et comme les systèmes agentiques sont souvent composés de plusieurs agents autonomes qui travaillent ensemble, cela entraîne des risques de défaillance. Engorgements, goulots d’étranglement, conflits de ressources : toutes ces erreurs peuvent avoir un effet domino.

Il est important que les modèles aient des objectifs clairement définis qui puissent être mesurés, avec des boucles de rétroaction, le but étant qu’ils se rapprochent de plus en plus de l’intention de l’organisation au fil du temps.
