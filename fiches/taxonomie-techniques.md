---
titre: "Taxonomie des techniques de prompting (The Prompt Report)"
theme: prompting
niveau: 🟡
source_url: https://arxiv.org/abs/2406.06608
source_titre: "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques"
---

# Taxonomie des techniques de prompting (The Prompt Report)

> Source : The Prompt Report — A Systematic Survey of Prompting Techniques, Schulhoff et al., 2024 ([papier complet](../sources/prompt-report/md/prompt-report.md), [arXiv](https://arxiv.org/abs/2406.06608)).
> La version **systématique et sourcée** du catalogue de techniques (~58 techniques textuelles).

Les techniques textuelles sont organisées en familles. Pour chacune : nom (forme d'origine), une ligne de description, et l'auteur/origine tel que cité.

**Décompte exact (5 ou 6 ?).** Le texte du §2.2 annonce « 58 text-based prompting techniques, broken into 6 major categories (Figure 2.2) », et la Figure 2.2 affiche bien six boîtes de tête : Zero-Shot, Few-Shot, Thought Generation, Ensembling, Self-Criticism, Decomposition. **Mais** le découpage en sections numérotées du rapport ne compte que **5 familles** : Zero-Shot et Few-Shot y sont rassemblés sous **In-Context Learning (ICL)** (§2.2.1, avec Few-Shot en §2.2.1.2 et Zero-Shot en §2.2.1.3), les quatre autres étant Thought Generation (§2.2.2), Decomposition (§2.2.3), Ensembling (§2.2.4) et Self-Criticism (§2.2.5). Cette fiche adopte le décompte des sections : **5 familles, Zero-Shot et Few-Shot rangés sous l'ICL** (le « 6 » de la figure vient de leur séparation visuelle). Une technique pouvant relever de plusieurs familles est placée dans la catégorie « of most relevance ». Les auteurs notent aussi que le terme « learn » de l'ICL est trompeur : il peut s'agir d'une simple spécification de tâche.

## In-Context Learning (ICL)

ICL : capacité des modèles génératifs à apprendre une tâche à partir d'exemplaires et/ou d'instructions placés dans le prompt, sans mise à jour des poids (Brown et al., 2020 ; Radford et al., 2019).

### Few-Shot — sélection et génération d'exemplaires
- **K-Nearest Neighbor (KNN)** — sélectionne des exemplaires proches de l'échantillon de test pour booster la performance ; efficace mais coûteux en temps/ressources (Liu et al., 2021).
- **Vote-K** — sélection d'exemplaires similaires en deux étapes : un modèle propose des candidats non étiquetés à annoter, puis le pool étiqueté sert au few-shot ; garantit aussi la diversité (Su et al., 2022).
- **Self-Generated In-Context Learning (SG-ICL)** — utilise un modèle génératif pour générer automatiquement les exemplaires quand les données d'entraînement manquent (Kim et al., 2022).
- **Prompt Mining** — découvre les « middle words » optimaux d'un prompt via l'analyse d'un large corpus, au lieu du format « Q: A: » habituel (Jiang et al., 2020).

### Zero-Shot
- **Role Prompting** — assigne un rôle ou une persona spécifique au modèle (ex. « travel writer ») ; aussi appelé persona prompting (Wang et al., 2023 ; Zheng et al., 2023).
- **Style Prompting** — spécifie le style, le ton ou le genre souhaité dans le prompt pour façonner la sortie (Lu et al., 2023).
- **Emotion Prompting** — intègre des formulations à charge psychologique humaine (ex. « This is important to my career ») pour améliorer la performance (Li et al., 2023).
- **System 2 Attention (S2A)** — demande d'abord au modèle de réécrire le prompt en retirant l'information non pertinente, puis soumet ce nouveau prompt pour obtenir la réponse (Weston et Sukhbaatar, 2023).
- **SimToM** — pour les questions impliquant plusieurs personnes/objets : établit l'ensemble des faits connus d'une personne, puis répond uniquement sur cette base (processus à deux prompts) (Wilf et al., 2023).
- **Rephrase and Respond (RaR)** — demande au modèle de reformuler et étendre la question avant de générer la réponse finale (Deng et al., 2023).
- **Re-reading (RE2)** — ajoute la phrase « Read the question again: » et répète la question ; améliore le raisonnement sur les questions complexes (Xu et al., 2023).
- **Self-Ask** — fait décider au modèle s'il doit poser des questions de suivi ; si oui, il les génère, y répond, puis répond à la question d'origine (Press et al., 2022).

## Thought Generation (CoT et variantes)

Ensemble de techniques poussant le modèle à expliciter son raisonnement pendant la résolution (Zhang et al., 2023).

- **Chain-of-Thought (CoT) Prompting** — exploite le few-shot pour faire exprimer au modèle son processus de raisonnement avant la réponse finale ; améliore nettement maths et raisonnement (Wei et al., 2022).

### Zero-Shot CoT
- **Zero-Shot-CoT** — ajoute une phrase inductrice de pensée comme « Let's think step by step. », sans exemplaire (Kojima et al., 2022).
- **Step-Back Prompting** — variante de CoT où le modèle répond d'abord à une question générique de haut niveau sur les concepts pertinents avant de raisonner (Zheng et al., 2023).
- **Analogical Prompting** — proche de SG-ICL : génère automatiquement des exemplaires incluant des CoT ; améliore raisonnement mathématique et génération de code (Yasunaga et al., 2023).
- **Thread-of-Thought (ThoT) Prompting** — inducteur de pensée amélioré : « Walk me through this context in manageable parts step by step, summarizing and analyzing as we go. » ; efficace sur les contextes longs et complexes (Zhou et al., 2023).
- **Tabular Chain-of-Thought (Tab-CoT)** — prompt Zero-Shot CoT qui fait sortir le raisonnement sous forme de table markdown, structurant ainsi le raisonnement (Jin et Lu, 2023).

### Few-Shot CoT
- **Contrastive CoT Prompting** — ajoute des exemplaires avec explications correctes ET incorrectes pour montrer au modèle comment ne pas raisonner (Chia et al., 2023).
- **Uncertainty-Routed CoT Prompting** — échantillonne plusieurs chemins de raisonnement CoT, retient la majorité si elle dépasse un seuil, sinon échantillonne en greedy (Google, 2023).
- **Complexity-based Prompting** — sélectionne des exemples complexes (longueur, nb d'étapes) et fait un vote majoritaire parmi les chaînes dépassant un seuil de longueur (Fu et al., 2023).
- **Active Prompting** — fait résoudre des exemplaires par le modèle, calcule l'incertitude (désaccord), puis fait réécrire par des annotateurs humains les exemplaires les plus incertains (Diao et al., 2023).
- **Memory-of-Thought Prompting** — construit des prompts Few-Shot CoT au moment du test à partir d'exemplaires non étiquetés traités au préalable par CoT (Li et Qiu, 2023).
- **Automatic Chain-of-Thought (Auto-CoT) Prompting** — utilise le prompt Zero-Shot de Wei et al. (2022) pour générer automatiquement les chaînes de pensée d'un prompt Few-Shot CoT (Zhang et al., 2022).

## Decomposition

Décomposition de problèmes complexes en sous-questions plus simples (Patel et al., 2022).

- **Least-to-Most Prompting** — fait d'abord décomposer le problème en sous-problèmes sans les résoudre, puis les résout séquentiellement en accumulant les réponses (Zhou et al., 2022).
- **Decomposed Prompting (DECOMP)** — few-shot montrant au modèle comment appeler des fonctions (découpe de chaîne, recherche internet…) ; le modèle découpe son problème et délègue aux fonctions (Khot et al., 2022).
- **Plan-and-Solve Prompting** — prompt Zero-Shot CoT amélioré : « Let's first understand the problem and devise a plan… Then, let's carry out the plan and solve the problem step by step » (Wang et al., 2023).
- **Tree-of-Thought (ToT)** — crée un problème de recherche arborescent en générant plusieurs étapes-pensées, évaluant leur progression et décidant lesquelles poursuivre ; efficace pour recherche et planification (Yao et al., 2023 ; aussi Long, 2023).
- **Recursion-of-Thought** — comme CoT, mais chaque sous-problème complexe rencontré est envoyé dans un autre appel/prompt dont la réponse est réinsérée ; gère les problèmes dépassant la longueur de contexte (Lee et Kim, 2023).
- **Program-of-Thoughts** — utilise des modèles type Codex pour générer du code comme étapes de raisonnement, exécuté par un interpréteur ; excelle en maths et programmation (Chen et al., 2023).
- **Faithful Chain-of-Thought** — génère un CoT mêlant langage naturel et langage symbolique (ex. Python), avec différents langages symboliques selon la tâche (Lyu et al., 2023).
- **Skeleton-of-Thought** — accélère la réponse par parallélisation : fait créer un squelette de réponse (sous-problèmes) résolus en parallèle puis concaténés (Ning et al., 2023).
- **Metacognitive Prompting** — chaîne de prompts en cinq parties imitant la métacognition humaine : clarification, jugement préliminaire, évaluation, confirmation de décision, évaluation de confiance (Wang et Zhao, 2024).

## Ensembling

Utilisation de plusieurs prompts pour le même problème, dont les réponses sont agrégées (souvent par vote majoritaire) ; réduit la variance mais multiplie les appels modèle.

- **Demonstration Ensembling (DENSE)** — crée plusieurs prompts few-shot, chacun avec un sous-ensemble distinct d'exemplaires, puis agrège leurs sorties (Khalifa et al., 2023).
- **Mixture of Reasoning Experts (MoRE)** — crée des « experts » de raisonnement via des prompts spécialisés (retrieval pour le factuel, CoT pour le multi-hop/maths, generated knowledge pour le commonsense) ; sélectionne la meilleure réponse par score d'accord (Si et al., 2023).
- **Max Mutual Information Method** — crée plusieurs templates de prompt (styles et exemplaires variés) et retient celui maximisant l'information mutuelle entre prompt et sorties (Sorensen et al., 2022).
- **Self-Consistency** — échantillonne plusieurs chemins de raisonnement CoT (température non nulle) puis fait un vote majoritaire sur les réponses (Wang et al., 2022).
- **Universal Self-Consistency** — comme Self-Consistency mais sélectionne la réponse majoritaire en insérant toutes les sorties dans un prompt ; utile pour le texte libre (Chen et al., 2023).
- **Meta-Reasoning over Multiple CoTs** — génère plusieurs chaînes de raisonnement puis les insère dans un seul prompt pour produire la réponse finale (Yoran et al., 2023).
- **DiVeRSe** — crée plusieurs prompts, applique Self-Consistency à chacun, score les chemins de raisonnement étape par étape puis sélectionne la réponse finale (Li et al., 2023).
- **Consistency-based Self-adaptive Prompting (COSP)** — construit des prompts Few-Shot CoT en exécutant Zero-Shot CoT + Self-Consistency, en retenant un sous-ensemble à fort accord comme exemplaires (Wan et al., 2023).
- **Universal Self-Adaptive Prompting (USP)** — généralise COSP à toutes les tâches via des données non étiquetées et une fonction de score plus complexe, sans Self-Consistency (Wan et al., 2023).
- **Prompt Paraphrasing** — transforme un prompt en modifiant le vocabulaire tout en conservant le sens ; technique d'augmentation de données pour générer un ensemble (Jiang et al., 2020).

## Self-Criticism

Faire critiquer au modèle ses propres sorties, soit par jugement, soit par feedback réinjecté pour améliorer la réponse (Huang et al., 2022).

- **Self-Calibration** — après une première réponse, construit un nouveau prompt incluant question, réponse et instruction demandant si la réponse est correcte ; utile pour jauger la confiance (Kadavath et al., 2022).
- **Self-Refine** — cadre itératif : le modèle donne une réponse, produit un feedback dessus, puis l'améliore, jusqu'à une condition d'arrêt (Madaan et al., 2023).
- **Reversing Chain-of-Thought (RCoT)** — fait reconstruire le problème à partir de la réponse générée, compare finement à l'original pour détecter les incohérences, converties en feedback de révision (Xue et al., 2023).
- **Self-Verification** — génère plusieurs solutions candidates par CoT, puis score chacune en masquant des parties de la question et en demandant au modèle de les prédire (Weng et al., 2022).
- **Chain-of-Verification (COVE)** — génère une réponse, crée une liste de questions de vérification, y répond, puis produit la réponse finale révisée à partir de tout cela (Dhuliawala et al., 2023).
- **Cumulative Reasoning** — génère plusieurs étapes potentielles, les fait accepter/rejeter par le modèle, vérifie si la réponse finale est atteinte, sinon répète (Zhang et al., 2023).

## À retenir (pour un ingénieur)

- Cette taxonomie est **systématique et sourcée** (revue PRISMA, 58 techniques, chaque technique attribuée à son papier d'origine), là où un catalogue ad hoc liste quelques recettes sans généalogie ni provenance.
- Elle distingue clairement des **familles souvent absentes des catalogues de base** : l'**Ensembling** (Self-Consistency, DiVeRSe, COSP/USP, MoRE…) qui agrège plusieurs réponses pour réduire la variance, et le **Self-Criticism** (Self-Refine, Chain-of-Verification, Self-Verification, RCoT…) où le modèle révise ses propres sorties.
- La **Decomposition** va bien au-delà du seul Tree-of-Thought : Least-to-Most, DECOMP, Plan-and-Solve, Program-of-Thoughts, Skeleton-of-Thought, Recursion-of-Thought, etc. — autant de stratégies explicites de découpe absentes d'un catalogue basique.
- Beaucoup de techniques sont **composables** : Self-Consistency s'applique au-dessus de CoT, COSP combine Zero-Shot CoT + Self-Consistency, DiVeRSe empile prompts multiples + Self-Consistency + scoring.
- Plusieurs techniques sont de simples **inducteurs textuels** (Zero-Shot-CoT, ThoT, RE2, RaR, Plan-and-Solve) : coût quasi nul, à essayer en premier avant les approches multi-appels coûteuses (Ensembling, ToT).

## Voir aussi
- [Catalogue des techniques](techniques-catalogue.md)
- [papier complet](../sources/prompt-report/md/prompt-report.md)
