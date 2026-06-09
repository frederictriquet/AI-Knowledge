---
titre: "Modèles de langage augmentés (taxonomie de Weng)"
theme: fondamentaux-agents
niveau: 🔴
provenance: 🔗
base: sources/lilian-weng
source_url: https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/
source_titre: "Prompt Engineering"
---

# Modèles de langage augmentés (taxonomie de Weng)

> Fiche **source : Lilian Weng** · [post complet](../sources/lilian-weng/md/2023-03-15-prompt-engineering.md) · Pertinence 🔴 substance

**En une phrase** — la généalogie sourcée des agents tool-using : avant le « function calling » packagé, trois familles de techniques (récupération, exécution de code, appels d'API) augmentaient déjà un LLM gelé via le seul prompt.

## Ce que dit la source
Weng s'appuie sur le survey *Augmented Language Models* de Mialon et al. (2023) pour structurer trois catégories. **Récupération** : pour les connaissances postérieures au cutoff ou privées, on récupère puis on injecte dans le prompt (style RAG) ; Lazaridou et al. (2022) utilisent Google Search avec un classement TF-IDF des paragraphes, et Liu et al. (2022) montrent qu'une « récupération interne » — générer la connaissance avant de répondre — aide aussi. **Langage de programmation** : PAL (Gao et al. 2022) et PoT (Chen et al. 2022) font générer au LLM du code exécuté par un interpréteur Python, découplant calcul et raisonnement. **APIs externes** : TALM (Parisi et al. 2022) génère des appels `|tool-call`/`tool input` et boucle par self-play ; Toolformer (Schick et al. 2023) apprend en auto-supervision, à partir de quelques démonstrations, à appeler calculatrice, Q&R, moteur de recherche, traduction et calendrier, en filtrant les appels selon qu'ils réduisent la perte de prédiction des tokens futurs.

## Ce que ça ajoute vs IBM
Là où le guide IBM présente le tool calling comme une capacité produit, Weng en expose la filiation de recherche (TALM → Toolformer) et le mécanisme d'apprentissage auto-supervisé sous-jacent.

## Sources primaires (citées par Weng)
- Mialon et al., *Augmented Language Models: a Survey* (2023)
- Gao et al., *PAL: Program-aided language models* (2022)
- Chen et al., *Program of Thoughts Prompting* (2022)
- Parisi et al., *TALM: Tool Augmented Language Models* (2022)
- Schick et al., *Toolformer* (2023)

## Voir aussi
- (base agents) [Tool calling](tool-calling.md) · [CodeAct, incluant PAL (hors-corpus)](codeact.md)
- (base prompting) [Prompt chaining](prompt-chaining.md)
- [post complet](../sources/lilian-weng/md/2023-03-15-prompt-engineering.md)
