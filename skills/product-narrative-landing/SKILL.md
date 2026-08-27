---
name: product-narrative-landing
description: "Build or reshape product landing pages for desktop, AI, privacy, and developer tools when the page must explain value, evidence, and trust clearly."
---

# Product Narrative Landing

Use this skill when a product website needs a strong narrative, a product-shaped hero, and transparent boundaries. It is especially useful for software whose value depends on workflow, privacy, reliability, or model choice. Do not use it to force this structure onto ecommerce catalogs, dashboards, or content-only sites.

## Outcome

Produce a coherent landing page plan or implementation with:

- one primary product promise and one primary CTA;
- a section map where each section makes one claim and supports it with evidence;
- a visual system built from role-based tokens rather than scattered one-off values;
- a responsive, accessible interactive product demo when a product UI is central to the story;
- explicit capability boundaries, data-flow explanations, and release state labels.

## Workflow

1. Extract the product truth before writing copy. Separate shipped, beta, planned, and unverified capabilities. Record what the product explicitly does not do.
2. Write the information architecture as a sequence of claims: hero/demo, core outcome, evidence or measurement, transformation example, trust/data flow, terminology or workflow detail, plans or deployment modes, compatibility, changelog, and final CTA. Omit sections that have no real evidence.
3. Make the hero demonstrative. Prefer semantic HTML, CSS, and SVG for a product-shaped mockup. Model the demo as a finite state machine with named scenes and predictable transitions; expose pause, replay, and sound controls when motion or audio is present. Provide a static first frame and a reduced-motion path.
4. Apply the visual rules in [references/design-system.md](references/design-system.md). Keep the grid, surface colors, typography, border language, and spacing consistent across sections. Use viewport-height chapters only when they improve reading rhythm and do not hide content on short screens.
5. Make trust concrete. Explain where audio, text, credentials, history, or telemetry go; distinguish local processing, user-supplied providers, and hosted services; state retention or failure behavior when relevant.
6. Implement semantic structure: one meaningful h1, ordered headings, labeled regions, keyboard-operable tabs and controls, real links for CTA actions, and visible focus states. Do not make the demo the only way to understand the product.
7. Validate at a desktop and a mobile viewport. Check overflow, sticky navigation, section anchors, demo controls, reduced motion, link targets, and whether the primary CTA remains obvious without animation.

## Copy and implementation guardrails

- Never invent prices, release dates, benchmarks, compatibility, or security guarantees. Mark unknowns as unknown or planned.
- Use concise outcome-led headings; reserve monospace styling for commands, paths, model names, versions, or other technical tokens.
- Keep marketing claims subordinate to the product truth. If a claim cannot be tied to a product behavior, test, release note, or explicit source, rewrite or remove it.
- Reuse arrays/configuration for repeated cards, scenes, and release items so the page can evolve without duplicated markup.
