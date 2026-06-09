> Source : https://www.ibm.com/fr-fr/think/topics/one-shot-prompting

# Qu’est-ce que l’apprentissage one-shot ?

L’apprentissage one-shot désigne la méthode consistant à fournir à un modèle un seul exemple ou prompt pour effectuer une tâche. Contrairement à d’autres techniques de prompt engineering, telles que l’apprentissage zero-shot, où aucun exemple n’est fourni, ou l’apprentissage few-shot, où quelques exemples sont fournis, l’apprentissage one-shot repose sur un seul prompt bien conçu pour obtenir le résultat souhaité. Cette méthode exploite de grands modèles de langage (LLM) tels que les modèles GPT-3/GPT-4 (Generative Pre-trained Transformer) d’OpenAI ou les [modèles IBM® Granite](https://www.ibm.com/fr-fr/products/watsonx-ai/foundation-models) pour comprendre et générer des textes de type humain à partir d’entrées minimales.

L’apprentissage one-shot est particulièrement utile dans les scénarios où la collecte de grandes quantités de données d’entraînement n’est pas pratique. Par exemple, dans des applications telles que le prompting par chaîne de pensée, l’apprentissage few-shot et l’apprentissage zero-shot, où les données étiquetées sont limitées ou inexistantes, l’apprentissage one-shot offre un avantage significatif en permettant aux modèles de généraliser à partir d’un seul exemple. La figure 1 illustre l’entraînement de l’apprentissage one-shot.

  Figure 1 – Formation de l’apprentissage one-shot

Dans le domaine en rapide évolution de l’intelligence artificielle (IA) et du traitement automatique du langage naturel (NLP), en particulier dans l’IA générative, le prompt engineering est devenue une technique essentielle. Parmi les différents types de prompting, l’apprentissage one-shot se distingue tant par son efficacité que par son efficience. Cet article explore le concept de l’apprentissage one-shot, ses mécanismes, ses applications, ses avantages, ses limites et ses perspectives d’avenir.

Le prompting est une technique utilisée en IA pour guider les modèles de langage dans la génération des résultats souhaités. Il existe différents types de prompting, notamment les apprentissages zero-shot, few-shot et one-shot. Chaque type varie en termes de volume de données et d’exemples fournis au modèle pour accomplir une tâche spécifique. Le prompt engineering consiste à élaborer ces prompts afin d’optimiser les performances du modèle.

## Les mécanismes derrière l’apprentissage one-shot

L’apprentissage one-shot exploite les capacités des grands modèles de langage (LLM) avancés pour générer des réponses cohérentes et adaptées au contexte à partir d’un seul exemple de prompt. Cette efficacité est rendue possible par plusieurs mécanismes sous-jacents, notamment le prompting par connaissances, le prompting visuel contextuel et la projection adaptative des caractéristiques. Si certains de ces mécanismes, tels que le prompting de connaissances et la projection adaptative de caractéristiques, sont généralisés et peuvent être appliqués à divers types de données comme le texte, l’image et la vidéo, d’autres, tels que le prompting visuel contextuel, sont spécifiquement conçus pour traiter des données image ou vidéo.

Le prompting visuel contextuel permet au modèle d’interpréter et de répondre sur la base d’indices visuels, ce qui est critique pour des tâches telles que la reconnaissance d’images ou l’analyse vidéo. En revanche, le prompting par connaissances et la projection adaptative des caractéristiques améliorent la capacité du modèle à comprendre et à générer des réponses à partir de différents types d’entrées, ce qui les rend polyvalentes dans de nombreux domaines.

Un exemple : vous devez résumer un document français en anglais et formater la sortie pour une API spécifique. Avec l’apprentissage one-shot, vous pouvez fournir un seul exemple de prompt, tel que : « Résumez ce texte français en anglais à l’aide du modèle d’API {Title}, {Key Points}, {Summary} ». Le LLM exploite ses capacités multilingues et la projection adaptative des caractéristiques pour produire le format de sortie souhaité. En Python, ce processus peut être automatisé en intégrant la réponse du modèle d’IA générative dans le workflow de l’API.

  Figure 2 – Différents mécanismes pour l’apprentissage one-shot

Prompting par connaissances

Cette méthode consiste à exploiter des bases de connaissances externes ou des corpus préexistants spécifiques à un domaine afin d’améliorer la compréhension contextuelle et les capacités de prise de décision du modèle. En intégrant des graphes de connaissances structurés ou des propositions de texte enrichies d’informations liées à des actions ou à des tâches données, le modèle peut récupérer efficacement les informations pertinentes qui permettent des inférences plus précises. Ainsi, l’intégration de corpus liés aux actions, tels que des séquences de tâches ou d’événements pertinents pour le domaine, permet au modèle de mieux généraliser à de nouvelles tâches dans des scénarios d’apprentissage one-shot. Cette approche permet au modèle de combler les lacunes de connaissances à l’aide de référentiels d’informations prédéfinis, améliorant ainsi sa capacité à s’adapter et à générer des réponses plus adaptées au contexte.[\[1\]](#f01) Cette technique est particulièrement efficace lorsqu’elle est associée à des LLM à grande échelle, car elle réduit le besoin de larges volumes de données d’entraînement spécifiques à une tâche tout en fournissant des résultats robustes.

Prompting visuel contextuel

Cette technique exploite des repères visuels tels que des masques de segmentation, des cadres de sélection ou des points clés pour aider les modèles à comprendre et à traiter plus efficacement les données d’images ou de vidéos. Dans le prompting visuel contextuel, le modèle reçoit une image de référence ou un ensemble de segments d’image qui mettent en évidence des zones d’intérêt spécifiques, ce qui lui permet de se concentrer sur les caractéristiques visuelles clés lors de l’inférence. Grâce à ces prompts visuels, le modèle peut mieux comprendre les relations spatiales, les limites des objets et les éléments contextuels au sein de l’image. Cela améliore considérablement ses performances dans les tâches de vision. Cette approche s’est avérée efficace pour améliorer les capacités d’apprentissage zero-shot et one-shot en permettant au modèle de généraliser à partir d’exemples minimaux dans diverses applications basées sur la vision, telles que la détection d’objets, la classification d’images et la segmentation.[\[2\]](#f02) De plus, cette technique permet au modèle d’affiner ses prédictions en s’adaptant de manière dynamique à de nouveaux contextes visuels avec un minimum de données, ce qui le rend très efficace dans les scénarios où les exemples d’entraînement étiquetés sont limités.

Projection adaptative des caractéristiques

Dans la reconnaissance d’actions one-shot, la projection adaptative des caractéristiques permet de relever le défi des variations temporelles dans les données vidéo en alignant et en affinant les caractéristiques extraites au fil du temps. Cette méthode consiste à pré-entraîner et à affiner le réseau de base afin d’apprendre un ensemble général de caractéristiques, puis à appliquer des techniques d’adaptation des caractéristiques qui permettent au modèle d’ajuster dynamiquement ses représentations internes des caractéristiques en fonction de la progression temporelle de la vidéo. En projetant les caractéristiques d’entrée sur un espace qui saisit à la fois les modèles spatiaux et temporels, le modèle peut mieux gérer la variabilité des séquences d’actions en fournissant des exemples tels que les changements de vitesse de mouvement ou l’interaction entre les objets. Cette approche améliore considérablement la capacité du modèle à reconnaître des actions à partir d’une seule vidéo d’entraînement, ce qui renforce sa généralisation et sa précision dans la reconnaissance d’actions complexes dans des séquences vidéo nouvelles et inédites.[\[3\]](#f03) La projection adaptative des caractéristiques est particulièrement utile pour gérer la dynamique temporelle fine des tâches basées sur la vidéo, ce qui en fait un élément critique pour la reconnaissance d’actions hautes performances en one-shot.

Zoom sur l’attention

Cette stratégie améliore l’apprentissage one-shot en concentrant progressivement l’attention du modèle sur les zones les plus pertinentes de l’entrée. Dans les tâches de détection d’actions, le zoom sur l’attention est employé via des mécanismes tels que l’attention croisée entre les ensembles de support et de requête. Cette approche permet au modèle de comparer et d’aligner les caractéristiques d’une vidéo de support (qui contient l’exemple d’action) avec une vidéo de requête (où l’action doit être détectée). En se focalisant sur des zones temporelles ou spatiales spécifiques qui sont les plus susceptibles de contenir l’action pertinente, le modèle génère des propositions d’actions de haute qualité. Ce mécanisme d’attention croisée permet au modèle de « zoomer » efficacement sur les parties clés de l’entrée, réduisant ainsi le bruit et les informations non pertinentes, ce qui améliore ses performances dans les scénarios d’apprentissage one-shot.[\[4\]](#f04) Cette technique réduit les espaces d’entrée complexes, ce qui facilite un traitement plus efficace de l’ensemble de requêtes tout en conservant la précision, même avec un minimum d’exemples d’entraînement.

Ces mécanismes illustrent l’adaptabilité et la robustesse de l’apprentissage one-shot dans différents domaines à l’aide d’exemples spécifiques. En tirant parti de techniques de prompting avancées et en intégrant des connaissances externes et des indices visuels, l’apprentissage one-shot peut atteindre une précision et une efficacité élevées avec un minimum de données d’entrée.

## Avantages et limites de l’apprentissage one-shot

L’apprentissage one-shot offre des avantages significatifs et pose certains défis, ce qui en fait une technique convaincante mais complexe dans le domaine de l’IA et du machine learning. Voici un aperçu détaillé de ses avantages et limites :

**Avantages**

- **Efficacité** – **réduction des données d’entraînement** : l’apprentissage one-shot nécessite beaucoup moins de données d’entraînement que les modèles de machine learning traditionnels. Cette efficacité réduit les ressources informatiques et le temps nécessaires à l’entraînement. Par exemple, dans des applications telles que la reconnaissance d’actions one-shot, les modèles peuvent atteindre une grande précision avec un minimum de données d’entrée.[\[3\]](#f03)
- **Rapidité** – **déploiement plus rapide** : l’apprentissage one-shot permet un déploiement rapide des modèles d’IA. Cela est particulièrement avantageux dans les environnements dynamiques où une adaptation rapide à de nouvelles tâches est primordiale. La capacité à générer des réponses de haute qualité à partir d’un seul exemple accélère le processus de déploiement.[\[5\]](#f05)
- **Flexibilité** – **adaptabilité à diverses applications** : l’apprentissage one-shot est très adaptable à toute une gamme d’applications, des chatbots de service client aux recommandations personnalisées. Cette flexibilité permet de l’employer dans divers cas d’utilisation, y compris dans des scénarios d’apprentissage few-shot et zero-shot.[\[1\]](#f01)

**Limites**

- **Risque de biais** – **biais hérités des données pré-entraînées** : l’un des défis importants de l’apprentissage one-shot est le risque de biais. Comme les modèles s’appuient fortement sur des données pré-entraînées, ils peuvent hériter et perpétuer les biais présents dans les jeux de données d’entraînement. Cela peut affecter l’équité et la précision des résultats du modèle.[\[6\]](#f06)
- **Précision** – **variabilité des performances** : si l’apprentissage one-shot peut être très efficace, il n’atteint pas toujours le même niveau de précision que les méthodes qui exploitent des données d’entraînement exhaustives. Les tâches complexes nécessitant une compréhension et un contexte détaillés peuvent poser des défis aux modèles d’apprentissage one-shot, ce qui entraîne une variabilité des performances.[\[7\]](#f07)

## Cas d’utilisation

L’apprentissage one-shot est une technique puissante qui trouve de nombreux exemples et applications dans un large éventail de secteurs et de scénarios. En tirant parti des capacités des grands modèles de langage (LLM) avancés et des méthodes de prompting sophistiquées, il peut considérablement améliorer l’efficacité et les performances dans diverses tâches. Voici quelques cas d’utilisation notables :

**1. Service client et chatbots**

L’apprentissage one-shot peut considérablement améliorer les performances des chatbots et des assistants virtuels dans le domaine du service client. En fournissant un seul exemple bien conçu, les chatbots peuvent être formés pour traiter des requêtes complexes, proposer des réponses personnalisées et améliorer la satisfaction globale des clients. Cette méthode réduit le besoin de données d’entraînement exhaustives, ce qui permet un déploiement rapide et une adaptation à différents scénarios de service client.[\[6\]](#f06)

**2. Création et automatisation de contenu**

Dans le domaine de la création et de l’automatisation de contenu, l’apprentissage one-shot peut être employé pour générer des articles, des rapports et du contenu créatif de haute qualité avec des entrées minimales. Ceci est particulièrement utile pour les spécialistes du marketing, les rédacteurs et les créateurs de contenu qui doivent produire efficacement de grands volumes. À l’aide d’un seul prompt, les modèles peuvent générer un contenu diversifié et pertinent sur le plan contextuel, ce qui permet d’économiser du temps et des ressources.[\[1\]](#f01)

**3. Recommandations personnalisées**

L’apprentissage one-shot renforce les systèmes de recommandation en générant des suggestions personnalisées à partir d’une saisie limitée. Ainsi, les plateformes de commerce électronique peuvent exploiter l’apprentissage one-shot pour fournir des recommandations de produits sur mesure, améliorant ainsi l’expérience d’achat et stimulant les ventes. Cette méthode exploite un minimum de données pour produire des recommandations très précises et pertinentes.[\[7\]](#f07)

**4. Reconnaissance des actions dans les vidéos**

Dans l’analyse vidéo, l’apprentissage one-shot peut être utilisé pour des tâches de reconnaissance d’actions, telles que l’identification d’actions spécifiques dans des images de vidéosurveillance ou l’analyse sportive. En fournissant une seule vidéo d’exemple, les modèles peuvent apprendre à reconnaître des actions similaires dans de nouvelles vidéos, même dans des conditions variables. Cet aspect est particulièrement utile dans des applications telles que la sécurité, l’analyse des performances sportives et le montage vidéo automatisé.[\[3\]](#f03)

Ainsi, l’apprentissage one-shot constitue une avancée significative dans le secteur de l’IA, offrant des solutions efficaces et flexibles dans divers domaines. À mesure que la recherche continue de s’attaquer à ses limites, les applications et les avantages potentiels de cette technique sont appelés à se développer, contribuant ainsi à l’évolution des systèmes intelligents.
