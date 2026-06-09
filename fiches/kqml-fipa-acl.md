---
titre: "KQML & FIPA-ACL"
theme: protocoles-interop
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-communication
source_titre: "Qu’est-ce que la communication des agents d’IA ?"---

# KQML & FIPA-ACL

> Fiche du glossaire des patterns · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [13-ai-agent-communication](../sources/ibm-guide-agents-ia/md/13-ai-agent-communication.md), [47-chatdev-chatchain-agent-communication-watsonx-ai](../sources/ibm-guide-agents-ia/md/47-chatdev-chatchain-agent-communication-watsonx-ai.md)

**En une phrase** — les deux langages de communication d'agents (ACL) historiques qui ont normalisé les « actes de communication » (informer, demander, interroger) bien avant les LLM, et que la plupart des frameworks actuels ignorent au profit du langage naturel.

## Ce que dit le corpus
Le fichier 13 présente KQML (Knowledge Query and Manipulation Language) et FIPA-ACL (Foundation for Intelligent Physical Agents – Agent Communication Language) comme « les deux protocoles privilégiés pour la communication avec les agents ». La DARPA a développé KQML dans les années 1990, « posant les bases d'une communication entre agents bien avant que des agents d'IA intelligents ne soient mis au point ». Les développeurs de la FIPA ont poursuivi ce travail « peu de temps après, apportant des améliorations en matière de standardisation et de clarté sémantique ». Le fichier 47 précise que ces ACL définissent des « actes de communication » standard (par exemple, informer, demander, interroger) pour permettre un dialogue structuré dans des environnements dynamiques. Il note que ChatDev, lui, « n'utilise pas de protocole formel de communication d'agent » : ChatChain assure l'interopérabilité « grâce aux capacités naturelles du LLM », via des conventions optimisées par LLM plutôt que des ACL formels.

## Tradeoff / insight pour un senior
Le compromis est explicite dans le corpus : structure formelle et clarté sémantique des ACL historiques contre la souplesse du langage naturel optimisé par LLM. Les frameworks LLM modernes (ChatDev/ChatChain) abandonnent les ACL formels — gain de flexibilité, perte de garanties de format et de sémantique. À connaître pour situer le débat « protocoles standardisés » (un des défis cités au fichier 13).

## Source primaire
Citée (fichier 13, note 2) : *The Current context of Agent Communication Languages*, Labrou *et al*, Université du Maryland, mars 1999.

## Voir aussi
- [droidspeak](droidspeak.md)
