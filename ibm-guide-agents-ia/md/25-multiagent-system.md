> Source : https://www.ibm.com/fr-fr/think/topics/multiagent-system

# Qu’est-ce qu’un système multi-agent ?

Un système multi-agent (MAS) est composé de plusieurs agents d’intelligence artificielle (IA) travaillant ensemble pour accomplir des tâches au nom d’un utilisateur ou d’un autre système.

Au sein d’un MAS, chaque agent possède des propriétés individuelles, mais tous se comportent de manière collaborative pour obtenir les propriétés globales souhaitées. Les systèmes multi-agents sont utiles pour effectuer des tâches complexes et de grande envergure qui peuvent impliquer des centaines, voire des milliers d’agents.

Les agents d’intelligence artificielle (IA) reflètent parfaitement ce principe. Un agent d’IA est un système ou un programme capable d’exécuter des tâches de manière autonome pour le compte d’un utilisateur ou d’un autre système en concevant son propre workflow et en utilisant les outils disponibles. Les agents d’IA reposent sur des grands modèles de langage (LLM). Ces agents intelligents exploitent les techniques avancées de traitement automatique du langage naturel des LLM pour comprendre les entrées de l’utilisateur et y répondre Les agents résolvent les problèmes étape par étape et déterminent quand il faut faire appel à des outils externes Ce qui différencie les agents d’IA des LLM traditionnels, c’est l’utilisation d’outils et la capacité à concevoir un plan d’action. Les outils dont dispose un agent peuvent inclure des jeux de données externes, des recherches sur le Web et des interfaces de programmation des applications (API). À l’instar de la prise de décision humaine, les agents d’IA peuvent également mettre à jour leur mémoire à mesure qu’ils acquièrent de nouvelles informations. Le partage d’informations, l’utilisation d’outils et l’apprentissage adaptatif permettent aux agents d’IA d’être plus polyvalents que les LLM traditionnels.

Pour en savoir plus sur les systèmes à agent unique, consultez notre contenu détaillé sur les agents d’IA.

## Systèmes mono-agents ou systèmes multi-agents

Les systèmes mono-agents intelligents interagissent avec leur environnement pour planifier, appeler les outils et produire des réponses de manière autonome. Les outils mis à la disposition d’un agent fournissent des informations qui ne sont pas disponibles pour l’agent autrement. Comme décrit précédemment, ces informations peuvent provenir d’une base de données acquise par le biais d’une API ou d’un autre agent. Il existe une distinction entre les systèmes mono-agents et multi-agents. Lorsqu’un autre agent est utilisé en tant qu’outil, cet agent secondaire fait partie des stimuli environnementaux de l’agent d’origine. Ces informations sont acquises et aucune autre coopération n’a lieu. En revanche, les systèmes multi-agents impliquent tous les agents de l’environnement pour modéliser les objectifs, la mémoire et le plan d’action de chacun. La communication entre les agents peut être directe ou indirecte en modifiant l’environnement partagé.

Chaque entité d’un système multi-agent est un agent autonome dans une certaine mesure. Cette autonomie est généralement visible par la planification de l’agent, l’appel des outils et le raisonnement général. Dans un système multi-agent, les agents restent autonomes, mais coopèrent et se coordonnent également dans des structures d’agents. Pour résoudre des problèmes complexes, la communication entre les agents et la résolution distribuée des problèmes sont essentielles. Ce type d’interaction entre agents peut être décrit comme l’apprentissage par renforcement multi-agent. Les informations partagées par cette forme d’apprentissage peuvent inclure des informations instantanées acquises par des capteurs ou des actions. De plus, les expériences d’un agent sous forme d’informations épisodiques peuvent être partagées. Ces épisodes peuvent être des séquences de sensations, d’actions et de politiques apprises. Enfin, les agents peuvent partager leurs expériences en temps réel pour éviter que d’autres agents n’apprennent de manière répétitive les mêmes politiques.

Les agents individuels sont puissants par eux-mêmes. Ils peuvent créer des tâches secondaires, utiliser des outils et apprendre grâce à leurs interactions. Le comportement collectif des systèmes multi-agents augmente le potentiel de précision, d’adaptabilité et d’évolutivité. Les systèmes multi-agents ont tendance à être plus performants que les systèmes mono-agents en raison du plus grand nombre de ressources partagées, de l’optimisation et de l’automatisation. Au lieu que plusieurs agents apprennent les mêmes politiques, l’expérience acquise est partagée pour optimiser la complexité temporelle et l’efficacité.

## Architectures des systèmes multi-agents

### Réseaux centralisés

