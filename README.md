# Corpus IA — agents & prompt engineering

Base de connaissances condensée et **sourcée** sur l'IA agentique et le prompt engineering, bâtie à partir des hubs **IBM Think** puis enrichie de sources externes de référence (Lilian Weng, Anthropic, Hamel Husain, Eugene Yan, Simon Willison, The Prompt Report, DeepSeek, OWASP/NIST/MITRE…).

## À quoi ça sert

1. **Monter en compétences** — une fiche par concept, dense, avec le lien vers la source primaire pour approfondir.
2. **Produire des posts courts** (messagerie interne) — chaque fiche tient en une accroche (« En une phrase ») + un lien « pour approfondir ».
3. **Affirmer une expertise** (LinkedIn) — même matière, format public.

## Par où commencer

- **[INDEX-THEMATIQUE.md](INDEX-THEMATIQUE.md)** — le point d'entrée : les 158 fiches rangées par **thème** (tous corpus confondus), avec niveau, provenance et lien source. ⚙️ généré.
- **[RAPPORT-CORPUS.md](RAPPORT-CORPUS.md)** — état du corpus : couverture par thème, fiches sans source, doublons. ⚙️ généré.

## Structure

```
fiches/      158 fiches à plat — la base de connaissances. Structure portée par le frontmatter.
sources/     matériaux bruts qui ont produit les fiches :
             ├ ibm-guide-agents-ia/, ibm-guide-prompt-engineering/  (pages md + html des hubs IBM)
             ├ lilian-weng/, hamel-husain/, …                       (md + README par source externe)
             └ SOURCES-PRIMAIRES.md, SOURCES-COMPLEMENTAIRES.md, METHODOLOGIE-IBM-THINK.md
tools/       build_index.py (génère les 2 index) · classification-themes.md (table de travail)
```

## Anatomie d'une fiche

Chaque fiche `fiches/<slug>.md` commence par un **frontmatter** qui porte toute la structure :

```yaml
---
titre: ReAct
theme: raisonnement-planification      # une des 14 catégories (voir INDEX-THEMATIQUE)
niveau: 🟢                             # 🔴 substance · 🟡 tradeoff · 🟢 survol
source_url: https://www.ibm.com/fr-fr/think/topics/react-agent
source_titre: "Qu'est-ce qu'un agent ReAct ? — IBM Think"
source_primaire: "Yao et al. (arXiv:2210.03629)"   # optionnel : papier d'origine
---
```

Suit le corps : **En une phrase** (l'accroche pour un post) · ce que dit la source · tradeoff/insight · source primaire · voir aussi.

## Ajouter ou mettre à jour une fiche

1. Créer/éditer `fiches/<slug>.md` avec le frontmatter ci-dessus (le `source_url` est **obligatoire**).
2. Régénérer les index :

```bash
python3 tools/build_index.py
```

Le rapport signale toute fiche sans `source_url`, les thèmes peu couverts et les doublons de titre.

## Les 14 thèmes

Fondamentaux des agents · Raisonnement & planification · Prompting · Outils & function-calling · RAG & contexte · Mémoire · Multi-agents · Protocoles & interopérabilité · Frameworks & outillage · Évaluation · Benchmarks · Sécurité · Efficacité & coût · Gouvernance, alignement & ops.
