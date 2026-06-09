# La taxonomie en familles de The Prompt Report

> Fiche **source : The Prompt Report (Schulhoff et al., 2024)** · [papier](../md/prompt-report.md) · Pertinence 🔴 substance

**En une phrase** — Une méta-structure qui range 58 techniques de prompting textuel en 5 grandes familles (In-Context Learning regroupant Zero-Shot et Few-Shot), pour savoir quel levier activer selon le problème.

## Ce que dit la source
Le rapport présente une « comprehensive taxonomical ontology » de 58 techniques de prompting textuel (§2.2). Une technique pouvant relever de plusieurs familles est placée dans la catégorie « of most relevance ». La taxonomie résulte d'une revue systématique PRISMA aboutissant à un corpus final de 1 565 papiers.

**Décompte exact (5 ou 6 ?).** Le texte du §2.2 annonce « 58 text-based prompting techniques, broken into 6 major categories (Figure 2.2) », et la Figure 2.2 affiche bien six boîtes de tête : Zero-Shot, Few-Shot, Thought Generation, Ensembling, Self-Criticism, Decomposition. **Mais** le découpage en sections numérotées du rapport ne compte que **5 familles** : Zero-Shot et Few-Shot y sont rassemblés sous **In-Context Learning (ICL)** (§2.2.1, avec Few-Shot en §2.2.1.2 et Zero-Shot en §2.2.1.3), les quatre autres étant Thought Generation (§2.2.2), Decomposition (§2.2.3), Ensembling (§2.2.4) et Self-Criticism (§2.2.5). Cette fiche adopte le décompte des sections : **5 familles, les techniques Zero-Shot et Few-Shot étant rangées sous l'ICL** (le « 6 » de la figure vient de la séparation Zero-Shot / Few-Shot au niveau visuel).

Les familles sont : In-Context Learning (ICL) — apprentissage par exemplars et/ou instructions sans mise à jour des poids, englobant Few-Shot et Zero-Shot ; Thought Generation — faire articuler le raisonnement (Chain-of-Thought et variantes) ; Decomposition — décomposer explicitement un problème en sous-problèmes ; Ensembling — générer plusieurs sorties et les agréger (souvent par majority vote) ; Self-Criticism — faire critiquer et réviser sa propre sortie par le modèle. Les auteurs notent aussi que le terme « learn » de l'ICL est trompeur : il peut s'agir d'une simple spécification de tâche.

## Ce que ça ajoute vs IBM
Là où le guide IBM liste des techniques au fil de l'eau, The Prompt Report fournit une carte structurée et exhaustive issue d'une revue systématique, qui situe chaque technique dans une famille de leviers et révèle des familles entières (Decomposition, Ensembling, Self-Criticism) peu couvertes par IBM.

## Techniques clés
- In-Context Learning (ICL) — Brown et al. — apprentissage par exemplars/instructions dans le prompt, sans entraînement.
- Thought Generation — Chain-of-Thought (Wei et al.) et variantes pour expliciter le raisonnement.
- Decomposition — découpage explicite en sous-problèmes (Least-to-Most, DECOMP, ToT...).
- Ensembling — agrégation de plusieurs sorties (Self-Consistency...).
- Self-Criticism — auto-vérification et révision (Self-Refine, COVE...).

## Voir aussi
- (IBM) [Catalogue des techniques](../../../ibm-guide-prompt-engineering/concepts/techniques-catalogue.md)
- (IBM) [Chain-of-Thought](../../../ibm-guide-prompt-engineering/concepts/chain-of-thought.md)
- (IBM) [Tree of Thoughts](../../../ibm-guide-prompt-engineering/concepts/tree-of-thoughts.md)
- [taxonomie complète](taxonomie-techniques.md)
- [papier complet](../md/prompt-report.md)
