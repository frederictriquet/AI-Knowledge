# How Claude remembers your project (CLAUDE.md & auto memory)

Source : https://code.claude.com/docs/en/memory — archivé le 2026-06-23.

## Extrait clé (CLAUDE.md vs auto memory)

> Each Claude Code session begins with a fresh context window. Two mechanisms carry knowledge across sessions:
> - **CLAUDE.md files**: instructions you write to give Claude persistent context
> - **Auto memory**: notes Claude writes itself based on your corrections and preferences

> Claude Code has two complementary memory systems. **Both are loaded at the start of every conversation. Claude treats them as context, not enforced configuration. To block an action regardless of what Claude decides, use a [PreToolUse hook] instead.** The more specific and concise your instructions, the more consistently Claude follows them.

## Quoi mettre dans CLAUDE.md

> Treat CLAUDE.md as the place you write down what you'd otherwise re-explain. Add to it when:
> - Claude makes the same mistake a second time
> - A code review catches something Claude should have known about this codebase
> - You type the same correction or clarification into chat that you typed last session
> - A new teammate would need the same context to be productive

> CLAUDE.md files are loaded into the context window at the start of every session, consuming tokens alongside your conversation. (…) Because they're context rather than enforced configuration, how you write instructions affects how reliably Claude follows them.

> **Size**: target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence.

## AGENTS.md

> Claude Code reads `CLAUDE.md`, not `AGENTS.md`. If your repository already uses `AGENTS.md` for other coding agents, create a `CLAUDE.md` that imports it (`@AGENTS.md`) so both tools read the same instructions without duplicating them.

## Pourquoi CLAUDE.md n'est pas une garantie

> CLAUDE.md content is delivered as a user message after the system prompt, not as part of the system prompt itself. Claude reads it and tries to follow it, but there's no guarantee of strict compliance, especially for vague or conflicting instructions.

> If the instruction is something that must run at a specific point, such as before every commit or after each file edit, write it as a **hook** instead. Hooks execute as shell commands at fixed lifecycle events and apply regardless of what Claude decides to do.

> Settings rules are enforced by the client regardless of what Claude decides to do. CLAUDE.md instructions shape Claude's behavior but are not a hard enforcement layer.
