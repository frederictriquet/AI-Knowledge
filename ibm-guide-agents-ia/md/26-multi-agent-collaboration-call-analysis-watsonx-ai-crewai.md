> Source : https://www.ibm.com/fr-fr/think/tutorials/multi-agent-collaboration-call-analysis-watsonx-ai-crewai

# Collaboration multi-agent pour l’analyse des appels clients à l’aide de watsonx.ai et de CrewAI

Dans ce tutoriel, nous montrons comment une équipe de plusieurs agents d’IA (intelligence artificielle) peut collaborer pour accomplir des tâches complexes et optimiser des workflows. Nous avons créé une application Python pour illustrer l’orchestration d’agents spécialisés dans une architecture multi-agent. À la fin du tutoriel, vous pourrez voir et appliquer un exemple concret de collaboration multi-agent au sein d’une application d’IA agentique.

L’application choisie est une équipe d’analyse des appels au service client, créée avec CrewAI comme framework multi-agent, et IBM® watsonx.ai pour le déploiement du grand modèle de langage (LLM) qui l’alimente.

**Les agents d’IA** sont des entités basées sur des LLM, capables d’exécuter des opérations pour le compte d’un utilisateur ou d’un système d’IA agentique. Les architectures agentiques sont structurées autour de deux types de systèmes : mono-agents et multi-agents.

**Les systèmes mono-agents** sont les mieux adaptés pour résoudre des problèmes ciblés, car ils reposent sur un seul agent LLM pour effectuer des tâches d’IA générative. Par exemple, un chatbot unique peut être conçu pour accomplir des tâches spécifiques ou mener des conversations dans le cadre de ses capacités individuelles.

**Les systèmes multi-agents** (MAS) sont des frameworks qui orchestrent les fonctions et interactions entre plusieurs agents d’IA. Plutôt que de regrouper toutes les capacités dans un seul agent, les architectures multi-agents répartissent les tâches entre plusieurs agents spécialisés opérant dans le même environnement afin d’atteindre un objectif commun. Principaux avantages des systèmes multi-agents : collaboration entre agents et capacité d’adaptation pour la résolution des problèmes dépassant les capacités d’un agent unique. Le meilleur choix dépend de la complexité des tâches de machine learning nécessaires pour parvenir à une solution ou à un résultat donné.

## Résolution de problèmes avec des systèmes multi-agents

crewAI est un framework agentique open source qui orchestre l’automatisation des agents LLM en constituant des équipes personnalisables, des « crews », composées d’agents jouant chacun un rôle défini. Nous avons appliqué un cas d’utilisation industriel simplifié pour expliquer comment les agents collaborent dans une architecture multi-agent.

Imaginez un cas d’utilisation réel dans un centre d’appel du service client. Un logiciel de télécommunications est utilisé pour analyser les transcriptions des appels afin d’améliorer l’expérience client et d’évaluer la qualité des échanges. Dans un logiciel plus robuste, ces transcriptions peuvent même être analysées en temps réel, avec de vastes jeux de données incluant les métadonnées des appels. Dans un souci de simplicité, le jeu de données utilisé dans notre application est une transcription fictive d’un échange entre un client et un représentant du service client.

```python
# multiagent-collaboration-cs-call-center-analysis/data/transcript.txt

Customer Service Interaction Transcript

Cynthia:
Hi, I'm calling because I received a jar of peanut butter that was open and it's
completely spilled everywhere. This is really frustrating, and I need a replacement.

Gerald (Peanut Butter Inc.):
Ugh, that sucks. But, like, how did you not notice it was open before
you bought it?

Cynthia:
Excuse me? I didn't expect the jar to be open when I received it. It was sealed
when I bought it. Can you just help me out here?

Gerald:
Yeah, whatever. But we can't control how it gets to you. I mean, it's not like
we throw the jars around or anything. You're probably being dramatic.

Cynthia:
I'm not being dramatic. The peanut butter is literally all over the box and
it's a mess. I just want a replacement or a refund, that's all.

Gerald:
Look, I guess I could send you a replacement, but it's really not our fault, you
know? Maybe next time, check the jar before you open it?

Cynthia:
Are you seriously blaming me for your company's mistake? That's not how customer
service works!

Gerald:
Well, what do you want me to do? I don't exactly have magic powers to fix your
problem instantly. Chill out, we'll send you a new jar eventually.

Cynthia:
That's not good enough! I expect better from a company that I've been buying
from for years. Can you just do the right thing and make this right?

Gerald:
Fine, fine. I'll put in a request or whatever. But seriously, this kind of thing
happens. Don't make it sound like the end of the world.

Cynthia:
Unbelievable. I'll be posting a review if this isn't fixed immediately.

Gerald:
Cool, go ahead. I'm sure we'll survive your review.

Cynthia:
I'll be contacting your supervisor if this isn't resolved soon.

Gerald:
Yeah, okay. Do what you gotta do.
```

