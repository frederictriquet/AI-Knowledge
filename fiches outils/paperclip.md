---
outil: "Paperclip"
titre: "Paperclip"
type: "Plateforme open-source d'orchestration et de gouvernance d'agents IA (« zero-human companies »)"
url: https://github.com/paperclipai/paperclip
modele_economique: "Open-source (MIT), auto-hébergé, gratuit — pas de compte ni d'offre payante ; tu fournis tes propres agents/clés"
cout_llm: "Aucun coût LLM propre (🟢) — « Bring Your Own Agent » : orchestre tes agents existants (Claude Code, Codex, Cursor…) qui portent leur propre auth ; Paperclip ne prend pas de clé LLM. Suivi de budget par agent"
---

# Paperclip

**En une phrase** — Plateforme open-source qui modélise une équipe d'agents IA comme une entreprise (organigramme, rôles, budgets, gouvernance par approbation) pour faire tourner des « zero-human companies » sous contrôle humain.

## Type & intégration
Plateforme d'orchestration multi-agents auto-hébergée (Node.js 20+ / React / PostgreSQL, ~98 % TypeScript). « Agent-agnostique » : elle ne fournit pas le modèle, elle coordonne des agents externes (Claude Code, OpenAI Codex, Google Gemini, Cursor, etc.) autour d'un organigramme commun, de buts partagés, de tickets/issues et de heartbeats planifiés. Multi-tenant (isolation par « company »).

## Modèle économique
Projet open-source sous licence MIT, gratuit et auto-hébergé. Aucun compte Paperclip requis, aucune offre payante annoncée à ce jour : le contrôle et les coûts restent côté utilisateur. Site officiel : https://paperclip.ing — dépôt canonique : https://github.com/paperclipai/paperclip.

## Coût LLM
**Aucun coût LLM propre** 🟢 — « **Bring Your Own Agent** » (vérifié README) : Paperclip ne revend ni n'intègre de LLM ; il **pilote tes agents existants** (Claude Code, Codex, Cursor, OpenClaw…), qui portent **leur propre auth/abonnement**. Paperclip ne demande **pas de clé LLM** — même logique que les orchestrateurs [Superset (superset-sh)](superset.md) / [Multica](multica.md) (et non un BYOK direct). Le contrôle des coûts se fait par **budget mensuel par agent** (avertissement à 80 %, blocage/auto-pause à 100 %), avec suivi des tokens/coûts par entreprise, agent, projet, but, issue, provider et modèle. *(Correction : précédemment marqué 🔑, à tort — vérifié le 2026-06-16.)*

## À quoi ça sert
Faire fonctionner des entreprises d'agents IA quasi autonomes tout en gardant l'humain comme « conseil d'administration ». Cœur produit : organigrammes et rôles hiérarchiques, alignement sur des objectifs, suivi de travail par tickets (checkout atomique pour éviter les doublons), heartbeats récurrents, et surtout une couche de gouvernance — plafonds budgétaires durs, portes d'approbation (un agent ne peut pas en « recruter » un autre ni exécuter une stratégie sans validation), cycle de vie des agents (pause/reprise/arrêt) et journal d'audit append-only.

## Notes / à creuser
- Nom très homonyme : à ne pas confondre avec le gestionnaire de presse-papier « Paperclip », le gem Rails ActiveStorage `paperclip`, etc. L'identité visée ici est bien la plateforme d'agents IA pour opérations business (vérifié).
- Sur les étoiles : le comparatif Liza cite « ~14k★ … 14k stars in days » (instantané au lancement). Le dépôt canonique `paperclipai/paperclip` affiche désormais bien plus (≈70k★ relevés le 2026-06-15), signe d'une traction très rapide. Un dépôt `agencyenterprise/paperclip-ai` existe aussi (≈3★) — probablement origine/miroir de l'éditeur (Agency Enterprise / Ry Walker).
- Positionnement « narratif » concurrent de [Liza](liza.md) : Paperclip = « zero-human companies » (opérations business) vs Liza = « sessions d'agents zero-trust » (ingénierie logicielle). Recouvrement fonctionnel direct faible mais frontale sur le récit. Voir aussi [MindFlight Orchestrator (MFO)](mindflight-orchestrator.md) côté automatisation d'entreprise.

## Source
- https://github.com/paperclipai/paperclip *(vérifié le 2026-06-15)*
- https://paperclip.ing/ *(vérifié le 2026-06-15)*
- https://github.com/agencyenterprise/paperclip-ai *(vérifié le 2026-06-15)*
- Comparatif Liza — specs/architecture/competition-survey/mas-survey.md *(vérifié le 2026-06-15)*
