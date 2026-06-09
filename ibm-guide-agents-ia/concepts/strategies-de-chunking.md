# Stratégies de chunking

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [66-agentic-chunking](../md/66-agentic-chunking.md)

**En une phrase** — quatre familles de découpage, du plus mécanique (taille fixe) au plus coûteux (sémantique, agentique), à choisir selon la structure du document.

## Ce que dit le corpus
IBM recense quatre méthodes. Le **découpage à taille fixe** divise le texte en morceaux égaux selon un nombre prédéfini de caractères ou de tokens ; pour ne pas fragmenter les phrases, on ajoute souvent un chevauchement qui répète la fin d'un chunk au début du suivant. Simple et léger, mais rigide. Le **découpage récursif** s'appuie sur une liste hiérarchique de séparateurs naturels (paragraphes, phrases, mots, voire définitions de classes/fonctions en Python) ; il produit des morceaux plus cohérents et Markdown aide le chunker. L'outil cité est `RecursiveCharacterTextSplitter` de LangChain. Le **découpage sémantique** crée des embeddings par phrase et regroupe les phrases similaires, ouvrant un nouveau segment quand la sémantique change ; plus intensif en calcul. Le **découpage agentique** combine ces approches sous le pilotage d'un agent.

## Tradeoff / insight pour un senior
Le coût calcul croît avec la qualité sémantique : fixe < récursif < sémantique < agentique. Le découpage récursif est le défaut pragmatique pour du texte structuré ; le sémantique se justifie sur des documents multi-sujets où un mauvais seuil de coupure dégrade la récupération.

## Source primaire
Le chunking sémantique est attribué par IBM à Greg Kamradt (discussion sur GitHub). Les autres stratégies ne sont pas rattachées à un auteur.

## Voir aussi
- [Agentic chunking](agentic-chunking.md)