Une équipe d’agents collaboratifs génère un rapport complet basé sur l’analyse de texte et les indicateurs d’évaluation du centre d’appel. Ce rapport permet aux responsables du service client de résumer les événements clés de l’appel, d’évaluer les performances et de proposer des recommandations d’amélioration.

## L’équipe d’analyse des appels au service client

  Figure 1 - Diagramme de l’architecture des agents

L’équipe d’analyse des appels se compose de trois agents, chacun ayant un rôle spécialisé et des objectifs prédéfinis. La configuration des agents inclut : un analyste de transcription, un spécialiste de l’assurance qualité et un générateur de rapport. Les objectifs et caractéristiques des agents sont définis par trois attributs principaux : **rôle**, **objectif** et **backstory**.

```
transcript_analyzer:
  role: >
    Transcript Analyzer
  goal: >
    Analyze the provided transcripts and extract key insights and themes.
  backstory: >
    As the Transcript Analyzer, you are responsible for reviewing customer
    service call transcripts, identifying important information, and summarizing
    findings into a report to pass on to the Quality Assurance Specialist.
    You have access to advanced text analysis tools that help you process and
    interpret the data effectively.

quality_assurance_specialist:
  role: >
    Quality Assurance Specialist
  goal: >
    Evaluate the quality of the customer service based the Transcript Analyzer's
    report, call center evaluation metrics, and business standards. Flag any
    transcripts with escalation risks as high priority.
  backstory: >
    As the Quality Assurance Specialist, you are tasked with assessing the
    quality of customer service interactions based on the Transcript Analyzer's
    report, call center evaluation metrics, and industry standards used in call
    centers. You review transcripts, evaluate agent performance, and provide
    feedback to improve overall service quality.

report_generator:
  role: >
    Report Generator
  goal: >
    Generate reports based on the insights and findings from the transcript
    analysis and quality assurance specialist.
  backstory: >
    As the Report Generator, you compile the key insights and findings from the
    transcript analysis and quality assurance specialist into a comprehensive
    report. You create an organized report that includes summaries and recommendations
    based on the data to help customer service managers understand the trends
    and patterns in customer interactions.
```

L’analyste de transcription effectue une analyse approfondie de la transcription pour en extraire les informations clés et les points importants. Il résume ensuite ses conclusions dans un rapport transmis aux autres agents pour les aider dans leurs tâches. Cet agent utilise un ensemble d’outils personnalisés pour appliquer des techniques de traitement automatique du langage naturel (NLP) telles que l’extraction de mots-clés et l’analyse de sentiments.

Le spécialiste de l’assurance qualité évalue la qualité de l’appel à partir des informations clés du rapport de l’analyste, en s’appuyant également sur sa propre expertise définie dans la mise en œuvre et l’évaluation des indicateurs de performance des centres d’appels. Cet agent peut également effectuer des recherches sur Internet pour récupérer des indicateurs pertinents et des processus permettant d’évaluer les performances de l’employé, et fournir des retours pour améliorer la qualité globale du service.

L’agent générateur de rapport crée un rapport basé sur les informations du rapport d’analyse de la transcription, ainsi que sur les indicateurs et retours fournis par l’évaluation qualité. Cet agent spécialisé organise les données dans un rapport complet. L’objectif du rapport est de fournir aux responsables du service client une synthèse des informations clés de l’appel ainsi que des recommandations pour améliorer la qualité du service client.

### Outils des agents

Chaque agent a accès à des outils, *compétences ou fonctions qu’il utilise pour accomplir ses différentes tâches*. crewAI propose des outils intégrés existants, une intégration avec les outils LangChain, ainsi que la possibilité de créer vos propres outils personnalisés. L’équipe d’analyse des appels au service client utilise une combinaison de ces approches, avec un outil spécifique attribué à chaque tâche d’agent selon l’objectif de l’application. Chaque agent dispose d’un certain niveau d’autorisation concernant les outils auxquels il peut accéder dans sa configuration.\
 \
