# Interaction Patterns

Use interaction to make complex content easier to scan.

Interaction is optional. Add it only when it supports one of these jobs:

- Compare alternatives.
- Reveal secondary detail.
- Navigate a long artifact.
- Filter repeated items.
- Update a detail panel from a map/list.
- Keep the main scan path concise.

## Good Defaults

- Scroll progress bar for long pages.
- Active nav state based on visible section.
- Smooth internal anchor navigation.
- Accordions for secondary details.
- Tabs for mutually exclusive views.
- Clickable maps/cards when one detail panel updates from several options.
- Filters for repeated cards or tracks.

For long presentations, use at least navigation plus progress. For short presentations, avoid unnecessary controls.

## JavaScript Rules

- Keep JavaScript small and local to the page.
- Use `data-*` attributes for content-driven controls.
- Preserve accessibility: `aria-expanded`, `aria-selected`, `aria-controls`, `aria-pressed`, and focus styles.
- Ensure default content is visible without requiring a click.
- Do not add fake controls that do nothing.
- Do not store critical presentation content only in JavaScript. The page should still contain meaningful default HTML.
- Avoid dependencies unless the user asks for a framework or library.
- Keep motion subtle and respect `prefers-reduced-motion` when adding animation.

## Accessibility Rules

- Buttons must be real `<button>` elements.
- Links must navigate; buttons must change UI state or trigger an action.
- Interactive controls need visible focus states.
- Tab panels should use `role="tablist"`, `role="tab"`, `role="tabpanel"` when practical.
- Accordions should update `aria-expanded`.
- Images need meaningful `alt` text unless decorative.

## Interaction Checklist

For each interaction, verify:

- There is a default active state.
- Keyboard users can activate it.
- State changes are reflected visually.
- The layout does not jump unexpectedly.
- The content still makes sense if JavaScript fails.
- The interaction reduces complexity instead of hiding necessary content.
