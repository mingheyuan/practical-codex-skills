# Design system reference

This reference captures the reusable design language observed in the Saymore reference page. Treat it as a starting point, not a brand clone. Adapt the values to the product and preserve the roles.

## Layout

- Use a centered content frame around `1180px` on wide screens, with generous side gutters.
- Build the page from editorial chapters. A chapter may fill roughly one viewport when the content benefits from deliberate pacing, but content height must win on short screens.
- Use two-column compositions for claim plus explanation, and ruled grids for comparisons, platform coverage, metrics, and release history.
- Alternate white, near-white, ink, and primary-color surfaces to signal a change in product idea.
- Use a sticky or compact navigation after the reader leaves the hero. Collapse it to a labeled menu on narrow screens.

## Role-based tokens

```css
:root {
  --canvas: #ffffff;
  --surface: #f5f5f3;
  --surface-raised: #fafaf9;
  --ink: #141414;
  --text: #454542;
  --muted: #686863;
  --border: #dededb;
  --primary: #2864e4;
  --primary-soft: #eef3ff;
  --success: #27885a;
  --success-soft: #eaf7ee;
}
```

Keep tokens semantic. A card should ask for `--surface-raised`, not a hard-coded gray chosen in isolation.

## Typography

- Use a high-quality sans-serif with a CJK fallback chain such as `GeistSans, PingFang SC, Microsoft YaHei, sans-serif`.
- Use a mono stack for technical labels and data, such as `GeistMono, ui-monospace, SFMono-Regular, monospace`.
- Wide-screen display headings can sit around `44px / 1.12` with tight tracking; body copy around `16px / 1.6`; controls around `13–14px`.
- Use `clamp()` or a responsive type scale. Do not ship a fixed desktop heading size that causes Chinese copy to overflow on mobile.
- Keep heading line lengths short enough to scan. A strong two-line outcome statement is usually better than a long paragraph-shaped heading.

## Component recipes

### Product-shaped hero

Build a contained app shell with a browser/desktop chrome, realistic empty space, one active workflow, and an audio or input affordance. Keep the UI legible at its actual rendered size. The surrounding marketing headline should explain the outcome; the shell should demonstrate it.

### Evidence band

Pair a statement with a small metric or status grid. State the measurement boundary and the publication condition instead of showing a precision-looking number without a sample definition.

### Transformation comparison

Show source text beside the conservative result, with a short annotation explaining exactly what changed and what was intentionally preserved.

### Trust/data-flow section

Use a dark surface, three or four equal-weight steps, subtle rules, and a final “does not do” statement. The sequence should be readable without hover.

### Plan or deployment cards

Compare modes by ownership and behavior (local, BYOK, hosted), not only by price. Add a status label such as Beta, configurable, or planned, and make the difference actionable with a real link.

## Motion

- Use short ease-out transitions for tabs, controls, and status changes.
- Keep the hero demo deterministic and restartable. Avoid animation that is required to reveal copy.
- Respect `prefers-reduced-motion: reduce` by freezing on a useful frame and removing autoplay or large transforms.
