# ASCII Smuggling : cacher des instructions via les Unicode Tags

> Fiche **source : Johann Rehberger (Embrace The Red)** · [post](../md/unicode-tags-smuggling.md) · Pertinence 🔴 substance

**En une phrase** — Un bloc de caractères Unicode (Tags Unicode Block) qui reflète l'ASCII reste invisible à l'humain dans l'UI, mais les LLM l'interprètent — d'où une prompt injection indétectable à l'œil.

## Ce que dit la source
Partant d'une découverte de Riley Goodside, Rehberger explique que le **Tags Unicode Block** mirroite l'ASCII et n'est généralement pas rendu par les interfaces ; selon le standard Unicode, une implémentation « tag-unaware » affiche ces caractères comme invisibles sans effet sur les caractères voisins. Or les tokenizers savent les traiter, sans doute parce que les données d'entraînement en contenaient. Le PoC initial montrait un texte anodin contenant des instructions invisibles forçant ChatGPT à invoquer DALL-E. Rehberger publie l'outil **ASCII Smuggler** pour encoder/décoder ces payloads et détecter du texte caché. Les implications dépassent l'injection : un LLM peut aussi *émettre* du texte invisible à l'utilisateur (staging d'exfiltration), et ces instructions peuvent vivre dans des sites, PDF, bases de données ou GPTs. Point crucial : la technique **contourne la mitigation « Human in the Loop »**, l'humain approuvant/transférant un texte dont il ne voit pas les instructions cachées.

## Ce que ça ajoute vs IBM
IBM reste générique sur la sécurité ; ici une attaque concrète, reproductible (outil fourni), qui défait explicitement la mitigation humaine que beaucoup considèrent comme un garde-fou.

## Points clés
- Mécanisme : caractères du Tags Unicode Block (U+E0000…) invisibles à l'écran mais lus par le LLM.
- Vecteur : texte collé, site web, PDF, base, GPT — input *et* output du modèle.
- Impact : prompt injection cachée + smuggling de données « in plain sight » + contournement du Human in the Loop.
- Mitigation : filtrer/supprimer les Unicode Tags Code Points en entrée et en sortie de l'application.

## Voir aussi
- (agents IBM) [Sécurité agentique](../../../ibm-guide-agents-ia/concepts/securite-agentique.md)
- (prompt-eng IBM) [Injection de prompt](../../../ibm-guide-prompt-engineering/concepts/prompt-injection.md)
- (Willison) [Injection : pourquoi c'est grave](../../simon-willison/concepts/injection-pourquoi-cest-grave.md)
- (security-references) [MITRE ATLAS](../../security-references/concepts/mitre-atlas.md)
- [post complet](../md/unicode-tags-smuggling.md)
