---
titre: "Data flywheel : collecte de feedback"
type: "Concept"
theme: evaluation
niveau: 🔴
source_url: https://eugeneyan.com/writing/llm-patterns/
source_titre: "Patterns for Building LLM-based Systems & Products (Collect user feedback)"
---

# Data flywheel : collecte de feedback

**En une phrase** — la donnée de production est le seul actif durable d'un produit LLM : capter le feedback utilisateur (explicite et implicite) crée un *flywheel* qui alimente à la fois les évals, le fine-tuning et les guardrails — l'avantage compétitif qui ne se copie pas.

## Ce que dit la source
Septième pattern de production d'Eugene Yan. Deux types de signaux :

- **Feedback explicite** : pouce haut/bas, notes, corrections, signalements. Précis mais **rare** (peu d'utilisateurs prennent la peine) et biaisé (les mécontents votent plus).
- **Feedback implicite** : l'utilisateur a-t-il copié la réponse ? régénéré ? reformulé ? abandonné ? accepté la suggestion de code ? Abondant mais **bruité** (un signal ambigu — une régénération peut signifier « mauvais » ou « explore une variante »).

Ces signaux ferment la boucle : ils deviennent des **cas d'éval** (les échecs réels → golden set, cf. [eval-driven-development](eval-driven-development.md)), des **données de fine-tuning** (paires préférées/rejetées), et des **règles de guardrails** (motifs d'erreur récurrents). Plus le produit est utilisé, plus il s'améliore — le *flywheel*.

## Tradeoff / insight pour un senior
- **C'est la vraie douve, pas le modèle.** Le modèle de base est un commodity accessible à tous ; la **boucle de données propriétaire** issue de tes utilisateurs ne l'est pas. Un produit sans capture de feedback jette son seul avantage cumulatif.
- **Instrumenter le feedback est une décision d'architecture, pas une après-coup.** Il faut relier chaque signal à la **trace** qui l'a produit (prompt, contexte, version de modèle/prompt) — sinon le signal est inexploitable. D'où le couplage fort avec l'[observabilité](observabilite-llm-best-practices.md) : sans `trace_id`, pas de flywheel.
- **Le feedback implicite ment souvent.** Définir la sémantique de chaque signal *avant* de l'optimiser (qu'est-ce qu'une « bonne » réponse : copiée ? non-régénérée ? convertie ?). Optimiser un proxy mal défini dégrade le produit.
- **Privacy.** Capturer prompts/réponses + feedback, c'est stocker de la donnée potentiellement sensible : consentement, anonymisation/PII scrubbing, rétention — mêmes exigences que pour l'ingestion d'observabilité.

## Source primaire
Eugene Yan, *Patterns for Building LLM-based Systems & Products*, section « Collect user feedback » (eugeneyan.com/writing/llm-patterns/). Concept de *data flywheel* popularisé côté produit ML (Andrew Ng, Tesla).

## Voir aussi
- [patterns-systemes-llm](patterns-systemes-llm.md) — les 7 patterns dont celui-ci.
- [eval-driven-development](eval-driven-development.md) — les échecs captés deviennent des évals.
- [error-analysis](error-analysis.md) — exploiter qualitativement les signaux collectés.
- [ux-defensive-llm](ux-defensive-llm.md) — l'UX qui rend le feedback capturable.
- [observabilite-llm-best-practices](observabilite-llm-best-practices.md) — relier feedback ↔ trace.
