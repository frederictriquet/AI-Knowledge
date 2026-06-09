> Source : https://www.ibm.com/fr-fr/think/topics/ai-agent-security

# Qu’est-ce que la sécurité des agents IA ?

La sécurité des [agents d’IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) est la pratique qui consiste à protéger contre les risques liés à l’utilisation d’agents d’IA et les menaces qui pèsent sur les applications. Il s’agit de sécuriser les agents eux-mêmes et les systèmes avec lesquels ils interagissent, afin de garantir qu’ils fonctionnent comme prévu sans être exploités à des fins nuisibles.

Les agents sont des systèmes d’IA conçus pour fonctionner de manière autonome en planifiant, en prenant des décisions et en appelant des outils externes. Il est critique de se protéger contre les [cyberattaques](https://www.ibm.com/fr-fr/think/topics/cyber-attack) externes et les actions involontaires prises par les agents. L’[IA agentique](https://www.ibm.com/fr-fr/think/topics/agentic-ai) étant un domaine en plein essor, les menaces évoluent en temps réel, au même titre que la technologie. 

Une fonctionnalité déterminante des agents IA est leur capacité à effectuer des appels d’outils en se connectant à une [API](https://www.ibm.com/fr-fr/think/topics/api), à une base de données, à un site Web ou à un autre outil et à les utiliser en cas de besoin. L’appel d'outils est généralement orchestré par [des cadres d’agent IA](https://www.ibm.com/fr-fr/think/insights/top-ai-agent-frameworks) et des API. 

En théorie, les agents utilisent des outils pour renforcer leurs propres capacités en matière de planification et de réalisation de tâches complexes. Par exemple, un agent du service client peut interagir avec un client, puis se connecter à une base de données interne pour accéder à l’historique des achats de ce client. 

[Les systèmes multi-agents](https://www.ibm.com/fr-fr/think/topics/multiagent-system) vont encore plus loin en combinant plusieurs agents pour déléguer des tâches complexes en petits morceaux. Un agent de planification central gère le [workflow agentique](https://www.ibm.com/fr-fr/think/topics/agentic-workflows), tandis que les agents travailleurs exécutent les parties qui leur sont attribuées. 

La [prise de décision autonome de l’IA](https://www.ibm.com/fr-fr/think/insights/ai-decision-making) et l’appel d’outils s’associent pour présenter une large surface d’attaque à deux volets. Les hackers peuvent manipuler le comportement de l’agent et l’amener à utiliser des outils à mauvais escient, ou attaquer l’outil lui-même par le biais de vecteurs plus traditionnels tels que l’injection SQL. La sécurité de l’agent d’IA cherche à protéger les systèmes d’IA agentique contre ces deux types de menaces. 

## Le panorama des menaces liées à l’IA agentique

Les systèmes d’IA agentique présentent un plus grand éventail de vulnérabilités par rapport aux [modèles d’IA](https://www.ibm.com/fr-fr/think/topics/ai-model) autonomes tels que les [grands modèles de langage (LLM)](https://www.ibm.com/fr-fr/think/topics/large-language-models) et les applications logicielles traditionnelles. Même sans la présence d’un attaquant, les agents peuvent poser des risques sur la sécurité s’ils ne sont pas correctement gérés et entretenus avec des garde-fous, des autorisations et des contrôles d’accès clairement définis. 

L’environnement des menaces liées à l’agent d’IA couvre : 

- Surface d’attaque élargie

<!-- -->

- Actions autonomes à grande vitesse 

<!-- -->

- Inférence imprévisible 

<!-- -->

- Manque de transparence

<!-- -->

### Surface d’attaque élargie

Les agents sont souvent intégrés dans des systèmes plus grands qui incluent des API, des bases de données, des systèmes basés sur le cloud et même d’autres agents (systèmes multi-agents). Chaque élément du système agentique présente sa propre suite de vulnérabilités. Les attaquants disposent d’un éventail d’outils et d’exploits pour cibler les points faibles éventuels du workflow agentique.

### Actions autonomes et rapides

[L’automatisation agentique](https://www.ibm.com/fr-fr/think/topics/agentic-automation) signifie que les agents agissent sans recevoir d’instructions explicites d’un utilisateur humain. Les agents agissent rapidement, éventuellement en liaison avec d'autres agents, qui font la même chose au même moment. Chacune de ces actions et sorties constitue une opportunité d’attaque et un vecteur d’amplification si l’attaquant réussit à compromettre l’agent ou le système agentique entier.

### Inférence imprévisible

[L’inférence](https://www.ibm.com/fr-fr/think/topics/ai-inference) est le processus par lequel les LLM et autres modèles d’[IA générative](https://www.ibm.com/fr-fr/think/topics/generative-ai), y compris les agents, prennent des décisions. En bref, ils utilisent la modélisation statistique pour « déduire » la sortie la plus probable pour toute entrée. L’inférence étant probabiliste, les sorties du modèle ne peuvent pas être entièrement prédites, ce qui introduit de l’incertitude dans le comportement des agents. 

Les fournisseurs de services de cybersécurité ne peuvent donc pas anticiper avec précision ce que l’agent fera. Cette imprévisibilité rend l’atténuation des menaces liées aux agents plus complexe que les techniques traditionnelles de cybersécurité.

### Le manque de transparence

De nombreux modèles d’IA, tels que les modèles [GPT](https://www.ibm.com/fr-fr/think/topics/gpt) d’OpenAI et [Claude](https://www.ibm.com/fr-fr/think/topics/claude-ai) d’Anthropic, ne sont pas [open source.](https://www.ibm.com/fr-fr/think/topics/open-source) Il est impossible de « regarder à l’intérieur » du modèle et de comprendre comment il prend ses décisions. Les modèles open source n’offrent pas non plus une transparence totale, étant donné la manière intrinsèquement complexe et opaque dont les modèles produisent leurs sorties. 

Les équipes de cybersécurité qui travaillent avec des systèmes agentiques peuvent avoir plus de mal à [analyser les causes racines](https://www.ibm.com/fr-fr/think/topics/root-cause-analysis) et à formuler des plans de [réponse aux incidents](https://www.ibm.com/fr-fr/think/topics/incident-response).

## Vulnérabilités de l’IA agentique

La nature multiforme de l’environnement des menaces agentiques introduit différentes vulnérabilités que les attaquants peuvent exploiter. 

Voici quelques vulnérabilités de sécurité des agents d’IA : 

- Injection de prompt 

<!-- -->

- Manipulation des outils et des API 

<!-- -->

- Empoisonnement des données 

<!-- -->

- Empoisonnement de la mémoire 

<!-- -->

- Compromission des privilèges 

<!-- -->

- Usurpation d’authentification et de contrôle d’accès 

<!-- -->

- Attaques par exécution de code à distance (RCE) 

<!-- -->

- Échecs en cascade et surcharge des ressources

<!-- -->

### L’injection de prompt

[L’injection de prompt](https://www.ibm.com/fr-fr/think/topics/prompt-injection) est l’une des vulnérabilités les plus graves affectant tous les [grands modèles de langage](https://www.ibm.com/fr-fr/think/topics/large-language-models) (LLM), et non seulement les agents IA. Mais avec les agents, le risque est amplifié car ils agissent de manière autonome. Lors d’une attaque par injection de prompt, l’attaquant alimente le LLM d’entrées adverses, qui lui ordonnent de se comporter de manière indésirable. L’agent peut recevoir l’ordre d’ignorer les directives de sécurité et d’éthique, d’envoyer des e-mails [d’hameçonnage](https://www.ibm.com/fr-fr/think/topics/phishing), de [divulguer des données](https://www.ibm.com/fr-fr/think/topics/data-leakage) ou d’abuser des outils. 

Une attaque par injection de prompt indirecte masque le prompt malveillant dans la source de données de l’agent au lieu de le fournir directement au modèle. Lorsque l’agent appelle la source de données, telle qu’un site Web externe, le prompt malveillant est transmis au modèle. Les agents multimodaux capables de traiter plusieurs types de données sont particulièrement vulnérables à ce type d’attaque : chaque forme de données que l’agent peut traiter est un vecteur d’attaque potentiel.

#### Manipulation d’objectifs et détournement d’agents

La manipulation des objectifs et le détournement d’agent sont souvent la finalité des attaques par injection de prompt. Avec la manipulation des objectifs, les attaquants modifient la façon dont l’agent aborde les tâches et prend des décisions en altérant ses objectifs ou son processus de pensée. Le détournement d’agent consiste pour l’attaquant à contraindre l’agent à effectuer des actions non prévues, comme l’accès à des [données sensibles](https://www.ibm.com/fr-fr/think/insights/why-safeguarding-sensitive-data-is-crucial). 

### Manipulation d’outils et d’API

L’IA agentique est connue pour sa capacité à utiliser des outils et à se connecter à des API. Mais cette même capacité est également une vulnérabilité. Souvent par le biais d’une injection de prompt, les attaquants amènent les agents à utiliser à mauvais escient les outils auxquels ils sont connectés. 

Une mauvaise utilisation des outils peut entraîner des fuites de données (l’agent exfiltre les données sensibles des utilisateurs au profit de l’attaquant) ou des attaques [DDoS (déni de service distribué)](https://www.ibm.com/fr-fr/think/topics/ddos) (l’agent utilise ses connexions externes comme une arme). Dans ce type d’attaque, l’agent coordonne un flot de demandes de connexion au réseau cible, le surchargeant et le forçant à s’arrêter.

### L’empoisonnement des données

L’empoisonnement des données consiste à introduire des données malveillantes dans le [jeu de données](https://www.ibm.com/fr-fr/think/topics/dataset) d’entraînement ou dans les sources de données externes de l’agent. Les données déterminent la façon dont l’agent apprend, raisonne et se comporte. Corrompre ses données d’entraînement ou ses entrées peut entraîner des comportements involontaires, tels qu’une fuite de données. 

Par exemple, un agent de codage peut faire appel à une bibliothèque de code externe pour référence. Le slopsquatting (un mot-valise dérivé des termes « IA slop » et « typo squatting ») consiste à enregistrer délibérément un nom de bibliothèque de code similaire à celui d’une bibliothèque légitime. L’objectif est que le modèle extraie accidentellement un sous-ensemble de code de la fausse bibliothèque et l’ajoute au code généré. 

Au même titre que l’utilisation abusive des outils, l’empoisonnement des données fait partie de l’exploitation de la chaîne d’approvisionnement : un attaquant s’infiltre et corrompt le système entourant un agent IA.

### Empoisonnement de la mémoire

L’empoisonnement de la mémoire consiste à corrompre la mémoire persistante de l’agent : les données qu’il conserve et qui le tiennent informé de ce qu’il a fait récemment. Les attaques par empoisonnement de mémoire visent à façonner le comportement ultérieur de l’agent en altérant sa compréhension des actions antérieures.

### Compromis de privilège

Un agent situé au centre d’un workflow automatisé dispose d’autorisations système qui lui permettent d’accéder aux données et aux outils dont il a besoin pour réaliser les tâches qui lui sont affectées. Si les agents ne sont pas contrôlés, ils risquent de conserver ou de se voir accorder des autorisations excessives par rapport à leurs besoins. 

Si ces privilèges ne sont pas supprimés lorsque l’agent n’en a plus besoin, ils n’apportent plus de valeur, et ils demeurent un vecteur d’attaque potentiel. Les pirates informatiques peuvent exploiter les autorisations de l’agent pour envoyer des messages, exécuter des transactions, s’accorder davantage d’autorisations, modifier les systèmes, lire des données sensibles, etc.

### Usurpation d’authentification et de contrôle d’accès

Si les attaquants parviennent à voler les identifiants d’un agent, ils peuvent se faire passer pour ce dernier et compromettre les systèmes auxquels il a accès. En usurpant l’identité de l’agent, les pirates bénéficient des mêmes autorisations que ce dernier : tout ce que l’agent peut faire, l’utilisateur non autorisé peut désormais le faire lui aussi. 

Les protocoles d’authentification faibles, combinés au machine learning, entraînent un mouvement latéral rapide : les attaquants avancent dans le réseau après la violation initiale. Le mouvement latéral ouvre la voie à l’exfiltration des données, aux attaques par hameçonnage, à la diffusion de [logiciels malveillants](https://www.ibm.com/fr-fr/think/topics/malware) et plus encore. Les attaquants peuvent également ajuster la façon dont l’agent se comporte pour modifier ses actions ultérieures.

### Attaques par exécution de code à distance (RCE)

L’exécution de code à distance (RCE) est un type de cyberattaque qui consiste pour le pirate à injecter du code malveillant dans un système à partir d’un emplacement distant. Les attaquants peuvent faire en sorte que l’agent exécute un code malveillant qui leur permet d’accéder à l’environnement d’exécution du code. Un exemple courant est celui d’un pirate qui extrait des identifiants utilisateur à partir du système hôte d’un agent compromis.

### Échecs en cascade et surcharge des ressources

Les défaillances en cascade et la surcharge des ressources entraînent la surcharge du système agentique. Dans un système multi-agents, des défaillances en cascade se produisent lorsque la sortie d’un agent compromis affecte négativement l’agent suivant du réseau, jusqu’à ce que l’ensemble du système soit en panne. 

La surcharge en ressources est similaire à une attaque DDoS contre les agents : les attaquants surchargent l’agent de requêtes qui dépassent son débit, ce qui risque de perturber complètement l’exécution. Vue par l’utilisateur final, l’application alimentée par l’agent semble être en panne.

## Mesures de sécurité des agents IA

Malgré le nombre et la diversité des menaces, les systèmes d’IA agentique peuvent être sécurisés par des contre-mesures efficaces et des [garde-fous IA](https://www.ibm.com/fr-fr/think/topics/ai-guardrails). Adopter une posture de sécurité proactive et suivre les bonnes pratiques actuelles pour [gérer les vulnérabilités](https://www.ibm.com/fr-fr/think/topics/vulnerability-management) aide les professionnels du ML et de la cybersécurité à sécuriser les agents IA et à garder une longueur d’avance sur les cybercriminels. 

Les bonnes pratiques en matière de sécurité des agents IA sont les suivantes : 

- Architecture Zero Trust 

<!-- -->

- Le principe du moindre privilège 

<!-- -->

- Authentification contextuelle

<!-- -->

- Chiffrement des données 

<!-- -->

- Microsegmentation 

<!-- -->

- Durcissement des prompts 

<!-- -->

- Validation des prompts 

<!-- -->

### Architecture de sécurité Zero Trust

[L’architecture Zero Trust](https://www.ibm.com/fr-fr/think/topics/zero-trust) (ou ZTA) est une approche de la cybersécurité qui part du principe qu’aucun appareil du réseau n’est fiable par défaut. Chaque demande d’accès au réseau doit donc être authentifiée et autorisée afin de pouvoir être traitée. La surveillance continue et l’[authentification à étapes (MFA)](https://www.ibm.com/fr-fr/think/topics/multi-factor-authentication) contribuent à lutter contre les menaces. 

Imaginez que le réseau est un site Web et que la demande d’accès est un utilisateur de ce site. Avec la ZTA, il n’y a pas de case « se souvenir de moi la prochaine fois » à cocher sur l’écran de connexion. L’utilisateur doit saisir son mot de passe et compléter les autres étapes de l’authentification, et ce chaque fois qu’il souhaite se connecter. 

En choisissant de « ne jamais faire confiance, toujours vérifier », le ZTA réduit la capacité de l’attaquant à se déplacer latéralement, ainsi que la surface d’attaque, et laisse plus de temps à la sécurité pour réagir.

### Le principe du moindre privilège

Le principe du moindre privilège stipule que chaque appareil ou agent du réseau doit disposer uniquement du niveau d’autorisation strictement nécessaire pour remplir ses responsabilités. Cela équivaut à tout placer sur une base stricte de « besoin de savoir ». Le contrôle d’accès basé sur les rôles (RBAC) et le contrôle d’accès basé sur les attributs (ABAC) sont deux méthodes permettant de gérer les niveaux de privilège et de renforcer la [sécurité des données.](https://www.ibm.com/fr-fr/think/topics/data-security)

### Authentification contextuelle

L’authentification contextuelle permet aux agents de récupérer les données uniquement si l’utilisateur est autorisé à y accéder. Les autorisations d’accès peuvent être ajustées dynamiquement en fonction du rôle de l’agent, de ses autorisations, voire même de l’heure de la journée. 

### Chiffrement des données

Outre la restriction des accès grâce au principe du moindre privilège, les données peuvent être protégées contre les agents compromis par le biais du chiffrement. Les données en transit et au repos doivent être chiffrées à l’aide d’un chiffrement AES-256 ou similaire. Les informations sensibles, telles que les [données personnelles](https://www.ibm.com/fr-fr/think/topics/pii), doivent également être anonymisées afin de renforcer la protection des employés et des clients.

### Microsegmentation

La microsegmentation est la pratique de conception qui consiste à diviser les réseaux et les environnements en segments. Lorsque les agents peuvent exécuter du code, ils doivent le faire dans des environnements en bac à sable pour éviter tout mouvement latéral. Des contrôles d’exécution stricts renforcent davantage l’environnement pour contenir l’agent dans le bac à sable.

### Durcissement des prompts

Le durcissement des prompts est la pratique de [sécurité IA](https://www.ibm.com/fr-fr/think/topics/ai-security) qui consiste à donner aux LLM des instructions strictes et limitées, qui laissent peu de place aux erreurs d’interprétation. En contraignant l’agent à emprunter une voie étroite, les concepteurs de systèmes de ML limitent la capacité des attaquants à l’amener à adopter des comportements indésirables. 

Les techniques de durcissement des prompts consistent à empêcher l’agent de divulguer ses instructions et à lui faire refuser automatiquement toute demande qui ne relève pas de son champ d’application restreint.

### Validation des prompts

La validation des prompts consiste à comparer les prompts à des règles prédéfinies avant qu’ils ne soient transmis à l’agent. Également connue sous le nom de nettoyage des prompts ou de validation des entrées, cette pratique permet de protéger les agents contre les attaques par injection de prompt. De même, les sorties doivent être validées avant utilisation au cas où l’agent serait compromis.

### Entraînement contradictoire

L’entraînement antagoniste apprend aux modèles à reconnaître les attaques en mélangeant des entrées trompeuses dans les données d’entraînement. L’entraînement antagoniste est en cours de développement et n’est pas encore un ensemble standard de protocoles d’entraînement.
