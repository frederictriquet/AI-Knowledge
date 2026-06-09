> Source : https://www.ibm.com/fr-fr/think/tutorials/build-rewoo-reasoning-agent-granite

# Créer un agent de raisonnement ReWOO à l’aide d’IBM Granite

[Les grands modèles de langage (LLM)](https://www.ibm.com/fr-fr/think/topics/large-language-models) et leurs variantes améliorées, les modèles de langage augmentés (ALM), sont devenus la pièce maîtresse des systèmes d’IA modernes. En combinant une puissante génération de langage avec des techniques externes de récupération de connaissances comme la [génération augmentée par récupération (RAG)](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation), ils fournissent un raisonnement avancé, des réponses aux questions et une automatisation dans divers domaines. Cependant, malgré leurs capacités remarquables, ces modèles rencontrent souvent des difficultés lorsqu’ils doivent traiter des tâches complexes : robustesse incohérente entre les systèmes, utilisation élevée des tokens, temps de réponse lent et inefficacités causées par des prompts répétitifs et un contexte redondant. Ces limitations augmentent les coûts opérationnels et entravent l’évolutivité et les performances en temps réel.

Pour surmonter ces problèmes, le framework ReWOO (rationalisation sans observation) offre une approche novatrice qui vise à découpler le raisonnement de la récupération externe de connaissances. Au lieu d’avoir un seul LLM qui essaie de raisonner et d’observer de manière dissociée, ReWOO sépare ces préoccupations en modules distincts, chacun potentiellement alimenté par un LLM, mais avec un rôle spécifique. En structurant le processus en étapes distinctes de planification, de collecte de preuves et de synthèse, ReWOO améliore l’efficacité et la précision des tokens. Il facilite également le débogage du système et permet des [workflows](https://www.ibm.com/fr-fr/think/topics/agentic-workflows) d’IA plus rationalisés et plus efficaces.

## La méthodologie sous‑jacente de ReWOO

Le workflow de ReWOO s’articule autour de trois composants principaux : le raisonnement par étapes, les [appels d’outils](https://www.ibm.com/fr-fr/think/topics/tool-calling) et la synthèse. Ces composants sont implémentés dans une structure modulaire composée de trois parties : le planificateur, le worker et le solveur.

### Planificateur

Le planificateur décompose la tâche principale en une séquence de sous‑questions ciblées, créant ainsi un schéma directeur clair. Au lieu de demander au LLM de répondre à une question complexe en même temps, ce qui peut conduire à une utilisation massive des tokens et à des réponses confuses, le planificateur crée un schéma directeur ou une feuille de route. Cette répartition étape par étape guide le workflow et maintient la structure du processus de raisonnement.

### Worker

Le worker appelle des outils externes tels que des moteurs de recherche ou des bases de données pour récupérer les informations et les preuves pertinentes nécessaires pour répondre aux sous‑questions. Il utilise le LLM pour formuler des réponses claires et concises basées uniquement sur ces informations récupérées. Cette phase d’observation externe est séparée du processus de raisonnement afin d’éviter une répétition inutile des prompts et de réduire la consommation de tokens.

### Solveur

Le solveur synthétise toutes les informations recueillies pour générer une réponse finale récente et bien structurée. Cette séparation modulaire permet de garantir un raisonnement efficace, précis et évolutif avec de grands modèles de langage.

Des frameworks comme [LangChain](https://www.ibm.com/fr-fr/think/topics/langchain) et [LangGraph](https://www.ibm.com/fr-fr/think/topics/langgraph) offrent des outils puissants pour mettre en œuvre l’architecture ReWOO en utilisant des modèles d’OpenAI, [IBM Granite](https://www.ibm.com/fr-fr/products/watsonx-ai/foundation-models) ou des outils spécialisés comme Serper et Tavily pour la recherche.

Dans ce tutoriel, vous découvrirez comment créer un agent ReWOO qui effectue la tâche de synthèse de contenu. Cet [agent](https://www.ibm.com/fr-fr/think/topics/ai-agents) peut :

- Décomposer une tâche de premier niveau en sous‑questions
- Utiliser la recherche Web pour recueillir le contexte pertinent pour chaque sous‑question
- Générer des réponses à l’aide d’IBM Granite
- Résumer les résultats dans une réponse finale

Cette architecture est utile pour :

- Les tâches de synthèse
- Répondre aux questions sur les connaissances externes
- Le raisonnement dynamique augmenté par des outils

## Technologies utilisées

Ce tutoriel étape par étape s’appuie sur des technologies d’IA de pointe, notamment :

1.  IBM Granite Instruct : LLM puissant pour le suivi des instructions générales, idéal pour les assistants d’IA en entreprise et dans d’autres domaines.
2.  Transformers : bibliothèque Python très utilisée qui fournit des outils pour charger, tokeniser et exécuter des modèles de langage tels qu’IBM Granite. Elle permet un traitement efficace des entrées textuelles et la génération des sorties de modèle.

## Étapes

### Étape 1 : Configurer votre environnement

Ce tutoriel vous guide tout au long du processus de configuration de votre environnement de développement local afin d’exécuter un pipeline de raisonnement de type ReWOO à l’aide de Jupyter Notebook. Vous utiliserez le modèle de langage IBM Granite et Serper.dev pour la récupération des recherches Web en direct.

**Remarque** : aucun GPU n’est nécessaire, mais l’exécution peut être plus lente sur les systèmes basés sur CPU. Cette étape ouvre un environnement de notebook dans lequel vous pouvez copier le code de ce tutoriel. Ce tutoriel est également disponible sur GitHub.

### Étape 2 : Installer les dépendances requises

Ces bibliothèques sont nécessaires pour exécuter le pipeline ReWOO et interagir avec des outils externes :

**transformers** : charge et exécute le grand modèle de langage IBM Granite.

**torch** : framework d’apprentissage profond nécessaire au bon fonctionnement du modèle.

**accelerate** : optimise les performances du modèle sur l’ensemble du matériel (en option).

**requests** : envoie des requêtes HTTP POST aux [API](https://www.ibm.com/fr-fr/think/topics/api) externes (comme Serper).

```
!pip install transformers accelerate torch requests
```

### Étape 3 : Importer les bibliothèques requises

Dans cette étape, nous importons les bibliothèques Python nécessaires à la création des composants principaux du pipeline ReWOO.

**transformers.AutoTokenizer** : charge le tokeniseur qui convertit le texte en tokens compatibles avec le modèle de langage.

**transformers.AutoModelForCausalLM** : charge le modèle de langage pré-entraîné IBM Granite pour générer des réponses.

**transformers.pipeline** : fournit une interface de premier niveau pour créer rapidement un pipeline de génération de texte à l’aide du tokeniseur et du modèle.

```python
import requests
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
```

### Étape 4 : Charger le modèle IBM Granite et créez un pipeline de génération de texte

Lors de cette étape, nous chargeons le modèle de langage IBM Granite et nous initialisons un pipeline de génération de texte à l’aide de la bibliothèque de transformers de Hugging Face. Consultez le modèle d’instruction Granite 3.2 2B sur Hugging Face [ici](https://huggingface.co/ibm-granite/granite-3.2-2b-instruct).

**model_id = "ibm-granite/granite-3.2-2b-instruct"** : indique le nom du point de contrôle du modèle IBM Granite hébergé sur Hugging Face. Ce modèle est optimisé pour les tâches qui suivent des instructions.

**AutoTokenizer.from_pretrained(model_id)** : charge le tokeniseur associé au modèle spécifié. Assure la conversion du texte d’entrée en tokens et le décodage des tokens de sortie en texte.

**AutoModelForCausalLM.from_pretrained(model_id)** : charge le modèle de langage (instruction Granite 3.2 2B) pour les tâches de génération de texte telles que les réponses aux questions ou la synthèse.

**pipeline("text-generation", model=model, tokenizer=tokenizer)** : crée un pipeline de génération de texte de premier niveau qui combine le modèle et le tokeniseur, ce qui facilite la génération de réponses à partir de prompts.

```
model_id = "ibm-granite/granite-3.2-2b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
```

### Étape 5 : Configurer l’API Serper pour la récupération des recherches Web

Dans cette étape, nous définissons une fonction qui agit comme le worker dans l’architecture ReWOO. Ce worker utilise un outil de recherche Web, Serper.dev, pour récupérer des informations pertinentes et à jour sur Internet afin de soutenir le [raisonnement](https://www.ibm.com/fr-fr/think/topics/ai-reasoning) et la génération de réponses. Serper.dev est une API rapide et légère qui fournit des résultats de recherche Google dans un format structuré, idéale pour récupérer des informations en temps réel dans les workflows d’IA.

Cette configuration permet au système ReWOO d’« observer » le monde réel en interrogeant des sources de connaissances externes avant que le LLM ne prenne des décisions finales.

Pour utiliser Serper dans le pipeline ReWOO :

1.  Accédez à [https://serper.dev](https://serper.dev/) et créez un compte gratuit.
2.  Après l’inscription, accédez au tableau de bord et copiez la clé API.
3.  Stockez la clé API dans le code de manière sécurisée. Pour l’instant, attribuez-la directement comme indiqué après ceci :

**SERPER_API_KEY = "\"** \# Replace this with your actual key

**Remarque** : ne remplacez jamais votre clé API sur des référentiels publics. Pour les paramètres de production ou d’équipe, utilisez des fichiers .env ou des variables d’environnement pour les sécuriser.

**def query_serper(question, num_results=3)** : définit une fonction qui prend une question de recherche et renvoie des extraits pertinents à partir des principaux résultats de recherche.

**payload = {"q": question, "num": num_results}** : prépare la charge utile de la requête avec le terme de recherche et le nombre de résultats à renvoyer.

**réponse = Requests.post (...)** : envoie une requête POST à l’API Serper avec votre requête et vos en-têtes.

**response.raise_for_status()** : déclenche une erreur si la réponse de l’API est non valide ou échoue.

**snippets = \[...\]** : récupère un extrait de texte à partir des résultats de recherche organique.

**return "\n".join(snippets)** : relie et renvoie les extraits sous forme de chaîne unique, servant de contexte pour le modèle de langage.

**Remarque** : cette fonction est l’élément central de l’étape « observation » de ReWOO, où des preuves externes sont collectées pour un raisonnement plus approfondi. Assurez-vous que votre clé API est valide et non limitée en débit lors du test.

```python
SERPER_API_KEY = "your_serper_api_key_here"  # Replace with your actual key
def query_serper(question, num_results=3):
url = "https://google.serper.dev/search"
headers = {
"X-API-KEY": SERPER_API_KEY,
"Content-Type": "application/json"
}
payload = {"q": question, "num": num_results}
response = requests.post(url, headers=headers, json=payload)
response.raise_for_status()
data = response.json()
snippets = [item.get("snippet", "") for item in data.get("organic", [])]
return "\n".join(snippets)
```

### Étape 6 : Générer des réponses documentées à l’aide de la fonction experte

Dans cette étape, nous définissons la fonction expert(), qui sert de solveur dans l’architecture ReWOO. Le solveur synthétise les preuves externes récupérées et génère une réponse finale à l’aide du modèle de langage.

**def expert(question: str) -\> str** : la fonction expert() prend une question (chaine) et renvoie une réponse (chaine) générée par le modèle Granite. Elle effectue une recherche sur le Web avec Serper.dev, recueille des informations pertinentes et les utilise pour générer une réponse claire et complète.

**context = query_serper(question)** : utilise l’outil de recherche Web Serper pour récupérer les informations pertinentes (worker).

**prompt = f"""..."""** : crée un prompt qui indique au modèle de répondre en utilisant uniquement le contexte récupéré.

**générator(...)** : appelle le modèle Granite pour générer une réponse basée sur le prompt d’entrée.

**for \_ in range(5)** : cette boucle permet au modèle de générer une réponse divisée en fragments, jusqu’à 5 fois. Elle est utile si la réponse est longue et ne peut pas être envoyée en une seule fois.

**generated_text += new_text** : ajoute chaque nouveau fragment de texte pour former la réponse complète.

**if new_text.endswith(...)** : met fin à la boucle si la réponse semble complète (se termine par un point, un point d’interrogation ou un point d’exclamation) et comporte suffisamment de mots (plus de 50).

**return generated_text.strip()** : renvoie la réponse finale nettoyée.

**Remarque** : le format du prompt est important, il garantit que le modèle n’« hallucine » pas ou ne s’écarte pas du sujet. Il doit s’en tenir au contexte. Nous limitons chaque fragment de génération à 120 tokens afin de contrôler la longueur de sortie et gérer efficacement l’utilisation des ressources tout en empêchant l’utilisation excessive de tokens.

```python
def expert(question: str) -> str:
context = query_serper(question) # your retrieval function
prompt = f"""You are a knowledgeable expert. Based ONLY on the context below, answer the question clearly and concisely in your own words.
Do NOT mention any sources or references.
Context:
{context}
Question: {question}
Answer:"""
input_prompt = prompt
generated_text = ""
last_generated = ""
for _ in range(5): # up to 5 chunks
outputs = generator(
input_prompt,
max_new_tokens=120,
do_sample=False,
eos_token_id=tokenizer.eos_token_id,
# no invalid flags like 'temperature' here
)
text = outputs[0]["generated_text"]
new_text = text[len(input_prompt):].strip()
# Stop if no new content
if new_text == last_generated:
break
generated_text += new_text + " "
input_prompt = prompt + generated_text
last_generated = new_text
if new_text.endswith(('.', '!', '?')) and len(generated_text.split()) > 50:
break
return generated_text.strip()
```

### Étape 7 : Définir le module planificateur

À cette étape, nous définissons la fonction Planner, qui décompose une tâche d’entrée large en sous‑questions plus petites et bien définies, un principe fondamental du [raisonnement par étapes](https://www.ibm.com/fr-fr/think/topics/agentic-reasoning) de ReWOO.

**def planner(task: str)** : définit une fonction nommée planner qui accepte une tâche à un seul argument (une chaîne décrivant la tâche à effectuer).

**topic = task.replace("Summarize", "").replace("the novella", "").strip()** : extrait l’objet principal de la tâche (par exemple, le titre ou le thème). Nettoie l’entrée en supprimant les expressions de prompt courantes telles que « Résumer » et « le roman », puis élimine les espaces blancs de début et de fin pour isoler le sujet principal.

**return \[ ... \]** : renvoie une liste de questions spécifiques qui guident le module Worker.

**Remarque** : vous pouvez élargir cette liste avec des sous‑questions plus spécifiques en fonction de la profondeur et du thème de l’entrée.

```python
def planner(task: str):
topic = task.replace("Summarize", "").replace("the novella", "").strip()
return [
f"What is the main plot related to {topic}?",
f"Who are the key characters in {topic}?",
f"What themes are explored in {topic}?"
]
```

### Étape 8 : Définir le synthétiseur final (module solveur)

À cette étape, nous définissons la fonction final_summarizer, qui agit comme le solveur dans le pipeline ReWOO. Cette fonction prend les sous‑réponses (preuves) fournies par le worker et génère un résumé nouvellement écrit et cohérent en utilisant le modèle de langage.

**def final_summarizer(task: str, sub_answers: dict) -\> str** : définit la fonction qui reçoit la tâche d’origine et les sous‑réponses, et renvoie un résumé concis.

**insights = "\n".join(sub_answers.values())** : combine toutes les réponses en une seule chaîne séparée par des nouvelles lignes pour l’inclusion dans le prompt.

**base_prompt = f"""..."""** : construit le prompt de base demandant au modèle de résumer les informations fournies. Guide le modèle pour générer un résumé actualisé basé uniquement sur les sous‑réponses.

**max_total_tokens = 400** : définit une limite supérieure pour le nombre de jetons générés afin d’éviter les sorties excessivement longues.

**max_loops = 5** : permet d’effectuer jusqu’à 5 itérations de génération pour construire progressivement le résumé.

**for in range(maxloops)** : boucles permettant de générer des fragments de texte à l’aide du modèle de langage.

**response = generator(..., max_new_tokens=100, ...)** : utilise le générateur (objet pipeline) pour générer jusqu’à 100 nouveaux tokens dans chaque boucle. Le mode Sampling (do_sample=True) permet la variation et la créativité dans la réponse.

**if summary.endswith(...) or total_tokens_used \>= max_total_tokens** : met fin à la boucle si le résumé se conclut par la ponctuation appropriée ou atteint la limite du token.

**return summary.strip()** : renvoie le résumé final et peaufiné, sans espaces de fin.

```python
def final_summarizer(task: str, sub_answers: dict) -> str:
insights = "\n".join(sub_answers.values())
base_prompt = f"""You are an expert summarizer. Based on the following insights, write a fresh, concise summary of the text. The summary must be newly written and must end in a complete sentence with proper punctuation.
Insights:
{insights}
Summary:"""
summary = ""
current_prompt = base_prompt
max_total_tokens = 400
total_tokens_used = 0
max_loops = 5
for _ in range(max_loops):
response = generator(current_prompt, max_new_tokens=100, do_sample=True, top_p=0.9, eos_token_id=tokenizer.eos_token_id)
chunk = response[0]["generated_text"][len(current_prompt):].strip()
summary += " " + chunk
summary = summary.strip()
total_tokens_used += len(chunk.split())
if summary.endswith(('.', '!', '?')) or total_tokens_used >= max_total_tokens:
break
# Prepare prompt for next loop
current_prompt = base_prompt + summary
return summary.strip()
```

### Étape 9 : Orchestrer l’agent ReWOO avec la fonction de solveur

Dans cette étape, nous définissons la fonction Solver, qui représente l’étape finale du pipeline ReWOO. Elle orchestre le processus complet en utilisant le planificateur, en appelant l’expert (worker) et en générant un résumé à l’aide du final_summarizer (solveur). L’architecture ReWOO permet un raisonnement à plusieurs étapes en décomposant la tâche principale en sous‑questions à l’aide d’un planificateur. Chaque sous‑question est traitée indépendamment par un module expert, et le synthétiseur final synthétise toutes les réponses en une réponse cohérente. Cette approche modulaire permet au système de s’attaquer plus efficacement à des tâches complexes.

**def solver(task: str)** : définit la fonction de contrôleur principal pour l’exécution du workflow ReWOO complet.

subquestions = planner(task) : utilise le planificateur pour diviser la tâche d’entrée en sous‑questions ciblées.

**ans = expert(q)** : pour chaque sous‑question, appelle la fonction experte pour récupérer des preuves sur le Web et générer une réponse pertinente. Chaque sous‑question générée par le planificateur est transmise à l’expert en tant qu’entrée d’outil. Le module expert traite l’entrée à l’aide d’un modèle de langage. Cela peut être considéré comme exécuter un outil pour une sous‑tâche spécifique.

**answers\[q\] = ans** : stocke chaque réponse associée à sa question correspondante pour un résumé ultérieur.

**final_summary = final_summarizer(task, answers)** : insère toutes les réponses collectées dans le final_summarizer pour générer un résumé clair et cohérent.

**print(final_summary) and return final_summary** : affiche et renvoie le résumé terminé pour la tâche d’origine.

**Remarque** : le temps total nécessaire à la fonction solver() peut varier d’un système à l’autre en raison des différences de vitesse du processeur, de la mémoire RAM disponible et de l’efficacité avec laquelle le modèle s’exécute sur différentes configurations matérielles. Comme le code utilise une stratégie de génération en boucle avec un modèle de langage, les systèmes dotés d’une puissance de traitement ou d’une mémoire plus faible peuvent prendre beaucoup plus de temps. La récupération basée sur le réseau et les tailles de prompt importantes peuvent également contribuer aux retards. Pour améliorer les performances, envisagez de réduire max_loops en utilisant un modèle plus petit ou quantifié, en optimisant le pipeline de tokenisation et de génération ou en exécutant le code dans un environnement compatible GPU tel que Google Colab ou Kaggle Notebooks.

```python
def solver(task: str):
print(f"Planner: Breaking down '{task}' into sub-questions...\n")
subquestions = planner(task)
answers = {}
for q in subquestions:
print(f"🔎 Expert answering: {q}")
ans = expert(q)
print(f"➡ Answer: {ans}\n")
answers[q] = ans
print("=== Final Summary ===\n")
final_summary = final_summarizer(task, answers)
print(final_summary)
return final_summary
```

### Étape 10 : Exécuter le pipeline ReWOO pour générer le résumé final

Dans cette dernière étape, nous exécutons le pipeline ReWOO complet en appelant la fonction solver avec une tâche spécifique.

**solver("Summarize the novella The Metamorphosis")** : déclenche l’ensemble du processus ReWOO; [planification](https://www.ibm.com/fr-fr/think/topics/ai-agent-planning), récupération des preuves et génération d’un résumé pour la tâche d’entrée : résumé de l’[ensemble de données](https://www.ibm.com/fr-fr/think/topics/dataset) The Metamorphosis.

Cette étape génère le résumé final et montre comment les composants ReWOO fonctionnent ensemble de bout en bout pour un cas d’utilisation réel.

```
solver("Summarize the novella The Metamorphosis")
```

## Points essentiels à retenir

1.  L’agent ReWOO est parvenu à décomposer la tâche (« Résumer le roman La Métamorphose ») en sous‑questions pertinentes concernant l’action, les personnages et les thèmes, permettant ainsi une récupération ciblée des informations.
2.  Chaque sous‑question a été traitée à l’aide d’une recherche Web en temps réel (Serper.dev) et d’IBM Granite pour produire des réponses pertinentes et bien structurées qui capturent les éléments essentiels du texte.
3.  La réponse finale était cohérente, nouvellement rédigée et précise, démontrant comment la génération augmentée par récupération peut produire des résumés de style humain de haute qualité pour les tâches d’analyse littéraire.

**Remarque** : pour améliorer les performances et la fiabilité du pipeline ReWOO, il est important d’améliorer les indicateurs d’évaluation tels que la qualité du résumé, la cohérence et la latence de génération. Ces indicateurs permettent d’évaluer les performances du système sur différentes tâches et configurations matérielles. L’architecture peut être étendue en intégrant des [algorithmes](https://www.ibm.com/fr-fr/think/topics/machine-learning-algorithms) intelligents, qui permettent de diviser les grandes questions en questions plus petites et de trier les réponses les plus utiles. Ces améliorations devaient permettre un raisonnement plus précis et plus efficace, réduire le temps de génération et améliorer la qualité globale des résultats finaux.