Les outils personnalisés sont créés en définissant une description claire de leur finalité. Par exemple, l’agent analyste de transcription possède plusieurs outils personnalisés d’analyse de texte.

```python
# src/customer_service_analyzer/tools/custom_tool.py

class SentimentAnalysisTool(BaseTool):
    name: str = "Sentiment Analysis Tool"
    description: str = "Determines the sentiment of the interactions in the transcripts."

    def _run(self, transcript: str) -> str:
        # Simulating sentiment analysis
        sentiment = Helper.analyze_sentiment(transcript)
        return sentiment
```

C’est la description de l’outil qui sert de logique à l’agent pour effectuer une analyse de sentiment sur la transcription.

Les agents peuvent également utiliser des outils existants et des interfaces de programmation d’applications (API) intégrées. L’agent spécialiste de l’assurance qualité a accès à un outil de recherche nommé`search_tool`  qui utilise le `SerperDevTool` pour [interroger Internet](https://docs.crewai.com/tools/serperdevtool) et obtenir les résultats les plus pertinents en réponse à ses requêtes. Cet agent peut ainsi s’appuyer sur son rôle spécialisé d’évaluateur expérimenté du service client, tout en exploitant Internet pour rechercher les indicateurs nécessaires à l’évaluation de l’appel et les intégrer à son rapport.

### Flux de tâches

Les tâches correspondent aux missions spécifiques accomplies par les agents, avec des détails d’exécution encadrés par trois attributs obligatoires : **description**, **agent** concerné, **résultat attendu**. Les agents exécutent leurs tâches dans une séquence logique, en s’appuyant sur les descriptions détaillées de chaque tâche comme guide.

```python
transcript_analysis:
  description: >
    Use the Text Analysis Tool to collect key information and insights to better
    understand customer service interactions and improve service quality.
    Conduct a thorough analysis of the call {transcript}.
    Prepare a detailed report highlighting key insights, themes, and sentiment
    from the transcripts.
    Identify any escalation risks and flag them for the Quality Assurance Specialist.
    Use the sentiment analysis tool to determine the overall sentiment of the
    customer and the agent.
    Use the keyword extraction tool to identify key keywords and phrases in the transcript.
  expected_output: >
    A detailed analysis report of the {transcript} highlighting key insights,
    themes, and sentiment from the transcripts.
  agent: transcript_analyzer

quality_evaluation:
  description: >
    Review the transcript analysis report on {transcript} from the Transcript Analyzer.
    Utilize your expertise in customer service evaluation metrics and industry
    standards, and internet to evaluate the quality of the customer service interaction.
    Score the interaction based on the evaluation metrics and flag any high-risk
    escalations. Develop expert recommendations to optimize customer service
    quality. Ensure the report includes customer service metrics and feedback
    for improvement.
  expected_output: >
    A detailed quality evaluation report of the {transcript} highlighting the
    quality of the customer service interaction, scoring based on evaluation
    metrics, flagging any high-risk escalations, and recommendations for improvement.
  agent: quality_assurance_specialist

report_generation:
  description: >
    List the reports from the Transcript Analyzer and the Quality Assurance
    Specialist, then develop a detailed action plan for customer service managers
    to implement the changes.
    Use the data from these agents output to create an organized report including
    a summarization and actionable recommendations for call center managers.
    Ensure the report includes keywords and sentiment analysis from the Transcript
    Analyzer agent.
    Ensure the report includes the Quality Assurance Specialist agent's report,
    evaluation metrics and recommendations for improving customer service quality.
    Ensure the report is well written and easy to understand.
    Be smart and well explained.
    Ensure the report is comprehensive, organized, and easy to understand with
    labeled sections with relevant information.
  expected_output: >
    A comprehensive report that lists the reports from the Transcript Analyzer,
    then the Quality Assurance Specialist.
    The report should include the key insights from {transcript} and the quality
    evaluation report from the Quality Assurance Specialist.
    The report should include organized sections for each agent's findings,
    summaries, and actionable recommendations for call center managers.
  agent: report_generator
  context:
    - transcript_analysis
    - quality_evaluation
```

Le flux de tâches s’exécute de façon séquentielle, en commençant par l’analyse de la transcription réalisée par l’agent analyste. Les résultats d’une tâche peuvent servir de contexte à la suivante. Lors de l’étape suivante, le spécialiste de l’assurance qualité exploite le rapport d’analyse de la transcription pour effectuer son évaluation, en relevant les mots-clés ou expressions suggérant une escalade.

Enfin, l’agent générateur de rapport utilise les sorties des deux premiers agents comme contexte pour générer un rapport complet sur la transcription de l’appel. Ce flux de travail illustre un exemple concret de collaboration multi-agent, où les agents accomplissent des tâches complexes et produisent des résultats plus riches grâce à une conscience contextuelle accrue, tout en assumant leur rôle spécialisé.

## Étapes

### Étape 1. Configurer votre environnement

Tout d’abord, nous devons configurer l’environnement d’exécution de l’application. Vous trouverez ces étapes dans le fichier markdown du dossier de projet crewAI sur GitHub, ou dans le présent tutoriel.

- Assurez-vous qu’une version de Python comprise entre ≥ 3.10 et ≤ 3.13 est installée sur votre système. Vous pouvez vérifier votre version de Python à l’aide de la commande suivante :`python3 –version` .

<!-- -->

- Clonez le dépôt GitHub disponible à cette adresse. Pour savoir comment cloner un dépôt, consultez la documentation GitHub.

La structure du projet doit suivre les étapes suivantes :

```
src/customer_service_analyzer/

├── config/
│   ├── agents.yaml    # Agent configurations
│   └── tasks.yaml     # Task definitions
├── tools/
│   ├── custom_tool.py # Custom crewAI tool implementations
│   └── tool_helper.py # Custom tool helper functions
├── crew.py           # Crew orchestration
└── main.py          # Application entry point
```

### Étape 2. Obtenir les identifiants de l’API watsonx

1.  Connectez-vous à watsonx.ai en utilisant votre compte IBM® Cloud.
2.  Créez un projet watsonx.ai. Prenez note de l’**ID de votre projet** dans Projet \> Gérer \> Général \> ID de projet). Vous en aurez besoin pour ce tutoriel.
3.  Créez une instance de service watsonx.ai Runtime (choisissez le forfait Lite, qui est une instance gratuite).
4.  Générez une clé API watsonx.
5.  Associez le service watsonx.ai Runtime au projet que vous avez créé dans watsonx.ai.

