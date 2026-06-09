---
titre: "MemGPT (Letta)"
theme: memoire
niveau: 🔴
provenance: ➕
base: ibm-guide-agents-ia/hors-corpus
source_url: https://arxiv.org/abs/2310.08560
---

# MemGPT (Letta)

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. Glossaire · Pertinence 🔴 substance

**En une phrase** — gérer la mémoire d'un LLM comme un système d'exploitation : pagination entre un contexte « RAM » limité et un stockage externe « disque », le modèle décidant lui-même quoi charger.

## L'idée
La fenêtre de contexte est traitée comme une mémoire principale bornée. MemGPT donne au LLM des **fonctions** pour déplacer l'information entre ce contexte et un store externe (historique, faits, documents), gérer l'éviction et relire à la demande — comme la pagination mémoire d'un OS. Résultat : conversations et documents de taille effectivement illimitée, avec une mémoire persistante entre sessions.

## Tradeoff / quand l'utiliser
La bonne référence si tu construis de la **mémoire long-terme sérieuse** (assistants persistants, agents au long cours) plutôt qu'un simple RAG. Coût : latence et appels supplémentaires pour les opérations mémoire, complexité de la gestion d'état. Le projet est devenu **Letta**.

## Source primaire
Packer et al., 2023, *MemGPT: Towards LLMs as Operating Systems*, arXiv:2310.08560 (UC Berkeley). *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [memoire-court-long-terme](memoire-court-long-terme.md) (corpus)
- [memoire-episodique-semantique-procedurale](memoire-episodique-semantique-procedurale.md) (corpus)
