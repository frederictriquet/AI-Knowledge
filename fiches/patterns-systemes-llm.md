---
titre: "Patterns pour systèmes LLM en production"
theme: evaluation
niveau: 🔴
source_url: https://eugeneyan.com/writing/llm-patterns/
source_titre: "Patterns for Building LLM-based Systems & Products"---

# Patterns pour systèmes LLM en production

> Fiche **source : Eugene Yan** · [post](../sources/eugene-yan/md/llm-patterns.md) · Pertinence 🔴 substance

**En une phrase** — Sept patterns pratiques pour transformer une démo LLM en produit fiable, organisés selon deux axes : améliorer la performance vs réduire coût/risque, et proche de la donnée vs proche de l'utilisateur.

## Ce que dit la source
Eugene distille recherche académique, ressources industrielles et savoir-faire de praticiens en sept patterns clés : **Evals** (mesurer la performance et détecter les régressions, sinon « on vole à l'aveugle »), **RAG** (ajouter du savoir externe récent, réduire les hallucinations en ancrant le modèle), **Fine-tuning** (spécialiser sur une tâche), **Caching** (réduire latence et coût en mettant en cache les réponses, mais « caching safely » plutôt que la seule similarité sémantique), **Guardrails** (valider la sortie : schéma JSON, factualité, contenu nuisible, entrées adverses), **Defensive UX** (anticiper et gérer les erreurs côté interface) et **Collecte de feedback** (construire le data flywheel — explicite ou implicite). Il cite un commentaire HackerNews : l'importance accordée aux evals distingue ceux qui « rushent du hot garbage » de ceux qui construisent sérieusement.

## Ce que ça ajoute vs IBM
IBM décrit des patterns d'agents de façon conceptuelle ; Eugene fournit la **vue système/produit de bout en bout** avec le détail d'ingénierie : métriques concrètes (BLEU, ROUGE, BERTScore et leurs limites), le caching comme levier coût/latence souvent ignoré, et surtout l'insistance que sans evals représentatives on ne peut pas mesurer un changement à l'échelle. C'est l'angle production que la doc IBM survole.

## Points clés
- 7 patterns sur un plan 2×2 : data ↔ user, défensif ↔ offensif.
- Evals = fondation : mesurer chaque composant (LLM, prompt, contexte, température).
- RAG : moins cher de maintenir un index à jour que de re-pré-entraîner.
- Caching sémantique = « disaster waiting to happen » s'il est naïf.
- Le feedback utilisateur alimente evals, fine-tuning ET guardrails.

## Voir aussi
- (Anthropic) [Patterns de workflow](patterns-de-workflow.md)
- (agents IBM) [RAG agentique](rag-agentique.md)
- (Hamel) [Eval-driven development](eval-driven-development.md)
- [post complet](../sources/eugene-yan/md/llm-patterns.md)
