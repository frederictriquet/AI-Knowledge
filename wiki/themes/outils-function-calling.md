---
type: index
titre: "Thème — Outils & function-calling"
theme: outils-function-calling
---

# 🔧 Outils & function-calling

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Donner des outils à un agent et soigner l'interface agent-ordinateur._

## Concepts (11)

### 🔴 Substance / cœur
- **[CodeAct (le code comme espace d'action)](../fiches/codeact.md)** — l'agent émet du **code Python exécutable** comme action, au lieu d'appels d'outils en JSON rigide.
- **[Computer-use & agents GUI](../fiches/computer-use-gui-agents.md)** — piloter un navigateur ou un OS comme un humain, via **captures d'écran** en entrée et **actions** (clic, frappe, défilement) en sortie.
- **[Le cadre canonique : Agent = LLM + Planification + Mémoire + Outils](../fiches/agent-architecture-canonique.md)** — la décomposition de référence d'un agent autonome : un LLM joue le rôle de cerveau (contrôleur), épaulé par trois composants — planification, mémoire et usage d'outils.
- **[Toolformer](../fiches/toolformer.md)** — un LLM *fine-tuné* pour décider seul quand et comment appeler un outil, sans exemples few-shot ni prompt d'orchestration.
- **[Voyager & bibliothèque de compétences](../fiches/voyager-skill-library.md)** — un agent à apprentissage continu qui **acquiert, stocke et réutilise** des compétences sous forme de code, se constituant une mémoire procédurale auto-construite.

### 🟡 Tradeoff / intermédiaire
- **[LLM Compiler (parallel function calling)](../fiches/llm-compiler.md)** — planifier un **DAG d'appels d'outils** et exécuter en parallèle ceux qui sont indépendants, au lieu de les enchaîner séquentiellement comme ReAct.
- **[LLM imbriqué dans un outil](../fiches/llm-dans-un-outil.md)** — un outil appelé par l'agent utilise lui-même un appel LLM en interne (ex. classifieur de pertinence yes/no).
- **[MRKL Systems](../fiches/mrkl.md)** — architecture de **routage** où un LLM aiguille chaque requête vers un ensemble de modules experts (symboliques : calculatrice, base de données, API ; ou neuronaux).
- **[ReAct vs function calling](../fiches/react-vs-function-calling.md)** — le function calling est plus rapide et économe sur des tâches prévisibles ; ReAct gère mieux l'imprévisible au prix des tokens de boucle de raisonnement.
- **[Tool grounding](../fiches/tool-grounding.md)** — donner à l'agent des outils qui exposent l'état légal vérifiable (ex. coups d'échecs légaux) pour l'empêcher d'halluciner ses décisions.

### 🟢 Survol / introductif
- **[Tool calling / function calling](../fiches/tool-calling.md)** — le modèle émet un appel structuré (JSON + tool_call_id) que ton code exécute, puis dont il réinjecte le résultat.

## Outils (6)

- **[Chrome DevTools MCP](../fiches%20outils/chrome-devtools-mcp.md)** — _Serveur MCP (automatisation navigateur)_
- **[Computer use (Anthropic / Claude)](../fiches%20outils/computer-use.md)** — _Capacité/outil de modèle (API Anthropic) + implémentation de référence open-source_
- **[Firefox DevTools MCP](../fiches%20outils/firefox-devtools-mcp.md)** — _Serveur MCP (automatisation / inspection navigateur)_
- **[Playwright MCP](../fiches%20outils/playwright-mcp.md)** — _Serveur MCP (automatisation navigateur)_
- **[Puppeteer MCP](../fiches%20outils/puppeteer-mcp.md)** — _Serveur MCP (automatisation navigateur)_
- **[Serena](../fiches%20outils/serena.md)** — _Serveur MCP / toolkit d'agent de codage_