Les systèmes multi-agents peuvent fonctionner selon différentes architectures. Dans les réseaux centralisés, une unité centrale contient la base de connaissances globale, relie les agents et supervise leurs informations. La force de cette structure réside dans la facilité de communication entre les agents et l’uniformité des connaissances. L’une des faiblesses de la centralité est la dépendance à l’égard de l’unité centrale : si elle est défaillante, c’est tout le système d’agents qui est défaillant.

### Réseaux décentralisés

Les agents des réseaux décentralisés partagent des informations avec leurs agents voisins au lieu d’une base de connaissances mondiale. Certains avantages des réseaux décentralisés sont la robustesse et la modularité. La défaillance d’un seul agent n’entraîne pas la défaillance de l’ensemble du système puisqu’il n’y a pas d’unité centrale. L’un des défis des agents décentralisés est de coordonner leur comportement pour qu’il soit bénéfique aux autres agents coopérants.

## Structures des systèmes multi-agents

Il existe également de nombreuses façons d’organiser les agents au sein d’un système multi-agent :

### Structure hiérarchique

Une structure hiérarchique est arborescente et contient des agents avec différents niveaux d’autonomie. Dans une structure hiérarchique simple, un seul agent peut avoir le pouvoir de décision. Dans une structure hiérarchique uniforme, la responsabilité peut être répartie entre plusieurs agents.

### Structure holonique

Dans ce type d’architecture, les agents sont regroupés en holarchies. Un holon est une entité qui ne peut pas fonctionner sans ses composants. Par exemple, le corps humain est un holon parce qu’il ne peut pas fonctionner sans organes fonctionnels. De même, dans les systèmes multi-agents holoniques, l’agent principal peut avoir plusieurs sous-agents tout en apparaissant comme une entité singulière. Ces sous-agents peuvent également jouer des rôles dans d’autres holons. Ces structures hiérarchiques sont auto-organisées et créées pour atteindre un objectif grâce à la collaboration des sous-agents.

### Structure de coalition

Les coalitions sont utiles lorsque les agents individuels ne sont pas performants dans un groupe. Dans ces situations, les agents s’unissent temporairement pour améliorer l’utilité ou les performances. Une fois la performance souhaitée atteinte, les coalitions sont distribuées. Il peut être difficile de maintenir ces coalitions dans des environnements dynamiques. Un regroupement est souvent nécessaire pour améliorer les performances.

### Équipes

Les équipes ont une structure similaire aux coalitions. En équipes, les agents coopèrent pour améliorer les performances du groupe. Les agents des équipes ne travaillent pas de manière indépendante, contrairement aux coalitions. Les agents d’équipe dépendent beaucoup plus les uns des autres et leur structure est plus hiérarchique que les coalitions.

## Comportements des systèmes multi-agents

Les comportements des agents au sein d’un système multi-agent reflètent souvent des comportements observés dans la nature. Les comportements suivants peuvent s’appliquer à la fois aux agents multilogiciels et aux agents multirobots.

#### Regroupement

Le comportement collectif observé dans les systèmes multi-agents peut ressembler à celui des oiseaux, des poissons et des humains. Dans ces systèmes, les agents partagent un objectif et nécessitent une certaine organisation pour coordonner leur comportement. Le regroupement se rapporte à la synchronisation directionnelle, et la structure de ces nuées peut être décrite par l’heuristique suivante :

- Séparation : essayer d’éviter les collisions avec les agents à proximité.
- Alignement : essayer d’atteindre la vitesse des agents à proximité.
- Cohésion : essayer de rester proche des autres agents.

Dans le contexte des agents logiciels, cette coordination est cruciale pour les systèmes multi-agents gérant des réseaux de transport tels que les systèmes ferroviaires.

#### Essaimage

Le positionnement spatial des agents dans un système multi-agent peut être comparé au phénomène d’essaimage qui se produit dans la nature. Par exemple, les oiseaux volent en synchronisation en s’adaptant aux oiseaux à proximité. D’un point de vue technique, l’essaimage est l’auto-organisation et l’agrégation émergentes parmi les agents logiciels avec un contrôle décentralisé. L’un des avantages de l’essaimage est qu’un opérateur peut être formé à gérer un essaim d’agents. Cette méthode est moins coûteuse en termes de calcul et plus fiable que de former un opérateur pour chaque agent.

### Cas d’utilisation des systèmes multi-agents

Les systèmes multi-agents peuvent résoudre de nombreuses tâches complexes du monde réel. Voici quelques exemples de domaines applicables :

Transports

