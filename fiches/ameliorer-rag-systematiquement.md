---
titre: "Améliorer son RAG systématiquement"
theme: rag-contexte
niveau: 🔴
source_url: https://jxnl.co/writing/2024/05/22/systematically-improving-your-rag/
source_titre: "Systematically Improving Your RAG"---

# Améliorer son RAG systématiquement

> Fiche **source : Jason Liu (jxnl)** · [post](ameliorer-rag-systematiquement.md) · Pertinence 🔴 substance

**En une phrase** — Traiter un système RAG comme un produit mesurable qu'on améliore par itérations guidées par des métriques, et non comme une recette figée.

## Ce que dit la source
Liu propose un *runbook* incrémental issu de son travail de consultant. Première erreur courante : se concentrer sur la *synthèse* (la génération) sans vérifier que la *récupération* fonctionne. Il faut donc commencer par générer des **questions synthétiques** pour chaque chunk, puis mesurer **precision et recall** de la récupération afin d'établir une baseline. Sur ses tests, full-text search et embeddings se valaient parfois (full-text 10× plus rapide), mais sur des issues de dépôt le recall passait de 55 % (full-text) à 65 % (embeddings) — d'où l'intérêt de combiner les deux. Il insiste sur l'**extraction de métadonnées** (dates, sources) et le *query understanding*, car certaines questions (« quels développements récents ? ») échappent à la fois au texte et au vecteur. Il recommande des **mécanismes de feedback** explicites (« A-t-on répondu correctement ? oui/non »), puis le **clustering** des requêtes par topics et capabilities pour prioriser les zones sous-performantes, et un monitoring continu avec arbitrage **latence vs recall** selon l'enjeu (diagnostic médical vs doc grand public).

## Ce que ça ajoute vs IBM
IBM décrit le RAG agentique comme une *architecture* (récupération, reranking, raisonnement). Liu apporte la vue *production* manquante : comment **mesurer** la récupération, créer une boucle de feedback, segmenter les échecs par topic et décider quoi améliorer avec des chiffres — le RAG comme système d'amélioration continue.

## Points clés
- Mesurer la récupération avant la génération : recall/precision sur questions synthétiques (baseline).
- Hybride full-text + vector ; idéalement une seule base pour éviter la désynchronisation.
- Métadonnées + query understanding pour les questions de filtrage (dates, sources).
- Feedback utilisateur ciblé (« réponse correcte ? oui/non ») pour bâtir un dataset d'éval.
- Clustering par topics/capabilities pour prioriser ; arbitrer latence vs recall selon l'enjeu.

## Voir aussi
- (agents IBM) [RAG agentique](rag-agentique.md) · [Sous-types RAG agentique](sous-types-rag-agentique.md)
- (agents IBM hors-corpus) [Reranking](reranking.md)
- (Hamel) [Error analysis](error-analysis.md) · [Eval-driven development](eval-driven-development.md)
- [post complet](ameliorer-rag-systematiquement.md)
