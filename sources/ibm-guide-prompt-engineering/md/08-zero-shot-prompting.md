> Source : https://www.ibm.com/fr-fr/think/topics/zero-shot-prompting

# Qu’est-ce que l’apprentissage zero-shot ?

L’apprentissage zero-shot est une méthode de [prompt engineering](https://www.ibm.com/fr-fr/think/topics/prompt-engineering) qui repose sur l’entraînement préalable d’u [grand modèle de langage (LLM)](https://www.ibm.com/fr-fr/think/topics/large-language-models) en vue de déduire une réponse appropriée. Contrairement à d’autres méthodes de prompt engineering telles que l’apprentissage few-shot, les modèles ne reçoivent pas d’exemples de sortie lorsqu’ils sont interrogés avec la technique zero-shot.[1](#f1)

### Comment fonctionne l’apprentissage zero-shot ?

L’une des promesses des [modèles de fondation](https://research.ibm.com/blog/what-are-foundation-models) est qu’ils peuvent être adaptés à de nombreux cas d’utilisation sans nécessiter de données de formation supplémentaires. Dans l’apprentissage zero-shot, le modèle est invité à générer une production sans recevoir d’exemple de la sortie souhaitée pour le cas d’utilisation. L’apprentissage zero-shot est une application de [l’apprentissage zero-shot](https://www.ibm.com/fr-fr/think/topics/zero-shot-learning), un modèle de machine learning qui demande aux modèles de faire des prédictions avec zéro donnée d’entraînement.

Dans l’exemple ci-dessous, le modèle granite-3-8b-instruct d’IBM de [la série Granite d’IBM](https://www.ibm.com/fr-fr/granite) est déclenché à l’aide de l’apprentissage zero-shot sur un cas d’utilisation de classification.[2](#f2) Dans ce cas, on demande au modèle de classer un problème informatique comme appartenant à la classe *« Élevé »*  ou à la classe *« Faible »*, indiquant* *l’urgence du problème. Dans cet exemple, le modèle déduit l’étiquette de classification **« Élevé »** pour le prompt (comme représenté par le résultat en **gras**), une réponse appropriée dans ce contexte.

Remarque : la commande a été exécutée dans IBM® [watsonx.ai](https://www.ibm.com/fr-fr/products/watsonx-ai) Prompt Lab en utilisant le mode « Freeform ».

*Définis le nom de classe pour le problème décrit : Élevé, Moyen ou Faible. Prévois uniquement le nom de la classe pour le dernier problème. Fournis une brève description de la raison pour laquelle ce nom de classe a été choisi.*

*Nom de la classe : Élevé\
Description : il s’agit d’un problème qui a un coût commercial élevé, qui affecte de nombreux utilisateurs ou les deux.*

*Nom de la classe : Moyen\
Description : le problème qui se situe quelque part entre les niveaux élevé et faible.*

*Nom de la classe : Faible\
Description : il s’agit d’un problème qui a un impact sur quelques utilisateurs, qui n’a pas de coût d’entreprise élevé, ou les deux.*

*Problème : les utilisateurs signalent qu’ils ne sont pas en mesure de télécharger des fichiers.*

**Classe : Élevé**

**Description : ce problème est considéré comme élevé, car il affecte de nombreux utilisateurs et son coût commercial est élevé. L’impossibilité de télécharger des fichiers peut empêcher les utilisateurs d’effectuer leurs tâches, ce qui peut entraîner des retards et une baisse de productivité. En outre, ce problème peut affecter plusieurs services ou équipes, ce qui augmente davantage le coût pour l’entreprise.**

Une stratégie d’apprentissage zero-shot consiste souvent à utiliser le prompt engineering par défaut lors de l’attribution d’un nouveau problème à un modèle.[1](#f1) Cet exemple montre comment le modèle est censé générer une inférence appropriée sans exemples explicites de réponses. Le scénario d’apprentissage zero-shot imite l’apprentissage humain en appliquant les connaissances antérieures pour résoudre de nouveaux problèmes.[3](#f3)

### Composants d’un prompt

  Figure-2 - Composants d’un prompt

Bien que le modèle ne soit pas fourni avec des exemples de prompts, il est fourni avec des détails sur la façon d’accomplir la tâche :[1](#f1)

**Instruction :** tout d’abord, les instructions fournies au modèle sont les suivantes : *« Définir le nom de la classe pour le problème décrit... »*

**Contexte :*** *ensuite, le contexte du modèle inclut une description des noms de classe.*\*

**Données d’entrée :** le modèle reçoit les données d’entrée pour exécuter la tâche de classification avec le prompt « *Problème : les utilisateurs signalent qu’ils ne sont pas en mesure de télécharger des fichiers »*.

**Indicateur de sortie :** en option, le modèle peut recevoir un indicateur de sortie, dans ce cas le texte *« Classe :* », ce qui incite le modèle à répondre avec le nom de classe du problème. Les indicateurs de sortie indiquent au modèle le type de sortie à produire pour un type de réponse spécifique.\

Le format personnalisé de ce prompt est adapté au problème de classification en question. D’autres cas d’utilisation peuvent nécessiter un format de prompt différent et ne pas contenir les mêmes composants d’instruction, de contexte, de données d’entrée et d’indicateur de sortie.[1](#f1) Différents modèles peuvent nécessiter différents formats pour un prompt. Veillez à suivre toutes les instructions données pour formater un prompt pour un modèle spécifique. Dans cet exemple, grâce au pré-entraînement du modèle et à ce prompt bien conçu utilisant les composants décrits, le modèle répond avec une sortie appropriée pour cette tâche.

## Apprentissage zero-shot et apprentissage few-shot

  Figure 2 - Comparaison des apprentissages zero-shot, one-shot et few-shot

Contrairement à l’apprentissage zero-shot, l’apprentissage few-shot fournit au modèle des exemples d’entrée et de sortie attendues pour la tâche.[1](#f1) L’image précédente montre la différence entre l’apprentissage zero-shot et l’apprentissage few-shot, l’apprentissage one-shot étant également présenté à titre de cas particulier. 

En utilisant le même modèle IBM granite-3-8b-instruct, des exemples de *« problèmes »* et leurs « *classes* » correspondantes sont fournis pour cette tâche.[2 ](#f2)Les trois exemples d’entrée et de sortie qui sont fournis illustrent la stratégie d’apprentissage few-shot. En réponse à ce prompt, le modèle fait une prédiction raisonnable de la classe **« Moyen** » (comme indiqué en **gras).**

Remarque : le prompt a été exécuté avec IBM [watsonx.ai](https://www.ibm.com/fr-fr/products/watsonx-ai) Prompt Lab en mode « Freeform ».

*Définis le nom de classe pour le problème décrit : Élevé, Moyen ou Faible. J’ai fourni quelques exemples de problèmes et les noms de classe correspondants. Prévois uniquement le nom de la classe pour le dernier problème. Fournis une brève description de la raison pour laquelle ce nom de classe a été choisi.*

*Nom de la classe : Élevé\
Description : il s’agit d’un problème qui a un coût commercial élevé, qui affecte de nombreux utilisateurs ou les deux.*

*Nom de la classe : Moyen\
Description : un problème qui se situe quelque part entre les niveaux élevé et bas.*

*Nom de la classe : Faible\
Description : il s’agit d’un problème qui a un impact sur quelques utilisateurs, qui n’a pas de coût d’entreprise élevé, ou les deux.*

*Problème : les nouveaux utilisateurs signalent qu’ils ne peuvent pas créer de comptes.\
Classe : Élevé*

*Problème : un utilisateur signale que les libellés se chevauchent dans la fonction analytique de l’application.\
Classe : Faible*

*Problème : les utilisateurs aux États-Unis signalent que l’application se bloque lorsqu’ils tentent d’effectuer un achat.\
Classe : Élevé*

*Problème : les utilisateurs signalent que les images ne se chargent pas dans l’application.*

Classe : **Moyen**

**Explication : le problème des images qui ne se chargent pas dans l’application a une incidence sur l’expérience des utilisateurs et peut engendrer de la frustration, mais cela n’a pas un coût élevé pour l’entreprise et n’affecte pas de nombreux utilisateurs. Elle est donc classée comme étant problème moyen.**

L’apprentissage few-shot, qui est une stratégie dérivée du paradigme [d’apprentissage few-shot](https://www.ibm.com/fr-fr/think/topics/few-shot-learning), est généralement utilisé pour améliorer la performance du modèle par rapport à l’apprentissage zero-shot sur une tâche.[1](#f1) Dans cet exemple, les modèles IA produisent des inférences utiles dans les scénarios d’apprentissage zero-shot et d’apprentissage few-shot. Pour décider d’utiliser l’apprentissage zero-shot ou l’apprentissage few-shot, il faut prendre en compte les contraintes du problème et les performances démontrées des deux stratégies. Reynolds et McDonell (2021) ont constaté qu’avec des améliorations de la structure des prompts, l’apprentissage zero-shot peut être plus performant que l’apprentissage few-shot dans certains scénarios.[4](#f4) Schulhoff et al. (2024) trouvent des résultats différents en comparant les performances de plusieurs stratégies de prompting.[5](#f5)

## Avantages et limites de l’apprentissage zero-shot

L’apprentissage zero-shot est une approche populaire en raison de ses avantages.[6](#f6) Les chercheurs continuent à développer des techniques pour pallier les limites de ces techniques de prompting.[8](#f8)

**Avantages**

1.  **Simplicité :** les prompts sont simples à créer et faciles à comprendre. Cette approche permet aux utilisateurs d’expérimenter différents prompts sans connaissances approfondies en prompt engineering. 
2.  **Facilité d’utilisation :** l’apprentissage zero-shot ne nécessite aucune donnée supplémentaire, ce qui le rend utile dans les cas où les données pertinentes sont difficiles à trouver ou rares.
3.  **Flexibilité :** les prompts sont faciles à adapter selon les besoins. L’amélioration ou la mise à jour d’un prompt en raison de changements de circonstances ne nécessite que peu d’efforts.

**Limites**

1.  **Variabilité des performances** : si l’apprentissage zero-shot peut être efficace, ses performances peuvent varier considérablement en fonction de la complexité et de la spécificité de la tâche. Les modèles peuvent rencontrer des difficultés avec les tâches qui nécessitent des connaissances approfondies dans un domaine, une compréhension nuancée ou des résultats très spécifiques, ce qui conduit à des résultats insatisfaisants par rapport aux modèles affinés spécifiques à une tâche.
2.  **Dépendance envers la qualité du modèle pré-entraîné :** le succès de l’apprentissage zero-shot dépend fortement de la qualité et de l’exhaustivité du modèle de langage pré-entraîné. Si le modèle n’est pas suffisamment exposé à certains sujets, langages ou contextes pendant le pré-entraînement, ses performances zero-shot sur les tâches connexes seront probablement médiocres.

Les progrès des méthodes d’entraînement pour les LLM ont amélioré la production des modèles pour l’apprentissage zero-shot dans divers cas d’utilisation.[7](#f7)

## Amélioration des performances de l’apprentissage zero-shot

L’apprentissage zero-shot repose sur les connaissances pré-entraînées du modèle de fondation et sa flexibilité pour s’adapter au prompt demandé et fournir une réponse appropriée.[1](#f1)

L’amélioration des réponses dans le scénario zero-shot est l’une des priorités des chercheurs.[1 ](#f1)La précision de la réponse aux prompts zero-shot est souvent utilisée pour évaluer la performance des modèles tout en testant de nouvelles méthodes d’entraînement des modèles.[7](#f7) Le réglage des instructions et [l’apprentissage par renforcement avec les commentaires humains](https://www.ibm.com/fr-fr/think/topics/rlhf) (RLHF) sont les deux améliorations qui ont entraîné une meilleure performance de l’apprentissage zero-shot.[8,](#f8) [9](#f9)

Dans le réglage des instructions, un modèle est réglé en utilisant un apprentissage supervisé sur un jeu de données qui comprend des instructions pour diverses tâches et les résultats de ces tâches. Le jeu de données comprend des tâches telles que la synthèse de textes, la conversion et la compréhension de lecture. Cette stratégie de réglage fin avec un jeu de données d’instructions a permis d’améliorer les performances de l’apprentissage zero-shot pour les nouvelles tâches de ces catégories.[8](#f8)

Un autre exemple d’utilisation du réglage fin pour améliorer les résultats de l’apprentissage zero-shot est le réglage fin du RLHF, dans lequel [l’apprentissage par renforcement](https://www.ibm.com/fr-fr/think/topics/reinforcement-learning) apprend une politique qui guide le modèle vers de meilleurs résultats. Dans ce processus en trois étapes, le modèle est d’abord affiné à l’aide d’un jeu de données d’instructions dans lequel les humains ont fourni les réponses cibles. Ensuite, le modèle projette les résultats vers plusieurs prompts classés par des humains. Enfin, les résultats classés sont utilisés pour entraîner un modèle d’apprentissage par renforcement qui apprend une politique pour sélectionner les meilleures sorties sur la base de ces classements fournis par l’humain.[12](#f12)

La dernière étape utilise la capacité de l’apprentissage par renforcement à utiliser les conséquences (récompenses ou pénalités) des actions (décision ou chemin pris) pour apprendre une stratégie (ou une politique) permettant de prendre de bonnes décisions. Dans ce cas, l’espace du problème est constitué de l’ensemble des stratégies potentielles qui pourraient être utilisées pour sélectionner une bonne sortie à titre de réponse.[9](#f9)

## Applications de l’apprentissage zero-shot

En comparaison avec le machine learning supervisé traditionnel pour le traitement automatique du langage naturel (NLP), l’apprentissage zero-shot n’a pas besoin de données d’entraînement étiquetées. Les praticiens de l’intelligence artificielle et les data scientists peuvent utiliser la technologie d’IA générative des grands modèles de langage dans le scénario d’apprentissage zero-shot pour divers cas d’utilisation, notamment :[10](#f10)

**Classification de texte**

Comme le montre l’exemple précédent de classification de la priorité des problèmes informatiques avec le modèle granite-3-8b-instruct d’IBM, le modèle peut effectuer la classification sans exemples antérieurs appartenant aux différentes classes. Cette fonctionnalité est idéale pour les situations où les données d’entraînement étiquetées sont limitées ou inexistantes. Ce tutoriel de [classification zero-shot](https://www.ibm.com/fr-fr/think/tutorials/zero-shot-classification "https://www.ibm.com/fr-fr/think/tutorials/zero-shot-classification") montre une implémentation de ce cas d’utilisation.

**Extraction d’informations**

À partir d’un corps de texte et d’une question, un LLM peut extraire les informations demandées conformément à un prompt.

**Réponse aux questions**

En utilisant les connaissances pré-entraînées d’un modèle, un utilisateur peut obtenir une réponse à une question.

**Synthèse de texte**

À partir d’un texte et d’une instruction de synthèse de texte, les grands modèles de langage peuvent exécuter cette tâche dans le scénario de prompt zéro-shot sans avoir besoin d’exemples de résumés d’autres textes.

**Génération**

Les LLM génèrent des données sous forme de texte, de code, d’images et plus encore pour des cas d’utilisation donnés.

**Conversation**

En utilisant généralement des modèles adaptés pour le chat (tels que la série chat-GPT bien connue), les LLM peuvent interagir avec un utilisateur en mode chat, réalisant ainsi de nombreux cas d’utilisation précédents.

## Autres méthodes de prompt engineering

Pour les cas d’utilisation complexes tels que les tâches de raisonnement à plusieurs étapes, l’apprentissage zero-shot et l’apprentissage few-shot peuvent ne pas produire une réponse appropriée à partir du modèle. Les techniques de prompting avancées, notamment la chaîne de pensée et l’arbre des pensées, peuvent être plus efficaces pour ces cas plus complexes.

[Chaîne de pensée](https://www.ibm.com/fr-fr/think/topics/chain-of-thoughts) : l’apprentissage par chaîne de pensée (CoT) est une stratégie qui impose une tâche au modèle en spécifiant la tâche la plus importante sous la forme d’une série d’étapes distinctes à résoudre. Cette exposition des étapes intermédiaires améliore la capacité du modèle à générer une réponse correcte. Le CoT assure également une meilleure transparence dans le processus de résolution des problèmes en élucidant les étapes intermédiaires. Cette technique de prompt engineering donne de bons résultats dans des domaines tels que l’amélioration des performances des chatbots de service client, en aidant à organiser les pensées des chercheurs et des rédacteurs et en générant des descriptions étape par étape pour les problèmes pédagogiques en mathématiques et en sciences.[11](#f11)

[Arbre des pensées](https://www.ibm.com/fr-fr/think/topics/tree-of-thoughts): l’arbre de pensée (ToT) génère une arborescence de texte ramifiée montrant les différentes étapes suivantes et des solutions associées au problème. Cette arborescence permet au modèle de découvrir plusieurs chemins et de faire marche arrière, si nécessaire, lorsqu’un chemin ne découvre pas une solution acceptable. Il est conçu pour rapprocher les stratégies de raisonnement humain lors de la comparaison des chemins potentiels vers une solution. Les stratégies courantes pour découvrir des solutions sont l’algorithme de parcours en largeur (BFS) et l’algorithme de parcours en profondeur (DFS), ainsi que les approches de recherche heuristique et d’apprentissage par renforcement. Les chercheurs ont utilisé cette application pour résoudre des énigmes telles que le sudoku et le puzzle 24.[12,](#f12) [13](#f13)
