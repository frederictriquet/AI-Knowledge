# Pattern superviseur & équipes hiérarchiques

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. [Glossaire](../../GLOSSAIRE-PATTERNS.md) · Pertinence 🟡 tradeoff

**En une phrase** — un agent **superviseur** route les tâches vers des sous-agents spécialisés et agrège leurs réponses ; généralisable en équipes d'équipes.

## L'idée
Un agent central joue le rôle de routeur : il analyse la requête, choisit le sous-agent spécialisé compétent, lui délègue la tâche, puis agrège les résultats. En empilant ce schéma, le superviseur peut piloter non plus des agents isolés mais d'autres superviseurs, formant une **hiérarchie d'équipes** (teams of teams). C'est un pattern d'orchestration explicite, popularisé par LangGraph, qui rend le contrôle de flux lisible et le routage déterministe.

## Tradeoff / quand l'utiliser
Adapté quand les compétences sont **clairement partitionnables** et qu'on veut un point de contrôle central auditable. Coût : le superviseur devient un goulot et un point de défaillance unique ; la hiérarchie ajoute de la latence à chaque niveau. Pour des agents pairs sans spécialisation nette, une collaboration horizontale est préférable.

## Source primaire
LangGraph — *Multi-agent supervisor / hierarchical agent teams* (documentation officielle ; pas d'arXiv).

## Voir aussi
- [structures-multi-agents](../structures-multi-agents.md) (corpus)
- [orchestration-types](../orchestration-types.md) (corpus)
