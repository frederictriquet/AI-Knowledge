# Routage & cascades de modèles

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. [Glossaire](../../GLOSSAIRE-PATTERNS.md) · Pertinence 🟡 tradeoff

**En une phrase** — router chaque requête vers le modèle le moins cher CAPABLE, ou enchaîner du petit au gros (cascade) avec un juge de confiance ; réduit fortement le coût à qualité quasi constante.

## L'idée
Tous les appels n'ont pas besoin du plus gros modèle. Deux stratégies. Le **routage** classe la requête en amont et l'envoie au modèle adapté (petit pour le trivial, gros pour le difficile). La **cascade** essaie d'abord un modèle bon marché, puis évalue la réponse via un score de confiance ou un juge ; si la confiance est insuffisante, elle *escalade* au modèle supérieur. On ne paie le gros modèle que sur la fraction de requêtes qui le justifient.

## Tradeoff / quand l'utiliser
Idéal sur du trafic à volume élevé et difficulté hétérogène : économies massives à qualité quasi constante. Le coût se déplace vers le **routeur/juge** (lui-même faillible) et la latence des escalades en cascade s'additionne. Le seuil de confiance est un curseur coût/qualité à calibrer.

## Source primaire
Chen et al., 2023, *FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance*, arXiv:2305.05176 *(arXiv vérifié — HTTP 200 + titre)* ; RouteLLM (LMSYS, 2024).

## Voir aussi
- [llm-as-a-judge](../llm-as-a-judge.md) (corpus)
- [semantic-caching](../semantic-caching.md) (corpus)
