# BabyAGI

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [43-babyagi](../md/43-babyagi.md)

**En une phrase** — la boucle minimale de 2023 (Yohei Nakajima) à trois agents — exécution, création, priorisation — adossée à une mémoire vectorielle ; un « bac à sable éducatif » plus qu'un outil de production.

## Ce que dit le corpus
IBM présente BabyAGI comme un cadre d'agent autonome partagé par Yohei Nakajima en 2023, qui génère et exécute une séquence de tâches selon un objectif utilisateur. Il orchestre une boucle de création, d'exécution et de priorisation à l'aide d'un LLM (généralement GPT-4) et d'un magasin de mémoire vectorielle. L'implémentation standard est un script Python utilisant les modèles GPT via API, une base vectorielle (typiquement Pinecone ; FAISS et Chroma dans des variantes) et LangChain pour structurer les rôles. La boucle en trois étapes : l'agent d'exécution exécute une tâche avec le contexte de la base ; l'agent de création génère des tâches de suivi à partir du résultat ; l'agent de priorisation réordonne la file selon dépendances et pertinence, jusqu'à épuisement ou condition d'arrêt. Le corpus qualifie BabyAGI de bac à sable éducatif plutôt que d'application de production, et précise qu'il n'est pas une IAG. En 2024, Nakajima a lancé BabyAGI 2, variante expérimentale utilisant un cadre *functionz* pour stocker fonctions et métadonnées en base.

## Tradeoff / insight pour un senior
Souvent comparé à AutoGPT : BabyAGI exécute une boucle compacte (création/exécution/priorisation + mémoire vectorielle), tandis qu'AutoGPT offre un cadre plus riche en intégration d'outils et passe mieux à l'échelle. BabyAGI reste un outil de recherche : sa lisibilité pédagogique est sa vraie valeur.

## Source primaire
Non citée formellement par IBM ; attribuée à Yohei Nakajima (2023). Voir le dépôt GitHub BabyAGI (hors-corpus).

## Voir aussi
- [autogpt](autogpt.md)
- [taxonomie-5-types-agents](taxonomie-5-types-agents.md)
