> Source : https://www.ibm.com/fr-fr/think/insights/ai-agent-ethics

# De nouveaux risques éthiques liés aux agents d’IA ? Les chercheurs se penchent sur la question

Lorsque les systèmes d’IA deviennent incontrôlables, les résultats ne sont pas beaux à voir. Des fuites d’informations confidentielles, des messages insultants et, dans un cas, une recette simple pour confectionner du chlore gazeux mortel ont tous été imputés à des chatbots qui ont mal tourné.1

Ces cas ont conduit à mettre davantage l’accent sur l’alignement de l’IA, qui consiste à encoder les valeurs humaines et les principes éthiques dans les modèles IA. Mais les chercheurs en IA ne se contentent pas d’étudier les implications éthiques des technologies de machine learning actuelles. Ils s’efforcent également de répondre aux questions éthiques de demain, en particulier celles posées par l’intelligence artificielle agentique.

Également appelée agents IA, l’IA agentique est une technologie autonome qui présente un ensemble élargi de dilemmes éthiques par rapport aux modèles IA, comme l’explique Kush Varshney, IBM Fellow chez IBM Research.

« Comme les agents d’IA peuvent agir sans votre supervision, de nombreux problèmes de confiance supplémentaires se posent. », dit-il. « La situation va évoluer en termes de capacités, mais aussi de conséquences imprévues. Du point de vue de la sécurité, il faut y travailler dès maintenant. Il est important de continuer à renforcer les mesures de protection à mesure que la technologie progresse. »

## Que sont exactement les agents IA ?

Avant d’aborder les mesures de protection des agents IA, il est important de comprendre exactement ce qu’ils sont : des systèmes ou des programmes intelligents qui peuvent effectuer des tâches de manière autonome pour le compte d’un être humain ou d’un autre système. Alors qu’ils présentent des capacités de grand modèle de langage (LLM) comme le traitement automatique du langage naturel, ces systèmes autonomes peuvent aussi prendre des décisions, résoudre des problèmes, exécuter des actions et interagir avec des environnements externes.

Dotés de ces capacités, les agents d’IA peuvent aller au-delà de la création de réponses textuelles aux prompts utilisateur et accomplir des tâches dans le monde réel.

Par exemple, les interactions externes se font via l’appel d’outil, également appelé appel de fonction, une interface qui permet aux agents de travailler sur des tâches qui nécessitent des informations opportunes, lesquelles seraient autrement indisponibles pour les LLM. Ainsi, les agents IA déployés dans un écosystème de chaîne d’approvisionnement pourraient travailler de manière autonome sur l’optimisation des niveaux de stock en modifiant les calendriers de production et en passant des commandes auprès des fournisseurs si nécessaire.

## Quel est le risque d’une plus grande autonomie de l’IA ?

Lorsqu’il s’agit d’intelligence artificielle avancée comme l’IA agentique, à quel moment l’autonomie devient-elle excessive ? Pour répondre à cette question, nous pouvons nous appuyer sur le scénario de l’optimiseur de trombone. Le célèbre exercice mental du philosophe Nick Bostrom se concentre sur le concept encore hypothétique de superintelligence de l’IA ou ASI, un système d’IA doté de capacités intellectuelles qui dépassent celles de l’intelligence humaine. Nick Bolstrom réfléchit à ce qui pourrait se produire si un tel système privilégiait la fabrication de trombones avant tout autre objectif.

Dans le scénario proposé, le système finirait par consacrer toutes les ressources de notre planète à la fabrication de trombones, un résultat contraire à l’éthique lorsque la vie dépend de plus qu’une quantité infinie de minuscules fournitures de bureau en métal. Pour en revenir à notre question, nous pouvons évidemment conclure que, dans cette hypothèse, le système d’IA en question aurait eu trop d’autonomie.

