---
titre: "Techniques d'auto-critique"
type: "Concept"
theme: prompting
niveau: 🔴
source_url: https://arxiv.org/abs/2406.06608
source_titre: "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques"
objectifs: [fiabilite]
---

# Techniques d'auto-critique

**En une phrase** — Faire évaluer, vérifier et corriger par le modèle sa propre sortie, en boucle si besoin, pour fiabiliser la réponse sans intervention humaine.

## Ce que dit la source
La famille Self-Criticism (§2.2.5) repose sur l'idée qu'il est utile que les LLM critiquent leurs propres sorties : un simple jugement (la réponse est-elle correcte ?) ou un feedback servant à améliorer la réponse. Self-Calibration (Kadavath et al.) rejoue la question avec la réponse du modèle et demande si elle est correcte, pour jauger la confiance. Self-Refine (Madaan et al.) est un cadre itératif : le modèle produit une réponse, génère un feedback dessus, puis l'améliore, jusqu'à une condition d'arrêt. Reversing Chain-of-Thought / RCoT (Xue et al.) reconstruit le problème à partir de la réponse générée et compare pour détecter des incohérences converties en feedback. Self-Verification (Weng et al.) génère plusieurs solutions CoT puis les score en masquant des parties de la question. Chain-of-Verification / COVE (Dhuliawala et al.) génère des questions de vérification, y répond, puis produit une réponse révisée. Cumulative Reasoning (Zhang et al.) génère des étapes, les fait accepter ou rejeter par le LLM, et itère jusqu'à la réponse finale.

## Exemple
COVE (Dhuliawala et al.) se déroule en quatre temps : le modèle répond, génère une liste de questions de vérification ciblées sur les faits de sa propre réponse, y répond une à une indépendamment, puis produit une réponse révisée à la lumière de ces vérifications — ce qui réduit les hallucinations factuelles en QA. Self-Verification (Weng et al.) procède autrement : il échantillonne plusieurs solutions CoT, puis masque une partie de l'énoncé d'origine et demande au modèle de la reconstituer à partir de la solution candidate ; une solution qui permet de retrouver l'information masquée est mieux scorée. Gains rapportés sur huit jeux de données de raisonnement.

## Pourquoi c'est utile
Cette famille couvre tout le pan de l'auto-vérification et de l'auto-révision (Self-Refine, COVE, Self-Verification, Cumulative Reasoning), où le modèle boucle sur sa propre sortie pour la corriger.

## Techniques clés
- Self-Refine (Madaan et al.) — boucle feedback puis amélioration jusqu'à arrêt.
- Self-Verification (Weng et al.) — scoring de solutions CoT par masquage de la question.
- Chain-of-Verification / COVE (Dhuliawala et al.) — questions de vérification puis réponse révisée.
- Self-Calibration (Kadavath et al.) — re-question pour jauger la confiance.
- Reversing Chain-of-Thought / RCoT (Xue et al.) — reconstruction du problème pour détecter les incohérences.
- Cumulative Reasoning (Zhang et al.) — étapes acceptées/rejetées en boucle.

## Voir aussi
- [Chain-of-Thought](chain-of-thought.md)
- [Auto-réflexion des agents](self-reflection-agents.md)
- [papier complet](../sources/prompt-report/md/prompt-report.md)
