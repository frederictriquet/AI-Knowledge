> Source : https://www.ibm.com/fr-fr/think/topics/prompt-chaining

# Qu'est-ce que le prompt chaining ?

##

Le prompt chaining est une technique de traitement automatique du langage naturel (NLP) qui tire parti de grands modèles de langage (LLM) et qui consiste à générer la sortie souhaitée en suivant une série de prompts. Dans ce processus, un modèle NLP reçoit une séquence de prompts qui le guident pour produire la réponse souhaitée. Le modèle apprend à comprendre le contexte et les relations entre les prompts, lui permettant de générer un texte cohérent et riche en contexte\[1\].

  Concept de prompt chaining

Ce concept est une implémentation avancée du prompt engineering. Il suscite un certain intérêt dans le domaine du NLP en raison de sa capacité à améliorer la qualité et la contrôlabilité de la génération de texte. Une chaîne de prompts efficace peut être préférée à d’autres techniques d’ingénierie, telles que les modèles zero-shot, few-shot ou les modèles affinés personnalisés\[2\]. En proposant une direction et une structure claires, le prompt chaining aide le modèle à mieux comprendre les intentions de l’utilisateur et à produire des réponses plus précises et plus pertinentes.

Le prompt chaining peut améliorer l’efficacité de l’assistance basée sur l’IA dans divers domaines. En décomposant les tâches complexes en prompts plus petits et en les enchaînant, les développeurs peuvent créer des réponses plus personnalisées et plus précises, adaptées aux besoins de chaque utilisateur. Cette approche améliore non seulement l’expérience utilisateur globale, mais permet également une personnalisation et une adaptabilité accrues face à l’évolution des besoins des utilisateurs ou des scénarios d’application\[3\].

## Types de prompts

Il existe deux principaux types d’invites générées lors de l’utilisation de LLM. Ce sont :

### Les invites simples

Il s’agit d’invites de base qui contiennent une seule instruction ou une seule question à laquelle le modèle doit répondre. Elles sont généralement utilisées pour initier une conversation ou demander des informations. Voici un exemple de prompt simple : « Quel temps fait-il aujourd’hui ? »

### Les invites complexes

Ces invites contiennent plusieurs instructions ou questions qui demandent au modèle d'effectuer une série d'actions ou de fournir une réponse détaillée. Elles sont souvent utilisées pour faciliter des tâches plus avancées ou pour engager des conversations plus approfondies. Un exemple d'invite complexe serait : « Je recherche un restaurant qui sert de la nourriture végétalienne et qui est ouvert jusqu'à 22 heures. Pouvez-vous m'en recommander un ? »

## Simplifier des prompts complexes

La conversion d'une invite complexe en une série d'instructions simples peut aider à décomposer une tâche complexe en sous-tâches plus petites. Cette approche permet aux utilisateurs de comprendre plus facilement les étapes nécessaires pour traiter une demande et de réduire les risques d'erreurs ou de malentendus.

  Conversion d'une invite complexe en invite simple

### Un exemple : la traduction linguistique

Considérez le scénario où nous avons des informations en langue espagnole. Nous devons extraire ces informations, mais nous ne comprenons pas l'espagnol. Tout d'abord, nous devons traduire le texte de l'espagnol en anglais. Ensuite, nous devons poser une question pour extraire les informations, puis traduire à nouveau les informations extraites de l'anglais vers l'espagnol. Il s’agit d’une tâche complexe, et si nous essayons de combiner ces étapes dans une seule invite, elle sera trop complexe, ce qui augmentera la probabilité d’erreurs supplémentaires dans la réponse. Par conséquent, il est préférable de convertir une invite complexe en une séquence d'invites simples. Voici quelques étapes à suivre :

1.  Identifiez le but ou l’objectif principal de l’invite. 
2.  Décomposez l’objectif principal en sous-tâches, c’est-à-dire en actions ou tâches plus spécifiques.
3.  Créez une invite pour chaque action ou tâche spécifique.
4.  Veillez à ce que chaque message soit clair, concis et sans ambiguïté.
5.  Testez les invites pour vous assurer qu'elles sont faciles à comprendre et complètes.

Voici notre invite complexe : « Considérez le texte donné en espagnol. Traduisez-le en anglais. Retrouvez toutes les statistiques et tous les faits utilisés dans ce texte et répertoriez-les sous forme de puces. Traduisez-les à nouveau en espagnol. »

