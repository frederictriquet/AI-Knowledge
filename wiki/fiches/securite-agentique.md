---
titre: "Sécurité agentique"
type: "Concept"
theme: securite
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-security
source_titre: "Qu’est-ce que la sécurité des agents IA ?"
---

# Sécurité agentique

**En une phrase** — la surface d'attaque d'un agent (décision autonome + appel d'outils) est bien plus large que celle d'un LLM seul, et appelle des contre-mesures de type Zero Trust, moindre privilège et sandbox.

## En détail
La surface d'attaque d'un agent se décompose en deux volets : manipuler le comportement de l'agent, ou attaquer l'outil lui-même (ex. injection SQL). Le panorama des menaces : surface élargie, actions autonomes rapides, inférence imprévisible (probabiliste, donc non prédictible), manque de transparence. Vulnérabilités listées : **injection de prompt** directe et **indirecte** (prompt malveillant caché dans la source de données, déclenché à l'appel — agents multimodaux particulièrement exposés), **manipulation d'outils et d'API**, **empoisonnement des données**, **empoisonnement de la mémoire** (corruption de la mémoire persistante pour façonner le comportement ultérieur), **compromission des privilèges**, **usurpation d'authentification**, **RCE**, **échecs en cascade** (la sortie d'un agent compromis dégrade le suivant jusqu'à panne du système). Le **slopsquatting** (mot-valise « IA slop » + « typosquatting ») : enregistrer un nom de bibliothèque proche d'une légitime pour que le modèle extraie du code de la fausse lib — exploitation de la chaîne d'approvisionnement. Contre-mesures : **Zero Trust** (ne jamais faire confiance, toujours vérifier), **moindre privilège** (RBAC/ABAC), authentification contextuelle, chiffrement (AES-256), microsegmentation et **sandbox** pour l'exécution de code, durcissement et validation des prompts, entraînement contradictoire (encore immature).

## Exemple
Un agent de service client interagit avec un utilisateur puis se connecte à la base interne pour lire son historique d'achats : si ses privilèges ne sont pas révoqués après la tâche, un attaquant qui usurpe ses identifiants hérite de ces mêmes droits (lire des données sensibles, exécuter des transactions, s'octroyer plus d'autorisations) et progresse en mouvement latéral. Côté supply-chain, le slopsquatting illustre l'angle mort : un agent de codage extrait du code d'une fausse lib au nom proche d'une légitime, et l'injecte dans le livrable sans qu'aucune validation d'entrée ne le détecte.

## Tradeoff / insight pour un senior
La taxonomie recoupe l'OWASP Top 10 for LLM/Agentic (injection de prompt, fuite, supply-chain). Le point non trivial : l'inférence probabiliste rend la défense différente de la cybersécurité classique — on ne peut pas énumérer les comportements, d'où l'importance des contrôles d'exécution (sandbox, moindre privilège) plutôt que de la seule validation d'entrée.

## Source primaire
Aucune référence académique ; taxonomie proche de l'OWASP Top 10 for LLM Applications.

## Voir aussi
- [guardrail-noeud-entree](guardrail-noeud-entree.md)
- [ethique-gouvernance](ethique-gouvernance.md)
