# Mémoire épisodique / sémantique / procédurale

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [15-ai-agent-memory](../md/15-ai-agent-memory.md)

**En une phrase** — trois sous-types de mémoire long terme calqués sur la psychologie : traces d'événements vécus (épisodique), faits structurés (sémantique), savoir-faire automatisé (procédural).

## Ce que dit le corpus
Les chercheurs classent la mémoire agentique comme les psychologues classent la mémoire humaine ; l'article CoALA de Princeton décrit ces types. La **mémoire épisodique** permet à l'agent de se souvenir d'expériences passées spécifiques, utile pour le raisonnement basé sur des cas ; elle est mise en œuvre en enregistrant événements, actions et résultats dans un format structuré accessible lors de la décision (ex. un conseiller financier se rappelant les choix d'investissement passés). La **mémoire sémantique** stocke des connaissances factuelles structurées — faits, définitions, règles — via bases de connaissances, IA symbolique ou embeddings vectoriels ; elle sert aux domaines experts (assistant juridique, diagnostic médical). La **mémoire procédurale** stocke compétences, règles et comportements appris permettant d'agir sans raisonner explicitement à chaque fois ; inspirée de la procédurale humaine (faire du vélo), elle s'acquiert par entraînement, souvent par apprentissage par renforcement.

## Tradeoff / insight pour un senior
Découpler ces trois mémoires évite de tout pousser dans un seul vector store : l'épisodique appelle un journal append-only horodaté, la sémantique une base de faits dédupliquée, la procédurale des politiques/skills figées. Confondre épisodique et sémantique pollue la récupération (événements ponctuels traités comme des faits généraux).

## Source primaire
« Cognitive Architectures for Language Agents » (CoALA), Université de Princeton, février 2024 — source mémoire de référence du corpus.

## Voir aussi
- [Mémoire court terme vs long terme](memoire-court-long-terme.md)
- [Raisonnement par cas (case-based reasoning)](case-based-reasoning.md)
