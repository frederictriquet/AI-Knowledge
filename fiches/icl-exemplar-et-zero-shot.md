---
titre: "ICL : sélection d'exemples & techniques zero-shot"
theme: prompting
niveau: 🔴
provenance: 🔗
base: sources/prompt-report
source_url: https://arxiv.org/abs/2406.06608
source_titre: "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques"
---

# ICL : sélection d'exemples & techniques zero-shot

> Fiche **source : The Prompt Report (Schulhoff et al., 2024)** · [papier](../sources/prompt-report/md/prompt-report.md) · Pertinence 🔴 substance

**En une phrase** — En few-shot, le choix des exemples, leur ordre et leur quantité pèsent autant que le contenu du prompt ; en zero-shot, plusieurs reformulations simples de la consigne suffisent à améliorer la sortie.

## Ce que dit la source
Le rapport (§2.2.1) présente l'In-Context Learning : le modèle apprend une tâche via des exemplars et/ou instructions dans le prompt, sans mise à jour des poids. Il isole six décisions de conception du few-shot. La quantité d'exemplars aide en général (surtout sur gros modèles), avec des bénéfices parfois décroissants au-delà de 20. L'ordre des exemplars peut faire varier l'exactitude de moins de 50% à plus de 90% sur certaines tâches (Lu et al., 2021). Comptent aussi la distribution et la qualité des labels, le format, et la similarité au cas de test. Pour sélectionner les exemplars, K-Nearest Neighbor (Liu et al.) retient les plus proches du test, et Vote-K (Su et al.) propose des candidats à annoter en deux étapes tout en garantissant la diversité. Côté zero-shot, il nomme Role Prompting, Style Prompting, Emotion Prompting, System 2 Attention (S2A), SimToM, Rephrase and Respond (RaR), Re-reading (RE2) et Self-Ask.

## Ce que ça ajoute vs IBM
Là où IBM décrit few-shot et zero-shot comme principes, le rapport quantifie la sensibilité empirique (ordre, quantité, similarité) et nomme des techniques zero-shot précises (S2A, SimToM, RaR, RE2, Self-Ask) absentes du guide.

## Points clés
- Exemplar Ordering : l'ordre seul peut faire chuter ou monter l'exactitude de plus de 40 points.
- Exemplar Quantity : plus d'exemplars aide, mais bénéfices parfois décroissants au-delà de 20.
- KNN / Vote-K : sélection d'exemplars similaires au cas de test (KNN coûteux ; Vote-K ajoute la diversité).
- Role / Style / Emotion Prompting : assigner un rôle, un style, ou une phrase à charge psychologique.
- S2A, SimToM, RaR, RE2, Self-Ask : reformuler, filtrer le contexte ou auto-questionner avant de répondre.

## Voir aussi
- (IBM) [Few-shot](few-shot-prompting.md)
- (IBM) [Zero-shot](zero-shot-prompting.md)
- (IBM) [In-context learning](in-context-learning.md)
- (IBM) [Role prompting](role-prompting.md)
- [papier complet](../sources/prompt-report/md/prompt-report.md)
