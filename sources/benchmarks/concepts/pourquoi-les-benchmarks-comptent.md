# Pourquoi les benchmarks d'agents comptent 🔴

## En une phrase

Les benchmarks publics d'agents (SWE-bench, τ-bench, GAIA, WebArena) sont le rappel chiffré et reproductible que, sur des tâches **réelles, longues et outillées**, les agents de pointe échouent encore largement — et ils définissent *où* regarder pour progresser.

## Ce que disent les sources

- **SWE-bench** — sur de vrais bugs GitHub, le meilleur modèle de l'époque (Claude 2) ne résout que **1,96 %** des issues. Résoudre un bug réel exige de coordonner des changements multi-fichiers, d'exécuter du code et de digérer de longs contextes.
- **τ-bench** — face à un utilisateur simulé et à des règles métier, même gpt-4o réussit **moins de 50 %** des tâches et reste très **incohérent** (pass^8 < 25 % en retail). La fiabilité, pas seulement la réussite ponctuelle, est mesurée via **pass^k**.
- **GAIA** — sur des questions « simples pour un humain », l'écart est brutal : **92 % (humains) vs 15 % (GPT-4 + plugins)**.
- **WebArena** — sur des tâches web long-horizon, le meilleur agent GPT-4 plafonne à **14,41 %** contre **78,24 %** pour l'humain. L'évaluation porte sur la **correction fonctionnelle**, pas sur la ressemblance de surface.

## Ce que ça ajoute vs IBM

Le guide IBM cadre *comment* évaluer un agent (trajectoire, étapes, outils). Ces benchmarks apportent le **point de référence externe** qui manque souvent en interne :

- des **scores absolus** comparables d'un papier à l'autre, qui désamorcent l'optimisme (« notre agent marche ») ;
- des **protocoles d'évaluation par l'état final** (τ-bench compare l'état de la base de données, WebArena la correction fonctionnelle) plutôt que par le texte produit — directement transposable à une éval métier ;
- une métrique de **fiabilité** (pass^k) qui formalise l'idée qu'un agent qui réussit *parfois* n'est pas déployable ;
- une **borne humaine** (GAIA, WebArena) pour situer l'agent sans se mentir.

## Points clés

- Mesurer sur des tâches **réalistes et long-horizon**, pas sur des micro-tâches synthétiques.
- Évaluer l'**état final / la correction fonctionnelle**, pas la similarité de surface.
- Mesurer la **cohérence sur plusieurs essais** (pass^k), pas seulement le succès au premier coup.
- Garder une **borne humaine** comme référence honnête.
- Les chiffres datent : ils valent comme **méthode** et comme rappel d'humilité, pas comme classement figé.

## Voir aussi

- (agents IBM) [Évaluation de trajectoire](../../../ibm-guide-agents-ia/concepts/evaluation-trajectoire.md) · (agents IBM hors-corpus) [Computer-use & agents GUI](../../../ibm-guide-agents-ia/concepts/hors-corpus/computer-use-gui-agents.md) · (Hamel) [Error analysis](../../hamel-husain/concepts/error-analysis.md)
