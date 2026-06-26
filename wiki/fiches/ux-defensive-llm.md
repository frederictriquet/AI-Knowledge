---
titre: "UX défensive (Defensive UX) pour produits LLM"
type: "Concept"
theme: gouvernance-alignement-ops
niveau: 🔴
source_url: https://eugeneyan.com/writing/llm-patterns/
source_titre: "Patterns for Building LLM-based Systems & Products (Defensive UX)"
---

# UX défensive (Defensive UX) pour produits LLM

**En une phrase** — un LLM se trompe, hallucine et répond lentement *par construction* ; l'UX défensive conçoit l'interface en partant de cette faillibilité plutôt qu'en la niant — guider l'entrée, gérer l'erreur avec grâce, et garder l'humain aux commandes de la sortie.

## Ce que dit la source
C'est l'un des 7 patterns de production d'Eugene Yan : « anticiper et gérer les erreurs côté interface ». L'idée centrale : la qualité perçue d'un produit LLM dépend autant de l'**enrobage UX** que du modèle. Trois familles de leviers :

- **Côté entrée — réduire la surface d'échec** : suggestions/exemples de prompts, autocomplétion, contraintes de saisie, templates. On guide l'utilisateur vers les requêtes que le système traite bien.
- **Côté latence — gérer le temps perçu** : *streaming* token-par-token (réduit le *time-to-first-token* ressenti), indicateurs de progression, réponses optimistes. Un LLM qui « tape » paraît plus rapide qu'un spinner figé à durée égale.
- **Côté sortie — garder l'humain juge** : présenter plusieurs candidats, permettre d'éditer avant d'envoyer, citer les sources ([vérification de source](verification-de-source.md)), afficher un niveau de confiance, faciliter le *undo* et le signalement. Ne jamais faire passer une sortie non vérifiée pour une vérité.

## Tradeoff / insight pour un senior
- **L'UX est un guardrail aussi puissant que le prompt.** Beaucoup d'« échecs modèle » sont en réalité des échecs d'interface : l'utilisateur a posé une question hors périmètre faute d'être guidé, ou a pris une hallucination pour un fait faute de friction. Corriger l'UX est souvent moins cher et plus fiable que de re-prompter ou fine-tuner.
- **Friction calibrée.** Trop de confirmations tue l'usage ; zéro friction transforme chaque hallucination en action. Le bon niveau dépend du **coût de l'erreur** (suggérer un texte ≠ exécuter une transaction). C'est la jonction avec le [human-in-the-loop](hitl-statique-dynamique.md).
- **Le streaming est un couteau à double tranchant** : il améliore la latence perçue mais expose la réponse *avant* tout post-filtrage (guardrails de sortie, modération). Streamer ET filtrer demande de l'ingénierie (buffering, redaction à la volée).
- **Honnêteté > magie.** Annoncer les limites (« je peux me tromper, vérifiez ») construit plus de confiance durable qu'une UX qui surjoue l'omniscience et trahit au premier faux pas.

## Source primaire
Eugene Yan, *Patterns for Building LLM-based Systems & Products*, section « Defensive UX » (eugeneyan.com/writing/llm-patterns/). Lignée : guidelines Human-AI interaction (Microsoft/Apple) citées dans le post.

## Voir aussi
- [patterns-systemes-llm](patterns-systemes-llm.md) — les 7 patterns dont celui-ci fait partie.
- [resilience-fallback-llm](resilience-fallback-llm.md) — le versant infra de la dégradation gracieuse.
- [hitl-statique-dynamique](hitl-statique-dynamique.md) — calibrer la friction selon le risque.
- [data-flywheel-feedback](data-flywheel-feedback.md) — le signalement utilisateur alimente la boucle.
