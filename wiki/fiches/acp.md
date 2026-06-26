---
titre: "ACP (Agent Communication Protocol)"
type: "Concept"
theme: protocoles-interop
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/agent-communication-protocol
source_titre: "Qu’est-ce que l’ACP (Agent Communication Protocol ) ?"
---

# ACP (Agent Communication Protocol)

**En une phrase** — le protocole agent↔agent de BeeAI/IBM, fondé sur REST/HTTP léger (vs JSON-RPC), asynchrone par défaut, avec découverte hors-ligne ; il a fusionné avec A2A sous la Linux Foundation.

## En détail
L'ACP est une norme ouverte de communication entre agents, introduite par BeeAI d'IBM et désormais sous la Linux Foundation. Composants : un client ACP et un serveur ACP ; le client envoie des requêtes via une API RESTful sur HTTP, et le serveur héberge un ou plusieurs agents derrière un point HTTP unique, routant les tâches. Fonctionnalités clés : **communication REST** (conventions HTTP standard, utilisable avec cURL, Postman ou un navigateur ; SDK disponible mais non requis), **découverte hors-ligne** (métadonnées intégrées aux paquets de distribution, adaptée aux environnements scale-to-zero ; découverte en ligne possible via manifestes à des URL bien connues), **asynchrone par défaut** (synchrone pris en charge) et acceptation de types de messages variés (audio, images, texte, vidéos, binaire). À noter : ACP s'oppose au MCP sur ce point — JSON-RPC plus complexe vs conception REST plus légère. Un tutoriel illustre un workflow multi-agents BeeAI + crewAI où ACP sert de couche de messagerie partagée (JSON + métadonnées) via l'`acp-sdk`.

## Exemple
Cas inter-organisations : un fabricant (agent de planification de production) doit chiffrer le délai de livraison d'un équipement sur mesure pour établir un devis ; il doit interroger l'agent d'un prestataire logistique (estimation de transit, disponibilité transporteurs). Sans ACP, il faut une intégration sur mesure entre les deux API, avec gestion manuelle de l'authentification et des formats — fragile et non réplicable. Avec ACP, chaque organisation enveloppe son agent d'une interface ACP : le fabricant envoie commande + destination, le logisticien renvoie options d'expédition et délais, sans exposer son fonctionnement interne. Côté code, un agent compatible se définit en décorant une fonction `@server.agent()` puis `server.run()`.

## Tradeoff / insight pour un senior
Conçu délibérément léger et neutre fournisseur : REST + async par défaut convient aux tâches longues et aux contextes inter-organisations décentralisés. La découverte hors-ligne (metadata dans le paquet) est le détail rare et utile : un agent reste découvrable même éteint. Point d'attention : ACP s'est associé à A2A sous la Linux Foundation — surveiller la convergence des SDK.

## Source primaire
Introduit par BeeAI d'IBM, site officiel agentcommunicationprotocol.dev, dépôt github.com/i-am-bee/acp.

## Voir aussi
- [beeai](beeai.md)
- [a2a](a2a.md)
