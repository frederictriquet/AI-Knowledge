---
titre: "ASCII Smuggling : cacher des instructions via les Unicode Tags"
type: "Concept"
theme: securite
niveau: 🔴
source_url: https://embracethered.com/blog/posts/2024/hiding-and-finding-text-with-unicode-tags/
source_titre: "Hiding and Finding Text with Unicode Tags"
---

# ASCII Smuggling : cacher des instructions via les Unicode Tags

**En une phrase** — Un bloc de caractères Unicode (Tags Unicode Block) qui reflète l'ASCII reste invisible à l'humain dans l'UI, mais les LLM l'interprètent — d'où une prompt injection indétectable à l'œil.

## Ce que dit la source
Partant d'une découverte de Riley Goodside, Rehberger explique que le **Tags Unicode Block** mirroite l'ASCII et n'est généralement pas rendu par les interfaces ; selon le standard Unicode, une implémentation « tag-unaware » affiche ces caractères comme invisibles sans effet sur les caractères voisins. Or les tokenizers savent les traiter, sans doute parce que les données d'entraînement en contenaient. Le PoC initial montrait un texte anodin contenant des instructions invisibles forçant ChatGPT à invoquer DALL-E. Rehberger publie l'outil **ASCII Smuggler** pour encoder/décoder ces payloads et détecter du texte caché. Les implications dépassent l'injection : un LLM peut aussi *émettre* du texte invisible à l'utilisateur (staging d'exfiltration), et ces instructions peuvent vivre dans des sites, PDF, bases de données ou GPTs. Point crucial : la technique **contourne la mitigation « Human in the Loop »**, l'humain approuvant/transférant un texte dont il ne voit pas les instructions cachées.

## Pourquoi c'est utile
L'attaque est concrète, reproductible (outil fourni), et défait explicitement la mitigation humaine que beaucoup considèrent comme un garde-fou.

## Points clés
- Mécanisme : caractères du Tags Unicode Block (U+E0000…) invisibles à l'écran mais lus par le LLM.
- Vecteur : texte collé, site web, PDF, base, GPT — input *et* output du modèle.
- Impact : prompt injection cachée + smuggling de données « in plain sight » + contournement du Human in the Loop.
- Mitigation : filtrer/supprimer les Unicode Tags Code Points en entrée et en sortie de l'application.

## Voir aussi
- [Sécurité agentique](securite-agentique.md)
- [Injection de prompt](prompt-injection.md)
- [Injection : pourquoi c'est grave](injection-pourquoi-cest-grave.md)
- [MITRE ATLAS](mitre-atlas.md)
- [post complet](../sources/embrace-the-red/md/unicode-tags-smuggling.md)
