---
titre: "Types d'orchestration des agents IA"
theme: multi-agents
niveau: 🟡
provenance: ✅
base: ibm-guide-agents-ia
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-orchestration
source_titre: "Qu’est-ce que l’orchestration des agents IA ?"
---

# Types d'orchestration des agents IA

> Fiche du glossaire des patterns · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [23-ai-agent-orchestration](../sources/ibm-guide-agents-ia/md/23-ai-agent-orchestration.md)

**En une phrase** — quatre façons de répartir la prise de décision entre agents : un chef unique, un collectif sans chef, des couches hiérarchiques, ou des organisations qui collaborent sans se partager les données.

## Ce que dit le corpus
IBM distingue quatre types d'orchestration, souvent combinés dans les systèmes réels. L'**orchestration centralisée** repose sur un agent orchestrateur unique, le « cerveau » qui dirige les autres, attribue les tâches et prend les décisions finales ; elle garantit cohérence, contrôle et prévisibilité. L'**orchestration décentralisée** s'éloigne d'une entité dominante : les agents décident en toute indépendance ou par consensus, ce qui rend le système plus évolutif et plus résistant (aucune défaillance unique ne l'arrête). L'**orchestration hiérarchique** organise les agents en couches, comme une structure de commande à plusieurs niveaux où les agents supérieurs supervisent les inférieurs ; une hiérarchie trop rigide peut nuire à l'adaptabilité. L'**orchestration fédérée** porte sur la collaboration entre agents indépendants ou entreprises distinctes, leur permettant de travailler ensemble sans partager entièrement les données ni renoncer au contrôle de leurs systèmes.

## Tradeoff / insight pour un senior
Le seul type non trivial est le fédéré : il répond explicitement aux contraintes de confidentialité, de sécurité ou de réglementation (santé, banque, collaborations inter-entreprises) qui interdisent le partage illimité de données. Les autres recoupent des choix d'architecture distribuée classiques — point unique de défaillance vs résilience, contrôle vs autonomie.

## Source primaire
Non citée par IBM — la page expose la taxonomie sans référence académique (hors-corpus).

## Voir aussi
- [openai-swarm](openai-swarm.md)
- [crewai](crewai.md)