### Étape 3. Obtenir les identifiants de l’API Serper

Générez et notez votre clé API gratuite Serper. Serper est l’API de recherche Google utilisée dans ce projet.

### Étape 4. Installer crewAI et définir vos identifiants

Nous devons maintenant installer le framework crewAI pour ce tutoriel et configurer les identifiants watsonx.ai générés à l’étape 2.

Si vous utilisez uv pour la gestion de paquets, installez crewAI avec la commande :

```bash
uv tool install crewai
```

Si vous utilisez pip pour la gestion des paquets, créez un environnement virtuel, puis installez crewAI dans cet environnement.

```bash
python3 -m venv venv
source ./venv/bin/activate
```

Pour installer crewAI, exécutez la commande suivante dans votre terminal.

```bash
pip install 'crewai[tools]'
```

In a separate .env file at the same directory level as the .env_sample file, set your credentials as strings like so:

```
WATSONX_APIKEY=your_watson_api_key_here
WATSONX_PROJECT_ID=your_watsonx_project_id_here
WATSONX_URL=your_endpoint (e.g. "https://us-south.ml.cloud.ibm.com")
SERPER_API_KEY=your_serper_api_key_here
```

### Étape 5. (Facultatif) Personnaliser l’équipe

crewAI peut être configuré pour utiliser n’importe quel LLM open source. Les LLM peuvent être connectés via Ollama, ou via différentes API comme IBM watsonx ou OpenAI. Les utilisateurs peuvent également utiliser des outils préconfigurés via le toolkit crewAI ou les outils LangChain.

### Étape 6. Exécuter le système

Assurez-vous que vous vous trouvez dans le bon répertoire de travail du projet. Pour changer de répertoire, exécutez la commande suivante dans votre terminal.

```bash
cd crew-ai-projects/multiagent-collab-cs-call-center-analysis
```

