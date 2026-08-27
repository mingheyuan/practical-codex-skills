---
name: product-copy-guardrails
description: "Write or review software product copy with evidence-backed claims, explicit release states, clear data boundaries, and terminology that survives technical scrutiny."
---

# Product Copy Guardrails

Use this skill when drafting a landing page, release note, product brief, or feature explanation for software, AI, developer tools, or privacy-sensitive products. It is for making claims trustworthy and comprehensible, not for inventing a more aggressive marketing angle.

## Workflow

1. Build a claim inventory from the supplied product behavior, source code, release notes, tests, or approved product brief. For every claim, record evidence, status (`shipped`, `beta`, `planned`, `unknown`), and risk if misunderstood.
2. Separate capabilities from boundaries. Write what the product does, what it does not do, what data it needs, where that data goes, and what happens on timeout or failure when those facts are available.
3. Treat numbers as conditional evidence. Keep the sample, baseline, measurement method, version, and date with a benchmark. If any part is missing, remove the number or label it as unverified.
4. Preserve exact technical tokens such as URLs, email addresses, paths, commands, versions, provider names, model names, and API terminology. Normalize casing only when the canonical spelling is known.
5. Write headings as user outcomes and body copy as short, concrete explanations. Use Chinese-friendly line lengths and avoid a pile-up of slogans, adjectives, and exclamation marks.
6. Mark lifecycle state near the capability. Do not make planned cloud services, future integrations, or pending prices sound available today.
7. Return the claim matrix, recommended copy, unresolved questions, and a short list of claims that were intentionally rejected.

## Guardrails

- Never invent prices, dates, customer counts, speed multipliers, security certifications, compatibility, or provider behavior.
- Avoid implying that an LLM reads screens, knows facts, executes tasks, or sends messages unless the product demonstrably does so and the copy says how.
- Avoid saying “private”, “secure”, “local”, or “encrypted” without specifying the relevant data, boundary, or storage behavior.
- Prefer “can”, “supports”, or “is designed to” when behavior depends on configuration. Use absolute language only when the source warrants it.
- When evidence conflicts, surface the conflict instead of silently choosing the most flattering statement.

Read [references/claim-matrix.md](references/claim-matrix.md) when the copy contains technical or quantitative claims.
