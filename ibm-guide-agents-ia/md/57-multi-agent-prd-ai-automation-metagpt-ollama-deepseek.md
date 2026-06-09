> Source : https://www.ibm.com/fr-fr/think/tutorials/multi-agent-prd-ai-automation-metagpt-ollama-deepseek

# Automatisation multi-agents des PRD avec MetaGPT, Ollama et DeepSeek

Apprenez à utiliser MetaGPT, DeepSeek et Ollama pour construire un outil alimenté par l’IA qui aide les chefs de produit à créer rapidement des documents d’exigences produit complets en s’appuyant sur une équipe d’agents IA spécialisés.

[MetaGPT](https://www.ibm.com/fr-fr/think/topics/metagpt) est un cadre multi-agents développé par DeepWisdom, une start-up technologique spécialisée dans le développement d’outils open source qui automatisent le travail en utilisant l’intelligence artificielle, les systèmes multi-agents et les workflows agentiques.

Contrairement aux approches à agent unique, selon lesquelles un seul modèle vise de gérer tous les aspects de la tâche, ce système multi-agents attribue à chaque agent un rôle particulier et des responsabilités clairement définies. En suivant des workflows structurés et en examinant les sorties de chacun, l’équipe génère collectivement un PRD de qualité, plus aligné sur les objectifs des parties prenantes, mieux organisé et moins sujet aux omissions.

Avant de commencer, voici quelques termes pour vous familiariser avec la pile technologique de l’application :

**MetaGPT :** un cadre qui structure les agents de grands modèles de langage ([LLM](https://www.ibm.com/fr-fr/think/topics/large-language-models)) en rôles collaboratifs, leur permettant de travailler ensemble comme une équipe coordonnée.\
**Ollama :** un environnement d’exécution local conçu pour exécuter et gérer les LLM open source directement sur votre ordinateur personnel ou sur votre poste de travail.\
**DeepSeek** : un modèle de langage open source optimisé pour des tâches telles que la recherche, le raisonnement et la rédaction technique.

## Automatiser les PRD grâce à la collaboration multi-agents

La création de PRD peut prendre du temps, mais l’intelligence artificielle peut aider en accélérant le processus de réalisation.

La collaboration multi-agents est mise en œuvre dans des cadres comme MetaGPT, un outil d’IA qui coordonne plusieurs agents jouant chacun un rôle pour effectuer une tâche complexe. Par tâche complexe, on entend toute tâche qui requiert plusieurs étapes pour être réalisée.

La création d’un PRD par l’IA est un excellent cas d’utilisation pour la collaboration entre plusieurs agents, car elle reflète un processus de développement de produits réel, où de multiples parties prenantes contribuent à des étapes telles que la recherche, la planification, la révision et l’affinement. Pour tirer pleinement parti du contenu généré par l’IA, il faut envisager d’utiliser un système multi-agents plutôt que d’utiliser un chatbot unique comme ChatGPT d’OpenAI ou Copilot de Microsoft.

### Pourquoi utiliser un système multi-agents comme MetaGPT ?

MetaGPT utilise des agents IA spécialisés dotés de rôles distincts, chacun pouvant être personnalisé pour s’adapter à tout workflow, ou presque, avec un travail de codage minime. Cette flexibilité est possible grâce à la capacité des LLM à comprendre le langage naturel. Les utilisateurs définissent les comportements et les workflows des agents grâce au prompt engineering et au développement de logiciels légers.

L’objectif de MetaGPT est de permettre une collaboration multi-agents efficace. En simulant une équipe structurée, il permet de raisonner en fonction des rôles et de déléguer des tâches, afin d’obtenir des sorties plus cohérentes et mieux adaptées au contexte, comme un PRD de qualité.

Lors de ce tutoriel, nous verrons également comment un agent unique génère un premier brouillon de PRD (un peu comme si vous utilisiez un chatbot autonome). Nous comparerons ensuite ce brouillon au PRD final, plus précis, produit grâce à la collaboration multi-agents. Cette méthode démontrera que le travail d’équipe apporte de meilleurs résultats que celui réalisé par un seul agent.

### Pourquoi utiliser DeepSeek pour l’automatisation des PRD ?

Développée par DeepSeek-AI, la famille de LLM open source [DeepSeek](https://www.ibm.com/fr-fr/think/topics/deepseek) est optimisée pour les tâches de raisonnement, la création de contenu structuré et les workflows de développement d’IA. Dans ce projet, nous utilisons deepseek-r1, un modèle de base performant, idéal pour automatiser la documentation produit.

Voici pourquoi DeepSeek se distingue dans la création de PRD avec un système multi-agents comme MetaGPT :

- **Sorties structurées pour l’automatisation :** les modèles DeepSeek génèrent des sorties markdown cohérentes, ce qui correspond parfaitement aux workflows qui exigent une structure de documents formelle comme les PRD et les spécifications techniques.
- **Capacités de raisonnement :** le modèle prend en charge les boucles d’interaction multi-agents en gérant les étapes de raisonnement et de révision séquentielles.
- **Benchmarks de performance **: selon les benchmarks publiés, les modèles de DeepSeek sont compétitifs face à d’autres modèles open source dans la gamme de paramètres 7-13B, notamment les modèles de Mistral, LLaMA et IBM® Granite. Développé par IBM® Research pour les entreprises, Granite met l’accent sur la gouvernance, la robustesse et le raisonnement métier structuré.
- **Inférence locale :** l’exécution de deepseek-r1 via Ollama sur des GPU locaux permet une expérimentation à faible latence, sans s’appuyer sur des interfaces de programmation d’applications externes comme OpenAI ou les points de terminaison Microsoft Azure (pas besoin d’une clé d’API !). Cette approche peut s’avérer utile dans le cas des workflows exigeant d’assurer la confidentialité des données ou un développement hors ligne.
- **Support linguistique et fenêtre contextuelle :** DeepSeek propose un support multilingue solide, y compris le chinois, et inclut une fenêtre contextuelle assez longue, qui permet d’étendre la mémoire pour les sessions multi-agents.

Nous utilisons DeepSeek dans ce tutoriel. Sachez toutefois que le même système multi-agents peut être configuré pour s’exécuter avec d’autres LLM compatibles avec Ollama, Hugging Face ou l’API d’OpenAI. Le choix du modèle dépend du compromis entre la précision du raisonnement, la structure des sorties, la disponibilité des ressources et l’environnement de déploiement prévu.

## Comment fonctionne MetaGPT ?

MetaGPT utilise le concept de procédures opérationnelles standard (POS) pour aligner la collaboration entre les humains et l’IA en structurant les workflows en fonction d’équipes réelles (à savoir une entreprise de développement logiciel ou une équipe de développement produit).

Les POS fournissent des lignes directrices détaillées, étape par étape, pour mener à bien une tâche ou un processus. MetaGPT applique ce concept en décomposant les tâches complexes (comme la création d’un PRD) en étapes claires et exploitables.

Chaque action est attribuée à un « membre de l’équipe » désigné ou à un agent IA.

### Agent de base MetaGPT

Les agents MetaGPT opèrent au sein d’un système structuré basé sur les rôles, conçu pour simuler et coordonner leurs tâches par le biais de workflows collaboratifs.

Chaque agent suit un workflow agentic organisé, axé sur **quatre** concepts fondamentaux :

1.  **Rôle :** un profil spécialisé permettant d’atteindre un objectif donné (gestionnaire de projet, concepteur, analyste).
2.  **Action** : la capacité à effectuer certaines tâches (rédaction, révision, recherche, etc.).
3.  **Mémoire** : la mémoire est stockée individuellement, sous la forme d’une liste d’objets de message qui incluent les interactions, les observations et les actions passées. Ces messages sont publiés dans un pool de messages partagé pour la communication entre agents. La mémoire informe les actions des agents.
4.  **Environnement** : un espace commun (le pool de messages global) pour accéder aux informations provenant d’autres agents sans interaction directe. Cet espace sert de contexte commun à tous les agents.

Ensemble, ces composants permettent l’autonomie des agents et l’exécution des tâches dans MetaGPT. Ensuite, nous découvrirons la façon dont ces agents communiquent et collaborent pour effectuer des tâches multi-étapes telles que la génération de PRD.

### Comment les agents MetaGPT collaborent

Les agents MetaGPT suivent un processus coordonné lors duquel chaque agent contribue à un objectif commun. Chaque agent traite les informations et raisonne en fonction de son rôle, prend des mesures et partage les résultats avec les autres. Cette approche permet une collaboration dynamique, étape par étape, vers la sortie finale.

**Workflow des agents MetaGPT :**

1.  **Observer** : l’agent observe les états actuels (par exemple, le dernier brouillon du PRD).
2.  **Réfléchir :** en utilisant le LLM, il décide de la marche à suivre en fonction de ses rôles et des informations disponibles.
3.  **Agir** : l’agent effectue la tâche qui lui est affectée comme la rédaction, la révision ou la recherche.
4.  **Partager** : l’agent journalise sa sortie et diffuse un message dans l’environnement partagé pour que les autres agents de l’équipe puissent y accéder.
5.  **Agent suivant** : on passe à l’agent suivant, qui reprend là où le dernier s’est arrêté et répète le processus jusqu’à ce qu’un consensus soit atteint.

Les agents itèrent sur cette boucle structurée, s’appuyant sur le travail de chacun à chaque tour, et ce jusqu’à ce qu’ils atteignent une sortie finale, plus complète et plus précise.

Avec MetaGPT, il est possible de constituer une équipe de développement produits IA entièrement automatisée en personnalisant les rôles des agents, les POS, les templates de PRD, les priorités des parties prenantes et les objectifs globaux du projet. Le cadre est extensible, ce qui permet aux équipes de l’adapter aux différents workflows et exigences.

Maintenant que nous savons comment les agents fonctionnent et collaborent, voyons comment ce processus est orchestré au niveau de l’application dans le workflow de génération de PRD.

### Fonctionnement du workflow PRD multi-agents

Cette section sert de guide étape par étape pour comprendre le workflow de l’équipe d’agents MetaGPT de cette application de génération de PRD multi-agents.

#### Définir la procédure opérationnelle standard (POS)

Nous allons définir un workflow agentique structuré avec notre équipe MetaGPT en créant une POS. Cette POS décompose la tâche complexe de création du PRD en étapes claires et exploitables, dont chacune est attribuée à un agent spécialisé.

##### Rôles et responsabilités

Une POS bien définie clarifie le rôle et les actions de chaque agent. Cette structure favorise la responsabilisation et la fluidité d’exécution tout au long du cycle de vie du PRD : rédaction, enrichissement de la recherche, évaluation par les pairs et révision.

**Rôles dans l’équipe :**

- **Responsable produit (responsable d’équipe) :** orchestre le workflow, rédige le PRD initial, collecte les recherches et les commentaires, passe en revue le document et enregistre toutes les versions. L’agent de gestion de projet dirige le processus et coordonne les autres agents. \
  \
- **Chercheur :** enrichit le PRD grâce à des recherches pertinentes et à des données justificatives.\
  \
- **Évaluateur :** examine le PRD et fournit un retour d’information exploitable en vue de l’améliorer.

#### Étapes du workflow

1.  **Idée d’utilisateur :** l’utilisateur fournit une idée de projet (« Rédiger un PRD d’application bancaire pour la gestion de patrimoine ») via la ligne de commande.
2.  **Configuration de l’équipe :** l’application crée une équipe et attribue les rôles suivants : chef de produit, chercheur, évaluateur.
3.  **Rédaction :** le chef de produit (en tant que chef d’équipe) génère et enregistre le PRD initial sous forme de DraftPRD.md qui décrit les objectifs du produit, les profils d’utilisateurs, les fonctionnalités principales et les exigences fonctionnelles.
4.  **Recherche :** le chercheur examine l’ébauche et fournit des éléments de recherche.
5.  **Révision :** l’évaluateur examine le brouillon et fournit un feedback.
6.  **Révision :** le responsable projet recueille les commentaires de recherche et de révision, passe en revue le PRD et enregistre le document final sous le nom de PRD.md.\
7.  **Sortie :** le PRD final (avec recherches et révisions) est enregistré en tant que fichier Markdown dans le répertoire du projet.

Ce SOP garantit que le responsable projet dirige l’équipe, en coordonnant toutes les contributions pour automatiser la création d’un PRD soutenu par la recherche et révisé.

## Configuration requise

Pour exécuter ce tutoriel efficacement, les utilisateurs ont besoin de la configuration suivante :

- **Système d’exploitation :** macOS, Linux ou Windows
- **Mémoire (RAM) :** \> = **16 Go**\
- **Espace disque :** \>= **10 Go** disponibles (pour l’environnement Python, les modèles Ollama et les fichiers générés)
- **Ollama :** installé et exécuté localement (port 11434 par défaut)
- **Version de Python :** 3.11.x

**Remarque :** L’exécution de modèles plus grands ou de plusieurs agents peut nécessiter plus de mémoire (32 Go ou plus recommandés pour de meilleures performances). Des erreurs de délai d’attente intermittentes peuvent se produire. Si vous rencontrez des erreurs de délais d’attente, essayez de redémarrer le processus et de vous assurer que votre système dispose de ressources suffisantes.

## Étapes

### Étape 1 : créez un venv

Ces étapes peuvent être suivies ici ou dans le dossier de projet bien nommé sur [GitHub](https://github.com/IBM/ibmdotcom-tutorials/tree/main/docs/tutorials/projects). \
\
Commencez par créer un environnement virtuel pour éviter les problèmes de dépendance à Python. **Ce projet fonctionne de manière très stable avec Python 3.11.**

```bash
python3.11 -m venv myvenv
source myvenv/bin/activate
```

### Étape 2. Installer MetaGPT

Installez la dernière version de développement de MetaGPT.

```bash
pip install git+https://github.com/geekan/MetaGPT
```

**Important :** pour ce tutoriel, vous devez installer MetaGPT à l’aide de la commande ci-dessus. **Évitez** d’installer MetaGPT à partir de PyPI ou d’une autre source, car seule la dernière version de développement est prise en charge ici.

### Étape 3 : Installer Ollama

Installez Ollama en suivant l’une des méthodes suivantes, en fonction de votre système d’exploitation :

**Pour macOS (avec Homebrew)**

```bash
brew install ollama
```

**Télécharger à partir du** [**site officiel d’Ollama**](https://ollama.com/download) **(macOS, Linux, Windows)**

### Étape 4. Démarrer le serveur Ollama et extraire deepseek-r1:8b

Après l’installation, vous pouvez démarrer le serveur Ollama et extraire un modèle (deepseek-r1:8b) avec :

```bash
ollama serve
ollama pull deepseek-r1:8b
```

### Étape 5. Configurer MetaGPT pour utiliser Ollama

Afin de configurer Ollama et Deepseek pour MetaGPT, nous devons créer et modifier un fichier de configuration.

Initialiser la configuration MetaGPT :

```
metagpt --init-config
```

Cette action crée un fichier à l’adresse`~/.metagpt/config2.yaml`

Modifiez le fichier pour configurer votre LLM en suivant les étapes suivantes :

1\. Dans une fenêtre de terminal, exécutez la commande suivante pour ouvrir le fichier de configuration dans l’éditeur nano :

```
nano ~/.metagpt/config2.yaml
```

2.       Modifiez le fichier pour qu’il corresponde à cette configuration Ollama, qui utilise le modèle deepseek-r1:8b.

```
llm:
api_type: 'ollama'
base_url: 'http://127.0.0.1:11434/api'
model: 'deepseek-r1:8b'
```

**Remarque :** si le champ`api_key:` apparaît dans le fichier YAML, ne le laissez pas vide. Veuillez fournir une clé valide ou supprimer complètement le champ. Le programme ne s’exécutera pas si`api_key:` existe et est vide.

1.  Après avoir effectué les modifications précédemment citées, appuyez sur `Ctrl + O`  pour enregistrer, puis appuyez sur `Enter` pour confirmer.
2.  Appuyer`Ctrl + X` pour quitter l’éditeur nano

Les modifications apportées à la configuration du LLM ont bien été enregistrées.

Pour voir d’autres exemples de configuration, consultez les deux fournis dans les documents MetaGPT [ici](https://github.com/FoundationAgents/MetaGPT/blob/main/config/config2.example.yaml) et [](https://github.com/FoundationAgents/MetaGPT/blob/main/metagpt/config2.py)ici.

### Étape 6. Découvrir le fonctionnement des agents MetaGPT : actions et rôles

Les agents MetaGPT comportent deux composants principaux :

- **Actions :** tâches ou opérations discrètes qu’un agent peut effectuer (par exemple, rédiger un PRD, mener des recherches).
- **Rôles :** ils définissent les responsabilités de l’agent et les actions qu’il peut entreprendre (par exemple, chef de projet, chercheur).

#### Actions

 `Action` est une classe Python qui définit une tâche spécifique pour un agent.\
Les actions indiquent à chaque agent ce qu’il doit faire et comment interagir avec le modèle de langage.

Chaque action comprend généralement :

-  `PROMPT_TEMPLATE` : l’instruction ou le message que l’on envoie au LLM (par exemple, « Écrire un PRD au format markdown »).
-  `run()`  méthode : remplit le template de prompt, l’envoie au LLM et renvoie la réponse du modèle.
- De manière facultative,`parse_text()` méthode : traite la sortie du LLM pour extraire les informations pertinentes (telles que markdown, code ou JSON).

**Exigez des importations pour les actions :**

```python
import re
import os
from metagpt.actions import Action
```

- `re` est réservé aux expressions régulières (utilisées dans`parse_text` )
- `os` est réservé aux opérations sur les fichiers (utilisé dans`SavePRD` )
- `Action` est la classe de base pour toutes les actions dans MetaGPT

#### Rôles

La classe de rôles représente un agent IA ou un membre de l’équipe dans le workflow. Les rôles indiquent au modèle comment agir et définissent la partie du processus qu’il doit suivre (comme la gestion, la recherche ou la révision).

Chaque rôle comprend généralement :

- `__init__` : initialise le rôle, configure ses actions et définit les événements ou les messages qu’il doit surveiller.\
  \
-  `_act` : exécute une ou plusieurs actions attribuées lorsque c’est au tour de l’agent d’agir. Cette méthode définit le comportement de l’agent dans le workflow.

**Importations requises pour les rôles :**

```python
from metagpt.roles import Role
from metagpt.schema import Message
from metagpt.logs import logger
```

- `Role` est une classe de base pour tous les rôles d’agent dans MetaGPT.
- `Message` est utilisé pour renvoyer les résultats des actions.
- `logger` est utilisé pour la journalisation des sorties et les informations de débogage.

#### Vue d’ensemble du workflow

MetaGPT organise le workflow en tours, qui sont des cycles itératifs au cours desquels les agents collaborent pour améliorer le PRD. Chaque tour comporte les étapes suivantes :

**Tour 1 : premier jet**

- Le chef de projet crée et enregistre le premier jet du PRD en fonction du prompt de l’utilisateur.\
- Le chercheur et le réviseur reçoivent ce brouillon pour leurs tâches.

**Tour 2 (et au-delà) : examen et révision :**

- Le chercheur génère des études à l’appui pour le PRD.\
- Le réviseur fournit un feedback sur le brouillon de PRD.\
- Le responsable de projet passe en revue le PRD en lançant de nouvelles recherches et consultant les commentaires, puis enregistre la version mise à jour.

**Répéter**

- Le processus peut se répéter sur plusieurs cycles, ce qui permet d’améliorer progressivement le PRD à chaque cycle.

**Schéma d’un workflow de génération de PRD multi-agents :**

```
User prompt
↓
Team initialization
↓
PRD draft (Project Manager)
↓
Research and review (Researcher & Reviewer)
↓
Draft revision (Project Manager)
↓
Save final PRD
```

À l’étape suivante, vous constituerez une équipe d’agents pour l’automatisation IA du PRD.\
Nous définirons le rôle de chaque agent et connecterons les actions de workflow correspondantes.

### Étape 7. Constituer une équipe PRD multi-agents avec MetaGPT

Dans cette section, vous allez découvrir comment définir les **actions** des agents, créer des **rôles** d’agent et constituer une équipe pour automatiser la génération, la recherche et la révision des PRD.

#### Définir les actions des agents

Voici les actions d’agent que l’équipe PRD effectuera avec`Action` classe :

```python
import re
import os
from metagpt.actions import Action

def clean_response(rsp):
# Cleans LLM output, extracting markdown and removing extra tags
rsp = re.sub(r"<think>.*?</think>", "", rsp, flags=re.DOTALL)
pattern = r"```(?:markdown)?(.*?)```"
match = re.search(pattern, rsp, re.DOTALL)
text = match.group(1) if match else rsp
return text.strip()

class WritePRD(Action):
PROMPT_TEMPLATE: str = """
Write a comprehensive product requirements document (PRD) for {instruction} and provide the output in markdown format.
**Important:**
- Do NOT include any code, programming language, or technical implementation details.
- Only write markdown for a PRD document (sections like Introduction, Goals, User Stories, Requirements, etc.).
- Do NOT include code blocks, scripts, or pseudocode.
- Limit your response to a maximum of 1,500-3,000 words and no more than 7 unique sections.
- Ensure that no sections are repeated.
- Ensure that each section is ordered and formatted correctly with appropriate headings and subheadings.

Return ```your markdown text here with NO other texts, your text:
"""

name: str = "WritePRD"

async def run(self, instruction: str):
prompt = self.PROMPT_TEMPLATE.format(instruction=instruction)
rsp = await self._aask(prompt)
prd_text = self.parse_text(rsp)
return prd_text

@staticmethod
def parse_text(rsp):
return clean_response(rsp)

class SavePRD(Action):
name: str = "SavePRD"

async def run(self, content: str, filename: str = "PRD.md"):
filepath = os.path.join(os.getcwd(), filename)
with open(filepath, "w", encoding="utf-8") as f:
f.write(content)
return f"PRD saved to {filepath}"

class ConductResearch(Action):
PROMPT_TEMPLATE: str = """
Context: {context}
You are a research assistant working with the Project Manager to ensure that
the PRD includes information from a detailed research report for the given PRD.
Use the {instruction} to generate a detailed research report on relevant details
that should be included in the PRD and provide the output in markdown format.
Include relevant data, statistics, and references to support the PRD.
**Important**:
1. Return only the markdown text.
2. Do not include any other text or explanations.
3. Limit your response to the content that is relevant to the PRD and a maximum of 500-1,500 words.
Return ```your markdown text here``` with NO other texts, your text:
"""

name: str = "ConductResearch"

async def run(self, instruction: str, context: str = ""): 
prompt = self.PROMPT_TEMPLATE.format(instruction=instruction, context=context)
rsp = await self._aask(prompt)
research_content = self.parse_text(rsp)
return research_content    

@staticmethod
def parse_text(rsp):
return clean_response(rsp)

class PerformReview(Action):
PROMPT_TEMPLATE: str = """
You are a product reviewer. The following is a Product Requirements Document
(PRD) generated for a project.

Please review the PRD below and provide critical, actionable feedback to improve
its clarity, completeness, and effectiveness. Highlight any missing sections,
unclear requirements, or potential risks. Ensure that no sections are repeated.

**Important**:
1.  Return only the markdown text.
2. Do not include any other text or explanations.
3. Limit your response to the content that is relevant to the PRD.
4. Limit your response to a maximum of 500-1,000 words.

Return your feedback in markdown format only.

PRD to review:
{context}
"""

name: str = "PerformReview"
async def run(self, context: str):
prompt = self.PROMPT_TEMPLATE.format(context=context)
rsp = await self._aask(prompt)
review_content = self.parse_text(rsp)
return review_content

@staticmethod
def parse_text(rsp):
return clean_response(rsp)

class RevisePRD(Action):
PROMPT_TEMPLATE: str = """
Revise the Product Requirements Document (PRD) based on the following review feedback.
Revise the PRD to address all reviewer suggestions, clarifying vague terms, adding
measurable goals, expanding on integrations, including user stories, functional requirements, and adding
any missing sections as suggested.
**Important**:
1. Return only the markdown text.
2. Do not include any other text or explanations.
3. Include a section at the end titled "Document revision notes" that summarizes the key revisions.
4. Limit your response to a maximum of 1,500-4,000 words and no more than unique 12 sections.
5. Ensure that no sections are repeated.
6. Ensure that each section is ordered and formatted correctly with appropriate headings and subheadings.

PRD:
{prd}

Review Feedback:
{review}

Return ```your markdown text here``` with NO other texts, your text:
"""

name: str = "RevisePRD"

async def run(self, prd: str, review: str):
prompt = self.PROMPT_TEMPLATE.format(prd=prd, review=review)
rsp = await self._aask(prompt)
revised_prd = self.parse_text(rsp)
return revised_prd

@staticmethod
def parse_text(rsp):
return clean_response(rsp)
```

**Tâches principales**

Les 5 classes d’action suivantes définissent les principales tâches effectuées par les agents dans ce workflow de génération de PRD alimenté par l’IA :

1.  WritePRD crée le PRD.
2.  SavePRD enregistre le PRD sur disque.
3.  ConductResearch génère des recherches de soutien.
4.  PerformReview passe en revue le PRD.
5.  RevisePRD révise le PRD en fonction du feedback.

#### Définir le rôle des agents

Voici les rôles d’agent qui représentent l’équipe PRD multi-agents. Vous trouverez ci-dessous le code qui indique les actions qu’ils effectuent.

```python
class ProjectManager(Role):
name: str = "Pam"
profile: str = "Project Manager"

def __init__(self, **kwargs):
super().__init__(**kwargs)
self.write_action = WritePRD()
self.save_action = SavePRD()
self.revise_action = RevisePRD()
self._watch([UserRequirement, ConductResearch, PerformReview])
self.set_actions([self.write_action, self.save_action, self.revise_action])

async def _act(self) -> Message:
logger.info(f"{self.profile}: Starting PRD generation process.")
memories = self.get_memories()
# If this is the first round, generate and save the draft PRD
if not any(m.role == "Researcher" or m.role == "Reviewer" for m in memories):
msg = self.get_memories(k=1)[0]
prd_content = await self.write_action.run(msg.content)
draft_save_result = await self.save_action.run(prd_content, filename="DraftPRD.md")
return Message(
content=draft_save_result,
role=self.profile,
cause_by=type(self.write_action)
)
# If this is the second round, combine revised PRD and research, then save
else:
research_msgs = [m for m in memories if m.role == "Researcher"]
review_msgs = [m for m in memories if m.role == "Reviewer"]
research_content = research_msgs[-1].content if research_msgs else "No research found."
review_content = review_msgs[-1].content if review_msgs else "No review found."
# Load the draft PRD from file or memory
with open("DraftPRD.md", "r", encoding="utf-8") as f:
prd_content = f.read()
# Only revise if review feedback exists and is not empty
if review_msgs and review_content.strip() and review_content.strip() != "No PRD draft found.":
revised_prd = await self.revise_action.run(prd_content, review_content)
else:
logger.info(f"{self.profile}: No review feedback found, skipping revision this round.")
revised_prd = prd_content.strip()
final_content = (
f"{revised_prd}\n\n"
f"---\n\n"
f"## Research\n{research_content}\n"
)
await self.save_action.run(final_content, filename="PRD.md")
return Message(
content=final_content,  # Only the markdown document
role=self.profile,
cause_by=type(self.write_action)
)

class Reviewer(Role):
name: str = "Rico"
profile: str = "Reviewer"

def __init__(self, **kwargs):
super().__init__(**kwargs)
self.review_action = PerformReview()
self.set_actions([self.review_action])   
self._watch([WritePRD])

async def _act(self) -> Message:
try:
with open("DraftPRD.md", "r", encoding="utf-8") as f:
prd_content = f.read()
except FileNotFoundError:
prd_content = "No PRD draft found."
logger.info(f"{self.profile}: Reviewing PRD...")
review_content = await self.review_action.run(prd_content)
return Message(content=review_content, role=self.profile, cause_by=type(self.review_action))

class Researcher(Role):
name: str = "Rita"
profile: str = "Researcher"

def __init__(self, **kwargs):
super().__init__(**kwargs)
self.research_action = ConductResearch()
self.set_actions([self.research_action])
self._watch([UserRequirement, WritePRD])

async def _act(self) -> Message:
try:
with open("DraftPRD.md", "r", encoding="utf-8") as f:
prd_content = f.read()
except FileNotFoundError:
prd_content = "No PRD draft found."
logger.info(f"{self.profile}: Researching for PRD...")
research_content = await self.research_action.run(
"Provide supporting research for the following PRD.", context=prd_content
)
return Message(content=research_content, role=self.profile, cause_by=type(self.research_action))
```

**Définition du workflow et des rôles principaux**

Les agents suivants collaborent pour automatiser chaque étape du processus de création de PRD :

- `ProjectManager` (Pam) crée, enregistre et révise le PRD.
- `Reviewer` (Rico) passe en revue le PRD et fournit un feedback.
- `Researcher` (Rita) génère des recherches d’appui pour le PRD.

### Étape 8. Constituer et piloter l’équipe

Utiliser le`Team` classe pour embaucher des agents et exécuter le workflow. Cette application utilise Typer pour exécuter le processus de manière interactive à partir de la ligne de commande.

```python
import typer
import asyncio
from metagpt.team import Team

app = typer.Typer()

@app.command()
def main(
idea: str = typer.Argument(..., help="A PRD for a banking application for wealth management"),
investment: float = typer.Option(3.0, "--investment", "-i", help="Dollar amount to invest in the project."),
n_round: int = typer.Option(2, "--n-round", "-n", help="Number of rounds to run the simulation."),
):
async def runner():
team = Team(use_mgx=False)
team.hire([
ProjectManager(),
Researcher(),
Reviewer(),
])
team.idea = idea
team.invest(investment=investment)
team.run_project(idea)
await team.run(n_round=n_round)
asyncio.run(runner())

if __name__ == "__main__":
app()
```

#### Comment fonctionne la CLI

- `@app.command()` : indique à Typer que la fonction suivante (`main` ) est une commande qui peut être exécutée à partir du terminal.
- `main(...)` : la fonction principale qui exécute le programme. Il faut trois arguments :
  - `idea` : l’idée du projet (par exemple, « Un PRD pour une application bancaire de gestion de patrimoine ».)\
  - `investment` : un montant d’investissement facultatif (par défaut :`3.0` ). Cette action simule le budget de l’équipe et peut affecter la prise de décision des agents et la planification.
  - `n_round` : argument facultatif spécifiant le nombre de cycles que la simulation doit exécuter (par défaut :`2` ).

#### Constitution et pilotage de l’équipe

- `runner()` : une fonction asynchrone qui exécute le workflow :
  - `team = Team(use_mgx=False)` : crée un nouvel`Team` objet représentant un groupe d’agents IA.  `use_mgx=False` L’option désactive le mode de communication MGX avancé en s’appuyant sur le comportement d’équipe standard.
  - `team.hire([...])` : embauche (ajoute) des agents à l’équipe.
  - `team.idea = idea` : définit l’idée de projet de l’équipe à partir de l’entrée CLI.
  - `team.invest(investment=investment)` : attribue le « financement » de l’équipe, influençant la façon dont les agents simulent la planification et l’allocation des ressources.
  - `team.run_project(idea)` : démarre le projet avec l’idée donnée.
  - `await team.run(n_round=n_round)` : exécute le workflow avec le nombre de tours spécifié, ce qui permet aux agents d’améliorer de manière itérative le PRD.

#### Remarque sur la variabilité des sorties

**Remarque importante :**\
Les documents et sorties générés par ce tutoriel utilisent de grands modèles de langage (LLM), qui sont probabilistes et peuvent occasionnellement produire des résultats incomplets, inexacts ou incohérents.\
**Examinez et validez vous-même tout le contenu généré.**\
Les LLM sont des outils utiles, mais ils ne peuvent pas remplacer entièrement les compétences et le jugement d’une véritable équipe de développement de produits.

#### Exemple de commande

Pour exécuter le programme avec les valeurs par défaut pour`n_round` et`investment` :

```bash
python metagpt_prd_generator.py "Write a PRD for a banking app for wealth managers."
```

Cette commande lancera l’équipe d’agents, automatisera le processus de création de PRD et répétera le processus en respectant le nombre de tours spécifié.

#### Résumé du processus de création d’équipe

- Les **actions** définissent ce que chaque agent peut faire.
- **Les rôles** représentent les agents et les relient aux actions.
- La classe **Équipe** rassemble les agents pour automatiser le workflow PRD.

Cette approche modulaire permet d’affiner le processus d’automatisation des tâches de développement de produits complexes.

## Exemple de brouillon de sortie et PRD final

Lorsque vous exécutez l’application, les agents collaborent pour produire et affiner une PRD.

- **Brouillon de PRD** (`DraftPRD.md` ) : le PRD initial créé par l’agent chef de projet.
- Examiner le feedback : suggestions et critiques de l’agent évaluateur.
- **Rapport de recherche** : il appuie les études techniques et de marché de l’agent chercheur.
- **PRD final** (`PRD.md` ): le PRD révisé, intégrant les modifications et la recherche.

### Brouillon de PRD (extrait)

```
# Product Requirements Document: Wealth Manager Banking App

## 1. Introduction & Overview
*   **Product Name:** [Proposed Name - e.g., "WealthBank Pro", "Portfolio Navigator"]
*   **Version:** v0.1 (Initial Draft)
*   **Author:** [Your Team/Name]
*   **Date:** October 26, 2
*   **Status:** Draft

## 2. Purpose & Goals
The purpose of this app is to solve key pain points faced by wealth managers and
their clients with a seamless, integrated digital platform for managing assets,
monitoring portfolio performance, accessing banking services, and facilitating
communication within the financial advisory context.

... (see full draft (`example_DraftPRD.md`) for more sections)
```

### PRD final (extrait)

```
# Product Requirements Document: Wealth Manager Banking App

## 1. Introduction & Overview
*   **Product Name:** WealthBank Pro (or Portfolio Navigator - to be confirmed)
*   **Version:** v0.2
*   **Author:** [Your Team/Name]
*   **Date:** October 26, 2023
*   **Status:** Draft
*   **Document Revision Notes:** Addressed reviewer suggestions by clarifying
terms, adding measurable goals, expanding integrations, including user stories,
and added missing sections (User Roles, Data Flow).

## 2. Purpose & Goals
This app provides a secure digital platform for financial advisors to manage client
portfolios and offers clients an intuitive interface to monitor their investments
alongside core banking services.

### Measurable Key Goals:
1.  **Enhance Advisor Efficiency:** Reduce investment monitoring time by
[Specify %]%,decrease report generation time by [Specify %]%.
2.  **Improve Client Experience:** Achieve a Net Promoter Score (NPS) of
[Target NPS score], increase client engagement via app to [Target percentage]%.
3.  **Secure Collaboration:** Reduce email inquiries between advisor and clients
by [Target reduction %]%, ensure all messages are traceable within the platform.

## 3. User Roles
*   **Wealth Manager/Financial Advisor:** Full access to assigned portfolios,
reporting, and communication.
*   **High-Net-Worth Client:** View-only access to their own portfolio and
account information.
*   **Administrative Staff (Optional):** Read-only access for reporting/client onboarding.

... (see full final PRD (`example_PRD.md`)for more sections)
```

#### Améliorations apportées par les agents

Le fichier PRD.md final inclut une section intitulée **Notes de révision du document** qui résume les principales modifications apportées au cours du processus de révision. Cette section aide les parties prenantes à identifier rapidement ce qui a été mis à jour dans le document.

Voici les principales améliorations apportées à la version finale du PRD pour l’application de gestion de patrimoine :

- **Objectifs mesurables ajoutés :** ajout d’indicateurs de réussite (KPI clairs, scores NPS et réduction des délais), pour éclairer le MVP et l’optimisation.
- **Rôles des utilisateurs :** rôles et autorisations définis pour les conseillers, les clients et le personnel.
- **Intégrations :** API et protocoles de sécurité spécifiés pour le flux de données.
- **Notes de révision des documents :** résumé des principales modifications pour faciliter le suivi.
- **Histoires d’utilisateurs :** scénarios développés et clarifiés pour garantir des exigences exploitables.
- **Recherche :** incorporation de la stratégie de mise sur le marché, comme les modèles tarifaires et les données techniques pour étayer les décisions.

#### Exemples de fichiers de sortie

- `DraftPRD.md` : document d’exigences initial.
- `PRD.md` : document d’exigences final et révisé.
- (Facultatif) `Research.md` : Études de marché et techniques à l’appui du PRD.

## Conclusion

En suivant ce tutoriel, vous avez appris à automatiser la création et l’affinement d’un document sur les exigences produit en utilisant MetaGPT et Ollama. Vous avez mis en place une équipe multi-agents, défini des actions et rôles personnalisés et exécuté un workflow itératif qui produit des PRD de qualité et exploitables. Cette approche modulaire peut être adaptée à d’autres tâches d’IA collaboratives, ce qui en fait un outil puissant pour rationaliser la gestion des produits avec l’IA.
