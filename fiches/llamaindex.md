---
titre: "LlamaIndex"
theme: frameworks-outillage
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/insights/top-ai-agent-frameworks
source_titre: "Cadres d’agents d’IA : choisir de bonnes bases pour votre entreprise"
---

# LlamaIndex

**En une phrase** — un cadre d'orchestration d'agents dont l'unité de base est le *workflow* événementiel : des étapes déclenchées par des événements et reliées par un contexte partagé, sans chemins prédéfinis entre elles.

## En détail
LlamaIndex est un cadre open source d'harmonisation des données pour créer des solutions d'IA générative et agentique, offrant agents et outils préconfigurés. Le mécanisme central est celui des *workflows*, conçus pour développer des systèmes multi-agents. Trois éléments composent un workflow : les *étapes* (actions spécifiques à chaque agent, briques de base), les *événements* (qui déclenchent les étapes et servent de moyen de communication entre elles) et le *contexte* (partagé tout au long du workflow, permettant aux étapes de stocker, récupérer et transmettre des données et de maintenir l'état). Cette architecture événementielle permet une exécution asynchrone. Contrairement à une architecture graphique, les parcours entre étapes n'ont pas besoin d'être définis, ce qui autorise des transitions plus souples. Les workflows LlamaIndex conviennent donc aux agents dynamiques qui doivent souvent revenir à des étapes antérieures ou se ramifier vers plusieurs étapes.

## Tradeoff / insight pour un senior
Le contraste explicite avec LangGraph est l'insight : graphe (nœuds/arêtes câblés à l'avance, contrôle granulaire) vs événements (couplage par publication/abonnement, parcours émergents). LlamaIndex paie la souplesse par une traçabilité moindre du flux de contrôle ; LangGraph paie le contrôle par la rigidité du graphe. Choix selon que les transitions sont connues d'avance ou non.

## Source primaire
Voir la documentation LlamaIndex Workflows et le dépôt GitHub.

## Voir aussi
- [semantic-kernel](semantic-kernel.md)
- [orchestration-types](orchestration-types.md)
