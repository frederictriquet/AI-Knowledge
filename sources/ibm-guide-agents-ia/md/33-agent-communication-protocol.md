> Source : https://www.ibm.com/fr-fr/think/topics/agent-communication-protocol

# Qu’est-ce que l’ACP (Agent Communication Protocol ) ?

L’Agent Communication Protocol (ACP) est une norme ouverte pour la communication entre agents. Ce protocole permet de transformer notre paysage actuel d’agents isolés en systèmes agentiques interopérables, facilitant ainsi l’intégration et la collaboration.

## Qu’est-ce que l’ACP (Agent Communication Protocol ) ?

Avec [l’ACP](https://towardsdatascience.com/tag/acp/), introduit à l’origine par [BeeAI](https://beeai.dev/) d’IBM, les [agents d’IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) peuvent collaborer librement entre équipes, cadres, technologies et organisations.

L’ACP est un protocole universel qui transforme le paysage fragmenté actuel des agents d’IA en coéquipiers interconnectés. De plus, cette norme ouverte permet des niveaux inédits d’interopérabilité, de réutilisation et d’évolutivité. Dans la lignée du Model Context Protocol (MCP), une norme ouverte pour l’accès aux outils et aux données, l’ACP définit la façon dont les agents fonctionnent et communiquent.[1](#f01)\
\
Un [agent d’IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) est un système ou programme capable d’exécuter des tâches de manière autonome pour le compte d’un utilisateur ou d’un autre système. Il exécute ces tâches en concevant son propre workflow et en utilisant les outils disponibles. Les [systèmes multi-agents](https://www.ibm.com/fr-fr/think/topics/multiagent-system) sont composés de plusieurs agents d’IA travaillant collectivement pour exécuter des tâches au nom d’un utilisateur ou d’un autre système.

En tant que norme de communication entre agents d’IA régie par un processus ouvert, l’ACP permet aux agents d’IA de communiquer à travers différents frameworks et environnements technologiques.

De la réception de requêtes utilisateur en langage naturel à l’exécution de séries d’actions, les agents d’IA fonctionnent mieux lorsqu’ils disposent de protocoles de communication structurés. Ces protocoles permettent de relayer les informations entre les outils, aux autres agents, et en fin de chaîne, à l’utilisateur. 

[La communication des agents d’IA](https://www.ibm.com/fr-fr/think/topics/ai-agent-communication) fait référence à la manière dont les agents d’intelligence artificielle interagissent entre eux, avec les humains ou avec des systèmes externes, pour échanger des informations, prendre des décisions et accomplir des tâches.

Cette communication est particulièrement importante dans les systèmes multi-agents, où plusieurs agents d’IA collaborent, et dans les interactions humain-IA.

L’ACP fait partie d’un écosystème en pleine croissance, incluant BeeAI. Voici quelques-unes de ses fonctionnalités principales (pour plus de détails, consultez la [documentation officielle](https://agentcommunicationprotocol.dev/introduction/welcome)).

  Exemple de communication entre un client ACP et des agents ACP issus de différents frameworks.

## Fonctionnalités principales de l’ACP

- **Communication basée sur REST :** l’ACP utilise les conventions HTTP standard, ce qui facilite son intégration en production. Le MCP, quant à lui, repose sur le format JSON-RPC, qui nécessite des méthodes de communication beaucoup plus complexes.
- **Aucun SDK requis :** l’ACP ne nécessite aucune bibliothèque dédiée. Vous pouvez interagir avec des agents intelligents via cURL, Postman, ou même votre navigateur. Un SDK est néanmoins disponible pour plus de confort.
- **Découverte hors ligne :** les agents ACP peuvent intégrer des métadonnées directement dans leurs paquets de distribution, ce qui permet leur découverte même lorsqu’ils sont inactifs. Cette approche convient aux environnements dits scale-to-zero, où les ressources sont allouées dynamiquement et ne sont pas toujours en ligne.
- **Asynchrone par défaut, synchrone pris en charge :** l’ACP est conçu avec une communication asynchrone par défaut. Cette méthode est idéale pour des tâches complexes ou longues. Les requêtes synchrones sont également prises en charge.

**Remarque :** l’ACP permet l’orchestration d’agents pour toute architecture agentique, mais ne gère pas les workflows, les déploiements ou la coordination entre agents. À la place, il permet l’orchestration entre des agents hétérogènes en standardisant leur mode de communication. IBM Research a développé BeeAI, un système open source conçu pour gérer l’orchestration, le déploiement et le partage d’agents en utilisant l’ACP comme couche de communication.

## Pourquoi avons-nous besoin de l’ACP ?

  Architectures d’agents diverses rendues compatibles via l’ACP.

Alors que l’[IA agentique](https://www.ibm.com/fr-fr/think/topics/agentic-ai) prend de l’ampleur, la situation se complique : comment tirer le meilleur parti de chaque technologie indépendante selon votre [cas d’utilisation](https://www.ibm.com/fr-fr/think/topics/ai-agent-use-cases), sans dépendre d’un fournisseur donné ? Chaque [cadre](https://www.ibm.com/fr-fr/think/insights/top-ai-agent-frameworks), plateforme ou boîte à outils offre ses avantages, mais les intégrer dans un même système agentique reste un défi majeur.

Aujourd’hui, la plupart des systèmes d’agents fonctionnent en silos. Ils reposent sur des frameworks incompatibles, exposent des API et des points de terminaison personnalisés, et n’ont pas de protocole de communication commun. Les connecter implique des intégrations fragiles, non réplicables et coûteuses à construire.\
\
L’ACP représente un changement fondamental : passer d’un écosystème fragmenté et ad hoc à un réseau interconnecté d’agents, capables de se découvrir, de se comprendre et de collaborer, peu importe qui les a créés ou sur quelle pile ils s’exécutent.

Grâce à l’ACP, les développeurs peuvent exploiter l’intelligence collective d’agents diversifiés pour créer des workflows plus puissants que ce dont un seul système est capable.\
\

## Défis actuels

Malgré la croissance rapide des capacités des agents, l’intégration dans le monde réel reste un obstacle majeur. En l’absence de protocole de communication commun, les organisations font face à plusieurs défis récurrents :

- Diversité des cadres : les entreprises exploitent souvent des centaines voire des milliers d’agents basés sur différents frameworks comme [LangChain](https://www.ibm.com/fr-fr/think/topics/langchain), [crewAI](https://www.ibm.com/fr-fr/think/topics/crew-ai), AutoGen ou des piles maison.
- Intégrations personnalisées : sans protocole standard, les développeurs doivent coder des connecteurs spécifiques pour chaque interaction.
- Explosion du développement : avec n agents, il faut potentiellement n(n-1)/2 points d’intégration différents, ce qui rend les écosystèmes à grande échelle difficiles à gérer.
- Considérations inter-organisationnelles : des modèles de sécurité, systèmes d’authentification et formats de données variés compliquent l’intégration entre entreprises.

## Un exemple concret

Pour illustrer les besoins réels en matière de [communication entre agents](https://www.ibm.com/fr-fr/think/topics/ai-agent-communication), prenons l’exemple de deux entreprises :

- Une entreprise de fabrication qui utilise un agent autonome pour gérer les calendriers de production et l’exécution des commandes en fonction des stocks internes et de la demande des clients.
- Un prestataire logistique qui exploite un agent pour estimer les délais d’expédition en temps réel, connaître les disponibilités des transporteurs et optimiser les itinéraires.

  Un exemple de cas d’utilisation de deux agents (fabrication et logistique) échangeant entre organisations grâce à l’ACP.

Imaginez maintenant que le système du fabricant doive estimer les délais de livraison pour un gros équipement sur mesure, afin d’établir un devis.

*Sans l’ACP :* il faut créer une intégration sur mesure entre le logiciel de planification du fabricant et les [API](https://www.ibm.com/fr-fr/think/topics/api) du prestataire logistique. Cela implique la gestion manuelle de l’authentification, des incompatibilités de formats de données et de la disponibilité des services. Ces intégrations sont coûteuses, fragiles, et peu évolutives quand de nouveaux partenaires rejoignent l’écosystème.\
\
*Avec l’ACP :* chaque organisation enveloppe son agent avec une interface ACP. L’agent manufacturier envoie les détails de la commande et de la destination à l’agent logistique, qui répond en renvoyant les options d’expédition en temps réel et les délais estimés.

Les deux systèmes collaborent sans exposer leur fonctionnement interne ni développer d’intégrations spécifiques. De nouveaux partenaires logistiques peuvent être ajoutés facilement, simplement en implémentant l’ACP.

L’automatisation offerte par les agents d’IA associés à l’ACP permet d’assurer l’évolutivité et la rationalisation des échanges de données.

## Prendre un bon départ

La simplicité est un principe clé de la conception de l’ACP. Envelopper un agent avec l’ACP peut se faire en quelques lignes de code. Avec le [SDK](https://www.ibm.com/fr-fr/think/topics/api-vs-sdk) Python , vous pouvez définir un agent compatible ACP simplement en décorant une fonction.

Cette mise en œuvre minimale :

1.  Crée une instance de serveur ACP.
2.  Définit une fonction d’agent via le décorateur @server.agent() .
3.  Implémente un agent en utilisant le framework LangChain avec un back-end de [grand modèle de langage (LLM)](https://www.ibm.com/fr-fr/think/topics/large-language-models) et une mémoire pour la persistance du contexte.
4.  Traduit le format de message ACP et le format natif du framework pour renvoyer une réponse structurée.
5.  Démarre le serveur, rendant l’agent disponible via HTTP.

Exemple de code :

```python
from typing import Annotated
import os
from typing_extensions import TypedDict
from dotenv import load_dotenv
#ACP SDK
from acp_sdk.models import Message
from acp_sdk.models.models import MessagePart
from acp_sdk.server import RunYield, RunYieldResume, Server
from collections.abc import AsyncGenerator
#Langchain SDK
from langgraph.graph.message import add_messages
from langchain_anthropic import ChatAnthropic

load_dotenv()

class State(TypedDict):
    messages: Annotated[list, add_messages]

#Set up the AI model of your choice
llm = ChatAnthropic(model="claude-3-5-sonnet-latest",
api_key=os.environ.get("ANTHROPIC_API_KEY"))

#------ACP Requirement-------#
#START SERVER
server = Server()
#WRAP AGENT IN DECORACTOR
@server.agent()
async def chatbot(messages: list[Message])-> AsyncGenerator[RunYield, RunYieldResume]:
    "A simple chatbot enabled with memory"
    #formats ACP Message format to be compatible with what langchain expects
    query = " ".join(
        part.content
        for m in messages
        for part in m.parts
    )
    #invokes llm
    llm_response = llm.invoke(query)
    #formats langchain response to ACP compatible output
    assistant_message = Message(parts=[MessagePart(content=llm_response.content)])
    # Yield so add_messages merges it into state
    yield {"messages": [assistant_message]}

server.run()
#---------------------------#
```

Vous avez maintenant créé un agent entièrement compatible ACP qui peut :

- Être découvert par d’autres agents (en ligne ou hors ligne).
- Traiter des requêtes en mode synchrone ou asynchrone.
- Communiquer via des formats de message standardisés.
- S’intégrer avec tout système compatible ACP.

## Comparaison entre l’ACP, le MCP et l’A2A

Pour mieux comprendre le rôle de l’ACP dans cet écosystème IA en évolution, comparons-le à d’autres protocoles émergents. *Ces protocoles ne sont pas nécessairement concurrents :* ils couvrent différents niveaux de la pile d’intégration du système d’IA et se complètent souvent.

Récapitulatif :

[**Model Context Protocol (MCP) :**](https://www.ibm.com/fr-fr/think/topics/model-context-protocol) conçu pour enrichir le contexte d’un modèle unique avec des outils, de la mémoire et des ressources. Par Anthropic.\
*Focalisation : un modèle, plusieurs outils*

**Agent Communication Protocol (ACP) :** conçu pour la communication entre agents indépendants, entre systèmes et organisations. Par BeeAI d’IBM.\
*Focalisation : plusieurs agents, travail collaboratif, pas d’enfermement propriétaire, gouvernance ouverte*

**Agent2Agent Protocol (A2A)** : conçu pour la communication entre agents indépendants, entre systèmes et organisations. Par Google.

*Focalisation : Plusieurs agents collaboratifs, optimisé pour l’écosystème Google*

## ACP et MCP

L’équipe ACP a initialement envisagé d’adapter le Model Context Protocol (MCP), qui offre une bonne base pour les interactions modèle-contexte. Mais elle a rapidement rencontré des limitations architecturales qui le rendent inadapté à une vraie communication entre agents.

Pourquoi le MCP n’est pas adapté aux systèmes multi-agents :

**Streaming :** le MCP prend en charge un streaming basique (messages complets), mais pas le streaming de type delta, plus granulaire, où les mises à jour sont envoyées dès qu’elles surviennent. Les flux delta, (tokens et trajectoires, par exemple), sont des flux composés de mises à jour incrémentielles plutôt que de charges utiles de données complètes. Cette limitation vient du fait que, lorsque le MCP a été créé, il n’était pas destiné aux interactions de type agent.

**Partage de mémoire :** le MCP ne prend pas en charge l’exécution de plusieurs agents sur des serveurs avec conservation d’une mémoire partagée. L’ACP ne prend pas encore entièrement en charge cette fonction, mais elle est en cours de développement.

**Structure des messages :** le MCP accepte tous les schémas JSON, mais ne définit pas la structure du corps du message. Cette flexibilité nuit à l’interopérabilité, en particulier pour la création d’agents qui doivent interpréter divers formats de message.

**Complexité du protocole :** le MCP utilise JSON-RPC et nécessite des SDK et des environnements d’exécution spécifiques. En revanche, la conception REST de l’ACP avec prise en charge asynchrone/synchrone intégrée est plus légère et plus conviviale pour l’intégration.\
\
\
Considérez le **MCP** comme un moyen de donner de meilleurs outils à une personne, comme une calculatrice ou un livre de référence, pour améliorer ses performances. En revanche, **l’ACP** permet de former des *équipes*, où chaque personne, ou agent, collabore et met ses capacités à profit dans l’application d’IA.\
\
*L’ACP et le MCP peuvent être complémentaires :*

Le protocole Agent2Agent (A2A) de Google, introduit peu après l’ACP, vise également à standardiser la communication entre agents d’IA.\
\
Ces deux protocoles ont pour objectif de soutenir les systèmes multi-agents, mais ils diffèrent en termes de philosophie et de gouvernance. *Les principales différences :*

L’ACP a été délibérément conçu pour être :

- Simple à intégrer en utilisant des outils HTTP courants et les conventions REST.
- Flexible pour une grande variété de types d’agents et de workloads.
- Indépendant des fournisseurs, avec une gouvernance ouverte et une large compatibilité avec divers écosystèmes.

**Les deux protocoles peuvent coexister, chacun répondant à des besoins différents selon l’environnement**. Le design léger, ouvert et extensible de l’ACP le rend particulièrement adapté aux systèmes décentralisés et à l’interopérabilité dans des contextes inter-organisationnels réels. L’intégration naturelle de l’A2A peut en revanche convenir davantage à ceux qui utilisent l’écosystème Google.

## Feuille de route et communauté

À mesure que l’ACP évolue, de nouvelles possibilités sont explorées pour améliorer la communication entre agents. Voici quelques axes prioritaires :

- Fédération d’identités : Comment l’ACP peut-il fonctionner avec les systèmes d’authentification pour renforcer la confiance entre réseaux ?
- Délégation d’accès : Comment permettre à des agents de déléguer des tâches de manière sécurisée, tout en conservant le contrôle utilisateur ?
- Prise en charge multirépertoire : L’ACP peut-il permettre la découverte d’agents de façon décentralisée sur plusieurs réseaux ?
- Partage d’agents : Comment faciliter le partage et la réutilisation d’agents entre les organisations ou au sein de ces dernières ?
- Déploiements : Quels outils et modèles peuvent simplifier le déploiement d’agents ?

L’ACP est développé en open source, car les standards fonctionnent mieux lorsqu’ils sont élaborés avec les utilisateurs eux-mêmes. Les [contributions](https://agentcommunicationprotocol.dev/about/contribute) des développeurs, des chercheurs et des entreprises intéressés par l’avenir de l’interopérabilité des agents d’IA sont les bienvenues. Participez à la définition de ce nouveau standard pour l’IA générative.

Pour en savoir plus, consultez le [site officiel de l’ACP](https://agentcommunicationprotocol.dev/introduction/welcome) et rejoignez la conversation sur [GitHub](https://github.com/i-am-bee/acp/discussions) et [Discord](https://discord.com/invite/49BmB5BcNY).
