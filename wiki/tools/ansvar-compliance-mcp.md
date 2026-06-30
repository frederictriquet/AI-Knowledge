---
tool: "Ansvar Compliance MCP (suite)"
title: "Ansvar Compliance MCP (suite)"
themes: [rag-context, governance-alignment-ops]
type: "Suite of MCP servers (regulatory / legal data sources)"
url: https://github.com/Ansvar-Systems
pricing_model: "Open-source connectors (Apache 2.0) self-hosted free + hosted Ansvar Gateway (Free 100 searches/day/seat; Premium €249/seat/month or €2490/year; Team/Company on quote). Vendor: Ansvar Systems AB (Sweden)"
llm_cost: "No LLM — verbatim retrieval of official text; BYO client (Claude, Cursor…)"
objectives: [production]
family: "Specialized knowledge & data sources (MCP servers)"
eco_icons: "🔓🎁"
llm_cost_icons: "🟢"
summary: "Suite of ~150 open-source MCP servers (Ansvar AI, Stockholm) exposing the *verbatim* text of regulations: EU (GDPR, AI Act, DORA, NIS2…), per-country law (UK, FR, DE…), data protection/cybersecurity/competition/finance by authority. Zero LLM summarization (client-side BYOK), Apache 2.0, self-host or Gateway (Free 100 requests/day/seat; Premium €249/seat/month). ⚠️ US scope removed (404)"
---

# Ansvar Compliance MCP (suite)

**In one sentence** — a family of ~150 open-source MCP servers (by **Ansvar AI**, Stockholm) that give AI agents *structured, verbatim* access to official regulatory and legal texts — you ask in natural language and get the **exact official text**, not an LLM-generated summary.

> This fiche covers the **whole suite**. The best-known entry point is `EU_compliance_MCP` (the first recorded), but the org actually publishes around a hundred analogous servers.

## Type & integration
**MCP servers** (read-only) queryable from Claude Code, Claude Desktop, Cursor, Cline, and any MCP-compatible client. Two data architectures depending on the server:
- **Embedded database** (SQLite FTS5) holding the verbatim text (e.g. the EU one, based on EUR-Lex), with daily freshness checks.
- **Live government APIs** for some scopes (e.g. the US scope relied on eCFR.gov, California LegInfo, regulations.gov).

Common principle: **zero LLM summary / paraphrase**, serving citable official text. Mostly written in TypeScript. GitHub org: `Ansvar-Systems` (**150 public repos**), vendor **Ansvar AI** (ansvar.eu — "cited answers for compliance, legal, and security teams").

## Coverage (catalogue excerpts)
- **EU — `EU_compliance_MCP`** (flagship): ~49–61 regulations (GDPR, **AI Act**, DORA, NIS2, MiFID II, eIDAS, MDR, Chips Act…), thousands of articles/recitals/definitions + **ISO 27001 / NIST CSF** mappings.
- **National law by country**: UK (`UK-law-mcp`, 3,243 acts), Luxembourg (4,551), Ireland (3,972), France (Civil/Criminal/Labor Codes), Germany, Italy, Spain, Netherlands, Sweden, Finland, Denmark, etc.
- **Data protection by authority**: CNIL-like per country — ICO (UK), AEPD (ES), Garante (IT), BfDI/BfD (DE), CNPD, IMY (SE), DPC (IE), FDPIC (CH)…
- **Cybersecurity by authority**: BSI (DE), NCSC (UK/IE/FI), CCN-CERT (ES), MSB (SE), CIRCL (LU)…
- **Competition**, **financial regulation** (BaFin, CNMV, FI, MFSA…) and **energy** by country.

## Pricing model
- **Open-source MCP connectors, Apache 2.0 license** (a few repos under `NOASSERTION`) — self-hosting free. Gateway + licensed data = proprietary.
- **Ansvar Gateway** (hosted, 100% EU/Hetzner, OAuth): **Free €0 = 100 searches/day per seat** (concurrency 1, B2B account + VAT required); **Premium €249/seat/month** (or €2490/year, ~5000 searches/day/seat); **Team/Company** on quote (waitlist). Advisory from €2000.
- Free tier = **100 requests/day per seat** (verified on ansvar.eu/limits).

## LLM cost
**No LLM** 🟢 — no inference: the servers retrieve and present the official text. You bring your client (BYO Claude/Cursor subscription); the LLM cost is that client's, not the servers'. The value = **fidelity** (exact, citable text), not generation.

## What it's for
An "AI-readable" compliance/legal reference for anyone building products for European markets (and beyond): searching, cross-referencing and citing regulations directly inside the agent. Mappings to frameworks (ISO/NIST), audit artifacts, sector-based applicability rules.

## Notes
- **Family 8 (knowledge sources via MCP)**: the archetype of the category. A technical cousin of [Polaris (polarismcp.com)](polaris.md)/[Cavemem](cavemem.md) (SQLite FTS5 + local MCP) but on **business domains** (law/regulation) instead of code.
- ⚠️ **Vendor disclaimer**: the *control mappings* are "interpretive aids, not official guidance" — verify against official sources, consult a lawyer. An aid tool, **not legal advice**.
- ⚠️ **US scope removed**: `US_Compliance_MCP` and `US-law-mcp` (HIPAA, CCPA, GLBA, FERPA, COPPA, SOX, FDA 21 CFR Part 11) are referenced by search engines but return **HTTP 404** (deleted/renamed/private as of 2026-06-15). Watch if they reappear.
- Catalogue growing fast (150 repos, many pushed in June 2026) — coverage is evolving.

## Source
- GitHub org: https://github.com/Ansvar-Systems (150 public repos) · flagship: https://github.com/Ansvar-Systems/EU_compliance_MCP · npm: `@ansvar/eu-regulations-mcp`
- Vendor: https://ansvar.eu/ (Ansvar AI, Stockholm)
- MCP directories: mcpservers.org, lobehub, pulsemcp

*(verified on 2026-06-15 — org's GitHub API [150 public repos confirmed] + EU README + web search; US scope confirmed 404 via GitHub API)*
