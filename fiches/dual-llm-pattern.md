---
titre: "Le Dual LLM pattern (source primaire)"
theme: securite
niveau: 🔴
source_url: https://simonwillison.net/2023/Apr/25/dual-llm-pattern/
source_titre: "The Dual LLM pattern for building AI assistants that can resist prompt injection"---

# Le Dual LLM pattern (source primaire)

> Fiche **source : Simon Willison** · [post complet](dual-llm-pattern.md) · Pertinence 🔴 substance

**En une phrase** — Architecture de défense : un Privileged LLM (avec outils et privilèges, ne voit JAMAIS le contenu non fiable) plus un Quarantined LLM (traite le contenu non fiable, sans privilèges) ; le privileged manipule des références symboliques, pas le texte non fiable.

## Ce que dit la source
Willison propose une paire d'instances : un **Privileged LLM**, cœur de l'assistant, qui reçoit l'entrée de sources de confiance (l'utilisateur) et a accès aux **tools** (envoyer un email, modifier l'agenda) via le pattern ReAct ; et un **Quarantined LLM**, utilisé dès qu'il faut traiter du contenu non fiable, sans accès aux outils et supposé pouvoir « partir en vrille » à tout moment. Règle cruciale : la sortie non filtrée du Quarantined LLM ne doit *jamais* être transmise au Privileged LLM. Un **Controller** (logiciel classique, pas un LLM) orchestre le tout et manipule des variables (`$VAR1`, `$VAR2`) : le Privileged LLM ne voit que ces noms de variables, jamais le contenu non fiable ni le résumé potentiellement « radioactif ». Willison souligne les limites : *social engineering* (copier-coller piégé), risques du *chaining*, et reconnaît que « this solution is pretty bad » — coûteuse en complexité et non fiable à 100 %. La mise à jour 2025 renvoie à CaMeL (Google DeepMind), qui corrige une faille de cette proposition.

## Ce que ça ajoute vs IBM
Willison est la source primaire : ce post de 2023 a introduit le Dual LLM pattern, repris ensuite par d'autres. La fiche IBM (dual-LLM & CaMeL) en est une version dérivée et plus tardive.

## À retenir
- Privileged LLM : outils + privilèges, jamais exposé au contenu non fiable.
- Quarantined LLM : contenu non fiable, aucun outil, considéré comme compromis.
- Controller (code, pas LLM) : passe des variables, jamais le texte brut.
- Sortie du Quarantined LLM = « radioactive », ne jamais la renvoyer au Privileged.
- Limites : social engineering, chaining ; pas fiable à 100 %. CaMeL va plus loin.

## Voir aussi
- (agents IBM, fiche dérivée) [dual-LLM & CaMeL](dual-llm-camel.md)
- (prompt-eng IBM) [Prévenir l'injection](prevent-prompt-injection.md)
- [lethal-trifecta](lethal-trifecta.md)
- [post complet](dual-llm-pattern.md)
