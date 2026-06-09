---
titre: "MacNet : passage à l'échelle multi-agents"
theme: multi-agents
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/topics/chatdev
source_titre: "Qu’est-ce que ChatDev ?"---

# MacNet : passage à l'échelle multi-agents

> Fiche du glossaire des patterns · Pertinence 🔴 substance · Provenance ✅ présent · Sources corpus : [46-chatdev](../sources/ibm-guide-agents-ia/md/46-chatdev.md)

**En une phrase** — l'extension de ChatDev qui structure plus de mille agents en graphe acyclique (DAG) et les fait raisonner dans l'ordre topologique, avec une loi de croissance de la qualité en fonction du nombre d'agents.

## Ce que dit le corpus
ChatDev met en œuvre un moyen de dimensionner la collaboration multi-agents basée sur un LLM avec les **réseaux de collaboration multi-agents (MacNet)**. MacNet s'inspire du principe de dimensionnement neuronal — augmenter le nombre de neurones fait émerger des capacités — et l'applique à l'augmentation du nombre d'agents. Concrètement, MacNet « utilise des graphiques acycliques pour structurer les agents et améliorer leur raisonnement interactif grâce à l'ordre topologique ». Les solutions sont dérivées des interactions des agents. Le corpus indique que ce processus surpasse systématiquement les modèles de référence, favorise une collaboration efficace sur différentes topologies de réseau et « permet la coopération entre plus d'un millier d'agents ». Grâce à cette application, ChatDev a identifié une **loi d'évolutivité collaborative** montrant que la qualité des solutions s'améliore selon un **modèle de croissance logistique** à mesure que le nombre d'agents augmente.

## Tradeoff / insight pour un senior
Insight réel : le DAG + ordre topologique transpose l'ordonnancement de dépendances (déjà connu des pipelines) à la collaboration LLM, ce qui rend le passage à l'échelle déterministe. La loi logistique implique des rendements décroissants — au-delà d'un certain nombre d'agents, le gain de qualité plafonne ; empiler des agents n'est pas gratuit indéfiniment.

## Source primaire
Décrit par IBM sans DOI dans le texte — voir l'article MacNet de l'équipe ChatDev/OpenBMB (hors-corpus pour la référence exacte).

## Voir aussi
- [chatdev-chatchain](chatdev-chatchain.md)
- [orchestration-types](orchestration-types.md)
