---
titre: "Des rapports plutôt que du RAG (RAG comme feature, pas comme bénéfice)"
theme: rag-contexte
niveau: 🟢
source_url: https://jxnl.co/writing/2024/06/05/predictions-for-the-future-of-rag/
source_titre: "Predictions for the Future of RAG"---

# Des rapports plutôt que du RAG (RAG comme feature, pas comme bénéfice)

> Fiche **source : Jason Liu (jxnl)** · [post](../sources/jason-liu/md/predictions-future-rag.md) · Pertinence 🟢 vision

**En une phrase** — Liu prédit un glissement du RAG « question-réponse » vers la **génération de rapports**, parce que la valeur d'un rapport (aide à la décision) dépasse largement le temps gagné à trouver une réponse.

## Ce que dit la source
« RAG is the feature, not the benefit. » Selon Liu, les systèmes RAG en Q&A délivrent une valeur **unidimensionnelle** : le temps économisé pour trouver une réponse, difficile à vendre au-delà de ça. Un **rapport**, lui, est un outil de décision : il s'évalue comme une fraction d'un enjeu à fort levier (allouer un budget, recruter), pas comme une fraction de salaire horaire. Son exemple : un même pipeline RAG « en boucle » qui produit une réponse vaut quelques heures de salaire, mais le **rapport** qui en découle peut se facturer 20 000 $ s'il éclaire l'allocation d'un budget de 5 M$. Il insiste sur le rôle des **SOPs** (standard operating procedures) : la *forme* du rapport — template structuré, livrables clairs, objectif, critères de décision, follow-ups — est ce qui crée la valeur, davantage qu'un transcript brut. Il anticipe l'émergence d'un **marché de templates de rapports** et le fait que savoir définir le bon template deviendra une compétence en soi.

## Ce que ça ajoute vs IBM
IBM présente le RAG agentique surtout comme un mécanisme de récupération-raisonnement. Liu déplace la question vers la **valeur produit** : à quoi sert la sortie de l'agent ? Sa thèse — concevoir l'agent pour produire un livrable structuré orienté décision (rapport/SOP) plutôt qu'une réponse ponctuelle — est une perspective stratégique absente du corpus IBM.

## Points clés
- « RAG is the feature, not the benefit » : le Q&A est unidimensionnel (temps gagné).
- Un rapport s'évalue comme % d'un outcome à fort levier, pas comme % de salaire.
- La valeur vient de la *forme* (SOP/template structuré), pas du transcript brut.
- Prédiction : marketplaces de templates ; définir le bon template = compétence clé.

## Voir aussi
- (jxnl) [Améliorer son RAG systématiquement](ameliorer-rag-systematiquement.md)
- (agents IBM) [RAG agentique](rag-agentique.md)
- (Hamel) [Error analysis](error-analysis.md)
- [post complet](../sources/jason-liu/md/predictions-future-rag.md)
