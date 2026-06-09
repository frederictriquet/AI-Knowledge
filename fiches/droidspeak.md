---
titre: "DroidSpeak"
theme: multi-agents
niveau: 🔴
provenance: ✅
base: ibm-guide-agents-ia
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-communication
source_titre: "Qu’est-ce que la communication des agents d’IA ?"
---

# DroidSpeak

> Fiche du glossaire des patterns · Pertinence 🔴 substance · Provenance ✅ présent · Sources corpus : [13-ai-agent-communication](../sources/ibm-guide-agents-ia/md/13-ai-agent-communication.md)

**En une phrase** — au lieu de faire dialoguer deux LLM en texte, on partage directement le cache KV entre eux pour accélérer la communication inter-agents, avec une perte de précision annoncée comme minimale.

## Ce que dit le corpus
Le fichier 13 mentionne DroidSpeak dans la section « Communication d'agent à agent », parmi les recherches sur des « modes de communication d'agent à agent plus efficaces ». Le corpus la décrit comme « la solution "DroidSpeak" de Microsoft, qui vise à permettre aux agents de communiquer plus rapidement avec une perte de précision minimale ». La fiche s'inscrit dans le constat général du fichier : « lorsque les agents ont la capacité de communiquer entre eux, un système agentique devient plus que la somme de ses parties », mais la latence reste un défi (communication en temps réel ralentie par le réseau et les contraintes de calcul).

## Tradeoff / insight pour un senior
La pépite technique : DroidSpeak court-circuite la sérialisation en langage naturel en partageant le cache KV (les états d'attention déjà calculés) entre LLM distincts. C'est un échange latence/précision — on gagne en vitesse de communication contre une dégradation jugée minimale. Le mécanisme suppose des modèles compatibles (architectures proches) pour que le cache d'un LLM soit réutilisable par un autre. Le titre exact de la source (« Cross-LLM Communication and Multi-LLM Serving ») indique aussi un enjeu de mutualisation de service multi-LLM, pas seulement d'inter-agents.

## Source primaire
Citée par titre (fichier 13, note 1) : *Droidspeak: KV Cache Sharing for Cross-LLM Communication and Multi-LLM Serving*, Liu *et al*, Université de Chicago, Microsoft, 19 décembre 2024.

## Voir aussi
- [kqml-fipa-acl](kqml-fipa-acl.md)