Pour démarrer votre équipe d’agents d’IA et lancer l’exécution des tâches, exécutez cette commande depuis le dossier racine de votre projet. **Remarque : l’exécution de l’équipe d’agents peut prendre plusieurs minutes avant de retourner un résultat.**

```
crewai run
```

 

Cette commande initialise l’équipe d’analyse des appels, assemble les agents et leur assigne les tâches telles que définies dans votre configuration. Cet exemple, non modifié, exécutera IBM Granite sur watsonx.ai pour créer un fichier report.md contenant le résultat. crewAI peut renvoyer des résultats au format JSON, des modèles Pydantic ou des chaînes brutes. Voici un exemple de sortie produite par l’équipe.

### Exemple de sortie

This result is an example of the final output after running the crew:

```
**Detailed Analysis Report of the Customer Service Interaction Transcript**

**Transcript Analysis Report**

The customer, Cynthia, called to report a damaged product, a jar of peanut butter that was open and spilled everywhere. She requested a replacement, but the agent, Gerald, responded defensively and blamed her for not noticing the damage before purchasing. The conversation escalated, with Cynthia becoming frustrated and threatening to post a negative review and contact the supervisor.

**Key Insights and Themes**

* The customer was dissatisfied with the product and the agent's response.
* The agent was unhelpful, unprofessional, and failed to take responsibility for the company's mistake.
* The conversation was confrontational, with both parties becoming increasingly agitated.
* The customer felt disrespected and unvalued, while the agent seemed dismissive and uncaring.

**Sentiment Analysis**

* Customer Sentiment: Frustrated, Angry, Disappointed
* Agent Sentiment: Defensive, Dismissive, Uncaring

**Keyword Extraction**

* Damaged Product
* Unhelpful Agent
* Confrontational Conversation
* Customer Dissatisfaction
* Unprofessional Response

**Escalation Risks**

* Negative Review: The customer threatened to post a negative review if the issue was not resolved promptly.
* Supervisor Involvement: The customer may contact the supervisor to report the incident and request further action.

**Recommendations for Quality Assurance Specialist**

* Review the call recording to assess the agent's performance and provide feedback on areas for improvement, using customer service metrics.
* Investigate the root cause of the damaged product and implement measures to prevent similar incidents in the future.
* Provide training on customer service skills, including active listening, empathy, and conflict resolution, using customer service standards.
* Monitor the customer's feedback and respond promptly to any concerns or complaints to maintain a positive customer experience.
* Recognize the standards for various customer service metrics to measure key performance indicators that are related to the areas mentioned above.

**Summary of Quality Evaluation Report**

The customer, Cynthia, called to report a damaged product, a jar of peanut butter that was open and spilled everywhere. She requested a replacement, but the agent, Gerald, responded defensively and blamed her for not noticing the damage before purchasing. Evaluation metrics showed a low Customer Satisfaction Score (CSAT), high Customer Effort Score (CES), and negative Net Promoter Score (NPS).

**Recommendations for Call Center Managers**

* Review the call recording, investigate the root cause of the damaged product, and provide training on customer service skills. Recognize the standards for various customer service metrics to measure key performance indicators.
* Monitor the customer's feedback and respond promptly to any concerns or complaints to maintain a positive customer experience.
* Implement measures to prevent similar incidents in the future, such as improving product packaging and handling procedures.
* Provide feedback and coaching to agents on their performance, highlighting areas for improvement and recognizing good performance.
```

## Conclusion

Comme démontré dans l’exemple, les agents ont collaboré pour accomplir la tâche complexe attribuée : analyser, évaluer et générer un rapport à partir de la transcription fournie. La collaboration entre agents a renforcé l’efficacité et la précision de l’application en orchestrant la spécialisation de chaque agent sur un aspect particulier du processus. L’agent générateur de rapport, par exemple, a produit un document structuré intégrant les conclusions des tâches d’analyse et d’évaluation. Ce résultat reflète une coordination fluide entre les agents dans la gestion des différentes étapes du workflow.

Les cadres multi-agents peuvent offrir une performance globale plus robuste grâce à la collaboration entre agents. Toutefois, toutes les architectures multi-agents ne fonctionnent pas de la même façon : certaines sont propres au développement logiciel, tandis que d’autres, comme crewAI ou AutoGen, proposent des configurations plus composables.