La bonne nouvelle, c’est que l’IA agentique d’aujourd’hui n’est pas la même chose que l’ASI, de sorte qu’une dystopie de trombone motivée par une éthique de machine catastrophiquement défectueuse reste peu probable. « Nous sommes plus proches, mais nous en sommes encore loin », observe M. Varshney.

D’autres risques liés à l’automatisation de l’IA sont toutefois plus imminents. Les possibilités vont des agents artificiels envoyant des e-mails inappropriés à l’arrêt et au démarrage de machines d’une manière que les utilisateurs n’avaient pas prévue, dit-il. Les inquiétudes concernant le comportement autonome de l’IA sont suffisamment sérieuses pour que, dans un rapport d’avril 2024 sur les directives de sûreté et de sécurité de l’IA, le Département de la sécurité intérieure des États-Unis (DHS) ait inscrit « l’autonomie » dans sa liste de risques pour les systèmes d’infrastructure critiques tels que les communications, les services financiers et les soins de santé.2

## Des solutions évolutives pour soutenir le comportement éthique des agents

Les solutions de gouvernance de l’IA existantes peuvent contribuer à l’éthique des agents IA, tandis que des outils logiciels permettent déjà aux organisations de surveiller, d’évaluer et de corriger les biais issus des jeux de données d’entraînement et  des algorithmes susceptibles de fausser les processus de prise de décision. Ces solutions peuvent aussi aider les développeurs et les entreprises à s’assurer que les outils d’IA qu’ils utilisent répondent aux normes d’une IA de confiance, aux objectifs d’explicabilité et aux principes d’IA responsable largement adoptés par diverses entreprises et gouvernements.

Mais alors que les entreprises intègrent de plus en plus l’IA agentique dans leurs workflows, les chercheurs travaillent également sur de nouvelles solutions et stratégies d’IA éthique qui peuvent limiter les mauvais comportements des agents autonomes et améliorer la durabilité de la technologie de l’IA. En voici quelques-unes qui méritent d’être étudiées :

### Une nouvelle approche de l’alignement de l’IA

Aujourd’hui, les modèles IA pré-entraînés font l’objet d’un réglage précis pour être entraînés sur des données spécifiques à un domaine. Au cours de la phase de réglage fin du développement de l’IA, les modèles peuvent être alignés sur les valeurs morales et les considérations éthiques, mais des questions se posent souvent quant aux valeurs normatives à inclure. Après tout, les valeurs et les cadres éthiques varient selon l’entreprise, le pays, le groupe de parties prenantes, etc.

Kush Varshney et une équipe de chercheurs IBM ont proposé une approche axée sur la technologie qui serait plus spécifique au contexte : connue sous le nom d’Alignment Studio, elle aligne les grands modèles de langage sur les règles et les valeurs décrites dans les documents de politique en langage naturel, tels que les réglementations gouvernementales ou les propres directives éthiques d’une entreprise.

Présentée dans un article publié en septembre 2024 dans le magazine IEEE Internet Computing, l’approche comprend un cycle continu de développement afin que les modèles n’apprennent pas seulement le vocabulaire lié aux politiques à partir des documents associés, mais adoptent réellement les comportements souhaités pour un meilleur alignement des valeurs.3

### Détection des hallucinations associées aux appels de fonction

Parmi les causes des mauvais comportements liés aux agents d’IA, citons le manque d’instructions spécifiques de la part de l’utilisateur ou une mauvaise interprétation de ces instructions par l’agent. De tels « malentendus » peuvent conduire les agents à choisir les mauvais outils ou à les utiliser de manière inappropriée ou préjudiciable, ce que l’on appelle une hallucination d’appel de fonction.

Heureusement, l’amélioration des appels de fonction est devenue une activité concurrentielle, avec la création de plusieurs critères de référence mesurant la capacité des LLM à appeler les API. L’une des améliorations les plus récentes est apportée par une nouvelle fonctionnalité de la dernière version d’IBM Granite Guardian, Granite Guardian 3.1, qui fait partie de la famille de modèles de langage Granite d’IBM spécialement conçus pour les entreprises. Le modèle est capable de détecter les hallucinations d’appel de fonction par les agents avant que des conséquences imprévues ne se produisent. « Le détecteur recherche toutes sortes d’erreurs, de la description en langage humain à la fonction appelée », explique M. Varshney.

