---
titre: "ChatDev : ChatChain, CAMEL, déshallucination communicative"
type: "Concept"
theme: securite
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/topics/chatdev
source_titre: "Qu’est-ce que ChatDev ?"
---

# ChatDev : ChatChain, CAMEL, déshallucination communicative

**En une phrase** — un cadre qui simule une société de logiciels en cascade (conception/codage/test) via un dialogue à deux agents par phase, où l'assistant inverse délibérément les rôles pour réclamer des précisions avant de coder.

## En détail
ChatDev (OpenBMB) applique l'IA au modèle en cascade et orchestre ses agents par **ChatChain** : le processus est segmenté en phases séquentielles (Analyse de la demande, Sélection du langage, Codage, CodeCompleteAll, CodeReview, Test, EnvironmentDoc, Manuel). Chaque phase est un **dialogue à deux agents** — un instructeur qui dirige, un assistant qui exécute — poursuivi en multi-tours jusqu'à achèvement ou consensus. Pour limiter les hallucinations de codage, ChatDev introduit la **déshallucination communicative** : l'assistant « recherche de manière proactive plus d'informations » (noms de dépendances, dépôt GitHub) en adoptant un « renversement de rôle » délibéré — il joue l'instructeur pour demander des précisions — avant de fournir sa réponse formelle. ChatDev est bâti sur le cadre **CAMEL**, qui gère rôles, tâches et interactions des agents avec les modèles ; les agents communiquent par messages JSON structurés faisant office de tampon de mémoire partagée. Le tutoriel watsonx.ai illustre l'intégration via Llama-4-Maverick et une boucle CodeReview plafonnée à 10 itérations.

## Tradeoff / insight pour un senior
Insight non trivial : le « renversement de rôle » formalise le « pose des questions avant de coder ». Plutôt que de laisser l'assistant halluciner des détails manquants, le protocole l'oblige à interroger l'instructeur — anti-hallucination par interaction, là où MetaGPT le fait par schématisation.

## Source primaire
Dépôt OpenBMB/ChatDev et l'article fondateur ; la déshallucination communicative et MacNet y sont décrites sans DOI explicite dans le texte (voir l'article ChatDev / MacNet pour la référence exacte).

## Voir aussi
- [metagpt-pattern](metagpt-pattern.md)
- [macnet](macnet.md)
