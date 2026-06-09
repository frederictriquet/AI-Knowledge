# Role prompting (persona)

> Fiche du [glossaire prompting](../GLOSSAIRE-PROMPTING.md) · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [../md/22-using-role-prompting-with-watsonx-and-granite.md](../md/22-using-role-prompting-with-watsonx-and-granite.md)

**En une phrase** — assigner au modèle un rôle ou persona explicite (« You are a compassionate veterinarian… ») pour orienter ton, style et comportement de la réponse.

## Ce que dit le corpus
Le fichier 22 est un tutoriel pratique watsonx.ai + Granite (granite-3-8b-instruct, via langchain_ibm). IBM définit le role prompting (ou persona prompting) comme la technique consistant à demander au modèle d'assumer un rôle spécifique. Deux exemples sont déroulés : réécrire « Twinkle, Twinkle, Little Star » en sonnet shakespearien (rôle = William Shakespeare), et comparer un prompt système nu à un prompt système avec rôle « vétérinaire compatissant, professionnel et expérimenté » pour un assistant de cabinet vétérinaire. IBM note que la réponse avec rôle est jugée plus nuancée, plus empathique et mieux contextualisée. Le corpus mentionne aussi que des frameworks multi-agents comme ChatDev utilisent le role prompting (« mécanisme d'auto-attention »), et que les modèles Granite, entraînés sur des données d'entreprise, assument bien les rôles. L'évaluation reste purement qualitative : aucune métrique, aucun chiffre.

## Tradeoff / insight pour un senior
Technique à coût quasi nul et effet réel sur le ton, mais l'effet sur la justesse factuelle est inconstant et non mesuré ici. Le persona peut induire des hallucinations « dans le personnage » (un « expert » plus assertif n'est pas plus exact). À traiter comme un levier de style et d'UX, pas comme un mécanisme de raisonnement.

## Source primaire
Non citée par IBM — tutoriel sans bibliographie. Voir la littérature sur le persona/role prompting (hors-corpus).

## Voir aussi
- [Zero-shot prompting](zero-shot-prompting.md)
- [Catalogue des techniques](techniques-catalogue.md)
