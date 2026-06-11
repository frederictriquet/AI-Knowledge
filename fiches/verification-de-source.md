---
titre: "Vérification de source (anti-contamination contexte)"
type: "Concept"
theme: raisonnement-planification
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/tutorials/build-corrective-rag-agent-granite-tavily
source_titre: "Créer un agent RAG correctif avec IBM Granite et Tavily"
---

# Vérification de source (anti-contamination contexte)

**En une phrase** — une étape LLM qui rejette un passage récupéré dès qu'il provient d'une source hors-périmètre, avant qu'il ne pollue le contexte.

## En détail
Dans le cadre cRAG, la vérification de source constitue un nouveau prompt essentiel. Le `CONTEXT_SOURCE_VERIFICATION_PROMPT` demande au LLM de distinguer un texte issu d'une source générale/publique d'un texte spécifique à une police privée. Si le contexte mentionne ou implique fortement des programmes de santé publique (Medi-Cal, Medicaid, Medicare, NHS, programmes financés par l'État) ou s'il est trop général, le modèle répond « NO » ; sinon « YES ». Concrètement, après chaque recherche Tavily, `is_relevant_source = llm(verification_prompt).strip().upper()` : seul un « YES » ajoute le passage à `retrieved_context_pieces` ; un « NO » provoque le log « context source rejected » et le passage n'est pas intégré, ce qui laisse le contexte court et déclenche le fallback suivant ou le refus final. But déclaré : « empêche la génération de réponses trompeuses et permet l'autocorrection ».

## Exemple
Cas du tutoriel : l'agent répond à des questions sur une police d'assurance privée (« Super Star Health » de Care Health Insurance). Le PDF interne ne couvre pas la question, l'agent bascule sur Tavily ; la recherche Web remonte un passage factuel sur Medi-Cal (programme de santé publique financé par l'État). Ce passage passerait le scoring de pertinence 0-5, mais le `CONTEXT_SOURCE_VERIFICATION_PROMPT` renvoie « NO », log « context source rejected » : il n'entre jamais dans `retrieved_context_pieces`. Le contexte reste sous `MIN_CONTEXT_LENGTH`, ce qui déclenche la réécriture de requête puis, à défaut, le refus poli.

## Tradeoff / insight pour un senior
C'est un filtre de pertinence de domaine, distinct du grader de pertinence à la requête. Le scoring 0-5 dit « ce passage répond-il à la question ? » ; la vérification de source dit « ce passage a-t-il le droit d'entrer dans ce contexte ? ». Sans elle, un résultat web factuel mais hors-périmètre (un programme public) passerait le scoring et contaminerait une réponse censée porter sur une police privée. Le coût est un appel LLM par passage externe, et la décision binaire yes/no reste sujette aux erreurs du juge.

## Source primaire
« Cette fonction empêche la génération de réponses trompeuses et permet l'autocorrection, ce qui contribue à l'affinement des connaissances. » ([source](../sources/ibm-guide-agents-ia/md/68-build-corrective-rag-agent-granite-tavily.md))

## Voir aussi
- [Corrective RAG (cRAG)](corrective-rag.md)
- [Tool grounding](tool-grounding.md)
