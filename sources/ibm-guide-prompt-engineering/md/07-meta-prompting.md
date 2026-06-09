> Source : https://www.ibm.com/fr-fr/think/topics/meta-prompting

# Qu’est-ce que le méta-prompting ?

Imaginez un scénario. Vous posez une question à un [modèle d’IA](https://www.ibm.com/fr-fr/think/topics/ai-model), il vous donne une réponse, et c’est tout. Maintenant, donnez-lui un template testé lui montrant exactement comment résoudre un problème complexe et, soudain, il résoudra une catégorie entière, plus rapidement, plus intelligemment et avec plus de cohérence. C’est ce que permet le méta-prompting.  

Si les [grands modèles de langage](https://www.ibm.com/fr-fr/think/topics/large-language-models) (LLM) comme [ChatGPT](https://www.ibm.com/fr-fr/think/topics/chatgpt) d’OpenAI, Gemini de Google et les modèles [open source](https://www.ibm.com/fr-fr/think/topics/open-source) d’Anthropic peuvent gérer de nombreuses tâches, le raisonnement complexe n’est souvent pas leur point fort. Les méthodes actuelles telles que la [chaîne de pensée et l’arbre de pensée](https://www.ibm.com/fr-fr/think/topics/chain-of-thoughts) sont utiles, mais elles ne peuvent pas égaler le raisonnement humain. Le méta-prompting y remédie en donnant aux LLM un cadre structuré pour améliorer leur performance.

Le méta-prompting est une [technique avancée de prompt engineering](https://www.ibm.com/fr-fr/think/topics/prompt-engineering-techniques) qui consiste à donner aux LLM un template de prompt réutilisable, étape par étape, en langage naturel. Cette méthode permet au modèle de résoudre toute une catégorie de tâches complexes, au lieu de lui fournir un seul prompt pour résoudre un seul problème. Le méta-prompting apprend aux modèles d’IA à résoudre les problèmes en se concentrant sur la structure, la syntaxe et le schéma de raisonnement nécessaires pour obtenir la réponse finale. En d’autres termes, on utilise le [prompt engineering](https://www.ibm.com/fr-fr/think/topics/prompt-engineering) pour définir la manière dont le modèle doit réfléchir au problème, étape par étape, avant de produire la réponse finale.

Par exemple, un utilisateur demande à une IA de résoudre un système de deux équations linéaires, **x - y = 4 et 2x + 3y = 12.** En utilisant un méta-prompt, on peut guider l’IA pour :  

- Déterminer les coefficients de chaque équation.
- Choisir une méthode de résolution.
- Résoudre le problème étape par étape pour obtenir chaque variable.
- Introduire les valeurs dans les deux équations et vérifier le résultat.

Cette architecture est adaptable, assure des sorties de qualité et permet aux [agents IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) de traiter des problèmes complexes dans presque tous les domaines, avec peu de prompts.

## Comment fonctionne le méta-prompting ?

La technique de méta-prompting est basée sur des concepts mathématiques, la **théorie des types** et la **théorie des catégories**, qui offrent une méthode organisée d’associer les problèmes aux solutions.[1](#f01)

Cette approche est importante car elle assure une structure claire entre les tâches et leurs prompts, ce qui permet à l’IA de suivre facilement un template standard et de résoudre un large éventail de problèmes. L’idée de base de la théorie des catégories est de cartographier les relations. Une catégorie est un « monde » d’objets avec leurs relations. Dans le méta-prompting, nous pouvons considérer :  

- Une catégorie (T) comme étant un ensemble de tâches (par exemple, « résoudre un système d’équations »). 
- Une autre catégorie (P) comme étant l’ensemble de prompts structurés pour ces tâches. 
- Le foncteur de méta-prompting (M) traduit chaque tâche T en son prompt structuré correspondant dans P, tout en conservant la structure logique. 

Si vous modifiez la tâche (par exemple, les chiffres dans un problème de mathématiques), le cadre de raisonnement reste le même, et le prompt s’adapte en conséquence.

Ce scénario est renforcé par la théorie des types, qui garantit que la conception du prompt correspond au type de problème. En méta-prompting, le type peut être un « problème mathématique » ou une « requête de synthèse ». Il garantit que les tâches mathématiques bénéficient d’une structure de raisonnement spécifique aux mathématiques, tandis que les tâches de synthèse ont un template orienté synthèse qui préserve la précision, l’adaptabilité et empêche tout raisonnement non pertinent dans les tâches complexes.

Pour mettre ces concepts en pratique, le méta-prompting comporte trois étapes : 

**1. Déterminer la tâche (T) :** préciser la catégorie du problème, et non seulement le cas en question. 

**2. Associer la tâche à un prompt structuré (P) :** créer un template séquentiel organisé pour raisonner à l’aide du foncteur de méta-prompt (M). Les prompts peuvent être générés automatiquement par les agents IA, ou manuellement. 

**3. Exécuter et produire :** le LLM garantit une résolution des problèmes cohérente et compréhensible, en appliquant le prompt structuré et spécifique à l’entrée en question. \

### Exemple : méta-prompting pour équations linéaires

Dans l’exemple précédent (résoudre deux équations linéaires) : **\[ 2x + 3y = 12 et x - y = 4 \],** la tâche (T) est de « résoudre tout système de deux équations linéaires ». Le mappage génère un nouveau prompt (P) comme celui-ci : 

*« En tant que prof de mathématiques, explique comment résoudre étape par étape l’ensemble d’équations linéaires donné. \
2x + 3y = 12 and x - y = 4 »*

*Utiliser ce template structuré :*

*1 : Identifier les coefficients a1, b1, c1 de la première équation, et a2, b2, c2 de la seconde. *

*2 : Choisir une méthode de résolution (substitution ou élimination).  *

*3 : Si la méthode d’élimination est utilisée, multiplier une ou les deux équations jusqu’à ce que les coefficients de x ou y correspondent à la valeur absolue. *

*4 : Additionner ou soustraire les équations pour supprimer une variable.*

*5 : Calculer la variable restante.*

*6 : Pour trouver l’autre variable, entrer la valeur résolue dans l’une des équations initiales.*

*7 : Vérifier en remplaçant x et y dans les deux équations initiales.*

*8 : Synthétiser la réponse finale par (x, y). »*

Si les équations changent, le LLM peut quand même les résoudre et continuer à raisonner, car le foncteur fournit la même structure avec de nouveaux chiffres. Le résultat est un template rapide et bien pensé, qui permet aux [workflows d’IA](https://www.ibm.com/fr-fr/think/topics/ai-workflow) générative de résoudre les problèmes de manière fiable, adaptable et évolutive.

## Applications du méta-prompting

Le méta-prompting a été testé sur diverses tâches de raisonnement, de programmation et de création, et il surpasse souvent les modèles de prompting standard, et même les modèles affinés. Par exemple, sur le [jeu de données](https://www.ibm.com/fr-fr/think/topics/dataset) MATH contenant 5 000 problèmes mathématiques de niveau compétition, les chercheurs ont utilisé une méta-prompt zero-shot avec le LLM Qwen-72B. [Il a atteint une précision de 46,3 %, dépassant le score initial de GPT-4 de 42,5 %, et a battu les modèles affinés.](https://www.ibm.com/fr-fr/think/topics/fine-tuning) Le méta-prompt a fourni un cadre de raisonnement étape par étape, ce qui lui a permis de traiter les nouveaux problèmes sans utiliser d’exemples mémorisés.

Le méta-prompting gère le workflow de développement logiciel de la planification à la révision de code, permettant aux LLM de fonctionner comme des architectes, développeurs et testeurs. Par exemple, l’ajout d’un spécialiste Python à l’architecture de méta-prompting pour la génération et l’exécution du code a augmenté le pourcentage de réussite au puzzle de programmation Python de 32,7 à 45,8 %.[2](#f02) Il peut définir le ton et la structure lors du développement de contenu et itérer les documents pour obtenir des résultats riches. Par exemple, lors d’une tâche d’écriture de sonnets shakespeariens exigeant une structure poétique stricte, le méta-prompting a augmenté la précision de 62 % avec des prompts standard. Avec un interpréteur Python, la précision est passée à 79,6 %, contre 77,6 % sans lui, ce qui montre sa capacité à affiner le ton et la structure. 

Compte tenu de ces cas d’utilisation, le méta-prompting convertit les instructions complexes en étapes faciles à gérer, qui fournissent des résultats plus adaptés au domaine.

## Méta-prompting et autres techniques de prompting

Le méta-prompting diffère des techniques de prompting telles que le zero-shot et l’apprentissage few-shot en termes d’objectif et d’exécution.

Avec le [prompting zero-shot](https://www.ibm.com/fr-fr/think/topics/zero-shot-prompting), le LLM reçoit une tâche sans exemples et s’appuie uniquement sur le pré-entraînement. S’il convient aux tâches simples, il produit souvent un raisonnement incohérent sur les tâches complexes. Le méta-prompting améliore ce problème grâce à un template de prompt réutilisable et organisé, qui guide la résolution des problèmes et garantit des résultats cohérents et explicables.

L’[apprentissage few-shot](https://www.ibm.com/fr-fr/think/topics/few-shot-prompting) donne au modèle quelques exemples à imiter (par exemple, lui montrer trois problèmes de mathématiques résolus avant de lui demander d’en résoudre un quatrième). Cette méthode enseigne « par l’exemple », mais elle relie toujours le raisonnement du modèle à ces exemples. Le méta-prompting, quant à lui, présente le processus de résolution de problèmes dans un template généralisé, étape par étape, indépendant des exemples flexibles et réutilisables pour résoudre des classes entières de problèmes.

Contrairement au prompting de type chaîne de pensée, qui demande au modèle de réfléchir étape par étape, le méta-prompting définit les étapes à suivre pour un type de tâche donné, ce qui rend le processus de raisonnement plus adaptable. 

Cette capacité rend le méta-prompting particulièrement utile dans le cas de l’IA générative, des agents IA et des workflows complexes, où la fiabilité et l’adaptabilité sont essentielles.

## Types de méta-prompting

Le méta-prompting peut être appliqué de différentes manières selon qui crée le méta-prompt, comment il est généré et comment il est utilisé dans le workflow d’IA. 

### Méta-prompting fourni par l’utilisateur

Il s’agit du type de méta-prompting le plus simple. Un utilisateur, tel qu’un spécialiste ou un prompt engineer, rédige un template clair, étape par étape, pour la tâche. Le LLM suit cette structure pour trouver la réponse. Cette approche fonctionne bien lorsque vous savez exactement comment le problème doit être résolu et que vous souhaitez obtenir des sorties cohérentes et de qualité. Il faut donc du temps et du savoir-faire pour créer ces prompts pour un grand nombre de tâches différentes.

### Méta-prompting récursif (RMP)

Ici, le LLM ou l’agent IA crée la méta-prompt pour lui-même avant de résoudre le problème. Ce type se déroule en deux étapes : la première prend la description de la tâche et génère un prompt structuré, étape par étape ; la seconde utilise ce prompt pour produire la réponse finale. Ce type permet à l’IA d’adapter son processus de résolution de problèmes, ce qui le rend utile dans les scénarios zero-shot and few-shot, sans exemples prêts à l’emploi. L’inconvénient est que la qualité des sorties dépend de la qualité du prompt IA.

### Méta-prompting des modèles conducteurs

Ce type est utilisé dans les workflows complexes d’IA, où plusieurs LLM ou agents IA travaillent ensemble. Un modèle conducteur planifie le processus et crée différents méta-prompts pour chaque modèle spécialiste. Le conducteur décompose la tâche principale en sous-tâches, puis utilise les templates de prompt pour attribuer chaque partie au spécialiste approprié. Par exemple, un modèle gère les opérations arithmétiques, un autre écrit le code Python, et un autre vérifie les résultats. Ce travail d’équipe améliore la précision et l’adaptabilité, mais exige une plus grande puissance de calcul.

Le méta-prompting n’est pas seulement une méthode permettant d’améliorer les réponses de l’IA, mais aussi un moyen d’interagir avec les LLM. Au lieu de donner des instructions directes aux modèles d’IA, nous influençons leur processus de réflexion en leur apprenant à générer efficacement leurs propres prompts. Le méta-prompting permet une forme d’auto-optimisation de l’IA (le raisonnement et l’adaptabilité évoluent à chaque itération) qui contribue au développement de systèmes d’IA plus intelligents et autonomes.
