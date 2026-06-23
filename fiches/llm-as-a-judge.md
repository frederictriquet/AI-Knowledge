---
titre: "LLM-as-a-judge"
type: "Concept"
theme: evaluation
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-evaluation
source_titre: "Qu’est-ce que l’évaluation des agents IA ?"
---

# LLM-as-a-judge

**En une phrase** — utiliser un LLM, guidé par une rubrique de critères, pour noter automatiquement les sorties d'un agent quand il n'existe pas de vérité terrain à comparer.

## En détail
Le LLM-as-a-judge est « un système d'évaluation automatisé qui évalue la performance des agents IA à l'aide de critères et d'indicateurs prédéfinis. Au lieu de s'appuyer uniquement sur des examinateurs humains, un LLM en tant que juge applique des algorithmes, des heuristiques ou des modèles de notation basés sur l'IA pour évaluer les réponses, les décisions ou les actions d'un agent IA ». Il est mobilisé quand il n'y a pas de critères de réussite prédéfinis, et pour l'évaluation sémantique du tool-calling. Une mise en œuvre concrète : un agent de voyage noté sur trois critères (exactitude, utilité, cohérence) via un `evaluation_prompt` structuré demandant un score `/5` motivé — `eval_input = evaluation_prompt.format(...)` puis `agent.invoke(eval_input)`.

## Tradeoff / insight pour un senior
À calibrer : la littérature documente des biais (auto-préférence, sensibilité à la position/à l'ordre, à la verbosité) qui rendent la note non neutre. Surtout, l'implémentation présentée est méthodologiquement discutable : elle réutilise *le même* `agent` outillé comme juge (`agent.invoke(eval_input)`) au lieu d'un évaluateur distinct — un agent qui se note lui-même cumule auto-préférence et fuite de contexte. En production, séparer le modèle-juge du modèle évalué et fixer une rubrique versionnée.

## Source primaire
Pas de référence académique formelle — pattern « LLM-as-a-judge » de l'état de l'art.

## Voir aussi
- [taxonomie-erreurs-appel-fonction](taxonomie-erreurs-appel-fonction.md)
- [evaluation-trajectoire](evaluation-trajectoire.md)
