---
titre: "Integrated prompt environments — donner les prompts aux experts métier"
theme: prompting
niveau: 🔴
source_url: https://hamel.dev/blog/posts/field-guide/
source_titre: "A Field Guide to Rapidly Improving AI Products"
---

# Integrated prompt environments — donner les prompts aux experts métier

**En une phrase** — les prompts « ne sont que de l'anglais » : les équipes les plus efficaces donnent aux experts métier les outils pour écrire et itérer les prompts **directement**, dans le contexte de l'application, au lieu de faire transiter leur expertise par les ingénieurs.

## Ce que dit la source
Hamel décrit un anti-pattern récurrent : un expert métier (designer pédagogique, juriste, médecin…) formalise son savoir dans un PowerPoint, que les ingénieurs « retraduisent » ensuite en prompts. Or **un prompt est de l'anglais** : cet aller-retour crée une friction inutile et dilue l'expertise. Les meilleures équipes inversent le modèle.

Deux niveaux d'outillage :
1. **Prompt playgrounds** (Arize Phoenix, LangSmith, Braintrust) — bon point de départ : tester des prompts, injecter des jeux d'exemples, comparer les résultats.
2. **Integrated prompt environments** — l'étape que la plupart des équipes ratent. Une vraie application IA n'est pas qu'un prompt : RAG sur une base de connaissances, orchestration d'agents, logique métier. Au lieu d'un playground isolé, on construit un **« mode admin » de l'interface réelle** qui expose l'édition du prompt **dans son contexte applicatif** (mêmes données, même RAG, même logique que ce que voit l'utilisateur final). Exemple donné : un assistant immobilier où l'UI agent reçoit un « admin mode » permettant à l'équipe produit d'éditer le prompt et de déboguer en situation réelle.

**Barrière annexe — le jargon.** Envelopper le travail dans du vocabulaire technique (« on construit un agent », « RAG », « prompt injection ») exclut les vrais experts du domaine, qui se croient incompétents alors que la tâche réelle est… d'écrire un prompt. Hamel donne une table de traduction : « RAG » → « s'assurer que le modèle a le bon contexte » ; « prompt injection » → « empêcher qu'on piège l'IA pour ignorer nos règles » ; « hallucination » → « parfois l'IA invente, il faut vérifier ses réponses ».

## Pourquoi c'est utile
Mettre l'expert métier au centre de la boucle d'itération, dans le contexte applicatif réel, est un levier d'amélioration produit souvent négligé : la plupart des guides d'outillage IA se concentrent sur l'ingénierie/plateforme et ne traitent pas le **qui** écrit les prompts.

## À retenir
- Les prompts sont de l'anglais : faire écrire et itérer les experts métier **directement**, pas via une retraduction par les ingénieurs.
- Playground = point de départ ; **integrated prompt environment** (mode admin de l'UI réelle, avec RAG/agents/logique métier en place) = la marche que les équipes oublient.
- Bannir le jargon qui exclut les experts : décrire la tâche en clair, pas en termes techniques.

## Voir aussi
- [Error analysis : regarde tes données](error-analysis.md)
- [Eval-driven development](eval-driven-development.md)
- [AgentOps](agentops.md)
- [post complet](../sources/hamel-husain/md/field-guide.md)
