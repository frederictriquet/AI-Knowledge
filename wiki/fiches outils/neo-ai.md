---
outil: "Neo-AI"
titre: "Neo-AI"
themes: [frameworks-outillage]
type: "CLI — assistant IA pour terminal Linux"
url: https://github.com/Vasco0x4/Neo-AI
modele_economique: "Open-source (BSD 3-Clause), gratuit — projet communautaire"
cout_llm: "🟢🔑 — mode local LM Studio = SANS clé, gratuit (🟢) ; mode cloud DigitalOcean = credentials requis (🔑). OpenAI/Anthropic accessibles UNIQUEMENT via la passerelle DigitalOcean"
objectifs: [generer-code]
famille: "Assistants IA pour terminal / shell"
eco_icones: "🔓"
cout_icones: "🟢🔑"
resume: "Assistant IA pour terminal Linux open-source (BSD-3, Python, par Vasco0x4) : exécute des commandes avec contexte + approbation, analyse système (logs, fichiers, santé), volet cybersécurité (scan réseau, CTF). LLM local (LM Studio) ou cloud (OpenAI/Claude). ⚠️ Beta, Linux"
---

# Neo-AI

**En une phrase** — assistant IA qui vit dans le terminal Linux : il comprend le contexte, exécute des commandes système (avec ton approbation), analyse le système et aide aux tâches CLI et cybersécurité. On l'invoque par `neo`.

## Type & intégration
**Outil CLI** pour Linux, écrit en **Python** (~96 %), avec une UI terminal (coloration syntaxique, historique). Nécessite Python 3.6+ et un émulateur compatible (GNOME Terminal, Konsole…). Capacités : **exécution intelligente de commandes** (interprétation + approbation utilisateur), **analyse système** (logs, inspection de fichiers, santé), multi-protocole (terminal, fichiers, réseau, sécurité), outils orientés **cybersécurité** (scan réseau, CTF).

## Modèle économique
**Open-source, licence BSD 3-Clause**, gratuit. Projet communautaire (auteur : Vasco0x4). Statut **beta**, en développement.

## Coût LLM
**🟢🔑** — pas de LLM embarqué ; deux modes (vérifié dans `config.yaml` / `src/ai_core.py`) :
- **Local** via **LM Studio** (serveur OpenAI-compatible `127.0.0.1:1234`, `api_key` vide) → **sans clé, gratuit** (🟢), tourne sur ta machine.
- **Cloud** via **DigitalOcean** (`agent_id` + `agent_key` requis) → credentials nécessaires (🔑). ⚠️ OpenAI/Anthropic ne sont accessibles **que via la passerelle DigitalOcean**, pas en clé OpenAI/Anthropic directe.

Coût réel = celui du backend choisi ; le mode local est gratuit (hors matériel).

## À quoi ça sert
Rendre le terminal plus intuitif : traduire l'intention en commandes, exécuter sous contrôle, diagnostiquer le système, assister sur des tâches d'administration et de sécurité. Compagnon généraliste du quotidien shell, avec un **système d'approbation des commandes** pour la sûreté.

## Notes / à creuser
- **Famille 11 (assistants terminal/shell)** : premier du genre ici. À distinguer de [AIDA (AI-Driven Security Assessment)](aida.md) (même auteur, mais agent de **pentest autonome** spécialisé, famille 10) : Neo-AI est un **compagnon terminal généraliste** interactif, AIDA un agent offensif de bout en bout. Distinct aussi des agents de codage ([Kilo Code](kilo-code.md)) — Neo-AI vise l'**administration/usage système**, pas le développement dans un projet.
- Voisins de catégorie : Warp AI, term_agent, arch-ai, termax, Gemini CLI (usage shell).
- ⚠️ Exécution de commandes système → garder le garde-fou d'approbation actif ; prudence avec un LLM cloud sur des commandes sensibles.
- Beta → fonctionnalités évolutives.

## Source
- Dépôt : https://github.com/Vasco0x4/Neo-AI · doc : github.com/Vasco0x4/Neo-AI/blob/master/docs/INSTALLATION.md
- Présentation : dev.to/vasco0x4_85 (« Neo-AI, your intelligent Linux terminal companion »)

*(vérifié le 2026-06-15 — README GitHub + recherche web)*
