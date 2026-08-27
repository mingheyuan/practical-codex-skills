# Viewport matrix and report template

## Matrix

| Viewport | What it catches |
| --- | --- |
| 1280 × 720 | Wide layout, sticky navigation, one-screen hero rhythm, grid alignment |
| 1024 × 768 | Intermediate breakpoints, dense two-column sections, navigation pressure |
| 390 × 844 | Mobile wrapping, off-canvas navigation, touch targets, stacked cards |
| 768 × 1024 | Tablet-specific layout when the product supports it |

Do not treat these sizes as a promise that every product must support every device. Add the project's documented breakpoints and test the nearest boundary when the layout uses custom media queries.

## Report row

```text
Viewport: 390 × 844
Route: /
Area: Primary navigation
Priority: P1
Expected: The menu opens, exposes the four section links, and can be closed with keyboard focus.
Actual: The menu remains visually hidden after activation.
Evidence: screenshot or selector
Recommendation: keep menu state in one source of truth and expose aria-expanded/aria-controls.
```

## Quick checks

- `document.documentElement.scrollWidth` should not exceed `window.innerWidth` unless horizontal scrolling is intentional.
- A sticky header should not obscure the top of an anchor target.
- A card grid should have a deliberate mobile transformation: stack, scroll, or compact—not accidental clipping.
- A hero demo should have a meaningful static frame before JavaScript starts.
- Text-only links and icon-only controls need distinguishable names and visible focus.