Pour convertir cette invite complexe en invites simples, nous pouvons décomposer l'objectif principal en actions ou tâches plus petites, et nous pouvons créer une chaîne d'invites comme ci-dessous :

1.  « Lire le texte espagnol donné. »
2.  « Traduire le texte en anglais ».
3.  « Récupérer les statistiques et les faits du texte. »
4.  « Créer une liste à puces de tous ces faits. »
5.  « Les traduire en espagnol. »

  Exemple de prompt chaining, traduction et extraction d'informations

## Créer une chaîne de prompts

Une chaîne de prompts structurée est un ensemble prédéfini de prompts ou de questions conçues pour guider l’utilisateur à travers une conversation ou une série d’actions spécifiques, assurant ainsi un flux d’informations cohérent et contrôlé\[4\]. Cette technique est souvent utilisée dans le support client, le tutorat et d’autres systèmes interactifs pour maintenir la clarté, la précision et l’efficacité de l’interaction. Les prompts d’une chaîne sont généralement liés, ce qui permet au système de s’appuyer sur les réponses précédentes et de conserver le contexte. Cette approche peut contribuer à réduire l’ambiguïté, à améliorer la satisfaction des utilisateurs et à permettre une communication plus efficace entre les humains et les machines.

#### Créez une bibliothèque de référence avec différents modèles d’invites

Commencez par rassembler une série d’invites pré-écrites qui peuvent être personnalisées pour différents scénarios. Ces modèles doivent couvrir les tâches, les demandes et les questions courantes que les utilisateurs pourraient rencontrer.

#### Définissez les invites principales

Identifiez les questions ou instructions fondamentales qui doivent être transmises dans la chaîne d’invites. Ces invites doivent être simples, claires et directes, et elles doivent pouvoir être prises seules en tant qu’invites individuelles.

#### Identifier les entrées et les sorties de la séquence d’invites

Déterminez les informations ou les actions spécifiques que l'utilisateur doit fournir en réponse à chaque demande. Ces entrées doivent être clairement définies et faciles à comprendre, et doivent être liées aux invites correspondantes dans la chaîne d'invites.

#### Mettre en œuvre l’ensemble de la chaîne d’invites

Utilisez la bibliothèque de référence et les invites principales pour créer la chaîne d’invites complète. Assurez-vous que chaque invite est logiquement liée à la suivante et que l'utilisateur est invité à saisir les entrées nécessaires aux points appropriés de la séquence.

#### Testez la chaîne d'invites

Une fois la chaîne d’invites créée, testez-la soigneusement pour vous assurer qu’elle est facile à comprendre et à compléter. Demandez à un échantillon d’utilisateurs de compléter la chaîne d’invites et de recueillir des commentaires sur les domaines à améliorer.

#### Itérez et affinez la chaîne d’invites

En fonction des commentaires reçus lors des tests, apportez les ajustements ou améliorations nécessaires à la chaîne d’invites. Cela peut inclure la réécriture de certaines invites, l’ajout ou la suppression d’invites, ou la modification de l’ordre dans lequel les invites sont présentées.

En suivant ces étapes, les représentants du service client et les programmeurs peuvent créer des chaînes d'invites efficaces qui guident les utilisateurs à travers une série d'actions ou de tâches.

### Les avantages d'un prompt chaining

Le prompt chaining présente plusieurs avantages par rapport aux méthodes classiques utilisées dans le prompt engineering. En guidant le modèle à travers une série d'invites, le prompt chaining renforce la cohérence et l'homogénéité de la génération de texte, ce qui permet d'obtenir des résultats plus précis et plus engageants.

Cohérence

En exigeant que le modèle suive une série d’incitations, le prompt chaining permet de maintenir la cohérence dans la génération de texte. Ceci est particulièrement important dans les applications où le maintien d’un ton, d’un style ou d’un format cohérent est crucial, comme dans les fonctions de support client ou de rédaction\[5\].

Dans le support client, le prompt chaining peut être utilisé pour assurer une communication cohérente avec les utilisateurs. Par exemple, le bot peut être invité à s'adresser à l'utilisateur en utilisant le nom de son choix ou à suivre une tonalité spécifique tout au long de la conversation.

Créez des assistants IA pour le service client avec watsonx assistant

Contrôle renforcé

