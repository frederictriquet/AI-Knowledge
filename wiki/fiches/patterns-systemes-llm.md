---
titre: "Patterns pour systèmes LLM en production"
type: "Concept"
theme: evaluation
niveau: 🔴
source_url: https://eugeneyan.com/writing/llm-patterns/
source_titre: "Patterns for Building LLM-based Systems & Products"
---

# Patterns pour systèmes LLM en production

**En une phrase** — Sept patterns pratiques pour transformer une démo LLM en produit fiable, organisés selon deux axes : améliorer la performance vs réduire coût/risque, et proche de la donnée vs proche de l'utilisateur.

## Ce que dit la source
Eugene distille recherche académique, ressources industrielles et savoir-faire de praticiens en sept patterns clés : **Evals** (mesurer la performance et détecter les régressions, sinon « on vole à l'aveugle »), **RAG** (ajouter du savoir externe récent, réduire les hallucinations en ancrant le modèle), **Fine-tuning** (spécialiser sur une tâche), **Caching** (réduire latence et coût en mettant en cache les réponses, mais « caching safely » plutôt que la seule similarité sémantique), **Guardrails** (valider la sortie : schéma JSON, factualité, contenu nuisible, entrées adverses), **Defensive UX** (anticiper et gérer les erreurs côté interface) et **Collecte de feedback** (construire le data flywheel — explicite ou implicite). Il cite un commentaire HackerNews : l'importance accordée aux evals distingue ceux qui « rushent du hot garbage » de ceux qui construisent sérieusement.

## Exemple
Le cache sémantique naïf illustré par Eugene : une requête « résumé de *Mission Impossible 2* » est jugée assez proche, par similarité d'embeddings, de « *Mission Impossible 3* » — et l'on sert le mauvais résumé. La parade « caching safely » : clé sur l'item ID (ou la paire d'IDs pour une comparaison), pré-calcul offline en batch des requêtes anticipées, et choix du pattern selon la loi de puissance du trafic (un cache n'a de sens que si une minorité de requêtes concentre la majorité des hits ; sur un trafic uniformément aléatoire, le coût de maintien annule le gain).

## Pourquoi c'est utile
Eugene fournit la **vue système/produit de bout en bout** avec le détail d'ingénierie : métriques concrètes (BLEU, ROUGE, BERTScore et leurs limites), le caching comme levier coût/latence souvent ignoré, et surtout l'insistance que sans evals représentatives on ne peut pas mesurer un changement à l'échelle.

## Points clés
- 7 patterns sur un plan 2×2 : data ↔ user, défensif ↔ offensif.
- Evals = fondation : mesurer chaque composant (LLM, prompt, contexte, température).
- RAG : moins cher de maintenir un index à jour que de re-pré-entraîner.
- Caching sémantique = « disaster waiting to happen » s'il est naïf.
- Le feedback utilisateur alimente evals, fine-tuning ET guardrails.

## Voir aussi
- [Patterns de workflow](patterns-de-workflow.md)
- [RAG agentique](rag-agentique.md)
- [Eval-driven development](eval-driven-development.md)
- [post complet](../sources/eugene-yan/md/llm-patterns.md)
