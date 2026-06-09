# La « lethal trifecta » (source primaire)

> Fiche **source : Simon Willison** · [post complet](../md/lethal-trifecta.md) · Pertinence 🔴 substance

**En une phrase** — La combinaison fatale : accès à des données privées + exposition à du contenu non fiable + capacité de communication sortante (exfiltration) ; retirer une des trois pattes neutralise la classe d'attaque.

## Ce que dit la source
La **lethal trifecta** réunit trois capacités : *access to your private data*, *exposure to untrusted content* (tout texte ou image contrôlé par un attaquant pouvant atteindre le LLM) et *the ability to externally communicate* d'une manière permettant le vol de données (l'*exfiltration*). Quand un agent combine ces trois traits, un attaquant peut facilement le piéger pour lui faire envoyer des données privées. Le problème de fond : les LLM suivent les instructions présentes dans le contenu et ne distinguent pas de façon fiable l'origine des instructions — tout est aplati en une séquence de tokens. Willison rappelle que les **guardrails** ne protègent pas : un produit qui arrête « 95 % des attaques » est un échec en sécurité applicative. MCP aggrave le risque en encourageant à mélanger des outils de sources différentes. La seule parade sûre côté utilisateur : éviter entièrement cette combinaison.

## Ce que ça ajoute vs IBM
Willison est LA source primaire de référence sur la **prompt injection** : il a forgé le terme et la notion de lethal trifecta. La fiche IBM correspondante en est une version dérivée et vulgarisée.

## À retenir
- Trois pattes : private data, untrusted content, external communication.
- Casser une seule patte suffit à neutraliser la classe d'attaque.
- Les guardrails à « 95 % » ne suffisent pas en sécurité.
- MCP multiplie l'exposition en mélangeant les outils.
- Côté utilisateur : éviter la combinaison, les fournisseurs ne vous sauveront pas.

## Voir aussi
- (agents IBM, fiche dérivée) [lethal trifecta](../../../ibm-guide-agents-ia/concepts/hors-corpus/lethal-trifecta.md)
- (prompt-eng IBM) [Injection de prompt](../../../ibm-guide-prompt-engineering/concepts/prompt-injection.md)
- [dual-llm-pattern](dual-llm-pattern.md)
- [post complet](../md/lethal-trifecta.md)
