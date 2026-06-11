---
titre: "BabyAGI"
type: "Concept"
theme: fondamentaux-agents
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/babyagi
source_titre: "Qu’est-ce que BabyAGI ?"
---

# BabyAGI

**En une phrase** — la boucle minimale de 2023 (Yohei Nakajima) à trois agents — exécution, création, priorisation — adossée à une mémoire vectorielle ; un « bac à sable éducatif » plus qu'un outil de production.

## En détail
BabyAGI est un cadre d'agent autonome partagé par Yohei Nakajima en 2023, qui génère et exécute une séquence de tâches selon un objectif utilisateur. Il orchestre une boucle de création, d'exécution et de priorisation à l'aide d'un LLM (généralement GPT-4) et d'un magasin de mémoire vectorielle. L'implémentation standard est un script Python utilisant les modèles GPT via API, une base vectorielle (typiquement Pinecone ; FAISS et Chroma dans des variantes) et LangChain pour structurer les rôles. La boucle en trois étapes : l'agent d'exécution exécute une tâche avec le contexte de la base ; l'agent de création génère des tâches de suivi à partir du résultat ; l'agent de priorisation réordonne la file selon dépendances et pertinence, jusqu'à épuisement ou condition d'arrêt. BabyAGI est qualifié de bac à sable éducatif plutôt que d'application de production, et n'est pas une IAG. En 2024, Nakajima a lancé BabyAGI 2, variante expérimentale utilisant un cadre *functionz* pour stocker fonctions et métadonnées en base.

## Exemple
Mise en route canonique : on clone le dépôt, `pip install` des dépendances, on copie le `.env` d'exemple et on y colle une clé API OpenAI et une clé Pinecone. On définit ensuite la variable `OBJECTIVE` (par ex. « rédiger un plan d'étude du marché des VE ») plus une tâche initiale, puis `python babyagi.py`. La boucle démarre : l'agent d'exécution traite la tâche avec le contexte vectoriel, l'agent de création en génère les suites, l'agent de priorisation réordonne la file selon dépendances — itération jusqu'à file vide ou condition d'arrêt. Toute la config tient dans un seul fichier `.env`.

## Tradeoff / insight pour un senior
Souvent comparé à AutoGPT : BabyAGI exécute une boucle compacte (création/exécution/priorisation + mémoire vectorielle), tandis qu'AutoGPT offre un cadre plus riche en intégration d'outils et passe mieux à l'échelle. BabyAGI reste un outil de recherche : sa lisibilité pédagogique est sa vraie valeur.

## Source primaire
Attribué à Yohei Nakajima (2023). Voir le dépôt GitHub BabyAGI.

## Voir aussi
- [autogpt](autogpt.md)
- [taxonomie-5-types-agents](taxonomie-5-types-agents.md)