Le prompt chaining offre un meilleur contrôle sur la génération de texte, ce qui permet aux utilisateurs de spécifier la sortie souhaitée avec précision. Cette approche est particulièrement utile dans les situations où les données en entrée sont bruyantes ou ambiguës, car le modèle peut être invité à clarifier ou à affiner l’entrée avant de générer une réponse\[6\].

Dans un système de résumé de texte, le prompt chaining permet aux utilisateurs de contrôler le niveau de détail et de spécificité du résumé généré. Par exemple, l’utilisateur peut d’abord être invité à fournir le contenu qu’il souhaite résumer, comme un document de recherche. Une invite ultérieure peut suivre pour formater ce résumé dans un format ou un modèle spécifique.\

Découvrez comment vous pouvez effectuer des tâches pour résumer des textes avec watsonx.ai (2:19)

Taux d'erreur réduit

Le prompt chaining permet de réduire les taux d’erreur en fournissant au modèle un meilleur contexte et des entrées plus ciblées. Un prompt chaining structuré est utile pour réduire les efforts humains et valider le code et les sorties plus rapidement. En décomposant l’entrée en prompts plus petits et plus gérables, le modèle peut mieux comprendre les intentions de l’utilisateur et générer des réponses plus précises et plus pertinentes\[7\].

Dans un système de traduction automatique, avant de traduire une phrase, le système peut d’abord inviter l’utilisateur à spécifier la langue source, la langue cible et tout contexte ou terminologie pertinent. Cela permet au modèle de mieux comprendre le texte source et de générer une traduction plus précise.

En tirant parti de ces avantages, le prompt chaining peut améliorer considérablement les performances et l’efficacité des modèles de NLP dans diverses applications, du support client à la rationalisation de la rédaction et de la traduction.

## Cas d'utilisation du prompt chaining

Le prompt chaining est une technique polyvalente qui peut être appliquée à un large éventail de cas d’utilisation, se répartissant principalement en deux catégories : les réponses aux questions et les tâches en plusieurs étapes.

### Réponse aux questions

Comme leur nom l’indique, les tâches de réponse aux questions fournissent des réponses aux questions fréquemment posées par les humains. Le modèle automatise la réponse en fonction du contexte à partir de documents généralement trouvés dans une base de connaissances. Les applications courantes incluent :\

- **Service client/assistance :** le prompt chaining peut aider les utilisateurs à interroger la base de connaissances d’une entreprise pour trouver la réponse la plus pertinente, ce qui améliore l’expérience de l’utilisateur et son efficacité\[8\].
- **Plateformes pédagogiques :** les formateurs peuvent créer des expériences d’apprentissage interactives en posant des questions aux étudiants en fonction de leurs progrès, ce qui permet un apprentissage personnalisé et adaptatif \[9\].
- **Aide à la recherche :** les chercheurs peuvent utiliser le prompt chaining pour automatiser le processus de recherche et d’analyse de la littérature pertinente, ce qui leur permet de gagner du temps et d’économiser des ressources\[3\]\[10\].

### Tâches en plusieurs étapes

Comme on pouvait s’y attendre, les tâches en plusieurs étapes sont composées d’une séquence d’étapes permettant d’atteindre un objectif donné. En voici quelques exemples :\

- **Création de contenu :** le prompt chaining peut rationaliser les différentes étapes du processus de création de contenu, telles que la recherche sur un thème, la création d’un plan, la rédaction d’un article, la validation du contenu, la correction et plus encore\[11\]\[12\].
- **Développement de la programmation** : le prompt chaining peut guider les développeurs à travers une série d’étapes, en commençant par la logique de base, en passant au pseudo-code et enfin à l’implémentation d’un code spécifique dans un langage donné, tout en garantissant la validation du code\[3\]\[13\].
- **Recommandations personnalisées :** ce cas d’utilisation s’applique à divers secteurs, où le prompt chaining permet d’adapter les recommandations en fonction des préférences, du comportement et des données historiques de l’utilisateur\[14\].

Le prompt chaining est une technique puissante qui peut être utilisée dans de nombreuses applications en temps réel pour aider les utilisateurs et les professionnels à effectuer une série d'actions ou de tâches. En décomposant les tâches complexes en une série d’invites plus simples, le prompt chaining permet de s’assurer que les utilisateurs et les professionnels comprennent les étapes nécessaires pour répondre à une demande et offrir une meilleure expérience globale. Qu’il soit utilisé dans le service client, la programmation ou la formation, le prompt chaining peut contribuer à simplifier des processus complexes et à améliorer l’efficacité et la précision.
