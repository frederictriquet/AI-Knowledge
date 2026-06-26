---
type: index
titre: "Thème — Prompting"
theme: prompting
---

# ✍️ Prompting

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Formuler et optimiser les prompts (techniques, in-context learning)._

## Concepts (22)

### 🔴 Substance / cœur
- **[Directional Stimulus Prompting (DSP)](../fiches/directional-stimulus-prompting.md)** — entraîner un petit policy model qui génère, par instance, des stimuli (mots-clés, indices) orientant un grand LLM boîte noire gelé — on optimise le policy model, jamais le LLM.
- **[ICL : sélection d'exemples & techniques zero-shot](../fiches/icl-exemplar-et-zero-shot.md)** — En few-shot, le choix des exemples, leur ordre et leur quantité pèsent autant que le contenu du prompt ; en zero-shot, plusieurs reformulations simples de la consigne suffisent à améliorer la sortie.
- **[In-context learning (ICL)](../fiches/in-context-learning.md)** — capacité d'un LLM à apprendre une tâche depuis les démonstrations placées dans son prompt, sans aucune mise à jour de ses poids.
- **[Integrated prompt environments — donner les prompts aux experts métier](../fiches/integrated-prompt-environments.md)** — les prompts « ne sont que de l'anglais » : les équipes les plus efficaces donnent aux experts métier les outils pour écrire et itérer les prompts **directement**, dans le contexte de l'application, au lieu de faire transiter leur expertise par les ingénieurs.
- **[Le prompt engineering est empirique (étude de cas)](../fiches/prompt-engineering-est-empirique.md)** — Une étude de cas réelle (détection d'« entrapment » dans des textes à risque suicidaire) montre que le prompt engineering est un processus itératif, sensible et peu transférable, où même les techniques réputées ne gagnent pas toujours.
- **[Prompt tuning (soft prompts)](../fiches/prompt-tuning.md)** — méthode PEFT qui entraîne par descente de gradient un petit jeu de vecteurs continus (« soft prompts » / tokens virtuels) injectés en entrée, le backbone restant gelé — à ne pas confondre avec le prompt engineering textuel.
- **[Techniques d'auto-critique](../fiches/self-criticism-techniques.md)** — Faire évaluer, vérifier et corriger par le modèle sa propre sortie, en boucle si besoin, pour fiabiliser la réponse sans intervention humaine.
- **[Techniques d'ensembling](../fiches/ensembling-techniques.md)** — Résoudre le même problème via plusieurs prompts/chemins de raisonnement, puis agréger les sorties (souvent par vote majoritaire) pour réduire la variance, au prix de N appels.
- **[Techniques de décomposition](../fiches/decomposition-techniques.md)** — Casser explicitement un problème complexe en sous-problèmes plus simples, puis les résoudre un à un, pour fiabiliser la réponse finale.

### 🟡 Tradeoff / intermédiaire
- **[Automatic Prompt Engineer (APE) & design automatique de prompts](../fiches/automatic-prompt-engineer-ape.md)** — le prompt n'est pas un texte à rédiger à la main mais un objet à optimiser : on fait générer des candidats d'instruction par le LLM puis on garde le meilleur selon une fonction de score mesurable.
- **[Décomposition anticipée vs au fil de l'eau](../fiches/decomposition-first-vs-interleaved.md)** — tout planifier d'avance puis exécuter sans re-raisonner (ReWOO) versus planifier et réviser à chaque observation (ReAct).
- **[Méta-prompting](../fiches/meta-prompting.md)** — fournir au LLM un template de raisonnement réutilisable par classe de tâches (structure et étapes), plutôt qu'un prompt jetable pour un cas unique.
- **[Optimisation des prompts](../fiches/prompt-optimization.md)** — affiner automatiquement (ou semi-automatiquement) des prompts existants par itération, évaluation par indicateurs et boucles de feedback, à distinguer du prompt engineering manuel qui les conçoit de zéro.
- **[Prompt caching](../fiches/prompt-caching.md)** — réutiliser une réponse déjà calculée pour un prompt identique, mais attention : le tutoriel implémente un cache de réponses exact-match côté client (LangChain `SQLiteCache`), pas le prompt caching de préfixe (KV-cache) côté fournisseur.
- **[Prompt chaining](../fiches/prompt-chaining.md)** — décomposer une tâche complexe en une séquence de prompts simples où la sortie de chaque étape alimente la suivante.
- **[Taxonomie des techniques de prompting (The Prompt Report)](../fiches/taxonomie-techniques.md)** — La version systématique et sourcée du catalogue de prompting : ~58 techniques textuelles classées en 5 familles (ICL, Thought Generation, Decomposition, Ensembling, Self-Criticism), chacune attribuée à son papier d'origine.

### 🟢 Survol / introductif
- **[Catalogue des techniques de prompting](../fiches/techniques-catalogue.md)** — un index des stratégies de structuration de prompts, appliquées à une tâche unique (« expliquer le changement climatique ») pour comparer leurs comportements.
- **[Few-shot prompting](../fiches/few-shot-prompting.md)** — fournir quelques exemples étiquetés dans le prompt pour guider le modèle, en exploitant ses connaissances pré-entraînées sans réentraînement.
- **[One-shot prompting](../fiches/one-shot-prompting.md)** — fournir au modèle un seul exemple bien conçu pour qu'il généralise une tâche, à mi-chemin entre zero-shot et few-shot.
- **[Qu'est-ce que le prompt engineering](../fiches/prompt-engineering.md)** — la discipline de conception et de raffinement itératif des instructions textuelles fournies à un LLM pour orienter sa sortie.
- **[Role prompting (persona)](../fiches/role-prompting.md)** — assigner au modèle un rôle ou persona explicite (« You are a compassionate veterinarian… ») pour orienter ton, style et comportement de la réponse.
- **[Zero-shot prompting](../fiches/zero-shot-prompting.md)** — demander une tâche à un LLM sans lui fournir d'exemple, en s'appuyant uniquement sur ses connaissances pré-entraînées.

## Outils (3)

- **[GitHub Spec Kit](../fiches%20outils/spec-kit.md)** — _Toolkit CLI (spec-driven development)_
- **[GSD (Get Shit Done)](../fiches%20outils/gsd.md)** — _Framework de méta-prompting / spec-driven development pour agents de codage (couche par-dessus Claude Code & autres)_
- **[Ponytail](../fiches%20outils/ponytail.md)** — _Skill / Plugin (multi-agents)_
