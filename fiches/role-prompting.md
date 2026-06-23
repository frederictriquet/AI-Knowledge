---
titre: "Role prompting (persona)"
type: "Concept"
theme: prompting
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/tutorials/using-role-prompting-with-watsonx-and-granite
source_titre: "Utiliser l'invite de rôles avec IBM watsonx et Granite"
---

# Role prompting (persona)

**En une phrase** — assigner au modèle un rôle ou persona explicite (« You are a compassionate veterinarian… ») pour orienter ton, style et comportement de la réponse.

## En détail
La mise en pratique s'appuie sur watsonx.ai + Granite (granite-3-8b-instruct, via langchain_ibm). Le role prompting (ou persona prompting) consiste à demander au modèle d'assumer un rôle spécifique. Deux exemples l'illustrent : réécrire « Twinkle, Twinkle, Little Star » en sonnet shakespearien (rôle = William Shakespeare), et comparer un prompt système nu à un prompt système avec rôle « vétérinaire compatissant, professionnel et expérimenté » pour un assistant de cabinet vétérinaire. La réponse avec rôle est plus nuancée, plus empathique et mieux contextualisée. Des frameworks multi-agents comme ChatDev utilisent également le role prompting (« mécanisme d'auto-attention »), et les modèles Granite, entraînés sur des données d'entreprise, assument bien les rôles. L'évaluation reste purement qualitative : aucune métrique, aucun chiffre.

## Tradeoff / insight pour un senior
Technique à coût quasi nul et effet réel sur le ton, mais l'effet sur la justesse factuelle est inconstant et non mesuré ici. Le persona peut induire des hallucinations « dans le personnage » (un « expert » plus assertif n'est pas plus exact). À traiter comme un levier de style et d'UX, pas comme un mécanisme de raisonnement.

## Source primaire
Pas de bibliographie. Voir la littérature sur le persona/role prompting.

## Voir aussi
- [Zero-shot prompting](zero-shot-prompting.md)
- [Catalogue des techniques](techniques-catalogue.md)
