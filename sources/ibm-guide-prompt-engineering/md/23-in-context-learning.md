> Source : https://www.ibm.com/fr-fr/think/topics/in-context-learning

# Qu’est-ce que l’apprentissage contextuel ?

Le déploiement des [modèles d’IA](https://www.ibm.com/fr-fr/think/artificial-intelligence) pour assurer des tâches complexes telles que la synthèse de rapports, la réponse aux requêtes ou la traduction de documents s’accompagne souvent de défis importants. Ces modèles doivent généralement être entraînés à nouveau sur des [jeux de données](https://www.ibm.com/fr-fr/think/topics/dataset) volumineux et annotés, et faire l’objet de processus d'[optimisation](https://www.ibm.com/fr-fr/think/topics/fine-tuning) coûteux. Chaque nouvelle tâche ajoute de la complexité, ralentit l’innovation, augmente les dépenses et limite l’évolutivité de l’IA dans les divers cas d’utilisation.

Maintenant, imaginez une approche différente. Et si les modèles d’IA pouvaient s’adapter instantanément à de nouvelles tâches, sans avoir à les entraîner à nouveau, ni à leur fournir des données supplémentaires ? C’est la promesse que fait l’apprentissage contextuel (ICL), qui permet aux modèles d’IA d’apprendre des tâches de manière dynamique, en donnant simplement des exemples dans un prompt. Il élimine les goulots d’étranglement du [machine learning](https://www.ibm.com/fr-fr/think/topics/machine-learning) (ML) traditionnel et offre des solutions plus rapides, plus adaptables et plus rentables.

## Le mécanisme d’apprentissage contextuel

L’apprentissage contextuel (ICL) est une capacité d’IA avancée introduite par l’article fondateur « Language Models are Few-Shot Learners », qui a révélé GPT-3.[1](#f01) Contrairement à l’[apprentissage supervisé](https://www.ibm.com/fr-fr/think/topics/supervised-learning), lors duquel le modèle passe par une phase d’entraînement avec rétropropagation pour modifier ses paramètres, l’ICL s’appuie entièrement sur des modèles de langage pré-entraînés et garde leurs paramètres inchangés.

Le modèle d’IA utilise le prompt comme guide temporaire pour déduire la tâche et générer la sortie attendue. L’ICL reconnaît les relations entre les exemples du prompt, également appelés paires entrée-sortie, et applique le même mappage aux nouvelles entrées. Ce processus imite le raisonnement humain, à savoir résoudre de nouveaux problèmes en s’appuyant sur les analogies des expériences antérieures. Il exploite les schémas et les connaissances apprises lors du pré-entraînement, et s’adapte dynamiquement aux nouvelles tâches, ce qui le rend très flexible et efficace.

Essentiellement, l’apprentissage contextuel fonctionne en conditionnant un [grand modèle de langage](https://www.ibm.com/fr-fr/think/topics/large-language-models) (LLM) sur un prompt qui inclut un jeu d’exemples (paires entrée-sortie ou exemples contextuels) généralement écrits en langage naturel dans le cadre de la séquence d’entrée. Ces exemples, souvent tirés d’un jeu de données, ne sont pas utilisés pour entraîner à nouveau le modèle, mais sont introduits directement dans sa [fenêtre contextuelle](https://www.ibm.com/fr-fr/think/topics/context-window). Cette fenêtre, qui sert de mémoire temporaire pour générer des réponses cohérentes, indique la quantité de texte qu’un LLM peut traiter à la fois. Elle fait partie du modèle qui traite les entrées séquentielles.

Formellement, le prompt sera constitué de k exemples sous la forme de paires d’entrées/de sorties :

```
C={(x1 ,y1 ),(x2 ,y2 ),...,(xk ,yk )}
```

À partir d’une nouvelle entrée x et d’un espace de sortie candidat Y={y1,...,ym}, le modèle calcule la probabilité de chaque sortie possible en fonction du prompt :

```
P(yj ∣ x,C)
```

La prévision est déterminée en choisissant l’option qui a la probabilité la plus élevée :

```
 y^=argmaxyj∈YP(yj∣x,C)
```

Le modèle ne met pas à jour ses pondérations pendant ce processus. Au lieu de cela, en tirant parti de son architecture transformatrice d’[apprentissage profond](https://www.ibm.com/fr-fr/think/topics/deep-learning), le modèle apprend le schéma de manière dynamique en utilisant uniquement les exemples du prompt actuel.

Pour voir cette méthode en pratique, prenons comme exemple une tâche de classification des sentiments. Le prompt peut ressembler à ceci :

Avis : Le film était fantastique → Sentiment : positif

Avis : Je n’ai pas aimé l’histoire → Sentiment : négatif

Avis : La musique était agréable → Sentiment :

Le modèle complète la dernière ligne en prédisant « Positif » et en continuant la structure observée dans les mappings étiquette-entrée précédents. Cet exemple illustre l’[apprentissage few-shot](https://www.ibm.com/fr-fr/think/topics/few-shot-learning), lors duquel le modèle déduit la tâche et génère des réponses appropriées en fonction d’un nombre réduit d’exemples.

## Le rôle du prompt engineering dans l’apprentissage contextuel

Comme le succès du modèle d’IA dépend de ce qui est montré dans le prompt, le [prompt engineering](https://www.ibm.com/fr-fr/think/prompt-engineering) joue un rôle essentiel dans l’ICL. Le prompt engineering consiste à créer des prompts de qualité, informatifs et bien structurés, qui guident efficacement le modèle. Les prompts suivent généralement des templates en langage naturel, qui sont soigneusement choisis pour correspondre à ce que le modèle a vu lors du pré-entraînement. Toute variation dans la formulation, le format des étiquettes, l’ordre des exemples et même la ponctuation peut affecter la performance du modèle, surtout s’il s’agit d’un [petit modèle](https://www.ibm.com/fr-fr/think/topics/small-language-models) ou d’un cas extrême.

Il est important de noter que le prompt engineering n’est pas un mécanisme distinct, mais un ensemble de techniques fonctionnant dans le cadre du concept plus large d’apprentissage en contexte. Exemple :

- [Apprentissage zero-shot](https://www.ibm.com/fr-fr/think/topics/zero-shot-prompting) : la tâche est expliquée sans fournir d’exemples

<!-- -->

- [Apprentissage one-shot](https://www.ibm.com/fr-fr/think/topics/one-shot-prompting) : un seul exemple est inclus pour illustrer la tâche 

<!-- -->

- [Apprentissage few-shot](https://www.ibm.com/fr-fr/think/topics/few-shot-prompting) : plusieurs exemples sont fournis 

<!-- -->

- [Apprentissage chain-of-thought](https://www.ibm.com/fr-fr/think/topics/chain-of-thoughts) : chaque exemple inclut des étapes de raisonnement intermédiaires pour guider la logique du modèle

Ces stratégies de prompt sont souvent combinées avec des prompts few-shot et évaluées sur des [benchmarks](https://www.ibm.com/fr-fr/think/topics/llm-benchmarks) qui testent la généralisation. Même les paires entrée-sortie avec des étiquettes aléatoires peuvent améliorer la performance, ce qui démontre que le format et la distribution du prompt sont aussi importants que les étiquettes.

À mesure que nous passons des prompts ICL contrôlés à des systèmes complexes et réels, le défi n’est plus de créer des entrées statiques, mais de pratiquer une ingénierie contextuelle. Il s’agit d’une discipline émergente qui consiste à concevoir systématiquement toutes les entrées dont un LLM a besoin pour fonctionner de manière fiable dans des scénarios concrets.  

L’ingénierie contextuelle consiste à concevoir des systèmes dynamiques qui assemblent et fournissent au LLM les informations, les outils, les instructions et le format appropriés pour lui permettre d’effectuer sa tâche de manière fiable. Contrairement au [prompt engineering](https://www.ibm.com/fr-fr/think/topics/prompt-engineering-guide) statique, l’ingénierie contextuelle consiste à créer des entrées complètes, adaptées aux tâches, à partir de sources multiples telles que les entrées utilisateur, les interactions précédentes, les sorties d’outils et les données externes au moment de l’exécution. Cela garantit que les LLM reçoivent les données nécessaires dans une structure qu’ils peuvent interpréter efficacement. Cette approche est essentielle dans le cas des systèmes agentiques complexes, où les défaillances sont souvent liées à un manque de contexte ou un mauvais formatage, et non aux limitations du modèle. En intégrant outils, mécanismes de récupération et mémoire dans le processus de construction des prompts, l’ingénierie contextuelle comble le fossé entre le potentiel du modèle et sa performance en situation réelle.

## Comprendre l’apprentissage contextuel grâce à l’inférence et à l’optimisation

Alors que les premières explications considéraient l’ICL comme une répétition de schémas au niveau de la surface ou comme une prédiction du token suivant, les recherches plus récentes révèlent des processus plus profonds. Une explication convaincante présente l’ICL comme une forme d’inférence bayésienne, une méthode qui consiste à estimer les probabilités en mettant à jour les croyances avec des preuves.[2](#f02) Selon cette perspective, le modèle examine les exemples few-shot ou one-shot et en déduit un concept latent (une tâche ou une structure invisible, comme « il s’agit d’une classification des sentiments ») à partir du prompt. Au fur et à mesure que d’autres exemples contextuels sont ajoutés, le modèle gagne en assurance et améliore ses prédictions sans modifier ses [paramètres](https://www.ibm.com/fr-fr/think/topics/model-parameters).

Une autre explication relie l’ICL à la [descente de gradient](https://www.ibm.com/fr-fr/think/topics/gradient-descent), la méthode d’optimisation derrière la plupart des systèmes de machine learning pour minimiser les erreurs. Des études récentes ont montré que les [modèles de type transformer](https://www.ibm.com/fr-fr/think/topics/transformer-model) peuvent simuler en interne le processus d’apprentissage, en particulier pour des tâches simples telles que la [régression linéaire](https://www.ibm.com/fr-fr/think/topics/linear-regression). Même si aucune mise à jour de paramètre n’a lieu, le modèle se comporte comme s’il s’adaptait au prompt grâce à une boucle interne de raisonnement. Ce processus se déroule entièrement dans la fenêtre contextuelle du modèle.

Ces résultats suggèrent que l’ICL implique un comportement interne de type apprentissage pendant l’inférence, même dans les configurations [zero-shot](https://www.ibm.com/fr-fr/think/topics/zero-shot-learning) ou few-shot. Au lieu d’être des prédicteurs statiques, les LLM s’adaptent à la structure des tâches en temps réel à l’aide de prompts en langage naturel. Ce mélange d’inférence et d’apprentissage implicite fait de l’ICL une méthode efficace de s’attaquer à de nouvelles tâches sans avoir à entraîner à nouveau le modèle.

## Défis, limites et potentiel de l’apprentissage contextuel

### Défis et limites de l’apprentissage contextuel

**1. Échelle du modèle et sensibilité des paramètres **\
L’efficacité de l’ICL est fortement influencée par l’échelle et la conception des LLM. Les modèles plus grands démontrent des capacités émergentes plus importantes en ICL. Les petits modèles, quant à eux, ont souvent du mal à rivaliser avec les capacités d’apprentissage contextuel, car leurs paramètres n’ont pas la capacité nécessaire pour modéliser efficacement les tâches complexes.

**2. Qualité des données de pré-entraînement et biais** \
L’efficacité de l’apprentissage contextuel dépend de la diversité et de la qualité des données de pré-entraînement. Les modèles entraînés sur des jeux de données étroits ou biaisés peuvent reproduire ces limitations lors de l’inférence, ce qui entraîne une mauvaise généralisation et des problèmes d’équité. 

**3. Transfert de domaine et généralisation **\
Bien que les LLM fassent preuve d’une adaptabilité impressionnante, leur performance peut se dégrader lors des tâches hautement spécialisées. Pour des domaines tels que le droit ou la médecine, des démonstrations spécialisées, voire un réglage fin traditionnel peuvent encore être nécessaires.

**4. Éthique et équité **\
L’ICL peut involontairement conserver et renforcer les préjugés sociaux présents dans les données d’entraînement. Les prompts pouvant influencer le comportement des modèles, garantir des sorties éthiques et équitables dans les interactions dynamiques en temps réel reste un défi majeur.

**5. Problèmes de confidentialité et de sécurité **\
Les systèmes ICL utilisés dans des applications du monde réel peuvent mémoriser ou reproduire involontairement des informations sensibles, si ces données étaient présentes dans le corpus de pré-entraînement. Cette possibilité soulève des questions critiques en matière de respect de la vie privée, en particulier dans les domaines de la santé, de la justice et des assistants personnels.

**6. Sensibilité et stabilité des prompts **\
L’ICL est sensible à la conception des prompts. La moindre modification apportée au nombre, à l’ordre ou au format des exemples contextuels peut entraîner des changements importants au niveau des sorties. Garantir une performance constante devient alors difficile. 

### Orientations de recherche et stratégies d’optimisation

**1. Entraîner les modèles**

Afin d’améliorer l’apprentissage contextuel des LLM, les chercheurs explorent diverses options d’amélioration pendant ou immédiatement après l’entraînement des modèles.[3](#f03) L’une des principales orientations est le pré-entraînement sur des données structurées, lors duquel les paires entrée-sortie ou les clusters de tâches sont explicitement organisés. Cette approche permet aux modèles de devenir plus sensibles aux schémas et aux relations des tâches, au lieu de s’appuyer sur des distributions linguistiques généralistes.

Une autre approche efficace est la méta-distillation, selon laquelle le modèle est exposé à des formes de connaissances distillées et abstraites ; des paires d’exemples courts et informatifs qui transmettent l’essence de la tâche (par exemple, « Intrigue forte → positif », « Jeu d’acteur médiocre → négatif »). Cette méthode permet aux modèles de se généraliser rapidement pendant l’inférence, avec une surcharge de démonstration minimale.

L’entraînement d’échauffement affine le modèle entre le pré-entraînement et l’inférence réelle à l’aide d’exemples alignés sur les tâches sous forme de prompt. Par exemple, lui montrer quelques exemples de « Titre → Catégorie » avant le test augmente sa capacité à se généraliser au contenu connexe sans avoir à procéder à un nouvel entraînement.

Le réglage des instructions est une autre stratégie critique, qui consiste à entraîner les modèles à l’aide de milliers de tâches écrites sous forme d’instructions en langage naturel (par exemple, « Classer le ton de la phrase »). Cette stratégie améliore la généralisation few-shot et zero-shot en alignant plus étroitement le comportement du modèle sur les conseils humains.

**2. Créer un prompt**

La conception de prompt pendant l’inférence joue un rôle essentiel dans l’exploitation d’ICL. L’une des techniques les plus efficaces est la sélection des démonstrations : choisir les bons exemples à l’aide d’indicateurs de similarité, de scores d’incertitude ou de récupérateurs entraînés. 

Le reformatage des démonstrations modifie la structure des exemples. À la place des simples paires entrée-sortie, certaines méthodes utilisent des chaînes de raisonnement (par exemple, « Prémisse → Raisonnement → Conclusion ») pour améliorer l’alignement avec les représentations internes du modèle.

Un autre facteur subtil, mais non moins important, est l’organisation des démonstrations. Organiser les exemples du plus simple au plus complexe, par exemple en commençant par une instruction d’impression de programmation de base avant de passer aux boucles, aide le modèle à créer progressivement son contexte, à améliorer sa compréhension et la qualité de ses sorties.

Enfin, le formatage des instructions et l’apprentissage de type « chain-of-thought » améliorent les tâches à forte intensité de raisonnement, en guidant explicitement le modèle à travers les étapes intermédiaires. Cette approche est particulièrement utile dans des domaines tels que l’arithmétique et le raisonnement logique, où une répartition comme « Étape 1 : soustraire 3 de 8 → Étape 2 : la réponse est 5 » améliore la précision par rapport aux formats de question-réponse directes.

## Applications de l’apprentissage contextuel

**Détection des anomalies :** en utilisant l’apprentissage contextuel, les LLM peuvent être alimentés de quelques exemples étiquetés d’activité réseau normale et anormale. Le modèle peut ensuite classer avec précision les nouvelles instances de trafic comme étant normales ou suspectes, ce qui permet une surveillance flexible et efficace, sans la nécessité de renouveler son entraînement de manière exhaustive. Cette approche peut être appliquée à diverses tâches de cybersécurité et de gestion des réseaux.

Par exemple, un article de recherche présentait une application de l’apprentissage contextuel avec un LLM, GPT-4 plus précisément, pour assurer la détection automatique d’intrusion réseau dans les environnements sans fil.[4](#f04) Au lieu de faire appel aux méthodes traditionnelles, qui nécessitent un grand volume de données étiquetées et un réglage fin coûteux, les chercheurs ont élaboré trois approches d’apprentissage contextuel : illustrative, heuristique et interactive. Ces méthodes guident GPT-4 pour identifier les types d’attaques en fournissant quelques exemples étiquetés dans les prompts et en incorporant des questions spécifiques au domaine pour améliorer la précision. Testés sur un jeu de données réel avec 9 types d’attaques par déni de service distribué (DDoS), les résultats ont montré une performance améliorée. Grâce à ces améliorations, la précision et le score F1 ont augmenté d’environ 90 %, et GPT-4 a dépassé les 95 % avec seulement 10 exemples. Cela démontre que l’apprentissage contextuel permet aux LLM de s’adapter rapidement et de fonctionner efficacement dans des scénarios de cybersécurité réels, avec un minimum de données d’entraînement.

**Traitement automatique du langage naturel (TAL) spécialisé** : l’ICL permet aux LLM de fonctionner correctement sur des tâches spécialisées en utilisant des exemples pertinents dans le prompt. Cette approche permet de relever les défis liés aux tâches de [traitement automatique du langage naturel](https://www.ibm.com/fr-fr/think/topics/natural-language-processing) (TAL) spécialisé, où les données étiquetées sont rares, ou l’optimisation n’est pas pratique. Cette route permet au modèle de s’adapter et de générer des résultats précis en s’appuyant uniquement sur les indices contextuels fournis lors de l’inférence.

Une étude démontre que les LLM peuvent analyser efficacement les rapports de sécurité aéronautique grâce à l’ICL et résoudre des défis tels que la parcimonie sémantique et le besoin d’optimisation, coûteuse en termes de calcul.[5](#f05) L’étude a utilisé BM25 (un algorithme de récupération d’informations permettant de classer les documents en fonction de leur pertinence), afin de sélectionner les exemples les plus pertinents pour les prompts. Le modèle a considérablement amélioré sa capacité de classification avec huit exemples, affichant une précision allant jusqu’à 80,24 % et un score F1 de 84,15 %. En fournissant des exemples pertinents et de qualité dans le prompt, le modèle peut généraliser sa compréhension et classer avec précision les nouveaux rapports. Augmenter le nombre d’exemples bien choisis améliore généralement la performance, car le modèle acquiert plus de contexte et repère mieux les schémas sous-jacents présents dans les données. Cette approche montre qu’un ICL avec une sélection stratégique d’exemples permet aux LLM de comprendre et de classer efficacement les données aéronautiques spécialisées, ce qui en fait une solution pratique pour les tâches TAL spécialisées.

**Analyse des sentiments :** l’ICL permet aux LLM d’analyser les sentiments grâce à quelques échantillons de texte étiquetés (par exemple, « Excellent service → positif », « Mauvais produit → négatif »). Devant une nouvelle phrase non étiquetée, le modèle peut déduire le sentiment avec une grande précision. Cette approche permet de rationaliser les tâches d’analyse de l’expérience client, d’opinion mining et de surveillance de marque.

L’apprentissage contextuel marque un changement fondamental dans la façon dont nous interagissons avec les grands modèles de langage et en extrayons l’intelligence. Cela permet aux modèles de s’adapter dynamiquement aux nouvelles tâches à l’aide de descriptions et de quelques exemples. L’ICL apporte flexibilité, efficacité et accessibilité aux systèmes d’IA. Il comble le fossé entre les modèles pré-entraînés, statiques, et les besoins dynamiques du monde réel. En effet, il permet à un seul et même modèle d’effectuer un large éventail de tâches en observant tout simplement quelques exemples. À mesure que la recherche en matière d’algorithmes d’apprentissage, de stratégies de pré-entraînement, de conception des prompts et d’optimisation des démonstrations, l’ICL promet de devenir la pierre angulaire de l’IA à usage général, ouvrant la voie à des systèmes plus adaptatifs, interprétables et évolutifs dans tous les secteurs d’activité.
