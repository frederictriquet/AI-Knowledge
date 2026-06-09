---
titre: "Attaques adversariales sur les LLM (taxonomie de Weng)"
theme: securite
niveau: 🔴
source_url: https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/
source_titre: "Adversarial Attacks on LLMs"
---

# Attaques adversariales sur les LLM (taxonomie de Weng)

**En une phrase** — la mécanique réelle des attaques : à poids gelés et à l'inférence, on distingue cinq familles d'attaques, séparées surtout par l'axe boîte blanche (accès au gradient) vs boîte noire (API seule).

## Ce que dit la source
Weng pose le threat model : l'attaque a lieu **à l'inférence**, poids fixes, et se divise en **boîte blanche** (accès complet aux poids, donc au gradient — seulement pour modèles open source) vs **boîte noire** (API entrée/sortie). Elle énumère cinq familles. **Manipulation de tokens** (boîte noire) : remplacer quelques tokens en gardant le sens — TextAttack (Morris et al. 2020), TextFooler (Jin et al. 2019), BERT-Attack (Li et al. 2020), qui ciblent d'abord les mots les plus importants. **Attaques par gradient** (boîte blanche) : GBDA (Guo et al. 2021) avec l'astuce Gumbel-Softmax, HotFlip (Ebrahimi et al. 2018), les Universal Adversarial Triggers (Wallace et al. 2019), et surtout Zou et al. (2023) avec la recherche **Greedy Coordinate Gradient (GCG)** produisant des suffixes adversariaux transférables vers des modèles commerciaux. **Jailbreak** (boîte noire, heuristique) : Wei et al. (2023) distinguent « objectifs concurrents » (prefix injection, refusal suppression, DAN) et « généralisation défaillante » (Base64, ROT13, payload splitting). **Red-teaming humain** et **red-teaming par modèle** (Perez et al. 2022) complètent la taxonomie.

## Pourquoi c'est utile
Weng fournit la profondeur mécaniste sur les attaques adversariales : gradient, GCG, Gumbel-Softmax, transférabilité, perplexité comme filtre défensif — au-delà de la simple catégorisation jailbreak/injection.

## Sources primaires (citées par Weng)
- Zou et al., *Universal and Transferable Adversarial Attacks on Aligned Language Models* (GCG, 2023)
- Wallace et al., *Universal Adversarial Triggers for Attacking and Analyzing NLP* (2019)
- Wei et al., *Jailbroken: How Does LLM Safety Training Fail?* (2023)
- Guo et al., *Gradient-based adversarial attacks against text transformers* (GBDA, 2021)
- Perez et al., *Red Teaming Language Models with Language Models* (2022)

## Voir aussi
- [Jailbreak](jailbreak.md) · [Injection de prompt](prompt-injection.md)
- [Sécurité agentique](securite-agentique.md)
- [post complet](../sources/lilian-weng/md/2023-10-25-adv-attack-llm.md)
