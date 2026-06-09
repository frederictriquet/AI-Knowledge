---
titre: "LlamaIndex"
theme: frameworks-outillage
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/insights/top-ai-agent-frameworks
source_titre: "Cadres d’agents d’IA : choisir de bonnes bases pour votre entreprise"---

# LlamaIndex

> Fiche du glossaire des patterns · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [39-top-ai-agent-frameworks](../sources/ibm-guide-agents-ia/md/39-top-ai-agent-frameworks.md)

**En une phrase** — un cadre d'orchestration d'agents dont l'unité de base est le *workflow* événementiel : des étapes déclenchées par des événements et reliées par un contexte partagé, sans chemins prédéfinis entre elles.

## Ce que dit le corpus
IBM présente LlamaIndex comme un cadre open source d'harmonisation des données pour créer des solutions d'IA générative et agentique, offrant agents et outils préconfigurés. Le mécanisme mis en avant est celui des *workflows*, introduits récemment pour développer des systèmes multi-agents. Trois éléments composent un workflow : les *étapes* (actions spécifiques à chaque agent, briques de base), les *événements* (qui déclenchent les étapes et servent de moyen de communication entre elles) et le *contexte* (partagé tout au long du workflow, permettant aux étapes de stocker, récupérer et transmettre des données et de maintenir l'état). Cette architecture événementielle permet une exécution asynchrone. Le corpus insiste : contrairement à une architecture graphique, les parcours entre étapes n'ont pas besoin d'être définis, ce qui autorise des transitions plus souples. Les workflows LlamaIndex conviennent donc aux agents dynamiques qui doivent souvent revenir à des étapes antérieures ou se ramifier vers plusieurs étapes.

## Tradeoff / insight pour un senior
Le contraste explicite avec LangGraph est l'insight : graphe (nœuds/arêtes câblés à l'avance, contrôle granulaire) vs événements (couplage par publication/abonnement, parcours émergents). LlamaIndex paie la souplesse par une traçabilité moindre du flux de contrôle ; LangGraph paie le contrôle par la rigidité du graphe. Choix selon que les transitions sont connues d'avance ou non.

## Source primaire
Non citée par IBM — voir la documentation LlamaIndex Workflows et le dépôt GitHub (hors-corpus).

## Voir aussi
- [semantic-kernel](semantic-kernel.md)
- [orchestration-types](orchestration-types.md)