### Détection des textes générés par l’IA et désinformation

Des acteurs malveillants ont déjà utilisé l’IA générative pour infiltrer les réseaux sociaux avec des deepfakes, qui sont des fichiers audio, vidéo ou images réalistes générés par l’IA et capables de recréer l’image d’une personne. Dans le même temps, des escrocs tiraient parti de textes générés par l’IA pour envoyer des e-mails de phishing plus sophistiqués. La puissance de l’IA agentique pourrait encore aggraver ces tendances dangereuses.

« Il devient évident que les résultats générés par l’IA sont aussi convaincants que les arguments humains », ont averti les chercheurs de Google DeepMind dans un rapport d’avril 2024. Selon eux, à l’avenir, les acteurs malveillants pourraient utiliser l’IA autonome pour « adapter des contenus de désinformation auprès des utilisateurs de manière hyperprécise, en exploitant leurs émotions et leurs vulnérabilités ».4.

À ce jour, les performances des outils conçus pour détecter les tromperies alimentées par l’IA sont mitigées. Mais les chercheurs continuent de relever le défi d’améliorer la détection de l’IA, certains des résultats les plus prometteurs provenant de la dernière génération de détecteurs de texte IA.5

Par exemple, un nouveau cadre des exigences appelé RADAR, créé par des chercheurs de l’Université chinoise de Hong Kong et d’IBM Research, utilise l’apprentissage contradictoire entre deux modèles de langage distincts et réglables pour entraîner un détecteur de texte IA, qui améliore les performances par rapport aux anciennes solutions de détection de texte.6

Alors que la technologie de détection de l’IA continue de progresser, des entreprises technologiques comme IBM, Microsoft et OpenAI appellent également les décideurs politiques à adopter des lois pour cibler la distribution de deepfakes et tenir les mauvais acteurs responsables.7

### Préserver la dignité des travailleurs humains

Si de nombreuses considérations éthiques liées à l’IA agentique concernent les mauvais comportements, d’autres questions de cet ordre se posent même lorsque la technologie de l’IA autonome fonctionne comme prévu. Par exemple, de nombreuses discussions ont porté sur les applications d’IA comme ChatGPT d’OpenAI qui remplacent le travail humain et suppriment les moyens de subsistance.

Cependant, même lorsque l’IA est déployée pour augmenter (plutôt que de remplacer) le travail humain, les employés risquent d’en subir les conséquences sur le plan psychologique. Comme l’explique Kush Varshney, si les travailleurs humains perçoivent les agents d’IA comme plus performants qu’eux, leur estime de soi peut diminuer. « Si vous vous trouvez dans une situation où votre expertise semble inutile – comme subordonnée à l’agent d’IA – vous risquez de perdre votre dignité », dit-il. Dans certains débats autour de l’éthique de l’IA, une telle perte de dignité est considérée comme une violation des droits humains.8

Dans un article de recherche d’août 2024, Kush Varshney et plusieurs chercheurs universitaires ont proposé une approche organisationnelle pour répondre au problème de la dignité : la collaboration contradictoire. Selon leur modèle, les humains auraient toujours la responsabilité de fournir les recommandations finales, tandis que les systèmes d’IA seraient déployés pour analyser le travail des humains.

« En fin de compte, l’humain prend la décision finale ; l’algorithme n’est pas conçu pour rivaliser dans ce rôle, mais pour interroger et, par conséquent, affiner les recommandations de l’agent humain », écrivent les chercheurs.9 Une telle collaboration contradictoire « est une façon d’organiser les choses qui peuvent préserver la dignité humaine », explique Kush Varshney.
