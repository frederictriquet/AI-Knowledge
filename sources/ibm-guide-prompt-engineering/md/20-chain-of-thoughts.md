> Source : https://www.ibm.com/fr-fr/think/topics/chain-of-thoughts

# Qu’est-ce que le prompting par chaîne de pensée (CoT) ?

##

La chaîne de pensée (CoT) est une technique de [prompt engineering](https://www.ibm.com/fr-fr/think/topics/prompt-engineering) qui améliore les résultats des grands modèles de langage ([LLM](https://www.ibm.com/fr-fr/think/topics/large-language-models)), en particulier pour les tâches complexes impliquant un raisonnement en plusieurs étapes. Elle facilite la résolution de problèmes en guidant le modèle à travers un processus de raisonnement par étapes à l’aide d’une série cohérente d’étapes logiques. 

Le prompt engineering est employé en [intelligence artificielle](https://www.ibm.com/fr-fr/think/topics/artificial-intelligence) pour affiner les entrées (prompts) afin d’obtenir les résultats les plus précis possibles. Cette étude présente le concept de prompting par chaîne de pensée, qui suscite le raisonnement dans les LLM.[1](#f1) Elle soutient que le fait d’inciter les modèles à générer des étapes de raisonnement intermédiaires améliore considérablement leur capacité à résoudre avec précision des problèmes à plusieurs étapes, tels que le raisonnement arithmétique, le raisonnement symbolique et le raisonnement basé sur le bon sens. 

Les chercheurs se sont inspirés de la capacité des LLM à « penser à voix haute » en langage naturel, notant que plus la taille des paramètres augmentait, plus la capacité de raisonnement et la précision s’amélioraient. C’est pourquoi l’apprentissage CoT est considéré comme une capacité émergente, c’est-à-dire une capacité qui apparaît à mesure que la taille ou la complexité du modèle augmente. Les grands LLM ont tendance à être plus performants car ils ont appris de modèles de raisonnement plus nuancés grâce à leur entraînement sur des jeux de données massifs. 

Cependant, l’augmentation de la taille du modèle n’est pas le seul moyen d’améliorer la précision de la résolution de problèmes dans divers benchmarks. Les progrès réalisés dans le domaine du [réglage des instructions](https://www.ibm.com/fr-fr/think/topics/instruction-tuning) ont permis à des modèles plus petits d’effectuer le raisonnement CoT. Les modèles IBM Granite Instruct, par exemple, sont affinés à l’aide de jeux de données spécialisés composés de prompts et d’exemples adaptés aux tâches CoT. Un exemple de référence est un exemple de prompt que le modèle utilise comme moyen idéal pour répondre.

## Pourquoi le prompting CoT est-il efficace ?

Le prompting par chaîne de pensée simule des processus de raisonnement humains en décomposant des problèmes complexes en étapes intermédiaires gérables qui mènent séquentiellement à une réponse concluante.[2](#f2) Cette structure de résolution de problèmes étape par étape vise à garantir que le processus de raisonnement est clair, logique et efficace.

Dans les formats de prompt standard, la sortie du modèle est généralement une réponse directe à l’entrée fournie. Par exemple, si l’on fournit un prompt d’entrée demandant « De quelle couleur est le ciel ? », l’IA générera une réponse simple et directe, telle que « Le ciel est bleu ». 

Cependant, si on lui demande d’expliquer pourquoi le ciel est bleu à l’aide du prompting CoT, l’IA commencerait par définir ce que signifie « bleu » (une couleur primaire). Elle en déduirait ensuite que le ciel apparaît bleu en raison de l’absorption des autres couleurs par l’atmosphère. Cette réponse démontre la capacité de l’IA à construire un raisonnement logique.

L’utilisateur inclut généralement des instructions à la fin du prompt créé. Ces instructions peuvent être, par exemple, « décrivez vos étapes de raisonnement » ou « expliquez votre réponse étape par étape ». En substance, cette technique de prompting demande au LLM non seulement de générer un résultat, mais aussi de détailler la série d’étapes intermédiaires qui ont conduit à cette réponse.[3](#f3)

Le [prompt chaining](https://www.ibm.com/fr-fr/think/topics/prompt-chaining) est une autre méthode populaire utilisée dans les applications d’IA générative pour améliorer la fiabilité en utilisant plusieurs prompts qui s’appuient les uns sur les autres de manière séquentielle afin de décomposer des tâches complexes. Des techniques telles que le prompt chaining et la CoT guident le modèle pour qu’il raisonne étape par étape plutôt que de sauter à une réponse qui semble simplement correcte. Cette méthode peut également être utile pour l’observabilité et le débogage, car elle encourage le modèle à être plus transparent dans son raisonnement. La principale différence entre ces méthodes réside dans le fait que le prompt chaining enchaîne plusieurs prompts pour décomposer les tâches étape par étape, tandis que la CoT suscite le processus de raisonnement du modèle à l’aide d’un seul prompt.

## Comment fonctionne le prompting par chaîne de pensée ?

Le prompting par chaîne de pensée s’appuie sur de grands modèles de langage (LLM) pour articuler une succession d’étapes de raisonnement, orientant ainsi le modèle vers la génération de chaînes de raisonnement analogues pour de nouvelles tâches. Pour ce faire, des prompts basés sur des exemples illustrent le processus de pensée, améliorant ainsi la capacité du modèle à relever des défis complexes en termes de raisonnement.[4](#f4) Le flux de cette technique de prompting se comprend en résolvant le problème inhérent à un concept mathématique connu, la résolution d’une équation polynomiale.

### Exemple : comment le prompting par chaîne de pensée fonctionne-t-il pour résoudre les équations polynomiales ?

Le prompting par chaîne de pensée (CoT) peut aider de manière significative à résoudre des équations polynomiales en guidant un LLM pour qu’il suive une série d’étapes logiques, décomposant ainsi le processus de résolution des problèmes.[5](#f5) Examinons comment le prompting CoT parvient à résoudre une équation polynomiale.

Prenons l’exemple de la résolution d’une équation du second degré.

**Prompt d’entrée** : Résoudre l’équation du second degré : **x2 - 5x + 6 = 0**

Lorsque nous soumettons ce prompt au chat [IBM watsonx.ai](https://www.ibm.com/fr-fr/products/watsonx-ai), nous pouvons voir la conversation suivante entre la question humaine et la réponse de l’assistance basée sur l’IA.

Pour générer ce type de résultat, les principes fondamentaux du CoT fonctionnent comme illustré dans l’image ci-dessous. La réponse finale de la chaîne de pensée sera « Les solutions de l’équation **x2 – 5x + 6 = 0** sont **x = 3** et **x = 2**. »

## Variantes de la chaîne de pensée

Le prompting par chaîne de pensée (CoT) a donné vie à diverses variantes innovantes, chacune répondant à des défis spécifiques et améliorant les capacités de raisonnement du modèle de manière unique. Ces adaptations permettent non seulement d’étendre l’applicabilité de la CoT à différents domaines, mais aussi d’affiner le processus de résolution de problèmes du modèle.[6](#f6)

### Chaîne de pensées zero-shot

La variante de la chaîne de pensée zero-shot exploite les connaissances inhérentes aux modèles pour résoudre les problèmes sans exemples spécifiques ni affinement pour la tâche à accomplir. Cette approche est particulièrement utile face à des problèmes nouveaux ou diversifiés où des données d’entraînement sur mesure ne sont pas disponibles.[7](#f7) Cette approche peut tirer parti des propriétés du prompting standard et de l’apprentissage few-shot.

Par exemple, lorsqu’on répond à la question « Quelle est la capitale d’un pays limitrophe de la France dont le drapeau est rouge et blanc ? », un modèle utilisant la CoT zero-shot s’appuierait sur ses connaissances de la géographie et des drapeaux pour déduire les étapes menant à la Suisse (la réponse), bien qu’elle n’ait pas été entraînée de manière formelle sur de telles requêtes.

### Chaîne de pensées automatique

L’objectif de la chaîne de pensées automatique (auto-CoT) est de minimiser le travail manuel dans l’élaboration des prompts en automatisant la génération et la sélection de processus de raisonnement efficaces. Cette variante améliore l’évolutivité et l’accessibilité du prompting CoT pour un plus large éventail de tâches et d’utilisateurs.[8](#f8), [9](#f9)

Par exemple, pour résoudre un problème mathématique comme « Si vous achetez 5 pommes et que vous en avez déjà 3, combien en avez-vous au total ? », un système auto-CoT peut générer automatiquement des étapes intermédiaires, telles que « Commencer avec 3 pommes » et « Ajouter 5 pommes aux 3 existantes », aboutissant à « Total du nombre de pommes = 8 », rationalisant le processus de raisonnement sans intervention humaine.

### Chaîne de pensées multimodale

La chaîne de pensée multimodale étend le cadre CoT pour incorporer des entrées provenant de diverses modalités, telles que du texte et des images, ce qui permet au modèle de traiter et d’intégrer divers types d’informations pour des tâches de raisonnement complexes.[10](#f10)

Par exemple, lorsqu’on lui présente une image d’une plage bondée et qu’on lui demande : « Cette plage est-elle susceptible d’être populaire en été ? », un modèle utilisant un CoT multimodal peut analyser des repères visuels. Ainsi, des repères tels que le taux d’occupation de la plage et les conditions météorologiques, ainsi que la compréhension textuelle de la popularité saisonnière, aident le modèle à produire une réponse détaillée, telle que « La plage est bondée, ce qui indique une popularité élevée, qui augmente probablement en été ».

Ces variantes d’incitation à la chaîne de pensée témoignent non seulement de la flexibilité et de l’adaptabilité de l’approche CoT, mais laissent également entrevoir le vaste potentiel de développement dans le domaine des capacités de raisonnement de l’IA et de résolution de problèmes.

## Avantages et limites

Le prompting CoT est une technique puissante pour améliorer les performances des grands modèles de langage (LLM) sur des tâches de raisonnement complexes, offrant des avantages significatifs dans divers domaines, tels que l’amélioration de la précision, de la transparence et des capacités de raisonnement à plusieurs étapes. Cependant, il est essentiel de tenir compte de ses limites, notamment la nécessité d’utiliser des prompts de haute qualité, l’augmentation du coût de calcul, la vulnérabilité aux attaques par exemples contradictoires et les difficultés liées à l’évaluation des améliorations qualitatives dans le raisonnement ou la compréhension. En relevant ces limites, les chercheurs et les spécialistes peuvent assurer un déploiement responsable et efficace du prompting CoT dans diverses applications.[11](#f11)

### Avantages de l’incitation par chaine de pensées

Les utilisateurs peuvent bénéficier d’un certain nombre d’avantages dans le cadre du prompting par chaîne de pensée. En voici quelques-uns :\

- **Amélioration des résultats des prompts** : l’incitation à la chaîne de pensée améliore les performances des LLM sur les tâches de raisonnement complexes en les décomposant en étapes plus simples et logiques.
- **Transparence et compréhension :** la génération d’étapes de raisonnement intermédiaires offre une transparence sur la manière dont le modèle arrive à ses conclusions, ce qui rend le processus de prise de décision plus compréhensible pour les utilisateurs.
- **Raisonnement en plusieurs étapes :** en abordant systématiquement chaque composante d’un problème, le prompting par chaîne de pensée conduit souvent à des réponses plus précises et plus fiables, en particulier dans les tâches nécessitant un raisonnement en plusieurs étapes. Le raisonnement en plusieurs étapes fait référence à la capacité d’effectuer des opérations logiques complexes en les décomposant en étapes plus petites et séquentielles. Cette compétence cognitive est essentielle pour résoudre des problèmes complexes, prendre des décisions et comprendre les relations de cause à effet. 
- **Le souci du détail :** le modèle d’explication étape par étape s’apparente à des méthodes d’enseignement qui encouragent la compréhension par le biais de ventilations détaillées, ce qui rend l’incitation par CoT utile dans des contextes éducatifs.
- **Diversité :** la CoT peut être appliquée à un large éventail de tâches, y compris, mais sans s’y limiter, au raisonnement arithmétique, au raisonnement de bon sens et à la résolution de problèmes complexes, démontrant sa souplesse d’utilisation.

### Limites de l’incitation par chaîne de pensées

Voici quelques limitations qui peuvent être rencontrées lors de l’adoption de la chaîne de pensée.

- **Contrôle qualité :** l’efficacité du prompting CoT dépend largement de la qualité des prompts fournis, ce qui nécessite des exemples soigneusement conçus pour orienter le modèle avec précision.
- **Puissance de calcul élevée :** la génération et le traitement de plusieurs étapes de raisonnement nécessitent plus de puissance de calcul et de temps que les incitations standard en une seule étape. L’adoption de cette technique est donc plus coûteuse quel que soit le type d’organisation.
- **Concept erroné :** il existe un risque de générer des chemins de raisonnement plausibles mais incorrects, ce qui conduit à des conclusions trompeuses ou erronées.
- **Coûts et délais :** une conception d'incitations par CoT efficace peut être plus complexe et plus laborieuse, nécessitant une compréhension approfondie du domaine du problème et des capacités du modèle.
- **Surajustement des modèles :** il existe un risque que les modèles soient trop adaptés au style ou au schéma de raisonnement des instructions, ce qui pourrait réduire leurs capacités de généralisation pour d’autres tâches.
- **Évaluation et validation :** même si la CoT peut améliorer l’interprétabilité et la précision, il peut être difficile de mesurer les améliorations qualitatives en matière de raisonnement ou de compréhension. Cela est dû à la complexité inhérente de la cognition humaine et à la nature subjective de l’évaluation des expressions linguistiques. Cependant, plusieurs approches peuvent être utilisées pour évaluer l’efficacité de l’incitation CoT. Par exemple, la comparaison des réponses du modèle à celles d’un modèle de référence ou d’experts humains peut fournir des informations sur les gains de performance relatifs. De plus, l’analyse des étapes de raisonnement intermédiaires générées par le LLM peut offrir des informations précieuses sur le processus de prise de décision, même s’il est difficile de mesurer directement les améliorations dans le raisonnement ou la compréhension.

## Avancées dans la chaîne de pensées

L’évolution de la chaîne de pensée (CoT) témoigne des avancées synergiques dans plusieurs domaines, notamment le traitement automatique du langage naturel (NLP), le machine learning et le domaine en plein essor de l’IA générative. Ces progrès ont non seulement propulsé la CoT à l’avant-garde de la résolution de problèmes complexes, mais ont également mis en évidence son utilité dans un large éventail d’applications. Ici, nous nous penchons sur les développements clés, en intégrant les termes spécifiés pour brosser un tableau complet des progrès de la CoT.

### Ingénierie rapide et invite originelle

Les innovations en matière de prompt engineering ont considérablement amélioré la compréhension des modèles et l’interaction avec le prompt d’origine, conduisant à des voies de raisonnement plus nuancées et alignées sur le contexte. Ce développement a été essentiel pour affiner l’efficacité de la CoT.[12](#f12)

### Raisonnement symbolique et raisonnement logique

Son intégration dans les tâches de raisonnement symbolique et de raisonnement logique a amélioré la capacité de réflexion abstraite et de déduction des modèles, marquant ainsi une avancée significative dans la résolution des défis logiques grâce à la CoT.[13](#f13)

Par exemple, le raisonnement symbolique consiste à résoudre des équations mathématiques telles que 2 + 3 = 5. Dans ce cas, le problème est décomposé en ses parties constitutives (addition et nombres), et le modèle déduit la bonne réponse en fonction de ses connaissances acquises et de ses règles d’inférence. Le raisonnement logique, en revanche, consiste à tirer des conclusions à partir de prémisses ou d’hypothèses, telles que « Tous les oiseaux peuvent voler et un pingouin est un oiseau ». Le modèle déterminerait alors qu’un pingouin peut voler en fonction des informations fournies. L’intégration du prompting CoT dans les tâches de raisonnement symbolique et de raisonnement logique a permis aux LLM de démontrer des capacités améliorées de pensée abstraite et de déduction, leur permettant de s’attaquer à des problèmes plus complexes et plus divers.

### Créativité décuplée

L’application de l’IA générative et des architectures transformatrices a révolutionné la CoT, permettant de générer des chemins de raisonnement sophistiqués qui font preuve de créativité et de profondeur. Cette synergie a élargi l’applicabilité de la CoT, influençant à la fois les domaines universitaires et pratiques.[14](#f14)

### Modèles plus petits et cohérence propre

Les progrès qui permettent aux petits modèles de s’engager efficacement dans le raisonnement CoT ont démocratisé l’accès à des capacités de raisonnement plus sophistiquées. L’accent mis sur la cohérence propre dans la CoT garantit l’intégrité logique des chemins générés, améliorant ainsi la fiabilité des conclusions générées par les modèles.[15](#f15)

## Cas d’utilisation de la chaîne de pensée

Avec sa capacité à décomposer les problèmes complexes en étapes de raisonnement compréhensibles, la méthodologie de la chaîne de pensée (CoT) a trouvé des applications dans un large éventail de domaines. Ces cas d’utilisation démontrent non seulement la polyvalence de la CoT, mais aussi sa capacité à transformer la façon dont les systèmes abordent les tâches de résolution de problèmes et de prise de décision. Dans la section suivante, vous trouverez plusieurs cas d’utilisation importants où la CoT a été appliquée de manière efficace.

### Assistants d’IA

L’intégration de la CoT dans les chatbots et l’utilisation de techniques [NLP](https://www.ibm.com/fr-fr/think/topics/natural-language-processing) de pointe ont transformé l’IA conversationnelle, permettant aux chatbots de mener des interactions plus complexes qui nécessitent un niveau de compréhension et de résolution de problèmes plus approfondi.

Ces avancées constituent collectivement un bond en avant dans les capacités de la CoT et l’importance de l’intégration des chatbots et des modèles CoT, soulignant leur capacité à révolutionner la prise de décision et les processus de résolution de problèmes pilotés par l’IA. En alliant les capacités conversationnelles des chatbots aux capacités de raisonnement avancées des modèles CoT, nous pouvons créer des systèmes d’IA plus sophistiqués et plus efficaces, capables de gérer un plus large éventail de tâches et d’applications.

En outre, l’intégration de diverses applications et divers modèles CoT peut améliorer l’expérience globale de l’utilisateur en permettant aux systèmes d’IA de mieux comprendre et répondre aux besoins et aux préférences des utilisateurs. En intégrant des techniques de [traitement automatique du langage naturel (NLP)](https://www.ibm.com/fr-fr/think/topics/natural-language-processing) dans les modèles CoT, nous pouvons permettre aux chatbots de comprendre et de répondre aux entrées des utilisateurs d’une manière plus proche de celle de l’humain, créant ainsi des expériences conversationnelles plus engageantes, intuitives et efficaces.

### Chatbots des services client

Les chatbots avancés s’appuient sur la CoT pour mieux comprendre et répondre aux requêtes des clients. En décomposant le problème d’un client en parties plus petites et gérables, ils peuvent fournir des réponses plus précises et plus utiles, améliorant ainsi la satisfaction du client et réduisant le besoin d’intervention humaine.

### Recherche et innovation

Les chercheurs utilisent la CoT pour structurer leur processus de pensée dans la résolution de problèmes scientifiques complexes, facilitant ainsi l’innovation. Cette approche structurée peut accélérer le processus de découverte et permettre la formulation de nouvelles hypothèses.

### Création et synthèse de contenu

Dans la création de contenu, la CoT aide à générer des schémas ou des résumés structurés en organisant logiquement les pensées et les informations, améliorant ainsi la cohérence et la qualité du contenu rédactionnel.

### Formation et apprentissage

La CoT joue un rôle essentiel dans les plateformes technologiques éducatives, contribuant à la génération d’explications étape par étape pour des problèmes complexes. Cette capacité est particulièrement utile dans des sujets tels que les mathématiques et les sciences, où la compréhension du processus est aussi cruciale que la réponse finale. Les systèmes basés sur la CoT peuvent guider les étudiants dans les procédures de résolution de problèmes, améliorant ainsi leur compréhension et leur apprentissage.

### IA éthique et prise de décision

La CoT est essentielle pour comprendre le raisonnement soutenant les décisions pilotées par l’IA, en particulier dans les scénarios nécessitant des considérations éthiques. En fournissant un parcours de raisonnement transparent, la CoT contribue à garantir que les décisions de l’IA sont conformes aux normes éthiques et sociétales.

Ces cas d’utilisation soulignent le potentiel de transformation de la CoT dans divers secteurs, offrant un aperçu de sa capacité à redéfinir les processus de résolution de problèmes et de prise de décision. Au fur et à mesure de l’évolution de la CoT, ses applications devraient se développer, intégrer davantage cette méthodologie dans le réseau des avancées technologiques et sociétales.

L’incitation par chaîne de pensées constitue un bond en avant dans la capacité de l’IA à entreprendre des tâches de raisonnement complexes, imitant les processus cognitifs humains. En élucidant les étapes intermédiaires du raisonnement, la CoT amplifie non seulement le sens de la résolution de problèmes des LLM, mais améliore également la transparence et l’interprétabilité. Malgré des limites intrinsèques, les explorations en cours des variantes et des applications de la CoT continuent d’étendre les capacités de raisonnement des modèles IA, annonçant de futures améliorations dans les fonctionnalités cognitives de l’IA.
