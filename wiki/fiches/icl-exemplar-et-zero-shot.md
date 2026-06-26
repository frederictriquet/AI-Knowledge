---
titre: "ICL : sélection d'exemples & techniques zero-shot"
type: "Concept"
theme: prompting
niveau: 🔴
source_url: https://arxiv.org/abs/2406.06608
source_titre: "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques"
---

# ICL : sélection d'exemples & techniques zero-shot

**En une phrase** — En few-shot, le choix des exemples, leur ordre et leur quantité pèsent autant que le contenu du prompt ; en zero-shot, plusieurs reformulations simples de la consigne suffisent à améliorer la sortie.

## Ce que dit la source
Le rapport (§2.2.1) présente l'In-Context Learning : le modèle apprend une tâche via des exemplars et/ou instructions dans le prompt, sans mise à jour des poids. Il isole six décisions de conception du few-shot. La quantité d'exemplars aide en général (surtout sur gros modèles), avec des bénéfices parfois décroissants au-delà de 20. L'ordre des exemplars peut faire varier l'exactitude de moins de 50% à plus de 90% sur certaines tâches (Lu et al., 2021). Comptent aussi la distribution et la qualité des labels, le format, et la similarité au cas de test. Pour sélectionner les exemplars, K-Nearest Neighbor (Liu et al.) retient les plus proches du test, et Vote-K (Su et al.) propose des candidats à annoter en deux étapes tout en garantissant la diversité. Côté zero-shot, il nomme Role Prompting, Style Prompting, Emotion Prompting, System 2 Attention (S2A), SimToM, Rephrase and Respond (RaR), Re-reading (RE2) et Self-Ask.

## Exemple
La sixième décision, Exemplar Label Quality, donne un résultat contre-intuitif : Min et al. (2022) montrent que fournir des exemplars aux labels *incorrects* ne dégrade pas forcément la performance — l'exactitude des labels semble parfois secondaire, les gros modèles encaissant même labels faux ou hors-sujet (Wei et al.). À l'inverse, la distribution biaise : 10 exemplars d'une classe contre 2 de l'autre pousse le modèle à sur-prédire la première. Côté zero-shot, S2A (Weston et Sukhbaatar) déroule en deux temps : un premier prompt réécrit la question en retirant l'information non pertinente, et seule cette version épurée est resoumise pour répondre.

## Pourquoi c'est utile
Au-delà des principes few-shot et zero-shot, ce rapport quantifie la sensibilité empirique (ordre, quantité, similarité) et nomme des techniques zero-shot précises (S2A, SimToM, RaR, RE2, Self-Ask) rarement documentées ailleurs.

## Points clés
- Exemplar Ordering : l'ordre seul peut faire chuter ou monter l'exactitude de plus de 40 points.
- Exemplar Quantity : plus d'exemplars aide, mais bénéfices parfois décroissants au-delà de 20.
- KNN / Vote-K : sélection d'exemplars similaires au cas de test (KNN coûteux ; Vote-K ajoute la diversité).
- Role / Style / Emotion Prompting : assigner un rôle, un style, ou une phrase à charge psychologique.
- S2A, SimToM, RaR, RE2, Self-Ask : reformuler, filtrer le contexte ou auto-questionner avant de répondre.

## Voir aussi
- [Few-shot](few-shot-prompting.md)
- [Zero-shot](zero-shot-prompting.md)
- [In-context learning](in-context-learning.md)
- [Role prompting](role-prompting.md)
- [papier complet](../sources/prompt-report/md/prompt-report.md)
