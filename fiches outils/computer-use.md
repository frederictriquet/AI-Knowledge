---
outil: "Computer use (Anthropic / Claude)"
type: "Capacité/outil de modèle (API Anthropic) + implémentation de référence open-source"
url: https://docs.claude.com/en/docs/agents-and-tools/tool-use/computer-use-tool
modele_economique: "Propriétaire (API Anthropic), à l'usage ; code de démo open-source"
cout_llm: "Revendu à l'usage / paiement à l'usage via l'API Anthropic — c'est le modèle Claude lui-même qui agit, donc facturation en tokens (texte ET images : chaque capture d'écran consomme ~1000–1800 tokens d'entrée)"
---

# Computer use (Anthropic / Claude)

**En une phrase** — « Computer use » n'est pas un produit autonome mais un **outil de l'API Anthropic** (`tool type` `computer_...`) qui donne à Claude la capacité de voir des captures d'écran et d'émettre des actions souris/clavier ; comme c'est Claude qui agit, tout passe en **tokens API facturés à l'usage**, captures d'écran comprises (coût potentiellement élevé).

## Type & intégration

C'est une **capacité/outil du modèle Claude**, exposée comme un outil de l'API Messages (côté `tools`), pas un logiciel local ni un serveur MCP. On l'active en déclarant un outil dont le `type` est :

- `computer_20251124` — pour Claude Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6 et Opus 4.5 ;
- `computer_20250124` — pour Claude Sonnet 4.5, Haiku 4.5 et d'anciens modèles (Opus 4.1 / Sonnet 4 / Opus 4, dépréciés).

La fonctionnalité est **en bêta** et requiert un en-tête bêta (`computer-use-2025-11-24` ou `computer-use-2025-01-24` selon le modèle). Le cycle est un **agent loop** côté client : Claude renvoie des actions (`screenshot`, clic, frappe, etc.), votre code les exécute dans un environnement (souvent un bureau virtuel), renvoie la nouvelle capture, et ainsi de suite. C'est un **outil client-side** : les captures, actions et fichiers restent chez vous ; Anthropic traite les images en temps réel pendant l'appel API mais ne les conserve pas après la réponse (éligible Zero Data Retention).

Anthropic fournit une **implémentation de référence open-source** : la démo Docker `computer-use-demo` dans le dépôt `anthropics/anthropic-quickstarts` (conteneur, implémentation des outils, agent loop, interface web). Disponible aussi via Amazon Bedrock et Google Vertex AI.

## Modèle économique

**Propriétaire** : la capacité est intégrée aux modèles Claude commerciaux et accessible uniquement via l'API Anthropic (ou Bedrock / Vertex AI), à l'usage. Seul le **code de démonstration** (computer-use-demo) est open-source ; le « cerveau » qui agit reste le modèle propriétaire payant.

## Coût LLM

Point essentiel et **contrastant avec les serveurs MCP** : ici, **ce n'est pas votre client LLM externe qui consomme — c'est Claude lui-même qui agit**, donc le coût est en **tokens de l'API Anthropic, payés à l'usage**. La tarification suit la grille standard du tool use, et s'additionne :

- **Surcoût de prompt système** : la bêta computer use ajoute ~466–499 tokens au prompt système.
- **Définition de l'outil** : ~735 tokens (modèles Claude 4.x).
- **Captures d'écran** : facturées comme des **tokens d'image** (vision) — comptez **~1000 à 1800 tokens d'entrée par capture**. Comme un agent loop génère beaucoup de captures, l'addition peut grimper vite ; le prompt caching et la limitation du nombre de captures sont recommandés.

Le tarif au token dépend du modèle choisi ; ne pas inventer de chiffres — se référer à la grille tarifaire de l'API Anthropic (https://www.anthropic.com/pricing). Conséquence : contrairement à un outil local « gratuit », **plus l'agent regarde l'écran, plus ça coûte cher**.

## À quoi ça sert

Permettre à Claude d'utiliser un ordinateur comme un humain : regarder l'écran (captures), déplacer/cliquer la souris, taper au clavier, automatiser n'importe quelle application ou interface de bureau, naviguer sur le web, remplir des formulaires, etc. Souvent combiné avec les outils `bash` et éditeur de texte pour des workflows d'automatisation plus complets. Anthropic présente des résultats état de l'art (parmi les systèmes mono-agent) sur le benchmark WebArena de navigation web autonome.

## Sécurité / précautions

Anthropic recommande explicitement de **n'exécuter computer use que dans un environnement isolé** : machine virtuelle ou conteneur dédié, à privilèges minimaux, isolé des données et actions sensibles (l'implémentation de référence tourne d'ailleurs dans un conteneur Docker).

Risque majeur : **l'injection de prompt**. Claude peut suivre des instructions trouvées dans le contenu de l'écran (pages web, texte dans des images) qui contredisent celles de l'utilisateur. Mitigations :

- Le modèle est entraîné à résister à ces injections, et une **couche de classifieurs** s'exécute automatiquement sur les prompts/captures ; si une injection potentielle est détectée dans une capture, le modèle **demande confirmation à l'utilisateur** avant l'action suivante (comportement désactivable via le support, p. ex. pour les usages sans humain dans la boucle).
- Anthropic conseille de commencer par des tâches à faible risque, et de lire le guide sur les jailbreaks/injections avant de fournir des identifiants de connexion (à passer dans des balises XML type `<robot_credentials>`).
- La capacité reste imparfaite et en bêta.

## Notes / à creuser

- **Contraste central du recensement** : les serveurs MCP de la famille « Automatisation & contrôle » — [[firefox-devtools-mcp]], [[playwright-mcp]], [[chrome-devtools-mcp]] — sont des outils **gratuits que l'agent pilote** (le coût LLM est celui de *ton* client LLM, qui décide des actions). Avec computer use, à l'inverse, **c'est le modèle Anthropic qui EST l'agent** : le coût est en **tokens API Anthropic**, captures d'écran (images) comprises, donc potentiellement bien plus élevé qu'un MCP local piloté par un LLM peu cher.
- Les captures d'écran sont redimensionnées par l'API (≤1568 px / ~1,15 Mpx pour les anciens modèles ; jusqu'à 2576 px sur Opus 4.7/4.8 avec coordonnées 1:1) — attention au mapping des coordonnées de clic.
- Modèles supportés exacts et en-têtes bêta susceptibles d'évoluer (fonctionnalité en bêta) : revérifier la doc officielle.

## Source

- Doc officielle « Computer use tool » : https://docs.claude.com/en/docs/agents-and-tools/tool-use/computer-use-tool *(vérifié le 2026-06-15)*
- Annonce « Introducing computer use » : https://www.anthropic.com/news/3-5-models-and-computer-use *(vérifié le 2026-06-15)*
- Implémentation de référence : https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo *(vérifié le 2026-06-15)*
