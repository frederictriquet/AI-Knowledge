> Source : https://www.ibm.com/fr-fr/think/topics/prompt-tuning

# Qu’est-ce que l’optimisation des prompts ?

Le réglage des prompts est une méthode de réglage fin à faible consommation de paramètres (PEFT) qui permet d'adapter rapidement les modèles pré-entraînés aux nouvelles tâches sans modifier leurs milliards de paramètres. La technique repose plutôt sur l’apprentissage d’un petit nombre de vecteurs entraînables—les soft prompts ou tokens virtuels—qui sont injectés dans l’espace d’entrée du modèle. Ces vecteurs servent de signaux continus pour contrôler le modèle non modifié afin d'obtenir le comportement escompté, tout en préservant l’architecture de base. Cette perspective réduit considérablement les coûts de calcul et de stockage, ce qui la rend idéale pour les entreprises qui ont besoin de personnaliser de grands modèles pour plusieurs cas d’utilisation. [1](#f01), [2](#f02)

#### Quelle est la différence avec le « prompting » et le « réglage fin » ?

Le prompt engineering consiste à élaborer des instructions textuelles précises (prompts codés en dur) afin d'extraire le bon comportement d’un modèle. S'ils s’avèrent efficaces dans certains scénarios, les prompts codés en dur manquent de souplesse et sont complexes à optimiser à grande échelle. Autrement dit, en prompt engineering, le moindre changement de mots peut induire des variations de performance significatives et imprévisibles, ce qui complique toute tentative d’optimisation systématique. Toutefois, le réglage fin modifie l'intégralité des paramètres du modèle, ce qui exige d’importantes ressources de calcul et de stockage, en particulier pour les modèles dotés de centaines de milliards de poids. L'optimisation des prompts offre un compromis : il utilise des intégrations continues au lieu d'un texte distinct, n'entraîne que ces quelques vecteurs et obtient, sur de nombreuses tâches, des performances similaires à l'ajustement fin intégral, le tout avec une efficacité nettement supérieure. [2,](#f02) [3](#f03)

## Principaux éléments

L'optimisation des prompts repose sur des éléments essentiels qui fonctionnent de concert pour adapter des modèles pré-entraînés de grande taille. L'approche fait appel à un modèle non modifié, entraîne un ensemble d'enchâssements de prompt souple par optimisation par descente de gradient et est orientée par un jeu de données spécifique. Ces éléments permettent une adaptation efficace des paramètres sans réentraîner l’ensemble du modèle. [1](#f01)[, 2](#f02)\
\
Modèle pré-entraîné gelé : Un grand modèle de langage (LLM) ou un transformeur de vision constitue la structure principale. Il n'est pas modifié pendant l’entraînement, ce qui lui permet de conserver ses connaissances générales tout en minimisant les coûts de calcul et de stockage. [4](#f04)\
\
Intégrations de prompts souples : ces prompts sont des vecteurs entraînables—également désignés comme jetons virtuels—qui sont joints ou insérés dans l'entrée sous forme de tokens. Ils agissent comme des signaux continus qui contrôlent le modèle vers la tâche de sortie sans modifier ses poids internes.[4](#f04)\
\
Jeu de données spécifique à la tâche : un jeu de données étiqueté aligné sur la tâche en aval est essentiel pour l’optimisation supervisée des prompts souples.\
\
Optimisation par gradient : Seuls les paramètres du prompt souple et de la couche de sortie allégée (en option) sont actualisés grâce à l'utilisation d'optimiseurs, l'architecture de base restant gelée. Cette méthode garantit l’efficacité et la stabilité pendant la tâche.[4](#f04)

  Figure 1 - Principaux composants de l'optimisation des prompts

Comme le montre le schéma, le prompt tuning introduit un jeu réduit de vecteurs entraînables dans l'entrée d'un modèle pré-entraîné gelé. Ces instructions masquées permettent de guider le modèle vers la tâche cible sans qu'il soit nécessaire d’actualiser des milliards de paramètres.\
\
Outre ces composants centraux, plusieurs décisions de conception ont un impact significatif sur la performance :\
\
Longueur du prompt : le nombre de tokens virtuels au sein du prompt souple est un hyperparamètre essentiel. Différents chercheurs ont mené des expériences et en ont déduit que la longueur optimale varie selon la tâche. À titre d'exemple, les tâches de classification les plus simples fonctionnent souvent mieux avec des prompts courts (inférieurs à 20 tokens), alors que les tâches complexes d’étiquetage de séquences peuvent en nécessiter de plus longs (environ 100 jetons).5\
\
Positionnement du prompt : cet élément optimise le positionnement des prompts, selon qu'ils sont introduits en préfixe, en suffixe ou intercalés dans la séquence de saisie.\
\
Stratégie d’initialisation : le lancement de prompts logiciels avec des valeurs aléatoires, des représentations vectorielles échantillonnées ou des jetons spécifiques à une tâche peut avoir un impact sur la vitesse et la précision de la convergence.4\
\
Bien que ces éléments additionnels ne soient pas obligatoires, leur utilisation est recommandée pour obtenir des résultats optimaux.

#### Exemple : Analyse des sentiments avec optimisation du prompt

Pour comprendre clairement la mécanique et les avantages de l'optimisation des prompts, étudions la tâche d'analyse des sentiments. Prenons l'exemple d'un modèle de 175 milliards de paramètres dont l'objectif est de catégoriser les critiques de films en « positives » ou « négatives ». Le réglage fin complet serait extrêmement coûteux et lent à mettre en œuvre. Avec l’optimisation des prompts, le processus est le suivant :\
\
**commencez par un modèle pré-entraîné gelé :** le réseau principal de 175B de paramètres reste entièrement intact, préservant son vaste référentiel de connaissances générales apprises lors du pré-entraînement.5\
\
**Ajoutez des prompts souples :** un petit ensemble de vecteurs pouvant être entraînés (par exemple, 20 tokens virtuels) est associé à l'intégration de chaque critique de film. Ces vecteurs ne sont pas du texte compréhensible par l'humain ; il s'agit d'intégrations continues qui coexistent dans le même espace de haute dimension que le vocabulaire du modèle (soit, par exemple, un espace de 12 288 dimensions pour un modèle de cette ampleur). Grâce à l’optimisation, ces vecteurs apprennent à encoder un signal continu et spécifique à une tâche qui dirige le comportement du modèle.\
\
**Alimenter l'entrée : **par exemple,

```
[Soft Prompts] Le film était absolument fantastique !
```

Dans cet exemple, supposons que nous initialisions 20 tokens de prompt pour une tâche d'analyse des sentiments. Après la formation, l’entrée peut ressembler à ceci en interne :

```
[<v1>, <v2>, <v3>, ... <v20>, The, movie, was, absolutely, fantastic, !]
```

Ici, chaque v1 est un vecteur de prompt de grande dimension appris.\
\
L’objectif de l’entraînement est de trouver les valeurs optimales pour les vecteurs qui guident le modèle gelé afin de classer correctement le sentiment du texte suivant. **Entraînez uniquement les prompts** : à l’aide d’un jeu de données étiquetées d’avis, le processus d’entraînement est lancé. Grâce à la rétropropagation, on calcule le gradient d'erreur, mais l'étape d'optimisation actualise uniquement les paramètres d'intégration du prompt souple. Cette approche consiste à régler seulement quelques milliers de paramètres au lieu de 175 milliards de poids du modèle.5\
\
**Déployez avec modularité** : une fois l'entraînement terminé, le jeu de 20 vecteurs qui en résulte constitue l'adaptation complète à la tâche. Pour adapter le même modèle de base à une tâche différente, telle que la détection des spams, il suffit d’entraîner un nouvel ensemble de prompts logiciels sur un jeu de données spam et de les permuter au moment de l’inférence.\
\
Cette technique offre des avantages considérables en termes d’efficacité. Contrairement à la nécessité de stocker une copie complète et séparée du modèle pour chaque tâche (ce qui, pour un modèle de 175 milliards de paramètres, peut atteindre 350 Go), il suffit ici de stocker les paramètres de prompt spécifiques à la tâche, dont la taille n’est que de quelques Ko.1 Cette modularité fait de l'optimisation des prompts une solution pratique et rentable pour l'adaptation de modèles à grande échelle.2

## Analyse comparative avec d’autres méthodes PEFT

Le réglage basé sur les prompts est l'une des nombreuses familles de méthodes et d’approches relevant du concept plus large de réglage fin économe en paramètres (PEFT). Il est fondamental pour les experts de comprendre en quoi cette méthode recoupe d’autres afin de pouvoir choisir la technique la plus pertinente. Le choix repose sur un équilibre entre la performance, l'expressivité, l'efficacité et la complexité de la mise en œuvre.

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| Méthode | Modification architecturale | Expressivité ou puissance | Taille entraînable | Avantages | Inconvénients |
| Optimisation des prompts approfondies (P-tuning v2)[3](#f03) | Ajoute des vecteurs d’entraînement (« prompts ») à chaque couche du modèle pour influencer le mécanisme d’attention. | Élevé. Exploite et combine efficacement les compétences des modèles existants. | ~0,1 à 3 % des paramètres du modèle. | Universal à l’échelle des modèles ; plus simple que la LoRA pour de nombreuses tâches NLU/NLG. | Moins expressif que la LoRA pour des tâches vraiment novatrices ; peuvent être sensibles aux hyperparamètres. |
| LoRA (Adaptation de bas rang)[6](#f06) | Injecte des matrices de bas rang pouvant être entraînées en parallèle aux matrices de poids existantes (par exemple, dans les couches d’attention). | Très élevé. Peut apprendre des modèles d’attention et des comportements entièrement nouveaux, ce qui le rend plus puissant que les méthodes basées sur les prompts. | ~0,1 à 1 % des paramètres du modèle. | La méthode PEFT la plus expressive ; aucune latence d’inférence supplémentaire, car les pondérations peuvent être fusionnées. | Plus complexe à implémenter et à régler l’hyperparamètre de classement. |
| Adaptateurs | Insère de nouveaux petits modules de réseaux de neurones *en série* dans chaque couche de transformeur. | Élevé. Ajoute une nouvelle capacité de calcul au modèle. | ~1 à 4 % des paramètres du modèle | Stable et bien établi, hautement modulaire. | Peut introduire une légère latence en raison du traitement en série, d'un nombre de paramètres plus élevé que le LoRA ou les prompts. |

## Avantages et limites

Le prompt présente de nombreux avantages dans les applications en temps réel, mais il est important de comprendre ses limites.

### Avantages

Les principaux atouts du réglage des invites sont l’efficacité, la modularité et la préservation des connaissances du modèle de base.\
\
Paramètres et rentabilité exceptionnels : l’avantage le plus important est la réduction drastique des paramètres pouvant être entraînés. En mettant à jour uniquement un petit ensemble de vecteurs de prompt, qui représentent souvent moins de 1 % du modèle total, le réglage des prompts réduit considérablement les coûts de calcul et de stockage. Cette Stratégie rend l’adaptation des modèles de fondation réalisable pour les entreprises disposant de ressources de calcul limitées.\
\
Modularité et déploiement évolutif : chaque tâche étant intégrée dans un jeu de paramètres de prompt réduit et autonome, un seul modèle de base gelé peut être adapté à plusieurs tâches en échangeant ces fichiers de prompt légers lors de l’inférence. Cette architecture « plug-and-play » est hautement modulaire et évite le besoin de magasin et de gérer des copies distinctes de plusieurs gigaoctets pour chaque application.\
\
Atténuation de l’oubli catastrophique : les risques liés au réglage fin intégral écrasent ou dégradent les connaissances préentraînées d’un modèle lors de l’apprentissage d’une nouvelle tâche. En bloquant complètement le poids du modèle principal, le prompt préserve le vaste référentiel de connaissances générales acquises lors de la pré-formation, permettant ainsi de réutiliser le modèle sans perdre ses capacités.\
\
Efficacité des données : contrairement au réglage fin, qui nécessite souvent de grands jeux de données étiquetés pour chaque nouvelle tâche, le prompt peut atteindre une forte performance avec des jeux de données plus petits et plus modestes.

### Limites

Malgré ses points forts, l’accord rapide n’est pas sans inconvénients, notamment des limitations de la puissance expressive, des difficultés d’entraînement et un manque d’interprétabilité.\
\
Pouvoir expressif limité : une limitation théorique centrale est que l'optimisation des invites et des préfixes est moins expressive que des méthodes telles que la LoRA ou le réglage fin intégral. Une analyse formelle a montré que ces méthodes fonctionnent en ajoutant un biais à la sortie des blocs d’attention, mais qu’elles ne peuvent pas modifier fondamentalement les schémas d’attention appris par le modèle. Cela signifie que le réglage des prompts est très efficace pour susciter et combiner les compétences déjà présentes dans le modèle, mais qu’il peut ne pas permettre l’apprentissage de tâches véritablement nouvelles qui nécessitent de nouveaux schémas de raisonnement.\
\
Instable entraînement et sensibilité aux hyperparamètres : l’un des défis pratiques les plus importants est la sensibilité de la méthode aux hyperparamètres. Le processus d’entraînement peut être difficile à faire converger et dépend fortement du choix du [taux d’apprentissage](https://www.ibm.com/fr-fr/think/topics/learning-rate) et de la stratégie d’initialisation prompt et de la durée, nécessitant souvent un réglage minutieux et approfondi pour obtenir des Résultats optimaux.\
\
Le problème de la « boîte noire » et de l'interprétabilité : une limitation majeure et persistante est le manque inhérent de lisibilité des prompts souples. Étant donné qu'il s'agit de vecteurs continus et de haute dimension optimisés par descente de gradient, ils n'ont aucune correspondance textuelle lisible pour l'humain. En raison de cette « boîte noire », il est difficile de comprendre ce que le prompt a appris, pourquoi il oriente le modèle d'une certaine manière et comment le déboguer en cas d'échec.\
\
Dépendance à l’échelle du modèle : l’efficacité de la méthode originale de réglage des prompts au niveau des entrées est corrélée à l’échelle du modèle de backbone. S’il devient compétitif avec un réglage complet sur les modèles comptant plus de 10 milliards de paramètres, ses performances sont nettement plus performantes sur les modèles plus petits et plus couramment utilisés.

## Cas d’utilisation

Les principes de l'optimisation des prompts se sont avérés hautement adaptables, s’étendant bien au-delà de leurs applications initiales dans le [traitement automatique du langage naturel](https://www.ibm.com/fr-fr/think/topics/natural-language-processing). Cette technique est désormais un élément clé pour personnaliser efficacement les modèles dans les domaines multimodaux, le traitement de la parole et pour les paradigmes d’apprentissage avancés.\
\
**Réglage multimodal du prompt (modèles de langage de vision) :** l'optimisation des prompts est une approche cruciale pour adapter les modèles vision-langage (VLM) pré-entraînés, comme CLIP, aux tâches visuelles d'application. Dans ce contexte, les invites peuvent être conçues pour l’une ou les deux modalités.[7](#f07)\
\
**Applications dans le traitement de la parole :** le paradigme du prompt a été étendu avec succès au domaine du traitement de la parole. Dans cette application, un énoncé de parole brute est encodé en unités acoustiques discrètes et un ensemble de prompts pouvant être apprises et spécifiques à une tâche est associé à cette séquence. Ce cadre des exigences est unifié et permet d’adapter un unique modèle vocal préentraîné à un large éventail de tâches. Cela inclut la détection de mots clés, la classification d'intentions et même la reconnaissance vocale automatique (ASR), le tout en ne formant qu'un petit prompt spécifique à une tâche.\
\
**Apprentissage multitâche et multilingue :** pour améliorer encore plus l’efficacité et la généralisation, les chercheurs déplacent au-delà de l’entraînement des prompts isolés en une seule tâche. Les méthodes les plus récentes visent désormais à apprendre des prompts communs pouvant être transférés à travers plusieurs tâches ou langues.

- **Réglage des prompts multitâches (MPT) :** cette approche distille les connaissances issues de plusieurs tâches sources en un seul prompt partagé transférable. Ce prompt partagé peut ensuite être adapté efficacement à de nouvelles tâches cibles, nécessitant aussi peu que 0,035 % des paramètres du modèle par tâche et montrant d’excellentes performances dans les scénarios d’apprentissage few-shot.
- **Ajustement multilingue** : des études sur des modèles multilingues ont révélé que le réglage multitâche d'une collection de jeux de données et de prompts uniquement en anglais peut améliorer de manière significative les performances zéro d'un modèle pour les tâches dans des langues autres que l'anglais. Cette méthode montre que le modèle acquiert des capacités de résolution de tâches qui sont, dans une certaine mesure, indépendantes du langage.

## Conclusion

Dans le domaine des recherches sur l’intelligence artificielle, le machine learning et le prompt de [l’IA générative sont devenus une méthode](https://www.ibm.com/fr-fr/think/topics/generative-ai) critique pour le réglage efficace des [modèles d’IA](https://www.ibm.com/fr-fr/think/topics/ai-model). Contrairement à l’entraînement complet des modèles, qui modifie tous les poids des modèles et risque de sur-ajustement avec des données d’entraînement limitées, cette technique se concentre sur l’optimisation des prompts d’entrée qui sont liés au texte d’entrée. Grâce à un processus d’automatisation et d’itération, l’objectif est de découvrir un prompt optimal qui crée des prompts efficaces pour des tâches spécifiques, un processus dont le succès dépend souvent de la taille du modèle. Cette approche offre une alternative évolutive au réentraînement approfondi et complète d’autres stratégies telles que la [RAG,](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation) renforçant ainsi son rôle de pierre angulaire dans la personnalisation des modèles de fondation.
