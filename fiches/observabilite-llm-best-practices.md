---
titre: "Observabilité LLM : best practices (indépendantes de l'outil)"
type: "Concept"
theme: gouvernance-alignement-ops
niveau: 🔴
source_url: https://opentelemetry.io/docs/specs/semconv/gen-ai/
source_titre: "OpenTelemetry — GenAI semantic conventions"
---

# Observabilité LLM : best practices (indépendantes de l'outil)

**En une phrase** — instrumenter une app LLM, ce n'est pas brancher un dashboard : c'est décider *quoi* tracer (span par étape de chaîne), *comment* évaluer la qualité sans se ruiner ni se mentir (juge calibré, échantillonné), et *quoi ne pas ingérer* (PII) — l'outil n'est que le réceptacle.

## En détail
Les trois questions de fond, souvent escamotées derrière « activez la feature » :

**1. Quoi tracer — la granularité span.** Une requête utilisateur = une *trace* ; chaque appel LLM, retrieval, function-call, parsing = un *span*. Le standard de fait est **OpenTelemetry GenAI semantic conventions** : attributs normalisés (`gen_ai.request.model`, `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, `gen_ai.request.temperature`…). Tracer au niveau span permet d'attribuer latence et coût *à l'étape responsable* — le seul moyen d'arbitrer le routage multi-modèle (cf. [agentops](agentops.md)). Best practice : instrumenter via OTel, pas via un SDK propriétaire → pas de vendor lock-in, l'app reste portable d'un backend d'observabilité à l'autre.

**2. Les 4 signaux à corréler.** (a) *Opérationnel* : latence p50/p95/p99 par étape, taux d'erreur, time-to-first-token ; (b) *Coût* : tokens in/out par requête, coût/requête, et surtout coût *par feature métier* (pas un agrégat global inexploitable) ; (c) *Qualité* : taux de « failure to answer », toxicité, sentiment, pertinence — voir piège ci-dessous ; (d) *Sécurité* : tentatives de prompt injection, fuite de PII en entrée *et en sortie*. La valeur naît de la **corrélation** : un pic de latence p95 corrélé à un cluster de prompts d'un même topic > trois dashboards isolés.

**3. Définir les SLO avant les dashboards.** « 98 % success rate » ne veut rien dire sans définition du succès. Best practice : écrire les objectifs (p95 < X ms, coût/requête < Y, taux de hallucination < Z % sur un golden set) *avant* d'instrumenter, et alerter sur la **dérive** (drift) de ces SLO, pas sur des seuils absolus figés.

**4. Boucler observabilité → éval → correctif.** Les traces de production sont le carburant des golden sets : les requêtes qui échouent en prod deviennent des cas de test. C'est le lien avec l'[eval-driven-development](eval-driven-development.md) — l'observabilité sans boucle de réinjection est de la décoration.

## Tradeoff / insight pour un senior
Les quatre pièges rarement explicités — et qui décident du ROI réel :

- **Le juge LLM n'est pas gratuit ni fiable.** Évaluer la qualité « out-of-the-box » via LLM-as-judge, c'est *doubler* le coût d'inférence (un appel d'éval par appel métier) et hériter des biais du juge : biais de position, biais de verbosité, auto-préférence, mauvaise calibration. Best practice : **échantillonner** l'éval (1–10 %, pas 100 %), calibrer le juge contre des labels humains avant de lui faire confiance, et préférer un modèle juge différent du modèle évalué. Cf. [llm-as-judge-correct](llm-as-judge-correct.md) et [llm-evaluators](llm-evaluators.md).
- **Faux positifs des checks automatiques.** « Toxicity », « negative sentiment », « failure to answer » sont des classifieurs faillibles : un sentiment négatif *légitime* (l'utilisateur décrit un problème) n'est pas un échec. Sans seuil calibré, on noie les vrais signaux sous le bruit et l'équipe finit par ignorer l'alerting.
- **Échantillonnage = arbitrage observabilité/coût.** Tracer 100 % des requêtes avec payloads complets explose le coût d'ingestion *et* de stockage (les prompts/réponses sont volumineux). Best practice : head-sampling sur le trafic nominal, tail-sampling 100 % sur les traces en erreur ou lentes — on garde ce qui informe.
- **Privacy : l'observabilité est une surface d'exfiltration.** Ingérer prompts et réponses, c'est dupliquer des données potentiellement sensibles (PII, secrets, données client) dans un système tiers, souvent hors de l'UE. Best practice : **scrubber le PII à la source, avant l'export** (pas « par défaut dans l'outil », ce qui veut dire qu'il a déjà transité), définir une rétention courte, et traiter le backend d'observabilité comme un actif soumis au même RGPD/DLP que la prod. Lien sécurité : [prompt-injection](prompt-injection.md), [prevent-prompt-injection](prevent-prompt-injection.md).

Insight : le différenciateur entre deux plateformes d'observabilité LLM n'est ni le nombre de dashboards ni le clustering sémantique — c'est la **qualité de la couche d'éval** (calibration du juge, faux positifs) et la **maîtrise du couple coût/privacy de l'ingestion**. C'est là que se joue le ROI réel, et c'est ce que les démos produit montrent le moins.

## Source primaire
- **OpenTelemetry GenAI semantic conventions** (opentelemetry.io/docs/specs/semconv/gen-ai/) — standard d'instrumentation.
- **OWASP Top 10 for LLM Applications** (owasp.org) — pour le pilier sécurité (LLM01 Prompt Injection, LLM06 Sensitive Information Disclosure).

## Voir aussi
- [agentops](agentops.md) — le cadre ops/DevOps des agents (session/trace/span OTel).
- [eval-driven-development](eval-driven-development.md) — la boucle qui ferme l'observabilité.
- [llm-as-judge-correct](llm-as-judge-correct.md) · [llm-evaluators](llm-evaluators.md) — éval automatique et ses biais.
- [prompt-injection](prompt-injection.md) · [prevent-prompt-injection](prevent-prompt-injection.md) — pilier sécurité.
