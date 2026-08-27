# Frontend audit checklist

Use only the rows relevant to the surface. Mark each item as observed, not observed, or needs verification.

## Structure

- [ ] The page has one clear primary task or CTA.
- [ ] The h1 states the product or user outcome.
- [ ] Sections follow a comprehensible order without relying on animation.
- [ ] Navigation labels match visible section names and anchors.
- [ ] Repeated items use consistent structure and state labels.

## Visual language

- [ ] Content frame and gutters are consistent.
- [ ] Heading, body, label, and mono roles are distinguishable.
- [ ] Surface changes communicate hierarchy rather than decoration only.
- [ ] Borders, radii, shadows, and icon strokes form a coherent family.
- [ ] Long CJK and technical strings wrap without clipping.

## Interaction

- [ ] Primary actions have clear hover, focus, disabled, and success/error states.
- [ ] Tabs expose selected state and a matching panel.
- [ ] Autoplay has pause/replay or an equivalent user control.
- [ ] Menus can open, close, and be reached from the keyboard.
- [ ] Empty and failure states explain what the user can do next.

## Responsive and accessibility

- [ ] No horizontal scroll at the narrow viewport.
- [ ] Fixed or sticky UI does not cover content or anchors.
- [ ] Touch targets remain usable.
- [ ] Regions, headings, controls, and links have meaningful names.
- [ ] Focus is visible and motion can be reduced.
- [ ] Contrast and non-color cues are sufficient for status differences.

## Trust and claims

- [ ] Numeric claims identify a source, sample, or test condition.
- [ ] Beta, planned, unavailable, and shipped states are not conflated.
- [ ] Data sent to third parties and retention behavior are explainable.
- [ ] Explicit non-features prevent over-reading the promise.
