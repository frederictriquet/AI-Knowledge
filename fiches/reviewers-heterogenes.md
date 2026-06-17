---
titre: "Reviewers hétérogènes : faible recouvrement entre outils"
theme: evaluation
niveau: 🟡
source_url: https://addyosmani.com/blog/agentic-code-review/
source_titre: "Agentic Code Review — Addy Osmani"
---

# Reviewers hétérogènes : faible recouvrement entre outils

**En une phrase** — Les reviewers de code IA se recoupent très peu : il ne faut pas chercher « le meilleur » outil mais en faire tourner plusieurs aux forces complémentaires, comme un ensemble.

## Ce que dit la source
Osmani cite une étude comparative parallèle de quatre reviewers IA : sur 617 emplacements signalés, **93,4 % n'étaient détectés que par un seul des quatre outils**, et *aucun* par les quatre ; seuls ~6,6 % des findings étaient repérés par deux outils ou plus. Autrement dit, chaque outil a une « signature » de détection distincte (l'un fort sur l'architecture, l'autre sur la sévérité des défaillances de prod, etc.), et choisir un seul « meilleur » outil revient à accepter un large angle mort. La recommandation : **faire tourner deux reviewers ou plus** de natures différentes pour capter des bugs complémentaires — au prix d'un bruit accru à trier (précision vs recall) et d'un coût en tokens. C'est la transposition, à la revue de code, de l'idée d'**ensembling** : des évaluateurs diversifiés couvrent plus de modes d'échec que la redondance d'un même évaluateur.

## Pourquoi c'est utile
Le chiffre (93,4 % de findings « solo ») contredit l'intuition du « shoot-out pour élire le meilleur outil » et justifie quantitativement une stratégie multi-reviewers ; il rejoint les patterns d'ensembling et de vérification par perspectives diverses.

## À retenir
- Ne pas benchmarker pour *élire* un outil ; benchmarker pour *combiner* des outils complémentaires.
- Privilégier la **diversité** des reviewers (architecture, sécurité, sévérité prod) à la redondance.
- Accepter le compromis : plus de recall = plus de bruit → un humain trie, l'IA ne décide pas.
- Surveiller le coût : N reviewers sur chaque PR = N× les tokens.

## Voir aussi
- [Revue de code agentique : de l'écriture à la vérification](revue-de-code-agentique.md)
- [Techniques d'ensembling](ensembling-techniques.md)
- [LLM-evaluators (juges LLM)](llm-evaluators.md)
