---
name: responsive-ui-qa
description: "Validate a web UI across desktop and mobile viewports, focusing on layout integrity, interaction states, accessibility, and actionable visual regressions."
---

# Responsive UI QA

Use this skill after a frontend is built or changed, when the user needs confidence that the interface works at multiple sizes. It complements unit tests by checking the rendered experience. Use the in-app browser skill for live page inspection when it is available.

## Test matrix

Start with the smallest useful matrix:

- desktop: `1280 × 720`;
- compact desktop/tablet: `1024 × 768` when the layout has a breakpoint near this range;
- mobile: `390 × 844`;
- tall mobile or tablet: `768 × 1024` only when the product has meaningful tablet behavior.

## Test loop

For each viewport:

1. Load a fresh state and record the URL and viewport.
2. Check the first frame: no horizontal overflow, no clipped text, the page has a visible primary action, and important content is not below an unnecessarily tall blank area.
3. Exercise the main route: open/close navigation, move through tabs or carousels, submit only safe test data, and verify the visible result after each action.
4. Scroll through every major section. Check sticky headers, anchor offsets, card grids, tables, media, code or model tokens, and footer columns.
5. Use keyboard navigation for the main controls. Confirm focus is visible, tab order is logical, and a tab or menu can be closed without a pointer.
6. Check reduced motion if the page animates. The useful content must remain available when autoplay is disabled or frozen.
7. Capture only the screenshots needed to explain a regression. Record the selector, viewport, expected behavior, actual behavior, and severity.

## Severity

- `P0`: core content or CTA is inaccessible, the page cannot load, or an interaction traps the user.
- `P1`: major content is clipped, a primary flow breaks at a supported size, or a key accessibility interaction is unavailable.
- `P2`: inconsistent spacing, minor wrapping, visual drift, or non-blocking polish issue.

Use [references/viewport-matrix.md](references/viewport-matrix.md) for the compact report template. Keep the working tree clean unless the user asked for fixes; this skill reports defects rather than silently rewriting the UI.
