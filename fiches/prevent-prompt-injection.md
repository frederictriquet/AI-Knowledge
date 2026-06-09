---
titre: "Prévenir l'injection de prompt"
theme: securite
niveau: 🔴
provenance: ✅
base: ibm-guide-prompt-engineering
source_url: https://www.ibm.com/fr-fr/think/insights/prevent-prompt-injection
source_titre: "Éviter les attaques par injection d’invites"
---

# Prévenir l'injection de prompt

> Fiche du glossaire prompting · Pertinence 🔴 substance · Provenance ✅ présent · Sources corpus : [../md/12-prevent-prompt-injection.md](../sources/ibm-guide-prompt-engineering/md/12-prevent-prompt-injection.md)

**En une phrase** — catalogue de défenses partielles contre l'injection de prompt, à empiler en défense en profondeur, aucune n'étant infaillible (la seule garantie absolue serait de ne pas utiliser de LLM).

## Ce que dit le corpus
IBM liste des contre-mesures, en soulignant qu'aucune n'est complète et qu'il faut les combiner pour qu'elles compensent mutuellement leurs lacunes. Bonnes pratiques de cybersécurité : mises à jour/correctifs, formation des utilisateurs, EDR/SIEM/IDPS. **Paramétrage** : séparer commandes et entrées comme en SQL est ici difficile ; les « requêtes structurées » de Berkeley convertissent système et données utilisateur dans des formats spéciaux, réduisent certaines injections mais exigent un fine-tuning du LLM et restent vulnérables aux arbres d'attaques. **Validation/assainissement et filtrage** : filtres par signature sur longueur, similarité au prompt système, similarité à des attaques connues — sujets à faux positifs/négatifs. **Détecteur LLM (classificateur)** : un second LLM filtre les entrées, mais étant lui-même un LLM il est injectable. **Délimiteurs** : chaînes uniques séparant système et entrée, contournables par les *completion attacks* (faire croire la tâche terminée) et par les fuites de prompt. **Filtrage des sorties**, **moindre privilège** (limite les dégâts sans empêcher l'attaque, ne couvre pas les comptes détournés) et **human-in-the-loop** (laborieux, contournable par ingénierie sociale).

## Tradeoff / insight pour un senior
Chaque défense impose un coût fonctionnel symétrique à sa robustesse : durcir le filtrage bloque des entrées légitimes, le human-in-the-loop tue la fluidité, le paramétrage par requêtes structurées force un fine-tuning et casse les chatbots ouverts. Le point non évident : le détecteur d'injection est lui-même une surface d'injection. Raisonner en couches indépendantes (et supposer chacune franchissable) plutôt qu'en barrière unique.

## Source primaire
Page IBM citée (think/insights/prevent-prompt-injection). Méthode des « requêtes structurées » attribuée à des chercheurs de l'université de Berkeley ; pas d'arXiv reproductible dans le corpus.

## Voir aussi
- [spotlighting](spotlighting.md) (base agents, hors-corpus)
- [dual-LLM & CaMeL](dual-llm-camel.md) (base agents, hors-corpus)
- [OWASP](owasp-llm-agentic.md) (base agents, hors-corpus)
- [prompt-injection](prompt-injection.md)
