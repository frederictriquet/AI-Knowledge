# MRKL Systems

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. [Glossaire](../../GLOSSAIRE-PATTERNS.md) · Pertinence 🟡 tradeoff (valeur de filiation)

**En une phrase** — architecture de **routage** où un LLM aiguille chaque requête vers un ensemble de modules experts (symboliques : calculatrice, base de données, API ; ou neuronaux).

## L'idée
MRKL (*Modular Reasoning, Knowledge and Language*, prononcé « miracle ») pose le LLM comme **routeur/contrôleur** devant des modules spécialisés, au lieu de tout faire en interne. Le modèle décide *quel module* invoquer et *avec quels arguments*, puis intègre la réponse. C'est l'ancêtre conceptuel direct des agents tool-using.

## Comment s'exprime le routage
Point souvent mal compris : dans MRKL, **le routeur est neuronal, pas des règles câblées** — déléguer la décision à un modèle (le `MR` = *Modular Reasoning*) est précisément ce qui distingue le pattern d'un `if/else` symbolique. Le papier reste agnostique sur le mécanisme exact, qui peut être (1) du **prompting** : décrire chaque module (nom + description) dans le contexte, le LLM émet le choix — l'expression dominante aujourd'hui, c'est ce que sont devenus ReAct et le [function calling](../tool-calling.md) ; ou (2) une **décision apprise** : un classifieur / fine-tuning qui sait router (leur exemple : détecter l'arithmétique → calculatrice dans Jurassic-X). À l'inverse, **du routage par règles déterministes** (scores, `if/else` dans une skill) relève du pattern [logique conditionnelle / heuristique](../logique-conditionnelle-heuristique.md) — c'est l'anti-MRKL. Les *modules cibles*, eux, peuvent être symboliques (calculatrice, DB, API) — d'où le « neuro-symbolique » — mais la **décision de routage** reste neuronale.

## Tradeoff / quand l'utiliser
Surtout une **référence de filiation** : ReAct, le function calling et les « agents de routage » du RAG agentique en sont des descendants. Connaître MRKL aide à voir que « router vers des outils » est un pattern formalisé dès 2022, pas une nouveauté.

## Source primaire
Karpas et al., 2022, *MRKL Systems: A modular, neuro-symbolic architecture…*, arXiv:2205.00445 (AI21 Labs). *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [sous-types-rag-agentique](../sous-types-rag-agentique.md) (corpus — agent de routage)
- [tool-calling](../tool-calling.md) (corpus)
