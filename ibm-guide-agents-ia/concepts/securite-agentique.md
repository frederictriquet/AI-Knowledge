# Sécurité agentique

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🔴 substance · Provenance ✅ présent · Sources corpus : [62-ai-agent-security](../md/62-ai-agent-security.md)

**En une phrase** — la surface d'attaque d'un agent (décision autonome + appel d'outils) est bien plus large que celle d'un LLM seul, et appelle des contre-mesures de type Zero Trust, moindre privilège et sandbox.

## Ce que dit le corpus
Le fichier 62 décrit une surface d'attaque « à deux volets » : manipuler le comportement de l'agent, ou attaquer l'outil lui-même (ex. injection SQL). Le panorama des menaces : surface élargie, actions autonomes rapides, inférence imprévisible (probabiliste, donc non prédictible), manque de transparence. Vulnérabilités listées : **injection de prompt** directe et **indirecte** (prompt malveillant caché dans la source de données, déclenché à l'appel — agents multimodaux particulièrement exposés), **manipulation d'outils et d'API**, **empoisonnement des données**, **empoisonnement de la mémoire** (corruption de la mémoire persistante pour façonner le comportement ultérieur), **compromission des privilèges**, **usurpation d'authentification**, **RCE**, **échecs en cascade** (la sortie d'un agent compromis dégrade le suivant jusqu'à panne du système). Le **slopsquatting** (mot-valise « IA slop » + « typosquatting ») : enregistrer un nom de bibliothèque proche d'une légitime pour que le modèle extraie du code de la fausse lib — exploitation de la chaîne d'approvisionnement. Contre-mesures : **Zero Trust** (ne jamais faire confiance, toujours vérifier), **moindre privilège** (RBAC/ABAC), authentification contextuelle, chiffrement (AES-256), microsegmentation et **sandbox** pour l'exécution de code, durcissement et validation des prompts, entraînement contradictoire (encore immature).

## Tradeoff / insight pour un senior
La taxonomie recoupe l'OWASP Top 10 for LLM/Agentic (injection de prompt, fuite, supply-chain), non cité par IBM. Le point non trivial : l'inférence probabiliste rend la défense différente de la cybersécurité classique — on ne peut pas énumérer les comportements, d'où l'importance des contrôles d'exécution (sandbox, moindre privilège) plutôt que de la seule validation d'entrée.

## Source primaire
Non citée par IBM — aucune référence académique ; taxonomie proche de l'OWASP Top 10 for LLM Applications (hors-corpus).

## Voir aussi
- [guardrail-noeud-entree](guardrail-noeud-entree.md)
- [ethique-gouvernance](ethique-gouvernance.md)
