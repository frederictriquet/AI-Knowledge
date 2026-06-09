---
titre: "Agentic chunking"
theme: rag-contexte
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/agentic-chunking
source_titre: "Qu’est-ce que le découpage agentique ?"
---

# Agentic chunking

**En une phrase** — un LLM découpe le texte par unité de sens et étiquette chaque morceau de métadonnées, au lieu d'appliquer des coupes mécaniques à taille fixe.

## En détail
Le chunking agentique utilise l'IA pour segmenter dynamiquement de longues entrées en blocs sémantiquement cohérents, adaptés à la fenêtre contextuelle du LLM. C'est un cas d'automatisation agentique : l'agent décide seul comment diviser le texte et l'étiqueter. Le workflow type comporte quatre étapes : préparation/nettoyage du texte, fractionnement récursif, découpage où le LLM combine et enrichit chaque morceau d'un titre et d'un résumé en métadonnées, puis embedding et stockage en base vectorielle. Cette technique s'inspire des méthodes antérieures (sections superposées, découpage récursif) et reste « aux stades exploratoires ». Avantages cités : récupération efficace, réponses exactes, flexibilité sur divers types de documents, préservation du sens. En pratique, l'implémentation réduit toutefois la technique à un seul prompt (`agentic_chunking`) demandant à Granite-3.0-8B-Instruct de diviser le texte en blocs significatifs, puis un `split("\n\n")`.

## Tradeoff / insight pour un senior
L'enrichissement par métadonnées (titre + résumé par chunk) améliore la recherche RAG, mais le coût LLM par document et la variabilité des sorties (la séparation reste un `split` fragile) pèsent face à un `RecursiveCharacterTextSplitter` déterministe. La distance entre le concept et son implémentation triviale signale un domaine encore peu mûr.

## Source primaire
Le chunking sémantique, dont le chunking agentique s'inspire, est attribué à Greg Kamradt (GitHub). Le chunking agentique lui-même n'est rattaché à aucun auteur précis.

## Voir aussi
- [Stratégies de chunking](strategies-de-chunking.md)
