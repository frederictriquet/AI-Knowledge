---
titre: "LLM imbriqué dans un outil"
type: "Concept"
theme: outils-function-calling
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/tutorials/local-tool-calling-ollama-granite
source_titre: "Appel d’outil avec Ollama"
---

# LLM imbriqué dans un outil

**En une phrase** — un outil appelé par l'agent utilise lui-même un appel LLM en interne (ex. classifieur de pertinence yes/no).

## En détail
Un outil `search_text_files(keyword)` parcourt les fichiers d'un dossier local. Plutôt qu'un simple matching de chaînes, la fonction utilise Granite 3.2 pour déterminer si le mot-clé décrit le texte du document. Concrètement, l'outil lit le document dans `document_text`, puis appelle `ollama.chat` avec le prompt : `"Respond only 'yes' or 'no', do not add any additional information. Is the following text about " + keyword + "? " + document_text`. Si le modèle répond « yes », l'outil renvoie le nom de fichier. Le second outil, `search_image_files`, applique le même principe via Granite 3.2 Vision pour décrire chaque image et y chercher le mot-clé. À noter : « l'un des points forts de l'utilisation d'Ollama est qu'on peut facilement construire des systèmes multi-agents pour appeler un modèle avec un autre ».

## Exemple
Requête utilisateur « Information about dogs ». Granite 3.2 Dense extrait le mot-clé `dogs` et déclenche les deux outils en parallèle : `search_text_files(keyword="dogs")` itère sur `./files/`, et pour chaque PDF/`.txt` lance un appel `ollama.chat(model="granite3.2:8b", ...)` avec le prompt « Respond only 'yes' or 'no'… » — il renvoie `./files/File4.pdf` sur le premier « Yes ». `search_image_files(keyword="dogs")` fait décrire chaque image par `granite3.2-vision` et renvoie `None`. Les résultats sont réinjectés au modèle qui conclut : « The keyword "dogs" was found in File4.pdf. »

## Tradeoff / insight pour un senior
Le LLM d'orchestration (Granite 3.2 Dense) sélectionne l'outil et génère ses arguments ; un second appel LLM, encapsulé dans l'outil, fait le classement sémantique fin. Tu paies un appel par document scanné — coûteux et lent à l'échelle — mais tu gagnes une correspondance par sens plutôt que par chaîne littérale. Le pattern transforme « function calling » en arborescence d'appels LLM imbriqués, à surveiller pour la latence et le coût en tokens.

## Source primaire
« comme Ollama facilite l'appel de LLM locaux, `research_text_files` utilisera Granite 3.2 pour déterminer si le mot-clé décrit le texte du document. » ([source](../sources/ibm-guide-agents-ia/md/20-local-tool-calling-ollama-granite.md))

## Voir aussi
- [Tool calling / function calling](tool-calling.md)
- [RAG agentique](rag-agentique.md)
