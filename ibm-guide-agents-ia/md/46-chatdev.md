> Source : https://www.ibm.com/fr-fr/think/topics/chatdev

# Qu’est-ce que ChatDev ?

ChatDev est un cadre des exigences open source qui met en œuvre la collaboration multi-agent par le biais d'une équipe organisée d'agents intelligents spécialisés qui sont alimentés par de grands modèles de langage (LLM). Chaque agent IA est orchestré pour collaborer sur des tâches au cours des phases principales du cycle de vie du développement logiciel afin de générer et de produire de manière autonome une application.[](https://www.ibm.com/fr-fr/think/topics/ai-agents)

ChatDev simule une société de logiciels virtuelle qui opère via divers agents intelligents jouant différents rôles au sein de l’environnement de l’entreprise. Ces agents forment une structure organisationnelle multi-agent dans laquelle ils peuvent collaborer en participant à des séminaires fonctionnels qui permettent de rationaliser le processus de développement de logiciels. ChatDev applique l’IA au modèle « en cascade », un modèle de cycle de vie du développement logiciel qui décompose le processus de développement en phases : conception, codage, test et documentation. Des agents spécialisés travaillent en collaboration pour mener à bien chaque phase.

Les principaux objectifs de ChatDev sont d’offrir un cadre des exigences d’orchestration LLM agentique personnalisable et évolutif et de servir de scénario idéal pour étudier l’intelligence collective. L’intelligence collective est une collaboration efficace, le phénomène où un groupe peut surpasser un individu dans une tâche complexe. L’approche largement acceptée de l’intelligence collective définit les individus comme des entités qui peuvent agir avec un objectif et une raison et s’adapter à un environnement.[1](#f1) Dans les cadres d'exigences tels que ChatDev, ces entités intelligentes sont appelées agents.

## Intelligence collective dans les systèmes multi-agents (MAS)

Les applications de l’intelligence collective dans l’IA et le machine learning comprennent des systèmes d’intelligence collective ou des cadres des exigences appelés MAS. Un MAS peut être décrit comme un réseau interconnecté d’entités ou d’agents capables de résoudre des problèmes qui collaborent pour résoudre des problèmes qui dépassent les capacités ou les connaissances d’un seul agent.[2](#f2)

Les outils d’IA, tels que les systèmes multi-agents, constituent une approche de la conception de l’intelligence collective (COIN). COIN est un système multi-agent étendu qui se caractérise par une communication ou un contrôle centralisés minimes, voire inexistants. Il comporte une fonction d’utilité universelle qui évalue les historiques potentiels de l’ensemble du système.[3](#f3) Le domaine des MAS s'intéresse aux interactions entre les agents au sein du système ainsi qu'à la composition de chaque agent. Bien qu’il existe plusieurs manières de concevoir un MAS, l’objectif principal reste le même : réaliser une tâche globale grâce aux actions de ses composants.

## Interactions coopératives entre plusieurs agents

L’une des étapes les plus difficiles de la conception d’un MAS fonctionnel est la coordination des agents de manière à garantir qu’ils coopèrent sur la tâche globale.[4](#f4) Une collaboration efficace nécessite à la fois des capacités individuelles de résolution de tâches et des interactions bien coordonnées entre les individus participants.[5](#f5) La planification d’un environnement MAS implique les considérations suivantes :

1.  Les contraintes que les activités des autres agents imposent sur le choix d’actions d’un agent
2.  Les contraintes que les engagements d'un agent envers d'autres imposent sur son choix d'actions
3.  L’évolution imprévisible du monde causée par d’autres agents non modélisés[6](#f6)

Une façon d’aborder ce défi de conception consiste à modéliser le travail d’équipe explicitement par le biais de la collaboration multiagent.

Le modèle de conception multicollaborative décompose les prompts complexes et délègue les tâches abstraites aux agents qui les exécutent en fonction de leurs rôles spécialisés.[7](#f7) Par exemple, ChatDev utilise une conception de communication à double agent appelée ChatChain pour faciliter la communication coopérative.

## Comment ChatDev fonctionne-t-il ?

Les cadres comme ChatDev étendent les fonctionnalités des LLM au-delà de leurs capacités exceptionnelles de traitement automatique du langage naturel pour la génération de texte. ChatDev positionne les LLM comme des agents polyvalents grâce à ses techniques d’orchestration qui impliquent de promptiser et d’évaluer plusieurs agents collaboratifs jouant divers rôles sociaux (par exemple, ingénieur logiciel, directeur de la technologie, PDG, concepteur, testeur).

Chaque agent utilise son rôle spécifique pour travailler en collaboration sur les phases principales du cycle de vie du développement logiciel. Ce processus implique une communication intensive entre les agents dans leurs rôles spécialisés pour comprendre et analyser les exigences en langage naturel, et le développement et le débogage à l’aide de langages de programmation. Les phases du ChatChain présentent différents niveaux d’engagement dans les langages naturels et de programmation, en fonction du rôle et du prompt des agents.

### Comment ChatDev prompt ses agents IA

Les agents de ChatDev utilisent le jeu de rôle et l’apprentissage automatique comme guides pour accomplir leurs tâches. L'incitation d'inception est une méthode d'auto-prompt automatique conversationnelle LLM qui permet aux agents de se prompter mutuellement pour résoudre des tâches par le biais de jeux de rôle.[8](#f8)

ChatDev applique le prompt engineering au début de chaque phase de sous-tâche. Bien que ChatChain puisse bien définir le processus de résolution des tâches, les agents se contentent d’échanger des réponses sans invites ni garde-fous supplémentaires n’est pas efficace pour une communication orientée tâches à plusieurs cycles. Pour faire progresser la progression des communications productives et éviter les défis tels que le retournement des rôles, la répétition des instructions et les fausses réponses, ChatDev utilise un mécanisme de prompting.

Le mécanisme de prompting d’inception fonctionne en encapsulant les LLM avec l’instructeur et le prompt du système assistant au fur et à mesure de leur instanciation. LLM hypnose peut avoir une connotation négative (elle peut être utilisée malveillante pour manipuler un modèle), mais dans ce cas, il s’agit d’un moyen de prompter efficacement les agents qui jouent un rôle. Dans le prompt, les tâches et les rôles sont spécifiés afin de garantir que le LLM indique aux agents comment remplir leur rôle collaboratif et suivre les instructions.

Ces prompts initiaux pour chaque rôle aident les agents à donner les réponses appropriées sans changement de rôle. Les prompts pour les deux rôles dans le système sont presque identiques : vue d’ensemble et objectifs de la sous-tâche en cours, rôles spécialisés, outils externes disponibles, protocoles de communication, conditions de terminaison et contraintes ou exigences pour empêcher les comportements indésirables.[9](#f9) Ce mécanisme fonctionne comme un garde-fou LLM, améliorant la qualité des réponses et réduisant le besoin d’intervention humaine.

### Comment les agents IA interagissent-ils dans ChatDev

Pour guider une communication coopérative efficace entre les agents, ChatDev introduit un workflow agentique appelé ChatChain pour décomposer chaque phase en sous-tâches plus faciles à gérer. Ce processus guide les communications multi-turns entre les différents rôles afin de proposer et de valider des solutions pour chaque sous-tâche. Les agents sont régis par un mécanisme appelé communicative « déshallucination , un modèle communicatif visant à atténuer les hallucinations inattendues. Avec ce mécanisme, les agents demandent des informations plus détaillées avant de répondre directement, puis de continuer la phase suivante de communication en fonction de ces informations.[10](#f10)

ChatDev fournit un visualiseur basé sur un navigateur qui permet d’étudier les interactions de chaque agent agissant dans le cadre de son rôle et de son environnement. Cette interface permet aux utilisateurs d’étudier la conception du système multi-agent lui-même. Les utilisateurs peuvent visualiser la structure de coopération artificielle qui permet aux agents de travailler ensemble pour accomplir une tâche globale qui dépasse leurs capacités individuelles.

#### ChatChain

ChatChain suit une conception de communication à deux agents qui simplifie le processus de résolution des tâches tout au long du workflow agentique. Le modèle de conception agentique commence par segmenter le processus de développement logiciel en trois phases séquentielles : conception, codage et test. Les phases de codage et de test sont ensuite divisées en sous-tâches : codage et réalisation, et avis (test statique) et test système (test dynamique).

Chaque phase de communication au sein d’un ChatChain est composée d’un agent instructeur et d’un agent assistant. Dans chaque sous-tâche, deux agents ayant des rôles spécialisés distincts (comme un réviseur et un programmeur de conception d'interface graphique) remplissent les fonctions d'un instructeur et d'un assistant. L’agent instructeur instruit le discours vers l’achèvement d’une tâche tandis que l’agent assistant reçoit et suit ces instructions et répond avec des solutions appropriées.[11](#f11) Les agents s’engagent dans un dialogue à plusieurs tours jusqu’à ce que la tâche soit terminée ou qu’un consensus soit atteint. Les solutions extraites de la phase de communication vont du texte (par exemple, une description de la fonctionnalité souhaitée de l'application) au code (par exemple, le code source initial).

Ce workflow simplifie les communications en évitant les topologies multi-agents complexes et en rationalisant efficacement le processus de consensus.[12](#f12) Cette approche permet une transition fluide entre les sous-tâches, car les solutions des tâches précédentes servent de ponts à la phase suivante. Ce workflow continue jusqu'à ce que toutes les sous-tâches soient terminées, guidant les agents tout au long du processus. La structure de type chaîne du workflow relie les sous-tâches en langage naturel et en langage de programmation, guidant efficacement les agents dans l’éléments à communiquer. ChatChain est une solution au problème le plus complexe de la conception de MAS, à savoir la coopération entre agents.

En utilisant les paramètres par défaut, le ChatChain produit les logiciels dans l’ordre suivant :

- **Analyse de la demande :** décidez de la procédure globale de méthode pour l’application.
- **Sélection du langage :** décidez quel langage de programmation utiliser pour créer et exécuter le logiciel.
- **Codage :** les agents écrivent le code pour créer l’application.
- **CodeCompleteAll** : compléter le code, y compris les fonctions/classes manquantes.
- **CodeReview :** revoir et modifier le code pour les fonctionnalités.
- **Test** : exécutez le logiciel et modifiez le code en fonction du rapport de test.
- **EnvironmentDoc :** documenter l’environnement.
- **Manuel :** documenter et rédiger un manuel pour l'application.

#### Déshallucination communicationnelle

Les hallucinations associées aux LLM se produisent lorsque les modèles produisent une sortie inexacte ou absurde. Les hallucinations de codage sont un type d’hallucination qui affecte les sorties des modèles effectuant des tâches liées à la programmation. Les chercheurs de ChatDev ont constaté que des hallucinations de codage apparaissent fréquemment lorsque l’agent exécutant les fonctionnalités d’assistant a du mal à suivre des instructions précises.[13](#f13) Les assistants ont généralement du mal à suivre les instructions en raison de leur vague, qui nécessite de multiples interactions de suivi et des ajustements. Pour éviter les résultats indésirables, ChatDev introduit une dhallucination comunicale.[](#f13)

La déshallucination communicationnelle invite l’assistant à demander activement des suggestions plus détaillées au formateur avant de fournir une réponse formelle.[14](#f14) Les assistants jouent un rôle d'instructeur et recherchent de manière proactive plus d'informations (par exemple, les noms précis des dépendances externes ou le référentiel GitHub dans lequel les modifications sont nécessaires), en adoptant un « renversement de rôle » délibéré avant de fournir une réponse. L’assistant effectue une optimisation précise après que l’instructeur a répondu avec des modifications. Le schéma de communication indique aux agents comment communiquer, ce qui permet un échange d’informations précis tout en réduisant les hallucinations de codage.

### Visualiseur

Le visualiseur de ChatDev est une application Python qui exécute une démo Web locale où les utilisateurs peuvent afficher des journaux en temps réel, des journaux rejoués et ChatChain. L'application contient trois visualiseurs de journaux distincts pour chacun.

- **Log Visualizer :** un journal en temps réel qui imprime les informations de boîte de dialogue de l’agent, les changements d’environnement et d’autres informations système utiles pour le débogage.
- **Visualiseur de replay :** le journal de replay imprime les informations de boîte de dialogue de l’agent.
- **Visualiseur ChatChain :** les utilisateurs peuvent télécharger n’importe quel fichier de configuration ChatChain et visualiser la chaîne de workflow pour tous les projets logiciels actuels ou précédents. Cette fonctionnalité offre une vue transparente de l’ensemble du processus de développement de logiciels qui permet aux utilisateurs d’examiner chaque sous-tâche de la solution et d’identifier les inefficacités possibles.

Le visualiseur contient également une page de revoir le chat qui affiche les boîtes de dialogue en langage naturel entre les agents pour une application donnée.

### Intégration des LLM de ChatDev

 Le concept du modèle de conception agentique de ChatDev est similaire à la technique du machine learning, à l'exception de ses agents IA, qui sont des experts spécialisés dans la gestion de tâches complexes. Les systèmes d’orchestration sont nécessaires pour coordonner la collaboration entre un mélange d’agents spécialisés.

Les modèles de transformeurs pré-entraînés, tels que les modèles GPT d’OpenAI, constituent la base de telles orchestrations.[15](#f15) Les modèles de fondation,comme la série Granite d’IBM, peuvent également être utilisés pour fonder les agents avec des capacités de langage robustes et leur accorder des fonctionnalités spécialisées. Par exemple, Granite Code est une famille de modèles allant de 3 à 34 milliards de paramètres et a été entraînée sur 116 langages de programmation. Cette offre est avantageuse pour les cadres des exigences agentiques qui prévoient d’utiliser des agents de communication pour le développement de logiciels. Au moment de la rédaction du présent document, ChatDev prend en charge les modèles GPT-3.5-turbo et GPT-4 d’OpenAI pour alimenter leurs agents intelligents.

### Comment ChatDev évolue

ChatDev met en œuvre un moyen de dimensionner la collaboration multi-agent basée sur un LLM avec des réseaux de collaboration multi-agent (MacNet). MacNet s’inspire du principe de dimensionnement neuronal, qui suggère que l’augmentation du nombre de neurones entraîne l’émergence de capacités.[16](#f16) ChatDev propose un principe similaire qui s’applique à l’augmentation du nombre d’agents dans le cadre d’une collaboration à plusieurs agents.

MacNet utilise des graphiques acycliques pour structurer les agents et améliorer leur raisonnement interactif grâce à l’ordre topologique. Les solutions sont dérivées des interactions des agents. Ce processus surpasse systématiquement les modèles de référence, favorisant une collaboration efficace entre les agents sur différentes topologies de réseau et permettant la coopération entre plus d’un millier d’agents. Grâce à cette application, ChatDev a identifié une loi d’évolutivité collaborative qui montre que la qualité des solutions s’améliore dans un modèle de croissance logistique à mesure que le nombre d’agents augmente.

## Systèmes multi-agents pour le développement de logiciels

Plutôt que d'essayer de réunir toutes les capacités dans un seul modèle, les systèmes multi-agents répartissent les tâches entre plusieurs agents spécialisés. Les agents peuvent utiliser le même modèle de langage ou d’autres, ce qui leur permet d’accomplir un large éventail de tâches.

ChatDev a effectué une évaluation dans un article de recherche populaire qui compare ses performances à celles de deux autres cadres d'orchestration de développement logiciel basés sur un LLM, GPT-Engineer et MetaGPT. Les indicateurs étaient basés sur l’exhaustivité, l’exécutable, la cohérence et la qualité. ChatDev et MetaGPT ont surpassé GPT-Engineer, une approche d’orchestration à agent unique, démontrant que les tâches complexes sont plus difficiles à résoudre dans une solution en une seule étape. Ces résultats en termes de performances suggèrent que le fait de décomposer des tâches complexes en sous-tâches plus faciles à gérer améliore l’efficacité de l’exécution des tâches.

ChatDev a surpassé MetaGPT de manière significative dans l'indicateur de qualité en raison des méthodes de communication coopératives des agents qui utilisent à la fois des langages naturels et de programmation. Les agents capables d’une communication efficace ont pu guider chaque sous-tâche jusqu’à son achèvement, en surmontant les restrictions qui sont généralement liées aux règles d’optimisation établies manuellement.[17](#f17) Ce résultat suggère que les cadres des exigences multi-agents qui utilisent des agents communicationnels et collaboratifs offrent des fonctions plus polyvalentes et plus adaptables.

## Autres cadres multi-agents

**GPT-Engineer** — Un cadre des exigences d'orchestration à agent unique pour créer des applications logicielles. L’utilisateur invite l’IA à créer une application avec la fonctionnalité logicielle souhaitée et peut communiquer avec le système pour apporter des améliorations ou des mises à jour.[18](#f18) Les utilisateurs peuvent comparer les implémentations de leurs propres agents aux jeux de données les plus répandus grâce à « benchmark », un fichier binaire installé dans le système qui contient une interface simple d’analyse comparative.

**MetaGPT** – Un cadre des exigences multiagent qui fonctionne comme une entité logicielle collaborative qui assigne différents agents de jeu de rôle à des modèles GPT pour effectuer des tâches complexes. Comme ChatDev, les agents occupent différents rôles au sein d’un environnement virtuel semblable à une société de logiciels. MetaGPT utilise également des SOP (Standard Operating Procedures) Orchestrate pour générer des logiciels.

**crewAI** – crewAI est un cadre multi-agents open source qui fonctionne sur LangChain. Elle organise les agents IA autonomes en équipes qui gèrent les workflows et les tâches liés aux applications. crewAI s’intègre à n’importe quel LLM.

**AutoGen** – le cadre de conversation multi-agent open source de Microsoft fournit une abstraction élevée des modèles de fondation. AutoGen est un cadre des exigences basé sur des agents qui utilise plusieurs agents pour interagir et traiter les tâches. Ses fonctionnalités principales incluent des agents IA personnalisables qui participent à des dialogues multi-agents avec des modèles adaptables, permettant ainsi la création de diverses applications LLM.
