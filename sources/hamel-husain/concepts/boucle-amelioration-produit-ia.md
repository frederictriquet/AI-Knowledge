# La boucle d'amélioration rapide d'un produit IA

> Fiche **source : Hamel Husain** · [post complet](../md/field-guide.md) · Pertinence 🟡 tradeoff

**En une phrase** — Améliorer un produit IA est une boucle itérative mesurer → analyser → corriger, dont la fondation est une eval infrastructure de confiance, et qu'on déraille en multipliant les métriques génériques et en écartant les experts métier.

## Ce que dit la source
Issu de 30+ implémentations en production, le guide identifie les patterns des équipes qui réussissent : elles « barely talk about tools at all » et obsèdent sur la mesure et l'itération. Erreurs fréquentes : le « tools first » mindset et les generic metrics, qui créent un « false sense of measurement » et fragmentent l'attention (« When everything is important, nothing is »). Les équipes performantes empower les domain experts (les prompts « are just English ») via des integrated prompt environments, et bootstrapent avec de la synthetic data même sans utilisateurs. Maintenir la confiance dans les évals est critique : Hamel recommande des binary decisions accompagnées de critiques détaillées, et de mesurer l'alignment avec le jugement humain pour contrer la « criteria drift » et la sur-confiance dans l'IA. Enfin, la roadmap doit compter des experiments, pas des features : time-boxer l'exploration, partager les échecs, et s'appuyer sur une eval infrastructure robuste (exemple GitHub Copilot).

## Ce que ça ajoute vs IBM
Hamel relie simplicité, AgentOps et mesure dans un processus humain explicite : moins de métriques mais les bonnes, experts métier au cœur de la boucle, et roadmap pilotée par l'expérimentation plutôt que par des deadlines de features.

## À retenir
- Regarder ses données d'abord (error analysis) ; les métriques émergent ensuite.
- Limiter le nombre de métriques aux quelques-unes qui comptent vraiment.
- Donner aux domain experts les outils pour écrire et itérer les prompts directement.
- Préférer binary pass/fail + critique à une échelle 1-5 arbitraire.
- Vérifier régulièrement l'alignment automated eval / humain (sampling stratégique).
- Compter les experiments menés, pas les features livrées ; time-boxer et partager les échecs.

## Voir aussi
- (Anthropic) [Trois principes : simplicité](../../anthropic-effective-agents/concepts/principes-simplicite.md)
- (agents IBM) [AgentOps](../../../ibm-guide-agents-ia/concepts/agentops.md)
- [post complet](../md/field-guide.md)
