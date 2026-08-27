---
name: frontend-audit
description: "Audit a live website or local frontend for information architecture, visual language, interaction quality, accessibility, and responsive risks, with evidence-backed findings."
---

# Frontend Audit

Use this skill when the user asks to inspect, review, reverse-engineer, or improve an existing frontend. It is an analysis skill: do not modify implementation files unless the user separately asks for fixes.

## Audit method

1. Establish the surface. Record the URL or app entry point, title, viewport, authentication state if relevant, and whether the observation is from source, runtime DOM, or a screenshot.
2. Map the information architecture. List the primary regions, headings, repeated components, navigation anchors, primary CTA, and any content that appears only after interaction.
3. Inventory the visual system. Extract layout max-widths, spacing rhythm, type scale, surface colors, borders, radii, shadows, icon language, and responsive changes. Prefer a small token table over a long aesthetic description.
4. Exercise meaningful states. Check tabs, menus, carousels, accordions, forms, loading/empty/error states, autoplay, pause/replay, and keyboard focus where they exist. After each action, inspect the resulting visible state before continuing.
5. Check responsive behavior at a wide desktop and a narrow mobile viewport. Look for clipped text, unexpected fixed heights, horizontal overflow, inaccessible off-canvas menus, sticky headers covering anchors, and controls that become too small.
6. Check semantics and accessibility. Verify heading order, named regions, button/link distinction, tab relationships, labels, focus visibility, color contrast risks, alt text, and reduced-motion behavior. Report a risk when a runtime check is not possible instead of claiming pass.
7. Review trust and copy. Flag unsupported numbers, unclear status labels, hidden limitations, unexplained data flows, and claims that imply capability not demonstrated by the interface.

## Report format

Return:

- a short executive summary;
- an information-architecture map;
- a token and pattern inventory;
- a prioritized findings table with `priority`, `evidence`, `impact`, and `recommendation`;
- a responsive and interaction checklist;
- the top three changes that would improve comprehension or conversion.

Use `P0` for broken or blocked core flows, `P1` for major usability/accessibility or trust issues, and `P2` for polish or consistency issues. Separate observed facts from inference. Link to exact routes or selectors when available and attach screenshots only when they materially clarify the issue. Use [references/audit-checklist.md](references/audit-checklist.md) for the detailed checklist.
