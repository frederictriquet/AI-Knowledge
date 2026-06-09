---
titre: "LLM-as-a-judge"
theme: evaluation
niveau: 🟡
provenance: ✅
base: ibm-guide-agents-ia
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-evaluation
source_titre: "Qu’est-ce que l’évaluation des agents IA ?"
---

# LLM-as-a-judge

> Fiche du glossaire des patterns · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [60-ai-agent-evaluation](../sources/ibm-guide-agents-ia/md/60-ai-agent-evaluation.md), [61-ai-agent-evaluation](../sources/ibm-guide-agents-ia/md/61-ai-agent-evaluation.md)

**En une phrase** — utiliser un LLM, guidé par une rubrique de critères, pour noter automatiquement les sorties d'un agent quand il n'existe pas de vérité terrain à comparer.

## Ce que dit le corpus
Le fichier 60 définit le LLM-as-a-judge comme « un système d'évaluation automatisé qui évalue la performance des agents IA à l'aide de critères et d'indicateurs prédéfinis. Au lieu de s'appuyer uniquement sur des examinateurs humains, un LLM en tant que juge applique des algorithmes, des heuristiques ou des modèles de notation basés sur l'IA pour évaluer les réponses, les décisions ou les actions d'un agent IA ». Il est mobilisé quand il n'y a pas de critères de réussite prédéfinis, et pour l'évaluation sémantique du tool-calling. Le fichier 61 en donne une mise en œuvre : un agent de voyage est noté sur trois critères (exactitude, utilité, cohérence) via un `evaluation_prompt` structuré demandant un score `/5` motivé. Concrètement, le tutoriel construit `eval_input = evaluation_prompt.format(...)` puis appelle `agent.invoke(eval_input)`.

## Tradeoff / insight pour un senior
À calibrer : la littérature documente des biais (auto-préférence, sensibilité à la position/à l'ordre, à la verbosité) que le corpus ne détaille pas mais qui rendent la note non neutre. Surtout, le tuto 61 est méthodologiquement discutable : il réutilise *le même* `agent` outillé comme juge (`agent.invoke(eval_input)`) au lieu d'un évaluateur distinct — un agent qui se note lui-même cumule auto-préférence et fuite de contexte. En production, séparer le modèle-juge du modèle évalué et fixer une rubrique versionnée.

## Source primaire
Non citée par IBM — concept présenté sans référence académique (pattern « LLM-as-a-judge » de l'état de l'art, hors-corpus).

## Voir aussi
- [taxonomie-erreurs-appel-fonction](taxonomie-erreurs-appel-fonction.md)
- [evaluation-trajectoire](evaluation-trajectoire.md)
