---
titre: "Mémoire court terme vs long terme"
theme: memoire
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-memory
source_titre: "Qu’est-ce que la mémoire des agents IA ?"
---

# Mémoire court terme vs long terme

**En une phrase** — la mémoire court terme est la fenêtre de contexte/buffer de la session courante ; la long terme est un store externe persistant relu à la demande.

## En détail
Un LLM seul ne mémorise rien : il faut un composant mémoire. La **mémoire à court terme (STM)** retient les entrées récentes pour des décisions immédiates ; utile en IA conversationnelle, elle est mise en œuvre par une mémoire tampon circulaire ou une fenêtre contextuelle contenant un volume limité de données récentes avant écrasement. Elle assure la continuité dans une session (ex. ChatGPT conserve l'historique d'une session) mais ne survit pas au-delà, ce qui la rend inadaptée à la personnalisation durable. La **mémoire à long terme (LTM)** stocke et récupère des informations entre sessions, pour un stockage permanent ; elle s'implémente via des bases de données, des graphes de connaissances ou des embeddings vectoriels. La RAG est considérée comme « l'une des techniques les plus efficaces » pour la LTM, l'agent extrayant l'information pertinente d'une base de connaissances stockée. Le défi central est l'efficacité de récupération : trop de données ralentit les réponses.

## Tradeoff / insight pour un senior
Le compromis est latence vs richesse : la STM est gratuite en infra mais volatile et bornée par la fenêtre ; la LTM apporte la persistance et la personnalisation au prix d'une couche de stockage/récupération et d'un risque de latence si le store n'est pas filtré.

## Source primaire
La classification s'appuie sur l'article CoALA (Cognitive Architectures for Language Agents, Université de Princeton, février 2024).

## Voir aussi
- [Mémoire épisodique / sémantique / procédurale](memoire-episodique-semantique-procedurale.md)
