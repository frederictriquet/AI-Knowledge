---
titre: "Sorties structurées (instructor / Pydantic)"
theme: efficacite-cout
niveau: 🟡
source_url: https://python.useinstructor.com/
source_titre: "Instructor: Top Multi-Language Library for Structured LLM Outputs"---

# Sorties structurées (instructor / Pydantic)

> Fiche **source : Jason Liu (jxnl)** · [post](../sources/jason-liu/md/instructor-home.md) · Pertinence 🟡 tradeoff

**En une phrase** — Obtenir d'un LLM des données typées et validées (via des modèles Pydantic) plutôt que de parser du texte libre, avec validation et retries automatiques.

## Ce que dit la source
*instructor* est une librairie (Python en tête, mais aussi TypeScript, Go, Ruby, Elixir, Rust) construite sur **Pydantic** pour extraire des **sorties structurées** d'un LLM. On définit un `BaseModel` qui décrit exactement les champs voulus, on le passe en `response_model`, et la librairie garantit une sortie structurée et validée. Quatre piliers : *structured outputs* (le schéma Pydantic), *automatic retries* (re-interrogation du modèle quand la validation échoue — « reasking »), *data validation* (via les validateurs Pydantic, ex. `field_validator`, contraintes `min_length`/`gt`), et *streaming* (objets partiels et itérables). L'interface `from_provider` est unifiée : même code pour OpenAI, Anthropic, Google, Ollama, DeepSeek et 15+ fournisseurs, en sync ou async. La doc positionne *instructor* comme spécialisé dans l'extraction (« Instructor for extraction, PydanticAI for agents ») : il fait une chose — fournir des données fiables et validées — et la fait bien, avec un contrôle total sur le prompt et l'inférence de type pour l'IDE.

## Ce que ça ajoute vs IBM
IBM évoque le décodage contraint et le tool calling au niveau du modèle. *instructor* apporte la couche *applicative* côté client : schéma déclaratif Pydantic, **retries de validation** quand la sortie ne respecte pas les contraintes, et streaming partiel — une approche portable across providers, indépendante du décodage contraint natif.

## Points clés
- Schéma déclaratif Pydantic comme contrat de sortie (type safety, support IDE).
- Validation + retries automatiques (« reasking ») en cas d'échec des contraintes.
- Streaming d'objets partiels/itérables ; `create_partial`, `create_iterable`.
- `from_provider` : interface unique multi-fournisseurs (sync/async).
- Périmètre volontairement étroit : extraction structurée, pas un framework d'agents.

## Voir aussi
- (agents IBM hors-corpus) [Décodage contraint / sortie structurée](constrained-decoding.md)
- (agents IBM) [Tool calling](tool-calling.md)
- (Hamel) [LLM-as-judge (bien fait)](llm-as-judge-correct.md)
- [post complet](../sources/jason-liu/md/instructor-home.md)
