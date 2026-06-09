# Embrace The Red — Johann Rehberger

Ingestion du blog sécurité [Embrace The Red](https://embracethered.com/blog/) de Johann Rehberger,
axée sur la sécurité offensive des LLM et agents IA (prompt injection, exfiltration, ASCII smuggling).

## Posts ingérés

| Slug | Titre | Année | Mots | URL |
|------|-------|-------|------|-----|
| `ai-injections-basics` | AI Injections: Direct and Indirect Prompt Injections and Their Implications | 2023 | 1710 | https://embracethered.com/blog/posts/2023/ai-injections-direct-and-indirect-prompt-injection-basics/ |
| `unicode-tags-smuggling` | Hiding and Finding Text with Unicode Tags (ASCII Smuggler) | 2024 | 581 | https://embracethered.com/blog/posts/2024/hiding-and-finding-text-with-unicode-tags/ |
| `m365-copilot-exfil` | Microsoft Copilot: From Prompt Injection to Exfiltration of Personal Information | 2024 | 1617 | https://embracethered.com/blog/posts/2024/m365-copilot-prompt-injection-tool-invocation-and-data-exfil-using-ascii-smuggling/ |

## Fiches

- [Injections IA : prompt injection directe et indirecte](concepts/ai-injections-basics.md)
- [ASCII Smuggling : cacher des instructions via les Unicode Tags](concepts/unicode-tags-smuggling.md)
- [Microsoft 365 Copilot : de l'injection à l'exfiltration d'e-mails](concepts/m365-copilot-exfil.md)

## Structure

- `html/` — pages brutes téléchargées (curl)
- `md/` — extractions markdown (extract_generic.py)
- `concepts/` — fiches de synthèse en français
