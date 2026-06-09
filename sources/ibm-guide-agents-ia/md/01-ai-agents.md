> Source : https://www.ibm.com/fr-fr/think/topics/ai-agents

# Qu'est-ce qu'un agent IA?

## Qu'est-ce qu'un agent IA ?

Un agent d’IA ([intelligence artificielle](https://www.ibm.com/fr-fr/think/topics/artificial-intelligence)) est un système qui exécute des tâches de manière autonome en concevant des [workflows](https://www.ibm.com/fr-fr/think/topics/agentic-workflows) à l’aide d’outils disponibles.

Les agents IA peuvent offrir un large éventail de fonctionnalités au-delà du traitement automatique du langage naturel, comme la prise de décision, la résolution de problèmes, l’interaction avec des environnements externes et l’exécution d’actions.

Les agents IA peuvent être utilisés dans l’entreprise dans diverses situations pour effectuer des tâches complexes, notamment la conception de logiciels, l’automatisation, la génération de code et l’assistance conversationnelle. 

Ils utilisent les techniques avancées de traitement automatique du langage naturel des grands modèles de langage (LLM) pour comprendre et répondre aux entrées utilisateur, étape par étape, et déterminer quand utiliser des outils externes.

## Fonctionnement des agents IA

Les grands modèles linguistiques (LLM) sont au cœur des agents IA. C’est pourquoi ces agents sont souvent appelés agents LLM. Les LLM traditionnels, comme les modèles IBM® Granite, produisent des réponses basées sur les données utilisées pour leur entraînement et sont limités par les connaissances et les capacités de raisonnement.

En revanche, la technologie d’agents utilise l’appel d’outils en arrière-plan pour obtenir des informations actualisées, optimiser les workflows et créer des sous-tâches de manière autonome afin d’atteindre des objectifs complexes.

Dans ce processus, l’agent autonome apprend à s’adapter aux attentes de l’utilisateur au fil du temps. La capacité de l’agent à mémoriser les interactions passées et à planifier des actions futures favorise une expérience personnalisée et des réponses complètes.1 

Cet appel d’outils peut se faire sans intervention humaine, élargissant ainsi les possibilités d’application réelle de ces systèmes d’IA. Ces trois étapes ou [composants agentiques](https://www.ibm.com/fr-fr/think/topics/components-of-ai-agents) définissent le fonctionnement des agents :

### Objectifs, règles et planification dans les systèmes d’agents IA

Bien que les agents IA soient autonomes dans leurs processus de prise de décision, ils ont besoin d’objectifs et de règles prédéfinies par les humains.2Le comportement des agents autonomes est influencé par trois facteurs principaux :

1.  L’équipe de développeurs qui conçoit et entraîne le système d’IA agentique. 
2.  L’équipe qui déploie l’agent et permet à l’utilisateur d’y accéder.
3.  L’utilisateur, qui fournit à l’agent des objectifs spécifiques à atteindre et définit les outils disponibles.

En fonction des objectifs de l’utilisateur et des outils disponibles, l’agent d’IA procède à la décomposition des tâches pour améliorer ses performances.3Essentiellement, l’agent crée un plan de tâches et de sous-tâches spécifiques pour atteindre des objectifs complexes.

Pour les tâches simples, la planification n’est pas nécessaire ; l’agent IA peut plutôt itérativement améliorer ses réponses sans planifier ses prochaines étapes.

### Raisonnement avec les outils disponibles

Les agents d’IA fondent leurs actions sur les informations qu’ils perçoivent. Cependant, ils ne disposent pas toujours de toutes les connaissances nécessaires pour s’attaquer à toutes les sous-tâches d’un objectif complexe.

Pour combler cette lacune, ils se tournent vers les outils disponibles tels que des jeux de données externes, des recherches sur le web, des API et même d’autres agents.

Une fois les informations manquantes collectées, l’agent d’IA met à jour sa base de connaissances et procède au [raisonnement agentique](https://www.ibm.com/fr-fr/think/topics/agentic-reasoning). Ce processus implique de réévaluer en permanence son plan d’action et d’apporter des corrections, ce qui permet une prise de décision plus éclairée et plus adaptative.

Pour illustrer ce processus, imaginons un utilisateur qui planifie ses vacances. L’utilisateur demande à un agent d’IA de prédire quelle semaine de l’année prochaine aura probablement les meilleures conditions météorologiques pour son voyage de surf en Grèce.

Comme le modèle LLM au cœur de l’agent n’est pas spécialisé dans les tendances météorologiques, ce dernier ne peut pas se fier uniquement à ses connaissances internes. Par conséquent, l’agent recueille des informations auprès d’une base de données externe contenant les bulletins météorologiques quotidiens de la Grèce des dernières années.

Même après l’acquisition de ces nouvelles informations, l’agent n’est toujours pas capable de déterminer les conditions météorologiques optimales pour le surf.

Par conséquent, une nouvelle sous-tâche est créée. Pour cette sous-tâche, l’agent communique avec un agent externe spécialisé dans le surf. Disons qu’en procédant ainsi, l’agent apprend que les marées hautes et le temps ensoleillé avec peu ou pas de pluie sont idéaux pour le surf.

L’agent peut alors combiner les informations apprises grâce à ses outils pour identifier des modèles et prédire quelle semaine de l’année prochaine en Grèce aura des marées hautes, un temps ensoleillé et un faible risque de pluie.

Ces résultats sont ensuite présentés à l’utilisateur. Ce partage d’informations entre outils est ce qui permet aux agents IA d’être plus polyvalents que les modèles IA traditionnels.3

### Apprentissage et réflexion

Les agents IA utilisent des mécanismes de retour d’information, tels que d’autres agents IA ou l’interaction humaine suivant le principe de l’humain dans la boucle (« human-in-the-loop » ou HITL) pour améliorer la précision de leurs réponses.

Reprenons l’exemple de surf pour l’illustrer. Après avoir formulé sa réponse à l’utilisateur, l’agent stocke les informations apprises ainsi que les retours de l’utilisateur pour améliorer ses performances et s’adapter aux préférences de ce dernier lors de futurs objectifs.

Si d’autres agents ont été utilisés pour atteindre l’objectif, leurs retours peuvent également être intégrés. Le retour d’information de plusieurs agents peut être particulièrement utile pour minimiser le temps que les utilisateurs humains consacrent à donner des instructions.

Cependant, les utilisateurs peuvent également fournir des retours tout au long des actions et du raisonnement interne de l’agent pour mieux aligner les résultats sur l’objectif fixé.2

Les mécanismes de retour d’information améliorent le raisonnement et la précision des agents d’IA, processus communément appelé raffinement itératif.3 

Pour éviter de répéter les mêmes erreurs, les agents d’IA peuvent également stocker des données sur les solutions trouvées face à des obstacles précédents dans une base de connaissances.

## Chatbots IA agentiques ou non agentiques

Les chatbots IA utilisent des techniques d’IA conversationnelle telles que le traitement automatique du langage naturel (NLP) pour comprendre les questions des utilisateurs et automatiser les réponses. Ces chatbots sont une modalité, tandis que l’agentivité est un cadre technologique.

Les chatbots IA non agentiques sont ceux qui ne disposent ni d’outils, ni de mémoire, ni de capacités de raisonnement. Ils ne peuvent atteindre que des objectifs à court terme et ne sont pas capables de planifier à l’avance. Tels que nous les connaissons, les chatbots non agentiques nécessitent une intervention continue de l’utilisateur pour répondre.

Ils peuvent produire des réponses à des questions courantes qui sont susceptibles de correspondre aux attentes de l’utilisateur, mais leurs performances sont insuffisantes face à des questions spécifiques à l’utilisateur ou à ses données. Étant donné que ces chatbots n’ont pas de mémoire, ils ne peuvent pas apprendre de leurs erreurs si leurs réponses sont insatisfaisantes.

En revanche, les chatbots IA agentiques apprennent à s’adapter aux attentes des utilisateurs au fil du temps, offrant ainsi une expérience plus personnalisée et des réponses plus complètes. Ils peuvent accomplir des tâches complexes en créant des sous-tâches sans intervention humaine et en élaborant différents plans.

Ces plans peuvent également être autocorrigés et mis à jour si nécessaire. Contrairement aux chatbots non agentiques, les chatbots IA agentiques évaluent leurs outils et utilisent les ressources disponibles pour combler les lacunes en matière d’information.

## Paradigmes de raisonnement

Il n’existe pas d’architecture standard pour la création d’agents IA. Différents paradigmes existent pour résoudre des problèmes à plusieurs étapes.

### ReAct (raisonnement et action)

Avec le paradigme ReAct, les agents sont instruits pour « réfléchir » et planifier après chaque action réalisée et chaque réponse obtenue d’un outil afin de décider quel outil utiliser ensuite. Ces boucles de réflexion, d’action et d’observation sont utilisées pour résoudre des problèmes étape par étape et améliorer les réponses de manière itérative.

Grâce à la structure des invites, les agents peuvent être instruits pour raisonner lentement et exposer chaque « pensée ».4 Le raisonnement verbal de l’agent permet de comprendre comment les réponses sont formulées.

Dans ce cadre, les agents actualisent en permanence leur contexte en intégrant de nouveaux raisonnements. Cette approche peut être interprétée comme une forme d’incitation par chaîne de pensée (CoT).

### ReWOO (raisonnement sans observation)

La méthode ReWOO, contrairement à ReAct, supprime la dépendance aux résultats des outils pour la planification des actions. Les agents planifient en amont, évitant ainsi une utilisation redondante des outils en anticipant ceux qu’il faudra utiliser dès la réception de l’invite initiale de l’utilisateur.

Cette approche est souhaitable du point de vue de l’utilisateur, car celui-ci peut confirmer le plan avant qu’il ne soit exécuté.

Le workflow de ReWOO se compose de trois modules. Dans le module de planification, l’agent anticipe ses prochaines étapes à partir de l’invite de l’utilisateur. L’étape suivante consiste à collecter les résultats des outils. Enfin, l’agent associe le plan initial aux résultats des outils pour formuler une réponse.

Cette planification anticipée peut réduire considérablement l’utilisation des jetons et la complexité informatique, tout en minimisant les impacts d’une éventuelle défaillance intermédiaire des outils.5

## Types d'agents d'IA

Les agents d’IA peuvent être développés avec différents niveaux de capacités. Un agent simple peut être utilisé pour des objectifs simples afin de limiter toute complexité informatique inutile. Dans l’ordre du plus simple au plus avancé, il existe cinq principaux types d’agents :

 

1.  Agents réflexes simples
2.  Agents réflexes basés sur un modèle
3.  Agents basés sur des objectifs
4.  Agents basés sur l’utilité
5.  Agents apprenants

### 1. Agents réflexes simples

Les agents réflexes simples sont la forme d’agent la plus basique qui fonde ses actions sur la perception. Ces agents ne bénéficient ni d’une mémoire ni d’une interaction avec d’autres agents lorsqu’il leur manque des informations. Ils fonctionnent sur la base de règles ou de réflexes préprogrammés. Ce comportement signifie que l’agent exécute des actions en fonction de certaines conditions définies à l’avance.

Si l’agent rencontre une situation pour laquelle il n’est pas programmé, il ne peut pas réagir de manière appropriée. Ces agents sont efficaces dans des environnements entièrement observables, où toutes les informations nécessaires sont disponibles.6

**Exemple** : s’il est 20 heures, le chauffage est activé (par exemple, un thermostat qui allumera le système de chauffage à une heure définie tous les soirs).\

  Diagramme de l'agent réflexe simple

### 2. Agents réflexes basés sur un modèle

Les agents réflexes basés sur un modèle utilisent à la fois leur perception actuelle et leur mémoire pour maintenir un modèle interne du monde. À mesure que l'agent reçoit de nouvelles informations, ce modèle est mis à jour. Les actions de l'agent dépendent de ce modèle, de ses réflexes, des perceptions antérieures et de son état actuel.

Contrairement aux agents réflexes simples, ces agents peuvent stocker des informations en mémoire et opérer dans des environnements partiellement observables et dynamiques. Cependant, ils restent limités par leur ensemble de règles.6

**Exemple :** un aspirateur robot. Lorsqu’il nettoie une pièce, il détecte les obstacles comme les meubles et s’ajuste en conséquence. Le robot stocke également un modèle des zones déjà nettoyées pour éviter de repasser aux mêmes endroits.

  Diagramme d'un agent réflexe basé sur un modèle

### 3. Agents basés sur des objectifs

Les agents basés sur des objectifs possèdent un modèle interne du monde ainsi qu'un ou plusieurs objectifs. Ces agents recherchent des séquences d'actions pour atteindre leurs objectifs et planifient ces actions avant de les exécuter. Cette recherche et cette planification améliorent leur efficacité par rapport aux agents réflexes simples et aux agents basés sur un modèle.7

**Exemple :** un système de navigation qui recommande l'itinéraire le plus rapide pour atteindre votre destination. Le modèle prend en compte différents itinéraires permettant d'atteindre votre destination, ou en d'autres termes, votre objectif. Dans cet exemple, la règle condition-action de l'agent stipule que si un itinéraire plus rapide est trouvé, l'agent le recommande à la place.

  Diagramme d’agent basé sur les objectifs

### 4. Agents basés sur l'utilité

Les agents d’IA basés sur l’utilité sélectionnent la séquence d’actions qui permet d’atteindre l’objectif tout en maximisant l’utilité ou la récompense. L’utilité est calculée à l’aide d’une fonction d’utilité. Cette fonction attribue une valeur d’utilité, un indicateur mesurant l’utilité d’une action ou le degré de satisfaction de l’agent, à chaque scénario en fonction d’un ensemble de critères fixes.

Les critères peuvent inclure des facteurs tels que la progression vers l’objectif, le temps requis ou la complexité informatique. L’agent sélectionne ensuite les actions qui maximisent l’utilité attendue. Ces agents IA sont donc utiles dans les cas où plusieurs scénarios permettent d’atteindre un objectif souhaité et où il faut en sélectionner un optimal.7

**Exemple :** un système de navigation qui recommande l’itinéraire vers votre destination en optimisant l’efficacité énergétique et en minimisant le temps passé dans les embouteillages et le coût des péages. Cet agent mesure l’utilité à travers cet ensemble de critères pour sélectionner l’itinéraire le plus favorable.

  Diagramme d'un agent basé sur l'utilité

### 5. Agents apprenants

Les agents apprenants possèdent les mêmes capacités que les autres types d’agents, mais leur particularité réside dans leur capacité d’apprentissage. De nouvelles expériences sont ajoutées à leur base de connaissances initiale de manière autonome.

Cet apprentissage améliore la capacité de l’agent à opérer dans des environnements peu familiers. Le raisonnement des agents apprenants peut être basé sur l’utilité ou sur un objectif, et ils se composent de quatre éléments principaux :7

- **Apprentissage :** ce processus améliore les connaissances de l’agent en apprenant de l’environnement par le biais de ses préceptes et capteurs.

<!-- -->

- **Critique :** ce composant fournit un retour à l’agent sur la qualité de ses réponses par rapport à la norme de performance.

<!-- -->

- **Performance :**  cet élément est responsable de la sélection des actions à partir de l’apprentissage acquis.

<!-- -->

- **Générateur de problème :** ce module crée diverses propositions d’actions à entreprendre.

**Exemple** : recommandations personnalisées sur les sites de commerce électronique. Ces agents enregistrent l’activité et les préférences de l’utilisateur dans leur mémoire.

Ces informations sont utilisées pour recommander certains produits et services à l’utilisateur. Le cycle se répète à chaque fois que de nouvelles recommandations sont faites. L’activité de l’utilisateur est continuellement stockée pour améliorer l’apprentissage, ce qui permet à l’agent d’affiner ses recommandations au fil du temps.

  Diagramme d'un agent apprenant

### Cas d’utilisation des agents d’IA

Expérience client

Les agents IA peuvent être intégrés dans des sites web et des applications pour améliorer l’expérience client, en servant d’un assistant virtuel, en fournissant un soutien en matière de santé mentale, en simulant des entretiens, et pour d’autres tâches connexes.8 Il existe de nombreux modèles no-code permettant aux utilisateurs de créer facilement ces agents IA.

Soins de santé

Les agents d’intelligence artificielle peuvent également être utilisés dans diverses applications dans le secteur de la santé. Les systèmes multi-agents peuvent être utiles pour la résolution de problèmes dans ces environnements. Qu’il s’agisse de la planification des traitements des patients dans les services d’urgence ou de la gestion des processus médicamenteux, ces systèmes permettent aux professionnels de la santé de consacrer leur temps et leurs efforts à des tâches plus urgentes.9

Réponse aux situations d'urgence

En cas de catastrophe naturelle, les agents IA peuvent utiliser des algorithmes d’apprentissage profond pour récupérer sur les réseaux sociaux les informations des utilisateurs ayant besoin d’être secourus. La localisation de ces utilisateurs peut être cartographiée pour aider les services de secours à sauver davantage de personnes en moins de temps. Ainsi, les agents IA peuvent considérablement améliorer la vie humaine, tant dans les tâches quotidiennes que dans des situations de sauvetage.10

Finance et chaîne d’approvisionnement

Les agents peuvent être conçus pour analyser des données financières en temps réel, anticiper les tendances futures du marché et optimiser la gestion de la chaîne d’approvisionnement. La personnalisation des agents IA autonomes nous permet de personnaliser les résultats de nos données uniques. Lorsque vous travaillez avec des données financières, il est essentiel de mettre en place des mesures de sécurité pour garantir la confidentialité des données.

## Avantages des agents d’IA

### Automatisation des tâches

Avec les progrès continus de l’IA générative et le machine learning, l’optimisation des workflows grâce à l’IA, ou l’automatisation intelligente, suscite un intérêt croissant. 

Les agents IA sont des outils capables d’automatiser des tâches complexes qui nécessiteraient autrement des ressources humaines. Cela permet d’atteindre des objectifs à moindre coût, rapidement et à grande échelle. Grâce à ces avancées, les agents humains n’ont plus besoin de fournir des instructions à l’assistant d’IA pour qu’il crée et gère ses tâches. 

### Performances accrues

Les cadres multi-agents ont tendance à surpasser les agents uniques.11 En effet, plus un agent dispose de plans d’action, plus il peut apprendre et réfléchir.

Un agent d'IA qui intègre les connaissances et les retours d'autres agents d'IA spécialisés dans des domaines connexes peut être utile pour la synthèse d'informations. Cette collaboration en arrière-plan entre agents d'IA, ainsi que leur capacité à combler les lacunes en matière d'information, est propre aux cadres agentiques, en faisant un outil puissant et une avancée majeure dans l'intelligence artificielle.

### Qualité des réponses

Les agents IA fournissent des réponses plus complètes, précises et personnalisées que les modèles IA traditionnels. Cette adaptabilité est importante pour nous, en tant qu’utilisateurs, car des réponses de meilleure qualité améliorent généralement l’expérience client. Comme décrit précédemment, cette capacité est rendue possible grâce à l’échange d’informations avec d’autres agents, à l’utilisation d’outils et à la mise à jour de leur flux de mémoire. Ces comportements émergent d’eux-mêmes et ne sont pas préprogrammés.12

## Risques et limites des agents IA

### 1. Dépendances multi-agents

Certaines tâches complexes nécessitent les connaissances de plusieurs agents IA.  L’orchestration de ces cadres multi-agents présente un risque de dysfonctionnement.

 Les systèmes multi-agents construits sur les mêmes modèles de fondation peuvent rencontrer des écueils communs. Ces faiblesses peuvent entraîner une défaillance de l’ensemble du système pour tous les agents concernés ou exposer des vulnérabilités face à des attaques adverses.13 

Cela souligne l’importance d’une bonne gouvernance des données dans la conception des modèles de fondation ainsi que de processus rigoureux de formation et de test.

### 2. Boucles de rétroaction infinies

Si la commodité d’un raisonnement autonome offert par les agents IA est appréciable pour les utilisateurs, elle n’en comporte pas moins des risques. 

Les agents qui ne parviennent pas à établir un plan complet ou à analyser leurs résultats peuvent se retrouver à utiliser les mêmes outils à plusieurs reprises, entraînant des boucles de rétroaction infinies. Pour éviter ces redondances, un certain niveau de surveillance humaine en temps réel peut être requis.13

### 3. Complexité informatique

Créer des agents IA à partir de zéro prend du temps et peut également être coûteux en termes de ressources informatiques. Les ressources nécessaires à la formation d’un agent performant peuvent être considérables. De plus, en fonction de la complexité de la tâche, les agents peuvent mettre plusieurs jours à la terminer.12

### 4. Confidentialité des données

En cas de mauvaise gestion, l’intégration des agents IA dans les processus métier et les systèmes de gestion des clients peut soulever de graves problèmes de sécurité.

Par exemple, imaginez des agents IA dirigeant le processus de développement de logiciels, faisant passer les copilotes de codage au niveau supérieur ou déterminant la tarification pour les clients, sans aucune supervision humaine ni aucun garde-fou. Les résultats de tels scénarios peuvent être préjudiciables en raison du comportement expérimental et souvent imprévisible de l’[IA agentique](https://www.ibm.com/fr-fr/think/topics/agentic-ai).

Par conséquent, il est essentiel que les fournisseurs d’IA tels qu’IBM, Microsoft et OpenAI restent proactifs. Ils doivent mettre en œuvre des protocoles de sécurité étendus pour garantir que les données sensibles des employés et des clients sont stockées en toute sécurité. L’adoption de pratiques de déploiement responsables est essentielle pour minimiser les risques et maintenir la confiance dans ces technologies en rapide évolution.

## Bonnes pratiques

### 1. Journaux d’activité

Pour répondre aux préoccupations liées aux dépendances multi-agents, les développeurs peuvent donner aux utilisateurs un accès à un journal des actions de l’agent.14 

Ces actions peuvent inclure l’utilisation d’outils externes et décrire les agents externes utilisés pour atteindre l’objectif. Cette transparence permet aux utilisateurs de mieux comprendre le processus de prise de décision itératif, de détecter d’éventuelles erreurs et d’instaurer un climat de confiance.

### 2. Interruption

Il est recommandé d’empêcher les agents IA autonomes de fonctionner pendant des périodes trop longues. Cela est particulièrement important dans les cas de boucles de rétroaction infinies involontaires, de changements d’accès à certains outils ou de dysfonctionnements liés à des défauts de conception. L’une des solutions consiste à mettre en œuvre al capacité d’interruption.

Pour garder ce contrôle sur le processus décisionnel, il faut permettre aux utilisateurs humains d’interrompre une séquence d’actions ou l’opération entière de manière contrôlée.

Le choix de savoir si et quand interrompre un agent IA nécessite réflexion, car certaines interruptions peuvent causer plus de tort que de bien. Par exemple, il peut être plus sûr de laisser un agent défectueux continuer à fonctionner en cas d’urgence vitale plutôt que de l’arrêter complètement.5

### 3. Identifiants uniques pour les agents

Pour atténuer le risque que des systèmes agentiques soient utilisés à des fins malveillantes, des identifiants uniques peuvent être mis en œuvre. Rendre ces identifiants obligatoires pour l’accès des agents aux systèmes externes faciliterait la traçabilité de l’origine de leurs développeurs, déployeurs et utilisateurs.

Cette approche ajoute une couche de responsabilité essentielle. La traçabilité permet d’identifier les parties responsables lorsqu’un agent cause une utilisation malveillante ou des dommages involontaires. Au final, ce type de mesure de protection favoriserait un environnement opérationnel plus sécurisé pour les agents IA.

### 4. Supervision humaine

Pour faciliter le processus d’apprentissage des agents IA, notamment dans leurs premières phases d’intégration dans un nouvel environnement, il peut être utile d’avoir un certain niveau de supervision humaine.

Grâce à ces informations, l’agent IA peut ainsi comparer ses performances à la norme attendue et procéder à des ajustements. Cette forme de feedback améliore l’adaptabilité de l’agent aux préférences des utilisateurs.5

Outre cette mesure de protection, il est également préférable de demander une validation humaine avant qu’un agent IA ne prenne des actions à fort impact.

Par exemple, l’envoi d’e-mails en masse ou le trading financier devraient nécessiter une confirmation humaine.7 Un certain niveau de surveillance humaine est recommandé dans ces domaines à haut risque.
