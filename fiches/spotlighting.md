---
titre: "Spotlighting"
type: "Concept"
theme: securite
niveau: 🟡
source_url: https://arxiv.org/abs/2403.14720
---

# Spotlighting

**En une phrase** — marquer explicitement les données non fiables dans le prompt pour que le modèle distingue « instructions » de « données » et n'exécute pas le contenu injecté.

## L'idée
Le Spotlighting regroupe des techniques de transformation de prompt qui rendent visible la frontière entre les consignes du système et le contenu externe potentiellement hostile. Trois variantes : le **delimiting** (entourer les données de balises explicites), le **datamarking** (insérer un marqueur entre chaque token du contenu, ex. un caractère spécial répété) et l'**encoding** (encoder les données, base64 par exemple) pour qu'elles soient manifestement « à traiter, pas à obéir ». Le modèle apprend ainsi à ignorer les instructions cachées à l'intérieur de la zone marquée.

## Tradeoff / quand l'utiliser
Bon marché et sans réentraînement : applicable à n'importe quel pipeline qui injecte du contenu tiers (RAG, lecture de mails/pages). Mais c'est une mitigation probabiliste, pas une garantie : un attaquant déterminé peut tenter de reproduire les délimiteurs, et l'encodage dégrade parfois la compréhension du contenu légitime.

## Source primaire
Hines et al., 2024 (Microsoft), *Defending Against Indirect Prompt Injection Attacks With Spotlighting*, arXiv:2403.14720 *(arXiv vérifié — HTTP 200 + titre)*.

## Voir aussi
- [dual-llm-camel](dual-llm-camel.md)
- [guardrail-noeud-entree](guardrail-noeud-entree.md)
