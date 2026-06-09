---
titre: "Microsoft 365 Copilot : de l'injection à l'exfiltration d'e-mails"
theme: securite
niveau: 🔴
source_url: https://embracethered.com/blog/posts/2024/m365-copilot-prompt-injection-tool-invocation-and-data-exfil-using-ascii-smuggling/
source_titre: "Microsoft Copilot: From Prompt Injection to Exfiltration of Personal Information"
---

# Microsoft 365 Copilot : de l'injection à l'exfiltration d'e-mails

**En une phrase** — Une chaîne d'exploitation complète sur M365 Copilot, amorcée par une simple prompt injection dans un e-mail, qui vole les e-mails et données personnelles de la victime.

## Ce que dit la source
Rehberger décrit (divulgué à MSRC en janvier-février 2024) un exploit combinant plusieurs techniques. (1) **Prompt injection** via un e-mail malveillant ou un document partagé, qui prend le contrôle de Copilot (démo « Microsoft Defender for Copirate »). (2) **Automatic Tool Invocation** : le payload ordonne à Copilot de chercher d'autres e-mails — par exemple des codes MFA Slack — sans human in the loop, amenant des PII dans le contexte sans consentement. (3) **ASCII Smuggling** : Copilot encode les données volées en Unicode Tags invisibles, embarqués dans un lien hypertexte cliquable vers un domaine attaquant (`wuzzi.net`). (4) Quand l'utilisateur clique, les données partent vers le serveur, puis sont décodées avec l'ASCII Smuggler. Le payload inclut même un **exemple d'in-context learning** apprenant à Copilot comment encoder le corps de l'e-mail en Unicode Tags. Le mailto: peut servir de variante. Microsoft a corrigé (les liens ne sont plus rendus), mais la prompt injection elle-même reste possible.

## Pourquoi c'est utile
Cette kill chain réelle, divulguée de façon responsable, montre comment trois primitives anodines se composent en vol de données d'entreprise.

## Points clés
- Mécanisme : injection → invocation automatique d'outils → staging ASCII smuggling → exfiltration par clic sur lien.
- Vecteur : e-mail, SharePoint/OneDrive, ou récupération RAG comme angle d'injection.
- Aggravation : in-context learning dans le payload pour fiabiliser l'encodage Unicode par le LLM.
- Mitigation (recommandations de l'auteur) : ne pas interpréter/rendre les Unicode Tags, ne pas invoquer d'outils automatiquement, idéalement ne pas rendre de liens cliquables.

## Voir aussi
- [Sécurité agentique](securite-agentique.md)
- [Injection de prompt](prompt-injection.md)
- [Injection : pourquoi c'est grave](injection-pourquoi-cest-grave.md)
- [MITRE ATLAS](mitre-atlas.md)
- [post complet](../sources/embrace-the-red/md/m365-copilot-exfil.md)
