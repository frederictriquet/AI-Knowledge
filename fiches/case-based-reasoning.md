---
titre: "Raisonnement par cas (case-based reasoning)"
theme: raisonnement-planification
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-memory
source_titre: "Qu’est-ce que la mémoire des agents IA ?"---

# Raisonnement par cas (case-based reasoning)

> Fiche du glossaire des patterns · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [15-ai-agent-memory](../sources/ibm-guide-agents-ia/md/15-ai-agent-memory.md)

**En une phrase** — décider en réutilisant des cas passés similaires plutôt qu'en raisonnant à partir de zéro.

## Ce que dit le corpus
Le corpus mentionne le raisonnement basé sur des cas comme un usage direct de la mémoire épisodique : « Ce type de mémoire est utile pour le raisonnement basé sur des cas, où une IA apprend des événements passés afin de prendre de meilleures décisions à l'avenir. » La mémoire épisodique qui l'alimente est mise en œuvre en enregistrant les événements clés, les actions et leurs résultats dans un format structuré auquel l'agent peut accéder lorsqu'il prend des décisions. L'exemple cité est un conseiller financier alimenté par l'IA qui se souvient des choix d'investissement passés d'un utilisateur pour fournir de meilleures recommandations. Le corpus rattache aussi ce mécanisme à la robotique et aux systèmes autonomes, où l'agent doit se souvenir d'actions passées pour naviguer efficacement.

## Tradeoff / insight pour un senior
Réutiliser un cas passé est moins coûteux et plus explicable qu'un raisonnement génératif complet, mais la qualité dépend entièrement de la mesure de similarité et de la représentativité des cas stockés : un corpus de cas biaisé reproduit ses biais, et un cas « presque similaire » peut induire une décision fausse avec une fausse confiance. À cadrer comme du retrieval sur la mémoire épisodique, pas comme une généralisation.

## Source primaire
Non rattaché par IBM à une source nommée ; présenté comme application de la mémoire épisodique décrite dans CoALA (Princeton, 2024). Le case-based reasoning comme discipline est antérieur (hors-corpus).

## Voir aussi
- [Mémoire épisodique / sémantique / procédurale](memoire-episodique-semantique-procedurale.md)