Les systèmes multi-agents peuvent être utilisés pour gérer les systèmes de transport. Les qualités des systèmes multi-agents qui permettent la coordination de systèmes de transport complexes sont la communication, la collaboration, la planification et l’accès aux informations en temps réel. Parmi les systèmes distribués qui pourraient bénéficier d’un MAS, on trouve les systèmes ferroviaires, les affectations de camions et les navires maritimes visitant les mêmes ports.

Soins de santé et santé publique

Les systèmes multi-agents peuvent être utilisés pour diverses tâches spécifiques dans le domaine de la santé. Ces systèmes basés sur des agents peuvent aider à prédire et à prévenir les maladies grâce à des analyses génétiques. La recherche médicale sur le cancer pourrait être une application. En outre, les systèmes multi-agents peuvent servir d’outils pour prévenir et simuler la propagation des épidémies. Ces prévisions sont rendues possibles grâce à l’utilisation de réseaux neuronaux informés sur le plan épidémiologique et de techniques de machine learning (ML) pour gérer de grands jeux de données. Ces résultats peuvent avoir une incidence sur la santé publique et les politiques publiques.

Gestion de la chaîne d'approvisionnement

De nombreux facteurs ont un impact sur la chaîne d’approvisionnement. Ces facteurs vont de la création de biens à l’achat par le consommateur. Les systèmes multi-agents peuvent utiliser leurs vastes ressources informationnelles, leur polyvalence et leur évolutivité pour connecter les composants de la gestion de la chaîne d’approvisionnement. Pour utiliser au mieux cette automatisation intelligente, les agents conversationnels doivent négocier entre eux. Cette négociation est importante pour les agents qui collaborent avec d’autres agents ayant des objectifs contradictoires.

Systèmes de défense

Les systèmes multi-agents peuvent contribuer à renforcer les systèmes de défense. Les menaces potentielles peuvent inclure à la fois des problèmes physiques de sécurité nationale et des cyberattaques. Les systèmes multi-agents peuvent utiliser leurs outils pour simuler des attaques potentielles, par exemple une simulation d’attaque maritime. Ce scénario impliquerait que des agents travaillent en équipe pour identifier les interactions entre des bateaux terroristes en approche et des navires de défense. De plus, en travaillant en équipes, les agents peuvent surveiller différentes zones du réseau pour détecter les menaces entrantes telles que les attaques par déni de service distribué (DDoS).

## Avantages des systèmes multi-agents

Les systèmes multi-agents présentent plusieurs caractéristiques avantageuses, notamment :

### Flexibilité

Les systèmes multi-agents peuvent s’adapter à différents environnements en ajoutant, en supprimant ou en adaptant des agents.

### Évolutivité

La coopération de plusieurs agents permet de disposer d’un plus grand nombre d’informations partagées. Cette collaboration permet aux systèmes multi-agents de résoudre des problèmes et des tâches plus complexes que les systèmes mono-agents.

### Spécialisation dans un domaine

Les systèmes mono-agents nécessitent un agent pour effectuer des tâches dans divers domaines, tandis que chaque agent dans un système multi-agent peut détenir une expertise spécifique propre à un domaine.

### Performances accrues

Les cadres multi-agents ont tendance à surpasser les agents uniques. En effet, plus un agent dispose de plans d’action, plus il peut apprendre et réfléchir. Un agent d’IA qui intègre les connaissances et les retours d’autres agents d’IA spécialisés dans des domaines connexes peut être utile pour la synthèse d’informations. Cette collaboration en arrière-plan entre agents d’IA, ainsi que leur capacité à combler les lacunes en matière d’information, est propre aux cadres agentiques, en faisant un outil puissant et une avancée majeure dans l’intelligence artificielle.

## Défis liés aux systèmes multi-agents

La conception et la mise en œuvre de systèmes multi-agents posent plusieurs défis, notamment :

### Dysfonctionnements des agents

Les systèmes multi-agents construits sur les mêmes modèles de fondation peuvent partager des faiblesses. Ces faiblesses peuvent entraîner une défaillance à l’échelle du système de tous les agents concernés ou représenter des vulnérabilités face à des attaques. Cela souligne l’importance de la gouvernance des données dans la création de modèles de fondation et la nécessité de processus de formation et de test approfondis.

### Complexité de la coordination

L’un des plus grands défis de la création de systèmes multi-agents est de développer des agents qui peuvent se coordonner et négocier entre eux. Cette coopération est essentielle pour qu’un système multi-agent fonctionne.

### Comportement imprévisible

Les agents fonctionnant de manière autonome et indépendante dans les réseaux décentralisés peuvent avoir des comportements contradictoires ou imprévisibles. Dans ces conditions, il peut s’avérer difficile de détecter et de gérer les problèmes au sein d’un système plus vaste.
