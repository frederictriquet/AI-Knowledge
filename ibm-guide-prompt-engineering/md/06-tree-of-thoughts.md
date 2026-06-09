> Source : https://www.ibm.com/fr-fr/think/topics/tree-of-thoughts

# Qu’est-ce que l’arbre des pensées ?

L’arbre de pensées (ToT) est un cadre révolutionnaire conçu pour améliorer les capacités de raisonnement des grands modèles de langage (LLM). Cette approche simule les stratégies cognitives humaines pour la résolution de problèmes, permettant aux LLM d’explorer de multiples solutions potentielles de manière structurée, un peu comme les ramifications d’un arbre.\[1\]

## Comment fonctionne l’arbre de pensées ?

Le ToT guide les LLM à travers une série d’étapes de raisonnement, où chaque étape peut se diviser en plusieurs cheminements, permettant au modèle de revenir en arrière ou d’explorer des stratégies alternatives selon ses besoins. Par exemple, la résolution d’un sudoku peut guider le modèle dans l’exploration de différents placements de chiffres par essais et erreurs. Il fait marche arrière lorsqu’un nombre mène à une contradiction et essaie un autre nombre jusqu’à ce que le jeu soit résolu. Cette expérience imite l’approche humaine de résolution des problèmes, dans laquelle plusieurs solutions sont prises en compte et rejetées si elles sont jugées incorrectes.[\[1\]](#f01)[\[3\]](#f03)

### Cadre pour l’arbre des pensées (ToT)

L’arbre de pensées (ToT) est un cadre sophistiqué conçu pour améliorer les capacités de résolution de problèmes des LLM en structurant leur raisonnement d’une manière analogue aux processus cognitifs humains. Le cadre est composé de quatre éléments clés :

#### **Décomposition de la pensée**

Le cadre des exigences ToT décompose explicitement un problème en étapes plus petites et gérables appelées pensées, qui sont regroupées pour former une solution. Chaque idée doit avoir la bonne taille, ni trop grande pour être gérée ou trop petite pour être utile. Par exemple, si vous planifiez un voyage, une réflexion peut vous amener à choisir d’abord une destination, puis le meilleur mode de transport et enfin un endroit où séjourner. Dans un problème mathématique, une pensée peut être une seule ligne d’équation ou une explication concise d’un concept. Ainsi, le problème est décomposé en étapes clés, faciles à aborder et à évaluer individuellement. La décomposition dépend de la nature du problème, en veillant à ce que les pensées soient à la fois significatives et réalisables pour l’évaluation.

#### **Génération de pensées**

Après avoir défini ce qui constitue une pensée, l’étape suivante consiste à déterminer comment ces pensées sont générées. Le cadre propose deux techniques principales.[\[4\]](#f04)

- **Échantillonnage :** cette technique consiste à générer plusieurs pensées indépendamment en utilisant la même invite. Cette méthode fonctionne mieux lorsque l’espace de pensée est riche et diversifié, car les pensées générées indépendamment sont moins susceptibles d’être dupliquées. Par exemple, en écriture créative, plusieurs idées d’élaboration indépendantes peuvent être générées.
- **Proposition :** cette technique génère des pensées de manière séquentielle à l’aide d’une « invite de proposition ». Chaque pensée est fondée sur la précédente, ce qui permet d’éviter les doublons dans des espaces de pensée plus contraints. Par exemple, dans la résolution logique de problèmes, chaque étape s’appuie sur la précédente pour assurer la cohérence et la progression.

#### **Évaluation des états**

Une fois les idées générées, elles doivent être évaluées pour garantir la progression vers une solution. À cette fin, le cadre utilise deux stratégies :

- **Valeur :** cette stratégie consiste à attribuer une valeur scalaire (par exemple, une note de 1 à 10) ou une classification (par exemple, sûr, probable ou impossible) à chaque état. Cela permet d’indiquer la qualité de la valeur ou sa probabilité de conduire à une solution. Cette méthode permet une évaluation quantitative du potentiel de chaque pensée.
- **Vote :** cette stratégie compare différentes solutions et sélectionne la plus prometteuse. Le vote est particulièrement utile pour les tâches où la qualité d’une solution est subjective ou difficile à quantifier, comme dans la rédaction créative ou la planification stratégique. De multiples évaluations se combinent pour déterminer la meilleure voie à suivre.

#### **Algorithme de recherche :**

Le composant final implique l’algorithme de recherche utilisé pour naviguer dans l’espace de la solution. Le cadre utilise généralement deux algorithmes fondamentaux :

- **Algorithme de parcours en largeur (BFS) :** cet algorithme explore toutes les branches possibles à chaque niveau avant d’aller plus loin dans l’arbre. Il garantit que toutes les solutions potentielles sont considérées de la même manière, ce qui le rend utile pour les problèmes où le chemin le plus court ou la solution la moins profonde est privilégié. Par exemple, dans un jeu de réflexion, le BFS vérifierait tous les mouvements immédiats avant d’envisager les suivants.
- **Algorithme de parcours en profondeur (DFS) :** cet algorithme explore en profondeur une branche avant de revenir en arrière pour explorer d’autres branches. Il permet un examen approfondi de chaque solution potentielle, ce qui le rend utile pour les problèmes nécessitant une exploration détaillée de chaque option. Par exemple, pour résoudre un problème de logique complexe, le DFS suivrait en profondeur une seule hypothèse, vérifiant sa validité avant d’envisager des alternatives.

En intégrant ces composants, le cadre ToT imite la résolution humaine des problèmes en tenant systématiquement compte de plusieurs solutions et en éliminant les solutions jugées incorrectes.

La dynamique opérationnelle du cadre ToT implique une exploration itérative et en arborescence des solutions possibles. À partir de la question initiale, le modèle génère une série de réflexions ou de réponses, chacune conduisant à des questions ou à des développements ultérieurs. Ces branches se développent au fur et à mesure que le modèle explore différentes voies de raisonnement. Il permet de suivre les progrès et d’explorer l’ensemble de cet espace de solutions grâce à une auto-évaluation basée sur le LLM qui permet de garantir la validité de chaque étape. Si un raisonnement aboutit à une contradiction ou à une impasse, le système peut revenir à un nœud précédent pour explorer d’autres possibilités.

Cette approche structurée mais flexible permet aux LLM de gérer plus efficacement des tâches de raisonnement complexes à plusieurs étapes. Elle ressemble à la capacité humaine de naviguer dans un labyrinthe de pensées et d’options, en réévaluant et en ajustant les stratégies selon les besoins.

En substance, le cadre ToT dote les LLM d’une capacité de raisonnement et de résolution des problèmes plus proche de celle de l’homme, ce qui renforce leur efficacité dans les tâches qui exigent une réflexion et une prise de décision stratégiques et approfondies.

## Différence entre la chaîne des pensées (CoT) et l’arbre des pensées (ToT)

Les cadres de l’arbre de pensées (ToT) et de la chaîne de pensées (CoT) servent d’algorithmes conceptuels pour comprendre l’organisation et la progression de la génération de texte dans les modèles de langage (LMs) tels que les transformateurs génératifs pré-entraînés (par exemple, GPT-3 et GPT-4). Ces techniques d’incitation font partie de l’ingénierie rapide, qui consiste à créer des entrées (invites) pour guider efficacement les LMs dans la génération des résultats préférés.

**Invite de l’arbre de pensées :** ce cadre repose sur la capacité du modèle à générer du texte de manière hiérarchique, avec un sujet ou une idée centrale menant à des sous-sujets et à des détails ramifiés. Cette approche reflète la façon dont un modèle peut développer une invite spécifique en générant un texte de plus en plus spécifique et connexe, similaire à une structure d’arborescence. Elle permet des stratégies de recherche en amont et d’arborescence, où le modèle peut explorer plusieurs branches avant de s’engager sur une voie, ce qui la rend adaptée à la résolution de problèmes généraux et à des scénarios nécessitant une prise de décision complexe. Cette méthode intègre le raisonnement logique et l’heuristique pour évaluer la qualité de chaque branche. Le mécanisme de cohérence propre est utilisé pour fournir des évaluations fiables en sollicitant le modèle plusieurs fois.

Incitation à la chaîne de pensée : ce concept correspond à la capacité du modèle à générer du texte de manière linéaire, de gauche à droite, où chaque jeton suivant est directement influencé par les jetons précédents. Cette progression séquentielle reflète une approche plus simple et plus directe de la génération de texte. La CoT est efficace pour les tâches qui nécessitent un flux logique clair par étapes. L’apprentissage few-shot, où le modèle est fourni avec quelques exemples pour apprendre, peut améliorer cette méthode en fournissant une compréhension contextuelle. La CoT sert de technique de base dans le prompt engineering, offrant une méthode fondamentale plus simple à mettre en œuvre, mais qui peut ne pas offrir la profondeur et la complexité du ToT.

**Comparaison et applications :** ben que l’incitation par ToT incarne une approche plus complexe et plus interconnectée dans la génération de texte, en utilisant des stratégies de recherche en amont et par arborescence, la CoT reflète une progression séquentielle plus simple. La nature hiérarchique du ToT répond aux tâches nécessitant une exploration détaillée de plusieurs solutions, telles que les scénarios d’apprentissage par renforcement, où le retour en arrière et les stratégies alternatives sont essentiels. Cependant, la progression linéaire de la CoT est idéale pour les tâches qui nécessitent une séquence claire et logique de pensées.

Dans les applications pratiques, les API pour les modèles de langage, notamment GPT-3 et GPT-4, utilisent des techniques de prompting telles que le ToT et la CoT pour améliorer leurs performances dans diverses tâches, de l’écriture créative à la résolution de problèmes complexes.\[2\] Le prompt engineering continue d’évoluer, fournissant des outils puissants permettant d’exploiter les capacités des transformeurs avancés dans les modèles de langage.

## Avantages et limites de l’arbre de pensées

Le cadre ToT représente une avancée significative dans les capacités des LLM pour la résolution de problèmes complexes. Toutefois, la mise en œuvre de ce cadre implique des compromis.

### Avantages

Ce cadre offre des avantages au domaine de l’intelligence artificielle, notamment :

#### Des capacités améliorées de résolution de problèmes

Le ToT améliore considérablement les compétences de résolution de problèmes des LLM en leur permettant d’explorer plusieurs cheminements de raisonnement simultanément. Cela reflète les processus cognitifs humains dans lesquels plusieurs solutions potentielles sont envisagées et la plus viable est sélectionnée. Par exemple, dans les tâches nécessitant une réflexion stratégique ou une planification, comme la résolution de jeux de mots ou la génération d’écriture créative, le ToT a démontré des performances supérieures, obtenant des taux de réussite plus élevés que les méthodes traditionnelles. Cette capacité accrue de raisonnement complexe par décomposition des étapes intermédiaires est particulièrement évidente dans les tâches difficiles où les décisions initiales influencent considérablement les résultats.\[4\]

#### Gestion de l’incertitude

L’arbre de pensées incertaines (TouT), une extension du ToT, aborde spécifiquement les incertitudes inhérentes aux processus de prise de décision des LLM. En quantifiant et en gérant ces incertitudes, le TouT permet d’obtenir des résultats plus précis et plus fiables. Il utilise des techniques telles que le Monte Carlo Dropout. Cette technique est utilisée dans le machine learning, en particulier dans les modèles d’apprentissage profond, pour estimer l’incertitude des prédictions. Il s’agit d’abandonner aléatoirement des neurones pendant l’entraînement et l’inférence, ce qui crée plusieurs « chemins » différents à travers le réseau. En faisant la moyenne des prédictions de ces différents chemins, le modèle peut fournir des estimations plus fiables de l’incertitude. Cette technique est précieuse dans les applications où des prédictions précises et fiables sont essentielles, telles que le diagnostic médical ou les prévisions financières.\[5\]

### Limites

Outre les avantages, certaines limites inhérentes doivent être prises en compte.

#### Surcharge de calcul

Le cadre ToT implique des opérations complexes telles que le maintien de plusieurs chemins de décision, le retour en arrière et l’exploration de solutions alternatives. Ces processus sont intensifs en termes de calcul et nécessitent souvent des ressources importantes en termes de puissance de traitement et de mémoire. Le besoin de ressources peut limiter l’évolutivité du ToT, en particulier dans les environnements où les ressources informatiques sont limitées ou dans les applications en temps réel où des temps de réponse rapides sont essentiels.

#### Complexité de la mise en œuvre

La mise en place d’un système d’arbre de pensées implique l’intégration de divers composants tels que l’agent prompteur, le module de vérification, le module de mémoire et le contrôleur ToT.\[1\] Chaque composant doit être finement réglé pour fonctionner en harmonie, ce qui peut s’avérer un processus complexe et chronophage. En outre, l’efficacité du système dépend fortement de la qualité de sa mise en œuvre. La mauvaise configuration d’un composant peut réduire l’efficacité de l’ensemble du système, le rendant moins fiable ou conduisant à des cheminements de résolution de problèmes incorrects.

#### Inefficacité de la recherche

Des recherches récentes ont suscité des inquiétudes quant à l’efficacité de l’apprentissage de type ToT. L’étude souligne que le ToT peut conduire à une exploration redondante des chemins de raisonnement à faible valeur, ce qui entraîne des frais de calcul inutiles et une performance plus lente. Contrairement aux stratégies de planification plus ciblées, le ToT manque de mécanismes pour hiérarchiser les branches prometteuses, ce qui peut nuire à son efficacité dans les tâches de raisonnement complexes.[\[6\]](#f06)

\
Pour résoudre ces problèmes, les chercheurs proposent une approche alternative, appelée **« pensée de recherche »** (Thought of Search), qui intègre des heuristiques de planification et le gain d’information afin de guider plus efficacement le processus de raisonnement. Ces résultats suggèrent que si le ToT reste un cadre conceptuel puissant, sa mise en œuvre pourrait bénéficier d’une intégration avec des stratégies de recherche plus efficaces.[\[6\]](#f06)

## Études de cas

Le cadre ToT a démontré son efficacité dans diverses applications, mettant en valeur sa robustesse et son adaptabilité. Nous explorons ici 4 études de cas convaincantes dans lesquelles le ToT a considérablement amélioré ses capacités de résolution de problèmes :

### Résolution de sudoku

L’application du ToT dans la résolution de grilles de sudoku illustre sa capacité à relever des défis logiques complexes. En guidant le modèle à travers différents placements de chiffres et en lui permettant de revenir en arrière lorsqu’il rencontre des contradictions, le ToT rationalise le cheminement vers des solutions correctes. Cette capacité à réévaluer dynamiquement les décisions améliore considérablement la précision et l’efficacité de la résolution des problèmes, soulignant l’avantage du ToT par rapport aux approches de résolution de problèmes plus statiques[\[1\]](#f01).

### Puzzle 24

Dans le jeu d’arithmétique stratégique 24, le ToT a considérablement amélioré ses taux de réussite en permettant au modèle d’explorer plusieurs cheminements de calcul. Ce processus de raisonnement adaptatif a permis au modèle de résoudre des énigmes de manière plus créative et plus efficace, démontrant la capacité du ToT à améliorer la flexibilité cognitive dans la résolution de problèmes numériques.[\[4\]](#f04)

### Écriture créative

Le ToT a également été appliqué à des tâches d’écriture créative, pour lesquelles il permet aux LLM de générer des récits plus cohérents et plus adaptés au contexte. En structurant le processus de réflexion sous la forme d’un arbre ramifié, le modèle peut explorer différents développements de l’intrigue ou choix stylistiques et sélectionner ou réviser un texte à partir des résultats les plus prometteurs. Cette méthode a permis d’améliorer la qualité et l’authenticité du texte généré par les LLM, offrant ainsi une approche plus nuancée du storytelling automatisé.[\[4\]](#f04)

### Résolution de mots croisés 5 x 5

Une autre application remarquable du ToT est la résolution de mini-mots croisés 5 x 5. Le cadre permet au modèle d’envisager plusieurs choix de mots pour chaque indice de mots croisés, en les évaluant non seulement de manière isolée, mais aussi en fonction de leurs interactions avec les mots déjà placés. Cette approche d’évaluation itérative et holistique contribue à garantir une plus grande précision dans la résolution des énigmes et démontre la capacité du ToT à appliquer un raisonnement logique et contextuel à des tâches linguistiquement complexes. L’utilisation du ToT dans ce contexte met en évidence sa polyvalence et son efficacité dans les tâches qui nécessitent l’intégration de plusieurs types de connaissances et de stratégies de raisonnement.[\[4\]](#f04)

Ces études de cas illustrent les diverses capacités du cadre de l’arbre de pensées, de l’amélioration du raisonnement logique et numérique à la stimulation de la créativité et de la compréhension contextuelle dans les tâches basées sur le langage. Chaque exemple souligne le potentiel du ToT pour révolutionner la résolution de problèmes dans toutes les disciplines.

## Avancées récentes

Les progrès récents du ToT ont mis l’accent sur l’expansion de ses capacités et la résolution des défis inhérents à son application. Principaux développements :

### Quantification de l’incertitude 

L’introduction de l’arbre des pensées incertaines (TouT) marque une avancée significative dans la recherche sur le ToT. Le TouT améliore le ToT en intégrant des mécanismes de quantification de l’incertitude qui évaluent la fiabilité de chaque cheminement de décision. Ce développement est crucial pour les applications où les décisions doivent être prises dans des conditions d’incertitude et où le coût des erreurs peut être élevé.[\[5\]](#f04)

### Prise de décision globale 

D’autres recherches se sont concentrées sur l’amélioration des capacités de prise de décision globale des LLM lors de l’utilisation du ToT. Des études récentes ont introduit des boucles de rétroaction dans le cadre, permettant aux modèles d’apprendre des décisions passées et d’ajuster leurs processus de raisonnement en temps réel. Ce mécanisme de retour d’information itératif permet d’affiner le processus de prise de décision, le rendant plus dynamique et réactif face à l’évolution du contexte du problème. Ces améliorations visent à rapprocher les capacités de raisonnement des LLM des processus cognitifs humains, dans lesquels l’apprentissage basé sur les expériences passées joue un rôle crucial dans la prise de décisions futures.[\[4\]](#f05)

Ces récents développements montrent les efforts continus qui sont fournis pour affiner et développer le cadre ToT, afin de garantir son applicabilité et son efficacité dans des scénarios de résolution de problèmes de plus en plus complexes. Ces avancées permettent non seulement d’améliorer les capacités des LLM, mais aussi d’ouvrir de nouvelles voies de recherche et d’application dans le domaine de l’intelligence artificielle.

##### Notes de bas de page

\[1\] Long, J. (mai 2023). Large Language Model Guided Tree-of-Thought.

\[2\] Karthik Narasimhan, S. Y. (juillet 2023). Official Repository of Tree of Thoughts (ToT). [https://github.com/princeton-nlp/tree-of-thought-llm](https://github.com/princeton-nlp/tree-of-thought-llm)

\[3\] Pengfei Liu, W. Y. (2021). *Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing.* ACM Computing Surveys.

\[4\] Shunyu Yao, D. Y. (2023). Tree of Thoughts: Deliberate Problem Solving with Large Language Models. *ArXiv, abs/2305.10601.* \
[https://arxiv.org/abs/2305.10601](https://arxiv.org/abs/2305.10601)

\[5\] 5 Shentong Mo, M. X. (septembre 2023). Tree of Uncertain Thoughts Reasoning for Large Language Models. *ArXiv, *abs/2309.07694. [https://arxiv.org/abs/2309.07694](https://arxiv.org/abs/2309.07694)

\[6\] Katz, M., Kokel, H., Srinivas, K., & Sohrabi, S. (2024). *Thought of search: Planning with language models through the lens of efficiency*. In A. Globerson, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, & C. Zhang (Eds.), *Advances in Neural Information Processing Systems* (Vol. 37, pp. 138491–138568).
