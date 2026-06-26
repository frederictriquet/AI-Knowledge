---
titre: "Chain-of-Verification (CoVe)"
type: "Concept"
theme: raisonnement-planification
niveau: 🟡
source_url: https://arxiv.org/abs/2309.11495
---

# Chain-of-Verification (CoVe)

**En une phrase** — le modèle écrit une réponse, en dérive des questions de vérification factuelle, y répond isolément, puis corrige sa réponse à la lumière de ces vérifications.

## L'idée
CoVe structure l'auto-vérification en quatre étapes : (1) générer une réponse baseline, (2) planifier des **questions de vérification** ciblant les faits affirmés, (3) répondre à ces questions de façon indépendante — idéalement sans regarder la réponse initiale pour éviter de répéter l'erreur, (4) produire une réponse finale révisée. L'isolement des vérifications est clé : il empêche le modèle de simplement re-justifier ses hallucinations.

## Exemple
Requête « Cite des politiciens nés à New York » (Figure 1) : la réponse baseline liste Hillary Clinton, Donald Trump, Michael Bloomberg. CoVe planifie une question de vérif par entité — « Où est née Hillary Clinton ? » — répondue isolément : Chicago (Illinois), Boston (Massachusetts)... Le modèle écarte alors Clinton et Bloomberg, garde Trump et ajoute Ocasio-Cortez. Sur les listes Wikidata avec Llama 65B, la précision passe de **0,17 (few-shot) à 0,32 (CoVe factored)** ; la variante factored, qui ne re-conditionne pas sur la réponse initiale, bat la joint (0,29) car elle ne recopie pas l'hallucination.

## Tradeoff / quand l'utiliser
Réduit nettement les hallucinations factuelles, notamment sur les listes d'entités et les questions à faits multiples. Coût : plusieurs appels supplémentaires et une orchestration des sous-prompts. À utiliser quand l'exactitude factuelle prime et qu'aucune source de vérité externe (recherche, base) n'est branchée ; sinon un RAG ou un grader externe sera plus fiable. Comme Self-Refine, le signal reste interne au modèle, donc borné par ses connaissances.

## Source primaire
Dhuliawala et al., 2023, *Chain-of-Verification Reduces Hallucination in Large Language Models*, arXiv:2309.11495. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [self-refine](self-refine.md)
- [reflexion](reflexion.md)
