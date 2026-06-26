---
titre: "Améliorer son RAG systématiquement"
type: "Concept"
theme: rag-contexte
niveau: 🔴
source_url: https://jxnl.co/writing/2024/05/22/systematically-improving-your-rag/
source_titre: "Systematically Improving Your RAG"
objectifs: [mise-en-prod]
---

# Améliorer son RAG systématiquement

**En une phrase** — Traiter un système RAG comme un produit mesurable qu'on améliore par itérations guidées par des métriques, et non comme une recette figée.

## Ce que dit la source
Liu propose un *runbook* incrémental issu de son travail de consultant. Première erreur courante : se concentrer sur la *synthèse* (la génération) sans vérifier que la *récupération* fonctionne. Il faut donc commencer par générer des **questions synthétiques** pour chaque chunk, puis mesurer **precision et recall** de la récupération afin d'établir une baseline. Sur ses tests, full-text search et embeddings se valaient parfois (full-text 10× plus rapide), mais sur des issues de dépôt le recall passait de 55 % (full-text) à 65 % (embeddings) — d'où l'intérêt de combiner les deux. Il insiste sur l'**extraction de métadonnées** (dates, sources) et le *query understanding*, car certaines questions (« quels développements récents ? ») échappent à la fois au texte et au vecteur. Il recommande des **mécanismes de feedback** explicites (« A-t-on répondu correctement ? oui/non »), puis le **clustering** des requêtes par topics et capabilities pour prioriser les zones sous-performantes, et un monitoring continu avec arbitrage **latence vs recall** selon l'enjeu (diagnostic médical vs doc grand public).

## Exemple
Liu génère des questions synthétiques par chunk pour établir une baseline de récupération. Surprise concrète : sur des essais, full-text search et embeddings font jeu égal en recall (mais le full-text est 10× plus rapide) ; sur des *issues* d'un dépôt, le full-text plafonne à 55 % de recall contre 65 % pour les embeddings. La leçon : on ne *devine* pas quel retriever choisir, on le *mesure* par cas d'usage. Côté feedback, il remplace le « pouce haut / bas » ambigu par une question ciblée — « A-t-on répondu correctement ? oui/non » — pour bâtir un vrai dataset d'éval, sans variables confondantes (ton, latence).

## Pourquoi c'est utile
Liu apporte la vue *production* : comment **mesurer** la récupération, créer une boucle de feedback, segmenter les échecs par topic et décider quoi améliorer avec des chiffres — le RAG comme système d'amélioration continue.

## Points clés
- Mesurer la récupération avant la génération : recall/precision sur questions synthétiques (baseline).
- Hybride full-text + vector ; idéalement une seule base pour éviter la désynchronisation.
- Métadonnées + query understanding pour les questions de filtrage (dates, sources).
- Feedback utilisateur ciblé (« réponse correcte ? oui/non ») pour bâtir un dataset d'éval.
- Clustering par topics/capabilities pour prioriser ; arbitrer latence vs recall selon l'enjeu.

## Voir aussi
- [RAG agentique](rag-agentique.md) · [Sous-types RAG agentique](sous-types-rag-agentique.md)
- [Reranking](reranking.md)
- [Error analysis](error-analysis.md) · [Eval-driven development](eval-driven-development.md)
- [post complet](../sources/jason-liu/md/ameliorer-rag-systematiquement.md)
