> Source : https://www.ibm.com/fr-fr/think/insights/llm-skeleton-key

# Quand les chatbots IA deviennent mauvais

Un nouveau défi est apparu dans le monde de l’intelligence artificielle, en constante évolution. Les « AI whisperers » ou spécialistes des prompts explorent les limites de l’éthique de l’IA en convaincant des chatbots bien conduits d’enfreindre leurs propres règles.

Connu sous le nom d’injections de prompt ou de « débridage », ces exploits exposent les vulnérabilités des systèmes d’IA et soulèvent des inquiétudes quant à leur sécurité. Microsoft a récemment fait des vagues avec sa technique « Skeleton Key », un processus à plusieurs étapes conçu pour contourner les garde-fous éthiques de l’IA. Mais cette approche n’est pas aussi nouvelle qu’il n’y paraît.

« Skeleton Key est unique en le sens qu’il nécessite de multiples interactions avec l’IA », explique Chenta Lee, architecte en chef des renseignements sur les menaces chez IBM. « Auparavant, la plupart des attaques par injection de prompt visaient à perturber l’IA en une seule tentative. Skeleton Key effectue plusieurs attaques, ce qui peut augmenter son taux de réussite. »

## L’art de la manipulation de l’IA

Le monde des débridages de l’IA est diversifié et en constante évolution. Certaines attaques sont étonnamment simples, tandis que d’autres impliquent des scénarios élaborés qui nécessitent l’expertise d’un pirate informatique sophistiqué. Ce qui les rassemble, c’est un objectif commun : pousser ces assistants digitaux au-delà des limites programmées.

Ces exploitations font appel à la nature même des modèles de langage. Les chatbots IA sont formés pour être utiles et pour comprendre le contexte. Les débridages créent des scénarios dans lesquels l’IA pense qu’il est approprié d’ignorer ses directives éthiques habituelles.

Alors que les attaques à plusieurs étapes comme Skeleton Key font la une des journaux, M. Lee affirme que les techniques single-shot restent une préoccupation plus urgente. « Il est plus facile d’attaquer un grand modèle linguistique en une seule fois », note-t-il. « Imaginez qu’il soit possible de faire une injection de prompt dans votre CV et que votre système de recrutement soit alimenté par l’IA. Il s’agit d’une attaque one-shot, sans aucune probabilité d’interactions multiples. »

Selon les experts en cybersécurité, les conséquences potentielles sont alarmantes. « Des acteurs malveillants pourraient utiliser Skeleton Key pour contourner les protections de l’IA et générer des contenus préjudiciables, diffuser de la désinformation ou automatiser des attaques d’ingénierie sociale à l’échelle », avertit Stephen Kowski, directeur technique au sein de SlashNext Email Security+.

Bien que bon nombre de ces attaques restent théoriques, les implications concrètes commencent à apparaître. M. Lee cite un exemple de chercheurs ayant convaincu l’agent conversationnel alimenté par l’IA d’une entreprise de proposer des remises massives et non autorisées. « Vous pouvez tromper leur agent conversationnel et obtenir une bonne réduction. Ce n’est peut-être pas ce que l’entreprise souhaite », dit-il.

Dans le cadre de ses propres recherches, M. Lee a développé des preuves de concept pour montrer comment un LLM peut être encapsulé pour créer du code vulnérable et malveillant et comment des conversations audio en direct peuvent être interceptées et déformées en temps quasi réel.

## Renforcer la frontière numérique

La défense contre ces attaques est un défi permanent. M. Lee décrit deux approches principales : améliorer l’entraînement de l’IA et créer des pare-feux IA.

« Nous voulons améliorer l’entraînement afin que le modèle lui-même sache détecter une attaque », explique M. Lee. « Nous allons également inspecter toutes les requêtes entrantes dans le modèle de langage et détecter les injections de prompt. »

Alors que l’IA générative occupe de plus en plus de place dans notre vie quotidienne, comprendre ces vulnérabilités n’est pas seulement une préoccupation pour les experts technologiques. Il est de plus en plus crucial pour toute personne interagissant avec les systèmes d’IA de prendre conscience de leurs faiblesses potentielles.

Lee compare les premiers jours des attaques par injection SQL sur les bases de données. « Il a fallu 5 à 10 ans aux secteurs pour faire comprendre à tout le monde que lors de l’écriture d’une SQL query, il faut paramétrer toutes les entrées pour être à l’abri des attaques par injection », explique-t-il. « Pour l’IA, nous commençons à utiliser partout des modèles de langage. Les gens doivent comprendre que vous ne pouvez pas vous contenter de donner des instructions simples à une IA, car cela rendrait votre logiciel vulnérable. »

La découverte de méthodes de débridage telles que Skeleton Key est susceptible d’altérer la confiance du public dans l’IA, ralentissant potentiellement l’adoption de technologies d’IA bénéfiques. Selon Narayana Pappu, PDG de Zendata, la transparence et la vérification indépendante sont essentielles pour reconstruire la confiance.

« Les développeurs d’IA et les entreprises peuvent trouver un équilibre entre la création de modèles de langage puissants et polyvalents et la mise en place de protections robustes contre les utilisations abusives », ajoute-t-il. « Ils peuvent y parvenir grâce à la transparence des systèmes internes, en comprenant les risques liés à l’IA et à la chaîne d’approvisionnement et en intégrant des outils d’évaluation à chaque étape du processus de développement. »
