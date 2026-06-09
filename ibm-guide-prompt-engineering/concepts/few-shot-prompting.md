# Few-shot prompting

> Fiche du [glossaire prompting](../GLOSSAIRE-PROMPTING.md) · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [../md/10-few-shot-prompting.md](../md/10-few-shot-prompting.md)

**En une phrase** — fournir quelques exemples étiquetés dans le prompt pour guider le modèle, en exploitant ses connaissances pré-entraînées sans réentraînement.

## Ce que dit le corpus
Le few-shot présente plusieurs exemples de la tâche dans le prompt (illustration IBM : classification de sentiments « positif / négatif »). Le corpus décrit un pipeline notable : les exemples sont stockés dans une base de données vectorielle, et lors d'une requête le système fait une correspondance sémantique pour récupérer les exemples les plus pertinents — c'est de la RAG appliquée à la sélection d'exemples, non systématiquement requise mais bénéfique. Le corpus cite plusieurs cadres de recherche : SetFit (Tunstall et al., réglage fin efficace de sentence-transformers), UPT / Unified Prompt Tuning (Feihu Jin et al.), TransPrompt (prompting transférable inter-tâches), ainsi que QaNER pour la NER. Il note aussi qu'un « prompt vide » (sans exemple ni template) peut atteindre une précision compétitive. Limites : dépendance à la qualité des prompts, complexité de calcul, généralisation difficile, capacités zero-shot limitées.

## Tradeoff / insight pour un senior
L'insight pratique : la sélection des exemples compte autant que leur nombre. Coupler le few-shot à une recherche vectorielle (RAG sur la banque d'exemples) adapte dynamiquement les démonstrations à chaque requête, ce qui surpasse un jeu d'exemples figé. Revers : on dépense du budget contexte et on ajoute une infra de récupération — à arbitrer contre un simple instruction tuning.

## Source primaire
Cadres cités par IBM : SetFit (Lewis Tunstall et al.), Unified Prompt Tuning / UPT (Feihu Jin et al.), TransPrompt, QaNER ; sans DOI/arXiv résolus dans le texte lu.

## Voir aussi
- [in-context-learning](in-context-learning.md)
- [zero-shot-prompting](zero-shot-prompting.md)
