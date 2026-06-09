---
titre: "BeeAI"
theme: frameworks-outillage
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/beeai
source_titre: "Qu’est-ce que BeeAI ?"
---

# BeeAI

**En une phrase** — une couche d'orchestration framework-agnostique d'IBM, fondée sur le protocole ACP, qui découvre, exécute et partage des agents quels que soient leurs cadres, en isolant chaque agent dans son conteneur.

## En détail
BeeAI est une plateforme open source pour découvrir, exécuter et partager des agents d'IA de manière centralisée, sur tous les cadres. Développée par IBM Research et hébergée par la Linux Foundation, elle repose sur le protocole ACP (Agent Communication Protocol). Elle répond à trois défis : écosystèmes cloisonnés, évolutivité limitée, découverte fragmentée — via un catalogue d'agents consultable et un centre de découverte centralisé. BeeAI utilise l'ACP pour normaliser l'usage des agents indépendamment du cadre ; on peut importer des agents locaux ou depuis GitHub, LangChain, etc. Chaque agent s'exécute dans son propre conteneur avec des limites de ressources définies. Les composants clés : agents conteneurisés communiquant par ACP, un serveur BeeAI (orchestration, cycles de vie, routage, télémétrie), une CLI et une UI, une intégration Python via le SDK ACP. L'observabilité est intégrée : collecte de télémétrie avec OpenTelemetry, envoyée à une instance Arize Phoenix. BeeAI privilégie une expérience locale donnant à l'utilisateur le contrôle total de ses données.

## Tradeoff / insight pour un senior
Le différenciateur réel est l'isolation par conteneur (limites de ressources, packaging d'agents hétérogènes contournant les incompatibilités) couplée à une télémétrie OTEL/Phoenix prête à l'emploi. BeeAI n'est pas un framework de plus mais une couche au-dessus des frameworks : la valeur est l'interopérabilité, au prix d'une dépendance à la maturité d'ACP/A2A.

## Source primaire
beeai.dev et la documentation ACP. Voir aussi le dépôt GitHub i-am-bee.

## Voir aussi
- [acp](acp.md)
- [a2a](a2a.md)
