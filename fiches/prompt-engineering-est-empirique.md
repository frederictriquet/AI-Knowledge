---
titre: "Le prompt engineering est empirique (étude de cas)"
type: "Concept"
theme: prompting
niveau: 🔴
source_url: https://arxiv.org/abs/2406.06608
source_titre: "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques"
---

# Le prompt engineering est empirique (étude de cas)

**En une phrase** — Une étude de cas réelle (détection d'« entrapment » dans des textes à risque suicidaire) montre que le prompt engineering est un processus itératif, sensible et peu transférable, où même les techniques réputées ne gagnent pas toujours.

## Ce que dit la source
Le rapport (§6.2) documente une étude de cas annotée : un prompt engineer expert tente de détecter l'entrapment dans des posts Reddit avec gpt-4-turbo-preview. Le processus est entièrement manuel et tâtonnant : le modèle ignore d'abord le concept, sur-génère des labels positifs, refuse parfois de répondre. Certaines décisions améliorant le F1 se révèlent mauvaises sur le fond (restreindre aux mentions explicites alors que l'entrapment peut être implicite). La discussion (§6.2.4) tire trois enseignements : le prompt engineering diffère de la programmation classique (on « cajole » le modèle, qui est extrêmement sensible à des détails sans raison apparente) ; il faut plonger dans les données ; et surtout collaborer entre prompt engineer et experts du domaine. La case study §6.1 ajoute que la sélection de technique s'apparente à une recherche d'hyperparamètres et que Zero-Shot-CoT peut chuter sous Zero-Shot. Enfin, DSPy (Khattab et al.) optimise automatiquement le prompt et dépasse l'expert humain sur le test, illustrant la promesse de l'automatisation.

## Exemple
Le « black art » se voit dans un détail : le prompt engineer colle par accident deux fois le même email de contexte — et ce doublon involontaire améliore nettement le F1 ; retirer la duplication le fait chuter, et anonymiser les noms propres de l'email le dégrade encore (effet rappelant la technique Re-reading). À l'opposé, DSPy (BootstrapFewShotWithRandomSearch, gpt-4-0125-preview, 16 itérations) bootstrappe seul un prompt de 15 exemplars + une démonstration de raisonnement et atteint 0.548 F1 / 0.385 précision / 0.952 rappel sur le test, sans recourir ni à l'email ni à l'instruction erronée sur l'explicite — battant l'humain.

## Pourquoi c'est utile
Apporte une leçon méthodologique étayée : le prompt engineering est empirique, finicky et fragile, justifiant l'évaluation rigoureuse et l'automatisation (type DSPy) plutôt que la confiance dans des recettes toutes faites.

## Points clés
- Processus itératif et tâtonnant ; le modèle est « cajolé », pas programmé.
- Sensibilité extrême à des détails sans raison apparente ; faible transférabilité entre modèles/tâches.
- Des gains de F1 peuvent masquer de mauvaises décisions sur le fond (explicite vs implicite).
- CoT n'aide pas toujours : Zero-Shot-CoT chute parfois sous Zero-Shot.
- Sélection de technique = recherche d'hyperparamètres ; DSPy automatise et bat l'expert sur le test.
- Recommandation clé : collaboration prompt engineer / experts du domaine.

## Voir aussi
- [Optimisation des prompts](prompt-optimization.md)
- [DSPy](dspy.md)
- [Qu'est-ce que le prompt engineering](prompt-engineering.md)
- [papier complet](../sources/prompt-report/md/prompt-report.md)
